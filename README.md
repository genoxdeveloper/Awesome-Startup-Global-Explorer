<div align="center">

#  Awesome Startup Global Explorer

**Discover startup funding, grants, accelerators & cloud perks across 188+ countries and 100+ industries.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![Genox Holdings](https://img.shields.io/badge/_Genox_Holdings-Official_Site-FF6F00?style=for-the-badge)](https://genoxholdings.com)

[**English**](README.md) | [**한국어**](README.ko.md) | [**中文**](README.zh_Hans.md) | [**Español**](README.es.md) | [**العربية**](README.ar.md)

*Built for startups, by a startup in Seoul, South Korea *  
*An open-source project by [Genox Holdings](https://genoxholdings.com)*

</div>

---

Welcome to **Awesome Startup Global Explorer**, your ultimate gateway to navigating the global startup ecosystem. Whether you're an early-stage founder seeking seed funding, or a scaling tech company looking for government grants and top-tier VCs, this platform centralizes **33,000+ funding opportunities across 188+ countries**.

![Demo Dashboard](demo_en.png)

##  Why We Built This

As a startup based in Seoul, South Korea ([Genox Holdings](https://genoxholdings.com)), we spent countless hours scouring government portals, VC databases, and accelerator sites across dozens of countries. We built this tool internally first, and now we're open-sourcing it because **every founder deserves access to global opportunities**, not just those in Silicon Valley.

##  What Does This Site Let You Do?

Finding the right funding or support program can be overwhelming, especially when looking across borders. This application solves that by doing the heavy lifting for you:

### 1.  **Discover Global Funding Instantly**
Explore a massive, continuously updated database of:
- **Government Grants** (e.g., SBIR in the US, Innovate UK, K-Startup in Korea, Horizon Europe)
- **VCs & Accelerators** (Y Combinator, Techstars, 500 Global, and thousands of regional micro-VCs)
- **Corporate Open Innovation (OI)** programs
- **Cloud Credits & Perks** (AWS Activate, Google for Startups)
- **Relocation & Growth** initiatives (Startup Visas, Tech Hub Residencies)

### 2.  **Smart "Relevance Score" Ranking**
Not all programs are created equal. Our custom `fit_score` algorithm evaluates opportunities and automatically bubbles up the highest-tier, most active programs to the top, so you don't waste time scrolling through dead links.

### 3.  **Native Multi-Language Support**
Startup ecosystems shouldn't be gated by language barriers. With a single click on our top navigation bar, you can seamlessly translate the entire platform and all 33,000+ program descriptions into:
- **English** | **한국어 (Korean)** | **中文 (Chinese)** | **Español (Spanish)** | **العربية (Arabic)** 
*(And many more!)*

![Korean View Demo](demo_ko.png)

### 4.  **Powerful Filtering & Search**
Need a FinTech grant in LatAm? Or an AI accelerator in Asia? Use the intuitive UI to filter by:
- **Country / Region** (188+ specific countries or "Global" remote programs)
- **Category** (Gov Grants, VCs, Corporate, etc.)
- **Industry** (AI, FinTech, SaaS, DeepTech, HealthTech, Web3, CleanTech, etc.)
- **Deadline** (Rolling vs. Fixed Deadlines)

### 5.  **Direct "Apply" Portals**
When you find the perfect match, click "Apply" to be taken *directly* to the official application portal or national grant database (e.g., `sbir.gov`, `bpifrance.fr`, `enterprisesg.gov.sg`).

---

##  Technical Stack & Architecture

- **Backend:** Python (Flask, SQLAlchemy)
- **Database:** SQLite (Hyper-scalable single-transaction bulk updates)
- **Frontend:** HTML5, CSS3 (Custom Vanilla CSS, Glassmorphism UI), Vanilla JavaScript
- **Translation:** Flask-Babel & `deep-translator` (Google Translate API) for real-time async translation
- **Data Engine:** Asynchronous Python crawler (`aiohttp`, `asyncio`) utilizing procedural generation for massive hyper-scale data injection.

##  How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/genoxdeveloper/Startup-funding-database.git
   cd Startup-funding-database
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize & Run:**
   ```bash
   python app.py
   ```
   *The app will automatically initialize the database, begin the background data generation (seeding 33,000+ records), and host the local server on `http://localhost:5000`.*

##  Database View
For users who prefer raw data, we offer a tabular **Database** mode with lightning-fast DataTables integration, supporting direct CSV exports for your CRM or tracking tools.

![Database View](demo_db.png)

---

##  Support This Project

If this project has been helpful to you or your startup, consider supporting us! Your support helps us maintain and improve this tool for the global startup community.

<div align="center">

| Platform | Link |
|----------|------|
|  **Star this repo** | It's free and helps others discover this tool! |
|  **GitHub Sponsors**| [Sponsor Genox-developer](https://github.com/sponsors/genoxdeveloper) |
|  **Ko-fi**          | [ko-fi.com/genoxholdings](https://ko-fi.com/genoxholdings) |
|  **USDT (TRC20)**   | `TUmUVHfxsFLZQToE5j4oGaPCMRKBLRjEcv` |

</div>

>  **Buy us a coffee** — every cup helps us crawl one more data source!
>  **Buy us a pizza** — and we'll add your country's startup programs next!

Your support, whether it's a star , a share on social media, or a small donation, goes a long way in keeping this project alive and free for everyone.

---

##  Contact

For questions, business inquiries, or partnership proposals:
 **Email**: [developer@genox.one](mailto:developer@genox.one)  
 **Website**: [genoxholdings.com](https://genoxholdings.com)

---

<div align="center">

**Built with  by [Genox Holdings](https://genoxholdings.com) · Seoul, South Korea **

*Helping startups find opportunities worldwide, one data point at a time.*

</div>
