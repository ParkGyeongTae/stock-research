# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, Yahoo Finance 일봉 API에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). **겹치는 시점 종가 대조**: 2026-08-18 종가는 이 문서 기준 $175.70(Yahoo Finance), 핵심 지표·밸류에이션 / 적정주가가 인용한 stockanalysis.com 기준 $175.70과 정확히 일치.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-19 ~ 2026-08-18)

<div class="leu-chart">
<style>
.leu-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .leu-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .leu-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.leu-chart svg { width:100%; height:auto; display:block; }
.leu-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.leu-chart .title { fill: var(--ink); font-weight:600; }
.leu-chart .grid { stroke: var(--grid); stroke-width:1; }
.leu-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Centrus Energy(LEU) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Centrus Energy (LEU) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-19 ~ 2026-08-18 · 마지막 종가 $175.70 (2026-08-18) · 단위 USD</text>
<line x1="60" y1="593.0" x2="1052" y2="593.0" class="grid"/>
<text x="52" y="597.0" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="510.3" x2="1052" y2="510.3" class="grid"/>
<text x="52" y="514.3" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="427.7" x2="1052" y2="427.7" class="grid"/>
<text x="52" y="431.7" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="345.1" x2="1052" y2="345.1" class="grid"/>
<text x="52" y="349.1" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="262.5" x2="1052" y2="262.5" class="grid"/>
<text x="52" y="266.5" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="179.9" x2="1052" y2="179.9" class="grid"/>
<text x="52" y="183.9" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="97.3" x2="1052" y2="97.3" class="grid"/>
<text x="52" y="101.3" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="97.5" y1="626.0" x2="97.5" y2="631.0" class="axis"/>
<text x="97.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="180.5" y1="626.0" x2="180.5" y2="631.0" class="axis"/>
<text x="180.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="271.4" y1="626.0" x2="271.4" y2="631.0" class="axis"/>
<text x="271.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="346.5" y1="626.0" x2="346.5" y2="631.0" class="axis"/>
<text x="346.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="433.5" y1="626.0" x2="433.5" y2="631.0" class="axis"/>
<text x="433.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="512.5" y1="626.0" x2="512.5" y2="631.0" class="axis"/>
<text x="512.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="587.6" y1="626.0" x2="587.6" y2="631.0" class="axis"/>
<text x="587.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="674.6" y1="626.0" x2="674.6" y2="631.0" class="axis"/>
<text x="674.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="757.6" y1="626.0" x2="757.6" y2="631.0" class="axis"/>
<text x="757.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="836.6" y1="626.0" x2="836.6" y2="631.0" class="axis"/>
<text x="836.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="919.6" y1="626.0" x2="919.6" y2="631.0" class="axis"/>
<text x="919.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="1006.5" y1="626.0" x2="1006.5" y2="631.0" class="axis"/>
<text x="1006.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="73.8" x2="1052" y2="73.8" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="76.8" font-size="10.5" fill="var(--muted)">$464 52주 최고</text>
<line x1="437.4" y1="56.0" x2="437.4" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="443.4" y="68.0" font-size="10.5" fill="var(--down)">2026-01-05 DOE $900M HALEU 증설 계약 발표</text>
<line x1="765.5" y1="56.0" x2="765.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="771.5" y="68.0" font-size="10.5" fill="var(--down)">2026-05-05 1분기 실적 발표(EPS 급감, -8.8%)</text>
<line x1="1014.5" y1="56.0" x2="1014.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="1020.5" y="68.0" font-size="10.5" fill="var(--down)">2026-08-05 2분기 실적+DOE 옵션 미행사 통보</text>
<line x1="62.0" y1="545.0" x2="62.0" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="545.5" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="65.9" y1="547.2" x2="65.9" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="550.0" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="69.9" y1="543.5" x2="69.9" y2="553.6" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="547.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="73.8" y1="523.6" x2="73.8" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="532.7" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="77.8" y1="521.7" x2="77.8" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="523.6" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="81.7" y1="491.3" x2="81.7" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="496.0" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="85.7" y1="493.0" x2="85.7" y2="514.2" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="501.1" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="89.6" y1="485.1" x2="89.6" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="494.9" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="93.6" y1="490.5" x2="93.6" y2="518.6" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="491.0" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="97.5" y1="502.1" x2="97.5" y2="532.7" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="503.9" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="101.5" y1="493.9" x2="101.5" y2="513.9" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="498.0" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="105.5" y1="500.6" x2="105.5" y2="513.6" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="507.0" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="109.4" y1="501.4" x2="109.4" y2="524.1" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="501.4" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="113.4" y1="496.8" x2="113.4" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="501.3" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="117.3" y1="470.7" x2="117.3" y2="506.3" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="480.8" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="121.3" y1="468.2" x2="121.3" y2="484.3" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="474.8" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="125.2" y1="456.4" x2="125.2" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="470.2" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="129.2" y1="464.1" x2="129.2" y2="477.5" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="473.8" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="133.1" y1="438.0" x2="133.1" y2="477.1" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="438.5" width="2.45" height="34.3" fill="var(--up)"/>
<line x1="137.1" y1="438.9" x2="137.1" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="439.3" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="141.0" y1="452.5" x2="141.0" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="455.8" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="145.0" y1="403.2" x2="145.0" y2="458.1" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="406.8" width="2.45" height="44.0" fill="var(--up)"/>
<line x1="148.9" y1="342.5" x2="148.9" y2="411.2" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="354.2" width="2.45" height="57.0" fill="var(--up)"/>
<line x1="152.9" y1="324.4" x2="152.9" y2="373.9" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="334.9" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="156.8" y1="325.3" x2="156.8" y2="353.3" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="328.6" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="160.8" y1="336.9" x2="160.8" y2="384.8" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="339.4" width="2.45" height="45.4" fill="var(--down)"/>
<line x1="164.7" y1="315.3" x2="164.7" y2="408.6" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="325.0" width="2.45" height="77.6" fill="var(--up)"/>
<line x1="168.7" y1="282.3" x2="168.7" y2="350.1" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="318.4" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="172.6" y1="308.8" x2="172.6" y2="346.0" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="317.5" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="176.6" y1="310.8" x2="176.6" y2="335.2" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="328.5" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="180.5" y1="287.7" x2="180.5" y2="339.2" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="293.7" width="2.45" height="44.8" fill="var(--up)"/>
<line x1="184.5" y1="262.5" x2="184.5" y2="303.0" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="264.0" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="188.4" y1="245.8" x2="188.4" y2="288.9" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="260.0" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="192.4" y1="243.7" x2="192.4" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="252.1" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="196.4" y1="198.7" x2="196.4" y2="251.0" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="229.4" width="2.45" height="20.1" fill="var(--up)"/>
<line x1="200.3" y1="203.0" x2="200.3" y2="247.6" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="214.8" width="2.45" height="24.2" fill="var(--down)"/>
<line x1="204.3" y1="197.4" x2="204.3" y2="241.1" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="227.7" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="208.2" y1="141.5" x2="208.2" y2="241.6" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="211.3" width="2.45" height="28.5" fill="var(--down)"/>
<line x1="212.2" y1="130.3" x2="212.2" y2="201.3" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="155.5" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="216.1" y1="154.9" x2="216.1" y2="229.5" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="186.3" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="220.1" y1="80.0" x2="220.1" y2="159.8" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="120.4" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="224.0" y1="73.8" x2="224.0" y2="170.0" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="90.7" width="2.45" height="63.7" fill="var(--down)"/>
<line x1="228.0" y1="160.9" x2="228.0" y2="236.7" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="182.1" width="2.45" height="30.6" fill="var(--down)"/>
<line x1="231.9" y1="165.1" x2="231.9" y2="225.2" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="179.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="235.9" y1="188.2" x2="235.9" y2="233.2" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="204.7" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="239.8" y1="237.7" x2="239.8" y2="355.3" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="260.5" width="2.45" height="60.1" fill="var(--down)"/>
<line x1="243.8" y1="262.6" x2="243.8" y2="331.9" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="272.1" width="2.45" height="40.0" fill="var(--up)"/>
<line x1="247.7" y1="199.7" x2="247.7" y2="255.9" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="208.0" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="251.7" y1="193.5" x2="251.7" y2="261.5" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="194.5" width="2.45" height="51.9" fill="var(--down)"/>
<line x1="255.6" y1="209.2" x2="255.6" y2="255.7" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="222.9" width="2.45" height="17.0" fill="var(--down)"/>
<line x1="259.6" y1="176.6" x2="259.6" y2="252.6" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="195.1" width="2.45" height="40.6" fill="var(--up)"/>
<line x1="263.5" y1="189.9" x2="263.5" y2="227.8" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="207.5" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="267.5" y1="196.4" x2="267.5" y2="245.7" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="203.0" width="2.45" height="30.6" fill="var(--down)"/>
<line x1="271.4" y1="242.6" x2="271.4" y2="292.3" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="261.3" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="275.4" y1="279.0" x2="275.4" y2="325.3" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="300.2" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="279.3" y1="280.9" x2="279.3" y2="310.4" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="293.9" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="283.3" y1="345.3" x2="283.3" y2="401.3" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="366.0" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="287.3" y1="346.8" x2="287.3" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="354.8" width="2.45" height="66.1" fill="var(--up)"/>
<line x1="291.2" y1="316.8" x2="291.2" y2="377.4" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="330.3" width="2.45" height="31.0" fill="var(--down)"/>
<line x1="295.2" y1="371.9" x2="295.2" y2="399.4" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="379.7" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="299.1" y1="371.7" x2="299.1" y2="400.0" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="383.0" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="303.1" y1="396.3" x2="303.1" y2="431.3" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="405.3" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="307.0" y1="409.6" x2="307.0" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="427.7" width="2.45" height="31.4" fill="var(--up)"/>
<line x1="311.0" y1="424.7" x2="311.0" y2="444.3" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="434.9" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="314.9" y1="425.6" x2="314.9" y2="451.9" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="434.2" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="318.9" y1="398.0" x2="318.9" y2="431.1" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="404.2" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="322.8" y1="368.3" x2="322.8" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="373.3" width="2.45" height="68.8" fill="var(--down)"/>
<line x1="326.8" y1="438.2" x2="326.8" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="441.4" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="330.7" y1="422.8" x2="330.7" y2="452.5" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="428.0" width="2.45" height="21.2" fill="var(--up)"/>
<line x1="334.7" y1="423.6" x2="334.7" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="428.0" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="338.6" y1="414.0" x2="338.6" y2="427.2" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="420.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="342.6" y1="405.3" x2="342.6" y2="421.9" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="412.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="346.5" y1="415.5" x2="346.5" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="425.5" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="350.5" y1="393.0" x2="350.5" y2="423.6" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="402.0" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="354.4" y1="394.7" x2="354.4" y2="421.5" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="397.8" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="358.4" y1="368.3" x2="358.4" y2="404.6" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="380.4" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="362.3" y1="366.3" x2="362.3" y2="412.9" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="366.6" width="2.45" height="34.3" fill="var(--down)"/>
<line x1="366.3" y1="395.5" x2="366.3" y2="414.5" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="395.9" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="370.2" y1="400.0" x2="370.2" y2="414.5" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="403.5" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="374.2" y1="393.9" x2="374.2" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="403.7" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="378.2" y1="388.1" x2="378.2" y2="418.5" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="389.6" width="2.45" height="27.0" fill="var(--up)"/>
<line x1="382.1" y1="390.2" x2="382.1" y2="438.5" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="390.2" width="2.45" height="39.2" fill="var(--down)"/>
<line x1="386.1" y1="424.5" x2="386.1" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="427.3" width="2.45" height="35.5" fill="var(--down)"/>
<line x1="390.0" y1="449.4" x2="390.0" y2="476.9" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="451.2" width="2.45" height="21.8" fill="var(--up)"/>
<line x1="394.0" y1="442.1" x2="394.0" y2="475.9" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="451.1" width="2.45" height="24.4" fill="var(--down)"/>
<line x1="397.9" y1="447.6" x2="397.9" y2="476.5" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="461.3" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="401.9" y1="401.5" x2="401.9" y2="453.0" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="408.3" width="2.45" height="43.9" fill="var(--up)"/>
<line x1="405.8" y1="376.0" x2="405.8" y2="412.9" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="394.3" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="409.8" y1="396.1" x2="409.8" y2="422.6" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="414.4" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="413.7" y1="407.8" x2="413.7" y2="424.4" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="410.9" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="417.7" y1="410.6" x2="417.7" y2="434.5" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="410.6" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="421.6" y1="405.1" x2="421.6" y2="435.8" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="429.0" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="425.6" y1="419.9" x2="425.6" y2="438.4" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="429.9" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="429.5" y1="430.2" x2="429.5" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="432.6" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="433.5" y1="390.2" x2="433.5" y2="434.2" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="390.6" width="2.45" height="40.7" fill="var(--up)"/>
<line x1="437.4" y1="335.6" x2="437.4" y2="384.8" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="344.5" width="2.45" height="32.6" fill="var(--up)"/>
<line x1="441.4" y1="309.3" x2="441.4" y2="346.8" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="325.5" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="445.3" y1="301.6" x2="445.3" y2="335.2" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="307.2" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="449.3" y1="315.4" x2="449.3" y2="369.7" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="315.4" width="2.45" height="52.4" fill="var(--down)"/>
<line x1="453.2" y1="315.3" x2="453.2" y2="345.1" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="334.9" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="457.2" y1="318.9" x2="457.2" y2="351.7" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="329.8" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="461.1" y1="292.3" x2="461.1" y2="349.9" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="312.3" width="2.45" height="35.7" fill="var(--down)"/>
<line x1="465.1" y1="324.5" x2="465.1" y2="368.3" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="332.6" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="469.1" y1="289.8" x2="469.1" y2="338.8" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="321.6" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="473.0" y1="293.3" x2="473.0" y2="348.4" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="293.9" width="2.45" height="36.4" fill="var(--up)"/>
<line x1="477.0" y1="282.8" x2="477.0" y2="329.9" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="307.1" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="480.9" y1="269.8" x2="480.9" y2="361.5" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="296.9" width="2.45" height="41.8" fill="var(--down)"/>
<line x1="484.9" y1="313.7" x2="484.9" y2="355.7" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="336.9" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="488.8" y1="330.2" x2="488.8" y2="361.2" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="330.6" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="492.8" y1="324.1" x2="492.8" y2="379.7" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="342.8" width="2.45" height="32.6" fill="var(--down)"/>
<line x1="496.7" y1="316.3" x2="496.7" y2="386.4" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="329.6" width="2.45" height="45.3" fill="var(--up)"/>
<line x1="500.7" y1="282.1" x2="500.7" y2="339.2" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="282.7" width="2.45" height="40.9" fill="var(--up)"/>
<line x1="504.6" y1="279.5" x2="504.6" y2="359.9" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="285.7" width="2.45" height="57.0" fill="var(--down)"/>
<line x1="508.6" y1="337.0" x2="508.6" y2="384.8" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="357.9" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="512.5" y1="361.7" x2="512.5" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="379.5" width="2.45" height="19.8" fill="var(--down)"/>
<line x1="516.5" y1="359.0" x2="516.5" y2="393.4" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="377.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="520.4" y1="383.1" x2="520.4" y2="459.9" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="386.9" width="2.45" height="38.5" fill="var(--down)"/>
<line x1="524.4" y1="421.1" x2="524.4" y2="450.9" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="439.3" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="528.3" y1="400.5" x2="528.3" y2="436.4" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="405.5" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="532.3" y1="383.3" x2="532.3" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="384.4" width="2.45" height="28.0" fill="var(--up)"/>
<line x1="536.2" y1="383.5" x2="536.2" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="386.0" width="2.45" height="17.0" fill="var(--down)"/>
<line x1="540.2" y1="414.5" x2="540.2" y2="500.1" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="422.8" width="2.45" height="70.8" fill="var(--down)"/>
<line x1="544.1" y1="491.9" x2="544.1" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="491.9" width="2.45" height="42.9" fill="var(--down)"/>
<line x1="548.1" y1="511.4" x2="548.1" y2="537.7" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="511.7" width="2.45" height="21.4" fill="var(--up)"/>
<line x1="552.0" y1="509.9" x2="552.0" y2="531.2" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="511.4" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="556.0" y1="493.0" x2="556.0" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="499.3" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="560.0" y1="493.5" x2="560.0" y2="513.9" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="495.7" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="563.9" y1="486.5" x2="563.9" y2="515.7" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="501.8" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="567.9" y1="507.5" x2="567.9" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="508.7" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="571.8" y1="497.8" x2="571.8" y2="528.5" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="498.5" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="575.8" y1="488.2" x2="575.8" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="490.5" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="579.7" y1="482.4" x2="579.7" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="492.2" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="583.7" y1="493.0" x2="583.7" y2="513.7" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="504.2" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="587.6" y1="492.4" x2="587.6" y2="523.0" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="497.1" width="2.45" height="23.9" fill="var(--up)"/>
<line x1="591.6" y1="509.5" x2="591.6" y2="532.8" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="512.5" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="595.5" y1="502.5" x2="595.5" y2="522.7" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="505.3" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="599.5" y1="506.9" x2="599.5" y2="531.4" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="511.3" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="603.4" y1="504.0" x2="603.4" y2="531.4" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="528.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="607.4" y1="514.9" x2="607.4" y2="539.9" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="517.2" width="2.45" height="17.9" fill="var(--up)"/>
<line x1="611.3" y1="499.3" x2="611.3" y2="520.3" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="509.0" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="615.3" y1="495.9" x2="615.3" y2="516.1" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="509.8" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="619.2" y1="480.6" x2="619.2" y2="515.7" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="485.8" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="623.2" y1="465.1" x2="623.2" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="480.6" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="627.1" y1="480.9" x2="627.1" y2="493.6" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="489.1" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="631.1" y1="475.8" x2="631.1" y2="493.7" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="486.6" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="635.0" y1="483.3" x2="635.0" y2="497.2" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="485.8" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="639.0" y1="494.7" x2="639.0" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="501.9" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="642.9" y1="505.1" x2="642.9" y2="536.0" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="507.4" width="2.45" height="24.8" fill="var(--down)"/>
<line x1="646.9" y1="515.3" x2="646.9" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="520.9" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="650.9" y1="514.8" x2="650.9" y2="536.3" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="517.2" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="654.8" y1="505.4" x2="654.8" y2="523.6" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="510.8" width="2.45" height="10.7" fill="var(--down)"/>
<line x1="658.8" y1="514.6" x2="658.8" y2="529.3" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="521.4" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="662.7" y1="524.6" x2="662.7" y2="539.3" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="528.5" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="666.7" y1="535.2" x2="666.7" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="536.4" width="2.45" height="26.0" fill="var(--down)"/>
<line x1="670.6" y1="550.3" x2="670.6" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="554.0" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="674.6" y1="527.7" x2="674.6" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="538.2" width="2.45" height="6.3" fill="var(--up)"/>
<line x1="678.5" y1="529.7" x2="678.5" y2="553.5" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="538.1" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="682.5" y1="531.2" x2="682.5" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="537.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="686.4" y1="542.7" x2="686.4" y2="567.1" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="544.0" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="690.4" y1="521.7" x2="690.4" y2="543.3" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="526.7" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="694.3" y1="527.2" x2="694.3" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="534.5" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="698.3" y1="525.2" x2="698.3" y2="544.2" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="531.5" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="702.2" y1="522.9" x2="702.2" y2="543.3" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="523.6" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="706.2" y1="502.9" x2="706.2" y2="525.9" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="508.4" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="710.1" y1="504.0" x2="710.1" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="514.0" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="714.1" y1="493.8" x2="714.1" y2="514.7" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="499.9" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="718.0" y1="494.1" x2="718.0" y2="518.4" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="502.8" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="722.0" y1="508.8" x2="722.0" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="511.0" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="725.9" y1="507.9" x2="725.9" y2="528.3" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="510.9" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="729.9" y1="481.8" x2="729.9" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="482.1" width="2.45" height="34.8" fill="var(--up)"/>
<line x1="733.8" y1="460.0" x2="733.8" y2="487.8" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="469.4" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="737.8" y1="464.9" x2="737.8" y2="501.7" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="467.1" width="2.45" height="33.9" fill="var(--down)"/>
<line x1="741.8" y1="469.4" x2="741.8" y2="493.0" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="474.0" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="745.7" y1="484.6" x2="745.7" y2="507.3" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="495.5" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="749.7" y1="497.7" x2="749.7" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="498.6" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="753.6" y1="491.9" x2="753.6" y2="519.5" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="492.2" width="2.45" height="25.9" fill="var(--up)"/>
<line x1="757.6" y1="492.5" x2="757.6" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="497.0" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="761.5" y1="492.7" x2="761.5" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="498.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="765.5" y1="493.8" x2="765.5" y2="511.4" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="494.8" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="769.4" y1="458.5" x2="769.4" y2="513.2" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="458.6" width="2.45" height="41.8" fill="var(--up)"/>
<line x1="773.4" y1="452.5" x2="773.4" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="457.5" width="2.45" height="42.5" fill="var(--down)"/>
<line x1="777.3" y1="493.0" x2="777.3" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="493.0" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="781.3" y1="482.8" x2="781.3" y2="516.1" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="488.5" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="785.2" y1="493.2" x2="785.2" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="497.1" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="789.2" y1="500.8" x2="789.2" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="501.5" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="793.1" y1="521.0" x2="793.1" y2="536.4" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="521.9" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="797.1" y1="537.5" x2="797.1" y2="545.9" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="539.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="801.0" y1="534.9" x2="801.0" y2="558.8" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="539.1" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="805.0" y1="554.5" x2="805.0" y2="571.0" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="559.9" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="808.9" y1="553.3" x2="808.9" y2="565.7" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="555.0" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="812.9" y1="545.2" x2="812.9" y2="563.5" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="548.1" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="816.8" y1="528.1" x2="816.8" y2="546.9" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="544.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="820.8" y1="528.4" x2="820.8" y2="542.4" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="535.0" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="824.7" y1="537.1" x2="824.7" y2="551.7" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="541.7" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="828.7" y1="533.6" x2="828.7" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="534.4" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="832.7" y1="529.8" x2="832.7" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="531.8" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="836.6" y1="520.2" x2="836.6" y2="555.0" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="528.5" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="840.6" y1="502.4" x2="840.6" y2="532.9" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="511.8" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="844.5" y1="514.0" x2="844.5" y2="541.1" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="518.6" width="2.45" height="22.0" fill="var(--down)"/>
<line x1="848.5" y1="531.1" x2="848.5" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="532.3" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="852.4" y1="538.6" x2="852.4" y2="579.7" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="538.7" width="2.45" height="34.8" fill="var(--down)"/>
<line x1="856.4" y1="564.6" x2="856.4" y2="573.1" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="564.8" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="860.3" y1="566.8" x2="860.3" y2="598.1" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="570.7" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="864.3" y1="582.6" x2="864.3" y2="601.8" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="586.6" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="868.2" y1="576.2" x2="868.2" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="578.6" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="872.2" y1="567.9" x2="872.2" y2="579.5" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="572.2" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="876.1" y1="543.9" x2="876.1" y2="559.0" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="548.9" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="880.1" y1="545.0" x2="880.1" y2="567.6" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="558.7" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="884.0" y1="547.6" x2="884.0" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="559.4" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="888.0" y1="523.0" x2="888.0" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="524.6" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="891.9" y1="530.3" x2="891.9" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="537.3" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="895.9" y1="523.6" x2="895.9" y2="555.2" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="547.5" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="899.8" y1="546.4" x2="899.8" y2="565.7" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="554.1" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="903.8" y1="549.0" x2="903.8" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="555.8" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="907.7" y1="560.1" x2="907.7" y2="570.6" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="565.5" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="911.7" y1="564.9" x2="911.7" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="567.4" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="915.6" y1="562.6" x2="915.6" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="563.4" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="919.6" y1="553.1" x2="919.6" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="563.4" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="923.6" y1="546.7" x2="923.6" y2="579.1" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="558.3" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="927.5" y1="543.7" x2="927.5" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="552.9" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="931.5" y1="552.7" x2="931.5" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="559.0" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="935.4" y1="559.9" x2="935.4" y2="573.5" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="565.7" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="939.4" y1="551.8" x2="939.4" y2="566.1" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="554.0" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="943.3" y1="547.8" x2="943.3" y2="559.6" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="550.2" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="947.3" y1="559.9" x2="947.3" y2="583.0" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="564.9" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="951.2" y1="567.3" x2="951.2" y2="581.6" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="571.1" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="955.2" y1="574.4" x2="955.2" y2="594.2" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="577.0" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="959.1" y1="588.8" x2="959.1" y2="600.9" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="588.8" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="963.1" y1="579.7" x2="963.1" y2="606.0" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="583.0" width="2.45" height="19.9" fill="var(--up)"/>
<line x1="967.0" y1="578.1" x2="967.0" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="582.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="971.0" y1="557.5" x2="971.0" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="557.9" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="974.9" y1="546.0" x2="974.9" y2="559.9" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="552.8" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="978.9" y1="554.8" x2="978.9" y2="566.2" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="558.6" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="982.8" y1="557.3" x2="982.8" y2="571.1" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="558.9" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="986.8" y1="548.6" x2="986.8" y2="567.6" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="550.0" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="990.7" y1="559.9" x2="990.7" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="560.5" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="994.7" y1="562.4" x2="994.7" y2="579.5" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="568.2" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="998.6" y1="547.4" x2="998.6" y2="572.9" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="548.8" width="2.45" height="20.8" fill="var(--up)"/>
<line x1="1002.6" y1="540.4" x2="1002.6" y2="554.1" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="544.2" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="1006.5" y1="531.1" x2="1006.5" y2="555.0" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="535.5" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="1010.5" y1="522.1" x2="1010.5" y2="535.1" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="526.9" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="1014.5" y1="525.2" x2="1014.5" y2="535.9" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="528.9" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="1018.4" y1="505.1" x2="1018.4" y2="550.0" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="507.0" width="2.45" height="39.6" fill="var(--down)"/>
<line x1="1022.4" y1="524.1" x2="1022.4" y2="548.4" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="524.6" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="1026.3" y1="520.1" x2="1026.3" y2="530.5" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="525.2" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="1030.3" y1="517.0" x2="1030.3" y2="535.4" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="524.2" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="1034.2" y1="517.0" x2="1034.2" y2="536.6" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="517.0" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="1038.2" y1="521.2" x2="1038.2" y2="538.1" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="523.9" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="1042.1" y1="513.8" x2="1042.1" y2="527.8" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="523.6" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="1046.1" y1="526.9" x2="1046.1" y2="539.3" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="528.5" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="1050.0" y1="537.8" x2="1050.0" y2="553.0" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="546.9" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="60" y1="544.8" x2="1052" y2="544.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="548.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$179 R1</text>
<text x="1058" y="560.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="503.8" x2="1052" y2="503.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="507.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$204 R2</text>
<text x="1058" y="519.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="483.8" x2="1052" y2="483.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="487.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$216 R3</text>
<text x="1058" y="499.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="569.4" x2="1052" y2="569.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="563.4" font-size="11.5" fill="var(--support)" font-weight="600">$164 S1</text>
<text x="1058" y="575.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="603.9" x2="1052" y2="603.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="597.9" font-size="11.5" fill="var(--support)" font-weight="600">$143 S2</text>
<text x="1058" y="609.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="550.5" r="3" fill="var(--ink)"/>
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

