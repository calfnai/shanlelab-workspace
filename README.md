# SHANLE LAB · 近期工作区

独立项目根目录：`/Users/ziqing/Documents/codexprojects/recent-workspace`。
唯一页面入口：`site/index.html`。原设计项目均未修改。

## 使用

- 本机预览：<http://127.0.0.1:18916/>
- 启动：`python3 /Users/ziqing/Documents/codexprojects/recent-workspace/serve.py start`
- 状态 / 停止：同一命令改为 `status` / `stop`。
- 刷新素材：在本项目运行 `python3 build.py`，再运行 `python3 verify.py`。
- 图稿清单是 2026-11-06 的快照，后续成果不会在后台自动收集。

## 已整理

5 个项目，86 张完整原图，另有缩略图、niko 双面桌面 v07 自包含 3D 演示、圣诞提案 v04 PDF、联名创作说明及 MCT 矢量预览。每条版本线独立标示，未找到的旧稿没有伪造补齐。原始路径映射保存在忽略的 `local-manifest.json`。

## AionUi

本机已安装 AionUi 2.2.2，注册了 `aionui` 协议；核对安装代码后使用其受支持的 `aionui://navigate?route=%2Fconversation%2F<id>`。浏览器点击已出现打开 AionUi 的确认框，但本轮未验证成功切换至目标对话，不能当作端到端通过。

备用 WebUI 地址仅保存在浏览器 localStorage，可在设置中修改。当前 `127.0.0.1:25808` 请求超时，WebUI 直达未通过验证。其他电脑应使用该设备能访问的地址，并登录 AionUi。集合页没有上传对话正文、凭据或登录令牌。

## GitHub 承载

纯静态 `site/` 可部署到 GitHub Pages；工作流已放在 `.github/workflows/pages.yml`，发布目录仅为 `site/`。本机既有 calfnai 凭据已通过 API 验证；已创建独立仓库 `calfnai/shanlelab-workspace`，本轮正在发布。

GitHub Pages 默认公开，私有仓库不等于私有页面。用户已于 2026-11-06 明确要求 GitHub 外部访问；本次发布当前工作台的设计素材与邮件正文阶段稿，不发布邮件收发地址。Pages 构建来源为 GitHub Actions。不要把 AionUi 数据库或本地原项目整体上传。

## 验证记录

- `python3 verify.py`：5 个项目、86 张完整图片、189 处本地文件引用通过检查；包含演示模型与模块依赖。
- `node --check site/app.js`：通过。
- 原生浏览器中观察到首页、项目详情、图稿放大预览。
- 预览占用锁及固定端口，重复启动会拒绝；没有停止其他项目服务。
- 旧的已在线 niko 3D 和包装评审页 HTTP 200；不能据此认定其内容与本机最新成果一致。

## 当前里程碑

用户于2026-11-06明确选择 `mct-three-directions-review/C-MVP-Savage.png`，首页与赛事赠送款详情突出这张原图。C款后续修订放入其他版本，不会因版本号较高自动替代选定成果。

Gmail 已发送记录 `1a1aa52fc02d775e` 已核对；已发送正文与本地后续完整草稿分别保存。已发送附件为旧截图；未把它说成已补发原图或合作方已批准。

网页版提案提供 PDF；可编辑 PPTX 原件保留在原设计项目中，未放入首版网页。
