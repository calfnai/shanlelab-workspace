# Recent workspace

- This is an independent index, with one canonical site entry at `site/index.html`.
- Preserve original projects. Curate copies through `build.py`; never move or edit source assets during indexing.
- Snapshot labels must distinguish latest generated, user selected, sent, recipient accepted, historical and withdrawn. A higher version number alone does not imply approval.
- Keep conversation content, credentials, pricing sheets and the source path manifest out of the published site.
- Preview only through `serve.py`; do not spawn duplicate servers or kill unrelated processes.
- Run `python3 verify.py` after changing the asset index and `node --check site/app.js` after editing JavaScript.
- The user explicitly authorized external GitHub hosting. Repository calfnai/shanlelab-workspace is the sole publication target; existing gh credentials were verified by API despite intermittent TLS failures. AionUi native navigation has a verified protocol but no successful target-navigation check yet; WebUI currently times out.
