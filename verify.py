"""Validate all curated assets and portable relative HTML/CSS references."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
from html.parser import HTMLParser
import json,re
from PIL import Image
ROOT=Path(__file__).resolve().parent/'site'
data=json.loads((ROOT/'data.js').read_text().removeprefix('window.WORKSPACE=').removesuffix(';'))
checked=set();failures=[]
def check(ref,parent):
    u=urlsplit(ref)
    if not ref or u.scheme or ref.startswith(('#','//')):return
    dest=(parent/unquote(u.path)).resolve()
    if not dest.is_relative_to(ROOT):failures.append('Outside site: '+ref)
    elif not dest.exists():failures.append(str(parent.relative_to(ROOT))+' -> '+ref)
    else:checked.add(dest)
class Links(HTMLParser):
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('src','href') and v:check(v,self.parent)
for p in data['projects']:
    assert len(p['conversation'])==8
    for item in p['items']:
        for key in ['file','thumb']:check(item[key],ROOT)
        with Image.open(ROOT/item['file']) as im:im.verify()
    for link in p['links']:check(link['href'],ROOT)
for page in ROOT.rglob('*.html'):
    parser=Links();parser.parent=page.parent;parser.feed(page.read_text())
    for ref in re.findall(r"(?:from\s*|\.load\()\s*['\"]([^'\"]+)",page.read_text()):check(ref,page.parent)
for js in (ROOT/'demos').rglob('*.js'):
    for ref in re.findall(r"from\s*['\"]([^'\"]+)['\"]",js.read_text()):
        if ref.startswith('.'):check(ref,js.parent)
assert not list(ROOT.rglob('.git')), 'Nested Git metadata must never be served'
assert not failures,'\n'.join(failures)
assert len({p['id'] for p in data['projects']})==len(data['projects'])
gift=next(p for p in data['projects'] if p['id']=='mlbb-gift')
assert gift['items'][0]['status']=='已选定' and gift['items'][0]['label'].startswith('C — MVP + SAVAGE')
assert gift['milestone']['email']['href']=='documents/mct-email-sent.html'
assert 'Production quantity, distribution locations and campaign dates remain to be agreed' in (ROOT/'documents/mct-email-sent.html').read_text()
assert '800 stickers' in (ROOT/'documents/mct-email-revised.html').read_text()
assert 'To:' not in (ROOT/'documents/mct-email-sent.html').read_text()
print(f'PASS: {len(data['projects'])} projects, {sum(len(p["items"]) for p in data["projects"])} full images, {len(checked)} local references')
