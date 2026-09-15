# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: warning 이 차트의 가격은 전부 분할 후 기준
2026-07-02 **4:1 분할**이 이 차트 기간 안에 있다. Yahoo Finance가 분할 전 구간을 소급 조정했으므로 시계열은 연속적이지만, **당시 실제 거래가격은 표시된 값의 4배**였다(예: 2025년 가을의 $119 구간은 당시 $476 부근). 4. 방법론 · 한계 참고.

:::
::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-15 종가 $242.49는 [핵심 지표 A.2 밸류에이션 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.**

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-16 ~ 2026-09-15)

<div class="crwd-chart">
<style>
.crwd-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .crwd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .crwd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.crwd-chart svg { width:100%; height:auto; display:block; }
.crwd-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.crwd-chart .title { fill: var(--ink); font-weight:600; }
.crwd-chart .grid { stroke: var(--grid); stroke-width:1; }
.crwd-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="크라우드스트라이크(CRWD) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">크라우드스트라이크 (CRWD) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-16 ~ 2026-09-15 · 마지막 종가 $242.49 (2026-09-15) · 단위 USD</text>
<line x1="60" y1="558.9" x2="1052" y2="558.9" class="grid"/>
<text x="52" y="562.9" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="475.1" x2="1052" y2="475.1" class="grid"/>
<text x="52" y="479.1" font-size="11" text-anchor="end" fill="var(--muted)">125</text>
<line x1="60" y1="391.3" x2="1052" y2="391.3" class="grid"/>
<text x="52" y="395.3" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="307.5" x2="1052" y2="307.5" class="grid"/>
<text x="52" y="311.5" font-size="11" text-anchor="end" fill="var(--muted)">175</text>
<line x1="60" y1="223.6" x2="1052" y2="223.6" class="grid"/>
<text x="52" y="227.6" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="139.8" x2="1052" y2="139.8" class="grid"/>
<text x="52" y="143.8" font-size="11" text-anchor="end" fill="var(--muted)">225</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="105.5" y1="626.0" x2="105.5" y2="631.0" class="axis"/>
<text x="105.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="196.4" y1="626.0" x2="196.4" y2="631.0" class="axis"/>
<text x="196.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="271.4" y1="626.0" x2="271.4" y2="631.0" class="axis"/>
<text x="271.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="358.4" y1="626.0" x2="358.4" y2="631.0" class="axis"/>
<text x="358.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="437.4" y1="626.0" x2="437.4" y2="631.0" class="axis"/>
<text x="437.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="512.5" y1="626.0" x2="512.5" y2="631.0" class="axis"/>
<text x="512.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="599.5" y1="626.0" x2="599.5" y2="631.0" class="axis"/>
<text x="599.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="682.5" y1="626.0" x2="682.5" y2="631.0" class="axis"/>
<text x="682.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="761.5" y1="626.0" x2="761.5" y2="631.0" class="axis"/>
<text x="761.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="844.5" y1="626.0" x2="844.5" y2="631.0" class="axis"/>
<text x="844.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="931.5" y1="626.0" x2="931.5" y2="631.0" class="axis"/>
<text x="931.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1014.5" y1="626.0" x2="1014.5" y2="631.0" class="axis"/>
<text x="1014.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="76.2" x2="1052" y2="76.2" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="79.2" font-size="10.5" fill="var(--muted)">$244 52주 최고</text>
<line x1="60" y1="607.0" x2="1052" y2="607.0" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="610.0" font-size="10.5" fill="var(--muted)">$86 52주 최저</text>
<line x1="998.6" y1="56.0" x2="998.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="1004.6" y="68.0" font-size="10.5" fill="var(--down)">2026-08-26 FY2027 2분기 실적발표</text>
<line x1="848.5" y1="56.0" x2="848.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="854.5" y="68.0" font-size="10.5" fill="var(--down)">2026-07-02 4:1 주식분할</text>
<line x1="62.0" y1="518.4" x2="62.0" y2="529.8" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="521.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="65.9" y1="513.7" x2="65.9" y2="530.2" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="520.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="69.9" y1="471.6" x2="69.9" y2="506.9" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="472.9" width="2.45" height="28.3" fill="var(--up)"/>
<line x1="73.8" y1="469.1" x2="73.8" y2="478.6" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="473.0" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="77.8" y1="474.9" x2="77.8" y2="486.6" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="478.5" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="81.7" y1="479.3" x2="81.7" y2="491.0" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="480.9" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="85.7" y1="486.0" x2="85.7" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="489.9" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="89.6" y1="490.6" x2="89.6" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="494.5" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="93.6" y1="488.8" x2="93.6" y2="500.0" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="490.7" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="97.5" y1="483.1" x2="97.5" y2="489.7" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="484.8" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="101.5" y1="482.8" x2="101.5" y2="492.5" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="483.2" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="105.5" y1="474.4" x2="105.5" y2="487.4" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="475.2" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="109.4" y1="473.2" x2="109.4" y2="481.5" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="474.1" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="113.4" y1="473.6" x2="113.4" y2="486.6" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="475.3" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="117.3" y1="472.2" x2="117.3" y2="479.8" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="478.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="121.3" y1="476.9" x2="121.3" y2="494.8" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="477.6" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="125.2" y1="466.7" x2="125.2" y2="483.2" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="466.8" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="129.2" y1="465.5" x2="129.2" y2="473.5" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="466.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="133.1" y1="460.5" x2="133.1" y2="480.7" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="467.6" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="137.1" y1="465.7" x2="137.1" y2="477.2" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="467.9" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="141.0" y1="474.7" x2="141.0" y2="485.5" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="475.0" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="145.0" y1="478.9" x2="145.0" y2="487.9" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="480.1" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="148.9" y1="476.5" x2="148.9" y2="495.7" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="483.7" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="152.9" y1="486.9" x2="152.9" y2="495.7" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="488.0" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="156.8" y1="471.4" x2="156.8" y2="486.5" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="472.1" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="160.8" y1="468.7" x2="160.8" y2="476.5" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="471.8" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="164.7" y1="470.6" x2="164.7" y2="482.1" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="472.9" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="168.7" y1="456.3" x2="168.7" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="456.7" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="172.6" y1="445.3" x2="172.6" y2="456.8" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="451.0" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="176.6" y1="446.3" x2="176.6" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="447.8" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="180.5" y1="430.2" x2="180.5" y2="445.0" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="435.8" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="184.5" y1="434.0" x2="184.5" y2="447.2" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="437.0" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="188.4" y1="433.2" x2="188.4" y2="446.5" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="439.0" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="192.4" y1="433.6" x2="192.4" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="439.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="196.4" y1="428.3" x2="196.4" y2="437.3" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="431.6" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="200.3" y1="433.6" x2="200.3" y2="449.0" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="441.8" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="204.3" y1="445.6" x2="204.3" y2="453.3" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="446.5" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="208.2" y1="441.6" x2="208.2" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="447.9" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="212.2" y1="439.7" x2="212.2" y2="459.1" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="441.7" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="216.1" y1="425.7" x2="216.1" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="426.9" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="220.1" y1="426.1" x2="220.1" y2="432.2" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="427.6" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="224.0" y1="419.0" x2="224.0" y2="437.4" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="423.9" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="228.0" y1="438.4" x2="228.0" y2="453.2" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="440.8" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="231.9" y1="438.2" x2="231.9" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="443.6" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="235.9" y1="441.0" x2="235.9" y2="452.8" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="444.1" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="239.8" y1="448.9" x2="239.8" y2="464.2" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="454.3" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="243.8" y1="453.3" x2="243.8" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="457.9" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="247.7" y1="442.2" x2="247.7" y2="475.0" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="447.8" width="2.45" height="26.2" fill="var(--down)"/>
<line x1="251.7" y1="474.3" x2="251.7" y2="493.9" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="476.9" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="255.6" y1="467.4" x2="255.6" y2="480.1" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="469.4" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="259.6" y1="463.6" x2="259.6" y2="481.0" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="464.8" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="263.5" y1="462.5" x2="263.5" y2="477.6" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="464.2" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="267.5" y1="466.2" x2="267.5" y2="473.5" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="467.4" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="271.4" y1="469.5" x2="271.4" y2="479.3" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="471.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="275.4" y1="457.5" x2="275.4" y2="469.2" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="461.2" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="279.3" y1="454.2" x2="279.3" y2="486.6" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="454.9" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="283.3" y1="453.9" x2="283.3" y2="466.5" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="455.1" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="287.3" y1="452.6" x2="287.3" y2="468.1" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="461.6" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="291.2" y1="458.1" x2="291.2" y2="467.7" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="462.4" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="295.2" y1="450.1" x2="295.2" y2="465.3" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="460.0" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="299.1" y1="457.0" x2="299.1" y2="471.3" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="458.7" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="303.1" y1="451.5" x2="303.1" y2="464.6" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="460.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="307.0" y1="460.5" x2="307.0" y2="476.2" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="461.4" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="311.0" y1="467.6" x2="311.0" y2="485.7" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="467.6" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="314.9" y1="482.3" x2="314.9" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="484.7" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="318.9" y1="483.1" x2="318.9" y2="500.4" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="484.0" width="2.45" height="16.3" fill="var(--down)"/>
<line x1="322.8" y1="490.2" x2="322.8" y2="497.0" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="492.1" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="326.8" y1="484.2" x2="326.8" y2="493.0" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="490.8" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="330.7" y1="487.0" x2="330.7" y2="496.2" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="489.3" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="334.7" y1="488.9" x2="334.7" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="489.8" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="338.6" y1="493.6" x2="338.6" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="494.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="342.6" y1="490.1" x2="342.6" y2="495.9" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="490.9" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="346.5" y1="489.1" x2="346.5" y2="496.4" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="493.3" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="350.5" y1="493.5" x2="350.5" y2="498.4" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="495.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="354.4" y1="495.2" x2="354.4" y2="501.6" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="495.3" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="358.4" y1="496.9" x2="358.4" y2="517.5" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="496.9" width="2.45" height="17.1" fill="var(--down)"/>
<line x1="362.3" y1="503.2" x2="362.3" y2="512.8" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="509.8" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="366.3" y1="508.3" x2="366.3" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="510.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="370.2" y1="486.4" x2="370.2" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="492.8" width="2.45" height="13.4" fill="var(--up)"/>
<line x1="374.2" y1="491.9" x2="374.2" y2="508.1" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="493.4" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="378.2" y1="495.3" x2="378.2" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="498.4" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="382.1" y1="501.4" x2="382.1" y2="508.9" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="502.8" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="386.1" y1="494.8" x2="386.1" y2="507.9" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="501.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="390.0" y1="494.4" x2="390.0" y2="515.6" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="503.8" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="394.0" y1="498.3" x2="394.0" y2="517.0" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="505.3" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="397.9" y1="508.9" x2="397.9" y2="522.4" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="511.4" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="401.9" y1="516.8" x2="401.9" y2="525.2" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="522.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="405.8" y1="511.9" x2="405.8" y2="526.1" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="520.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="409.8" y1="513.3" x2="409.8" y2="520.1" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="513.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="413.7" y1="509.6" x2="413.7" y2="517.5" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="513.1" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="417.7" y1="500.3" x2="417.7" y2="514.9" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="501.7" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="421.6" y1="485.8" x2="421.6" y2="497.4" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="493.2" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="425.6" y1="486.0" x2="425.6" y2="501.2" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="492.3" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="429.5" y1="507.3" x2="429.5" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="508.0" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="433.5" y1="518.1" x2="433.5" y2="526.9" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="524.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="437.4" y1="519.3" x2="437.4" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="525.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="441.4" y1="528.2" x2="441.4" y2="546.3" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="528.8" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="445.3" y1="540.5" x2="445.3" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="546.1" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="449.3" y1="545.3" x2="449.3" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="546.5" width="2.45" height="31.5" fill="var(--down)"/>
<line x1="453.2" y1="561.5" x2="453.2" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="562.7" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="457.2" y1="549.9" x2="457.2" y2="570.5" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="552.2" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="461.1" y1="543.1" x2="461.1" y2="558.3" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="547.7" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="465.1" y1="545.0" x2="465.1" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="545.7" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="469.1" y1="541.6" x2="469.1" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="543.1" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="473.0" y1="531.4" x2="473.0" y2="548.4" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="534.1" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="477.0" y1="537.2" x2="477.0" y2="558.9" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="539.2" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="480.9" y1="540.7" x2="480.9" y2="557.3" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="545.7" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="484.9" y1="538.8" x2="484.9" y2="550.6" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="540.4" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="488.8" y1="532.2" x2="488.8" y2="569.7" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="542.8" width="2.45" height="25.7" fill="var(--down)"/>
<line x1="492.8" y1="571.4" x2="492.8" y2="607.0" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="571.5" width="2.45" height="29.0" fill="var(--down)"/>
<line x1="496.7" y1="591.7" x2="496.7" y2="605.0" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="600.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="500.7" y1="587.5" x2="500.7" y2="603.8" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="589.7" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="504.6" y1="571.4" x2="504.6" y2="588.6" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="574.8" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="508.6" y1="581.2" x2="508.6" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="582.4" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="512.5" y1="569.7" x2="512.5" y2="581.5" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="571.6" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="516.5" y1="563.2" x2="516.5" y2="585.8" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="566.1" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="520.4" y1="551.9" x2="520.4" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="552.5" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="524.4" y1="534.1" x2="524.4" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="537.0" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="528.3" y1="530.7" x2="528.3" y2="542.0" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="534.6" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="532.3" y1="526.9" x2="532.3" y2="537.5" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="530.3" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="536.2" y1="518.7" x2="536.2" y2="535.0" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="521.2" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="540.2" y1="515.4" x2="540.2" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="523.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="544.1" y1="517.0" x2="544.1" y2="526.8" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="524.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="548.1" y1="516.5" x2="548.1" y2="530.0" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="522.1" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="552.0" y1="522.5" x2="552.0" y2="539.0" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="522.9" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="556.0" y1="526.2" x2="556.0" y2="542.5" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="531.1" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="560.0" y1="523.4" x2="560.0" y2="535.5" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="528.9" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="563.9" y1="524.8" x2="563.9" y2="539.3" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="526.2" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="567.9" y1="538.6" x2="567.9" y2="555.9" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="539.1" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="571.8" y1="544.3" x2="571.8" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="547.8" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="575.8" y1="549.8" x2="575.8" y2="566.8" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="550.2" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="579.7" y1="558.7" x2="579.7" y2="572.8" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="559.8" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="583.7" y1="562.7" x2="583.7" y2="574.7" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="565.1" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="587.6" y1="580.3" x2="587.6" y2="591.0" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="583.4" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="591.6" y1="566.9" x2="591.6" y2="578.7" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="575.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="595.5" y1="564.9" x2="595.5" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="567.0" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="599.5" y1="561.5" x2="599.5" y2="570.4" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="561.7" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="603.4" y1="558.3" x2="603.4" y2="570.0" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="559.7" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="607.4" y1="554.8" x2="607.4" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="554.8" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="611.3" y1="539.0" x2="611.3" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="539.5" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="615.3" y1="517.1" x2="615.3" y2="539.4" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="525.4" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="619.2" y1="536.3" x2="619.2" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="537.2" width="2.45" height="26.2" fill="var(--down)"/>
<line x1="623.2" y1="560.6" x2="623.2" y2="588.7" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="562.2" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="627.1" y1="556.4" x2="627.1" y2="577.2" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="557.1" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="631.1" y1="549.4" x2="631.1" y2="564.5" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="555.0" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="635.0" y1="548.9" x2="635.0" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="549.6" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="639.0" y1="537.3" x2="639.0" y2="549.6" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="540.6" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="642.9" y1="532.3" x2="642.9" y2="541.9" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="534.7" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="646.9" y1="530.6" x2="646.9" y2="544.7" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="531.2" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="650.9" y1="509.4" x2="650.9" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="517.4" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="654.8" y1="502.0" x2="654.8" y2="514.8" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="503.0" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="658.8" y1="513.7" x2="658.8" y2="528.3" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="514.0" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="662.7" y1="516.2" x2="662.7" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="518.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="666.7" y1="510.3" x2="666.7" y2="523.2" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="513.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="670.6" y1="505.6" x2="670.6" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="510.6" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="674.6" y1="514.4" x2="674.6" y2="522.7" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="515.0" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="678.5" y1="517.0" x2="678.5" y2="531.7" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="519.5" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="682.5" y1="510.3" x2="682.5" y2="520.7" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="512.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="686.4" y1="498.7" x2="686.4" y2="512.5" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="500.9" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="690.4" y1="491.3" x2="690.4" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="494.8" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="694.3" y1="495.8" x2="694.3" y2="510.8" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="501.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="698.3" y1="469.4" x2="698.3" y2="486.8" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="470.3" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="702.2" y1="450.9" x2="702.2" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="451.8" width="2.45" height="24.0" fill="var(--up)"/>
<line x1="706.2" y1="439.4" x2="706.2" y2="456.7" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="439.7" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="710.1" y1="431.2" x2="710.1" y2="447.5" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="436.4" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="714.1" y1="417.8" x2="714.1" y2="443.0" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="422.7" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="718.0" y1="404.9" x2="718.0" y2="429.0" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="408.1" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="722.0" y1="392.8" x2="722.0" y2="424.2" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="396.3" width="2.45" height="17.5" fill="var(--up)"/>
<line x1="725.9" y1="373.6" x2="725.9" y2="401.9" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="375.5" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="729.9" y1="362.6" x2="729.9" y2="380.2" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="374.5" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="733.8" y1="348.5" x2="733.8" y2="379.5" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="349.3" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="737.8" y1="341.4" x2="737.8" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="348.9" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="741.8" y1="328.6" x2="741.8" y2="349.7" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="338.1" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="745.7" y1="326.3" x2="745.7" y2="351.1" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="331.3" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="749.7" y1="340.4" x2="749.7" y2="363.6" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="353.3" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="753.6" y1="326.3" x2="753.6" y2="356.5" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="331.8" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="757.6" y1="281.1" x2="757.6" y2="328.5" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="281.5" width="2.45" height="44.9" fill="var(--up)"/>
<line x1="761.5" y1="235.7" x2="761.5" y2="279.0" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="238.6" width="2.45" height="38.9" fill="var(--up)"/>
<line x1="765.5" y1="241.4" x2="765.5" y2="269.4" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="249.7" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="769.4" y1="251.3" x2="769.4" y2="272.2" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="252.4" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="773.4" y1="289.9" x2="773.4" y2="331.7" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="291.5" width="2.45" height="37.7" fill="var(--up)"/>
<line x1="777.3" y1="302.3" x2="777.3" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="310.2" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="781.3" y1="320.9" x2="781.3" y2="347.7" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="329.7" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="785.2" y1="336.9" x2="785.2" y2="376.4" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="342.0" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="789.2" y1="339.2" x2="789.2" y2="361.2" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="351.3" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="793.1" y1="310.5" x2="793.1" y2="356.9" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="314.6" width="2.45" height="38.8" fill="var(--up)"/>
<line x1="797.1" y1="305.7" x2="797.1" y2="325.9" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="315.3" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="801.0" y1="309.6" x2="801.0" y2="333.6" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="313.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="805.0" y1="306.7" x2="805.0" y2="336.0" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="313.3" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="808.9" y1="315.1" x2="808.9" y2="331.9" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="321.8" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="812.9" y1="310.9" x2="812.9" y2="340.2" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="318.6" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="816.8" y1="297.3" x2="816.8" y2="329.9" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="320.0" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="820.8" y1="315.1" x2="820.8" y2="339.3" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="323.5" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="824.7" y1="318.2" x2="824.7" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="323.8" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="828.7" y1="313.6" x2="828.7" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="323.9" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="832.7" y1="303.4" x2="832.7" y2="329.6" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="306.6" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="836.6" y1="260.5" x2="836.6" y2="304.0" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="271.5" width="2.45" height="28.0" fill="var(--up)"/>
<line x1="840.6" y1="252.7" x2="840.6" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="254.5" width="2.45" height="22.3" fill="var(--up)"/>
<line x1="844.5" y1="235.4" x2="844.5" y2="253.0" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="244.6" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="848.5" y1="225.2" x2="848.5" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="243.8" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="852.4" y1="191.8" x2="852.4" y2="262.0" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="225.7" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="856.4" y1="219.1" x2="856.4" y2="249.7" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="221.3" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="860.3" y1="238.2" x2="860.3" y2="272.9" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="245.4" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="864.3" y1="227.8" x2="864.3" y2="267.2" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="229.0" width="2.45" height="33.8" fill="var(--up)"/>
<line x1="868.2" y1="230.4" x2="868.2" y2="269.0" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="235.0" width="2.45" height="31.6" fill="var(--down)"/>
<line x1="872.2" y1="259.7" x2="872.2" y2="287.4" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="264.2" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="876.1" y1="186.8" x2="876.1" y2="259.0" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="187.7" width="2.45" height="66.2" fill="var(--up)"/>
<line x1="880.1" y1="165.0" x2="880.1" y2="206.5" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="182.1" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="884.0" y1="197.9" x2="884.0" y2="223.4" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="199.6" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="888.0" y1="191.8" x2="888.0" y2="225.3" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="213.3" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="891.9" y1="196.0" x2="891.9" y2="231.0" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="213.3" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="895.9" y1="223.6" x2="895.9" y2="258.2" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="224.3" width="2.45" height="29.0" fill="var(--down)"/>
<line x1="899.8" y1="245.5" x2="899.8" y2="273.8" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="248.6" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="903.8" y1="256.5" x2="903.8" y2="284.7" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="258.8" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="907.7" y1="271.1" x2="907.7" y2="284.6" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="273.9" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="911.7" y1="262.2" x2="911.7" y2="292.4" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="264.2" width="2.45" height="26.1" fill="var(--down)"/>
<line x1="915.6" y1="275.1" x2="915.6" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="284.7" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="919.6" y1="269.3" x2="919.6" y2="302.6" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="281.9" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="923.6" y1="272.4" x2="923.6" y2="298.3" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="273.2" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="927.5" y1="251.7" x2="927.5" y2="276.8" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="254.3" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="931.5" y1="213.0" x2="931.5" y2="248.5" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="215.1" width="2.45" height="28.5" fill="var(--up)"/>
<line x1="935.4" y1="181.3" x2="935.4" y2="211.9" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="186.0" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="939.4" y1="158.8" x2="939.4" y2="191.6" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="178.2" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="943.3" y1="198.1" x2="943.3" y2="217.8" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="198.9" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="947.3" y1="168.1" x2="947.3" y2="196.2" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="175.3" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="951.2" y1="133.5" x2="951.2" y2="174.9" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="139.3" width="2.45" height="33.0" fill="var(--up)"/>
<line x1="955.2" y1="138.1" x2="955.2" y2="159.1" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="143.2" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="959.1" y1="140.0" x2="959.1" y2="163.7" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="150.6" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="963.1" y1="134.2" x2="963.1" y2="155.8" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="138.0" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="967.0" y1="131.4" x2="967.0" y2="168.4" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="134.3" width="2.45" height="32.5" fill="var(--down)"/>
<line x1="971.0" y1="159.3" x2="971.0" y2="180.0" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="168.2" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="974.9" y1="169.8" x2="974.9" y2="193.2" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="180.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="978.9" y1="176.8" x2="978.9" y2="232.9" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="178.8" width="2.45" height="39.4" fill="var(--down)"/>
<line x1="982.8" y1="221.2" x2="982.8" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="232.8" width="2.45" height="23.3" fill="var(--down)"/>
<line x1="986.8" y1="247.6" x2="986.8" y2="267.2" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="250.6" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="990.7" y1="239.1" x2="990.7" y2="262.4" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="254.9" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="994.7" y1="242.1" x2="994.7" y2="282.8" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="251.7" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="998.6" y1="252.8" x2="998.6" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="259.9" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="1002.6" y1="126.1" x2="1002.6" y2="203.2" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="129.9" width="2.45" height="66.1" fill="var(--up)"/>
<line x1="1006.5" y1="127.5" x2="1006.5" y2="188.3" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="129.0" width="2.45" height="33.0" fill="var(--down)"/>
<line x1="1010.5" y1="110.0" x2="1010.5" y2="153.2" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="119.7" width="2.45" height="30.7" fill="var(--up)"/>
<line x1="1014.5" y1="118.7" x2="1014.5" y2="181.2" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="129.8" width="2.45" height="43.4" fill="var(--down)"/>
<line x1="1018.4" y1="173.9" x2="1018.4" y2="221.6" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="176.0" width="2.45" height="36.2" fill="var(--down)"/>
<line x1="1022.4" y1="173.0" x2="1022.4" y2="211.0" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="173.5" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="1026.3" y1="162.3" x2="1026.3" y2="185.7" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="179.7" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="1030.3" y1="184.5" x2="1030.3" y2="205.5" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="190.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1034.2" y1="180.8" x2="1034.2" y2="200.2" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="188.5" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="1038.2" y1="174.4" x2="1038.2" y2="209.3" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="193.9" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="1042.1" y1="179.4" x2="1042.1" y2="208.8" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="196.7" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="1046.1" y1="91.6" x2="1046.1" y2="169.8" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="105.0" width="2.45" height="54.9" fill="var(--up)"/>
<line x1="1050.0" y1="76.2" x2="1050.0" y2="116.0" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="81.2" width="2.45" height="32.6" fill="var(--up)"/>
<line x1="60" y1="287.0" x2="1052" y2="287.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="281.0" font-size="11.5" fill="var(--support)" font-weight="600">$181 S1</text>
<text x="1058" y="293.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="494.3" x2="1052" y2="494.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="488.3" font-size="11.5" fill="var(--support)" font-weight="600">$119 S2</text>
<text x="1058" y="500.3" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="528.9" x2="1052" y2="528.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="522.9" font-size="11.5" fill="var(--support)" font-weight="600">$109 S3</text>
<text x="1058" y="534.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="81.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="73.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $242 (2026-09-15)</text>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$242.49** (2026-09-15 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $181 | 2 | 2026-07-13·2026-08-26 — 4:1 분할(2026-07-02) 직후부터 FY2027 2분기 실적발표 전날까지 머물던 가격대 |
| S2 | $119 | 5 | 2025-10-07·2025-10-16·2025-11-21·2025-12-03·2025-12-17 — 2025년 가을~겨울 석 달간의 박스권 하단(터치 5회로 이 표에서 가장 두껍다) |
| S3 | $109 | 2 | 2026-01-21·2026-04-30 — 2026년 초 조정 구간의 저점대 |
| 참고선 | $244 | — | 52주 최고 — 52주 최고 — 현재가($242.49)와 0.6% 차이로 사실상 신고가 부근이다. **터치가 1회뿐이라 클러스터로 잡히지 않았다** |
| 참고선 | $86 | — | 52주 최저 — 52주 최저 — 현재가 대비 65% 아래라 근시일 지지로 기능할 구간이 아니다 |

