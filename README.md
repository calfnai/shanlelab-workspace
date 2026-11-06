# SHANLE LAB · 共享工作区

[打开共享页面](https://calfnai.github.io/shanlelab-workspace/) · [GitHub 仓库](https://github.com/calfnai/shanlelab-workspace)

这是 SHANLE 通用成果入口，供不同项目、不同对话共同使用和维护。它独立于各设计项目；图稿、3D、版本、确认状态与接续对话在此汇总，原稿保留在原目录。

本机唯一根目录：`/Users/ziqing/Documents/codexprojects/recent-workspace`。

- 跨对话更新：见 [CONTRIBUTING.md](CONTRIBUTING.md)，或调用 [shanle-workspace 技能](skills/shanle-workspace/SKILL.md)。
- 每个项目独立维护 `projects/<id>.json`；更新有文件锁与版本冲突检查，允许继续新增项目。
- 构建：`python3 build.py`；验证：`python3 verify.py` 和 `node --check site/app.js`。
- 预览：`python3 serve.py start`，唯一地址 http://127.0.0.1:18916/ 。
- GitHub Actions 发布 `site/`。这不是后台自动同步系统；每次按用户要求整理和发布。

当前 MLBB 赠送款以用户于 2026-11-06 选定的 C — MVP + SAVAGE 原版为主；后续修订属于其他版本。已发送邮件与后续完整草稿分开保存，合作方审批不视作已完成。

对话入口仅使用 HTTP/HTTPS 网页，不唤起本机 AionUi，也不默认跳转 localhost。已直接接入现有 Tailscale WebUI：`http://100.114.160.99:25808/`，不要求用户填写地址；访问者需连接同一 Tailscale 并登录。2026-11-06 核对根页面和主脚本 HTTP 200、HashRouter 对话路由存在，浏览器控制宿主不可用，因此未完成登录后打开目标对话的验证。新增技能不会追溯注入已运行的对话，可直接提供 CONTRIBUTING.md 路径接续。

图稿与模型为设计审阅材料，用户选款、合作方批准、生产定稿分别记录。公开页面不含对话正文、邮件收发地址或凭据。
