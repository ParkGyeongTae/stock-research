---
search:
  exclude: true
---

# 문서 작성 가이드

이 문서는 `docs/` 안에서 리서치 문서를 **쓰고 관리할 때** 지키는 규칙을 모아둡니다 — 폴더 구조·명명 규칙, 작성 규칙, 신규 추가 절차, 로컬 확인까지 여기서 다룹니다. 회사 폴더 안 파일별 역할(01~10 번호 체계) 같은, 사이트를 **읽는** 사람에게 필요한 안내는 사이트 첫 페이지인 [`../README.md`](../README.md)에 있습니다.

---

## 📁 폴더 구조·명명 규칙

**`sectors/` 아래에 산업/섹터 폴더**, 그 아래에 회사 폴더를 둡니다. 리서치 콘텐츠는 전부 `sectors/` 한 곳에 모여 있고, `meta/`는 콘텐츠에 종속되지 않는 참고 문서로 별도 depth에 둡니다.

```
docs/
├── .pages                 # 최상위 nav 순서 (awesome-pages 플러그인)
├── README.md              # 공통 규칙 — 사이트 첫 페이지
├── meta/                  # 특정 회사·섹터에 종속되지 않는 참고 문서 모음
│   ├── glossary.md         # PER/PBR/DCF/WACC 등 문서 전반에서 쓰는 용어 정리 (빠른 참조용)
│   ├── concepts/            # glossary.md 용어를 예시로 풀어 쓴 학습용 문서 (공부용)
│   ├── macro/               # 여러 회사 문서가 공통으로 인용하는 거시지표 차트 — 통화·금리·채권·주가지수·금속·에너지·디지털자산 서브폴더로 나뉨
│   ├── exceptions.md        # 정리 대기 중인 규칙 위반 목록 ("알려진 예외")
│   └── .template/           # 새 회사/섹터 추가 시 복사해서 쓰는 템플릿 모음 (company/·sector/)
└── sectors/               # 모든 섹터/회사 리서치 콘텐츠가 이 아래에 모임
    ├── .pages             # 섹터 nav 순서 — 새 섹터는 여기 등록해야 사이트에 노출됨 (아래 참고)
    └── <sector>/          # 섹터 폴더명은 풀어 쓴 소문자 스네이크케이스 (예: electronic_design_automation) — 그 아래에 회사별 폴더
```

- 최상위(`docs/`)는 **`README.md` + `meta/`(참고 문서) + `sectors/`(리서치 콘텐츠)**로만 구성 — 리서치 콘텐츠와 참고 문서를 같은 depth에 섞지 않는다
- `meta/` 안에서도 성격이 갈린다: **`glossary.md`·`concepts/`는 읽는 문서**, **`macro/`는 여러 회사 문서가 공통으로 인용하는 거시지표 차트**(개별 회사·섹터의 밸류에이션 판단은 담지 않음), **`.template/`은 복사해서 쓰는 스캐폴딩**, **`exceptions.md`는 정리 대기 상태를 추적하는 목록**이다 — 같은 폴더에 있는 이유는 모두 "특정 회사·섹터에 종속되지 않는다"는 기준으로 묶였기 때문이다
- `macro/` 하위는 통화·금리·채권·주가지수·금속·에너지·디지털자산 성격별 서브폴더(`fx/`·`rates/`·`bonds/`·`equities/`·`metals/`·`energy/`·`crypto/`)로 나뉜다. `rates/`는 실제 거래되는 자산이 아닌 순수 금리·수익률(%), `bonds/`는 실제 거래되는 채권 ETF 가격($)으로 갈린다. 각 문서는 `09_technical_daily.md`·`10_technical_weekly.md`와 같은 `scripts/gen_technical_chart.py`로 생성 — 작성 방법은 아래 "주가가 아닌 시계열에 쓰기" 참고
- 섹터 폴더명: **풀어 쓴 소문자 스네이크케이스** (예: `electronic_design_automation`, `semiconductor`, `cloud_infrastructure`) — 약어보다 명확한 전체 표기 우선
- 회사 폴더명: **회사명 소문자 스네이크케이스** (예: `synopsys`, `nvidia`, `apple`)
- 복합기업은 "관심 이유"가 되는 사업 기준 섹터에 배치 (예: Siemens → `sectors/electronic_design_automation/`)
- 회사 폴더를 새로 만들면 [`../README.md`](../README.md) "📄 파일별 역할" 표의 파일을 전부 채운다 — 표의 "필수 여부"는 전부 필수다.
- **`.pages` 등록 규칙 (경고 없이 조용히 실패하므로 주의):**
    - 새 **섹터 폴더** → `docs/sectors/.pages`의 `nav:`에 직접 추가해야 사이트 좌측 내비게이션에 노출된다. 등록하지 않아도 빌드는 성공하고 검색에도 잡히지만 nav에서만 사라져 사실상 링크로만 닿는 고아 페이지가 된다(에러·경고가 안 뜬다).
    - 새 **회사 폴더**(기존 섹터 안) → 등록 불필요. 자동으로 nav에 들어온다.
    - 새 **최상위 폴더**(`meta/`·`sectors/` 옆) → `docs/.pages`(최상위)에 추가해야 한다. 규칙은 섹터와 같다.
    - 새 `macro/` **하위 카테고리 폴더**(`fx/`·`rates/` 등 옆에 새 카테고리를 만드는 경우) → `docs/meta/macro/.pages`에 추가해야 한다. 기존 카테고리 안에 문서만 추가할 땐 그 카테고리의 `.pages`(예: `docs/meta/macro/fx/.pages`)에 추가한다.
