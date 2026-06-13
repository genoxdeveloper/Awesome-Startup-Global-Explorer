<div align="center">

# Awesome Startup Global Explorer

**Discover startup funding, grants, accelerators & cloud perks across 188+ countries and 100+ industries.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

[**English**](README.md) | [**한국어**](README.ko.md) | [**中文**](README.zh_Hans.md) | [**Español**](README.es.md) | [**العربية**](README.ar.md)

*Built for startups, by a startup in Seoul, South Korea*  
*An open-source project by**[Genox](https://genoxholdings.com)**&**[Buygit.com](https://buygit.com)***

</div>

---

글로벌 스타트업 생태계를 탐색하기 위한 궁극적인 관문인**Awesome Startup Global Explorer**에 오신 것을 환영합니다. 초기 자금 조달을 원하는 초기 단계의 창업자이든, 정부 보조금 및 최고 수준의 VC를 찾고 있는 확장 기술 회사이든, 이 플랫폼은**188개 이상의 국가에서**35,000개 이상의 자금 조달 기회**를 중앙 집중화합니다.

![데모 대시보드](demo_en.png)

## 🏢 제녹스 소개

**Genox**는 대한민국 서울에 본사를 둔 혁신적인 기술 벤처 기업입니다. 우리는 글로벌 스타트업에 힘을 실어주는 데이터 기반 솔루션과 플랫폼을 설계합니다. 우리는 기회에 대한 접근을 민주화하고, 경계를 허물고, 혁신을 가속화하는 것이 중요하다고 믿습니다.

우리는 수십 개 국가의 정부 포털, VC 데이터베이스 및 액셀러레이터 사이트를 검색하는 데 셀 수 없이 많은 시간을 보냈습니다. 우리는 먼저 이 도구를 내부적으로 구축했으며 이제는 실리콘 밸리의 창업자뿐만 아니라**모든 창업자가 글로벌 기회에 접근할 자격이 있기 때문에**이제 오픈 소스화하고 있습니다.

## 🚀 이 사이트에서 무엇을 할 수 있나요?

적절한 자금이나 지원 프로그램을 찾는 것은 특히 국경을 넘어 살펴볼 때 부담스러울 수 있습니다. 이 애플리케이션은 다음과 같은 어려운 작업을 수행하여 이 문제를 해결합니다.

### 1. 즉시 글로벌 펀딩을 알아보세요
지속적으로 업데이트되는 대규모 데이터베이스를 살펴보세요.
-**정부 보조금**(예: 미국의 SBIR, Innovate UK, 한국의 K-Startup, Horizon Europe)
-**VC 및 액셀러레이터**(Y Combinator, Techstars, 500 Global 및 수천 개의 지역 마이크로 VC)
-**기업 개방형 혁신(OI)**프로그램
-**클라우드 크레딧 및 혜택**(AWS Activate, Google for Startups)
-**이전 및 성장**이니셔티브(스타트업 비자, 기술 허브 레지던시)

### 2. 기본 다국어 지원(국경 허물기)
우리는 차세대 대형 유니콘이 어디에서나 나올 수 있다는 것을 알고 있습니다. 그러나 역사적으로 글로벌 스타트업 생태계는 심각한 언어 장벽으로 인해 중요한 자금 조달 포털, 보조금 세부 정보, VC 투자 논문이 영어나 현지 방언으로 묻혀 있는 경우가 많았습니다. 어떤 창립자도 뒤쳐지지 않도록 하기 위해 우리 플랫폼은 믿을 수 없을 만큼 강력하고 업계 최고의**네이티브 다국어 지원 시스템**을 갖추고 있습니다.

상단 탐색 모음을 한 번만 클릭하면**35,000개 이상의 깊게 중첩된 프로그램 설명, 기준 및 동적 데이터베이스 항목**을 포함하여 전체 플랫폼을 다음으로 원활하게 변환할 수 있습니다.
- 🇺🇸**영어**(범용 기본값)
- instagram**한국어(한국어)**(아시아 태평양 허브)
- 🇨🇳**中文(중국어)**(중화권 및 SEA 생태계)
- 🇪🇸**Español(스페인어)**(호황을 누리고 있는 라틴 아메리카 및 이베리아 시장)
- 🇦🇪**العربية (아랍어)**(빠르게 성장하는 MENA 스타트업 생태계)
*(그리고 우리는 계속해서 더 많은 것을 추가하기 위해 노력하고 있습니다!)*

**이것이 왜 혁명적인가?**
대부분의 시작 데이터베이스는 실제 데이터(가장 중요한)를 원래 언어로 남겨두고 정적 UI(버튼, 메뉴)만 번역합니다. 우리 플랫폼은**이중 엔진 번역 아키텍처**를 사용하여 이 문제를 해결합니다.
1.**정적 UI 현지화:**'Flask-Babel'을 기반으로 사전 컴파일된 '.po' 및 '.mo' 메시지 카탈로그를 사용하여 모든 구조적 요소, 탐색 및 핵심 UX가 대기 시간 없이 완벽하게 현지화되도록 보장합니다.
2.**동적 데이터 번역:**'deep-translator'를 활용하는 비동기 파이프라인으로 구동됩니다. 언어를 전환하면 당사 시스템은 SQLite 데이터베이스에서 구조화되지 않은 라이브 프로그램 설명을 가져와 즉석에서 번역하여 정확한 데이터 스키마, 마크다운 형식 및 중요한 자금 조달 기준을 유지합니다.

이는 보고타, 리야드 또는 서울의 창업자가 미국 SBIR 보조금의 복잡한 규정 준수 요구 사항이나 런던 기반 VC 네트워크의 투자 논문을 샌프란시스코의 창업자처럼 쉽게 모국어로 읽을 수 있음을 의미합니다. 이는 국경을 넘는 모금 활동의 마찰을 완전히 제거합니다.

![한국어 보기 데모](demo_ko.png)

### 3. 스마트 '관련성 점수' 순위
모든 프로그램이 동일하게 만들어지는 것은 아닙니다. 우리의 맞춤형 'fit_score' 알고리즘은 기회를 평가하고 자동으로 최상위 계층, 가장 활동적인 프로그램을 맨 위로 표시하므로 데드 링크를 스크롤하는 데 시간을 낭비하지 않습니다.

### 4. 강력한 필터링 및 검색
라틴 아메리카에서 FinTech 보조금이 필요하십니까? 아니면 아시아의 AI 가속기인가요? 직관적인 UI를 사용하여 국가/지역, 카테고리, 산업 및 마감일별로 필터링하세요.

### 5. 직접 "적용" 포털
완벽하게 일치하는 것을 찾으면 "적용"을 클릭하여 공식 지원 포털로 *직접* 이동하세요.

---

## 💻 기술 스택 및 아키텍처

-**백엔드:**Python(Flask, SQLAlchemy)
-**데이터베이스:**SQLite(초확장성 단일 트랜잭션 대량 업데이트)
-**프런트엔드:**HTML5, CSS3(사용자 정의 바닐라 CSS, Glassmorphism UI), 바닐라 JavaScript
-**번역:**실시간 비동기 번역을 위한 Flask-Babel 및 `deep-translator`(Google 번역 API)
-**데이터 엔진:**대규모 하이퍼스케일 데이터 주입을 위해 절차적 생성을 활용하는 비동기 Python 크롤러(`aiohttp`, `asyncio`).

## 🛠️ 로컬로 실행하는 방법

1.**저장소 복제:**
   ``배쉬
   자식 클론 https://github.com/genoxdeveloper/Awesome-Startup-Global-Explorer.git
   CD Awesome-스타트업-글로벌-탐색기
   ````

2.**설치 종속성:**
   ``배쉬
   pip 설치 -r 요구사항.txt
   ````

3.**초기화 및 실행:**
   ``배쉬
   파이썬 app.py
   ````
   *앱이 자동으로 데이터베이스를 초기화하고, 백그라운드 데이터 생성을 시작하고(35,000개 이상의 레코드 시드) `http://localhost:5000`에서 로컬 서버를 호스팅합니다.*

## 📊 데이터베이스 보기
원시 데이터를 선호하는 사용자를 위해 우리는 CRM 또는 추적 도구에 대한 직접 CSV 내보내기를 지원하는 초고속 DataTables 통합 기능을 갖춘 테이블 형식의**데이터베이스**모드를 제공합니다.

![데이터베이스 보기](demo_db.png)

---

## 💖 이 프로젝트 및 파트너 지원

이 프로젝트가 귀하 또는 귀하의 스타트업에 도움이 되었다면 지원해 보세요! 귀하의 지원은 글로벌 스타트업 커뮤니티를 위해 이 도구를 유지하고 개선하는 데 도움이 됩니다.

<div align="center">

| Platform | Link |
|----------|------|
| ⭐**Star this repo**| It's free and helps others discover this tool! |
| 🤝**Buygit.com**| Check out our partner [Buygit.com](https://buygit.com) |
| 💼**GitHub Sponsors**| [Sponsor Genox-developer](https://github.com/sponsors/genoxdeveloper) |
| ☕**Ko-fi**         | [ko-fi.com/genoxholdings](https://ko-fi.com/genoxholdings) |
| 🪙**USDT (TRC20)**  | `TUmUVHfxsFLZQToE5j4oGaPCMRKBLRjEcv` |

</div>

>**커피 한 잔 사주세요**— 커피 한 잔은 데이터 소스를 하나 더 크롤링하는 데 도움이 됩니다!  
>**우리에게 피자를 사주세요**— 그러면 다음으로 귀하 국가의 스타트업 프로그램을 추가해 드리겠습니다!

스타, 소셜 미디어 공유, 소액 기부 등 여러분의 지원은 이 프로젝트를 모든 사람에게 무료로 유지하는 데 큰 도움이 됩니다.

---

## 🤝 기여하기
우리는 전 세계 창립자와 개발자의 기여를 환영합니다! 목록에 없지만 해당 국가의 보조금, VC 또는 액셀러레이터를 알고 있는 경우 이슈를 열거나 Pull Request를 제출하세요.

## 📬연락처

질문, 비즈니스 문의 또는 파트너십 제안의 경우:
-**이메일**: [developer@genox.one](mailto:developer@genox.one)  
-**웹사이트**: [genoxholdings.com](https://genoxholdings.com)
-**파트너**: [buygit.com](https://buygit.com)

---

<div align="center">

**[Genox](https://genoxholdings.com) 및 [Buygit.com](https://buygit.com) · 대한민국 서울의 ❤️으로 제작됨**

*한 번에 하나의 데이터 포인트로 스타트업이 전 세계에서 기회를 찾을 수 있도록 지원합니다.*

</div>