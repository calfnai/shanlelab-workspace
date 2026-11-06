"""Refresh the curated, portable workbench from original project assets. Originals stay untouched."""
from pathlib import Path
from PIL import Image, ImageOps
import json, shutil, hashlib, re
ROOT=Path(__file__).resolve().parent
SITE=ROOT/'site'; SITE.mkdir(exist_ok=True)
OVER=Path('/Users/ziqing/Documents/codexprojects/shanleoverseas/outputs')
SHOP=Path('/Users/ziqing/Documents/ChatGPT/店铺设计/projects')
NIKO=SHOP/'niko-christmas-20261029'
PACK=Path('/Users/ziqing/Documents/codexprojects/shanlelab-packingbag')
manifest=[]
def copy(p, destination=None):
    p=Path(p); assert p.is_file(), p
    relative=Path(destination or ('media/'+hashlib.sha256(str(p).encode()).hexdigest()[:10]+p.suffix.lower()))
    dest=SITE/relative; dest.parent.mkdir(parents=True,exist_ok=True)
    if not dest.exists() or dest.stat().st_mtime<p.stat().st_mtime: shutil.copy2(p,dest)
    manifest.append({'source':str(p),'file':str(relative)})
    return relative.as_posix()
def image(p,label,status='历史版本',note=''):
    file=copy(p); thumb='thumbs/'+Path(file).stem+'.webp'; target=SITE/thumb;target.parent.mkdir(exist_ok=True)
    if not target.exists():
        with Image.open(p) as im:
            im=ImageOps.exif_transpose(im).convert('RGB');im.thumbnail((1000,760));im.save(target,'WEBP',quality=83)
    return dict(file=file,thumb=thumb,label=label,status=status,note=note)
def pics(folder,label,status='历史版本',note=''):
    return [image(p,label+' · '+p.stem,status,note) for p in sorted(folder.glob('*.png')) if not any(x in p.name.lower() for x in ['reference','thumbnail','source','mask','generated','page','original'])]
def project(id,title,en,desc,cid,note,items,links=[]):
    assert items,title
    return dict(id=id,title=title,en=en,description=desc,conversation=cid,note=note,items=items,links=links)
projects=[]
folder=OVER/'popsticker-mlbb-recharge-20261104'
files=sorted(folder.glob('PopSticker-*.png'),key=lambda p:int(re.search(r'-v(\d+)',p.name)[1]),reverse=True)
projects.append(project('mlbb-retail','MLBB 联名售卖款','01 / COLLABORATION','表情包贴纸、包装内卡与充值兑奖玩法。','a680e3e8','v15 为当前找到的玩法图稿；价格与兑奖渠道请回原对话核对。',[image(p,p.stem,'当前图稿' if '-v15' in p.stem else '历史版本') for p in files]))
items=[]
for v in [3,2,1]:
    items+=pics(OVER/f'mct-c-refinement-v0{v}',f'C 款修订 v0{v}','近期修订' if v==3 else '历史版本','平面图、材质效果图属于不同审阅线；不代表生产定稿。')
items+=pics(OVER/'mct-three-directions-review','A/B/C 三方向')
items += [image(p,'四方向品牌修订 · '+p.stem) for p in sorted((OVER/'mlbb-partner-review-four-concepts/revised-branding').glob('*.png'))]
items+=pics(OVER/'mct-official-only-20261104','早期官方素材方向')
# The user explicitly selected the original C concept on 2026-11-06.
selected=image(OVER/'mct-three-directions-review/C-MVP-Savage.png','C — MVP + SAVAGE · 已选定使用版','已选定','用户于 2026-11-06 明确选择；后续 C 修订并未替代此选择。')
items=[selected]+[i for i in items if i['file']!=selected['file']]
projects.append(project('mlbb-gift','MLBB 赛事赠送款','02 / EVENT GIFT','MCT 赛事包 · 已选定 C 款与邮件阶段成果。','d5ba0668','当前采用 C — MVP + SAVAGE 原版。其他方向及 C 款修订保留为其他版本；用户选款与合作方批准分别记录。',items,[dict(label='A/B/C 平面矢量预览',href=copy(OVER/'mct-vector-abc/preview-standalone.html','documents/mct-vector.html'))]))
projects[-1]['milestone']={
 'title':'C — MVP + SAVAGE', 'status':'已选定使用', 'date':'2026.11.06',
 'summary':'深蓝赛事包，SEA 主贴 + MVP + SAVAGE。以用户本次确认的这张原图作为当前工作版本。',
 'next':'接续事项：核对官方标志生产原稿、补充平面图与凹凸说明，等待书面审阅意见。',
 'email':{'title':'设计与用途审批申请 · 已发送阶段稿','status':'已发送 · 待书面审阅','date':'2026.11.05',
 'summary':'设计概念、官方素材与二创边界、赛事包非售卖赠品及社媒用途申请。',
 'href':'documents/mct-email-sent.html', 'latestHref':'documents/mct-email-revised.html',
 'latestTitle':'后续完整邮件稿 · 含分发数量（草稿）'}
}