- `meta/.template/` 안의 상대 링크(`../../../meta/glossary.md` 등)는 **복사된 위치**(`docs/sectors/<sector>/<company>/`) 기준으로 적혀 있음 — 템플릿 폴더에서 직접 열면 깨져 보이는 게 정상이며, 복사 후에는 맞는다. (`.template`은 앞에 점이 붙어 있어 MkDocs 빌드에서도 제외됨)

---

## ✍️ 작성 규칙

- 모든 문서는 **최상단에 `#` 제목 + `>` 한 줄 요약(투자 관점)**으로 시작
- 재무·실적 수치는 **기준 시점을 반드시 명시** (예: "FY2026 1분기 기준")
- 사실 정보(실적·인수·인물)는 **출처 링크**를 문서 하단 "참고 자료"에 남기기
- 저장소 안의 다른 문서를 링크할 땐 **폴더가 아니라 `.md` 파일을 직접** 가리키기 (`../rocket_lab/` ❌ → `../rocket_lab/01_overview.md` ✅) — 폴더 링크는 MkDocs가 해석하지 못하고 빌드 경고만 남긴 채 깨진 링크로 배포된다
- 주관적 판단(투자 결론)과 객관적 사실(재무 수치)을 **섞지 말고 구분**해서 적기
- 회계연도(FY)처럼 헷갈리는 개념은 각주로 설명 — 예: "FY2026 1분기 = 2025-11 ~ 2026-01. Synopsys는 10월 결산 회계연도로, 캘린더 연도와 어긋난다."
- 문서 맨 아래에 `*작성일: YYYY-MM-DD*` 표기 — 기존 문서를 고쳤으면 `(최종 수정일: YYYY-MM-DD)`를 덧붙이되 **날짜만 적고 무엇을 고쳤는지는 서술하지 않는다**(변경 이력은 git log가 원 출처). 다시 고칠 땐 이 날짜를 오늘 날짜로 교체할 것 — 옛 날짜나 옛 설명을 이어 붙이지 않는다. 인용된 수치를 갱신했으면 그 값을 인용하는 다른 문서(같은 폴더의 `05_financials.md`·`06_valuation.md`·`07_investment.md`, 종가가 겹치면 `09_technical_daily.md`·`10_technical_weekly.md`도)도 함께 확인

### 회사 문서 파일 규율

