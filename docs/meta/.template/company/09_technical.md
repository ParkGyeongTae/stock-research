# <회사명> (<한글명>) — 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `05_metrics.md`의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API에서 직접 수집한 것이다(1년 일봉은 `05_metrics.md`가 다루는 범위 밖이라 단일 출처 규칙의 예외). 대신 **두 문서에서 겹치는 시점의 종가를 반드시 대조하고 그 결과를 여기 적을 것** — 예: `<YYYY-MM-DD>` 종가 `$<X>`는 [`06_valuation.md`](./06_valuation.md)에 인용된 `<출처>` 값과 일치. 어긋나면 어느 쪽이 수정주가(배당·분할 반영)인지부터 확인한다.

> ⚠️ 상장 후 거래일이 6개월 미만이거나 유동성이 극히 얕은 종목은 스윙 클러스터가 표본 부족으로 무의미해진다 — 그럴 땐 이 문서를 만들지 말거나, 기간을 실제 거래 구간으로 줄이고 §4에 그 사실을 남길 것.

<!--
────────────────────────────────────────────────────────────────────────
차트 생성 절차 (작성이 끝나면 이 주석 블록은 통째로 삭제할 것)

1) 데이터 수집 — 일봉 OHLCV, 최근 1년(약 250 거래일).
   예: https://query1.finance.yahoo.com/v8/finance/chart/<TICKER>?range=1y&interval=1d
   수집한 원자료는 저장소에 커밋하지 않는다(스크래치 디렉터리에서 처리).
   수정주가(adjusted)인지 원주가인지 확인하고 §4 "데이터"에 명시한다.

2) 좌표 매핑 — viewBox "0 0 1200 680", 플롯 영역 x:60~1052, y:56~626.
   p_min = 기간 최저가 − (최고−최저)×0.05,  p_max = 기간 최고가 + (최고−최저)×0.05
   scale = (626 − 56) / (p_max − p_min)                     [px per USD]
   y(p)  = 626 − (p − p_min) × scale
   step  = (1052 − 60 − 4) / (N − 1)                        [N = 거래일 수]
   x(i)  = 62 + i × step
   body_w = clamp(step × 0.62, 1.6, 6)
   캔들 = 심지 <line x1=x(i) y1=y(high) x2=x(i) y2=y(low)> + 몸통 <rect
   x=x(i)−body_w/2, y=y(max(open,close)), height=max(|y(open)−y(close)|, 1.0)>
   색: 종가 ≥ 시가면 var(--up), 아니면 var(--down).
   가로 그리드는 눈금이 5~8개 나오는 라운드 단위(10/25/50/100 등)로.
   x축 눈금·라벨은 각 월의 첫 거래일 위치에 "YY-MM" 형식으로.

3) 스윙 포인트 — 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저와 같으면
   스윙 고점/저점. 창 크기를 바꿨으면 §4에 바꾼 값을 적는다.

4) 클러스터링 — 스윙 포인트를 가격 오름차순 정렬 후, 기존 클러스터 중심과
   ±2.5% 이내면 합치고 중심 재계산. 터치 2회 이상인 클러스터만 선으로 그린다
   (터치 1회라도 52주 최고/최저처럼 의미가 뚜렷하면 예외로 표시하고 비고에 사유).
   현재가 위쪽은 저항(R1,R2,…), 아래쪽은 지지(S1,S2,…)로 현재가에서 가까운 순 번호.

5) 라벨 겹침 — 우측 라벨(x=1058)은 12px 이상 벌린다. 두 레벨이 가까워 겹치면
   한쪽 라벨을 위/아래로 옮기고, 클러스터 자체를 합치지는 말 것.

6) 클래스명 — 아래 `.<ticker>-chart`의 `<ticker>`를 소문자 티커로 치환(예: snps-chart).
   다크 모드는 `prefers-color-scheme`와 `[data-md-color-scheme="slate"]`(MkDocs Material
   테마 토글) 양쪽을 모두 정의해야 한다 — 한쪽만 두면 토글 시 글자가 안 보인다.
────────────────────────────────────────────────────────────────────────
-->

---

## 1. 차트 — 최근 1년 일봉 (<YYYY-MM-DD> ~ <YYYY-MM-DD>)

<div class="<ticker>-chart">
<style>
.<ticker>-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .<ticker>-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .<ticker>-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.<ticker>-chart svg { width:100%; height:auto; display:block; }
.<ticker>-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.<ticker>-chart .title { fill: var(--ink); font-weight:600; }
.<ticker>-chart .grid { stroke: var(--grid); stroke-width:1; }
.<ticker>-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="<회사명>(<TICKER>) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18"><회사명> (<TICKER>) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)"><YYYY-MM-DD> ~ <YYYY-MM-DD> · 마지막 종가 $<X> (<YYYY-MM-DD>) · 단위 USD</text>

<!-- (a) 가격 그리드 — 라운드 단위마다 반복 -->
<line x1="60" y1="<y(price)>" x2="1052" y2="<y(price)>" class="grid"/>
<text x="52" y="<y(price)+4>" font-size="11" text-anchor="end" fill="var(--muted)"><price></text>

<!-- (b) x축 월 눈금 — 각 월 첫 거래일마다 반복 -->
<line x1="<x(i)>" y1="626.0" x2="<x(i)>" y2="631.0" class="axis"/>
<text x="<x(i)>" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)"><YY-MM></text>

<!-- (c) 축선 -->
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>