items=[]
for v in [3,2,1]:
    f=OVER/f'booth-mlbb-20261105-v0{v}'
    items+=pics(f,f'11.05 · v0{v}','当前方向' if v==3 else '历史版本','空间概念图；v03 按主墙尺寸重新校正比例，施工以尺寸图为准。')
for v in [13,11]:items+=pics(SHOP/f'booth-3x3-MLBB-TH-v{v}'/'review',f'早期展位 v{v}')
projects.append(project('mlbb-booth','MLBB 赛事展位','03 / BOOTH','3 × 3 米相邻双开口 · 展示、体验与储物。','d1139134','近期 v01–v03 有渲染与平面图；尚未找到与这版设计对应的可旋转 3D。',items))
# Exactly two current display schemes. Rejected tabletop v01-v06 are excluded.
model=NIKO/'comparison-v08/site'
for p in model.rglob('*'):
    if p.is_file() and not any(part.startswith('.') for part in p.relative_to(model).parts):
        copy(p,'demos/niko-comparison/'+p.relative_to(model).as_posix())
items=[]
for scheme,label in [('pipe','水管吊海洋板'),('paper','纯纸板')]:
    for zone,zlabel in [('island','中岛'),('column','柱子区'),('back','中岛背面'),('overall','整体')]:
        p=model/'preview'/f'{scheme}-{zone}.png'
        if p.exists():items.append(image(p,f'{label} · {zlabel}','当前对比','同一底座 200×100×67cm；柱子每面125cm。'))
if not items:items=[image(model/'assets/front.jpg','联名区正面原稿','设计原稿')]
links=[]
for p in sorted((NIKO/'output').glob('*v04*')):
    if p.suffix=='.pdf':links.append(dict(label='圣诞提案 v04 · PDF',href=copy(p,'documents/'+p.name)))
projects.append(project('niko','niko and… 展位','04 / DISPLAY','水管吊海洋板 / 纯纸板 · 中岛与柱子区左右对照。','ea860ae7','中岛底座 200×100×67cm，沿用叉车板；柱子每面125cm。先看效果图，再看三维模型，最后看细节和参考。',items,links))
projects[-1]['comparison']={'root':'demos/niko-comparison/','schemes':[
 {'id':'pipe','title':'水管吊海洋板','tag':'A / PIPE + MARINE PLYWOOD','summary':'水管支架从上方两点吊挂海洋板；中岛与柱面配套。'},
 {'id':'paper','title':'纯纸板','tag':'B / CORRUGATED BOARD','summary':'EBUILD 厚纸板立板与阶梯结构；中岛与柱面配套。'}
], 'withdrawn':'用户截图指定的被否决或严重错误版本已退出成果展示。原始参考资料保留。',
 'dimensions':{'base_cm':[200,100,67],'column_face_cm':125,'person_cm':170},
 'details':[image(model/'assets/front.jpg','联名及首发区 · 正面原稿','设计原稿'),image(model/'assets/back.jpg','常规商品区 · 背面原稿','设计原稿')],
 'references':[]}
for file,label in [('pipe-plywood-reference.png','水管与海洋板 · 结构参考'),('v03-user-column-zones.png','柱子区 · 原始分区参考')]:
    p=SHOP/'island-column-20261023/assets'/file
    if p.exists():projects[-1]['comparison']['references'].append(image(p,label,'参考资料','保留原资料；图中的旧尺寸不替代本次确认尺寸。'))