[`../README.md`](../README.md) "📄 파일별 역할" 표의 파일명 앞 숫자(01~10)는 **읽는 순서**(개요→역사→경영진→원자료→해석→밸류에이션→결론→뉴스로그→차트(일봉·1년)→차트(주봉·5년))를 그대로 나타낸다. 새 회사 폴더는 `meta/.template/company/`를 복사해서 만들기 때문에 숫자도 그대로 따라온다 — 기존에 이미 만들어둔 회사 폴더(번호 없는 파일명)까지 소급 적용하려면 별도로 리네이밍이 필요하다. `08_news.md`는 핵심 분석 흐름(01~07) 완성 후에 붙는 로그, `09_technical_daily.md`·`10_technical_weekly.md`는 펀더멘털 판단과 별개인 가격 패턴 참고 자료라 순서상 뒤에 두고, 그중에서도 단기(일봉)를 장기(주봉)보다 앞에 둔다.

회사마다 파일을 **똑같은 이름**으로 유지하면, 나중에 회사 간 비교가 쉬워진다.

`04_metrics.md`가 원자료의 유일한 출처다. `05_financials.md`·`06_valuation.md`·`07_investment.md`는 숫자를 다시 채우지 말고 `04_metrics.md` 값을 인용해 해석만 쓴다. `06_valuation.md`에서 미래 추정치(E)처럼 `04_metrics.md`에 아직 없는 값을 쓸 때만 그 문서에 직접 근거를 남기고, 확정치는 항상 `04_metrics.md`로 되돌아가 채운다.

같은 폴더의 다른 문서들은 서로 전부 링크하는 것(풀 메시)이 기본값이다 — 이 표의 파일은 전부 필수이므로 원칙적으로 뺄 링크가 없어야 하고, 아직 정책 적용 전인 기존 회사 폴더처럼 예외적으로 없는 문서가 있을 때만 그 링크를 뺀다.

PER·PBR·DCF·WACC·%p 등 용어가 낯설면 [`glossary.md`](./glossary.md)를 먼저 본다.

### `04_metrics.md` 절 구조

파일 표에서 셀을 얇게 유지한 대신, 절 구조는 여기 따로 둔다.

- **A. 연간 표** — 최근 3개년 + 올해(연간). 매출·영업이익·PER·PBR·순부채·EV·유동비율·부채비율·FCF·SBC·배당(DPS) 등. 평균·중앙값 비교의 기준이 된다.
- **B. 분기 표** — 최근 6개 분기. 열은 A와 동일 축이되 계절성·최근 추세를 보기 위한 별도 표.
- **C. 사업 고유 지표** — 그 사업 고유의 backlog·ARR·거래대금 등. 규칙은 아래 "사업 고유 지표" 섹션에 있다. 단순한 사업이면 이 절을 통째로 삭제하고 A절 상단 각주에 사유를 남긴다.
- **D. 판단 메모** — 표 대비 위치(peer·역사 대비)·추세를 짧게 확인한다. **왜 그런지의 서술적 해석은 여기 쓰지 말고 `05_financials.md`로.** 여기서는 "매출성장률이 최근 3분기 연속 감소" 같은 관측만 남긴다.

### 숫자를 다룰 때 반드시 지키는 것

문서 간에 숫자가 어긋나는 사고는 대부분 아래 다섯 가지에서 납니다. 정의는 [`glossary.md`](./glossary.md), 예시 풀이는 [`concepts/`](./concepts/financial-metrics.md)에 있습니다.

