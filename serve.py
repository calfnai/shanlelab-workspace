"""Single canonical preview. Usage: python3 serve.py [start|status|stop]."""
from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import fcntl, os, sys, json, signal, subprocess
ROOT=Path(__file__).resolve().parent
RUNTIME=ROOT/'.runtime';RUNTIME.mkdir(exist_ok=True)
command=sys.argv[1] if len(sys.argv)>1 else 'start'
pidfile=RUNTIME/'server.json'
if command in ('status','stop'):
    if not pidfile.exists():print('Not running');sys.exit(0)
    record=json.loads(pidfile.read_text());pid=record['pid']
    process=subprocess.run(['ps','-p',str(pid),'-o','command='],capture_output=True,text=True).stdout
    if str(ROOT/'serve.py') not in process:print('Recorded process is no longer this preview');sys.exit(1)
    if command=='stop':os.kill(pid,signal.SIGTERM);print('Stopped preview')
    else:print(record)
    sys.exit(0)
if command!='start':raise SystemExit('Use start, status or stop')
lock=(RUNTIME/'preview.lock').open('w')
try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
except BlockingIOError:raise SystemExit('Preview already running; use python3 serve.py status')
try:server=ThreadingHTTPServer(('127.0.0.1',18916),partial(SimpleHTTPRequestHandler,directory=str(ROOT/'site')))
except OSError as exc:raise SystemExit(f'Cannot start canonical preview on 18916: {exc}')
pidfile.write_text(json.dumps(dict(pid=os.getpid(),url='http://127.0.0.1:18916/',root=str(ROOT/'site'))))
print('http://127.0.0.1:18916/',flush=True)
server.serve_forever()