**저항선이 하나도 잡히지 않았다** — 현재가가 52주 최고($243.98)의 0.6% 아래라 위쪽에 가격 기억이 없기 때문이다. 이 표를 "저항이 없으니 더 오른다"로 읽어서는 안 되며, **참조할 가격대가 없는 구간**이라는 뜻으로만 읽는다.

주목할 것은 **S1($181)과 현재가 사이의 25% 공백**이다. 아래 3절의 갭업 한 번으로 만들어진 빈 구간이라, 이 사이에는 매수 단가가 거의 쌓여 있지 않다.

---

## 3. 관측된 특이 구간 — 2026-08-27 FY2027 2분기 실적발표 갭업

- 2026-08-26 장 마감 후 FY2027 2분기 실적을 발표했다([최근 뉴스 / 이슈](./08_news.md) 로그 참고). 분기 순증 ARR이 사상 최대인 $332.8M(+51%)을 기록했고, 회사는 연간 순증 ARR 성장 가이던스를 630bp 상향했다.
- 종가 기준 전일 대비 **+20.5%** ($189.18 → $227.96). 단일 거래일 상승으로는 이 차트 기간 중 가장 크다.
- **이 하루가 현재 가격대를 만들었다.** 갭업 이전 약 두 달간 $181~$190 구간에 머물렀고(S1 클러스터), 갭 이후 $218~$243 구간으로 올라선 뒤 내려오지 않았다 — 그래서 **$190~$218 사이에 지지 클러스터가 전혀 형성되지 않았다.** 되돌림이 시작되면 S1($181)까지 참조할 가격대가 없다는 뜻이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-16~2026-09-15. 수집 시점: 2026-09-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py CRWD --name "크라우드스트라이크" --event 2026-08-26:"FY2027 2분기 실적발표" --event 2026-07-02:"4:1 주식분할" --ref-line 243.98:"52주 최고" --ref-line 85.68:"52주 최저" --close-on 2026-09-15 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3절의 갭업이 레벨 해석을 크게 제약한다.** $190~$218 구간에 거래가 사실상 없어 지지선이 비어 있고, S1($181)은 현재가에서 25% 아래다.
    - **주식분할**: 이 기간 안에 **2026-07-02 4:1 분할**이 있다. 차트 가격은 Yahoo Finance가 분할 전 구간을 **소급 조정한 값**이며, [핵심 지표](./04_metrics.md)의 주당 수치와 같은 기준(분할 후)이다. 분할 자체는 가격 연속성을 깨지 않았다 — 분할 전날(2026-07-01) 종가 $193.18과 당일(2026-07-02) 종가 $193.98이 이어진다.

---

*작성일: 2026-09-16*
