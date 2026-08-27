# 차트 생성 가이드

이 문서는 `scripts/gen_technical_chart.py`·`scripts/gen_index_overlay_chart.py`로 캔들 차트·비교 차트를 생성할 때 지키는 규칙을 모아둡니다 — 회사 문서의 `09_technical_daily.md`·`10_technical_weekly.md`, `docs/meta/macro/`의 거시지표 문서 모두 여기 규칙을 따릅니다. 사이트 방문자용 콘텐츠가 아니라 `docs/`를 쓰고 관리하는 사람(Claude Code 등 에이전트)만 참조하는 절차서라 [`authoring-guide.md`](./authoring-guide.md)와 같은 이유로 `docs/` 밖 저장소 루트에 둡니다.

폴더 구조·명명 규칙·회사 문서 파일별 역할의 마스터는 여전히 [`authoring-guide.md`](./authoring-guide.md)입니다 — 이 문서는 그중 차트 생성이라는 한 가지 절차만 떼어내 다룹니다.

---

## 기술적 분석 차트 생성 (`09_technical_daily.md`·`10_technical_weekly.md`)

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

> 왜 스크립트로 두는가 — 좌표 매핑·스윙 탐지 창(일봉 전후 5거래일 / 주봉 전후 4주)·클러스터링 허용오차(±2.5%, 두 인터벌 공통) 같은 파라미터를 회사마다 다시 구현하면 값이 조용히 달라져 **회사 간 차트 비교가 깨집니다.** 이 파라미터의 단일 출처는 스크립트 상단 `INTERVAL_PARAMS`이며, 바꾸면 이미 만들어둔 `09_technical_daily.md`·`10_technical_weekly.md`를 전부 재생성하고 각 문서 4. 방법론 · 한계에 바뀐 값을 남겨야 합니다.

스크립트가 만드는 것은 기계적 산출물뿐입니다. 갭·급락 구간의 **해석**(3. 관측된 특이 구간), 파라미터를 기본값에서 바꾼 **사유**(4. 방법론 · 한계)는 사람이 채웁니다. 2. 지지선 / 저항선 요약 비고의 "어느 시기의 스윙대인지"는 `--emit dates`로 뽑은 날짜 목록(아래)을 그대로 옮기고, 그 시기에 무슨 일이 있었는지 같은 해석만 사람이 덧붙이면 됩니다 — 날짜 자체를 눈대중으로 채우지 않습니다:

```bash
uv run python scripts/gen_technical_chart.py SNPS --interval 1wk --emit dates
```

`--close-on`으로 뽑은 종가는 `04_metrics.md`·`06_valuation.md`의 값과 대조해 문서 상단에 결과를 남기세요.

`--emit chart` 출력(`<div class="<ticker>-chart">…</div>`)은 클래스명·범례·다크모드 CSS가 한 벌로 들어 있으니 **그대로 붙여넣고 손대지 마세요.** 특히 다크모드 CSS는 세 규칙이 한 세트입니다 — (1) 기본(라이트) 값, (2) `@media (prefers-color-scheme: dark)` 안에 `body:not([data-md-color-scheme="default"])` 가드를 건 다크 값, (3) `[data-md-color-scheme="slate"]` 다크 값. (2)의 가드를 지우면 **OS가 다크인 사용자가 사이트에서 라이트 모드를 골랐을 때 페이지는 밝은데 차트만 어둡게** 남습니다(MkDocs Material이 이때 body에 `data-md-color-scheme="default"`를 붙입니다).

`--levels` 기본값은 3이지만 **억지로 3개를 채우지 마세요** — 유효한 클러스터가 2개면 2개만 씁니다. 개수를 바꿨거나 터치 2회 미만인 레벨을 `--force-level`로 넣었다면 그 사유를 각 문서 4. 방법론 · 한계와 표 비고에 남깁니다.

## 주가가 아닌 시계열(환율·금리 등)에 쓰기

이 스크립트는 Yahoo Finance 티커라면 주가가 아니어도(`KRW=X`=원달러, `^TNX`=미 국채 10년물 등) 그대로 쓸 수 있습니다. 기본값(`$` prefix, "USD")은 주가 전용이므로 `--symbol`·`--symbol-pos`·`--unit-label`·`--adj-note`로 바꿉니다:

```bash
uv run python scripts/gen_technical_chart.py "KRW=X" --interval 1wk \
  --symbol "원" --symbol-pos suffix --unit-label "원" \
  --adj-note "환율 원자료(조정 없음)"
```

