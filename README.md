# Startup-Global: The Global Ecosystem Explorer

![License](https://img.shields.io/github/license/Genox-developer/Startup-Global?color=blue)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Framework](https://img.shields.io/badge/Flask-3.1-black)
![Database](https://img.shields.io/badge/SQLite-Integrated-green)
![Coverage](https://img.shields.io/badge/Opportunities-32,500%2B-orange)

**Discover 32,500+ startup funding, grants, accelerators & cloud perks across 190+ countries and 100+ industries.**

Startup-Global is an open-source, scalable platform designed to democratize access to capital, infrastructure, and growth opportunities for founders worldwide. Built by **Genox Holdings**, it aggregates hyper-local and tier-1 venture data into a single, lightning-fast dashboard.

---

## 🌟 Key Features

1. **Hyper-Scale Coverage**: Scrapes, indexes, and normalizes 32,500+ opportunities across 190+ countries.
2. **Real-Time Crawler Engine**: A robust backend (Crawler API) pulling live data from VCs, Angel Networks, Government portals, and accelerators.
3. **Advanced Filtering**: Find precise matches by Country, Industry, Funding Stage, and Organization Type.
4. **Investor Ready**: Designed to highlight top-tier ecosystem drivers—from Sequoia and Y Combinator to niche hyper-local grants.
5. **Internationalization (i18n)**: Fully localized to support 17 languages natively.

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Genox-developer/Startup-Global.git
cd Startup-Global
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Application
```bash
# Optional: Set admin API key for Crawler Admin endpoints
export ADMIN_API_KEY="your-secure-key"

python app.py
```
Visit `http://localhost:5000` to access the dashboard.
Visit `http://localhost:5000/admin` to access the Crawler API dashboard.

## 🏗 Architecture
- **Backend**: Python 3.11, Flask, SQLAlchemy, asyncio/aiohttp (for concurrent scraping).
- **Frontend**: Vanilla CSS ("Serious Dark" standard), Jinja2 templates, async JS fetching.
- **Database**: SQLite (local) / PostgreSQL (production-ready via SQLAlchemy).

For details on the crawling infrastructure, see [CRAWLER_API_ARCHITECTURE.md](CRAWLER_API_ARCHITECTURE.md).

## 🌍 Open Source Mission
We believe that every founder deserves equal access to ecosystem data. This project is proudly open source. 
See [ROADMAP.md](ROADMAP.md) for our future plans.

## 🤝 Contributing
Please see our [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## 🔒 Security
For vulnerability reporting, please see [SECURITY.md](SECURITY.md).

---
*Built with ❤️ by [Genox Holdings](https://genoxholdings.com)*