items=[]
for v in [11,10,9,8,7,3]:
    items+=pics(PACK/f'assets/scenes/v{v:02d}',f'陈列评审 v{v:02d}','当前陈列评审' if v==11 else '陈列版本','现场陈列效果稿；现场尺寸与承重仍需核对。')
for v in [7,6,5,4,3]:
    items+=pics(PACK/f'assets/renders/v{v:02d}',f'装袋方向 v{v:02d}','近期装袋评审' if v==7 else '历史装袋版本','装袋效果与现场尺寸核对分别推进，不视作生产定稿。')
items.append(image(PACK/'assets/renders/empty-neutral-zip-v02.png','早期本白拉链 v02','早期袋型候选','后续装袋及陈列请优先看当前评审。'))
items+=pics(PACK/'assets/renders','早期装袋','历史概念','旧装袋比例未验证；旧三档尺寸已撤回。')
seen=set()
items=[i for i in items if not (i['file'] in seen or seen.add(i['file']))]
projects.append(project('pouch','透明外袋与店铺陈列','05 / PACKAGING','C 组 v11、暖木展区、Sunday Home 与各轮装袋评审。','cd8b04f8','当前工作接续正式目录对话。最新为 C 组三处陈列评审，暖木展区与 Sunday Home 另有近期图组；均保留现场尺寸核对与生产确认的边界。',items,[dict(label='完整包装与陈列评审页',href='https://calfnai.github.io/shanlelab-packaging/'),dict(label='C 组 · 相机／文具／礼盒',href='https://calfnai.github.io/shanlelab-packaging/#stores')]))
# Related niko collaboration booklet, copied with its actual assets.
book=NIKO/'concept-two-pages-v01'
if book.exists():
    for p in book.rglob('*'):
        if p.is_file() and p.suffix.lower() in ['.html','.png','.jpg','.jpeg','.pdf','.webp']:
            copy(p,'documents/niko-concept/'+p.relative_to(book).as_posix())
    for p in (NIKO/'product-copy-v01').glob('*.jpg'):
        copy(p,'documents/product-copy-v01/'+p.name)
    projects[3]['links'].append(dict(label='联名创作说明 · 两页',href='documents/niko-concept/创作说明.html'))
from html import escape
for source,destination,title,status in [
 ('email.txt','mct-email-sent.html','设计与用途审批申请 · 已发送正文','2026-11-05 · 已从 Gmail 已发送核对；附件为当时截图，尚未核实补发原图。'),
 ('email-complete-revised.txt','mct-email-revised.html','后续完整邮件稿 · 分发安排','本地阶段草稿；与已发送正文不同。800 stickers 与每日两组各50 sets 的单位和总量应在发送前统一核对。')]:
 body=(OVER/'mct-email-review-20261105'/source).read_text()
 body='\n'.join(line for line in body.splitlines() if not line.startswith('To:'))
 dest=SITE/'documents'/destination
 dest.write_text('<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+'</title><style>body{max-width:850px;margin:50px auto;padding:0 25px;background:#f5f4ef;color:#283c35;font:15px/1.85 system-ui}h1{font-size:28px}aside{padding:16px;background:#e6eadd;font-size:12px}pre{white-space:pre-wrap;font:14px/1.9 system-ui;background:white;padding:30px;border:1px solid #dedfd6}</style><a href="../index.html#mlbb-gift">← 返回赛事赠送款</a><h1>'+escape(title)+'</h1><aside>'+escape(status)+'</aside><pre>'+escape(body)+'</pre></html>')
conversation_names={'mlbb-retail':'MLBB表情包充值贴纸','mlbb-gift':'MLBB赛事包 MCT赛事Logo贴纸','mlbb-booth':'MLBB展位重设计','niko':'niko and 设计最终版回顾','pouch':'透明软塑料包装袋设计正式目录'}
for p in projects:p['conversationName']=conversation_names[p['id']]
(SITE/'data.js').write_text('window.WORKSPACE='+json.dumps(dict(updated='2026-11-06',projects=projects),ensure_ascii=False)+';',encoding='utf8')
(ROOT/'local-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(f'{len(projects)} projects; {sum(len(p["items"]) for p in projects)} images; {len(manifest)} files')