이렇게 만든 문서는 특정 회사·섹터에 종속되지 않으므로 회사 폴더가 아니라 `docs/meta/macro/`에 둡니다. 새 지표를 만들 땐 [`authoring-guide.md`](./authoring-guide.md) "📁 폴더 구조·명명 규칙"에 정리된 성격별 서브폴더(`foreign_exchange/`·`rates/`·`bonds/`·`equities/`·`metals/`·`energy/`·`cryptocurrency/`) 중 맞는 곳에 두세요 — 실제 예시는 [`foreign_exchange/usd_krw.md`](./docs/meta/macro/foreign_exchange/usd_krw.md)·[`rates/treasury_10y.md`](./docs/meta/macro/rates/treasury_10y.md)를 참고하세요.

## macro 문서의 산문은 시점에 종속되지 않게 씁니다

`docs/meta/macro/`의 문서에서 **수치·날짜·순위·기간은 스크립트 산출물(차트 SVG, 그리고 비교 문서의 `### 5년간 순변화 요약` 표)에만 둡니다.** intro 인용문과 `## 2. 해석`은 사람이 쓰는 부분이라 스크립트가 갱신해 주지 않으므로, 여기에 그 회차의 수치나 국면을 적어 두면 차트를 재생성할 때마다 손으로 다시 써야 하고 방치하면 표와 어긋납니다(2026-08-25 전체 36개 문서에 적용).

`## 2. 해석`은 "이번 구간에 무슨 일이 있었나"가 아니라 **"이 표를 어떻게 읽는가"**를 씁니다. 각 자산의 구조적 성격(듀레이션, 주가 가중, 산업 수요 vs 안전자산 등)은 바뀌지 않으므로 그대로 두되, 결과는 조건부로 서술합니다:

- ❌ `TLT가 -45.1%로 가장 크게 빠졌다 — 5년간 이어진 연준의 긴축이 반영된 결과다`
- ✅ `TLT는 듀레이션이 셋 중 가장 크다. TLT의 순변화 절대값이 나머지 둘보다 크게 벌어져 있으면 그 구간을 명목금리가 주도했다는 뜻이다`

같은 이유로 아래 표현을 쓰지 않습니다:

| 쓰지 않는 것 | 왜 |
|---|---|
| "최근", "최근 몇 년", "지금", "이 5년 동안", "지난 5년간" | 재생성하면 가리키는 시점이 달라진다 |
| intro 인용문 안의 시세·수준 (`달러인덱스 ~99` 등) | 스크립트가 갱신하지 않아 곧 틀린 값이 된다 |
| 특정 종목·기업명을 예시로 든 구성 비중 설명 ("엔비디아 같은 대형 회원사") | 지수 구성과 비중 순위는 바뀐다 |
| 5년 창(window) 안에서만 성립하는 근거 ("13주물이 2021년 한때 0%였으므로") | 창이 밀리면 근거가 사라진다 |
| 이번 회차에만 맞는 각주 ("WTI는 직전 주 종가를 쓴다") | 다음 회차엔 다른 지표가 그렇게 된다 → 조건으로 일반화한다 |

과거에 확정된 사건(비트코인 반감기 규칙, 이더리움 The Merge, 미국 현물 ETF 승인 등)은 시점이 지나도 사실이 바뀌지 않으므로 연도와 함께 적어도 됩니다 — 금지되는 것은 "그 뒤로 계속 ~해지고 있다" 같은 **진행형 서술**입니다.

## macro 문서 재현 파라미터

`docs/meta/macro/`의 단일 자산 문서(아래 표 28개)는 1. 차트만 스크립트로 생성하고 지지선 / 저항선 요약(지지/저항 표)·방법론 · 한계 절은 두지 않기로 했다(2026-08-20) — 그래서 각 문서 안에 재생성 커맨드를 반복해서 남기지 않는다. 아래 표가 전체의 티커·옵션에 대한 단일 출처다. 재생성할 땐 표의 값을 그대로 쓴다:

```bash
uv run python scripts/gen_technical_chart.py "<티커>" --name "<이름>" --interval 1wk \
  <옵션> --decimals 2 --emit chart
```

`--decimals 2`는 28개 문서 전부에 붙인다 — 기본 자동 규칙(20 이상이면 정수, 미만이면 소수 2자리)을 그대로 두면 지수·금 같은 큰 값에서 소수점이 사라져 기존 문서와 표시가 달라진다.

