# Startup Global v1.0.0

The highly anticipated open-source release of **Startup Global**.

## Key Features

- **Hyper-Scale Coverage:** Scrapes, indexes, and aggregates over 32,500+ startup funding, grants, and accelerators globally across 190+ countries.
- **Real-Time Crawler API System:** Features a robust Admin Dashboard to register, track, and monitor external data sources with background `aiohttp` parallel scraping.
- **Investor Ready Data:** Pre-loaded with top-tier VCs (Sequoia, YC, a16z), Angel Networks, and hyper-local government grant structures.
- **Global i18n Localization:** Native support for 17 languages (including Korean, Japanese, Chinese, French, Spanish, Arabic) using `Flask-Babel`.
- **"Serious Dark" UI/UX:** A beautifully designed, highly-performant dark mode interface standardized by Genox Holdings.

## Security & Architecture Enhancements
- Secured all crawler endpoints via an `X-Admin-Key` authentication layer.
- Implemented robust SQLAlchemy parameterized queries, preventing SQL injection vectors.
- Complete removal of legacy mock data in favor of a 100% real-world data engine.
- Ensured total secret sanitization and minimized repository bloat prior to release.

## Looking Ahead
See our [ROADMAP.md](ROADMAP.md) for details on upcoming features, including advanced rate-limiting, Corporate Venture Capital (CVC) pipelines, and AI-native matchmaking.
