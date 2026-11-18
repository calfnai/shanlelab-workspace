# TUNTUN × POPSTICKER · v02 萌宠组合与快乐补给站

2026-11-19 修订候选。[当前评审页](index.html) 只展示本轮候选与原有萌宠参考。

## 当前图稿

- [A · 三枚零食小剧场](04-products-multipatch.png)：三只带食物的独立角色贴片，蓝棋盘与短语错落组合；成人手、手机和回形针用于观察体感大小。
- [B · 四枚迷你肖像与 A6 比例对照](07-four-portraits-scale-proof.png)：四张用户原图直接排版，单枚高 32mm 为候选；右侧应用图高 38mm 为候选。
- [B · 原始 SVG 比例稿](07-four-portraits-scale-proof.svg) 与 [尺寸依据](scale-proof.json)。外形直接使用已确认蒙版，整体等比缩放；原图以原始字节嵌入。
- [niko · 快乐补给站中岛](05-niko-snack-island.png)：保留用户现场木托盘、常规款货架，补上小包装与手机、包、耳机的应用表达。
- [轻型展位 · 快乐补给站](06-light-snack-booth.png)：沿用背景布与纸中岛，区分放大的印刷角色和小尺寸实物商品。

## 参考与尺寸边界

已收集 21 款相关萌宠原图，重点参考花漾萌友、甜杯派对、海岛萌宠、星夜画廊、小困喵，以及三张现有实拍。清单在 [pet-reference-index.json](pet-reference-index.json)，原图与实拍在 `source/pet-references/`；没有将其他宠物角色作为 TUNTUN 新图案。

现有目录的整版宽为 147mm。目录高度记录 100mm，旧上架图记录 105mm，尚未实物复核。B 稿按已确认轮廓比例得 104.6mm，不冒充实测。A 的单枚约 35–45mm 为探索值；AI 实物图与场景不能作为量测或轮廓定稿。印刷和生产必须回到原图、标准蒙版及实物核对。

## 完整提示词与可编辑源

A 与两张场景使用内置 imagegen：[A 组合设计](prompts/04-products-multipatch.txt)、[A 尺度与品牌修正](prompts/04b-products-scale-correction.txt)、[niko 中岛](prompts/05-niko-snack-island.txt)、[niko 应用图修正](prompts/05b-niko-application-correction.txt)、[轻型展位](prompts/06-light-snack-booth.txt)。

B 由 [build-scale-proof.py](build-scale-proof.py) 用原画和原蒙版生成 SVG，经 rsvg-convert 渲染预览；不重绘角色。当前页由 [build-review.py](build-review.py) 生成，维持一个入口。

## 已否决方向

v01 三张图因比例不够写实、创意不够有趣被用户否决，已撤出当前页和共享图库。原文件与提示词保留追溯，不恢复为当前候选。本目录沿用初始名称，当前状态以本文件及页面 v02 为准。

所有新设计仍待用户评审，未选定、未打样、未获合作方批准。
