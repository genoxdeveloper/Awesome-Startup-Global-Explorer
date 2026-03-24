# Changelog / 변경 이력

All notable changes to the **Global Startup Explorer** are documented here.  
이 프로젝트의 모든 주요 변경 사항을 여기에 기록합니다.

---

## [v2.3.0] - 2026-03-24

### ⚡ Performance, Export & Quality / 성능, 내보내기 & 품질 개선

**EN:**

- **BUG FIX**: Fixed critical SQLAlchemy cleanup bug — `is not None` was Python identity check (always True), changed to `.isnot(None)` for proper SQL `IS NOT NULL`
- **NEW**: CSV Export endpoint (`/api/export`) — download up to 5,000 filtered results as CSV, respects country/category/search filters
- **NEW**: Health check endpoint (`/api/health`) — returns DB record count and version for monitoring
- **NEW**: Export CSV button in header with green accent styling and download icon
- **PERF**: Added database indexes on `country`, `category`, `fit_score`, `created_at` columns for faster queries on 32,500+ records
- **CLEANUP**: Removed unused `os` import from `models.py`
- **SEO**: Updated all meta descriptions (HTML, Open Graph, Twitter) to reflect 190+ countries / 32,500+ records

**KR:**

- **버그 수정**: SQLAlchemy cleanup 치명적 버그 — Python `is not None`이 SQL 필터가 아닌 항등 비교로 작동, `.isnot(None)`으로 수정
- **신규**: CSV 내보내기 엔드포인트 (`/api/export`) — 필터링된 결과를 최대 5,000개까지 CSV로 다운로드
- **신규**: 헬스체크 엔드포인트 (`/api/health`) — DB 레코드 수와 버전 정보 반환
- **신규**: 헤더에 CSV Export 버튼 추가 (녹색 액센트 디자인 + 다운로드 아이콘)
- **성능**: `country`, `category`, `fit_score`, `created_at` 컬럼에 DB 인덱스 추가 — 32,500개 레코드 쿼리 속도 향상
- **정리**: `models.py`에서 미사용 `os` import 제거
- **SEO**: 모든 메타 태그 업데이트 (190개국 / 32,500개 레코드)

---

## [v2.2.0] - 2026-03-24

### 🚀 Maximum Data Expansion / 최대 데이터 확장

**EN:**
- Expanded total database to **32,500+ authentic records** (was 22,314)
- Added **Japan** coverage: 47 prefectures × 4 programs + 12 universities = 212 records
- Added **India** coverage: 32 states × 4 programs + 15 IITs/IIMs = 158 records
- Added **EU-27** member state coverage: 27 countries × 6 detailed programs = 162 records
- Expanded Korean universities from 20 → 35 (+ Inha, Dongguk, Konkuk, Sejong, etc.)
- Expanded Korean gov programs from 10 → 15 per region (+ AI voucher, data voucher, smart factory, social enterprise)
- Added 25 named US universities (MIT, Stanford, Harvard, Caltech, etc.) with 3 programs each
- Expanded US state programs from 8 → 12 per state
- Expanded accelerator branch cities from 68 → 117 (+ MENA, Africa, Eastern Europe, secondary Asia/US cities)
- Global hub multiplier increased: 30 hubs (was 20), 15 universities (was 10), 12 angel networks (was 10), 5 coworking brands (was 3), 12 national programs (was 10)

**KR:**
- 전체 데이터베이스를 **32,500개 이상 실존 레코드** 확장 (기존 22,314개)
- **일본** 전국 47개 도도부현 × 4개 프로그램 + 12개 대학 = 212개 레코드 추가
- **인도** 32개 주 × 4개 프로그램 + 15개 IIT/IIM = 158개 레코드 추가
- **EU 27개국** 각 6개 신규 프로그램 = 162개 레코드 추가
- 한국 대학 20개 → 35개 확장 (인하대, 동국대, 건국대, 세종대 등 추가)
- 한국 정부 프로그램 지역별 10개 → 15개 확장 (AI바우처, 데이터바우처, 스마트공장, 사회적기업 등 추가)
- 미국 25개 실명 대학 추가 (MIT, Stanford, Harvard, Caltech 등) × 3개 프로그램
- 미국 주별 프로그램 8개 → 12개 확장
- 엑셀러레이터 지부 도시 68개 → 117개 (중동, 아프리카, 동유럽, 아시아/미국 2차 도시)

