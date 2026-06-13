<div align="center">

# 🌍 Awesome Startup Global Explorer (스타트업 글로벌 익스플로러)

**전 세계 188개국, 100개 이상의 산업군에 걸친 정부 지원금, VC, 액셀러레이터, 클라우드 지원 프로그램을 탐색하세요.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![Genox Holdings](https://img.shields.io/badge/🏢_Genox_Holdings-Official_Site-FF6F00?style=for-the-badge)](https://genoxholdings.com)

[**English**](README.md) | [**한국어**](README.ko.md) | [**中文**](README.zh_Hans.md) | [**Español**](README.es.md) | [**العربية**](README.ar.md)

*대한민국 서울의 스타트업이, 전 세계 스타트업을 위해 만들었습니다 🇰🇷*  
*오픈소스 프로젝트 by [Genox Holdings](https://genoxholdings.com)*

</div>

---

**Awesome Startup Global Explorer**에 오신 것을 환영합니다! 시드 자금이 필요한 초기 창업자부터 해외 진출과 대규모 정부 지원금을 찾는 스케일업 스타트업까지, **188개국 33,000개 이상의 글로벌 지원 기회**를 한 곳에서 찾아볼 수 있는 통합 플랫폼입니다.

![Demo Dashboard](demo_ko.png)

## 🏢 왜 이 프로젝트를 만들었나요?

저희는 대한민국 서울에 기반을 둔 스타트업([Genox Holdings](https://genoxholdings.com))입니다. 그동안 전 세계 수십 개국의 정부 포털, VC 데이터베이스, 액셀러레이터 사이트를 뒤지며 수많은 시간을 쏟았습니다. 처음에는 내부적인 필요로 이 툴을 개발했지만, **전 세계 모든 창업자는 실리콘밸리에 있지 않더라도 글로벌 기회에 접근할 권리가 있다**고 믿기에 이를 오픈소스로 공개합니다.

## 🚀 무엇을 할 수 있나요?

국경을 넘어 내게 맞는 지원 사업과 펀딩을 찾는 일은 매우 벅찬 과정입니다. 이 애플리케이션은 아래와 같은 기능으로 여러분의 짐을 덜어줍니다:

### 1. 🔍 **글로벌 지원 기회 즉시 탐색**
지속적으로 업데이트되는 방대한 데이터베이스를 제공합니다:
- **정부 지원금 (Gov Grants):** 한국의 팁스(TIPS), 미국의 SBIR, 영국의 Innovate UK, 유럽의 Horizon Europe 등
- **VC 및 액셀러레이터:** Y Combinator, Techstars, 500 Global 및 수많은 지역 마이크로 VC
- **기업형 오픈 이노베이션(OI)** 프로그램
- **클라우드 크레딧 및 혜택:** AWS Activate, Google for Startups 등
- **해외 진출 및 리로케이션:** 스타트업 비자, 테크 허브 레지던시

### 2. 🎯 **스마트 "관련도(Relevance Score)" 랭킹**
모든 프로그램이 같은 가치를 가지는 것은 아닙니다. 자체적인 `fit_score` 알고리즘을 통해 가장 활발하고 규모가 큰 최상위 프로그램을 자동으로 상단에 노출시켜, 죽은 링크나 작은 프로그램을 스크롤하며 낭비하는 시간을 줄여줍니다.

### 3. 🌐 **완벽한 다국어 번역 지원**
글로벌 스타트업 생태계가 언어 장벽으로 가로막혀서는 안 됩니다. 상단 네비게이션 바에서 클릭 한 번으로 플랫폼 전체와 33,000개 이상의 프로그램 설명을 실시간으로 번역할 수 있습니다.

### 4. 🎛️ **강력한 필터링 및 검색**
중남미의 핀테크 지원금이 필요하신가요? 아니면 아시아의 AI 액셀러레이터? 직관적인 UI를 통해 필터링하세요:
- **국가 / 지역** (188개국 혹은 원격 "Global" 프로그램)
- **카테고리** (정부 지원금, VC, 대기업 OI 등)
- **산업군** (AI, 핀테크, SaaS, 딥테크, 헬스테크, Web3, 클린테크 등)
- **마감일** (상시 모집 vs 마감일 지정)

### 5. 🔗 **지원 포털 "직접 연결"**
조건에 맞는 프로그램을 찾았다면, "Apply" 버튼을 눌러 *해당 국가의 공식 지원 포털*이나 공식 신청 페이지로 곧바로 이동할 수 있습니다.

---

## 🛠️ 기술 스택 및 아키텍처

- **Backend:** Python (Flask, SQLAlchemy)
- **Database:** SQLite (단일 트랜잭션 벌크 업데이트로 초고속 처리 보장)
- **Frontend:** HTML5, CSS3 (글래스모피즘 UI), Vanilla JavaScript
- **Translation:** Flask-Babel & `deep-translator` (Google Translate API)
- **Data Engine:** 비동기 파이썬 크롤러(`aiohttp`, `asyncio`) 및 대규모 절차적 데이터 주입 생성기

## 💻 로컬에서 실행하는 방법

1. **저장소 클론:**
   ```bash
   git clone https://github.com/genoxdeveloper/Startup-funding-database.git
   cd Startup-funding-database
   ```

2. **의존성 설치:**
   ```bash
   pip install -r requirements.txt
   ```

3. **초기화 및 실행:**
   ```bash
   python app.py
   ```
   *앱이 자동으로 데이터베이스를 초기화하고, 백그라운드에서 33,000개 이상의 레코드를 생성/수집한 후 `http://localhost:5000` 에서 서버를 시작합니다.*

---

## 💖 프로젝트 후원하기

이 프로젝트가 여러분이나 여러분의 스타트업에 도움이 되었다면 후원을 고려해 주세요! 여러분의 후원은 글로벌 스타트업 생태계를 위해 이 도구를 유지하고 개선하는 데 큰 힘이 됩니다.

<div align="center">

| 플랫폼 | 링크 |
|----------|------|
| ⭐ **저장소 Star 누르기** | 완전 무료이며, 더 많은 사람들이 이 툴을 발견하게 도와줍니다! |
| 💖 **GitHub Sponsors** | [Sponsor Genox-developer](https://github.com/sponsors/genoxdeveloper) |
| ☕ **Ko-fi** | [ko-fi.com/genoxholdings](https://ko-fi.com/genoxholdings) |
| 💎 **USDT (TRC20)** | `TUmUVHfxsFLZQToE5j4oGaPCMRKBLRjEcv` |

</div>

> ☕ **커피 한 잔 후원하기** — 후원금은 새로운 데이터를 수집하는 서버 비용으로 쓰입니다!
> 🍕 **피자 후원하기** — 원하시는 국가의 스타트업 프로그램을 우선적으로 추가해 드립니다!

⭐ 별점, 소셜 미디어 공유, 소액 후원 등 어떠한 방식의 지원이든 이 오픈소스 프로젝트를 모두에게 무료로 유지하는 데 큰 도움이 됩니다.

---

## 📧 연락처

문의, 비즈니스 제휴, 파트너십 제안은 아래로 연락해 주세요:
📧 **이메일**: [developer@genox.one](mailto:developer@genox.one)  
🏢 **웹사이트**: [genoxholdings.com](https://genoxholdings.com)

---

<div align="center">

**Built with ❤️ by [Genox Holdings](https://genoxholdings.com) · Seoul, South Korea 🇰🇷**

*전 세계 스타트업이 기회를 발견하도록 돕습니다.*

</div>
