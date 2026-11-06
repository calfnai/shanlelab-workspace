---
name: shanle-workspace
description: 查看或更新 SHANLE 通用成果工作区，将各项目的确认版本、其他版本、3D 演示和 AionUi 接续对话汇入同一 GitHub 页面。用于用户要求加入或同步 SHANLE 合集、工作区时。
---

唯一共享根目录：`/Users/ziqing/Documents/codexprojects/recent-workspace`。
页面：https://calfnai.github.io/shanlelab-workspace/
仓库：calfnai/shanlelab-workspace。它独立于任何 MLBB、niko、包装项目；不要另建合集仓库或把原项目迁进来。

先读根目录 `AGENTS.md` 和 `CONTRIBUTING.md`，再查看 Git 状态。项目源文件仍在各自原目录。

从任何工作目录执行：

```sh
python3 /Users/ziqing/Documents/codexprojects/recent-workspace/workspace.py list
python3 /Users/ziqing/Documents/codexprojects/recent-workspace/workspace.py get niko > /tmp/niko-update.json
```

只修改导出的 `project` 对象中本次任务涉及的内容，保留 `revision`。然后用 `workspace.py put /tmp/niko-update.json` 提交。检测到冲突时重新读取、合并，不要覆盖别人的工作。项目 JSON 是权威清单，`site/data.js` 为生成文件。
新项目使用稳定 id 和 `revision: null`，字段参考已有 `projects/*.json`。素材先复制到 `site/` 下独立子目录，引用用相对路径；无需迁移原稿。

最近生成不等于用户选定。保留既有确认、发送、审批状态，用户选定版本优先；未确认的修订排在其他版本。MLBB 赠送款当前选定 C — MVP + SAVAGE 原版；后续修订不可自动替代。

验证与发布遵循 CONTRIBUTING。用户只要求入库或同步本地时不要擅自推送；要求上线/更新共享页面时可推送既有发布目标。只暂存自己的文件，保留其他对话未提交的改动。报告本地更新、GitHub 部署和页面验证各自实际完成的状态。
