# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉 데이터는 핵심 지표가 다루는 범위 밖이다).
    - **⚠️ 차트의 마지막 봉(2026-08-24)은 확정 종가가 아니다.** 차트를 생성한 시점이 미 동부시간 2026-08-24 오전(정규장 개장 중)이라, 그날 봉은 장중 스냅숏($30.67, 거래량 190만 주 — 평소 1,246만 주의 15%)이다. **다른 문서가 인용하는 기준 종가는 직전 거래일인 2026-08-21 종가 $30.98이다.**
    - **대조 결과**: 스크립트로 조회한 2026-08-21 종가 $30.98은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)가 인용한 값과 일치한다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-25 ~ 2026-08-24)

<div class="kmi-chart">
<style>
.kmi-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .kmi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .kmi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.kmi-chart svg { width:100%; height:auto; display:block; }
.kmi-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.kmi-chart .title { fill: var(--ink); font-weight:600; }
.kmi-chart .grid { stroke: var(--grid); stroke-width:1; }
.kmi-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kinder Morgan(KMI) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Kinder Morgan (KMI) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-25 ~ 2026-08-24 · 마지막 종가 $30.67 (2026-08-24) · 단위 USD</text>
<line x1="60" y1="580.4" x2="1052" y2="580.4" class="grid"/>
<text x="52" y="584.4" font-size="11" text-anchor="end" fill="var(--muted)">26</text>
<line x1="60" y1="466.4" x2="1052" y2="466.4" class="grid"/>
<text x="52" y="470.4" font-size="11" text-anchor="end" fill="var(--muted)">28</text>
<line x1="60" y1="352.4" x2="1052" y2="352.4" class="grid"/>
<text x="52" y="356.4" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="238.4" x2="1052" y2="238.4" class="grid"/>
<text x="52" y="242.4" font-size="11" text-anchor="end" fill="var(--muted)">32</text>
<line x1="60" y1="124.4" x2="1052" y2="124.4" class="grid"/>
<text x="52" y="128.4" font-size="11" text-anchor="end" fill="var(--muted)">34</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="81.7" y1="626.0" x2="81.7" y2="631.0" class="axis"/>
<text x="81.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="164.7" y1="626.0" x2="164.7" y2="631.0" class="axis"/>
<text x="164.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="255.6" y1="626.0" x2="255.6" y2="631.0" class="axis"/>
<text x="255.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="330.7" y1="626.0" x2="330.7" y2="631.0" class="axis"/>
<text x="330.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="417.7" y1="626.0" x2="417.7" y2="631.0" class="axis"/>
<text x="417.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="496.7" y1="626.0" x2="496.7" y2="631.0" class="axis"/>
<text x="496.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="571.8" y1="626.0" x2="571.8" y2="631.0" class="axis"/>
<text x="571.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="658.8" y1="626.0" x2="658.8" y2="631.0" class="axis"/>
<text x="658.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="741.8" y1="626.0" x2="741.8" y2="631.0" class="axis"/>
<text x="741.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="820.8" y1="626.0" x2="820.8" y2="631.0" class="axis"/>
<text x="820.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="903.8" y1="626.0" x2="903.8" y2="631.0" class="axis"/>
<text x="903.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="990.7" y1="626.0" x2="990.7" y2="631.0" class="axis"/>
<text x="990.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="533.7" x2="62.0" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="540.5" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="65.9" y1="542.2" x2="65.9" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="545.1" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="69.9" y1="528.0" x2="69.9" y2="547.9" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="533.1" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="73.8" y1="520.6" x2="73.8" y2="538.8" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="522.8" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="77.8" y1="518.3" x2="77.8" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="523.4" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="81.7" y1="524.5" x2="81.7" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="538.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="85.7" y1="530.2" x2="85.7" y2="548.5" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="538.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="89.6" y1="514.9" x2="89.6" y2="545.6" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="530.8" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="93.6" y1="531.9" x2="93.6" y2="567.9" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="537.1" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="97.5" y1="518.3" x2="97.5" y2="563.9" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="537.7" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="101.5" y1="529.1" x2="101.5" y2="545.6" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="543.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="105.5" y1="497.2" x2="105.5" y2="545.1" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="501.7" width="2.45" height="43.3" fill="var(--up)"/>
<line x1="109.4" y1="490.3" x2="109.4" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="490.9" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="113.4" y1="477.2" x2="113.4" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="489.2" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="117.3" y1="480.7" x2="117.3" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="485.2" width="2.45" height="17.7" fill="var(--down)"/>
<line x1="121.3" y1="500.0" x2="121.3" y2="519.4" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="500.0" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="125.2" y1="485.8" x2="125.2" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="490.9" width="2.45" height="16.0" fill="var(--up)"/>
<line x1="129.2" y1="473.2" x2="129.2" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="485.2" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="133.1" y1="482.4" x2="133.1" y2="507.4" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="483.5" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="137.1" y1="497.2" x2="137.1" y2="513.1" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="504.0" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="141.0" y1="481.8" x2="141.0" y2="515.4" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="496.6" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="145.0" y1="464.7" x2="145.0" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="476.7" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="148.9" y1="455.0" x2="148.9" y2="480.7" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="470.4" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="152.9" y1="437.3" x2="152.9" y2="464.7" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="454.4" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="156.8" y1="445.3" x2="156.8" y2="465.8" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="445.3" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="160.8" y1="439.0" x2="160.8" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="448.7" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="164.7" y1="443.6" x2="164.7" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="449.3" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="168.7" y1="414.5" x2="168.7" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="452.7" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="172.6" y1="424.8" x2="172.6" y2="464.7" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="440.2" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="176.6" y1="431.1" x2="176.6" y2="470.4" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="432.8" width="2.45" height="37.6" fill="var(--down)"/>
<line x1="180.5" y1="461.8" x2="180.5" y2="482.4" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="465.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="184.5" y1="455.6" x2="184.5" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="458.4" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="188.4" y1="447.0" x2="188.4" y2="497.2" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="460.7" width="2.45" height="33.1" fill="var(--down)"/>
<line x1="192.4" y1="477.8" x2="192.4" y2="518.3" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="494.9" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="196.4" y1="502.3" x2="196.4" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="504.0" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="200.3" y1="501.7" x2="200.3" y2="523.4" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="505.7" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="204.3" y1="476.1" x2="204.3" y2="504.0" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="488.6" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="208.2" y1="481.2" x2="208.2" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="488.1" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="212.2" y1="500.6" x2="212.2" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="501.7" width="2.45" height="16.0" fill="var(--up)"/>
<line x1="216.1" y1="473.8" x2="216.1" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="486.4" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="220.1" y1="487.5" x2="220.1" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="488.1" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="224.0" y1="485.2" x2="224.0" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="491.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="228.0" y1="459.0" x2="228.0" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="466.4" width="2.45" height="99.8" fill="var(--down)"/>
<line x1="231.9" y1="553.0" x2="231.9" y2="594.1" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="553.0" width="2.45" height="35.3" fill="var(--down)"/>
<line x1="235.9" y1="569.6" x2="235.9" y2="591.2" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="571.9" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="239.8" y1="570.1" x2="239.8" y2="590.7" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="570.1" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="243.8" y1="557.6" x2="243.8" y2="588.4" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="571.3" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="247.7" y1="561.6" x2="247.7" y2="595.8" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="575.8" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="251.7" y1="564.4" x2="251.7" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="569.6" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="255.6" y1="575.3" x2="255.6" y2="603.2" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="575.8" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="259.6" y1="575.8" x2="259.6" y2="594.7" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="582.7" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="263.5" y1="567.9" x2="263.5" y2="599.8" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="585.0" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="267.5" y1="559.9" x2="267.5" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="573.6" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="271.4" y1="545.6" x2="271.4" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="549.1" width="2.45" height="24.5" fill="var(--up)"/>
<line x1="275.4" y1="516.0" x2="275.4" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="520.0" width="2.45" height="29.1" fill="var(--up)"/>
<line x1="279.3" y1="512.0" x2="279.3" y2="535.4" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="515.4" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="283.3" y1="504.0" x2="283.3" y2="528.5" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="522.8" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="287.3" y1="512.0" x2="287.3" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="518.8" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="291.2" y1="495.5" x2="291.2" y2="541.6" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="499.5" width="2.45" height="32.5" fill="var(--up)"/>
<line x1="295.2" y1="492.1" x2="295.2" y2="516.6" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="498.9" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="299.1" y1="505.2" x2="299.1" y2="528.0" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="518.3" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="303.1" y1="529.1" x2="303.1" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="533.7" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="307.0" y1="502.3" x2="307.0" y2="540.5" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="524.5" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="311.0" y1="519.4" x2="311.0" y2="549.6" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="524.5" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="314.9" y1="521.7" x2="314.9" y2="548.5" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="522.3" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="318.9" y1="535.4" x2="318.9" y2="562.2" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="541.1" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="322.8" y1="518.8" x2="322.8" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="526.2" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="326.8" y1="502.9" x2="326.8" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="505.2" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="330.7" y1="498.3" x2="330.7" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="506.9" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="334.7" y1="505.2" x2="334.7" y2="535.9" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="505.2" width="2.45" height="26.8" fill="var(--down)"/>
<line x1="338.6" y1="502.3" x2="338.6" y2="529.7" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="513.7" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="342.6" y1="474.4" x2="342.6" y2="520.0" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="475.5" width="2.45" height="40.5" fill="var(--up)"/>
<line x1="346.5" y1="466.4" x2="346.5" y2="484.1" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="473.8" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="350.5" y1="482.4" x2="350.5" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="482.4" width="2.45" height="24.5" fill="var(--down)"/>
<line x1="354.4" y1="476.7" x2="354.4" y2="508.0" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="504.0" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="358.4" y1="503.4" x2="358.4" y2="550.2" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="504.0" width="2.45" height="42.8" fill="var(--down)"/>
<line x1="362.3" y1="533.1" x2="362.3" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="533.7" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="366.3" y1="518.3" x2="366.3" y2="547.3" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="525.7" width="2.45" height="13.1" fill="var(--down)"/>
<line x1="370.2" y1="534.2" x2="370.2" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="536.5" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="374.2" y1="542.8" x2="374.2" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="542.8" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="378.2" y1="538.2" x2="378.2" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="543.4" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="382.1" y1="531.4" x2="382.1" y2="562.2" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="539.9" width="2.45" height="21.1" fill="var(--down)"/>
<line x1="386.1" y1="538.8" x2="386.1" y2="562.7" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="552.5" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="390.0" y1="526.8" x2="390.0" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="529.7" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="394.0" y1="506.9" x2="394.0" y2="532.5" stroke="var(--up)" class="wick"/>
<rect x="392.73" y="507.4" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="397.9" y1="502.9" x2="397.9" y2="513.1" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="508.0" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="401.9" y1="504.0" x2="401.9" y2="518.8" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="509.2" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="405.8" y1="493.8" x2="405.8" y2="510.9" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="501.7" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="409.8" y1="486.4" x2="409.8" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="490.3" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="413.7" y1="490.3" x2="413.7" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="492.6" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="417.7" y1="472.1" x2="417.7" y2="512.6" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="482.9" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="421.6" y1="468.7" x2="421.6" y2="516.0" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="468.7" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="425.6" y1="466.4" x2="425.6" y2="546.8" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="466.4" width="2.45" height="67.3" fill="var(--down)"/>
<line x1="429.5" y1="513.7" x2="429.5" y2="533.1" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="523.4" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="433.5" y1="496.6" x2="433.5" y2="523.4" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="508.0" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="437.4" y1="495.5" x2="437.4" y2="527.4" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="500.6" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="441.4" y1="509.2" x2="441.4" y2="540.5" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="515.4" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="445.3" y1="494.3" x2="445.3" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="501.7" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="449.3" y1="477.8" x2="449.3" y2="505.7" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="493.2" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="453.2" y1="482.4" x2="453.2" y2="505.2" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="495.5" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="457.2" y1="467.5" x2="457.2" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="468.7" width="2.45" height="23.9" fill="var(--up)"/>
<line x1="461.1" y1="447.0" x2="461.1" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="458.4" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="465.1" y1="428.8" x2="465.1" y2="452.7" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="433.3" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="469.1" y1="342.1" x2="469.1" y2="413.4" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="370.1" width="2.45" height="31.9" fill="var(--up)"/>
<line x1="473.0" y1="352.4" x2="473.0" y2="382.0" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="353.5" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="477.0" y1="361.5" x2="477.0" y2="410.0" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="363.8" width="2.45" height="26.2" fill="var(--down)"/>
<line x1="480.9" y1="374.6" x2="480.9" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="375.8" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="484.9" y1="334.7" x2="484.9" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="348.4" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="488.8" y1="319.9" x2="488.8" y2="351.8" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="323.9" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="492.8" y1="321.1" x2="492.8" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="324.5" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="496.7" y1="358.1" x2="496.7" y2="383.7" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="359.2" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="500.7" y1="330.2" x2="500.7" y2="371.8" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="334.2" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="504.6" y1="320.5" x2="504.6" y2="378.6" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="329.6" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="508.6" y1="330.2" x2="508.6" y2="369.5" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="333.6" width="2.45" height="21.1" fill="var(--up)"/>
<line x1="512.5" y1="318.8" x2="512.5" y2="338.7" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="323.9" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="516.5" y1="288.6" x2="516.5" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="296.0" width="2.45" height="29.1" fill="var(--up)"/>
<line x1="520.4" y1="264.6" x2="520.4" y2="301.1" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="282.9" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="524.4" y1="257.2" x2="524.4" y2="283.4" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="268.0" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="528.3" y1="239.0" x2="528.3" y2="271.5" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="256.1" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="532.3" y1="219.0" x2="532.3" y2="257.2" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="220.2" width="2.45" height="34.8" fill="var(--up)"/>
<line x1="536.2" y1="205.3" x2="536.2" y2="249.2" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="219.6" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="540.2" y1="206.5" x2="540.2" y2="230.4" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="209.9" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="544.1" y1="194.5" x2="544.1" y2="216.7" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="207.6" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="548.1" y1="194.5" x2="548.1" y2="228.7" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="196.8" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="552.0" y1="167.7" x2="552.0" y2="202.5" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="196.2" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="556.0" y1="197.4" x2="556.0" y2="230.4" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="199.1" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="560.0" y1="192.8" x2="560.0" y2="226.4" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="194.5" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="563.9" y1="167.7" x2="563.9" y2="205.9" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="178.0" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="567.9" y1="161.5" x2="567.9" y2="184.2" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="166.0" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="571.8" y1="117.0" x2="571.8" y2="177.4" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="130.7" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="575.8" y1="110.7" x2="575.8" y2="152.9" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="124.4" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="579.7" y1="123.8" x2="579.7" y2="154.6" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="129.0" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="583.7" y1="119.8" x2="583.7" y2="165.4" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="130.7" width="2.45" height="28.5" fill="var(--down)"/>
<line x1="587.6" y1="143.2" x2="587.6" y2="167.7" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="148.3" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="591.6" y1="143.8" x2="591.6" y2="172.8" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="143.8" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="595.5" y1="159.2" x2="595.5" y2="185.4" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="170.0" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="599.5" y1="164.3" x2="599.5" y2="200.2" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="176.8" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="603.4" y1="129.5" x2="603.4" y2="179.7" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="159.7" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="607.4" y1="149.5" x2="607.4" y2="167.7" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="150.1" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="611.3" y1="155.7" x2="611.3" y2="178.0" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="158.6" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="615.3" y1="131.2" x2="615.3" y2="168.3" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="151.8" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="619.2" y1="166.0" x2="619.2" y2="203.6" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="167.7" width="2.45" height="35.9" fill="var(--down)"/>
<line x1="623.2" y1="140.4" x2="623.2" y2="209.9" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="156.3" width="2.45" height="37.0" fill="var(--up)"/>
<line x1="627.1" y1="139.8" x2="627.1" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="153.5" width="2.45" height="37.1" fill="var(--down)"/>
<line x1="631.1" y1="134.7" x2="631.1" y2="213.3" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="140.9" width="2.45" height="51.3" fill="var(--up)"/>
<line x1="635.0" y1="111.3" x2="635.0" y2="146.6" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="128.4" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="639.0" y1="109.6" x2="639.0" y2="143.2" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="125.5" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="642.9" y1="101.6" x2="642.9" y2="137.5" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="120.4" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="646.9" y1="82.8" x2="646.9" y2="134.1" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="122.7" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="650.9" y1="103.9" x2="650.9" y2="151.8" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="108.4" width="2.45" height="35.9" fill="var(--down)"/>
<line x1="654.8" y1="130.7" x2="654.8" y2="179.7" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="135.2" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="658.8" y1="163.7" x2="658.8" y2="208.8" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="172.8" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="662.7" y1="152.9" x2="662.7" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="152.9" width="2.45" height="30.2" fill="var(--down)"/>
<line x1="666.7" y1="168.9" x2="666.7" y2="192.2" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="170.6" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="670.6" y1="135.8" x2="670.6" y2="168.9" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="164.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="674.6" y1="178.0" x2="674.6" y2="236.7" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="183.7" width="2.45" height="47.9" fill="var(--up)"/>
<line x1="678.5" y1="137.5" x2="678.5" y2="195.1" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="183.1" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="682.5" y1="184.8" x2="682.5" y2="212.2" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="192.8" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="686.4" y1="190.0" x2="686.4" y2="254.4" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="193.4" width="2.45" height="41.0" fill="var(--down)"/>
<line x1="690.4" y1="238.4" x2="690.4" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="243.5" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="694.3" y1="246.9" x2="694.3" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="255.5" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="698.3" y1="234.4" x2="698.3" y2="262.9" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="250.4" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="702.2" y1="233.3" x2="702.2" y2="300.0" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="237.3" width="2.45" height="49.6" fill="var(--up)"/>
<line x1="706.2" y1="214.5" x2="706.2" y2="254.9" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="241.8" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="710.1" y1="228.1" x2="710.1" y2="286.9" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="241.2" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="714.1" y1="237.3" x2="714.1" y2="253.8" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="247.5" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="718.0" y1="215.6" x2="718.0" y2="291.4" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="223.0" width="2.45" height="30.8" fill="var(--down)"/>
<line x1="722.0" y1="247.5" x2="722.0" y2="285.7" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="253.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="725.9" y1="239.5" x2="725.9" y2="310.8" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="256.6" width="2.45" height="41.6" fill="var(--down)"/>
<line x1="729.9" y1="245.8" x2="729.9" y2="279.4" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="250.4" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="733.8" y1="241.2" x2="733.8" y2="261.8" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="246.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="737.8" y1="187.1" x2="737.8" y2="257.8" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="188.8" width="2.45" height="61.6" fill="var(--up)"/>
<line x1="741.8" y1="186.0" x2="741.8" y2="216.7" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="191.7" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="745.7" y1="208.8" x2="745.7" y2="230.4" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="211.6" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="749.7" y1="205.9" x2="749.7" y2="233.3" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="213.3" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="753.6" y1="231.0" x2="753.6" y2="276.6" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="237.8" width="2.45" height="24.5" fill="var(--down)"/>
<line x1="757.6" y1="264.1" x2="757.6" y2="302.2" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="265.8" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="761.5" y1="250.4" x2="761.5" y2="282.3" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="264.6" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="765.5" y1="218.5" x2="765.5" y2="266.3" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="224.2" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="769.4" y1="198.5" x2="769.4" y2="225.9" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="207.6" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="773.4" y1="188.8" x2="773.4" y2="228.1" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="192.2" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="777.3" y1="154.0" x2="777.3" y2="193.4" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="158.6" width="2.45" height="31.9" fill="var(--up)"/>
<line x1="781.3" y1="134.7" x2="781.3" y2="165.4" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="145.5" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="785.2" y1="134.1" x2="785.2" y2="162.0" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="136.9" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="789.2" y1="78.2" x2="789.2" y2="149.5" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="106.7" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="793.1" y1="87.9" x2="793.1" y2="148.9" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="106.7" width="2.45" height="41.0" fill="var(--down)"/>
<line x1="797.1" y1="134.1" x2="797.1" y2="159.7" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="142.6" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="801.0" y1="130.7" x2="801.0" y2="161.5" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="136.4" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="805.0" y1="142.1" x2="805.0" y2="190.0" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="145.5" width="2.45" height="43.3" fill="var(--down)"/>
<line x1="808.9" y1="199.1" x2="808.9" y2="231.6" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="205.3" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="812.9" y1="213.3" x2="812.9" y2="246.4" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="215.6" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="816.8" y1="250.4" x2="816.8" y2="292.0" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="252.1" width="2.45" height="38.8" fill="var(--down)"/>
<line x1="820.8" y1="275.4" x2="820.8" y2="305.7" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="292.0" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="824.7" y1="266.3" x2="824.7" y2="304.5" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="270.3" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="828.7" y1="242.4" x2="828.7" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="266.9" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="832.7" y1="252.1" x2="832.7" y2="274.3" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="255.5" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="836.6" y1="242.4" x2="836.6" y2="264.1" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="256.6" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="840.6" y1="248.1" x2="840.6" y2="281.2" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="262.9" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="844.5" y1="258.4" x2="844.5" y2="293.7" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="275.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="848.5" y1="237.3" x2="848.5" y2="270.9" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="247.5" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="852.4" y1="229.8" x2="852.4" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="229.8" width="2.45" height="45.0" fill="var(--down)"/>
<line x1="856.4" y1="224.7" x2="856.4" y2="281.2" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="241.8" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="860.3" y1="254.4" x2="860.3" y2="295.4" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="269.2" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="864.3" y1="255.5" x2="864.3" y2="287.4" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="270.3" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="868.2" y1="264.1" x2="868.2" y2="288.6" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="275.4" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="872.2" y1="257.2" x2="872.2" y2="301.7" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="261.8" width="2.45" height="28.5" fill="var(--up)"/>
<line x1="876.1" y1="221.3" x2="876.1" y2="262.9" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="224.2" width="2.45" height="38.2" fill="var(--up)"/>
<line x1="880.1" y1="205.9" x2="880.1" y2="260.1" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="207.6" width="2.45" height="24.5" fill="var(--up)"/>
<line x1="884.0" y1="200.2" x2="884.0" y2="229.3" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="204.8" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="888.0" y1="166.0" x2="888.0" y2="219.6" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="180.8" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="891.9" y1="162.0" x2="891.9" y2="182.5" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="170.6" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="895.9" y1="164.3" x2="895.9" y2="227.6" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="174.0" width="2.45" height="49.0" fill="var(--down)"/>
<line x1="899.8" y1="199.6" x2="899.8" y2="243.0" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="213.3" width="2.45" height="26.8" fill="var(--down)"/>
<line x1="903.8" y1="236.7" x2="903.8" y2="266.3" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="246.9" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="907.7" y1="231.6" x2="907.7" y2="259.5" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="235.0" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="911.7" y1="221.9" x2="911.7" y2="258.4" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="237.3" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="915.6" y1="198.5" x2="915.6" y2="241.8" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="210.5" width="2.45" height="28.5" fill="var(--up)"/>
<line x1="919.6" y1="194.5" x2="919.6" y2="226.4" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="207.1" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="923.6" y1="193.4" x2="923.6" y2="218.5" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="213.9" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="927.5" y1="210.5" x2="927.5" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="217.3" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="931.5" y1="207.6" x2="931.5" y2="246.4" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="209.9" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="935.4" y1="204.2" x2="935.4" y2="228.7" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="207.6" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="939.4" y1="201.3" x2="939.4" y2="235.0" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="209.9" width="2.45" height="17.1" fill="var(--down)"/>
<line x1="943.3" y1="193.9" x2="943.3" y2="232.1" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="207.6" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="947.3" y1="183.1" x2="947.3" y2="231.0" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="186.0" width="2.45" height="35.3" fill="var(--down)"/>
<line x1="951.2" y1="177.4" x2="951.2" y2="224.2" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="205.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="955.2" y1="186.0" x2="955.2" y2="235.6" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="186.0" width="2.45" height="30.8" fill="var(--down)"/>
<line x1="959.1" y1="196.2" x2="959.1" y2="221.3" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="199.1" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="963.1" y1="166.6" x2="963.1" y2="237.3" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="181.4" width="2.45" height="13.1" fill="var(--down)"/>
<line x1="967.0" y1="166.6" x2="967.0" y2="204.2" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="186.0" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="971.0" y1="217.3" x2="971.0" y2="257.2" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="223.0" width="2.45" height="29.6" fill="var(--down)"/>
<line x1="974.9" y1="227.0" x2="974.9" y2="264.1" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="241.2" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="978.9" y1="222.4" x2="978.9" y2="259.5" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="232.7" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="982.8" y1="241.2" x2="982.8" y2="281.2" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="257.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="986.8" y1="222.4" x2="986.8" y2="264.1" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="228.1" width="2.45" height="35.9" fill="var(--up)"/>
<line x1="990.7" y1="253.8" x2="990.7" y2="280.0" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="258.9" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="994.7" y1="260.6" x2="994.7" y2="313.6" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="273.7" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="998.6" y1="267.5" x2="998.6" y2="300.5" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="277.2" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="1002.6" y1="258.9" x2="1002.6" y2="292.0" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="266.9" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="1006.5" y1="283.4" x2="1006.5" y2="308.5" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="292.0" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="1010.5" y1="272.0" x2="1010.5" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="273.2" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="1014.5" y1="256.1" x2="1014.5" y2="277.2" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="268.0" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="1018.4" y1="249.2" x2="1018.4" y2="274.9" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="253.8" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="1022.4" y1="216.2" x2="1022.4" y2="262.3" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="233.8" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="1026.3" y1="190.5" x2="1026.3" y2="231.0" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="191.7" width="2.45" height="33.6" fill="var(--up)"/>
<line x1="1030.3" y1="182.5" x2="1030.3" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="191.1" width="2.45" height="28.5" fill="var(--down)"/>
<line x1="1034.2" y1="178.0" x2="1034.2" y2="204.2" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="188.8" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="1038.2" y1="178.0" x2="1038.2" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="181.4" width="2.45" height="52.4" fill="var(--down)"/>
<line x1="1042.1" y1="221.9" x2="1042.1" y2="288.0" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="229.3" width="2.45" height="31.3" fill="var(--down)"/>
<line x1="1046.1" y1="246.4" x2="1046.1" y2="304.5" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="253.2" width="2.45" height="43.3" fill="var(--down)"/>
<line x1="1050.0" y1="296.4" x2="1050.0" y2="317.6" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="303.4" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="60" y1="174.9" x2="1052" y2="174.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="178.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$33 R1</text>
<text x="1058" y="190.4" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="90.6" x2="1052" y2="90.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="94.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$35 R2</text>
<text x="1058" y="106.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="569.3" x2="1052" y2="569.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="563.3" font-size="11.5" fill="var(--support)" font-weight="600">$26 S1</text>
<text x="1058" y="575.3" font-size="9.5" fill="var(--muted)">터치 5회</text>
<circle cx="1052.0" cy="313.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="305.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $31 (2026-08-24)</text>
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
| R2 | $35 | 3 | 2026-03-03 · 03-27 · 05-19 스윙 고점대. 최근 1년 최고가($34.81, 종가 기준 최고 $34.31)와 겹치는 상단 |
| R1 | $33 | 5 | 2026-05-01 · 06-26 · 07-09 · 07-23 · 07-24 스윙 고점대. Q2 2026 실적발표(07-22) 전후에 세 번 몰려 있어, 실적 기대가 소화된 뒤 되밀린 가격대 |
| **기준 종가** | **$30.98** (2026-08-21) | — | R1과 S1 사이. 다른 문서가 인용하는 값 |
| (차트 마지막 봉) | $30.67 (2026-08-24 장중, 미확정) | — | 위 ??? 블록 참고 — 확정 종가가 아니다 |
| S1 | $26 | 5 | 2025-09-05 · 11-03 · 11-25 · 12-16 · 2026-01-06 스윙 저점대. 최근 1년 최저($25.60)를 포함하는 가을~연초 박스권 바닥 |

