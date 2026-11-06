"""Shared project records, optimistic revisions and one atomic index writer."""
from pathlib import Path
from datetime import date
import argparse, fcntl, hashlib, json, os, re, tempfile

ROOT = Path(__file__).resolve().parent
RECORDS = ROOT / 'projects'

def lock():
    (ROOT / '.runtime').mkdir(exist_ok=True)
    handle = (ROOT / '.runtime/workspace.lock').open('a')
    fcntl.flock(handle, fcntl.LOCK_EX)
    return handle

def atomic(path, content):
    fd, tmp = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as out:
            out.write(content)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)

def record_path(key):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', key):
        raise ValueError('Use a stable lowercase project id.')
    return RECORDS / (key + '.json')

def revision(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None

def validate(project):
    record_path(project['id'])
    for key in ('title', 'en', 'description', 'note', 'conversation', 'conversationName', 'items', 'links'):
        if key not in project:raise ValueError('Missing project field: ' + key)
    if not project['items']:raise ValueError('A project needs at least one real image.')
    for item in project['items']:
        for key in ('file', 'thumb'):
            path = (ROOT / 'site' / item[key]).resolve()
            if not path.is_relative_to(ROOT / 'site') or not path.is_file():
                raise ValueError('Missing or nonportable asset: ' + item[key])

def assemble():
    projects = [json.loads(p.read_text()) for p in sorted(RECORDS.glob('*.json'))]
    for project in projects:validate(project)
    projects.sort(key=lambda p:p['en'])
    data = {'updated':date.today().isoformat(), 'projects':projects}
    atomic(ROOT / 'site/data.js', 'window.WORKSPACE=' + json.dumps(data, ensure_ascii=False) + ';')
    print(f'Built {len(projects)} shared project records.')

def put(envelope):
    project = envelope['project']
    validate(project)
    path = record_path(project['id'])
    if 'revision' not in envelope or envelope['revision'] != revision(path):
        raise ValueError('Revision conflict: read the latest project and merge your changes before retrying.')
    atomic(path, json.dumps(project, ensure_ascii=False, indent=2) + '\n')
    assemble()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    get = sub.add_parser('get');get.add_argument('id')
    write = sub.add_parser('put');write.add_argument('file', type=Path)
    sub.add_parser('build')
    args = parser.parse_args()
    with lock():
        if args.command == 'list':
            for path in sorted(RECORDS.glob('*.json')):
                p = json.loads(path.read_text());print(p['id'] + '\t' + p['title'])
        elif args.command == 'get':
            path = record_path(args.id)
            print(json.dumps({'revision':revision(path), 'project':json.loads(path.read_text())}, ensure_ascii=False, indent=2))
        elif args.command == 'put':put(json.loads(args.file.read_text()))
        else:assemble()

if __name__ == '__main__':main()