1. **할인율과 현금흐름의 짝** — `04_metrics.md`의 FCF(`CFO − CapEx`)는 지급이자가 이미 빠진 **Levered FCF**(≈ FCFE)다. DCF에서 이 값을 할인할 땐 **자기자본비용(Ke)**을 쓰고 순부채를 따로 빼지 않는다. WACC를 쓰려면 현금흐름을 FCFF(≈ EBIT×(1−t) + D&A − CapEx − ΔWC)로 바꾸고 마지막에 순부채를 차감해야 한다 — **섞으면 결과가 틀린다.** 정통 FCFE는 여기에 Net Borrowing(신규 차입 − 상환)을 더한 값이므로, 표 기간에 순차입이 크게 변한 회사(대규모 자사주매입용 차입, 대규모 채무상환)는 그 해만 별도 보정하거나 FCFF+WACC 프레임으로 통일하는 편이 안전하다.
2. **GAAP / Non-GAAP 구분** — 행마다 어느 기준인지 표기. 둘의 차이가 무엇으로 채워져 있는지(SBC / 인수 무형자산 상각 / 일회성)를 각주로 분해할 것. 반복되는 SBC를 "일회성 제거"로 읽지 않는다.
3. **부채총계 vs 이자부 차입금** — 이 레포의 **부채비율** = 부채총계(총자산−자기자본) ÷ 자기자본(한국 관행). **순부채·EV**는 이자부 차입금(단기+장기+리스부채) 기준. 두 값을 섞지 않는다. ⚠️ 미국 10-K의 **D/E ratio**(Debt-to-Equity)는 대개 이자부 차입금 ÷ 자기자본을 가리켜 여기 정의와 다르다 — 10-K가 보고한 D/E 값을 그대로 "부채비율" 열에 옮기지 말 것.
4. **평균·중앙값에 추정치(E)를 섞지 않는다** — 확정치만으로 계산하고, 몇 개년 기준인지 각주에 남긴다.
5. **주식분할 소급조정** — 표 기간 내 분할·병합이 있었으면 과거 전 구간(주가·EPS·BPS·DPS·주식수)을 조정 후 기준으로 맞춘다.

### 사업 고유 지표 (`04_metrics.md` C절)

표준 재무 지표만으로는 그 회사의 동력이 안 잡히는 경우가 있습니다 — 방산의 **수주잔고·book-to-bill**, 구독 소프트웨어의 **ARR·NRR·RPO**, 플랫폼의 **거래대금·테이크레이트**, 금융의 **AUC·예치금 운용수익(float)** 같은 것들입니다. 정의는 [`glossary.md`](./glossary.md) "5. 사업 모델 · 성장 지표"에 있습니다.

1. **지표는 회사가 아니라 섹터 단위로 정한다** — 같은 섹터의 모든 회사가 같은 지표를 채워야 회사 간 비교가 됩니다. 한 회사만 backlog를 기록하면 다른 회사와 나란히 놓고 비교할 수 없습니다. 섹터의 표준 지표는 첫 회사의 `04_metrics.md` C절에서 정하고, 다음 회사가 그 지표를 그대로 따릅니다.
2. **최대 5개** — 회사 IR이 자랑하는 지표를 다 옮기면 갱신이 안 돼 금방 낡습니다. "이 숫자가 나빠지면 투자 논거가 흔들리는가"로 고릅니다.
3. **정의를 반드시 병기** — 같은 이름이 회사마다 다른 것을 가리킵니다(backlog의 funded 포함 여부, ARR에 포함되는 계약 범위, NRR의 고객 수 기준 vs 금액 기준). 회사 공시 정의를 그대로 적습니다.
4. **잔고(stock)형 지표는 평균·중앙값을 내지 않는다** — backlog·AUC·이연수익처럼 "특정 시점의 잔량"은 기간 평균이 의미가 없어 해당 열을 `—`로 둡니다. book-to-bill·거래대금처럼 기간 유량(flow)인 지표만 평균을 냅니다.
5. **`glossary.md` §5에 없는 지표면 glossary를 먼저 갱신** — 회사 문서에서 용어를 새로 정의하지 않습니다.
6. 고유 지표를 따로 볼 필요가 없는 단순한 사업 구조라면 **C절을 통째로 삭제**하고 그 사유를 A절 상단 각주에 남깁니다.

### `glossary.md` · `concepts/` 작성 규칙

두 문서는 역할이 다릅니다 — **`glossary.md`는 정의, `concepts/`는 근거**입니다. 이 경계가 흐려지면 같은 내용이 두 곳에서 따로 낡고, 나중에 어디를 고쳐야 할지도 헷갈립니다.

