"""GitHub API helper. Uses existing gh credentials without printing or persisting them."""
import subprocess,urllib.request,urllib.error,json,sys,time

def api(path,method='GET',payload=None):
    auth=subprocess.run(['gh','auth','token','--hostname','github.com'],capture_output=True,text=True,check=True).stdout.strip()
    data=json.dumps(payload).encode() if payload is not None else None
    request=urllib.request.Request('https://api.github.com'+path,data=data,method=method,headers={'Authorization':'Bearer '+auth,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'shanlelab-workspace','Content-Type':'application/json'})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request,timeout=25) as r:return json.load(r) if r.status!=204 else {}
        except urllib.error.HTTPError:raise
        except Exception:
            if attempt==3:raise
            time.sleep(1)
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='create':
        try:r=api('/repos/calfnai/shanlelab-workspace')
        except urllib.error.HTTPError as e:
            if e.code!=404:raise
            r=api('/user/repos','POST',dict(name='shanlelab-workspace',description='SHANLE LAB recent workspace: selected milestones, visual versions, 3D demos and conversation links.',private=False,auto_init=False))
        print(r['html_url'])
    elif mode=='pages':
        try:r=api('/repos/calfnai/shanlelab-workspace/pages')
        except urllib.error.HTTPError as e:
            if e.code!=404:raise
            r=api('/repos/calfnai/shanlelab-workspace/pages','POST',dict(build_type='workflow'))
        print(json.dumps({k:r.get(k) for k in ['html_url','status','build_type']}))
    elif mode=='runs':
        r=api('/repos/calfnai/shanlelab-workspace/actions/runs?per_page=2')
        print(json.dumps([dict(id=x['id'],status=x['status'],conclusion=x['conclusion'],url=x['html_url']) for x in r['workflow_runs']]))
