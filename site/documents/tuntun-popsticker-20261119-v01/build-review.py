"""Build the single current TUNTUN review. Withdrawn images stay in history only."""
from pathlib import Path
from html import escape
import json
R = Path(__file__).resolve().parent
refs = json.loads((R/'pet-reference-index.json').read_text())['references']
def fig(file, title, caption, cls=''):
    url = file + ('?v=20261119-brand-shape' if file in ('08-mood-trio-063.png', '09-arcade-collage-052.png') else '')
    return f'<figure class="{cls}"><a href="{url}" target="_blank" rel="noopener"><img src="{url}" alt="{escape(title)}" loading="lazy"></a><figcaption><strong>{escape(title)}</strong><span>{escape(caption)}</span></figcaption></figure>'
page = r'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>TUNTUN · 三枚一体贴与定稿产品 · v07</title><style>
:root{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:#16356b;background:#f6f3eb;line-height:1.65}*{box-sizing:border-box}body{margin:0}header,main,footer{max-width:1536px;margin:auto;padding:28px 4vw}header{padding-top:48px}h1{font-size:clamp(32px,5.5vw,68px);line-height:1.12;margin:15px 0 22px;letter-spacing:-1px}h2{font-size:clamp(23px,3vw,34px);line-height:1.3;margin:0 0 12px}h3{font-size:22px;margin:8px 0 12px}small,.eyebrow{font-size:12px;letter-spacing:2px;color:#a85722}p{color:#5c6a7c;max-width:1000px;margin:10px 0 22px}a{color:inherit}nav{display:flex;gap:9px;flex-wrap:wrap;margin:22px 0}nav a,.switch button{border:1px solid #1b448a;border-radius:24px;padding:8px 17px;text-decoration:none;background:transparent;color:#173c7c;font:inherit;font-size:14px;cursor:pointer}nav a:first-child,.switch button[aria-pressed=true]{background:#173c7c;color:white}.status{display:inline-block;background:#e0edde;color:#3a634a;border-radius:5px;padding:5px 11px;font-size:13px}.note{background:#fff0cf;border-left:4px solid #ecae38;padding:13px 20px;color:#4e5260;border-radius:4px;margin:20px 0}.lead{font-size:17px}section{margin:35px 0 70px;scroll-margin-top:22px}figure{margin:0}figure>a{display:block}img{width:100%;height:auto;display:block;background:#fff;border-radius:10px}figcaption{padding:11px 1px 20px;font-size:13px;color:#5a6c83}figcaption strong{display:block;color:#233f69;font-size:15px;margin-bottom:2px}figcaption span{display:block}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px}.pair img{aspect-ratio:3/2;object-fit:contain}.ref-pair{display:grid;grid-template-columns:1.5fr 1fr;gap:24px;align-items:center}.ref-pair img{aspect-ratio:3/2;object-fit:contain}.ref-pair .outline img{aspect-ratio:1.4;max-width:409px;margin:auto}.directions{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:28px}.directions img{aspect-ratio:1.4;object-fit:contain}.ref-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.ref-grid img{aspect-ratio:1.4;object-fit:contain}.switch{display:flex;gap:10px;margin:16px 0}.scene{aspect-ratio:4/3;object-fit:contain}.retained{max-width:1100px}details{background:#edece5;padding:20px;border-radius:10px;margin:20px 0}summary{cursor:pointer;font-weight:650}details[open] summary{margin-bottom:20px}footer{border-top:1px solid #cbd0d7;font-size:13px;color:#607087;padding-bottom:45px}footer p{margin-bottom:12px}.source-link{font-size:13px}.smallprint{font-size:13px}.compare-label{font-size:13px;color:#a85722;margin-bottom:8px}@media(max-width:760px){header,main,footer{padding-left:18px;padding-right:18px}.pair,.ref-pair,.directions{grid-template-columns:1fr}.ref-grid{grid-template-columns:1fr 1fr}section{margin-bottom:48px}.lead{font-size:15px}}
</style></head><body><header><small>SHANLE LAB × TUNTUN · V07 / 2026.11.21</small><h1>两款定稿，<br>快乐随身。</h1><p class="lead">两款产品已于 2026.11.19 获用户确认定稿。本轮按反馈将零食组合修订为三枚一体贴，角色、食物与短语共用连续外轮廓；手机、包包及空间图继续保留。</p><span class="status">两款产品 · 用户确认定稿</span><nav aria-label="当前评审"><a href="#products">两款定稿产品</a><a href="#three-originals">三枚一体贴</a><a href="#applications">手机与包包应用</a><a href="#niko">最新现场中岛</a><a href="#booth">故事展位</a><a href="#packaging">真实包装</a><a href="#retained">保留的 04</a></nav></header><main><section id="products"><span class="eyebrow">01 / USER-CONFIRMED PRODUCTS</span><h2>两款产品，确认定稿</h2><div class="directions"><div><h3>B · 今天是什么表情？</h3><p>参考 063 的表情、文字与拼布关系。三枚独立头像，用 YUM / ZZZ / YAY 区分状态。</p>'''
page += fig('08-mood-trio-063.png','B · TUNTUN MOOD CLUB','2026.11.19 用户确认定稿 · 本轮保留原图不改。')
page += '</div><div><h3>C · 快乐加一格</h3><p>参考 052 的窗口拼贴与角色互动。披萨、椰子、奖励星与短语形成街机式小场景。</p>'
page += fig('09-arcade-collage-052.png','C · TUNTUN PLAY CLUB','2026.11.19 用户确认定稿 · 本轮保留原图不改。')
page += '</div></div><details><summary>对照用户指定的 063 / 052 原款</summary><div class="pair">'
page += fig('source/pet-references/pet-063.jpg','063 · 小困喵','参考组合方式、表情与文字的关系。')
page += fig('source/pet-references/pet-052.jpg','052 · 街机酷喵','参考层叠窗口、色块与角色互动。')
page += '</div></details></section><section id="three-originals"><span class="eyebrow">02 / THREE INTEGRATED STICKERS</span><h2>三个零食伙伴，每枚连成一体</h2><p>一包仅三枚：披萨角色＋YUM!、冰淇淋角色＋SWEET!、椰子角色＋CHILL!。每组共用一块贴片和连续外轮廓，收拢细碎边缘，重新留出包装间距。</p>'
page += fig('16-three-piece-package.png','TUNTUN SNACK CLUB · 3 PIECES','修订候选 · 包装内仅三枚，角色与对应短语连为一体。')
page += fig('17-three-integrated-stickers.png','三枚一体贴展开','披萨＋YUM! / 冰淇淋＋SWEET! / 椰子＋CHILL! · 每枚共用一个连续外轮廓。')
page += '<details><summary>本轮提供的三张角色原图</summary><div class="ref-grid">'
page += fig('source/three-originals-20261120/pizza-original.jpg','披萨原图','本轮用户提供，源文件原样保存。')
page += fig('source/three-originals-20261120/pink-icecream-original.jpg','冰淇淋原图','本轮用户提供，源文件原样保存。')
page += fig('source/three-originals-20261120/coconut-original.jpg','椰子原图','本轮用户提供，源文件原样保存。')
page += '</div></details></section>'
page += '<section id="applications"><span class="eyebrow">03 / EVERYDAY APPLICATIONS</span><h2>拿在手里，贴进日常</h2><p>表情款用在手机，街机款在包包上组成一组小场景。以成人手掌、完整手机和包身作参照，贴纸保持日常小物的大小。</p><div class="pair">'
page += fig('12-phone-application.png','手机 · 今天选 YAY!','手持定稿包装，表情贴用于手机壳 · 新增应用场景，待评审。')
page += fig('13-bag-application.png','包包 · 快乐加一格','披萨、椰子、奖励星与短语贴组成随身小剧场 · 新增应用场景，待评审。')
page += '</div></section>'
page += r'''<section id="niko"><span class="eyebrow">04 / SAME SITE, SMALL REAL PRODUCTS</span><h2>大画面负责吸引，小商品保持售卖尺度</h2><p>以最新现场照为基准，保留四包商品在背板中的大小与挂位，以及木托盘、后方挂货、前排卡套和护照夹。立牌展示故事与应用，销售包装不再排成大号方袋。</p><div class="switch" role="group" aria-label="同画幅现场对比"><button type="button" data-photo="10-niko-latest-photo-scale.png" data-caption="修订候选 · 四包小商品、四张应用立牌与原有生活周边。" aria-pressed="true">替换后</button><button type="button" data-photo="source/niko-latest-site-20261119.jpg" data-caption="用户最新现场原照片 · 本轮空间参照。" aria-pressed="false">最新现场原照</button></div><figure><a id="scene-link" href="10-niko-latest-photo-scale.png" target="_blank" rel="noopener"><img class="scene" id="scene-photo" src="10-niko-latest-photo-scale.png" alt="最新 niko 现场的 TUNTUN 陈列修订候选"></a><figcaption id="scene-caption">修订候选 · 四包小商品、四张应用立牌与原有生活周边。</figcaption></figure><p class="smallprint">这是现场替换视觉稿；保留照片中的尺度关系，不据此反推家具实测尺寸。</p></section><section id="booth"><span class="eyebrow">05 / A LITTLE CHARACTER WORLD</span><h2>快乐营业中：看故事、选款、试贴</h2><p>借鉴 Meeko 手册第 8、17 页的连续日常故事，以及同一图案在不同物件上的呼应。沿用纸中岛构造，增加漫画层板、三组挂货、表情窗口与试贴台；手机、护照夹和包装按小实物呈现。</p>'''
page += fig('11-story-shop-booth.png','TUNTUN · 快乐营业中','AI 空间候选 · 放大角色属于印刷画面；售卖包装和应用样品为小实物。')
page += '<p class="smallprint">按约 3m × 3m 的概念占地探索，未取得场地方实测图。中岛构造延续既有 MLBB 纸中岛，新增墙板、层板与柜体仍需结构落图。</p></section><section id="packaging"><span class="eyebrow">06 / REAL PACKAGE FIRST</span><h2>包装结构回到实拍，撤回错误的平面比例稿</h2><p>真实包装包含扁圆横向内卡、顶端挂孔区、两侧印刷弧线，以及浅透明 PET 罩和凸边。不能将一张平面椭圆当作整个实体包装，也不能用普通椭圆替代固定轮廓。</p><div class="ref-pair">'
page += fig('source/pet-references/pet-063-actual-front.jpg','现有 063 · 实体包装正面照片','实拍是包装结构参照；不是本轮新产品。')
page += fig('source/pet-references/approved-popsticker-outline.png','固定品牌轮廓原图','保持原图整体比例及两侧弧线；生成图不能替代源稿。','outline')
page += '</div><details><summary>本轮使用的原始品牌标识</summary>'
page += fig('source/brand/brand-assets-reference.svg','SHANLE LAB / POP STICKER 原资产','完整兔耳与下方横排英文；P 内星形与 O 内双弧线均以原资产为准。')
page += '</details><div>'
page += '</div><div class="note">07 四枚肖像比例稿已因外形与包装表现错误撤回。目录整版宽记为 147mm，高度存在 100 / 105mm 两种记录，待实物核验；本轮不再用“标注尺寸”证明生成图正确。</div></section><section id="retained"><span class="eyebrow">07 / RETAINED DIRECTION</span><h2>04 · 三枚零食小剧场，保留继续比较</h2><p>用户反馈“还行”：记录为方向暂留，原图不改，不扩大为生产或整体包装批准。</p><div class="retained">'
page += fig('04-products-multipatch.png','A · TUNTUN SNACK CLUB','三枚独立角色与零食小剧场 · 本轮保持原图。')
page += '</div></section><section id="references"><details><summary>其余现有萌宠款与实拍参考</summary><div class="ref-grid">'
for r in refs:
    if r['file'].endswith(('pet-063.jpg','pet-052.jpg')):continue
    page += fig(r['file'],r['name'],r['sku']+' · '+r['series'])
page += '</div><div class="pair">'
page += fig('source/pet-references/pet-real-multipack.jpg','现有多枚组合实拍','薄层贴片、内卡和透明罩。')
page += fig('source/pet-references/pet-real-phone-scale.jpg','现有手机应用实拍','观察小贴片与手机的实际关系。')
page += r'''</div></details></section></main><footer><p>两款产品定稿原文件保持不变。三枚一体贴修订图与生活应用使用内置 imagegen 制作，分别作为候选待评审。Meeko 手册仅在本地作为参考，未随页面公开。</p><p>v06 九枚拆分方案已因数量、空间和细碎切边问题撤回。v01 三图、v02 的 05 / 06 / 07 同样不再展示，历史原文件保留。<a href="README.md">状态与提示词索引</a> · <a href="review-state.json">版本状态</a> · <a href="product-finalization.json">两款产品定稿记录</a></p></footer><script>
document.querySelectorAll('[data-photo]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-photo]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));document.getElementById('scene-photo').src=button.dataset.photo;document.getElementById('scene-photo').alt=button.dataset.caption;document.getElementById('scene-link').href=button.dataset.photo;document.getElementById('scene-caption').textContent=button.dataset.caption;}));
</script></body></html>'''
(R/'index.html').write_text(page)
print('Built single v07 review; three integrated stickers replace the withdrawn nine-piece assortment; existing finals preserved.')