1. **정의는 글로서리에, 예시·근거는 concepts에** — 글로서리 셀은 1~2문장(정의 + 필요하면 핵심 규칙 한 줄)으로 끝내고, "왜 그런가"나 계산 예시는 셀 안에 다시 쓰지 않습니다. concepts에 아직 근거가 없다면 먼저 그쪽에 쓰고 글로서리에서 링크합니다.
2. **1:1 매핑을 유지합니다** — `concepts/`의 파일들은 `glossary.md`의 절(§1~§10)에 정확히 대응합니다. 새 개념이 생기면 새 파일을 만들지 말고 해당 절의 파일에 `##` 절을 추가합니다.
3. **예시 수치는 반드시 검산합니다** — concepts의 "예시" 블록은 실제로 대입해 계산이 맞는지 확인한 뒤 커밋합니다. 특히 식을 거꾸로 푸는 예시(역DCF 등)는 구한 값을 원래 식에 다시 대입해 검증합니다.
4. **concepts는 평생 참고용입니다** — "2026년 현재" 같은 특정 시점 서술을 넣지 않습니다. 시점에 따라 달라지는 값(금리·물가 등)은 원출처를 가리키고 이 문서에는 적지 않습니다.

---

## ➕ 새 회사 / 새 섹터 추가 방법

```bash
# 1. 템플릿 복사
cp -r docs/meta/.template/company docs/sectors/<sector>/<company-name>

# 2. 파일 내용 채우기 — 전부 필수, 삭제하지 않는다

# 3. 섹터 폴더가 새로 생기는 경우, 산업 자체를 설명하는 개요 문서도 필수로 추가
cp docs/meta/.template/sector/00_overview.md docs/sectors/<sector>/00_overview.md

# 4. 09_technical_daily.md·10_technical_weekly.md(차트)는 SVG·레벨 표를 손으로 만들지 말고 생성
uv run python scripts/gen_technical_chart.py <TICKER> --name <회사명>              # 09용 (일봉·1년)
uv run python scripts/gen_technical_chart.py <TICKER> --name <회사명> --interval 1wk  # 10용 (주봉·5년)
```

**섹터 자체가 새로 생기는 경우에만** `docs/sectors/.pages`에 폴더명을 추가하는 한 단계가 더 있다(규칙은 위 "📁 폴더 구조·명명 규칙"의 `.pages` 등록 규칙 참고). 기존 섹터에 회사만 추가할 땐 필요 없다.

### 기술적 분석 차트 생성 (`09_technical_daily.md`·`10_technical_weekly.md`)

두 문서의 캔들 SVG·지지/저항 표·방법론 수치는 **손으로 만들지 않고** 같은 스크립트 `scripts/gen_technical_chart.py`로 생성합니다(표준 라이브러리만 쓰므로 추가 설치 불필요). `--interval`만 다르고 나머지 사용법은 동일합니다 — 기본값 `1d`는 09용(일봉·1년), `1wk`는 10용(주봉·5년)입니다.

```bash
# 09_technical_daily.md (일봉·1년)
uv run python scripts/gen_technical_chart.py SNPS --name Synopsys \
  --event 2025-09-10:"실적발표 갭다운" --ref-line 626.24:"52주 최고" \
  --force-level '366:(52주 최저)' --close-on 2026-08-13

# 10_technical_weekly.md (주봉·5년) — --interval만 추가
uv run python scripts/gen_technical_chart.py SNPS --name Synopsys --interval 1wk \
  --close-on 2026-08-13
```

> 왜 스크립트로 두는가 — 좌표 매핑·스윙 탐지 창(일봉 전후 5거래일 / 주봉 전후 4주)·클러스터링 허용오차(±2.5%, 두 인터벌 공통) 같은 파라미터를 회사마다 다시 구현하면 값이 조용히 달라져 **회사 간 차트 비교가 깨집니다.** 이 파라미터의 단일 출처는 스크립트 상단 `INTERVAL_PARAMS`이며, 바꾸면 이미 만들어둔 `09_technical_daily.md`·`10_technical_weekly.md`를 전부 재생성하고 각 문서 §4에 바뀐 값을 남겨야 합니다.

스크립트가 만드는 것은 기계적 산출물뿐입니다. 갭·급락 구간의 **해석**(§3), 파라미터를 기본값에서 바꾼 **사유**(§4)는 사람이 채웁니다. §2 비고의 "어느 시기의 스윙대인지"는 `--emit dates`로 뽑은 날짜 목록(아래)을 그대로 옮기고, 그 시기에 무슨 일이 있었는지 같은 해석만 사람이 덧붙이면 됩니다 — 날짜 자체를 눈대중으로 채우지 않습니다:

