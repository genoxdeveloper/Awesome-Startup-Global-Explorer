<div align="center">

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

![Global Startup Ecosystem Explorer Demo](./demo.png)

<details>
<summary><b>🇰🇷 한국어로 읽기 (Click to read in Korean)</b></summary>
<br>

<div align="center">
  <h1>🌍 글로벌 스타트업 생태계 탐색기</h1>
  <p><strong>전 세계 190개국 100여 개 산업의 32,500개 이상 스타트업 지원 기회를 한곳에서 탐색하세요.</strong></p>
</div>

![Global Startup Ecosystem Explorer Demo](./demo.png)

---

## ✨ 핵심 기능

- **🌐 17개 언어 완벽 지원**: 영어, 한국어, 일본어, 중국어(간체/번체), 스페인어, 프랑스어, 독일어, 이탈리아어, 포르투갈어, 아랍어, 힌디어, 러시아어, 터키어, 인도네시아어, 베트남어, 태국어를 UI 및 DB 단위로 완벽하게 지원합니다.
- **🚀 32,500개 이상의 지원 기회**: 정부 지원금, 기업형 액셀러레이터, VC, 클라우드 크레딧, 해외 진출(Relocation) 프로그램을 자동으로 크롤링하여 제공합니다.
- **⚡ 비동기 크롤링 엔진**: 백그라운드에서 실시간으로 글로벌 소스에서 데이터를 수집하여 메인 스레드를 막지 않습니다.
- **🔒 관리자 대시보드**: 크롤러 소스를 관리하고, API를 테스트하며 데이터를 안전하게 검토할 수 있습니다.
- **☁️ 1-Click 무료 호스팅 지원**: Vercel, Railway, Render 등에 추가 설정 없이 바로 배포할 수 있는 설정 파일이 포함되어 있습니다.
- **📄 CSV 내보내기**: 원하는 필터로 정리된 데이터를 오프라인 분석을 위해 즉시 다운로드할 수 있습니다.

---

## 🛠️ 간편 설치 안내 (무료 호스팅)

이 플랫폼은 별도의 비용 없이 아래 서비스 중 하나를 선택해 즉시 배포할 수 있습니다.

### 옵션 1: Vercel (추천)
1. 본인의 GitHub 계정으로 이 저장소를 Fork 하거나 클론합니다.
2. [Vercel](https://vercel.com/)에 로그인 후 **Add New Project**를 클릭합니다.
3. `Startup-funding-database` 저장소를 선택하여 Import 합니다.
4. Vercel이 자동으로 `vercel.json`을 인식하여 배포를 준비합니다.
5. **Deploy** 버튼을 누르면 끝입니다!

### 옵션 2: Render
1. [Render](https://render.com/)에 로그인합니다.
2. **New +** 버튼을 누르고 **Web Service**를 선택합니다.
3. GitHub 계정을 연결하고 이 저장소를 선택합니다.
4. 내장된 `render.yaml` 설정 파일이 자동 적용됩니다.
5. **Create Web Service**를 클릭하세요.

### 옵션 3: Railway
1. [Railway](https://railway.app/)에 로그인합니다.
2. **New Project** → **Deploy from GitHub repo**를 선택합니다.
3. 이 저장소를 선택합니다.
4. Railway가 자동으로 `Procfile`을 인식하여 의존성을 설치하고 배포를 시작합니다.
5. **Deploy**를 누르세요.

---

## 💻 로컬 개발 환경 구성

### 1. 저장소 클론
```bash
git clone https://github.com/genoxdeveloper/Startup-funding-database.git
cd Startup-funding-database
```

### 2. 가상 환경 생성
```bash
# Windows 환경
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux 환경
python3 -m venv venv
source venv/bin/activate
```

### 3. 의존성 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 애플리케이션 실행
```bash
python app.py
```
서버는 `http://127.0.0.1:5000` 에서 시작됩니다.
- **데이터 실시간 갱신**: 메인 창 상단의 **Recrawl** 버튼을 클릭하여 백그라운드에서 데이터를 최신으로 갱신할 수 있습니다.

---

## 🤝 기여하기 (Contributing)

개발자, 스타트업 창업자, 생태계 조력자 여러분의 기여를 환영합니다!
1. 프로젝트를 Fork 합니다.
2. 새로운 기능 브랜치를 만듭니다. (`git checkout -b feature/AmazingFeature`)
3. 변경 사항을 Commit 합니다. (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 Push 합니다. (`git push origin feature/AmazingFeature`)
5. Pull Request를 열어주세요!

</details>

---

## ✨ Features

- **🌐 17 Languages Supported**: Native UI and data translations for English, 한국어, 日本語, 简体中文, 繁體中文, Español, Français, Deutsch, Italiano, Português, العربية, हिन्दी, Русский, Türkçe, Bahasa Indonesia, Tiếng Việt, and ไทย.
- **🚀 32,500+ Opportunities**: Automatically crawled database of Gov Grants, Corporate Accelerators, VCs, Cloud Perks, and Relocation programs.
- **⚡ Async Crawling**: Real-time background data fetching from global sources without blocking the main thread.
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
The server will start at `http://127.0.0.1:5000`. 
- **Main Dashboard**: `http://127.0.0.1:5000/`
- **Recrawl Functionality**: Click the **Recrawl** button at the top of the main dashboard to run the background web crawler and refresh startup funding data.
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

## 📜 License & Usage Rights

**Genox Non-Commercial Open Source License**

This project is open-source but specifically restricted against commercial monetization.

**✅ You are PERMITTED to:**
- Use the code, data, and software for personal, educational, or internal testing purposes.
- Fork the repository.
- Contribute features or bug fixes back to the project via Pull Requests.

**🚫 You are STRICTLY PROHIBITED from:**
- Using the software or its data for any commercial purposes.
- Selling, monetizing, or distributing the software for financial gain.
- Offering this software as a paid SaaS (Software as a Service) to external customers.

Ownership of the intellectual property remains strictly with **Genox Holdings**. Please see the full [LICENSE](LICENSE) file for complete legal details.

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
