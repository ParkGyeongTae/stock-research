# Visa Inc. (비자) — 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `04_metrics.md`의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API(Yahoo Finance)에서 직접 수집했다(1년 일봉은 `04_metrics.md`가 다루는 범위 밖이라 단일 출처 규칙의 예외). 겹치는 시점의 종가를 대조한 결과: `2025-09-30` 종가 $341.38은 [`04_metrics.md`](./04_metrics.md) A.2·[`06_valuation.md`](./06_valuation.md) §2에 인용된 FY2025 회계연도 말 종가와 **일치**한다. `2026-08-14` 종가 $364.15도 [`01_overview.md`](./01_overview.md)·[`06_valuation.md`](./06_valuation.md)에 인용된 현재주가와 **일치**한다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="v-chart">
<style>
.v-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .v-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .v-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.v-chart svg { width:100%; height:auto; display:block; }
.v-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.v-chart .title { fill: var(--ink); font-weight:600; }
.v-chart .grid { stroke: var(--grid); stroke-width:1; }
.v-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visa(V) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Visa (V) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $364.15 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="561.2" x2="1052" y2="561.2" class="grid"/>
<text x="52" y="565.2" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="431.7" x2="1052" y2="431.7" class="grid"/>
<text x="52" y="435.7" font-size="11" text-anchor="end" fill="var(--muted)">320</text>
<line x1="60" y1="302.1" x2="1052" y2="302.1" class="grid"/>
<text x="52" y="306.1" font-size="11" text-anchor="end" fill="var(--muted)">340</text>
<line x1="60" y1="172.6" x2="1052" y2="172.6" class="grid"/>
<text x="52" y="176.6" font-size="11" text-anchor="end" fill="var(--muted)">360</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="105.5" y1="626.0" x2="105.5" y2="631.0" class="axis"/>
<text x="105.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="188.4" y1="626.0" x2="188.4" y2="631.0" class="axis"/>
<text x="188.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="279.3" y1="626.0" x2="279.3" y2="631.0" class="axis"/>
<text x="279.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="354.4" y1="626.0" x2="354.4" y2="631.0" class="axis"/>
<text x="354.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="441.4" y1="626.0" x2="441.4" y2="631.0" class="axis"/>
<text x="441.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="520.4" y1="626.0" x2="520.4" y2="631.0" class="axis"/>
<text x="520.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="595.5" y1="626.0" x2="595.5" y2="631.0" class="axis"/>
<text x="595.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="682.5" y1="626.0" x2="682.5" y2="631.0" class="axis"/>
<text x="682.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="765.5" y1="626.0" x2="765.5" y2="631.0" class="axis"/>
<text x="765.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="844.5" y1="626.0" x2="844.5" y2="631.0" class="axis"/>
<text x="844.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="927.5" y1="626.0" x2="927.5" y2="631.0" class="axis"/>
<text x="927.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="1014.5" y1="626.0" x2="1014.5" y2="631.0" class="axis"/>
<text x="1014.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="757.6" y1="56.0" x2="757.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="763.6" y="68.0" font-size="10.5" fill="var(--down)">2026-04-29 FY2026 Q2 실적 서프라이즈(매출 +17%, EPS +36%)</text>
<line x1="62.0" y1="248.0" x2="62.0" y2="283.6" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="261.7" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="65.9" y1="265.0" x2="65.9" y2="296.0" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="277.3" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="69.9" y1="261.1" x2="69.9" y2="289.9" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="285.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="73.8" y1="253.9" x2="73.8" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="276.7" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="77.8" y1="272.9" x2="77.8" y2="303.9" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="278.2" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="81.7" y1="229.6" x2="81.7" y2="268.3" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="237.1" width="2.45" height="31.2" fill="var(--up)"/>
<line x1="85.7" y1="232.7" x2="85.7" y2="253.6" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="239.9" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="89.6" y1="215.3" x2="89.6" y2="253.9" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="229.7" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="93.6" y1="215.1" x2="93.6" y2="238.4" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="232.8" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="97.5" y1="230.6" x2="97.5" y2="246.4" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="233.5" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="101.5" y1="220.3" x2="101.5" y2="243.8" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="225.8" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="105.5" y1="236.3" x2="105.5" y2="262.8" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="236.9" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="109.4" y1="231.6" x2="109.4" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="231.7" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="113.4" y1="220.3" x2="113.4" y2="242.9" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="231.0" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="117.3" y1="220.4" x2="117.3" y2="300.8" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="228.4" width="2.45" height="52.9" fill="var(--down)"/>
<line x1="121.3" y1="273.8" x2="121.3" y2="295.7" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="287.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="125.2" y1="261.2" x2="125.2" y2="293.8" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="276.3" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="129.2" y1="285.2" x2="129.2" y2="325.2" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="285.2" width="2.45" height="29.1" fill="var(--down)"/>
<line x1="133.1" y1="279.3" x2="133.1" y2="315.9" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="279.5" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="137.1" y1="281.5" x2="137.1" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="294.2" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="141.0" y1="284.6" x2="141.0" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="298.2" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="145.0" y1="298.6" x2="145.0" y2="344.4" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="301.9" width="2.45" height="24.5" fill="var(--up)"/>
<line x1="148.9" y1="262.0" x2="148.9" y2="305.2" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="262.0" width="2.45" height="40.5" fill="var(--up)"/>
<line x1="152.9" y1="268.0" x2="152.9" y2="313.9" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="271.5" width="2.45" height="42.4" fill="var(--down)"/>
<line x1="156.8" y1="284.7" x2="156.8" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="291.7" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="160.8" y1="270.7" x2="160.8" y2="310.8" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="273.9" width="2.45" height="34.7" fill="var(--up)"/>
<line x1="164.7" y1="268.1" x2="164.7" y2="317.5" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="272.4" width="2.45" height="38.2" fill="var(--down)"/>
<line x1="168.7" y1="302.8" x2="168.7" y2="315.6" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="307.8" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="172.6" y1="300.8" x2="172.6" y2="337.7" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="312.8" width="2.45" height="22.2" fill="var(--down)"/>
<line x1="176.6" y1="305.4" x2="176.6" y2="326.6" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="319.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="180.5" y1="298.0" x2="180.5" y2="331.0" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="301.1" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="184.5" y1="265.8" x2="184.5" y2="311.8" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="293.2" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="188.4" y1="241.5" x2="188.4" y2="300.1" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="251.4" width="2.45" height="48.7" fill="var(--up)"/>
<line x1="192.4" y1="255.6" x2="192.4" y2="279.1" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="261.8" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="196.4" y1="216.9" x2="196.4" y2="263.3" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="238.4" width="2.45" height="24.2" fill="var(--up)"/>
<line x1="200.3" y1="230.1" x2="200.3" y2="274.0" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="237.3" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="204.3" y1="208.6" x2="204.3" y2="237.0" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="221.7" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="208.2" y1="205.0" x2="208.2" y2="230.2" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="212.9" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="212.2" y1="218.8" x2="212.2" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="227.8" width="2.45" height="28.7" fill="var(--down)"/>
<line x1="216.1" y1="234.8" x2="216.1" y2="281.1" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="252.7" width="2.45" height="25.8" fill="var(--down)"/>
<line x1="220.1" y1="252.5" x2="220.1" y2="297.4" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="278.0" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="224.0" y1="237.3" x2="224.0" y2="300.7" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="247.9" width="2.45" height="47.8" fill="var(--up)"/>
<line x1="228.0" y1="236.8" x2="228.0" y2="276.2" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="247.9" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="231.9" y1="265.3" x2="231.9" y2="339.9" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="269.8" width="2.45" height="62.2" fill="var(--down)"/>
<line x1="235.9" y1="279.8" x2="235.9" y2="321.6" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="289.9" width="2.45" height="26.7" fill="var(--up)"/>
<line x1="239.8" y1="270.0" x2="239.8" y2="309.0" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="273.6" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="243.8" y1="239.6" x2="243.8" y2="282.7" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="255.4" width="2.45" height="26.5" fill="var(--up)"/>
<line x1="247.7" y1="249.2" x2="247.7" y2="273.0" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="251.5" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="251.7" y1="255.8" x2="251.7" y2="273.2" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="262.0" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="255.6" y1="243.3" x2="255.6" y2="267.7" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="249.0" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="259.6" y1="240.5" x2="259.6" y2="269.7" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="243.8" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="263.5" y1="238.1" x2="263.5" y2="260.0" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="246.6" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="267.5" y1="231.0" x2="267.5" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="263.3" width="2.45" height="30.6" fill="var(--down)"/>
<line x1="271.4" y1="239.2" x2="271.4" y2="290.5" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="269.6" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="275.4" y1="282.7" x2="275.4" y2="314.0" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="288.7" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="279.3" y1="294.3" x2="279.3" y2="335.7" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="295.7" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="283.3" y1="300.1" x2="283.3" y2="339.4" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="300.2" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="287.3" y1="288.5" x2="287.3" y2="325.7" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="301.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="291.2" y1="310.9" x2="291.2" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="311.3" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="295.2" y1="313.2" x2="295.2" y2="335.5" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="323.3" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="299.1" y1="310.7" x2="299.1" y2="338.9" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="323.8" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="303.1" y1="308.0" x2="303.1" y2="346.2" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="309.1" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="307.0" y1="274.5" x2="307.0" y2="319.0" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="309.4" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="311.0" y1="292.7" x2="311.0" y2="330.6" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="308.4" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="314.9" y1="327.5" x2="314.9" y2="373.2" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="328.8" width="2.45" height="38.0" fill="var(--down)"/>
<line x1="318.9" y1="345.1" x2="318.9" y2="399.7" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="359.4" width="2.45" height="35.0" fill="var(--down)"/>
<line x1="322.8" y1="399.3" x2="322.8" y2="444.6" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="402.5" width="2.45" height="21.5" fill="var(--down)"/>
<line x1="326.8" y1="402.1" x2="326.8" y2="432.5" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="405.0" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="330.7" y1="377.3" x2="330.7" y2="411.3" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="405.0" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="334.7" y1="359.9" x2="334.7" y2="403.9" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="380.0" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="338.6" y1="362.2" x2="338.6" y2="392.8" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="371.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="342.6" y1="327.7" x2="342.6" y2="374.0" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="337.6" width="2.45" height="36.5" fill="var(--up)"/>
<line x1="346.5" y1="329.9" x2="346.5" y2="347.1" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="337.6" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="350.5" y1="334.4" x2="350.5" y2="354.0" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="338.1" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="354.4" y1="345.5" x2="354.4" y2="366.0" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="347.9" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="358.4" y1="348.8" x2="358.4" y2="385.0" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="357.5" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="362.3" y1="351.7" x2="362.3" y2="371.1" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="369.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="366.3" y1="351.5" x2="366.3" y2="404.0" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="358.6" width="2.45" height="27.1" fill="var(--down)"/>
<line x1="370.2" y1="340.3" x2="370.2" y2="390.2" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="358.9" width="2.45" height="28.6" fill="var(--up)"/>
<line x1="374.2" y1="358.2" x2="374.2" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="367.7" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="378.2" y1="378.4" x2="378.2" y2="398.8" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="388.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="382.1" y1="374.9" x2="382.1" y2="397.4" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="388.7" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="386.1" y1="254.7" x2="386.1" y2="366.5" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="265.7" width="2.45" height="84.4" fill="var(--up)"/>
<line x1="390.0" y1="238.4" x2="390.0" y2="263.5" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="250.3" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="394.0" y1="247.4" x2="394.0" y2="277.3" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="251.4" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="397.9" y1="252.8" x2="397.9" y2="278.0" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="263.3" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="401.9" y1="251.7" x2="401.9" y2="278.3" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="266.2" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="405.8" y1="253.4" x2="405.8" y2="274.5" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="263.2" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="409.8" y1="237.9" x2="409.8" y2="262.9" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="242.2" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="413.7" y1="215.1" x2="413.7" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="223.8" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="417.7" y1="196.0" x2="417.7" y2="224.4" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="215.5" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="421.6" y1="198.6" x2="421.6" y2="217.9" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="204.1" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="425.6" y1="193.8" x2="425.6" y2="213.3" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="204.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="429.5" y1="194.9" x2="429.5" y2="212.8" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="201.8" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="433.5" y1="205.8" x2="433.5" y2="220.1" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="211.5" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="437.4" y1="203.7" x2="437.4" y2="232.9" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="213.7" width="2.45" height="19.0" fill="var(--down)"/>
<line x1="441.4" y1="237.0" x2="441.4" y2="279.6" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="238.2" width="2.45" height="22.0" fill="var(--down)"/>
<line x1="445.3" y1="188.5" x2="445.3" y2="275.9" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="212.8" width="2.45" height="60.2" fill="var(--up)"/>
<line x1="449.3" y1="181.5" x2="449.3" y2="224.4" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="188.4" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="453.2" y1="183.7" x2="453.2" y2="208.2" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="191.1" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="457.2" y1="196.2" x2="457.2" y2="240.6" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="205.0" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="461.1" y1="206.9" x2="461.1" y2="242.8" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="223.4" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="465.1" y1="260.0" x2="465.1" y2="319.5" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="281.4" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="469.1" y1="318.2" x2="469.1" y2="406.9" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="321.6" width="2.45" height="59.1" fill="var(--down)"/>
<line x1="473.0" y1="367.6" x2="473.0" y2="406.2" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="372.3" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="477.0" y1="356.0" x2="477.0" y2="390.4" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="371.2" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="480.9" y1="371.8" x2="480.9" y2="396.7" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="377.9" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="484.9" y1="377.8" x2="484.9" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="394.0" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="488.8" y1="375.5" x2="488.8" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="390.0" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="492.8" y1="377.3" x2="492.8" y2="405.8" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="389.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="496.7" y1="381.2" x2="496.7" y2="401.8" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="391.7" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="500.7" y1="354.0" x2="500.7" y2="399.1" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="376.7" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="504.6" y1="373.8" x2="504.6" y2="399.9" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="376.8" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="508.6" y1="377.3" x2="508.6" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="386.5" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="512.5" y1="345.1" x2="512.5" y2="408.9" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="355.3" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="516.5" y1="347.5" x2="516.5" y2="421.3" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="352.5" width="2.45" height="67.3" fill="var(--down)"/>
<line x1="520.4" y1="336.5" x2="520.4" y2="405.1" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="342.0" width="2.45" height="58.4" fill="var(--up)"/>
<line x1="524.4" y1="329.4" x2="524.4" y2="374.2" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="356.2" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="528.3" y1="358.4" x2="528.3" y2="403.1" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="367.2" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="532.3" y1="317.7" x2="532.3" y2="374.6" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="347.5" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="536.2" y1="333.7" x2="536.2" y2="385.7" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="355.4" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="540.2" y1="348.6" x2="540.2" y2="408.2" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="362.0" width="2.45" height="33.6" fill="var(--down)"/>
<line x1="544.1" y1="367.7" x2="544.1" y2="402.2" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="378.8" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="548.1" y1="360.2" x2="548.1" y2="390.1" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="371.8" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="552.0" y1="352.4" x2="552.0" y2="405.8" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="374.1" width="2.45" height="30.5" fill="var(--down)"/>
<line x1="556.0" y1="389.7" x2="556.0" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="406.9" width="2.45" height="63.2" fill="var(--down)"/>
<line x1="560.0" y1="422.7" x2="560.0" y2="467.9" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="434.9" width="2.45" height="33.0" fill="var(--up)"/>
<line x1="563.9" y1="416.9" x2="563.9" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="429.7" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="567.9" y1="430.4" x2="567.9" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="438.6" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="571.8" y1="416.5" x2="571.8" y2="445.8" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="425.5" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="575.8" y1="428.3" x2="575.8" y2="530.7" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="437.9" width="2.45" height="81.1" fill="var(--down)"/>
<line x1="579.7" y1="501.2" x2="579.7" y2="541.3" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="514.5" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="583.7" y1="470.9" x2="583.7" y2="507.8" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="477.1" width="2.45" height="28.8" fill="var(--up)"/>
<line x1="587.6" y1="435.4" x2="587.6" y2="470.9" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="453.1" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="591.6" y1="430.2" x2="591.6" y2="483.8" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="430.8" width="2.45" height="36.8" fill="var(--up)"/>
<line x1="595.5" y1="414.8" x2="595.5" y2="466.7" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="428.4" width="2.45" height="32.5" fill="var(--up)"/>
<line x1="599.5" y1="418.5" x2="599.5" y2="468.3" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="426.3" width="2.45" height="32.5" fill="var(--up)"/>
<line x1="603.4" y1="394.3" x2="603.4" y2="433.0" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="422.4" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="607.4" y1="413.5" x2="607.4" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="433.0" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="611.3" y1="446.6" x2="611.3" y2="481.6" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="448.8" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="615.3" y1="455.0" x2="615.3" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="457.8" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="619.2" y1="450.3" x2="619.2" y2="487.1" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="461.3" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="623.2" y1="463.6" x2="623.2" y2="506.9" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="475.4" width="2.45" height="27.8" fill="var(--down)"/>
<line x1="627.1" y1="490.3" x2="627.1" y2="522.2" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="508.5" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="631.1" y1="494.2" x2="631.1" y2="519.6" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="512.1" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="635.0" y1="489.1" x2="635.0" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="495.7" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="639.0" y1="479.0" x2="639.0" y2="513.4" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="487.9" width="2.45" height="18.5" fill="var(--down)"/>
<line x1="642.9" y1="509.8" x2="642.9" y2="570.9" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="513.2" width="2.45" height="54.3" fill="var(--down)"/>
<line x1="646.9" y1="545.2" x2="646.9" y2="580.5" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="563.1" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="650.9" y1="542.3" x2="650.9" y2="567.6" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="550.7" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="654.8" y1="510.4" x2="654.8" y2="542.8" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="527.5" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="658.8" y1="522.1" x2="658.8" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="536.9" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="662.7" y1="506.2" x2="662.7" y2="547.2" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="525.7" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="666.7" y1="510.3" x2="666.7" y2="541.8" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="525.4" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="670.6" y1="531.5" x2="670.6" y2="598.0" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="533.2" width="2.45" height="57.0" fill="var(--down)"/>
<line x1="674.6" y1="556.8" x2="674.6" y2="587.8" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="564.2" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="678.5" y1="539.6" x2="678.5" y2="583.3" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="546.7" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="682.5" y1="528.5" x2="682.5" y2="600.8" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="528.5" width="2.45" height="42.4" fill="var(--down)"/>
<line x1="686.4" y1="545.2" x2="686.4" y2="588.1" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="556.0" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="690.4" y1="532.6" x2="690.4" y2="564.7" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="539.7" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="694.3" y1="529.0" x2="694.3" y2="554.0" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="544.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="698.3" y1="489.5" x2="698.3" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="503.2" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="702.2" y1="499.2" x2="702.2" y2="538.0" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="507.5" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="706.2" y1="502.9" x2="706.2" y2="538.5" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="504.8" width="2.45" height="28.2" fill="var(--down)"/>
<line x1="710.1" y1="498.1" x2="710.1" y2="546.1" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="500.4" width="2.45" height="35.4" fill="var(--up)"/>
<line x1="714.1" y1="482.7" x2="714.1" y2="512.7" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="487.6" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="718.0" y1="452.9" x2="718.0" y2="486.6" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="458.2" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="722.0" y1="444.6" x2="722.0" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="455.3" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="725.9" y1="435.3" x2="725.9" y2="462.9" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="451.0" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="729.9" y1="447.6" x2="729.9" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="455.0" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="733.8" y1="451.8" x2="733.8" y2="504.1" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="470.5" width="2.45" height="26.4" fill="var(--down)"/>
<line x1="737.8" y1="487.6" x2="737.8" y2="509.0" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="488.1" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="741.8" y1="482.2" x2="741.8" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="493.2" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="745.7" y1="496.6" x2="745.7" y2="532.1" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="500.2" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="749.7" y1="491.1" x2="749.7" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="498.7" width="2.45" height="13.9" fill="var(--up)"/>
<line x1="753.6" y1="470.8" x2="753.6" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="482.2" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="757.6" y1="289.3" x2="757.6" y2="342.4" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="325.5" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="761.5" y1="350.7" x2="761.5" y2="379.3" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="353.2" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="765.5" y1="329.0" x2="765.5" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="348.3" width="2.45" height="31.4" fill="var(--down)"/>
<line x1="769.4" y1="368.3" x2="769.4" y2="396.7" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="379.9" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="773.4" y1="395.5" x2="773.4" y2="433.9" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="398.6" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="777.3" y1="402.0" x2="777.3" y2="444.6" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="407.4" width="2.45" height="32.1" fill="var(--down)"/>
<line x1="781.3" y1="407.8" x2="781.3" y2="434.7" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="423.4" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="785.2" y1="424.8" x2="785.2" y2="456.6" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="425.3" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="789.2" y1="398.1" x2="789.2" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="406.7" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="793.1" y1="374.0" x2="793.1" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="390.1" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="797.1" y1="396.6" x2="797.1" y2="433.0" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="407.1" width="2.45" height="22.5" fill="var(--down)"/>
<line x1="801.0" y1="410.1" x2="801.0" y2="430.1" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="415.4" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="805.0" y1="373.3" x2="805.0" y2="406.8" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="394.4" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="808.9" y1="344.7" x2="808.9" y2="407.3" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="349.8" width="2.45" height="53.2" fill="var(--up)"/>
<line x1="812.9" y1="333.4" x2="812.9" y2="370.2" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="345.3" width="2.45" height="22.2" fill="var(--down)"/>
<line x1="816.8" y1="356.2" x2="816.8" y2="387.5" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="362.1" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="820.8" y1="350.6" x2="820.8" y2="384.8" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="359.7" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="824.7" y1="344.7" x2="824.7" y2="374.6" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="363.5" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="828.7" y1="376.6" x2="828.7" y2="402.5" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="389.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="832.7" y1="357.5" x2="832.7" y2="395.0" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="382.4" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="836.6" y1="385.8" x2="836.6" y2="425.9" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="392.8" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="840.6" y1="356.1" x2="840.6" y2="397.0" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="390.5" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="844.5" y1="380.8" x2="844.5" y2="440.2" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="384.7" width="2.45" height="29.1" fill="var(--down)"/>
<line x1="848.5" y1="409.0" x2="848.5" y2="474.5" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="415.4" width="2.45" height="33.6" fill="var(--down)"/>
<line x1="852.4" y1="446.9" x2="852.4" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="446.9" width="2.45" height="34.0" fill="var(--down)"/>
<line x1="856.4" y1="400.8" x2="856.4" y2="453.1" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="430.5" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="860.3" y1="392.9" x2="860.3" y2="425.4" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="408.6" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="864.3" y1="406.3" x2="864.3" y2="441.9" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="422.9" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="868.2" y1="396.1" x2="868.2" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="399.0" width="2.45" height="41.4" fill="var(--up)"/>
<line x1="872.2" y1="387.0" x2="872.2" y2="430.5" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="388.8" width="2.45" height="23.7" fill="var(--down)"/>
<line x1="876.1" y1="407.7" x2="876.1" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="418.7" width="2.45" height="19.1" fill="var(--down)"/>
<line x1="880.1" y1="393.3" x2="880.1" y2="433.0" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="416.2" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="884.0" y1="390.0" x2="884.0" y2="413.9" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="406.9" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="888.0" y1="345.6" x2="888.0" y2="403.3" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="346.7" width="2.45" height="48.1" fill="var(--up)"/>
<line x1="891.9" y1="322.7" x2="891.9" y2="367.1" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="344.2" width="2.45" height="20.2" fill="var(--down)"/>
<line x1="895.9" y1="351.8" x2="895.9" y2="386.3" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="360.4" width="2.45" height="24.4" fill="var(--down)"/>
<line x1="899.8" y1="347.5" x2="899.8" y2="393.7" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="377.7" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="903.8" y1="358.6" x2="903.8" y2="379.3" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="374.6" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="907.7" y1="335.8" x2="907.7" y2="384.9" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="352.5" width="2.45" height="20.9" fill="var(--up)"/>
<line x1="911.7" y1="302.5" x2="911.7" y2="366.5" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="350.3" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="915.6" y1="303.9" x2="915.6" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="326.6" width="2.45" height="25.8" fill="var(--up)"/>
<line x1="919.6" y1="264.5" x2="919.6" y2="313.3" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="291.4" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="923.6" y1="274.3" x2="923.6" y2="308.1" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="282.1" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="927.5" y1="215.6" x2="927.5" y2="295.8" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="230.4" width="2.45" height="42.2" fill="var(--up)"/>
<line x1="931.5" y1="158.8" x2="931.5" y2="221.1" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="158.8" width="2.45" height="62.3" fill="var(--up)"/>
<line x1="935.4" y1="140.1" x2="935.4" y2="244.8" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="153.2" width="2.45" height="37.2" fill="var(--down)"/>
<line x1="939.4" y1="198.0" x2="939.4" y2="257.3" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="223.1" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="943.3" y1="227.0" x2="943.3" y2="265.3" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="235.4" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="947.3" y1="247.1" x2="947.3" y2="273.5" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="249.0" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="951.2" y1="229.8" x2="951.2" y2="267.6" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="233.3" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="955.2" y1="175.9" x2="955.2" y2="230.6" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="187.2" width="2.45" height="39.0" fill="var(--up)"/>
<line x1="959.1" y1="173.0" x2="959.1" y2="213.5" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="198.4" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="963.1" y1="169.8" x2="963.1" y2="243.1" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="204.1" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="967.0" y1="139.3" x2="967.0" y2="191.3" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="139.3" width="2.45" height="46.0" fill="var(--up)"/>
<line x1="971.0" y1="142.6" x2="971.0" y2="192.0" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="149.5" width="2.45" height="32.5" fill="var(--down)"/>
<line x1="974.9" y1="153.2" x2="974.9" y2="195.7" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="168.9" width="2.45" height="22.5" fill="var(--up)"/>
<line x1="978.9" y1="178.3" x2="978.9" y2="207.0" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="192.1" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="982.8" y1="188.6" x2="982.8" y2="222.7" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="194.8" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="986.8" y1="224.1" x2="986.8" y2="247.1" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="224.1" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="990.7" y1="199.5" x2="990.7" y2="230.6" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="200.2" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="994.7" y1="148.9" x2="994.7" y2="183.9" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="156.2" width="2.45" height="20.6" fill="var(--up)"/>
<line x1="998.6" y1="100.3" x2="998.6" y2="154.9" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="129.9" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="1002.6" y1="82.1" x2="1002.6" y2="201.9" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="116.0" width="2.45" height="76.0" fill="var(--up)"/>
<line x1="1006.5" y1="127.2" x2="1006.5" y2="167.7" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="132.0" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="1010.5" y1="128.0" x2="1010.5" y2="171.9" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="132.9" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="1014.5" y1="95.1" x2="1014.5" y2="144.4" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="117.5" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="1018.4" y1="100.6" x2="1018.4" y2="172.0" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="110.5" width="2.45" height="50.7" fill="var(--up)"/>
<line x1="1022.4" y1="92.3" x2="1022.4" y2="129.1" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="92.9" width="2.45" height="24.4" fill="var(--down)"/>
<line x1="1026.3" y1="100.7" x2="1026.3" y2="138.6" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="104.8" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="1030.3" y1="106.2" x2="1030.3" y2="162.7" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="117.5" width="2.45" height="38.9" fill="var(--down)"/>
<line x1="1034.2" y1="145.6" x2="1034.2" y2="179.9" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="159.6" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="1038.2" y1="143.1" x2="1038.2" y2="172.8" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="154.3" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="1042.1" y1="150.9" x2="1042.1" y2="183.5" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="166.1" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="1046.1" y1="137.3" x2="1046.1" y2="180.9" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="137.3" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="1050.0" y1="128.5" x2="1050.0" y2="154.7" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="134.4" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="60" y1="120.5" x2="1052" y2="120.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="124.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$368 R1</text>
<text x="1058" y="136.0" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="263.3" x2="1052" y2="263.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="257.3" font-size="11.5" fill="var(--support)" font-weight="600">$346 S1</text>
<text x="1058" y="269.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="340.7" x2="1052" y2="340.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="334.7" font-size="11.5" fill="var(--support)" font-weight="600">$334 S2</text>
<text x="1058" y="346.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="429.6" x2="1052" y2="429.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="423.6" font-size="11.5" fill="var(--support)" font-weight="600">$320 S3</text>
<text x="1058" y="435.6" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="590.6" x2="1052" y2="590.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="584.6" font-size="11.5" fill="var(--support)" font-weight="600">$295 S4 (52주 최저)</text>
<text x="1058" y="596.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="145.7" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $368 | 3 | 2026년 7~8월 실적 서프라이즈 이후 랠리 구간의 고점대 |
| **현재가** | **$364.15** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $346 | 2 | 2025년 10월, 2026년 7월 초 구간에서 반복된 저항/지지 전환대 |
| S2 | $334 | 3 | 2025년 11월, 2026년 1월, 2026년 6월 구간 스윙 저점대 |
| S3 | $320 | 5 | 2025년 11월~2026년 4월 조정 국면 전반에 걸쳐 반복 형성된 핵심 지지(터치 최다) |
| S4 (52주 최저) | $295 | 2 | 2026년 3~4월 저점 — 터치 횟수는 기준(2회) 충족하지만 52주 최저가로서 별도 강제 포함 |

