# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉 데이터는 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 겹치는 시점의 종가 세 개를 대조했고 모두 **일치**했다 — `2025-12-31`(FY2025 회계연도 말) $193.56은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md) 2. 최근 3개년 — 적정주가 vs 실제주가의 값과, `2026-08-25` $366.43은 [개요](./01_overview.md)·[밸류에이션 / 적정주가](./06_valuation.md)의 현재주가와, `2026-08-14` $418.79는 직전 회차 문서들이 기준으로 삼았던 값과 각각 같다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-26 ~ 2026-08-25)

<div class="ter-chart">
<style>
.ter-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ter-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ter-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ter-chart svg { width:100%; height:auto; display:block; }
.ter-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ter-chart .title { fill: var(--ink); font-weight:600; }
.ter-chart .grid { stroke: var(--grid); stroke-width:1; }
.ter-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Teradyne(TER) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Teradyne (TER) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-26 ~ 2026-08-25 · 마지막 종가 $366.43 (2026-08-25) · 단위 USD</text>
<line x1="60" y1="619.0" x2="1052" y2="619.0" class="grid"/>
<text x="52" y="623.0" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="478.2" x2="1052" y2="478.2" class="grid"/>
<text x="52" y="482.2" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="337.5" x2="1052" y2="337.5" class="grid"/>
<text x="52" y="341.5" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="196.7" x2="1052" y2="196.7" class="grid"/>
<text x="52" y="200.7" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="77.8" y1="626.0" x2="77.8" y2="631.0" class="axis"/>
<text x="77.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="160.8" y1="626.0" x2="160.8" y2="631.0" class="axis"/>
<text x="160.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="251.7" y1="626.0" x2="251.7" y2="631.0" class="axis"/>
<text x="251.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="326.8" y1="626.0" x2="326.8" y2="631.0" class="axis"/>
<text x="326.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="413.7" y1="626.0" x2="413.7" y2="631.0" class="axis"/>
<text x="413.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="492.8" y1="626.0" x2="492.8" y2="631.0" class="axis"/>
<text x="492.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="567.9" y1="626.0" x2="567.9" y2="631.0" class="axis"/>
<text x="567.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="654.8" y1="626.0" x2="654.8" y2="631.0" class="axis"/>
<text x="654.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="737.8" y1="626.0" x2="737.8" y2="631.0" class="axis"/>
<text x="737.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="816.8" y1="626.0" x2="816.8" y2="631.0" class="axis"/>
<text x="816.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="899.8" y1="626.0" x2="899.8" y2="631.0" class="axis"/>
<text x="899.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="986.8" y1="626.0" x2="986.8" y2="631.0" class="axis"/>
<text x="986.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="496.7" y1="56.0" x2="496.7" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="502.7" y="68.0" font-size="10.5" fill="var(--down)">2026-02-03 FY2025 4분기 실적 서프라이즈</text>
<line x1="729.9" y1="56.0" x2="729.9" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="735.9" y="68.0" font-size="10.5" fill="var(--down)">2026-04-29 Q1 2026 실적 호조에도 보수적 가이던스로 급락</text>
<line x1="62.0" y1="591.1" x2="62.0" y2="595.5" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="592.8" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="65.9" y1="592.6" x2="65.9" y2="595.1" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="592.6" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="69.9" y1="592.6" x2="69.9" y2="595.0" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="593.8" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="73.8" y1="590.5" x2="73.8" y2="594.4" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="591.6" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="77.8" y1="589.4" x2="77.8" y2="598.6" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="590.0" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="81.7" y1="587.8" x2="81.7" y2="593.1" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="589.7" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="85.7" y1="590.8" x2="85.7" y2="596.4" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="591.7" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="89.6" y1="586.0" x2="89.6" y2="591.7" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="590.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="93.6" y1="589.0" x2="93.6" y2="594.2" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="590.5" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="97.5" y1="590.8" x2="97.5" y2="598.3" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="592.2" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="101.5" y1="593.5" x2="101.5" y2="600.5" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="593.9" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="105.5" y1="592.5" x2="105.5" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="593.9" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="109.4" y1="597.6" x2="109.4" y2="605.5" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="597.9" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="113.4" y1="598.9" x2="113.4" y2="603.6" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="599.2" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="117.3" y1="597.0" x2="117.3" y2="600.1" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="598.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="121.3" y1="596.0" x2="121.3" y2="600.9" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="598.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="125.2" y1="591.5" x2="125.2" y2="597.7" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="592.5" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="129.2" y1="590.0" x2="129.2" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="591.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="133.1" y1="569.0" x2="133.1" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="569.5" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="137.1" y1="565.1" x2="137.1" y2="572.3" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="568.3" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="141.0" y1="570.2" x2="141.0" y2="575.3" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="570.4" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="145.0" y1="572.3" x2="145.0" y2="578.7" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="572.7" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="148.9" y1="568.4" x2="148.9" y2="574.8" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="569.3" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="152.9" y1="566.5" x2="152.9" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="566.7" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="156.8" y1="565.3" x2="156.8" y2="572.5" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="566.0" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="160.8" y1="560.5" x2="160.8" y2="568.6" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="561.1" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="164.7" y1="555.1" x2="164.7" y2="560.2" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="555.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="168.7" y1="549.4" x2="168.7" y2="555.9" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="553.6" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="172.6" y1="547.6" x2="172.6" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="551.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="176.6" y1="548.2" x2="176.6" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="549.9" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="180.5" y1="555.8" x2="180.5" y2="562.4" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="556.2" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="184.5" y1="555.0" x2="184.5" y2="560.1" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="555.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="188.4" y1="551.4" x2="188.4" y2="574.3" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="554.5" width="2.45" height="19.3" fill="var(--down)"/>
<line x1="192.4" y1="562.8" x2="192.4" y2="567.5" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="563.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="196.4" y1="564.2" x2="196.4" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="566.9" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="200.3" y1="560.7" x2="200.3" y2="565.9" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="561.2" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="204.3" y1="558.4" x2="204.3" y2="565.2" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="559.9" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="208.2" y1="563.1" x2="208.2" y2="567.2" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="565.3" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="212.2" y1="560.6" x2="212.2" y2="564.5" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="561.5" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="216.1" y1="556.6" x2="216.1" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="558.0" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="220.1" y1="558.8" x2="220.1" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="560.5" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="224.0" y1="554.1" x2="224.0" y2="565.5" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="555.6" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="228.0" y1="550.0" x2="228.0" y2="556.9" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="552.0" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="231.9" y1="548.5" x2="231.9" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="551.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="235.9" y1="551.9" x2="235.9" y2="556.9" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="552.7" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="239.8" y1="510.3" x2="239.8" y2="531.5" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="514.9" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="243.8" y1="507.5" x2="243.8" y2="518.1" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="510.8" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="247.7" y1="498.1" x2="247.7" y2="509.2" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="503.9" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="251.7" y1="499.9" x2="251.7" y2="506.1" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="502.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="255.6" y1="503.1" x2="255.6" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="511.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="259.6" y1="493.8" x2="259.6" y2="511.3" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="495.7" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="263.5" y1="490.1" x2="263.5" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="495.5" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="267.5" y1="502.9" x2="267.5" y2="513.6" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="503.2" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="271.4" y1="494.1" x2="271.4" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="494.6" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="275.4" y1="501.6" x2="275.4" y2="512.5" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="501.6" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="279.3" y1="504.6" x2="279.3" y2="510.3" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="506.1" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="283.3" y1="510.6" x2="283.3" y2="523.8" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="511.7" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="287.3" y1="515.1" x2="287.3" y2="530.0" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="520.5" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="291.2" y1="515.7" x2="291.2" y2="528.2" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="522.6" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="295.2" y1="524.2" x2="295.2" y2="530.3" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="526.8" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="299.1" y1="519.9" x2="299.1" y2="530.6" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="522.9" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="303.1" y1="515.1" x2="303.1" y2="542.0" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="517.2" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="307.0" y1="533.6" x2="307.0" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="536.1" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="311.0" y1="523.8" x2="311.0" y2="535.2" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="526.1" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="314.9" y1="523.1" x2="314.9" y2="534.0" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="523.7" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="318.9" y1="505.1" x2="318.9" y2="522.1" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="507.2" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="322.8" y1="503.3" x2="322.8" y2="507.1" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="503.7" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="326.8" y1="502.3" x2="326.8" y2="509.1" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="506.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="330.7" y1="490.2" x2="330.7" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="492.4" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="334.7" y1="483.6" x2="334.7" y2="493.7" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="485.1" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="338.6" y1="477.0" x2="338.6" y2="488.1" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="480.2" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="342.6" y1="473.8" x2="342.6" y2="479.6" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="477.1" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="346.5" y1="471.2" x2="346.5" y2="476.1" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="473.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="350.5" y1="475.6" x2="350.5" y2="481.0" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="477.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="354.4" y1="471.6" x2="354.4" y2="479.9" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="472.6" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="358.4" y1="472.6" x2="358.4" y2="483.9" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="472.6" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="362.3" y1="475.0" x2="362.3" y2="489.7" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="476.4" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="366.3" y1="477.5" x2="366.3" y2="487.3" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="478.3" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="370.2" y1="484.7" x2="370.2" y2="493.5" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="486.1" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="374.2" y1="485.9" x2="374.2" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="486.7" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="378.2" y1="485.1" x2="378.2" y2="493.3" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="488.8" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="382.1" y1="483.2" x2="382.1" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="485.0" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="386.1" y1="475.4" x2="386.1" y2="482.6" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="476.7" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="390.0" y1="479.2" x2="390.0" y2="484.4" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="480.3" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="394.0" y1="478.7" x2="394.0" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="480.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="397.9" y1="479.0" x2="397.9" y2="482.8" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="479.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="401.9" y1="479.5" x2="401.9" y2="484.4" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="481.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="405.8" y1="480.8" x2="405.8" y2="485.3" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="481.0" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="409.8" y1="480.6" x2="409.8" y2="487.5" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="481.4" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="413.7" y1="465.8" x2="413.7" y2="479.3" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="467.6" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="417.7" y1="447.3" x2="417.7" y2="461.6" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="450.8" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="421.6" y1="436.5" x2="421.6" y2="450.6" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="437.6" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="425.6" y1="440.6" x2="425.6" y2="451.0" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="442.2" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="429.5" y1="448.1" x2="429.5" y2="460.4" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="448.1" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="433.5" y1="450.9" x2="433.5" y2="456.2" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="453.9" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="437.4" y1="441.3" x2="437.4" y2="454.9" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="443.9" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="441.4" y1="435.5" x2="441.4" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="437.0" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="445.3" y1="434.4" x2="445.3" y2="443.6" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="435.7" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="449.3" y1="423.4" x2="449.3" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="427.3" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="453.2" y1="433.1" x2="453.2" y2="442.1" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="436.5" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="457.2" y1="437.3" x2="457.2" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="444.5" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="461.1" y1="429.2" x2="461.1" y2="442.0" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="433.3" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="465.1" y1="424.7" x2="465.1" y2="441.2" stroke="var(--down)" class="wick"/>
<rect x="463.87" y="425.0" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="469.1" y1="435.7" x2="469.1" y2="444.2" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="437.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="473.0" y1="428.9" x2="473.0" y2="440.2" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="433.5" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="477.0" y1="421.9" x2="477.0" y2="428.4" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="423.4" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="480.9" y1="406.2" x2="480.9" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="407.2" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="484.9" y1="402.8" x2="484.9" y2="422.3" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="405.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="488.8" y1="400.5" x2="488.8" y2="423.6" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="410.1" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="492.8" y1="401.3" x2="492.8" y2="421.0" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="408.5" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="496.7" y1="357.2" x2="496.7" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="361.4" width="2.45" height="34.9" fill="var(--up)"/>
<line x1="500.7" y1="343.8" x2="500.7" y2="389.3" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="360.4" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="504.6" y1="363.7" x2="504.6" y2="390.6" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="378.1" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="508.6" y1="335.5" x2="508.6" y2="364.2" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="337.3" width="2.45" height="26.0" fill="var(--up)"/>
<line x1="512.5" y1="314.2" x2="512.5" y2="342.4" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="323.4" width="2.45" height="17.2" fill="var(--up)"/>
<line x1="516.5" y1="320.8" x2="516.5" y2="338.2" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="323.4" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="520.4" y1="301.9" x2="520.4" y2="322.1" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="307.3" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="524.4" y1="298.1" x2="524.4" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="302.7" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="528.3" y1="311.9" x2="528.3" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="316.8" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="532.3" y1="315.0" x2="532.3" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="328.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="536.2" y1="306.8" x2="536.2" y2="330.9" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="316.6" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="540.2" y1="311.8" x2="540.2" y2="324.8" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="315.1" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="544.1" y1="299.5" x2="544.1" y2="314.6" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="302.5" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="548.1" y1="304.4" x2="548.1" y2="322.8" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="310.3" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="552.0" y1="291.9" x2="552.0" y2="314.1" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="296.5" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="556.0" y1="276.0" x2="556.0" y2="294.3" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="277.2" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="560.0" y1="274.3" x2="560.0" y2="297.4" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="275.8" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="563.9" y1="302.3" x2="563.9" y2="323.4" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="303.7" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="567.9" y1="301.0" x2="567.9" y2="323.3" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="301.1" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="571.8" y1="322.0" x2="571.8" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="325.5" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="575.8" y1="316.4" x2="575.8" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="321.3" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="579.7" y1="322.9" x2="579.7" y2="348.9" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="329.6" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="583.7" y1="344.4" x2="583.7" y2="380.9" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="347.1" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="587.6" y1="342.5" x2="587.6" y2="389.5" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="342.5" width="2.45" height="43.7" fill="var(--up)"/>
<line x1="591.6" y1="323.7" x2="591.6" y2="344.6" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="336.4" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="595.5" y1="319.7" x2="595.5" y2="338.1" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="334.7" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="599.5" y1="342.8" x2="599.5" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="343.8" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="603.4" y1="343.7" x2="603.4" y2="359.2" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="351.6" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="607.4" y1="330.4" x2="607.4" y2="345.0" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="339.9" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="611.3" y1="337.9" x2="611.3" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="338.3" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="615.3" y1="326.5" x2="615.3" y2="342.4" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="333.0" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="619.2" y1="331.5" x2="619.2" y2="360.8" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="334.1" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="623.2" y1="333.3" x2="623.2" y2="358.8" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="334.5" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="627.1" y1="317.1" x2="627.1" y2="337.5" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="332.0" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="631.1" y1="298.9" x2="631.1" y2="340.3" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="309.1" width="2.45" height="28.3" fill="var(--up)"/>
<line x1="635.0" y1="301.2" x2="635.0" y2="318.5" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="302.3" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="639.0" y1="316.4" x2="639.0" y2="342.2" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="316.4" width="2.45" height="24.8" fill="var(--down)"/>
<line x1="642.9" y1="334.1" x2="642.9" y2="347.1" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="343.7" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="646.9" y1="336.1" x2="646.9" y2="375.4" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="336.1" width="2.45" height="34.7" fill="var(--down)"/>
<line x1="650.9" y1="341.2" x2="650.9" y2="368.5" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="342.5" width="2.45" height="25.6" fill="var(--up)"/>
<line x1="654.8" y1="313.8" x2="654.8" y2="337.1" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="320.3" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="658.8" y1="318.5" x2="658.8" y2="351.6" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="324.0" width="2.45" height="27.6" fill="var(--up)"/>
<line x1="662.7" y1="315.2" x2="662.7" y2="329.1" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="315.8" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="666.7" y1="308.1" x2="666.7" y2="324.0" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="308.7" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="670.6" y1="254.9" x2="670.6" y2="281.2" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="255.4" width="2.45" height="20.1" fill="var(--up)"/>
<line x1="674.6" y1="239.5" x2="674.6" y2="256.9" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="247.1" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="678.5" y1="234.7" x2="678.5" y2="245.3" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="237.6" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="682.5" y1="238.4" x2="682.5" y2="250.2" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="238.8" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="686.4" y1="239.0" x2="686.4" y2="249.5" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="243.8" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="690.4" y1="241.5" x2="690.4" y2="264.4" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="246.1" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="694.3" y1="239.9" x2="694.3" y2="255.6" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="244.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="698.3" y1="222.8" x2="698.3" y2="237.4" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="224.4" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="702.2" y1="217.9" x2="702.2" y2="234.7" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="221.1" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="706.2" y1="214.4" x2="706.2" y2="230.6" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="225.0" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="710.1" y1="209.7" x2="710.1" y2="230.0" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="212.4" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="714.1" y1="189.9" x2="714.1" y2="211.7" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="195.3" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="718.0" y1="165.6" x2="718.0" y2="195.1" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="171.3" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="722.0" y1="166.6" x2="722.0" y2="211.8" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="166.6" width="2.45" height="27.4" fill="var(--down)"/>
<line x1="725.9" y1="201.9" x2="725.9" y2="232.4" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="212.2" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="729.9" y1="288.2" x2="729.9" y2="334.9" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="317.0" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="733.8" y1="262.1" x2="733.8" y2="299.9" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="276.3" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="737.8" y1="261.5" x2="737.8" y2="285.9" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="273.6" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="741.8" y1="267.4" x2="741.8" y2="285.7" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="275.0" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="745.7" y1="244.4" x2="745.7" y2="274.1" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="257.1" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="749.7" y1="220.7" x2="749.7" y2="246.3" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="221.4" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="753.6" y1="226.3" x2="753.6" y2="273.4" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="226.9" width="2.45" height="34.4" fill="var(--down)"/>
<line x1="757.6" y1="242.0" x2="757.6" y2="261.1" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="243.2" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="761.5" y1="242.5" x2="761.5" y2="261.1" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="243.7" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="765.5" y1="253.3" x2="765.5" y2="280.8" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="255.2" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="769.4" y1="243.3" x2="769.4" y2="267.1" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="244.2" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="773.4" y1="246.0" x2="773.4" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="250.2" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="777.3" y1="271.9" x2="777.3" y2="287.8" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="281.8" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="781.3" y1="278.3" x2="781.3" y2="315.4" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="284.2" width="2.45" height="23.7" fill="var(--down)"/>
<line x1="785.2" y1="302.0" x2="785.2" y2="324.2" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="307.2" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="789.2" y1="274.9" x2="789.2" y2="303.0" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="275.1" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="793.1" y1="253.8" x2="793.1" y2="276.5" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="262.3" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="797.1" y1="252.6" x2="797.1" y2="263.7" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="255.2" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="801.0" y1="210.3" x2="801.0" y2="242.3" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="212.0" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="805.0" y1="187.4" x2="805.0" y2="245.9" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="193.7" width="2.45" height="37.0" fill="var(--down)"/>
<line x1="808.9" y1="216.0" x2="808.9" y2="246.2" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="221.2" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="812.9" y1="215.1" x2="812.9" y2="241.6" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="217.6" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="816.8" y1="229.5" x2="816.8" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="239.7" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="820.8" y1="206.7" x2="820.8" y2="244.9" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="207.1" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="824.7" y1="167.7" x2="824.7" y2="205.7" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="183.1" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="828.7" y1="177.2" x2="828.7" y2="213.5" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="187.1" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="832.7" y1="206.7" x2="832.7" y2="261.3" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="211.5" width="2.45" height="44.5" fill="var(--down)"/>
<line x1="836.6" y1="224.6" x2="836.6" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="227.9" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="840.6" y1="202.9" x2="840.6" y2="280.7" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="215.6" width="2.45" height="24.5" fill="var(--down)"/>
<line x1="844.5" y1="232.2" x2="844.5" y2="273.3" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="252.7" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="848.5" y1="222.7" x2="848.5" y2="257.8" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="222.9" width="2.45" height="32.2" fill="var(--up)"/>
<line x1="852.4" y1="185.5" x2="852.4" y2="224.9" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="192.2" width="2.45" height="29.9" fill="var(--up)"/>
<line x1="856.4" y1="143.6" x2="856.4" y2="164.3" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="151.1" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="860.3" y1="145.7" x2="860.3" y2="183.8" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="151.4" width="2.45" height="32.2" fill="var(--down)"/>
<line x1="864.3" y1="139.4" x2="864.3" y2="185.1" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="155.6" width="2.45" height="29.1" fill="var(--down)"/>
<line x1="868.2" y1="141.1" x2="868.2" y2="166.0" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="143.4" width="2.45" height="22.6" fill="var(--up)"/>
<line x1="872.2" y1="113.4" x2="872.2" y2="141.0" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="116.5" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="876.1" y1="156.4" x2="876.1" y2="184.4" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="168.4" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="880.1" y1="150.3" x2="880.1" y2="177.4" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="158.5" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="884.0" y1="94.9" x2="884.0" y2="158.6" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="95.5" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="888.0" y1="117.6" x2="888.0" y2="164.3" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="121.1" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="891.9" y1="99.5" x2="891.9" y2="175.7" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="107.8" width="2.45" height="31.8" fill="var(--up)"/>
<line x1="895.9" y1="73.0" x2="895.9" y2="112.3" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="78.7" width="2.45" height="23.0" fill="var(--up)"/>
<line x1="899.8" y1="107.1" x2="899.8" y2="161.4" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="110.9" width="2.45" height="47.4" fill="var(--down)"/>
<line x1="903.8" y1="154.9" x2="903.8" y2="250.2" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="158.2" width="2.45" height="82.1" fill="var(--down)"/>
<line x1="907.7" y1="197.0" x2="907.7" y2="228.9" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="215.6" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="911.7" y1="251.6" x2="911.7" y2="297.7" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="261.4" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="915.6" y1="261.1" x2="915.6" y2="288.1" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="264.9" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="919.6" y1="217.9" x2="919.6" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="226.0" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="923.6" y1="249.4" x2="923.6" y2="274.2" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="253.6" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="927.5" y1="269.1" x2="927.5" y2="289.1" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="274.1" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="931.5" y1="246.0" x2="931.5" y2="271.1" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="248.0" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="935.4" y1="255.9" x2="935.4" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="258.2" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="939.4" y1="287.7" x2="939.4" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="292.1" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="943.3" y1="294.3" x2="943.3" y2="342.0" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="306.0" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="947.3" y1="265.4" x2="947.3" y2="293.5" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="287.9" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="951.2" y1="226.0" x2="951.2" y2="258.7" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="233.3" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="955.2" y1="230.0" x2="955.2" y2="251.9" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="239.7" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="959.1" y1="227.0" x2="959.1" y2="249.3" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="233.7" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="963.1" y1="237.0" x2="963.1" y2="273.5" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="246.0" width="2.45" height="21.2" fill="var(--down)"/>
<line x1="967.0" y1="259.7" x2="967.0" y2="309.9" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="267.2" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="971.0" y1="303.8" x2="971.0" y2="336.1" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="308.4" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="974.9" y1="235.8" x2="974.9" y2="310.5" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="241.9" width="2.45" height="68.2" fill="var(--down)"/>
<line x1="978.9" y1="240.4" x2="978.9" y2="274.9" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="245.3" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="982.8" y1="208.0" x2="982.8" y2="249.9" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="220.7" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="986.8" y1="238.4" x2="986.8" y2="268.1" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="244.9" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="990.7" y1="183.1" x2="990.7" y2="220.8" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="191.7" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="994.7" y1="183.5" x2="994.7" y2="216.3" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="193.3" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="998.6" y1="201.5" x2="998.6" y2="239.0" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="218.0" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="1002.6" y1="200.1" x2="1002.6" y2="235.0" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="200.1" width="2.45" height="25.7" fill="var(--down)"/>
<line x1="1006.5" y1="215.0" x2="1006.5" y2="247.0" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="215.5" width="2.45" height="30.3" fill="var(--down)"/>
<line x1="1010.5" y1="213.9" x2="1010.5" y2="237.3" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="225.5" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="1014.5" y1="184.7" x2="1014.5" y2="206.4" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="192.9" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="1018.4" y1="165.3" x2="1018.4" y2="199.6" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="181.9" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="1022.4" y1="170.0" x2="1022.4" y2="199.0" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="170.3" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="1026.3" y1="134.6" x2="1026.3" y2="168.3" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="136.0" width="2.45" height="25.5" fill="var(--up)"/>
<line x1="1030.3" y1="161.9" x2="1030.3" y2="207.7" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="169.8" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="1034.2" y1="189.4" x2="1034.2" y2="233.3" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="189.4" width="2.45" height="35.9" fill="var(--down)"/>
<line x1="1038.2" y1="216.5" x2="1038.2" y2="234.9" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="220.5" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="1042.1" y1="217.0" x2="1042.1" y2="246.0" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="222.4" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="1046.1" y1="242.0" x2="1046.1" y2="268.5" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="246.1" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="1050.0" y1="226.7" x2="1050.0" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="232.9" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="60" y1="223.3" x2="1052" y2="223.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="226.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$381 R1</text>
<text x="1058" y="238.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="166.7" x2="1052" y2="166.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="170.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$421 R2</text>
<text x="1058" y="182.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="337.6" x2="1052" y2="337.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="331.6" font-size="11.5" fill="var(--support)" font-weight="600">$300 S1</text>
<text x="1058" y="343.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="244.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="236.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $366 (2026-08-25)</text>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $421 | 2 | 2026년 4월(4/24)·6월(6/3) 스윙 고점 — 두 차례 큰 폭 조정 이후의 반등 상단 |
| R1 | $381 | 2 | 2026년 5월(5/6)·7월(7/21) 스윙 고점 |
| **현재가** | **$366.43** (2026-08-25 종가) | — | R1과 S1 사이 |
| S1 | $300 | 3 | 2026년 4월(4/29, 실적 서프라이즈에도 급락한 날의 저점)·7월(7/17·7/28) 반복 형성된 지지대 |
| 참고선 | $487.91 | — | 최근 1년 최고가. 현재가와 −25% 떨어져 있고 반복 터치된 클러스터가 아니라 근시일 저항으로 보지 않는다 |