<!-- (d) 참고선 — 52주 최고/최저 등, 현재 레짐과 단절돼 지지/저항으로 보기 어려운 수준 (없으면 삭제) -->
<line x1="60" y1="<y(ref)>" x2="1052" y2="<y(ref)>" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="<y(ref)+3>" font-size="10.5" fill="var(--muted)">$<X> 52주 최고</text>

<!-- (e) 이벤트 수직선 — 실적발표 갭 등 §3에서 다루는 날짜만 (없으면 삭제) -->
<line x1="<x(i)>" y1="56.0" x2="<x(i)>" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="<x(i)+6>" y="68.0" font-size="10.5" fill="var(--down)"><YYYY-MM-DD> <이벤트 요약></text>

<!-- (f) 캔들 — 거래일 수만큼 반복 (양봉 예시 / 음봉은 var(--down)) -->
<line x1="<x(i)>" y1="<y(high)>" x2="<x(i)>" y2="<y(low)>" stroke="var(--up)" class="wick"/>
<rect x="<x(i)-body_w/2>" y="<y(max(open,close))>" width="<body_w>" height="<몸통 높이>" fill="var(--up)"/>

<!-- (g) 저항선 — R1부터 위로 반복. 라벨은 선 위쪽(y-6) 또는 아래쪽(y+3.5)에 배치 -->
<line x1="60" y1="<y(R)>" x2="1052" y2="<y(R)>" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="<y(R)+3.5>" font-size="11.5" fill="var(--resistance)" font-weight="600">$<X> R1</text>
<text x="1058" y="<y(R)+15.5>" font-size="9.5" fill="var(--muted)">터치 <n>회</text>

<!-- (h) 지지선 — S1부터 아래로 반복 -->
<line x1="60" y1="<y(S)>" x2="1052" y2="<y(S)>" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="<y(S)-6>" font-size="11.5" fill="var(--support)" font-weight="600">$<X> S1</text>
<text x="1058" y="<y(S)+6>" font-size="9.5" fill="var(--muted)">터치 <n>회</text>

<!-- (i) 마지막 종가 마커 -->
<circle cx="1052.0" cy="<y(마지막 종가)>" r="3" fill="var(--ink)"/>

<!-- (j) 범례 -->
<rect x="60" y="651" width="10" height="10" fill="var(--up)"/>
<text x="74" y="660" font-size="11" fill="var(--ink2)">상승(양봉)</text>
<rect x="150" y="651" width="10" height="10" fill="var(--down)"/>
<text x="164" y="660" font-size="11" fill="var(--ink2)">하락(음봉)</text>
<line x1="240" y1="656" x2="258" y2="656" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="264" y="660" font-size="11" fill="var(--ink2)">지지선(Support)</text>
<line x1="390" y1="656" x2="408" y2="656" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="414" y="660" font-size="11" fill="var(--ink2)">저항선(Resistance)</text>
</svg>
</div>

---

## 2. 지지선 / 저항선 요약

각 레벨은 "전후 <n>거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±<n>% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $ |  | <어느 시기의 스윙 고점대인지> |
| R2 | $ |  |  |
| R1 | $ |  |  |
| **현재가** | **$<X>** (<YYYY-MM-DD> 종가) | — | R1과 S1 사이 |
| S1 | $ |  | <현재가에 가장 근접한 지지> |
| S2 | $ |  |  |
| S3 | $ |  |  |
| 참고선 | $ | — | <52주 최고/최저 등 — 왜 근시일 지지/저항으로 보지 않는지> |

> 레벨 개수는 3개로 고정하지 말 것 — 유효한 클러스터가 2개면 2개만 쓰고, 억지로 채우지 않는다. 반대로 5개 이상 잡히면 터치 횟수가 많은 것부터 남기고 나머지는 생략한 사유를 각주로 남긴다.

---

## 3. 관측된 특이 구간 — <YYYY-MM-DD> <이벤트명>

<실적 발표 갭·인수 발표·규제 이슈 등 가격대가 구조적으로 재설정된 구간이 있으면 기록. 없으면 이 절을 통째로 삭제할 것>

- <이벤트 발생 시점과 계기. 관련 항목이 [`08_news.md`](./08_news.md) 로그에 있으면 링크>
- 종가 기준 전일 대비 **<±X>%** ($<전일 종가> → $<당일 종가>), 거래량은 평소(일 <X>만 주 내외) 대비 약 <n>배인 **<X>만 주**.
- <이 사건 이후 거래 레짐이 어떻게 달라졌는지 — 이전 스윙 레벨을 §2에서 참고선으로만 처리했다면 그 사유>

---

## 4. 방법론 · 한계

- **데이터**: <출처> 일봉 OHLCV(Open/High/Low/Close/Volume), <N>개 거래일, <YYYY-MM-DD>~<YYYY-MM-DD>. 수집 시점: <YYYY-MM-DD>. <수정주가(배당·분할 반영) 여부 명시>
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 <n>거래일(총 <2n+1>거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±<n>% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(<n>거래일)·허용오차(±<n>%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 <N>개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - <뉴스 이벤트로 인한 불연속 구간이 있으면 그 한계도 여기 적을 것(§3)>
    - <해당 기간에 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트가 있었다면 소급 조정 여부를 명시>

---

## 관련 문서

같은 폴더 내 다른 문서로 이동 (없는 문서는 링크 제거):

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [재무 / 실적](./04_financials.md)
- [핵심 지표](./05_metrics.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)

---

## 참고 자료

- [<일봉 OHLCV 원자료 출처>]() (수집 <YYYY-MM-DD>)
- [<주가 이력 대조용 출처>]()

---

*작성일: YYYY-MM-DD*
