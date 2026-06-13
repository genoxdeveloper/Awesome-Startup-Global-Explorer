<div align="center">
  <p>
    <a href="README.md">🇺🇸 English</a> • 
    <a href="README.ko.md">🇰🇷 한국어</a>
  </p>
</div>

<div align="center">
  <img src="https://raw.githubusercontent.com/genoxdeveloper/Startup-funding-database/main/.github/assets/logo.png" alt="Genox Logo" width="120" />
  <h1>🌍 글로벌 스타트업 생태계 탐색기</h1>
  <p><strong>전 세계 190개국 100여 개 산업의 32,500개 이상 스타트업 지원 기회를 한곳에서 탐색하세요.</strong></p>

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
서버는 `http://127.0.0.1:8000` 에서 시작됩니다.
- **메인 대시보드**: `http://127.0.0.1:8000/`
- **관리자 패널**: `http://127.0.0.1:8000/admin` (API 키 헤더가 필요하거나, `?api_key=default-insecure-admin-key-change-me` 파라미터를 추가하세요)

---

## 🤝 기여하기 (Contributing)

개발자, 스타트업 창업자, 생태계 조력자 여러분의 기여를 환영합니다!

1. 프로젝트를 Fork 합니다.
2. 새로운 기능 브랜치를 만듭니다. (`git checkout -b feature/AmazingFeature`)
3. 변경 사항을 Commit 합니다. (`git commit -m 'Add some AmazingFeature'`)
4. 브랜치에 Push 합니다. (`git push origin feature/AmazingFeature`)
5. Pull Request를 열어주세요!

---

## 🍕 개발자 야식 후원하기 (Crypto Donations)

☕ 커피 한 잔도 좋지만, 크립토는 잠들지 않죠! 이 프로젝트가 여러분의 다음 투자처를 찾는데 도움이 되었거나, 수십 시간의 노가다를 줄여주었다면 저희의 새벽 코딩에 작은 활력을 불어넣어 주세요. 보내주신 소중한 후원금은 서버 유지비와 카페인 수혈, 그리고 가끔씩 먹는 야식 피자 값으로 감사히 쓰겠습니다. 여러분의 따뜻한 마음에 진심으로 감사드립니다! 🍕

- **USDT (TRC20)**: `TFbyQEUbVJxRocXNb2jrGoJkp5SQHJ8qPv`
- **USDT (BEP20 / BSC)**: `0xB8c48E65D440fe7Ee0025ebD88Da3094272977F4`
- **BTC**: `bc1qf93535l4jqwj4gmyp8wzgdk498jndzklckgnrf`
- **ETH (ERC20)**: `0xB8c48E65D440fe7Ee0025ebD88Da3094272977F4`

---

## 🎖️ 기여자 (Contributors)

이 프로젝트를 현실로 만드는 데 도움을 준 핵심 기여자들에게 특별한 감사를 전합니다:
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
