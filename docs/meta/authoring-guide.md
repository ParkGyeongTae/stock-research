---
search:
  exclude: true
---

# 문서 작성 가이드

이 문서는 `docs/` 안에서 리서치 문서를 **쓰고 관리할 때** 지키는 규칙을 모아둡니다. 폴더 구조·파일별 역할 같은 내비게이션 정보는 사이트 첫 페이지인 [`../README.md`](../README.md)에 있습니다 — 이 문서는 그 규칙을 실행하는 방법(작성 규칙, 신규 추가 절차, 로컬 확인)만 다룹니다.

---

## ✍️ 작성 규칙

- 모든 문서는 **최상단에 `#` 제목 + `>` 한 줄 요약(투자 관점)**으로 시작
- 재무·실적 수치는 **기준 시점을 반드시 명시** (예: "FY2026 1분기 기준")
- 사실 정보(실적·인수·인물)는 **출처 링크**를 문서 하단 "참고 자료"에 남기기
- 저장소 안의 다른 문서를 링크할 땐 **폴더가 아니라 `.md` 파일을 직접** 가리키기 (`../rocket_lab/` ❌ → `../rocket_lab/01_overview.md` ✅) — 폴더 링크는 MkDocs가 해석하지 못하고 빌드 경고만 남긴 채 깨진 링크로 배포된다
- 주관적 판단(투자 결론)과 객관적 사실(재무 수치)을 **섞지 말고 구분**해서 적기
- 회계연도(FY)처럼 헷갈리는 개념은 각주로 설명 — 예: "FY2026 1분기 = 2025-11 ~ 2026-01. Synopsys는 10월 결산 회계연도로, 캘린더 연도와 어긋난다."
- 문서 맨 아래에 `*작성일: YYYY-MM-DD*` 표기 — 기존 문서를 고쳤으면 `(최종 수정일: YYYY-MM-DD)`를 덧붙이되 **날짜만 적고 무엇을 고쳤는지는 서술하지 않는다**(변경 이력은 git log가 원 출처). 다시 고칠 땐 이 날짜를 오늘 날짜로 교체할 것 — 옛 날짜나 옛 설명을 이어 붙이지 않는다. 인용된 수치를 갱신했으면 그 값을 인용하는 다른 문서(같은 폴더의 `05_financials.md`·`06_valuation.md`·`07_investment.md`, 종가가 겹치면 `09_technical_daily.md`·`10_technical_weekly.md`도)도 함께 확인

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

# 2. 파일 내용 채우기
# 3. 필요 없는 파일은 삭제 (01_overview.md는 유지 권장)

# 4. 섹터 폴더가 새로 생기는 경우, 산업 자체를 설명하는 개요 문서도 추가
cp docs/meta/.template/sector/00_overview.md docs/sectors/<sector>/00_overview.md

# 5. 09_technical_daily.md·10_technical_weekly.md(차트)를 쓸 거라면 SVG·레벨 표는 손으로 만들지 말고 생성
uv run python scripts/gen_technical_chart.py <TICKER> --name <회사명>              # 09용 (일봉·1년)
uv run python scripts/gen_technical_chart.py <TICKER> --name <회사명> --interval 1wk  # 10용 (주봉·5년)
```

**섹터 자체가 새로 생기는 경우에만** `docs/sectors/.pages`에 폴더명을 추가하는 한 단계가 더 있다(규칙은 [`../README.md`](../README.md) "📁 폴더 구조"의 `.pages` 등록 규칙 참고). 기존 섹터에 회사만 추가할 땐 필요 없다.

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

이렇게 만든 문서는 특정 회사·섹터에 종속되지 않으므로 회사 폴더가 아니라 `docs/meta/macro/`에 둡니다. `macro/`는 성격별 서브폴더(`fx/`·`rates/`·`equities/`·`commodities/`·`crypto/`)로 나뉘어 있으니 새 지표를 만들 땐 해당 서브폴더에 두세요 — 실제 예시는 [`fx/usd_krw.md`](./macro/fx/usd_krw.md)·[`rates/treasury_10y.md`](./macro/rates/treasury_10y.md)를 참고하세요.

### macro 문서 재현 파라미터

`docs/meta/macro/` 27개 문서는 §1(차트)만 스크립트로 생성하고 §3(지지/저항 표)·§4(방법론)는 두지 않기로 했다(2026-08-20) — 그래서 각 문서 안에 재생성 커맨드를 반복해서 남기지 않는다. 아래 표가 27개 전체의 티커·옵션에 대한 단일 출처다. 재생성할 땐 표의 값을 그대로 쓰고 `--close-on`엔 최신 종가 기준일을 넣는다:

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

| 문서 | 티커 | --name | 옵션 | 각주 |
|------|------|--------|------|------|
| `macro/commodities/gold.md` | `GC=F` | 금 | `--unit-label "USD/트로이온스"` | FUT |
| `macro/commodities/silver.md` | `SI=F` | 은 | `--unit-label "USD/트로이온스" --decimals 2` | FUT |
| `macro/commodities/copper.md` | `HG=F` | 구리 | `--unit-label "USD/파운드"` | FUT |
| `macro/commodities/oil_wti.md` | `CL=F` | WTI 원유 | `--unit-label "USD/배럴"` | FUT |
| `macro/commodities/natural_gas.md` | `NG=F` | 천연가스 | `--unit-label "USD/MMBtu"` | FUT |
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
| `macro/fx/eur_usd.md` | `EURUSD=X` | 유로/달러 | `--unit-label "USD/EUR"` | FX |
| `macro/fx/jpy_usd.md` | `JPY=X` | 엔/달러 | `--symbol "엔" --symbol-pos suffix --unit-label "엔"` | FX |
| `macro/fx/usd_krw.md` | `KRW=X` | 원달러 환율 | `--symbol "원" --symbol-pos suffix --unit-label "원"` | FX |
| `macro/rates/hyg.md` | `HYG` | 하이일드 회사채 ETF | (기본값) | ETF |
| `macro/rates/short_rate.md` | `^IRX` | 13주 단기금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | DISC |
| `macro/rates/tip.md` | `TIP` | 물가연동국채 ETF | (기본값) | ETF |
| `macro/rates/tlt.md` | `TLT` | 20년+ 장기국채 ETF | (기본값) | ETF |
| `macro/rates/treasury_10y.md` | `^TNX` | 미 국채 10년물 금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | YLD |
| `macro/rates/treasury_30y.md` | `^TYX` | 미 국채 30년물 금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | YLD |
| `macro/crypto/bitcoin.md` | `BTC-USD` | 비트코인 | (기본값) | BTCN |

새 macro 문서를 추가하면 이 표에 행을 하나 추가한다 — 개별 문서에는 재생성 커맨드를 남기지 않는다.

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
