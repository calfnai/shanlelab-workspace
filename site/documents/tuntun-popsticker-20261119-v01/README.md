# TUNTUN × POPSTICKER · 两款产品定稿与生活应用

[当前评审页](index.html) 沿用唯一入口。本目录名称保持初始 v01，当前状态以本文件与 [版本状态](review-state.json) 为准。

## 本轮状态

- [04 三枚零食小剧场](04-products-multipatch.png)：用户反馈“还行”，保留方向继续比较，原图不改；不是生产或包装定稿批准。
- [08 表情组合](08-mood-trio-063.png)：参考用户指定 063 的表情、文字与拼布组合，新增 YUM / ZZZ / YAY。2026.11.19 用户确认产品定稿，原图保持不变。
- [09 街机拼贴](09-arcade-collage-052.png)：参考用户指定 052 的窗口色块与角色互动。2026.11.19 用户确认产品定稿，原图保持不变。
- [12 手持包装与手机应用](12-phone-application.png)：使用定稿表情款，YAY 头像贴在手机壳上；新增应用图单独评审。
- [13 包包应用](13-bag-application.png)：使用定稿街机款的披萨、椰子、星星与短语贴，组成小幅随身场景；新增应用图单独评审。
- [10 最新现场中岛](10-niko-latest-photo-scale.png)：以最新现场照替换图面，四包小商品保留在背板中间，应用立牌与售卖包装分开呈现。
- [11 快乐营业中展位](11-story-shop-booth.png)：沿用纸中岛构造，增加连续故事、分组挂货、表情窗口、试贴与生活物件应用。

## 包装与空间依据

重新查看现有 063 的实体正面，以及纸杯萌宠、疯狂动物实拍：印刷内卡、顶端挂孔区、两侧印刷弧线、浅透明 PET 罩和凸边是不同结构，不能用平面椭圆代替实体包装。固定轮廓保持原图横向比例、曲率和两侧弧线，不以普通椭圆替代。

- [现有 063 实体包装照片](source/pet-references/pet-063-actual-front.jpg)
- [固定品牌轮廓原图](source/pet-references/approved-popsticker-outline.png)
- [最新现场照片](source/niko-latest-site-20261119.jpg)
- [用户指定 063](source/pet-references/pet-063.jpg) / [052](source/pet-references/pet-052.jpg)

目录整版宽 147mm，高度有 100 / 105mm 两种记录，待实物核验。两张定稿产品图以现有 063 实拍包装正面作为编辑底版，包含已确认的贴纸内容、纸卡、标识与实体外形；原桌面构图保存为历史节点。应用图以正常成人手掌、约 75×155mm 手机和约 320mm 宽包身作尺度参照，手机头像约 35–38mm、包包角色约 40–45mm 为视觉模拟目标。图像不承担实物量测或印刷源稿功能。

展位以约 3m × 3m 的概念占地探索，未取得场地方实测图；台面高度、层板、柜体与通道须进一步结构落图。Meeko 手册第 8、17 页用于参考连续日常故事及跨物件应用，不照搬其角色或品牌。用户提供的完整手册和阅读渲染保存在本地归档，未公开。

## 产品定稿记录

SHANLE LAB 采用原始兔耳图形与下方单行横排英文的完整组合；POP STICKER 采用原始专用字标，两个 P 为星形镂空、O 内含双弧线。使用 [原始品牌资产对照](source/brand/brand-assets-reference.svg)，不是普通字体替代。包装重新以实体正面照片作底，修订过长的平直段和两侧弧线。

用户在三项修订后确认两款产品正确并要求定稿。确认范围包含两款产品视觉设计，已记录于 [定稿记录](product-finalization.json)；两张原文件的 SHA-256 指纹固定，新增应用图不覆盖它们。手机、包包应用图以及中岛、展位分别保留自己的评审状态。

## 完整提示词与制作方式

使用内置 imagegen。所有选用结果保存本目录；初次尺寸不通过的生成稿只留本地历史，未进入当前页面。

- 当前 08：[实拍包装底版与两套标识修订](prompts/08e-real-package-base.txt)
- 当前 09：[实拍包装底版](prompts/09e-real-package-base.txt) / [完整品牌组合修订](prompts/09f-full-logo-lockup.txt)
- 手机应用：[场景提示词](prompts/12-phone-application.txt) / [尺度修订](prompts/12b-phone-scale.txt)
- 包包应用：[场景提示词](prompts/13-bag-application.txt) / [尺度与独立贴片修订](prompts/13b-bag-scale.txt)
- [10 现场替换](prompts/10-niko-latest-photo-scale.txt) / [10 立牌文案](prompts/10b-niko-placard-copy.txt)
- [11 故事展位](prompts/11-story-shop-booth.txt) / [11 商品尺度与图案修订](prompts/11b-booth-product-scale-and-identity.txt)
- [评审页构建源](build-review.py)

## 撤回与历史

v01 三张图已因比例、创意不足被用户否决，不恢复。

v02 的 [07 四枚肖像比例稿](07-four-portraits-scale-proof.png) 被用户指出外形及包装错误，已撤回。其 SVG、build-scale-proof.py、scale-proof.json 仅保留历史，不再作为当前轮廓或尺寸依据，不能因脚本控制了数值就认定外形正确。

v02 的 05 中岛商品排货尺寸不通过；06 轻型展位被指出单薄、空、无聊，两张都撤出当前评审。保留文件用于追溯，不作为当前候选。
