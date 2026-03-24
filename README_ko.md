<div align="center">

# 🌍 Global Startup Explorer

**100개국 이상, 100개 산업 분야의 스타트업 펀딩·지원금·액셀러레이터·클라우드 혜택을 한눈에 탐색하세요.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

[![Live Demo](https://img.shields.io/badge/🌐_라이브_데모-바로가기-00C853?style=for-the-badge)](https://global-startup-explorerglobal-startup.onrender.com)
[![Genox Holdings](https://img.shields.io/badge/🏢_Genox_Holdings-공식_사이트-FF6F00?style=for-the-badge)](https://genoxholdings.com)

<br/>

*서울 기반 스타트업 🇰🇷 [Genox Holdings](https://genoxholdings.com)가 만든 오픈소스 프로젝트입니다.*

[🌐 라이브 데모](https://global-startup-explorerglobal-startup.onrender.com) · [🏢 Genox Holdings](https://genoxholdings.com) · [시작하기](#-시작하기) · [주요 기능](#-주요-기능) · [배포 방법](#-배포-방법) · [후원하기](#-후원하기)

</div>

---

## 📖 소개

**Global Startup Explorer**는 전 세계 스타트업 생태계의 기회를 한곳에 모아놓은 오픈소스 웹 대시보드입니다. 정부 지원금, VC 프로그램, 액셀러레이터, 기업 오픈이노베이션, 클라우드/인프라 혜택을 검색하고 필터링할 수 있습니다.

### 왜 만들었나요?

서울에 기반을 둔 스타트업 [Genox Holdings](https://genoxholdings.com)로서, 수십 개국의 정부 포털, VC 데이터베이스, 액셀러레이터 사이트를 하나하나 검색하며 시간을 보냈습니다. 내부 도구로 먼저 만들고, 이제 오픈소스로 공개합니다. **모든 창업자가 글로벌 기회에 접근할 수 있어야 한다고** 믿기 때문입니다.

---

## ✨ 주요 기능

| 기능 | 설명 |
|------|------|
| 🌐 **100+ 국가** | 미국, 영국, EU, 싱가포르, 일본, 한국, 인도, UAE, 브라질, 나이지리아 등 |
| 🏭 **100+ 산업** | AI/ML, 핀테크, 바이오테크, 클린테크, 에듀테크, 우주기술, 농식품 등 |
| 🏛 **정부 지원금** | SBIR/STTR(미국), Innovate UK, Horizon Europe, TIPS(한국), MAFF(일본) 등 |
| 🚀 **VC & 액셀러레이터** | Y Combinator, Techstars, 500 Global, Sequoia, Plug and Play 등 |
| 🏢 **기업 오픈이노베이션** | SAP.io, Microsoft for Startups, Google for Startups, Samsung NEXT 등 |
| ☁️ **클라우드 & 혜택** | AWS Activate, Google Cloud 크레딧, Azure 크레딧, OpenAI, Anthropic 등 |
| 🔍 **스마트 검색** | 제목, 제공기관, 설명 전체 텍스트 검색 |
| 📊 **적합도 점수** | 모든 기회를 0-100으로 순위화 |
| 🤖 **자동 크롤러** | 6시간마다 신규 데이터 자동 수집 |
| 📄 **페이지네이션** | 수천 건의 데이터를 부드럽게 페이지네이션 |
| 🎨 **다크 모드 UI** | 프리미엄 다크 테마 |

---

## 🚀 시작하기

### 필요 환경

- **Python 3.11+** (3.9 이상도 가능)
- **pip** (Python 패키지 매니저)
- **Git**

### 빠른 시작 (로컬)

```bash
# 1. 레포지토리 클론
git clone https://github.com/Genox-developer/global-startup-dashboard.git
cd global-startup-dashboard

# 2. 가상환경 생성 (권장)
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. 의존성 설치
pip install -r requirements.txt

# 4. 앱 실행
python app.py

# 5. 브라우저에서 확인
# http://localhost:5000 접속
```

첫 실행 시 자동으로 **4,800건 이상**의 글로벌 기회 데이터가 시드됩니다.

---

## 🏗 아키텍처

```
global-startup-dashboard/
├── app.py                      # Flask 메인 애플리케이션
├── models.py                   # SQLAlchemy 데이터베이스 모델
├── data_mock.py                # 초기 데이터 생성기 (4,800+ 레코드)
├── startup_crawler_global.py   # 자동 크롤러 (SBIR, Innovate UK 등)
├── templates/
│   └── index.html              # 싱글 페이지 대시보드 UI
├── Dockerfile                  # Docker 컨테이너 설정
├── docker-compose.yml          # Docker Compose 설정
├── Procfile                    # PaaS 배포 (Heroku, Render 등)
└── requirements.txt            # Python 의존성
```

---

## 🌐 배포 방법

Python을 지원하는 곳이라면 어디든 배포 가능합니다.

### 방법 1: Render.com (무료, 추천)

1. 이 레포지토리를 GitHub에서 **Fork**
2. [render.com](https://render.com) 가입 (무료)
3. **"New Web Service"** 클릭
4. GitHub 레포 연결
5. 설정:
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. **Deploy** 클릭 — 약 2분 후 라이브!

### 방법 2: Railway.app

1. [railway.app](https://railway.app) 접속
2. **"Deploy from GitHub"** → Fork된 레포 선택
3. Railway가 Python을 자동 감지하고 배포

### 방법 3: Docker (자체 호스팅)

```bash
# Docker Compose 사용 (가장 쉬움)
docker-compose up -d

# 또는 직접 빌드
docker build -t startup-explorer .
docker run -p 5000:5000 startup-explorer
```

### 방법 4: VPS (DigitalOcean, AWS EC2 등)

```bash
git clone https://github.com/Genox-developer/global-startup-dashboard.git
cd global-startup-dashboard
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

### 환경 변수

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `DATABASE_URL` | 데이터베이스 연결 문자열 | `sqlite:///instance/global_data.db` |
| `PORT` | 서버 포트 | `5000` |

---

## 🧩 API 엔드포인트

| 엔드포인트 | 메서드 | 설명 |
|-----------|--------|------|
| `/` | GET | 대시보드 UI |
| `/api/data` | GET | 기회 조회 (`country`, `industry`, `category`, `search` 파라미터 지원) |
| `/api/refresh` | POST | 수동 리크롤 실행 |

---

## 🤝 기여하기

커뮤니티의 기여를 환영합니다! 새로운 데이터 소스 추가, UI 개선, 버그 수정 등 어떤 것이든 좋습니다.

1. 이 레포지토리를 **Fork**
2. 기능 브랜치 생성 (`git checkout -b feature/새기능`)
3. 변경사항 커밋 (`git commit -am '새 데이터 소스 추가'`)
4. 브랜치에 Push (`git push origin feature/새기능`)
5. **Pull Request** 오픈

---

## ☕ 후원하기

이 프로젝트가 도움이 되셨다면 후원을 고려해 주세요! 후원금은 글로벌 스타트업 커뮤니티를 위한 유지보수와 개선에 사용됩니다.

<div align="center">

| 플랫폼 | 링크 |
|--------|------|
| ⭐ **스타 찍기** | 무료이며 다른 사람이 이 도구를 발견하는 데 도움이 됩니다! |
| 🎗 **GitHub Sponsors** | [GitHub에서 후원](https://github.com/sponsors/Genox-developer) |
| ☕ **Ko-fi** | [ko-fi.com/genoxholdings](https://ko-fi.com/genoxholdings) |
| 🪙 **USDT (TRC20)** | `TUmUVHfxsFLZQToE5j4oGaPCMRKBLRjEcv` |

</div>

> ☕ **커피 한 잔 사주기** — 한 잔마다 새로운 데이터 소스를 크롤링할 수 있어요!
>
> 🍕 **피자 한 판 사주기** — 여러분 나라의 스타트업 프로그램을 다음에 추가하겠습니다!

---

## 📬 문의

질문, 비즈니스 문의, 파트너십 제안:

📧 **이메일**: [developer@genox.one](mailto:developer@genox.one)

🌐 **웹사이트**: [genoxholdings.com](https://genoxholdings.com)

---

## 📄 라이선스

이 프로젝트는 **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** 라이선스로 배포됩니다.

**비상업적 목적에 한해** 자유롭게 사용, 수정, 공유할 수 있습니다. 상업적 사용은 엄격히 금지됩니다. 상업 라이선스 문의: [developer@genox.one](mailto:developer@genox.one)

---

<div align="center">

**Built with ❤️ by [Genox Holdings](https://genoxholdings.com) · Seoul, South Korea 🇰🇷**

*전 세계 스타트업이 기회를 찾을 수 있도록, 하나의 데이터 포인트씩.*

</div>