> 현재가 위쪽에는 유효한 클러스터가 R1 하나뿐이다 — 2026년 7월 말 실적 서프라이즈 이후 주가가 52주 최고가($373.97) 부근까지 단기간에 올라서서 그 위로 반복 터치된 스윙 고점이 아직 충분히 쌓이지 않았기 때문이다. 억지로 R2·R3를 채우지 않았다. 아래쪽은 5개(S1~S4, 강제 포함 1개 포함)로 스크립트 기본값(3개)보다 많다 — 2025년 11월~2026년 4월의 장기 조정 국면에서 스윙 저점이 여러 층으로 형성됐기 때문에 `--levels`를 늘려 모두 반영했다.

---

## 3. 관측된 특이 구간 — 2026-04-29 FY2026 Q2 실적 서프라이즈

- 2026-04-28(화) 장 마감 후 Visa가 FY2026 2분기 실적을 발표(순매출 +17% YoY, GAAP EPS +36% YoY, Non-GAAP EPS +20% YoY) — 관련 원자료는 [`04_metrics.md`](./04_metrics.md) B절, 발표 사실 로그는 [`08_news.md`](./08_news.md) 참고.
- 종가 기준 전일(2026-04-28, $309.30) 대비 **+8.26%** ($309.30 → $334.86, 2026-04-29), 거래량은 직전 20거래일 평균(약 700만 주) 대비 약 2.4배인 **1,666만 주**.
- 이 갭 이후 주가는 2026년 5~6월 한동안 $310~$345 박스권에서 등락했으나, 2026년 7월 FY2026 3분기 실적(2026-07-28 발표, 매출 +14%)을 계기로 재차 상승해 8월 초 52주 최고가($373.97)를 경신했다 — 4월 갭 이후 형성된 새 지지대(S2 $334)가 그 사이 실제로 여러 차례 지지선 역할을 한 것으로 보인다(§2 터치 횟수 3회).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-15. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py V --name Visa --event 2026-04-29:"FY2026 Q2 실적 서프라이즈(매출 +17%, EPS +36%)" --force-level '293.89:(52주 최저)' --close-on 2025-09-30 --close-on 2026-08-14 --emit all`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다(기본값에서 변경한 것은 강제 레벨 1개 추가뿐).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 2026-04-29 실적발표 갭은 정보 이벤트(펀더멘털 서프라이즈)로 인한 불연속 구간이라, 그 직전 형성된 스윙 레벨(2026년 3~4월 저점대)은 이후 레짐에서 의미가 달라졌을 수 있다.
    - 조사 기간(2025-08~2026-08) 내 주식분할·유상증자는 없었다 — 소급조정 이슈 없음. 다만 이 기간 배당이 4회 지급됐고 차트는 배당 미반영(원주가) 기준이라, 배당락일 부근의 미세한 하락은 실제 가치 변동이 아닌 배당락 효과일 수 있다.

---

## 관련 문서

같은 폴더 내 다른 문서로 이동:

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 주봉·5년](./10_technical_weekly.md)

---

## 참고 자료

- [Yahoo Finance — Visa Inc. (V) 일봉 시세](https://finance.yahoo.com/quote/V/history/) (수집 2026-08-15)
- [stockanalysis.com — Visa 주가 이력 API 교차 확인](https://stockanalysis.com/stocks/v/history/)

---

*작성일: 2026-08-15 (최종 수정일: 2026-08-16)*
