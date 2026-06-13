# Keep vs. Remove Report

## Files Kept & Justification

| File/Directory | Purpose | Audience | Status |
|----------------|---------|----------|--------|
| `app.py`, `models.py`, `startup_crawler_global.py`, `data_vcs_massive.py`, `data_hyper_scale.py` | Core application logic, database models, and crawler data engines. | Developers, Operators | **KEPT** |
| `templates/` | Jinja2 templates for the UI and Crawler Admin Dashboard. | Users, Developers | **KEPT** |
| `requirements.txt` | Python dependencies required for deployment. | Operators, Contributors | **KEPT** |
| `Dockerfile`, `docker-compose.yml`, `Procfile`, `render.yaml` | Containerization and PaaS deployment configurations. | Operators | **KEPT** |
| `.gitignore`, `.dockerignore` | Git and Docker tracking rules. | Contributors | **KEPT** |
| `README.md` (and multilingual versions) | Core documentation and project entry point. | Users, Contributors | **KEPT** |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `ROADMAP.md` | Essential open-source governance and security policies. | Contributors, Users | **KEPT** |
| `LICENSE` | Legal usage rights (Open Source). | Everyone | **KEPT** |

## Files Removed & Justification

| File | Reason for Removal | Status |
|------|--------------------|--------|
| `push_repo.py` | Internal automation script containing a leaked GitHub token. Highly insecure. | **REMOVED** |
| `CLAUDE.md` | Internal AI instructions/scratchpad. | **REMOVED** |
| Intermediate Audit Reports (`SECURITY_REVIEW.md`, `QA_REPORT.md`, etc.) | Served their purpose during the audit phase. Clutters the repo. Contained sensitive historical leak data. | **REMOVED** |
| `.claude/settings.local.json` | Local IDE configuration not meant for public distribution. | **REMOVED** |
