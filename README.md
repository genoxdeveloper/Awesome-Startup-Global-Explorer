<div align="center">

# Awesome Startup Global Explorer

**Discover startup funding, grants, accelerators & cloud perks across 188+ countries and 100+ industries.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)
[**English**](README.md) | [**한국어**](README.ko.md) | [**中文 (简体)**](README.zh_Hans.md) | [**中文 (繁體)**](README.zh_Hant.md) | [**Español**](README.es.md) | [**العربية**](README.ar.md) | [**Deutsch**](README.de.md) | [**Français**](README.fr.md) | [**हिन्दी**](README.hi.md) | [**Bahasa Indonesia**](README.id.md) | [**Italiano**](README.it.md) | [**日本語**](README.ja.md) | [**Português**](README.pt.md) | [**Русский**](README.ru.md) | [**ไทย**](README.th.md) | [**Türkçe**](README.tr.md) | [**Tiếng Việt**](README.vi.md)

*Built for startups, by a startup in Seoul, South Korea*  
*An open-source project by
**[Genox](https://genoxholdings.com)** & **[Buygit.com](https://buygit.com)***

</div>

---

Welcome to **Awesome Startup Global Explorer**, your ultimate gateway to navigating the global startup ecosystem. Whether you're an early-stage founder seeking seed funding, or a scaling tech company looking for government grants and top-tier VCs, this platform centralizes **35,000+ funding opportunities across 188+ countries**.

![Demo Dashboard](demo_en.png)

## 🏢 About Genox & Partners

**Genox** is an innovative tech venture based in Seoul, South Korea. We architect data-driven solutions and platforms that empower global startups. We believe in democratizing access to opportunities, breaking down borders, and accelerating innovation.

This open-source project is proudly supported and co-developed in partnership with **[Buygit.com](https://buygit.com)**, a premier platform dedicated to empowering developers and creators worldwide. Together, Genox and Buygit.com are committed to providing founders with the tools and data they need to build the next generation of unicorn startups.

We spent countless hours scouring government portals, VC databases, and accelerator sites across dozens of countries. We built this tool internally first, and now we're open-sourcing it because **every founder deserves access to global opportunities**, not just those in Silicon Valley.

## 🚀 What Does This Site Let You Do?

Finding the right funding or support program can be overwhelming, especially when looking across borders. This application solves that by doing the heavy lifting for you:

### 1. Discover Global Funding Instantly
Explore a massive, continuously updated database of:
- **Government Grants** (e.g., SBIR in the US, Innovate UK, K-Startup in Korea, Horizon Europe)
- **VCs & Accelerators** (Y Combinator, Techstars, 500 Global, and thousands of regional micro-VCs)
- **Corporate Open Innovation (OI)** programs
- **Cloud Credits & Perks** (AWS Activate, Google for Startups)
- **Relocation & Growth** initiatives (Startup Visas, Tech Hub Residencies)

### 2. Native Multi-Language Support (Breaking Down Borders)
We recognize that the next big unicorn could come from anywhere. However, the global startup ecosystem has historically been gatekept by a severe language barrier. Critical funding portals, complex grant compliance details, and intricate VC investment theses are often buried entirely in English or localized dialects. This creates an unfair advantage based solely on geography and native tongue.

To ensure absolutely no founder is left behind, our platform features an incredibly powerful, industry-leading **Native Multi-Language Support System**. This isn't just a simple UI translation—it is a comprehensive, deep-data localization pipeline.

With a single click on our top navigation bar, you can seamlessly translate the entire platform. This means that all **35,000+ deeply nested program descriptions, evaluation criteria, industry focuses, and dynamic database entries** are instantly localized into:
- 🇺🇸 **English** (Universal Default)
- 🇰🇷 **한국어 (Korean)**
- 🇨🇳 **中文 (Simplified Chinese)** & 🇹🇼 **繁體中文 (Traditional Chinese)**
- 🇪🇸 **Español (Spanish)**
- 🇦🇪 **العربية (Arabic)**
- 🇩🇪 **Deutsch (German)**
- 🇫🇷 **Français (French)**
- 🇮🇳 **हिन्दी (Hindi)**
- 🇮🇩 **Bahasa Indonesia (Indonesian)**
- 🇮🇹 **Italiano (Italian)**
- 🇯🇵 **日本語 (Japanese)**
- 🇵🇹 **Português (Portuguese)**
- 🇷🇺 **Русский (Russian)**
- 🇹🇭 **ไทย (Thai)**
- 🇹🇷 **Türkçe (Turkish)**
- 🇻🇳 **Tiếng Việt (Vietnamese)**
*(And we are continuously working to add more!)*

**Why is this revolutionary?**
Most startup databases only translate their static UI (buttons, menus) while leaving the actual data (which matters most) in its original language. Our platform solves this using a **dual-engine translation architecture**:
1. **Static UI Localization:** Powered by `Flask-Babel`, ensuring all structural elements, navigation, and core UX are perfectly localized with zero latency using pre-compiled `.po` and `.mo` message catalogs.
2. **Dynamic Data Translation:** Powered by an asynchronous pipeline utilizing `deep-translator`. When you switch languages, our system fetches the live, unstructured program descriptions from our SQLite database and translates them on-the-fly, preserving exact data schemas, markdown formatting, and critical funding criteria.

This means a founder in Bogota, Riyadh, or Seoul can read the complex compliance requirements of a US SBIR grant, or the investment thesis of a London-based VC network, in their native tongue as effortlessly as a founder in San Francisco. It entirely removes the friction of cross-border fundraising.

![Korean View Demo](demo_ko.png)

### 3. Smart "Relevance Score" Ranking
Not all programs are created equal. Our custom `fit_score` algorithm evaluates opportunities and automatically bubbles up the highest-tier, most active programs to the top, so you don't waste time scrolling through dead links.

### 4. Powerful Filtering & Search
Need a FinTech grant in LatAm? Or an AI accelerator in Asia? Use the intuitive UI to filter by Country/Region, Category, Industry, and Deadlines.

### 5. Direct "Apply" Portals
When you find the perfect match, click "Apply" to be taken *directly* to the official application portal.

---

## 💻 Technical Stack & Architecture

- **Backend:** Python (Flask, SQLAlchemy)
- **Database:** SQLite (Hyper-scalable single-transaction bulk updates)
- **Frontend:** HTML5, CSS3 (Custom Vanilla CSS, Glassmorphism UI), Vanilla JavaScript
- **Translation:** Flask-Babel & `deep-translator` (Google Translate API) for real-time async translation
- **Data Engine:** Asynchronous Python crawler (`aiohttp`, `asyncio`) utilizing procedural generation for massive hyper-scale data injection.

## 🛠️ How to Run Locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/genoxdeveloper/Awesome-Startup-Global-Explorer.git
   cd Awesome-Startup-Global-Explorer
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize & Run:**
   ```bash
   python app.py
   ```
   *The app will automatically initialize the database, begin the background data generation (seeding 35,000+ records), and host the local server on `http://localhost:5000`.*

## 📊 Database View
For users who prefer raw data, we offer a tabular **Database** mode with lightning-fast DataTables integration, supporting direct CSV exports for your CRM or tracking tools.

![Database View](demo_db.png)

---

## 💖 Support This Project & Partners

If this project has been helpful to you or your startup, consider supporting us! Your support helps us maintain and improve this tool for the global startup community.

<div align="center">

| Platform | Link |
|----------|------|
| ⭐ **Star this repo** | It's free and helps others discover this tool! |
| 🤝 **Buygit.com** | Check out our partner [Buygit.com](https://buygit.com) |
| 💼 **GitHub Sponsors**| [Sponsor Genox-developer](https://github.com/sponsors/genoxdeveloper) 
| 🪙 **USDT (TRC20)**   | `TUmUVHfxsFLZQToE5j4oGaPCMRKBLRjEcv` |

</div>

Your support, whether it's a star, a share on social media, or a small donation, goes a long way in keeping this project alive and free for everyone.

---

## 🤝 Contributing
We welcome contributions from founders and developers worldwide! If you know of a grant, VC, or accelerator in your country that isn't listed, please open an issue or submit a Pull Request.

## 📬 Contact

For questions, business inquiries, or partnership proposals:
- **Email**: [admin@genox.one](mailto:admin@genox.one)  [support@buygit.com](mailto:support@buygit.com)
- **Website**: [genoxholdings.com](https://genoxholdings.com)
- **Partner**: [buygit.com](https://buygit.com)

---

<div align="center">

**Built with ❤️ by [Genox](https://genoxholdings.com) & [Buygit.com](https://buygit.com) · Seoul, South Korea**

*Helping startups find opportunities worldwide, one data point at a time.*

</div>