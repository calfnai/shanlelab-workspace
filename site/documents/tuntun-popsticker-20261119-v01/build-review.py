"""Keep one current review page, with real pet references and withdrawn v01 excluded."""
from pathlib import Path
import json
from html import escape

ROOT = Path(__file__).resolve().parent
references = json.loads((ROOT / 'pet-reference-index.json').read_text())['references']
cards = ''.join(f'<figure class="ref"><a href="{escape(r["file"])}" target="_blank" rel="noopener"><img loading="lazy" src="{escape(r["file"])}" alt="{escape(r["name"])}"></a><figcaption><b>{escape(r["name"])}</b><br>{escape(r["sku"])} · {escape(r["series"])}</figcaption></figure>' for r in references)

def figure(path, alt, caption):
    return f'<figure><a href="{path}" target="_blank" rel="noopener"><img src="{path}" alt="{alt}"></a><figcaption>{caption}</figcaption></figure>'

page = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>TUNTUN · 从萌宠款重新做 · v02</title>
<style>
:root{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;color:#173778;background:#f6f3ea;line-height:1.65}*{box-sizing:border-box}body{margin:0}header,main,footer{max-width:1480px;margin:auto;padding:30px 5vw}header{padding-top:45px}small{color:#bc551e;letter-spacing:2px}h1{font-size:clamp(30px,4.6vw,60px);line-height:1.16;margin:12px 0 20px}h2{font-size:27px;line-height:1.35;margin-bottom:10px}p{max-width:1000px;color:#506278}a{color:inherit}nav{display:flex;gap:10px;flex-wrap:wrap}nav a{background:#193f8d;color:white;padding:9px 16px;border-radius:24px;text-decoration:none}section{margin:0 0 55px;scroll-margin-top:24px}figure{margin:0}img{display:block;width:100%;height:auto;border-radius:10px;background:#fff}figure>a{display:block}figcaption{font-size:13px;color:#5c6c80;padding:10px 0}.pair{display:grid;grid-template-columns:1fr 1fr;gap:18px}.pair img{aspect-ratio:4/3;object-fit:contain}.ref-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.ref img{aspect-ratio:1.4;object-fit:contain;background:#fff}.ref figcaption{font-size:12px}.note{padding:17px 22px;border-left:5px solid #fa8427;background:#ffebc6;color:#3e4c60;border-radius:4px}details{padding:23px;border:1px solid #bcc6d5;border-radius:12px}details[open] summary{margin-bottom:25px}summary{cursor:pointer;font-size:18px;font-weight:650}.proof-links{display:flex;gap:20px;flex-wrap:wrap;margin:12px 0}.photos{display:grid;grid-template-columns:repeat(3,1fr);gap:15px}.photos img{aspect-ratio:3/4;object-fit:contain}footer{border-top:1px solid #c9cbd0;font-size:13px;color:#607185;padding-bottom:45px}@media(max-width:760px){header,main,footer{padding-left:18px;padding-right:18px}.pair,.photos{grid-template-columns:1fr}.ref-grid{grid-template-columns:1fr 1fr}h2{font-size:23px}}
</style>
<header><small>SHANLE LAB · TUNTUN · V02 / 2026.11.19</small><h1>TUNTUN 快乐补给站</h1><p>参考现有萌宠款的多枚组合、动作错落、文字与小道具，重新探索「三枚零食小剧场」与「四枚迷你肖像」。上一轮比例与创意已被否决，旧图已撤出当前展示。</p><nav aria-label="当前图稿"><a href="#a">A · 三枚小剧场</a><a href="#b">B · 四枚肖像与比例</a><a href="#niko">暖木中岛</a><a href="#booth">轻型展位</a><a href="#references">萌宠参考</a></nav></header>
<main><section id="a"><h2>A · 一包三枚，角色与零食组成小剧场</h2><p>参考「纸杯萌宠派对」「情绪小绿喵」的组合关系：将角色连同食物拆成独立贴片，以蓝色棋盘、橘黄点缀与 YUM / SLURP / CHILL 形成节奏。</p>'''
page += figure('04-products-multipatch.png','三枚 TUNTUN 皮质贴片、手机与成人手的产品体感稿','AI 体感稿 · 已修正包与手机的相对大小及品牌标识；生成外形细节仍须按标准蒙版落稿。')
page += '''</section><section id="b"><h2>B · 四枚迷你肖像，原图直接做尺度对照</h2><p>参考「萌宠肖像馆」的小尺寸多枚组合，保留四张完整原画。用已确认轮廓蒙版等比排版，以 A6 纸张作稳定参照。</p><div class="note">整版宽 147mm 来自现有目录；高度存在 100 / 105mm 两种记录，尚未实物复核。下图按标准轮廓等比得约 104.6mm。四枚肖像高 32mm、右侧应用高 38mm 均为本轮候选。</div>'''
page += figure('07-four-portraits-scale-proof.png','四枚 TUNTUN 原始肖像与 A6 纸张的固定比例排版','原画与原蒙版直接排版 · 尺度由 SVG 控制；非生产刀模。')
page += '''<div class="proof-links"><a href="07-four-portraits-scale-proof.svg" target="_blank" rel="noopener">打开原始 SVG 比例稿</a><a href="scale-proof.json" target="_blank" rel="noopener">尺寸依据与候选值</a></div></section><section id="niko"><h2>中岛 · 选一份今天的快乐</h2><p>保留现场木托盘与后方常规款挂货；前面用三种零食情绪作入口，手机、帆布包与耳机承担应用展示。销售包装保持手掌级大小。</p><div class="pair">'''
page += figure('source/niko-supplied-site-original.jpg','用户提供的 niko 现场原照片','用户现场原照片')
page += figure('05-niko-snack-island.png','TUNTUN 快乐补给站在同一 niko 中岛的陈列候选','v02 场景候选 · 小包装与小贴片，放大的角色属于印刷主视觉。')
page += '''</div></section><section id="booth"><h2>展位 · 同一套快乐补给站，延续轻型结构</h2><p>沿用背景布与纸中岛，强化角色、情绪与生活物件的联系；保留可用台面，将看主视觉、选角色和看应用连起来。</p>'''
page += figure('06-light-snack-booth.png','TUNTUN 快乐补给站的轻型展位候选','v02 视觉候选 · 现场结构与产品比例仍须按实际平面和实物核验。')
page += '''</section><section id="references"><h2>这轮具体参考了哪些现有萌宠款</h2><p>重点参考花漾萌友、甜杯派对、海岛萌宠、星夜画廊、小困喵的组合与实物呈现；相关 21 款原图保留在下方，点击可放大。</p><div class="photos">'''
page += figure('source/pet-references/pet-real-multipack.jpg','现有纸杯萌宠派对的真实包装照片','现有实拍：多枚组合、浅 PET 罩与薄层皮质贴片')
page += figure('source/pet-references/pet-real-phone-scale.jpg','现有萌宠贴片在真实手机上的应用照片','现有实拍：贴片相对手机的大小')
page += figure('source/pet-references/pet-real-animal-pack.jpg','现有疯狂动物系列的真实包装照片','现有实拍：文字、主角与小配件的层次')
page += f'''</div><details><summary>展开 21 款相关萌宠原图</summary><div class="ref-grid">{cards}</div></details></section></main><footer>A 产品与两张场景由内置 imagegen 生成；B 为原画与标准蒙版的直接排版。新设计均待用户评审，图片中的文字、图案和外形不替代印刷源稿。尺寸记录有冲突的部分已明确保留，未作为实测结论。<br><a href="README.md">本地原稿、提示词与版本状态</a></footer></html>'''
(ROOT / 'index.html').write_text(page)
print(f'Updated one current review page; {len(references)} source pet designs; v01 images excluded.')