> **직전 회차(2026-08-14 기준) 대비 달라진 점**: 그때는 현재가($418.79)가 R1($421) 바로 아래에 붙어 있어 유효 클러스터가 R1·S1 둘뿐이었다. 이후 −12.5% 조정으로 현재가가 내려오면서, 그때 현재가에 가려 있던 $381 스윙대(5월·7월 고점)가 새 R1으로 드러났고 기존 $421은 R2로 밀렸다. **레벨 자체가 새로 생긴 것이 아니라 현재가 위치가 바뀌면서 사이에 끼는 레벨이 늘어난 것**이다.
>
> 이 회사는 최근 1년간 최고($487.91)~최저($109.56)까지 가격이 약 4.5배 벌어질 만큼 극단적으로 변동성이 컸다 — AI 반도체 사이클 기대와 실제 실적·가이던스 사이의 간극이 반복적으로 가격에 충격을 준 결과다(3. 관측된 특이 구간 참고). 스윙이 넓은 밴드에 흩어져 있어 현재가 아래쪽 유효 클러스터는 여전히 S1 하나뿐이며, 억지로 레벨을 추가하지 않았다.

---

## 3. 관측된 특이 구간

### 3-A. 2026-02-03 — FY2025 4분기 실적 서프라이즈

- 2026-02-02(월) 장 마감 후 FY2025 4분기·연간 실적 발표 — 매출 $1,083M, Non-GAAP EPS $1.80로 가이던스 상단을 상회([최근 뉴스 / 이슈](./08_news.md) 참고).
- 종가 기준 2026-02-02 $249.53 → 2026-02-03 $282.98로 **+13.4%** 급등, 거래량은 1,180만 주로 직전 20거래일 평균(약 368만 주) 대비 약 3.2배.
- 이 갭 이후 주가는 2월~3월 한동안 $260~$300 박스권에서 등락하다, 4월 말 Q1 실적 발표를 계기로 한 단계 더 뛰어올랐다(3-B. 2026-04-29 — Q1 2026 실적 호조에도 보수적 가이던스로 급락("셀 더 뉴스")).