## 2. 지지/저항 레벨

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $216 | 2 | 2026년 2~3월 반등 국면의 스윙 고점대 |
| R2 | $204 | 2 | 2026년 2월과 6월에 걸쳐 반복 형성된 저항대 |
| R1 | $179 | 2 | 현재가에 가장 가까운 저항대, 2026년 7~8월 반등이 여러 차례 막힌 레벨 |
| **현재가** | **$175.70** (2026-08-18 종가) | — | R1과 S1 사이 |
| S1 | $164 | 2 | 현재가에 가장 근접한 지지, 2026년 6~7월 조정에서 방어된 레벨 |
| S2 | $143 | 2 | 52주 최저($142.13, 2026년 4~5월경)와 거의 일치하는 구간 |
| 참고선 | $464 | — | 52주 최고(정확히는 $464.25, 2025년 10월경) — 이후 대규모 조정으로 현재는 이 레벨과 단절된 국면(3. 관측된 특이 구간 — 2025년 10월 고점 이후 대조정과 2026년 개별 이벤트 참고), 근시일 저항으로 보지 않음 |

> 위 5개 레벨은 모두 52주 최고($464.25, 2025년 10월경)보다 한참 낮은 $143~$216 구간에 몰려 있다 — 큰 폭의 조정 이후 새로 형성된 거래 레짐을 반영한다. R1~S2는 2026년 3~8월 사이 반복적으로 되돌림·반등이 나타난 구간이며, 52주 최고는 이제 근시일 저항으로 작동한다고 보기 어려워 2. 지지/저항 레벨에서 참고선으로만 분리했다.

