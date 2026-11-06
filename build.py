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
model=NIKO/'tabletop-3d-v07/site'
for p in model.rglob('*'):
    if p.is_file() and not any(part.startswith('.') for part in p.relative_to(model).parts) and p.name!='README.md':copy(p,'demos/niko-v07/'+p.relative_to(model).as_posix())
items=pics(model/'preview','桌面双面 3D v07','当前 3D')
for name,label in [('tabletop-double-sided-v06','七件位置 v06'),('tabletop-double-sided-v05','桌面 v05'),('tabletop-double-sided-v04','桌面 v04'),('tabletop-double-sided-v03','桌面 v03'),('tabletop-ebuild-v02','厚纸板插接 v02'),('tabletop-corrugated-v01','纸板展具 v01')]:
    items+=pics(NIKO/name,label)
for p in sorted((SHOP/'island-column-20261023/outputs/store-renders-v09').glob('*.png')):
    if re.match(r'\d\d-',p.name):items.append(image(p,'旧中岛专柜 v09 · '+p.stem,'旧空间方案','与双面桌面 v07 为不同方案线；反向被拒图未纳入。'))
links=[dict(label='打开可旋转 3D · v07',href='demos/niko-v07/index.html',kind='3d'),dict(label='已有在线 3D',href='https://calfnai.github.io/nikoand-christmas-display/')]
for p in sorted((NIKO/'output').glob('*v04*')):
    if p.suffix == '.pdf':links.append(dict(label='圣诞提案 v04 · '+p.suffix[1:].upper(),href=copy(p,'documents/'+p.name)))
projects.append(project('niko','niko and… 展位','04 / DISPLAY','双面桌面 v07、七件位置图、纸板结构与旧中岛专柜。','ea860ae7','双面桌面 v07 与旧中岛 v09 为不同版本线；当前 3D 未摆入包包和护照夹。',items,links))
items=[image(PACK/'assets/renders/empty-neutral-zip-v02.png','本白拉链 v02','当前候选','尺寸及生产结构尚未定稿。')]
for v in [7,6,5,4,3]:items+=pics(PACK/f'assets/renders/v0{v}',f'装袋方向 v0{v}','历史概念','商品及包装比例未验证；不代表当前尺寸。')
items+=pics(PACK/'assets/renders','早期装袋','历史概念','旧装袋比例未验证；旧三档尺寸已撤回。')
# Deduplicate the current pouch image, which also appears in the older root folder.
seen=set()
items=[i for i in items if not (i['file'] in seen or seen.add(i['file']))]
projects.append(project('pouch','透明外袋','05 / PACKAGING','原始轮廓、本白拉链候选与各轮装袋效果。','11d13a34','仅大、中、小三档通用尺寸；旧尺寸已撤回待核算，历史装袋图仅供回顾。',items,[dict(label='已有在线评审页（可能落后于本机）',href='https://calfnai.github.io/shanlelab-packaging/')]))
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
(SITE/'data.js').write_text('window.WORKSPACE='+json.dumps(dict(updated='2026-11-06',projects=projects),ensure_ascii=False)+';',encoding='utf8')
(ROOT/'local-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(f'{len(projects)} projects; {sum(len(p["items"]) for p in projects)} images; {len(manifest)} files')