```bash
uv run python scripts/gen_technical_chart.py SNPS --interval 1wk --emit dates
```

`--close-on`으로 뽑은 종가는 `04_metrics.md`·`06_valuation.md`의 값과 대조해 문서 상단에 결과를 남기세요.

### 주가가 아닌 시계열(환율·금리 등)에 쓰기

이 스크립트는 Yahoo Finance 티커라면 주가가 아니어도(`KRW=X`=원달러, `^TNX`=미 국채 10년물 등) 그대로 쓸 수 있습니다. 기본값(`$` prefix, "USD")은 주가 전용이므로 `--symbol`·`--symbol-pos`·`--unit-label`·`--adj-note`로 바꿉니다:

```bash
uv run python scripts/gen_technical_chart.py "KRW=X" --interval 1wk \
  --symbol "원" --symbol-pos suffix --unit-label "원" \
  --adj-note "환율 원자료(조정 없음)"
```

이렇게 만든 문서는 특정 회사·섹터에 종속되지 않으므로 회사 폴더가 아니라 `docs/meta/macro/`에 둡니다. 새 지표를 만들 땐 위 "📁 폴더 구조·명명 규칙"에 정리된 성격별 서브폴더(`fx/`·`rates/`·`bonds/`·`equities/`·`metals/`·`energy/`·`crypto/`) 중 맞는 곳에 두세요 — 실제 예시는 [`fx/usd_krw.md`](./macro/fx/usd_krw.md)·[`rates/treasury_10y.md`](./macro/rates/treasury_10y.md)를 참고하세요.

### macro 문서 재현 파라미터

`docs/meta/macro/`의 단일 자산 문서(아래 표 28개)는 §1(차트)만 스크립트로 생성하고 §3(지지/저항 표)·§4(방법론)는 두지 않기로 했다(2026-08-20) — 그래서 각 문서 안에 재생성 커맨드를 반복해서 남기지 않는다. 아래 표가 전체의 티커·옵션에 대한 단일 출처다. 재생성할 땐 표의 값을 그대로 쓰고 `--close-on`엔 최신 종가 기준일을 넣는다:

```bash
uv run python scripts/gen_technical_chart.py "<티커>" --name "<이름>" --interval 1wk \
  <옵션> --adj-note "<조정 각주>" --close-on <YYYY-MM-DD> --emit chart
```

조정 각주 코드:

| 코드 | 텍스트 |
|------|--------|
| FUT | 선물 원자료(연속월물, 조정 없음) — 만기 롤오버 시 가격 갭 가능 |
| IDX | 지수 원자료(조정 없음) |
| FX | 환율 원자료(조정 없음) |
| ETF | ETF 원자료(가격 기준, 분배금 재투자 미반영 — 총수익률 아님) |
| YLD | 국채 수익률 원자료(조정 없음) |
| DISC | 13주 국채 할인율 원자료(조정 없음) |
| VIXN | VIX 지수 원자료(조정 없음) |
| DXYN | 달러인덱스 원자료(조정 없음) |
| BTCN | BTC/USD 원자료(조정 없음, 24시간 시장이라 주 마지막 거래일 기준 종가) |
| ETHN | ETH/USD 원자료(조정 없음, 24시간 시장이라 주 마지막 거래일 기준 종가) |
| URTN | 실물 우라늄 신탁 원자료(조정 없음) — 순자산가치(NAV) 대비 프리미엄/디스카운트로 거래될 수 있음 |