---

## 3. 관측된 특이 구간 — 2025년 10월 고점 이후 대조정과 2026년 개별 이벤트

- 주가는 2025년 10월경 52주 최고 $464.25를 기록한 뒤(원자력 르네상스·AI 데이터센터 전력수요 테마의 투기적 재평가로 추정 — 밸류에이션 / 적정주가 2. 최근 3개년 — 적정주가 vs 실제주가 참고), 2026년 상반기 내내 되돌림을 겪어 4~5월경 52주 최저 $142.13 부근까지 조정됐다(고점 대비 약 −69%). 이는 특정 하루의 갭이 아니라 수개월에 걸친 점진적 조정이라, 위 2. 지지/저항 레벨 표는 52주 최고를 참고선으로만 표시했다.
- 이후 6~8월 구간은 $143~$216 박스권 안에서 등락하며 저점 대비로는 일부 되돌렸지만 고점 대비로는 여전히 큰 폭 낮은 수준이다.
- 차트에 표시한 3개 이벤트(2026-01-05 DOE $900M HALEU 증설 계약, 2026-05-05 1분기 실적 발표 급락, 2026-08-05 2분기 실적+DOE 옵션 미행사 통보)는 모두 이 대조정 국면 **안에서** 발생했다 — 개별 이벤트가 방향을 뒤집었다기보다, 이미 진행 중이던 밸류에이션 재평가 흐름 위에 얹힌 뉴스로 해석하는 것이 더 정확하다(자세한 내용은 [최근 뉴스 / 이슈](./08_news.md) 참고).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-19~2026-08-18. 수집 시점: 2026-08-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py LEU --name "Centrus Energy" --ref-line 464.25:"52주 최고" --event 2026-01-05:"DOE $900M HALEU 증설 계약 발표" --event 2026-05-05:"1분기 실적 발표(EPS 급감, -8.8%)" --event 2026-08-05:"2분기 실적+DOE 옵션 미행사 통보" --close-on 2026-08-18`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 최근 1년 안에 주식분할은 없었으나 대규모 유상증자(2025년, 핵심 지표 참고)가 있었다 — 이는 가격 연속성 자체를 깨는 이벤트는 아니라(신주 발행이 시장가로 거래된 것이라 갭을 만들지 않음) 소급조정 대상은 아니지만, 이 기간 변동성이 순수 사업 펀더멘털 외에 수급(대규모 신주 물량 소화) 요인도 반영했을 수 있다는 점은 참고할 것.

---

## 관련 문서

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 주봉·5년](./10_technical_weekly.md)
- [최종 보고서](./11_final_report.md)

---

## 참고 자료

- [Yahoo Finance — LEU 일봉 시세](https://finance.yahoo.com/quote/LEU/history/)
- [stockanalysis.com — LEU 현재가·통계](https://stockanalysis.com/stocks/leu/) (핵심 지표·밸류에이션 대조용)

---

*작성일: 2026-08-19 (최종 수정일: 2026-08-23)*
