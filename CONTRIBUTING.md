# 跨项目共用 SHANLE 工作区

唯一根目录是 `/Users/ziqing/Documents/codexprojects/recent-workspace`，唯一发布仓库是 `calfnai/shanlelab-workspace`。任意项目/对话都能读取、贡献；原项目继续持有原稿、模型和决策记录。

## 每个项目独立更新

`projects/<稳定id>.json` 是成果清单的权威来源。`site/data.js` 只由构建命令生成，不直接编辑。现有 id：mlbb-retail、mlbb-gift、mlbb-booth、niko、pouch、booth-3x3、booth-4x4；可以继续新增 SHANLE 项目。

```sh
python3 /Users/ziqing/Documents/codexprojects/recent-workspace/workspace.py list
python3 /Users/ziqing/Documents/codexprojects/recent-workspace/workspace.py get niko > /tmp/niko-update.json
# 编辑 /tmp/niko-update.json 中的 project，保留 revision
python3 /Users/ziqing/Documents/codexprojects/recent-workspace/workspace.py put /tmp/niko-update.json
```

`put` 在同一把文件锁内校验版本、更新该项目并重建页面数据。其他项目记录保持原样。同一项目发生更新冲突时会拒绝旧记录；重新 get 后合并，不要删除 revision 或强制覆盖。临时文件名按任务取不同名称。

新增项目：参考已有 JSON 的字段，提交 `{ "revision": null, "project": { ... } }`。至少包含真实图稿；模型、邮件或提案可作为 links。新增素材复制到 `site/` 中项目独立目录，使用相对地址；本地源目录、凭据及对话正文不要进入公开清单。

`python3 build.py` 只汇总现有项目 JSON，不扫描或覆盖它们。旧的源素材采集代码保留为 `python3 refresh_sources.py --project <id>`：仅在确需重新采集对应旧项目时使用，执行前后审阅该项目差异，避免把手工维护的确认状态改回旧快照。此脚本仍可能复制共享附件，因此与其他构建共用文件锁。

## 确认状态与发布

最新渲染、用户选定、邮件已发送、合作方批准分别记录。用户选定成果置顶，其他版本保留；不要按版本号自动升级确认状态。MLBB C 原版与已发送邮件里程碑继续保留。

```sh
python3 verify.py
node --check site/app.js
python3 serve.py status
```

预览只用 serve.py。发布前查看 git status/diff，只暂存本次任务的文件。多人/多对话不同时修改共享 app.js、样式或构建器；项目更新尽量只写自己的 JSON 和素材。不要 git add .，不要覆盖或清理其他人的未提交成果。推送被拒绝时保留现场，整合远端后重试，禁止强推。GitHub Actions 负责发布 site/。

更新页面时提交对应项目 JSON、生成的 site/data.js 和本次新增素材。完成部署后核对在线页面和改动资源；Git 推送成功与线上验证成功分开报告。

## 在新对话调用

使用 `shanle-workspace` 技能，或把本文件绝对路径交给该对话。现有运行中对话不会自动重新载入新增技能，也不会自动收集新成果；用户要求“把这次成果同步到 SHANLE 共享工作区”时再执行更新。

网页对话地址已统一内置为现有 Tailscale WebUI `http://100.114.160.99:25808/`；不要恢复手填地址弹窗或唤起本机应用的协议。目标访问者须连接同一 Tailscale 并登录，不能将根页面 HTTP 200 当作登录后目标对话已验证。

## 当前收录范围与用户确认 · 2026-11-06

- `chengdu-2c2d` 是同一个成都项目：三套椭圆包装属于联名产品层面，店内优化属于零售陈列层面，二者关联维护，不拆成两个孤立项目。
- 巨型入口／门口装置计划已由用户取消。当前只保留店内陈列优化，以及头部增加几十厘米级小装置的设想；新造型、尺寸、安装方案尚未确认。用户进一步要求移除巨型装置3D：GLB／STEP、专用建模及检查文件已移出原目录，仅保留效果图。不要恢复模型或自动重新生成。旧巨型装置图不作为当前成果展示。
- `fluffycon-d06` 纳入近期推进，接续既有 v03 三墙结构稿；v01 毛绒袋主推已否决，不恢复为当前方向。
- `overseas-catalogs` 使用 `lifecycle: ongoing`，属于长期维护项目，不因阶段图解或一次发布而标记整个项目完成。首页和导航将其与近期推进分开。
- 用户明确暂不处理：圣诞护照夹贴纸应用、美国英文展布／桌布、PopSticker Temu 上架素材、ToyC 纸货架陈列、丕场陈列。不要仅因扫描到文件就自动收录。
- 杭州新物集与 Taggy 仍在此前候选清单中，本轮未新增。
- 项目可用 `currentFocus`、`cancelledScope`、`workstreams` 记录当前推进、已取消范围及同一项目内的层面；图库说明应区分现有参考图与尚未完成的新设想。