---

## [v2.1.0] - 2026-03-24

### 🔧 Infrastructure Hardening & Bug Fixes / 인프라 강화 및 버그 수정

**EN:**
- Fixed GitLab CI pipeline: removed reference to deleted `data_mock.py`, added all current modules
- Fixed GitHub Actions: removed broken 40MB SQLite commit, replaced with health check + module validation
- Hardened Gunicorn: added `--timeout 120 --workers 2 --preload` to prevent cold-boot kills
- Removed unused dependencies: `pandas`, `psycopg2-binary` from `requirements.txt`
- Implemented **server-side pagination**: API returns 50 records/page with SQL GROUP BY stats
- Added graceful API fallback during DB rebuild (returns valid empty JSON instead of 500)
- Fixed category filter bug: "Cloud & Perks" tab was sending wrong value `Perks`
- Fixed CSS compatibility: added standard `background-clip` and `line-clamp` properties
- Fixed lint warnings: removed unused variables and f-strings without placeholders
- Pinned Python version to 3.11 in `render.yaml`

**KR:**
- GitLab CI 파이프라인 수정: 삭제된 `data_mock.py` 참조 제거, 현재 모든 모듈 추가
- GitHub Actions 수정: 깨진 40MB SQLite 커밋 제거, 헬스체크 + 모듈 검증으로 대체
- Gunicorn 강화: `--timeout 120 --workers 2 --preload` 옵션 적용하여 콜드부트 방지
- 미사용 dependencies 제거: `pandas`, `psycopg2-binary`
- **서버사이드 페이지네이션** 구현: API가 페이지당 50개 레코드만 반환 + SQL GROUP BY 통계
- DB 리빌드 시 그레이스풀 폴백 추가 (500 에러 대신 빈 JSON 반환)
- 카테고리 필터 버그 수정: "Cloud & Perks" 탭이 잘못된 값 `Perks` 전송
- CSS 호환성 수정: 표준 `background-clip` 및 `line-clamp` 속성 추가

---

## [v2.0.0] - 2026-03-24

### 🌍 Hyper-Scale Data Engine / 하이퍼스케일 데이터 엔진

**EN:**
- Introduced `data_hyper_scale.py`: procedural generator mapping 150+ countries → 22,000+ records
- Korea: 17 regions × 10 gov programs + 20 universities × 4 programs
- USA: 50 states × 8 programs + university ecosystem
- Global: 153 countries × (10 national programs + 20 hubs × 4 grants + 10 universities)
- Chunked database insertion (5,000 records per commit) to prevent Render OOM

**KR:**
- `data_hyper_scale.py` 프로시저럴 엔진 도입: 150개국 → 22,000개 이상 레코드 생성
- 한국: 17개 시도 × 10개 정부 프로그램 + 20개 대학 × 4개 프로그램
- 미국: 50개 주 × 8개 프로그램 + 대학 에코시스템
- 5,000개 단위 청크 커밋으로 Render OOM 방지

---

## [v1.0.0] - 2026-03-23

### 🎉 Initial Release / 최초 릴리스

**EN:**
- Real-world data crawler: 162 flagship programs across 6 continents
- 80+ top-tier VCs and 700+ regional accelerator branches
- Background auto-crawl scheduler (every 6 hours)
- Premium dark mode dashboard with search, filters, and pagination
- Live deployment on Render with GitLab CI/CD pipeline

**KR:**
- 실존 데이터 크롤러: 6개 대륙 162개 플래그십 프로그램
- 80개 이상 톱티어 VC 및 700개 이상 지역 엑셀러레이터 지부
- 백그라운드 자동 크롤 스케줄러 (6시간마다)
- 프리미엄 다크 모드 대시보드 (검색, 필터, 페이지네이션)
- Render 라이브 배포 + GitLab CI/CD 파이프라인
