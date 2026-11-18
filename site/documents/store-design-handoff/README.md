# 给 ChatGPT Web：如何读取 SHANLE LAB 店铺设计 GitHub

这份 MD 是阅读指南。请沿下面的路径自行读取已有工作过程、原图和成果，不要求用户重讲，也不要只复述本指南。更新：2026-11-19。

## 入口与范围

- 仓库：https://github.com/calfnai/shanlelab-workspace
- 可视化成果网站：https://calfnai.github.io/shanlelab-workspace/
- 本指南固定地址：https://calfnai.github.io/shanlelab-workspace/documents/store-design-handoff/README.md
- overseas 接续资料：https://calfnai.github.io/shanlelab-workspace/documents/overseas-chatgpt-sync/current.md

仓库收录跨项目成果和部分决策过程，原项目继续持有源文件。不要说它包含全部本地文件、完整聊天或完整设计历史。这里只教你读取资料；不要求改写项目说明、长期记忆或原有重要文件，也不代表已建立自动双向同步。

## 第一步：从项目 JSON 找到当前工作，别只看仓库首页

先按用户提到的项目读取下表对应清单。用户要求全面了解店铺设计时才遍历七个项目；单项任务只读该项目和必要关联资料。不要扫描整仓、所有历史或下载全部大文件。

| 工作线 | 权威项目清单（可直接读取的 JSON） | 网页评审入口 |
| --- | --- | --- |
| niko and… | https://raw.githubusercontent.com/calfnai/shanlelab-workspace/main/projects/niko.json | https://calfnai.github.io/shanlelab-workspace/#niko |
| MLBB 3×3 | https://raw.githubusercontent.com/calfnai/shanlelab-workspace/main/projects/booth-3x3.json | https://calfnai.github.io/shanlelab-workspace/#booth-3x3 |
| 杭州新物集 SPACE | https://raw.githubusercontent.com/calfnai/shanlelab-workspace/main/projects/hangzhou-xinwuji-space.json | https://calfnai.github.io/shanlelab-workspace/#hangzhou-xinwuji-space |
| NOWRE B1 | https://raw.githubusercontent.com/calfnai/shanlelab-workspace/main/projects/nowre.json | https://calfnai.github.io/shanlelab-workspace/#nowre |
| 成都 2C2D | https://raw.githubusercontent.com/calfnai/shanlelab-workspace/main/projects/chengdu-2c2d.json | https://calfnai.github.io/shanlelab-workspace/#chengdu-2c2d |
| 4×4 | https://raw.githubusercontent.com/calfnai/shanlelab-workspace/main/projects/booth-4x4.json | https://calfnai.github.io/shanlelab-workspace/#booth-4x4 |
| TUNTUN | https://raw.githubusercontent.com/calfnai/shanlelab-workspace/main/projects/tuntun-popsticker.json | https://calfnai.github.io/shanlelab-workspace/#tuntun-popsticker |

读这些字段（有才读，不假定每个项目都具备）：

- `currentFocus`、`description`、`note`：目前做什么、最新更正与限制。
- `items`：成果原图；逐项读 `label`、`status`、`note` 和 `file`。不要只看第一张，也不要用缩略图代替重要细节。
- `links`：评审页、方案说明、尺寸册、PDF、SVG、3D和交接包。
- `progress` 中的 `decisions`、`history`、`next`、`sources`、`visualGroups`，以及顶层 `decisions`、`comparison`、`workstreams`、`milestone`：已有过程记录、分支比较、阶段交付与待办。
- `cancelledScope`、`withdrawnItems`、`reviewArchive`：取消、否决和替换范围。
- `sync.checkedAt` 只代表该项检查记录的日期；不要认为它保证清单中所有嵌套摘要同样新。

同一清单内也可能存在旧摘要：先核对明确日期、具体决定及其引用文件。遇到相互冲突，展示冲突和依据，不按字段顺序或最高版本号猜结论。

## 第二步：把清单变成能打开的文件，再实际看成果

项目 JSON 里的相对路径，相对于网站根目录，而不是 JSON 所在目录：