> 유효한 클러스터가 3개(R2·R1·S1)뿐이라 스크립트 기본값(`--levels 3`)을 그대로 뒀다. 현재가 위로 두 개, 아래로 하나만 잡히는 것은 **주가가 최근 1년 레인지($25.60~$34.81)의 중상단에 있기 때문**이며, S1($26) 아래로는 이 기간에 스윙 저점 자체가 없다.

---

## 3. 관측된 특이 구간 — 2025-10-23 Q3 2025 실적발표 후 급락

- 2025-10-22 장 마감 후 발표된 Q3 2025 실적([최근 뉴스 / 이슈](./08_news.md) 로그에는 별도 항목으로 남기지 않았다 — 이후 분기들에 흡수된 사건이라 판단에 영향을 주지 않았다) 직후의 반응이다. 그 분기는 GAAP EPS가 전년 동기와 같은 $0.28로 성장이 멈춘 분기였다([핵심 지표](./04_metrics.md) B절).
- 종가 기준 전일 대비 **−4.75%** ($27.56 → $26.25), 거래량은 평소(일 1,246만 주 내외) 대비 약 2.4배인 **2,959만 주**. 최근 1년 중 가장 큰 하루 낙폭이다.
- 이 하락으로 주가가 S1($26) 클러스터로 내려앉았고, 이후 2026-01-06까지 그 부근에서 세 차례 더 저점을 만들며 **$26대가 지지대로 굳어졌다.** 반대편의 전환점은 2026-01-22(FY2025 실적발표 다음날, +3.88% / 거래량 2.3배)로, 여기서 벗어난 뒤에는 $26 부근을 다시 시험하지 않았다.
- 두 사건 모두 실적발표 직후라 **레짐이 구조적으로 재설정된 것이 아니라 같은 레인지 안에서 위아래를 확인한 움직임**으로 보는 편이 맞다 — 그래서 2. 지지선 / 저항선 요약의 어떤 레벨도 참고선으로 격하하지 않았다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-25~2026-08-24. 수집 시점: 2026-08-24. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py KMI --name "Kinder Morgan" --close-on 2026-08-21 --emit all` (레벨 날짜는 `--emit dates`로 별도 조회). 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **마지막 봉이 확정 종가가 아니다** — 위 ??? 블록 참고. 다음 갱신 시 이 봉의 값이 달라진다.
    - **기간 내 배당이 4회 지급됐으나 원주가 기준이라 반영되지 않았다.** 배당수익률이 3.8%대인 종목이므로, 총수익률(주가 + 배당)로 보면 이 차트가 보여주는 것보다 연간 약 4%p 높다.
    - 최근 3개년 내 주식분할·병합은 없어 가격 연속성을 깨는 이벤트는 없다([핵심 지표](./04_metrics.md) 상단 참고).
    - **이벤트 수직선은 넣지 않았다** — 3. 관측된 특이 구간에서 다루는 두 날짜(2025-10-23, 2026-01-22)는 레짐 전환이 아니라 레인지 내 확인 움직임이라 판단해, 차트를 단순하게 두었다.

---

## 관련 문서

- **먼저 읽기** — [최종 보고서](./11_final_report.md): 아래 문서 전체를 종합한 요약이라, 처음이라면 여기부터 봐도 된다
- **회사 이해** — [개요](./01_overview.md) · [역사 / 주요 이벤트](./02_history.md) · [CEO / 경영진](./03_ceo.md)
- **숫자** — [핵심 지표](./04_metrics.md) · [재무 / 실적](./05_financials.md) · [밸류에이션 / 적정주가](./06_valuation.md)
- **판단 · 로그** — [투자 판단](./07_investment.md) · [최근 뉴스 / 이슈](./08_news.md)
- **가격 차트** — [기술적 분석 — 주봉·5년](./10_technical_weekly.md)

---

## 참고 자료

- [Kinder Morgan (KMI) 주가 — Yahoo Finance (일봉 OHLCV 원자료)](https://finance.yahoo.com/quote/KMI/history/)
- [Kinder Morgan (KMI) — stockanalysis (주가 이력 대조용)](https://stockanalysis.com/stocks/kmi/)

---

*작성일: 2026-08-24*
