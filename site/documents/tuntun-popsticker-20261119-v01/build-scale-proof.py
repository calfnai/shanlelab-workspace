"""Lay out unchanged supplied artwork in a dimensioned native SVG; no raster editing."""
from pathlib import Path
from base64 import b64encode
import json
from PIL import Image

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'source'
REFERENCE = SOURCE / 'pet-references/approved-popsticker-outline.png'

def uri(path):
    return 'data:image/png;base64,' + b64encode(path.read_bytes()).decode()

im = Image.open(REFERENCE).convert('RGB')
points = [(x, y) for y in range(im.height) for x in range(im.width)
          if min(im.getpixel((x, y))) > 240]
x0, y0 = min(x for x, y in points), min(y for x, y in points)
x1, y1 = max(x for x, y in points) + 1, max(y for x, y in points) + 1
scale = 147 / (x1 - x0)
height = (y1 - y0) * scale

# Use the original bitmap directly as an alpha mask, preserving its antialiased edge.
blue_background = im.getpixel((0, 0))[2]
alpha_slope = 255 / (255 - blue_background)
alpha_offset = -blue_background / (255 - blue_background)

pieces = []
placements = [('tuntun-icecream-original.png', 38, 34, -7),
              ('tuntun-pizza-original.png', 107, 34, 7),
              ('tuntun-coconut-original.png', 40, 76, 5),
              ('tuntun-bow-original.png', 106, 76, -5)]
for name, cx, cy, angle in placements:
    picture = Image.open(SOURCE / name)
    ax0, ay0, ax1, ay1 = picture.getchannel('A').getbbox()
    h = 32
    w = h * (ax1 - ax0) / (ay1 - ay0)
    pieces.append(f'<g transform="rotate({angle} {cx} {cy})"><svg x="{cx-w/2:.5f}" y="{cy-h/2:.5f}" width="{w:.5f}" height="{h}" viewBox="{ax0} {ay0} {ax1-ax0} {ay1-ay0}"><image href="{uri(SOURCE/name)}" width="{picture.width}" height="{picture.height}"/></svg></g>')

checks = ''.join(f'<rect x="{i*14.7}" y="{j*14.7}" width="14.7" height="14.7" fill="{["#243b83", "#354f9c", "#4e6fb1"][(i+j)%3]}"/>'
                 for i in range(10) for j in range(8))
stars = ''.join(f'<text x="{x}" y="{y}" font-size="5" fill="{color}">✦</text>'
                for x, y, color in [(63, 32, '#ffb82f'), (78, 72, '#ff8a3c'), (19, 59, '#9ee6d8'), (124, 56, '#ffd66f')])

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="297mm" height="210mm" viewBox="0 0 297 210">
<title>TUNTUN 四枚迷你肖像：原始图稿与标准轮廓的尺度排版</title>
<desc>包装宽147mm来自产品目录；目录高100mm与旧物料105mm不一致。本图等比使用已确认位图轮廓，高约{height:.1f}mm，不作为实测或刀模。</desc>
<defs><filter id="white-alpha" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 {alpha_slope:.8f} 0 {alpha_offset:.8f}"/></filter><mask id="approved" maskUnits="userSpaceOnUse" x="0" y="0" width="147" height="{height:.5f}" style="mask-type:alpha"><image href="{uri(REFERENCE)}" x="{-x0*scale:.6f}" y="{-y0*scale:.6f}" width="{im.width*scale:.6f}" height="{im.height*scale:.6f}" filter="url(#white-alpha)"/></mask><marker id="arrow" markerWidth="5" markerHeight="5" refX="2.5" refY="2.5" orient="auto-start-reverse"><path d="M5 0L0 2.5L5 5" fill="none" stroke="#263955" stroke-width=".6"/></marker></defs>
<rect width="297" height="210" fill="#f6f2e9"/>
<g font-family="PingFang SC,Microsoft YaHei,sans-serif" fill="#263955">
<text x="15" y="16" font-size="5.6" font-weight="700">B · TUNTUN MINI GALLERY</text>
<text x="15" y="23" font-size="3.1">参考「萌宠肖像馆」：一版四枚迷你肖像，直接排入用户原图</text>
<path d="M15 32H162" stroke="#263955" stroke-width=".35" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
<path d="M15 34V41M162 34V41" stroke="#263955" stroke-width=".3"/>
<rect x="60" y="28.5" width="59" height="7" fill="#f6f2e9"/><text x="89.5" y="33.2" font-size="3.5" text-anchor="middle">整版宽 147 mm</text>
<g transform="translate(15 45)"><g mask="url(#approved)">
{checks}<rect x="0" y="0" width="147" height="15" fill="#ff8a2c"/>
<rect x="0" y="95" width="147" height="12" fill="#ffe4ab"/>
<text x="73.5" y="12.5" text-anchor="middle" font-size="2.4" font-weight="700" fill="#243b83">SHANLE LAB × TUNTUN</text>
<circle cx="73.5" cy="5.5" r="1.7" fill="#f6f2e9"/>
{stars}{''.join(pieces)}
<text x="73.5" y="101.2" font-size="3.5" text-anchor="middle" font-weight="800">POPSTICKER</text>
</g></g>
<text x="15" y="160" font-size="3.3" font-weight="700">单枚高 32 mm · 本轮候选</text>
<text x="15" y="167" font-size="3">保留四张原画的图形、表情、徽章边框；不经过 AI 重画。</text>
<text x="15" y="174" font-size="3">外形及两侧弧形直接采用已确认位图蒙版，整体等比缩放。</text>
<text x="184" y="39" font-size="3.3" font-weight="700">A6 纸张参照 · 105 × 148 mm</text>
<rect x="184" y="45" width="105" height="148" rx=".4" fill="white" stroke="#9ca7af" stroke-width=".4"/>
<text x="236.5" y="63" font-size="3.5" text-anchor="middle">应用尺寸对照</text>
<image href="{uri(SOURCE/'tuntun-coconut-original.png')}" x="{236.5-38*1025/902/2:.4f}" y="87" width="{38*1025/902:.4f}" height="38"/>
<path d="M269 87V125" stroke="#263955" stroke-width=".3" marker-start="url(#arrow)" marker-end="url(#arrow)"/>
<text x="236.5" y="139" font-size="3.3" text-anchor="middle">此枚高 38 mm · 候选</text>
<text x="236.5" y="147" font-size="3" text-anchor="middle">不代表笔记本实物尺寸</text>
<text x="15" y="201" font-size="2.65">尺寸边界：目录高度 100 mm、旧图 105 mm；本图按标准轮廓等比得 {height:.1f} mm，待实物核验。非生产刀模。</text>
</g></svg>'''
(ROOT / '07-four-portraits-scale-proof.svg').write_text(svg)
(ROOT / 'scale-proof.json').write_text(json.dumps({
    'card_width_mm': 147, 'source_mask_bbox_px': [x0,y0,x1,y1],
    'proportional_height_mm': height, 'portrait_height_mm': 32,
    'applied_portrait_height_mm': 38, 'reference_paper_mm': [105,148],
    'height_conflict_mm': [100,105],
    'status': 'width from catalog; proportional template height and patch sizes are review proposals',
    'source_art': 'original supplied raster files embedded unchanged',
}, ensure_ascii=False, indent=2)+'\n')
print(f'Native SVG proof: width 147 mm; template-proportional height {height:.3f} mm; four 32 mm portraits; A6 reference.')