```text
items[].file = demos/niko-paper-final-v15/preview/paper-overall.png
图片地址 = https://calfnai.github.io/shanlelab-workspace/demos/niko-paper-final-v15/preview/paper-overall.png
仓库文件 = https://github.com/calfnai/shanlelab-workspace/blob/main/site/demos/niko-paper-final-v15/preview/paper-overall.png
```

同样转换 `links[].href`、`thumb` 以及比较组中的文件路径；已经是 HTTPS 的链接原样保留。`thumb` 是缩略图，`file` 才是原图。仓库的 `site/` 对应 Pages 网站根，网站地址不再加 `site/`。

需要文字文件时，也可以直接读仓库原文：

```text
https://raw.githubusercontent.com/calfnai/shanlelab-workspace/main/site/<相对路径>
```

按任务查看整体、正背面、关键局部/平面、实样及尺寸依据；比较方案要把各候选都看过。参考资料、当前成果、已否决图分别识别，不能把历史图全部当作当前设计。打开 `links` 中的评审 HTML 后继续读取其图片和附件，不停在入口标题。PDF看相关页面；3D打不开就看对应预览和说明，明确没有验证模型。ZIP仅在确需交接文件时下载，不能仅见下载链接便声称已检查包内源稿。

如果网页只返回空壳或 JavaScript，看对应 JSON 和文件直链；不要把无法抓取网页误判为没有成果。链接无法访问时说明具体地址和缺口，尝试同一文件的 GitHub/raw/Pages 入口，不编造已读内容。现有 `manifest.json` 只是2026-11-19的辅助快照，不替代最新 `projects/*.json`。

## 第三步：需要理解“怎么做过来”时，再追相关历史

先读项目清单中已经整理的决定、历史、比较说明及旧稿链接。还需要某次改动依据时，查看该文件的 Git 历史，例如：

https://github.com/calfnai/shanlelab-workspace/commits/main/projects/niko.json

其他项目将 `niko.json` 替换为表中的文件名。进入相关提交，查看该 JSON 的前后差异、同次新增的说明和图稿；找到被替换文件时，从该提交的文件版本或 Browse files 打开。只追与问题相关的几次提交，不遍历全部仓库历史。

由此确认：原要求/原图 → 候选 → 用户指出的问题 → 具体修改 → 当前成果及尚未确认项。每个结论带对应文件或提交链接。提交说明和上传时间是线索，不自动证明用户批准、设计时间或对方收件。仓库没有记录的原因、聊天和过程就写“未找到记录”，不填补故事。

能使用 GitHub 连接器时，按仓库名和精确路径读取；否则用上述公开 HTTPS。工具可用性不足时明确范围，不要求用户把整套成果重传。

## 如何从成果理解用户的工作方法

- 用户优先看图：给实际图或图片直链和简短说明。读文件名/状态文字不等于看过设计。
- 主角系列带动整体展位：从真实产品的图形、色彩、纹样和文化语言延伸空间，其他系列保留个性，共同主题统一；实物陈列要支撑视觉主角。
- 原稿、真实包装、标准轮廓与实样优先。不得默默替换、拉伸或自由重画；修正比例时保留已认可的创意构图。
- 先核实场地、现有道具和安装携带，再安排选款、POP在包箱耳机帽子的应用、体验、取货和补货。展示位置、不同SKU与库存分开。
- 不同项目不能串用场地尺寸、货盘、选项归属或否决状态。尺寸注明来源和暂拟项，效果图/3D不等于制造或实人验证。
- 已生成、候选、选定、发送、对方打开、批准、生产/安装验收是不同状态。已取消不复活，旧稿不因版本号或文件时间被自动提升。

这些是阅读时的检查方向，理解具体做法仍要回到原图与决定记录。不要只把这几条当作已了解全部设计工作的证明。

## 阅读后的回复与后续接续

用简短中文说明“实际读了哪些资料、看了哪些图、当前任务理解到哪里”，附相关成果直链。用户要过程才按关键转折展示前后图，不主动重写一大份工作回顾，不重复搬运整个仓库。未读、打不开、没有记录、尚未确认的部分直说。

后续任务重新读取对应项目最新 JSON；不要一直使用初次聊天里的快照。网页端新决定需要交回 Codex 时，只整理本次变更、所涉项目、依据和待办，不擅自改长期记忆。资料在 GitHub 可读，不代表它已被投递进 ChatGPT 项目或被所有对话自动读取。