### 3-B. 2026-04-29 — Q1 2026 실적 호조에도 보수적 가이던스로 급락("셀 더 뉴스")

- 2026-04-28(화) 장 마감 후 발표된 Q1 FY2026 실적은 매출 +87% YoY, Non-GAAP EPS $2.56(컨센서스 $2.11 상회)로 뚜렷한 서프라이즈였다. 그럼에도 다음 거래일 주가는 급락했다 — 컨센서스 대비 보수적인 향후 가이던스, 반도체 업종 전반의 거시 불확실성, 연초 급등 이후 차익실현이 복합적으로 작용한 "셀 더 뉴스(sell the news)" 반응으로 보도됐다([최근 뉴스 / 이슈](./08_news.md), 하단 출처 참고).
- 종가 기준 2026-04-28 $380.13 → 2026-04-29 $306.33로 **−19.4%** 급락, 거래량은 1,307만 주로 직전 20거래일 평균 대비 약 3.5배(최근 1년 중 최대 거래량 구간).
- 이날 저가($301.86)는 이후 7월 두 차례(7/17, 7/28) 재차 터치되며 S1($300) 지지대로 굳어졌다 — 실적 서프라이즈에도 불구한 하루의 급락이 오히려 이후 몇 달간의 지지선을 만든 역설적인 사례다.