| 문서 | 티커 | --name | 옵션 | 각주 |
|------|------|--------|------|------|
| `macro/metals/gold.md` | `GC=F` | 금 | `--unit-label "USD/트로이온스"` | FUT |
| `macro/metals/silver.md` | `SI=F` | 은 | `--unit-label "USD/트로이온스" --decimals 2` | FUT |
| `macro/metals/copper.md` | `HG=F` | 구리 | `--unit-label "USD/파운드"` | FUT |
| `macro/energy/oil_wti.md` | `CL=F` | WTI 원유 | `--unit-label "USD/배럴"` | FUT |
| `macro/energy/natural_gas.md` | `NG=F` | 천연가스 | `--unit-label "USD/MMBtu"` | FUT |
| `macro/energy/uranium.md` | `SRUUF` | Sprott Physical Uranium Trust | (기본값) | URTN |
| `macro/equities/dow.md` | `^DJI` | 다우존스산업지수 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/hang_seng.md` | `^HSI` | 항셍지수 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/kosdaq.md` | `^KQ11` | 코스닥 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/kospi.md` | `^KS11` | 코스피 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/nasdaq.md` | `^IXIC` | 나스닥종합지수 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/nikkei225.md` | `^N225` | 닛케이225 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/russell2000.md` | `^RUT` | 러셀2000 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/sox.md` | `^SOX` | 필라델피아 반도체지수 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/sp500.md` | `^GSPC` | S&P 500 | `--symbol "" --unit-label "지수"` | IDX |
| `macro/equities/vix.md` | `^VIX` | VIX 변동성지수 | `--symbol "" --unit-label "pt" --decimals 2` | VIXN |
| `macro/fx/dxy.md` | `DX-Y.NYB` | 달러인덱스 | `--symbol "" --unit-label "지수" --decimals 2` | DXYN |
| `macro/fx/eur_usd.md` | `EURUSD=X` | 유로/달러 환율 | `--unit-label "USD/EUR"` | FX |
| `macro/fx/jpy_usd.md` | `JPY=X` | 엔/달러 환율 | `--symbol "엔" --symbol-pos suffix --unit-label "엔"` | FX |
| `macro/fx/usd_krw.md` | `KRW=X` | 원/달러 환율 | `--symbol "원" --symbol-pos suffix --unit-label "원"` | FX |
| `macro/rates/treasury_13w.md` | `^IRX` | 미 국채 13주물 금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | DISC |
| `macro/rates/treasury_10y.md` | `^TNX` | 미 국채 10년물 금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | YLD |
| `macro/rates/treasury_30y.md` | `^TYX` | 미 국채 30년물 금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | YLD |
| `macro/bonds/hyg.md` | `HYG` | 하이일드 회사채 ETF | (기본값) | ETF |
| `macro/bonds/tlt.md` | `TLT` | 20년+ 장기국채 ETF | (기본값) | ETF |
| `macro/bonds/tip.md` | `TIP` | 물가연동국채 ETF | (기본값) | ETF |
| `macro/crypto/bitcoin.md` | `BTC-USD` | 비트코인 | (기본값) | BTCN |
| `macro/crypto/ethereum.md` | `ETH-USD` | 이더리움 | (기본값) | ETHN |

새 macro 문서를 추가하면 이 표에 행을 하나 추가한다 — 개별 문서에는 재생성 커맨드를 남기지 않는다.

### 여러 자산을 겹쳐 비교하는 문서

단일 자산이 아니라 여러 자산을 "상대적으로 어느 쪽이 더 크게 움직였는지" 비교하려면 `gen_technical_chart.py`가 아니라 `gen_index_overlay_chart.py`를 쓴다. 지지/저항 레벨은 다루지 않고 §1(차트+요약 표)·§2(해석)만 둔다 — 단일 자산 문서와 같은 규칙이다. **모드는 자산 단위로 정한다:**

- `--mode index`(기본): 환율·지수처럼 **단위 자체가 서로 다른** 자산. 공통 시작일을 100으로 맞춰 상대 변화율로 겹친다.
- `--mode raw`: 국채금리처럼 **이미 같은 단위(%)인** 자산. 지수화하면 안 된다 — 기준값이 0에 가까운 시리즈가 하나라도 있으면(예: 2021년 ZIRP 시기 13주물 금리 0.04%) 지수가 수천으로 튀어 왜곡된다. 원값을 그대로 겹치면 스프레드·역전 같은 실제 정보까지 보여줘 오히려 더 유용하다.

