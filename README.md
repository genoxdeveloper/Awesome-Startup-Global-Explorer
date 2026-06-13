# 🌍 Global Startup Funding Database 🚀

<div align="center">
  <img src="https://img.shields.io/github/stars/genoxdeveloper/Startup-funding-database?style=social" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/genoxdeveloper/Startup-funding-database?style=social" alt="GitHub forks"/>
  <img src="https://img.shields.io/github/license/genoxdeveloper/Startup-funding-database" alt="License"/>
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python Version"/>
  <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintained"/>
</div>

<p align="center">
  <strong>The Ultimate 100% Free, Automated Database for Startup Grants, VCs, and Corporate Innovation Programs.</strong>
</p>

---

## 🌟 Why Star This Repository?

If you are a **Founder, Investor, or Ecosystem Builder**, starring this repository ensures you stay updated on the latest global funding opportunities.

- 📈 **Continuous Updates:** We regularly integrate new crawlers for Global VCs, accelerators (YC, Techstars), and government grants.
- 💡 **AI Matchmaking (Coming Soon):** Future updates will feature AI-driven fit scoring for startups based on their profile.
- 🤝 **Community-Driven:** Join a fast-growing community of founders seeking non-dilutive capital and venture backing.

⭐ **Please consider starring the repo to support the open-source startup ecosystem!** ⭐

---

## 🚀 Features

- **32,500+ Opportunities:** Aggregates funding data from global government portals, massive VC databases, and corporate innovation sectors.
- **Multilingual Support (17 Languages):** Fully localized interface supporting English, Korean (한국어), Japanese (日本語), Chinese (中文), Spanish (Español), French (Français), German (Deutsch), Arabic (العربية), Hindi (हिन्दी), and more!
- **Automated Crawlers:** Built-in multi-threaded crawlers sync the latest data automatically in the background.
- **Premium "Serious Dark" UI:** Optimized for modern, fast, and accessible user experience without heavy frontend frameworks.
- **Zero-Cost Deployment:** Run it on the cloud for absolutely free (see guides below).

---

## 🌐 Supported Languages
The app automatically detects your browser language or can be forced via the URL (e.g., `/?lang=ko`).

`English (en)` | `Korean (ko)` | `Japanese (ja)` | `Chinese Simplified (zh_Hans)` | `Chinese Traditional (zh_Hant)` | `Spanish (es)` | `French (fr)` | `German (de)` | `Italian (it)` | `Portuguese (pt)` | `Russian (ru)` | `Arabic (ar)` | `Hindi (hi)` | `Turkish (tr)` | `Indonesian (id)` | `Vietnamese (vi)` | `Thai (th)`

---

## ⚡ 1-Click Free Deployment

You can deploy this application for free on popular cloud platforms. The repo includes all necessary configuration files out of the box!

### 🚂 Deploy on Railway (Recommended)
Railway reads the included `Procfile` and `requirements.txt` automatically.
1. Sign up on [Railway.app](https://railway.app/).
2. Click **New Project** -> **Deploy from GitHub repo**.
3. Select this repository. Railway will build and deploy the app instantly.

### ▲ Deploy on Vercel
Vercel is optimized for Serverless functions. This repo includes a ready-to-use `vercel.json`.
1. Sign up on [Vercel.com](https://vercel.com).
2. Click **Add New** -> **Project**.
3. Import this repository.
4. Keep the framework preset to "Other" and deploy.

### ☁️ Deploy on Render
Render reads the `render.yaml` infrastructure-as-code file.
1. Sign up on [Render.com](https://render.com).
2. Click **New** -> **Blueprint**.
3. Connect your GitHub and select this repository.
4. Render will provision the free web service automatically.

---

## 💻 Local Installation

Want to run it locally or contribute? It takes less than 2 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/genoxdeveloper/Startup-funding-database.git
cd Startup-funding-database

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the application
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 🛡️ Admin Dashboard
To monitor the background crawlers or trigger manual synchronization, navigate to:
`http://127.0.0.1:5000/admin`
*Requires an Admin API Key configured in your environment or prompted on load.*

---

## 🤝 Contributing
Pull requests are welcome! If you know a great public startup database or VC list, feel free to contribute a new crawler script in the `startup_crawler_global.py` file.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

<div align="center">
  <b>Built with ❤️ by the Genox Holdings Team for the Global Founder Community.</b><br>
  <a href="https://genoxholdings.com">genoxholdings.com</a>
</div>
