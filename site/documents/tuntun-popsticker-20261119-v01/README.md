# TUNTUN × POPSTICKER · v03 表情、街机与故事陈列

[当前评审页](index.html) 沿用唯一入口。本目录名称保持初始 v01，当前状态以本文件与 [版本状态](review-state.json) 为准。

## 本轮状态

- [04 三枚零食小剧场](04-products-multipatch.png)：用户反馈“还行”，保留方向继续比较，原图不改；不是生产或包装定稿批准。
- [08 表情组合](08-mood-trio-063.png)：参考用户指定 063 的表情、文字与拼布组合，新增 YUM / ZZZ / YAY，待评审。
- [09 街机拼贴](09-arcade-collage-052.png)：参考用户指定 052 的窗口色块与角色互动，待评审。
- [10 最新现场中岛](10-niko-latest-photo-scale.png)：以最新现场照替换图面，四包小商品保留在背板中间，应用立牌与售卖包装分开呈现。
- [11 快乐营业中展位](11-story-shop-booth.png)：沿用纸中岛构造，增加连续故事、分组挂货、表情窗口、试贴与生活物件应用。

## 包装与空间依据

重新查看现有 063 的实体正面，以及纸杯萌宠、疯狂动物实拍：印刷内卡、顶端挂孔区、两侧印刷弧线、浅透明 PET 罩和凸边是不同结构，不能用平面椭圆代替实体包装。固定轮廓保持原图横向比例、曲率和两侧弧线，不以普通椭圆替代。

- [现有 063 实体包装照片](source/pet-references/pet-063-actual-front.jpg)
- [固定品牌轮廓原图](source/pet-references/approved-popsticker-outline.png)
- [最新现场照片](source/niko-latest-site-20261119.jpg)
- [用户指定 063](source/pet-references/pet-063.jpg) / [052](source/pet-references/pet-052.jpg)

目录整版宽 147mm，高度有 100 / 105mm 两种记录，待实物核验。本轮小贴片约 35–42mm 仅为设计候选。产品图使用原 04 的构图作为修订基准，空间图使用最新现场的既有商品大小与挂位。图像生成仍可能改变边界、五官或局部大小，图片不承担量测或印刷源稿功能。

展位以约 3m × 3m 的概念占地探索，未取得场地方实测图；台面高度、层板、柜体与通道须进一步结构落图。Meeko 手册第 8、17 页用于参考连续日常故事及跨物件应用，不照搬其角色或品牌。用户提供的完整手册和阅读渲染保存在本地归档，未公开。

## 完整提示词与制作方式

使用内置 imagegen。所有选用结果保存本目录；初次尺寸不通过的生成稿只留本地历史，未进入当前页面。

- [08 初稿](prompts/08-mood-trio-063.txt) / [08 构图修订](prompts/08b-mood-fixed-composition.txt)
- [09 初稿](prompts/09-arcade-collage-052.txt) / [09 构图修订](prompts/09b-arcade-fixed-composition.txt)
- [10 现场替换](prompts/10-niko-latest-photo-scale.txt) / [10 立牌文案](prompts/10b-niko-placard-copy.txt)
- [11 故事展位](prompts/11-story-shop-booth.txt) / [11 商品尺度与图案修订](prompts/11b-booth-product-scale-and-identity.txt)
- [评审页构建源](build-review.py)

## 撤回与历史

v01 三张图已因比例、创意不足被用户否决，不恢复。

v02 的 [07 四枚肖像比例稿](07-four-portraits-scale-proof.png) 被用户指出外形及包装错误，已撤回。其 SVG、build-scale-proof.py、scale-proof.json 仅保留历史，不再作为当前轮廓或尺寸依据，不能因脚本控制了数值就认定外形正确。

v02 的 05 中岛商品排货尺寸不通过；06 轻型展位被指出单薄、空、无聊，两张都撤出当前评审。保留文件用于追溯，不作为当前候选。