```bash
# index 모드
uv run python scripts/gen_index_overlay_chart.py \
  --series "<티커1>:<라벨1>:<색상슬롯1>" --series "<티커2>:<라벨2>:<색상슬롯2>" ... \
  --title "<제목>" --period-label "최근 5년 주간"

# raw 모드 (같은 단위인 자산 — 예: 국채금리 %)
uv run python scripts/gen_index_overlay_chart.py --mode raw --unit-label "%" \
  --series "<티커1>:<라벨1>:<색상슬롯1>" --series "<티커2>:<라벨2>:<색상슬롯2>" ... \
  --title "<제목>" --period-label "최근 5년 주간"
```

색상슬롯은 `docs/meta/macro/`가 이미 쓰는 검증된 8색 팔레트 순번(1=파랑 2=주황 3=아쿠아 4=노랑 5=마젠타 6=초록 7=보라 8=빨강)이다 — 새 배색을 만들지 않고 그 순서를 재사용한다.

| 문서 | 모드 | 시리즈(티커:라벨:색상슬롯) |
|------|------|---------------------------|
| `macro/fx/comparison.md` | index | `DX-Y.NYB:달러인덱스 (DXY):1` · `EURUSD=X:유로/달러 환율:2` · `JPY=X:엔/달러 환율:3` · `KRW=X:원/달러 환율:4` |
| `macro/rates/comparison.md` | raw (`--unit-label "%"`) | `^IRX:미국 13주물 국채금리:1` · `^TNX:미국 10년물 국채금리:2` · `^TYX:미국 30년물 국채금리:3` |
| `macro/bonds/comparison.md` | index | `TLT:20년+ 장기국채 ETF (TLT):1` · `TIP:물가연동국채 ETF (TIP):2` · `HYG:하이일드 회사채 ETF (HYG):3` |
| `macro/metals/comparison.md` | index | `GC=F:금:1` · `SI=F:은:2` · `HG=F:구리:3` |
| `macro/energy/comparison.md` | index | `CL=F:WTI 원유:1` · `NG=F:천연가스:2` · `SRUUF:우라늄 실물 신탁 (SRUUF):3` |
| `macro/equities/us_comparison.md` | index | `^GSPC:S&P 500:1` · `^IXIC:나스닥종합지수:2` · `^DJI:다우존스산업지수:3` · `^RUT:러셀2000:4` |
| `macro/equities/kr_comparison.md` | index | `^KS11:코스피:1` · `^KQ11:코스닥:2` |
| `macro/crypto/comparison.md` | index | `BTC-USD:비트코인:1` · `ETH-USD:이더리움:2` |

### 로컬에서 확인하기

```bash
uv run mkdocs serve   # http://127.0.0.1:8000 에서 미리보기
uv run mkdocs build   # 배포와 동일하게 빌드 — 경고 메시지를 반드시 확인
```

`build` 출력에 뜨는 `unrecognized relative link` 경고는 **깨진 문서 간 링크**를 뜻한다. 깨진 링크가 있어도 빌드는 성공하고 GitHub Actions 배포도 그대로 통과하므로, 문서를 추가·이동한 뒤에는 경고가 늘지 않았는지 직접 봐야 한다. 나머지 nav 순서는 `awesome-pages` 플러그인이 `.pages` 파일과 파일명 숫자 접두사로 결정한다.

---

## 🗂 알려진 예외

위 규칙을 지키지 못한 채 "나중에 고칠 것"으로 남겨둔 항목은 이 문서가 아니라 [`exceptions.md`](./exceptions.md)에서 관리합니다 — 정리 대기 목록은 항목이 자주 추가·삭제되는데, 이 마스터 문서까지 매번 같이 건드리지 않기 위함입니다. 회사 사정상 템플릿을 벗어난 것이 오히려 맞는 경우(비상장 기간이 섞여 시장 지표를 채울 수 없다든지, Non-GAAP 대신 조정 EBITDA를 쓰는 회사)는 예외가 아니라 정상이므로, 그 목록에도 적지 말고 **그 문서 안에 왜 벗어났는지 각주로** 남기면 됩니다.

---

*작성일: 2026-08-17 (최종 수정일: 2026-08-21)*
