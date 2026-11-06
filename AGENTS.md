# Recent workspace

- This is an independent index, with one canonical site entry at `site/index.html`.
- Preserve original projects. Curate copies through `build.py`; never move or edit source assets during indexing.
- Snapshot labels must distinguish latest generated, user selected, sent, recipient accepted, historical and withdrawn. A higher version number alone does not imply approval.
- Keep conversation content, credentials, pricing sheets and the source path manifest out of the published site.
- Preview only through `serve.py`; do not spawn duplicate servers or kill unrelated processes.
- Run `python3 verify.py` after changing the asset index and `node --check site/app.js` after editing JavaScript.
- The user explicitly authorized external GitHub hosting. Repository calfnai/shanlelab-workspace is the sole publication target; existing gh credentials were verified by API despite intermittent TLS failures. Conversation entries must use browser HTTP/HTTPS URLs only. The user rejected launching the local AionUi app. Never add aionui:// links or default to localhost; show an unconfigured state until a reachable WebUI URL is supplied.

## Shared SHANLE ownership

- This is the universal SHANLE workspace, editable from multiple source projects and conversations. It does not belong to computerUsage, MLBB, niko, or packaging alone.
- Read CONTRIBUTING.md before updating. Canonical project records live in projects/*.json. Use workspace.py get/put with revision checks; never edit generated site/data.js directly.
- build.py only assembles records. Old asset collection moved to refresh_sources.py and requires --project; do not use it as a blanket refresh.
- Use the shared workspace lock for build/index mutations. Keep each task's project and asset changes separate; preserve other conversations' uncommitted work. Do not force push.
- Shared reusable entry: skills/shanle-workspace/SKILL.md. New source projects can be added without creating another hub.
