<div align="center">

# 🌍 Global Startup Explorer

**Discover startup funding, grants, accelerators & cloud perks across 100+ countries and 100+ industries.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Visit_Now-00C853?style=for-the-badge)](https://global-startup-explorerglobal-startup.onrender.com)
[![Genox Holdings](https://img.shields.io/badge/🏢_Genox_Holdings-Official_Site-FF6F00?style=for-the-badge)](https://genoxholdings.com)

<br/>

*Built for startups, by a startup in Seoul, South Korea 🇰🇷*
*An open-source project by [Genox Holdings](https://genoxholdings.com)*

[🌐 Live Demo](https://global-startup-explorerglobal-startup.onrender.com) · [🏢 Genox Holdings](https://genoxholdings.com) · [Getting Started](#-getting-started) · [Features](#-features) · [Deploy](#-deployment) · [Support Us](#-support-this-project)

</div>

---

## 📖 What is This?

**Global Startup Explorer** is a self-contained, open-source web dashboard that aggregates startup ecosystem opportunities from around the world — government grants, VC programs, accelerators, corporate open innovation, and cloud/infrastructure perks — into a single, searchable, filterable interface.

Whether you're a first-time founder looking for pre-seed grants or a scaling startup seeking cloud credits, this tool helps you find opportunities matched to your country, industry, and stage.

> 🌐 **Live Demo**: [global-startup-explorerglobal-startup.onrender.com](https://global-startup-explorerglobal-startup.onrender.com)
> 🏢 **Our Company**: [genoxholdings.com](https://genoxholdings.com)

### Why We Built This

As a startup based in Seoul, South Korea ([Genox Holdings](https://genoxholdings.com)), we spent countless hours scouring government portals, VC databases, and accelerator sites across dozens of countries. We built this tool internally first, and now we're open-sourcing it because **every founder deserves access to global opportunities**, not just those in Silicon Valley.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌐 **100+ Countries** | Opportunities from USA, UK, EU, Singapore, Japan, Korea, India, UAE, Brazil, Nigeria, and many more |
| 🏭 **100+ Industries** | AI/ML, FinTech, BioTech, CleanTech, EdTech, SpaceTech, Agri-Food, Gaming, Cybersecurity... |
| 🏛 **Gov Grants** | SBIR/STTR (USA), Innovate UK, Horizon Europe, TIPS (Korea), MAFF (Japan), and more |
| 🚀 **VCs & Accelerators** | Y Combinator, Techstars, 500 Global, Sequoia, Founders Factory, Plug and Play... |
| 🏢 **Corporate OI** | SAP.io, Microsoft for Startups, Google for Startups, Samsung NEXT, Intel Ignite... |
| ☁️ **Cloud & Perks** | AWS Activate, Google Cloud credits, Azure credits, Stripe Atlas, OpenAI, Anthropic... |
| 🔍 **Smart Search** | Full-text search across titles, providers, and descriptions |
| 📊 **Fit Score** | Every opportunity ranked 0–100 for quick prioritization |
| 🤖 **Auto-Crawler** | Background scheduler crawls new data every 6 hours automatically |
| 📄 **Pagination** | Handles thousands of records with smooth, paginated views |
| 🎨 **Dark Mode UI** | Premium dark theme designed for extended use |

---

## 📸 Screenshots & Demo

<div align="center">

### Dashboard Overview

![Dashboard](docs/screenshots/demo_landing.png)

*4,800+ opportunities across 104 countries — all searchable and filterable*

### Category Filtering

![Category Filter](docs/screenshots/demo_category_filter.png)

*Filter by Gov Grants, VCs & Accelerators, Corporate OI, Cloud Perks, and Relocation programs*

### Search — "Techstars" (103 results)

![Search](docs/screenshots/demo_search.png)

*Full-text search across titles, providers, and descriptions*

### Country Filter — Germany (65 results)

![Country Filter](docs/screenshots/demo_country_filter.png)

*Drill down by specific countries*

### Pagination

![Pagination](docs/screenshots/demo_pagination.png)

*Smooth pagination across thousands of records*

</div>

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+** (3.9+ should also work)
- **pip** (Python package manager)
- **Git**

### Quick Start (Local)

```bash
# 1. Clone the repository
git clone https://github.com/Genox-developer/global-startup-dashboard.git
cd global-startup-dashboard

# 2. Create a virtual environment (recommended)
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py

# 5. Open your browser
# Navigate to http://localhost:5000
```

That's it! The database will automatically seed with **4,800+** global opportunities on first run.

---

## 🏗 Architecture

```
global-startup-dashboard/
├── app.py                      # Main Flask application
├── models.py                   # SQLAlchemy database models
├── data_mock.py                # Initial data generator (4,800+ records)
├── startup_crawler_global.py   # Auto-crawler (SBIR, Innovate UK, etc.)
├── templates/
│   └── index.html              # Single-page dashboard UI
├── Dockerfile                  # Docker container config
├── docker-compose.yml          # Docker Compose config
├── Procfile                    # PaaS deployment (Heroku, Render, etc.)
├── requirements.txt            # Python dependencies
└── README.md                   # You are here
```

### How It Works

1. **First Run**: `data_mock.py` generates 4,800+ records covering 95 countries × 25 industry sectors
2. **Auto-Crawler**: Every 6 hours, `startup_crawler_global.py` crawls live sources (SBIR/STTR API, Innovate UK, etc.) and appends new data
3. **3-Month Cleanup**: Records older than 90 days are automatically purged to keep the database fresh
4. **No Limits**: There are zero hardcoded caps — data accumulates indefinitely

### Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3.11, Flask |
| Database | SQLAlchemy (SQLite locally, PostgreSQL in production) |
| Crawler | AsyncIO + aiohttp + BeautifulSoup4 |
| Frontend | Vanilla HTML/CSS/JS (no framework dependency) |
| Deployment | Docker, Gunicorn |

---

## 🌐 Deployment

You can deploy this anywhere that supports Python. Here are the most popular options:

### Option 1: Render.com (Free Tier, Recommended)

1. Fork this repository to your GitHub account
2. Go to [render.com](https://render.com) and sign up (free)
3. Click **"New Web Service"**
4. Connect your GitHub repo
5. Configure:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Click **Deploy** — your site will be live in ~2 minutes!

> 💡 **Tip**: For production, set the `DATABASE_URL` environment variable to a PostgreSQL connection string for better performance and persistence.

### Option 2: Railway.app

1. Go to [railway.app](https://railway.app)
2. Click **"Deploy from GitHub"** → select your forked repo
3. Railway auto-detects Python and deploys automatically
4. (Optional) Add a PostgreSQL plugin for persistent storage

### Option 3: Heroku

```bash
# Install Heroku CLI, then:
heroku create your-app-name
git push heroku main
heroku open
```

### Option 4: Docker (Self-Hosted)

```bash
# Using Docker Compose (easiest)
docker-compose up -d

# Or build manually
docker build -t startup-explorer .
docker run -p 5000:5000 startup-explorer
```

### Option 5: VPS (DigitalOcean, AWS EC2, etc.)

```bash
# SSH into your server
git clone https://github.com/Genox-developer/global-startup-dashboard.git
cd global-startup-dashboard

# Install Python & dependencies
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Run with Gunicorn (production)
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app

# (Optional) Use systemd or supervisor to keep it running
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///instance/global_data.db` |
| `PORT` | Server port | `5000` |

---

## 🧩 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard UI |
| `/api/data` | GET | Query opportunities (supports `country`, `industry`, `category`, `search` params) |
| `/api/refresh` | POST | Trigger a manual recrawl |

### Example API Call

```bash
# Get all AI opportunities in Germany
curl "http://localhost:5000/api/data?country=Germany&industry=AI%2FML&category=All"

# Search for Techstars programs
curl "http://localhost:5000/api/data?search=techstars"
```

---

## 🤝 Contributing

We welcome contributions from the community! Whether it's adding new data sources, improving the UI, or fixing bugs.

### How to Contribute

1. **Fork** this repository
2. Create a **feature branch** (`git checkout -b feature/add-new-source`)
3. **Commit** your changes (`git commit -am 'Add new data source for XYZ country'`)
4. **Push** to the branch (`git push origin feature/add-new-source`)
5. Open a **Pull Request**

### Ideas for Contributions

- 🌏 **Add more country-specific data sources** (e.g., India's DPIIT, Japan's METI)
- 🎨 **UI improvements** (charts, map visualizations, dark/light mode toggle)
- 🤖 **Crawler enhancements** (add new APIs, improve scraping resilience)
- 🌍 **Translations** (add more language support)
- 📊 **Analytics** (add trend charts, comparison features)

---

## ☕ Support This Project

If this project has been helpful to you or your startup, consider supporting us! Your support helps us maintain and improve this tool for the global startup community.

<div align="center">

### 💖 Ways to Support

| Platform | Link |
|----------|------|
| ⭐ **Star this repo** | It's free and helps others discover this tool! |
| 🎗 **GitHub Sponsors** | [Sponsor on GitHub](https://github.com/sponsors/Genox-developer) |
| ☕ **Ko-fi** | [ko-fi.com/genoxholdings](https://ko-fi.com/genoxholdings) |
| 🪙 **USDT (TRC20)** | `TUmUVHfxsFLZQToE5j4oGaPCMRKBLRjEcv` |

</div>

> ☕ **Buy us a coffee** — every cup helps us crawl one more data source!
>
> 🍕 **Buy us a pizza** — and we'll add your country's startup programs next!

Your support, whether it's a star ⭐, a share on social media, or a small donation, goes a long way in keeping this project alive and free for everyone.

---

## 📬 Contact

For questions, business inquiries, or partnership proposals:

📧 **Email**: [developer@genox.one](mailto:developer@genox.one)

🌐 **Website**: [genoxholdings.com](https://genoxholdings.com)

---

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and share this software for **non-commercial purposes only**. Commercial use of this software or its derivatives is strictly prohibited. For commercial licensing inquiries, please contact [developer@genox.one](mailto:developer@genox.one). 🙏

---

<div align="center">

**Built with ❤️ by [Genox Holdings](https://genoxholdings.com) · Seoul, South Korea 🇰🇷**

*Helping startups find opportunities worldwide, one data point at a time.*

[![Stars](https://img.shields.io/github/stars/GenoxAI/global-startup-dashboard?style=social)](https://github.com/GenoxAI/global-startup-dashboard)
[![Forks](https://img.shields.io/github/forks/GenoxAI/global-startup-dashboard?style=social)](https://github.com/GenoxAI/global-startup-dashboard/fork)

</div>