### 3-C. 2026년 8월 중순 — 고점 이후 되돌림

- 2026-08-14 $418.79에서 2026-08-25 $366.43까지 8거래일 만에 **−12.5%** 조정됐다. 단일 갭 이벤트가 아니라 여러 날에 걸친 하락이라 위 두 사례와 성격이 다르다.
- 같은 기간 반도체 장비 업종 전반이 함께 조정받았고(Applied Materials·Lam Research 등), 2026-08-21 Baird가 **밸류에이션**을 근거로 투자의견을 Outperform → Neutral로 하향했다([최근 뉴스 / 이슈](./08_news.md) 참고) — 실적·가이던스 변화가 아니라 **가격 자체에 대한 재평가**가 계기였다는 점이 특징이다.
- 이 조정으로 현재가가 R2($421)에서 R1($381) 아래로 내려왔고, [밸류에이션 / 적정주가](./06_valuation.md)의 괴리율 판정도 함께 바뀌었다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-26~2026-08-25. 수집 시점: 2026-08-26. 원주가(과거 분할은 소급 반영 — 조사 기간 내 분할 없음, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py TER --name Teradyne --event 2026-02-03:"FY2025 4분기 실적 서프라이즈" --event 2026-04-29:"Q1 2026 실적 호조에도 보수적 가이던스로 급락" --close-on 2025-12-31 --close-on 2026-08-14 --close-on 2026-08-25 --emit all`. 파라미터는 회사 간 비교가 가능하도록 스크립트 기본값 그대로 사용(강제 레벨 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - **1년 창(window)이 밀리면 레벨도 바뀐다.** 직전 회차(2026-08-14 종료)에서는 1년 최저가 $106.30이었으나 창이 11일 밀리면서 $109.56이 됐고, 레벨 구성도 R1·S1 2개에서 R2·R1·S1 3개로 달라졌다 — 이 표의 레벨은 특정 관측 창에 종속된 값이다.
    - 최근 1년간 세 차례의 가격 레짐 단절(3-A·3-B·3-C)이 있었다 — 특히 3-B는 "실적 호재=주가 상승"이라는 단순 도식이 통하지 않은 사례로, 이 회사가 얼마나 가이던스·거시 심리에 민감한지 보여준다.
    - 기간 내 배당이 4회 있었으나 원주가 기준이라 배당은 반영하지 않았다 — 배당수익률이 0.14%로 미미해 배당락 영향은 무시할 만한 수준이다.
    - 조사 기간(2025-08~2026-08) 내 주식분할·유상증자는 없었다.

---

*작성일: 2026-08-26*