⚠️ **`--close-on`·`--adj-note`는 `--emit chart`에서 아무 효과가 없다** — 둘 다 `--emit all`/`--emit facts`가 만드는 방법론·데이터 블록에만 반영되는데, macro 문서는 그 절을 두지 않아 차트만 뽑기 때문이다. 그래서 재현 커맨드에서 뺐다. 아래 각주 코드표는 커맨드에 넣는 플래그가 아니라 **각 시리즈의 원자료 성격을 기록해 둔 것**이다(문서 상단 인용문에 반영할 때 참고).

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
| `macro/metals/silver.md` | `SI=F` | 은 | `--unit-label "USD/트로이온스"` | FUT |
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
| `macro/equities/vix.md` | `^VIX` | VIX 변동성지수 | `--symbol "" --unit-label "pt"` | VIXN |
| `macro/foreign_exchange/dxy.md` | `DX-Y.NYB` | 달러인덱스 | `--symbol "" --unit-label "지수"` | DXYN |
| `macro/foreign_exchange/eur_usd.md` | `EURUSD=X` | 유로/달러 환율 | `--unit-label "USD/EUR"` | FX |
| `macro/foreign_exchange/jpy_usd.md` | `JPY=X` | 엔/달러 환율 | `--symbol "엔" --symbol-pos suffix --unit-label "엔"` | FX |
| `macro/foreign_exchange/usd_krw.md` | `KRW=X` | 원/달러 환율 | `--symbol "원" --symbol-pos suffix --unit-label "원"` | FX |
| `macro/rates/treasury_13w.md` | `^IRX` | 미 국채 13주물 금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | DISC |
| `macro/rates/treasury_10y.md` | `^TNX` | 미 국채 10년물 금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | YLD |
| `macro/rates/treasury_30y.md` | `^TYX` | 미 국채 30년물 금리 | `--symbol "%" --symbol-pos suffix --unit-label "%"` | YLD |
| `macro/bonds/hyg.md` | `HYG` | 하이일드 회사채 ETF | (기본값) | ETF |
| `macro/bonds/tlt.md` | `TLT` | 20년+ 장기국채 ETF | (기본값) | ETF |
| `macro/bonds/tip.md` | `TIP` | 물가연동국채 ETF | (기본값) | ETF |
| `macro/cryptocurrency/bitcoin.md` | `BTC-USD` | 비트코인 | (기본값) | BTCN |
| `macro/cryptocurrency/ethereum.md` | `ETH-USD` | 이더리움 | (기본값) | ETHN |

새 macro 문서를 추가하면 이 표에 행을 하나 추가한다 — 개별 문서에는 재생성 커맨드를 남기지 않는다.

## 여러 자산을 겹쳐 비교하는 문서

단일 자산이 아니라 여러 자산을 "상대적으로 어느 쪽이 더 크게 움직였는지" 비교하려면 `gen_technical_chart.py`가 아니라 `gen_index_overlay_chart.py`를 쓴다. 지지/저항 레벨은 다루지 않고 1. 차트(차트+요약 표)·2. 해석만 둔다 — 단일 자산 문서와 같은 규칙이다. **모드는 자산 단위로 정한다:**

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

`--title`은 아래 표의 값을 그대로 쓰고, `--period-label`은 8개 문서 모두 `"최근 5년 주간"`이다. 스크립트가 제목 뒤에 기준일·지수화 여부를 자동으로 붙이므로 제목에 그 정보를 직접 적지 않는다.

| 문서 | 모드 | --title | 시리즈(티커:라벨:색상슬롯) |
|------|------|---------|---------------------------|
| `macro/foreign_exchange/comparison.md` | index | 통화 4종 비교 | `DX-Y.NYB:달러인덱스 (DXY):1` · `EURUSD=X:유로/달러 환율:2` · `JPY=X:엔/달러 환율:3` · `KRW=X:원/달러 환율:4` |
| `macro/rates/comparison.md` | raw (`--unit-label "%"`) | 미국 국채금리 3종 비교 | `^IRX:미국 13주물 국채금리:1` · `^TNX:미국 10년물 국채금리:2` · `^TYX:미국 30년물 국채금리:3` |
| `macro/bonds/comparison.md` | index | 채권 3종 비교 | `TLT:20년+ 장기국채 ETF (TLT):1` · `TIP:물가연동국채 ETF (TIP):2` · `HYG:하이일드 회사채 ETF (HYG):3` |
| `macro/metals/comparison.md` | index | 금속 3종 비교 | `GC=F:금:1` · `SI=F:은:2` · `HG=F:구리:3` |
| `macro/energy/comparison.md` | index | 에너지 3종 비교 | `CL=F:WTI 원유:1` · `NG=F:천연가스:2` · `SRUUF:우라늄 실물 신탁 (SRUUF):3` |
| `macro/equities/us_comparison.md` | index | 미국 4대 지수 비교 | `^GSPC:S&P 500:1` · `^IXIC:나스닥종합지수:2` · `^DJI:다우존스산업지수:3` · `^RUT:러셀2000:4` |
| `macro/equities/kr_comparison.md` | index | 코스피·코스닥 비교 | `^KS11:코스피:1` · `^KQ11:코스닥:2` |
| `macro/cryptocurrency/comparison.md` | index | 디지털자산 2종 비교 | `BTC-USD:비트코인:1` · `ETH-USD:이더리움:2` |

---

*작성일: 2026-08-22 (최종 수정일: 2026-08-25)*
