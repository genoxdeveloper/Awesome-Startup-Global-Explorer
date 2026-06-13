<div align="center">
  <p>
    <a href="README.md">🇺🇸 English</a> • 
    <a href="README.ko.md">🇰🇷 한국어</a>
  </p>
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/genoxdeveloper/Startup-funding-database/main/.github/assets/logo.png" alt="Genox Logo" width="120" />
  <h1>🌍 Global Startup Ecosystem Explorer</h1>
  <p><strong>A comprehensive database of 32,500+ global startup opportunities across 190+ countries and 100+ industries.</strong></p>

  <p>
    <a href="https://github.com/genoxdeveloper/Startup-funding-database/stargazers"><img src="https://img.shields.io/github/stars/genoxdeveloper/Startup-funding-database?style=for-the-badge&color=f59e0b" alt="Stars"/></a>
    <a href="https://github.com/genoxdeveloper/Startup-funding-database/network/members"><img src="https://img.shields.io/github/forks/genoxdeveloper/Startup-funding-database?style=for-the-badge&color=3b82f6" alt="Forks"/></a>
    <a href="https://github.com/genoxdeveloper/Startup-funding-database/issues"><img src="https://img.shields.io/github/issues/genoxdeveloper/Startup-funding-database?style=for-the-badge&color=ef4444" alt="Issues"/></a>
    <a href="https://github.com/genoxdeveloper/Startup-funding-database/blob/main/LICENSE"><img src="https://img.shields.io/github/license/genoxdeveloper/Startup-funding-database?style=for-the-badge&color=10b981" alt="License"/></a>
    <br>
    <a href="https://github.com/sponsors/genoxdeveloper"><img src="https://img.shields.io/badge/Sponsor-GitHub-ea4aaa?style=for-the-badge&logo=github" alt="GitHub Sponsor"/></a>
  </p>
</div>

---

## ✨ Features

- **🌐 17 Languages Supported**: Native UI and data translations for English, 한국어, 日本語, 简体中文, 繁體中文, Español, Français, Deutsch, Italiano, Português, العربية, हिन्दी, Русский, Türkçe, Bahasa Indonesia, Tiếng Việt, and ไทย.
- **🚀 32,500+ Opportunities**: Automatically crawled database of Gov Grants, Corporate Accelerators, VCs, Cloud Perks, and Relocation programs.
- **⚡ Async Crawling**: Real-time background data fetching from global sources without blocking the main thread.
- **🔒 Admin Dashboard**: Manage crawler sources, test APIs, and review data securely.
- **☁️ 1-Click Free Hosting Ready**: Out-of-the-box configurations for Vercel, Railway, and Render.
- **📄 Export to CSV**: Download filtered datasets instantly for offline analysis.

---

## 🛠️ Quick Installation (Free Hosting)

Deploy this platform for **free** using one of the following providers. Configuration files are already included!

### Option 1: Vercel (Recommended)
1. Fork or clone this repository to your GitHub account.
2. Sign in to [Vercel](https://vercel.com/) and click **Add New Project**.
3. Import your `Startup-funding-database` repository.
4. Vercel will automatically detect the `vercel.json` and deploy the Python (Flask) app using serverless functions.
5. Click **Deploy**.

### Option 2: Render
1. Sign in to [Render](https://render.com/).
2. Click **New +** and select **Web Service**.
3. Connect your GitHub account and select this repository.
4. Render will automatically use the `render.yaml` configuration.
5. Click **Create Web Service**.

### Option 3: Railway
1. Sign in to [Railway](https://railway.app/).
2. Click **New Project** → **Deploy from GitHub repo**.
3. Select this repository.
4. Railway will automatically detect the `Procfile` and install dependencies.
5. Click **Deploy**.

---

## 💻 Local Development

### 1. Clone the repository
```bash
git clone https://github.com/genoxdeveloper/Startup-funding-database.git
cd Startup-funding-database
```

### 2. Create a virtual environment
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```
The server will start at `http://127.0.0.1:8000`. 
- **Main Dashboard**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin` (Requires API Key header or query parameter `?api_key=default-insecure-admin-key-change-me`)

---

## 🌎 Supported Translations

Powered by `flask-babel` and `deep-translator`, we offer true localized experiences for the startup community globally:
🇺🇸 English | 🇰🇷 Korean | 🇯🇵 Japanese | 🇨🇳 Chinese (Simplified/Traditional) | 🇪🇸 Spanish | 🇫🇷 French | 🇩🇪 German | 🇮🇹 Italian | 🇵🇹 Portuguese | 🇸🇦 Arabic | 🇮🇳 Hindi | 🇷🇺 Russian | 🇹🇷 Turkish | 🇮🇩 Indonesian | 🇻🇳 Vietnamese | 🇹🇭 Thai

*(Translations map automatically detects browser language or can be set manually via the dropdown).*

---

## 🤝 Contributing

We welcome contributions from developers, startup founders, and ecosystem builders! 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🍕 Fuel Our Late-Night Coding (Crypto Donations)

☕ Coffee is great, but crypto never sleeps! If this project helped you find your next big investment or saved you dozens of hours of manual research, consider fueling our late-night coding sessions. A tiny drop of crypto helps us keep the servers running and the bugs at bay. We promise to spend it on server costs, caffeine, and maybe a pizza. Thank you for your kindness! 🍕

- **USDT (TRC20)**: `TFbyQEUbVJxRocXNb2jrGoJkp5SQHJ8qPv`
- **USDT (BEP20 / BSC)**: `0xB8c48E65D440fe7Ee0025ebD88Da3094272977F4`
- **BTC**: `bc1qf93535l4jqwj4gmyp8wzgdk498jndzklckgnrf`
- **ETH (ERC20)**: `0xB8c48E65D440fe7Ee0025ebD88Da3094272977F4`

---

## 🎖️ Contributors

A special thanks to our core contributors who made this project possible:
- **@genoxdeveloper**
- **@claude**
- **@gemini**

---

<div align="center">
  <p><strong>Built with ❤️ by the Genox Holdings Team for the Global Founder Community.</strong></p>
  <p>© 2026 Genox 제녹스. All rights reserved.</p>
  <p>
    <a href="https://buygit.com">buygit.com</a> • 
    <a href="https://genoxholdings.com">genoxholdings.com</a> • 
    <a href="mailto:admin@genox.one">admin@genox.one</a> • 
    <a href="mailto:support@buygit.com">support@buygit.com</a>
  </p>
  <p>Seoul, South Korea</p>
</div>
