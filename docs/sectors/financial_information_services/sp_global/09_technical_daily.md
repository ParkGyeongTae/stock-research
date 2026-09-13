# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-11 종가 **$410.71**은 [핵심 지표](./04_metrics.md) A.2 밸류에이션 지표·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치**한다.
- **주의**: 이 시계열은 2026-07-01 Mobility 분사가 1057:1000 비율의 분할처럼 처리돼 **그 이전 가격이 약 5.4% 소급 하향조정**돼 있다. 아래 4. 방법론 · 한계 참고.
:::

---

## 1. 차트 — 최근 1년 일봉 (2025-09-12 ~ 2026-09-11)

<div class="spgi-chart">
<style>
.spgi-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .spgi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .spgi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.spgi-chart svg { width:100%; height:auto; display:block; }
.spgi-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.spgi-chart .title { fill: var(--ink); font-weight:600; }
.spgi-chart .grid { stroke: var(--grid); stroke-width:1; }
.spgi-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="S&P Global(SPGI) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">S&P Global (SPGI) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-12 ~ 2026-09-11 · 마지막 종가 $410.71 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="559.9" x2="1052" y2="559.9" class="grid"/>
<text x="52" y="563.9" font-size="11" text-anchor="end" fill="var(--muted)">375</text>
<line x1="60" y1="477.3" x2="1052" y2="477.3" class="grid"/>
<text x="52" y="481.3" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="394.7" x2="1052" y2="394.7" class="grid"/>
<text x="52" y="398.7" font-size="11" text-anchor="end" fill="var(--muted)">425</text>
<line x1="60" y1="312.1" x2="1052" y2="312.1" class="grid"/>
<text x="52" y="316.1" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="229.5" x2="1052" y2="229.5" class="grid"/>
<text x="52" y="233.5" font-size="11" text-anchor="end" fill="var(--muted)">475</text>
<line x1="60" y1="146.9" x2="1052" y2="146.9" class="grid"/>
<text x="52" y="150.9" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="64.3" x2="1052" y2="64.3" class="grid"/>
<text x="52" y="68.3" font-size="11" text-anchor="end" fill="var(--muted)">525</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="113.4" y1="626.0" x2="113.4" y2="631.0" class="axis"/>
<text x="113.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="204.3" y1="626.0" x2="204.3" y2="631.0" class="axis"/>
<text x="204.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="279.3" y1="626.0" x2="279.3" y2="631.0" class="axis"/>
<text x="279.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="366.3" y1="626.0" x2="366.3" y2="631.0" class="axis"/>
<text x="366.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="445.3" y1="626.0" x2="445.3" y2="631.0" class="axis"/>
<text x="445.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="520.4" y1="626.0" x2="520.4" y2="631.0" class="axis"/>
<text x="520.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="607.4" y1="626.0" x2="607.4" y2="631.0" class="axis"/>
<text x="607.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="690.4" y1="626.0" x2="690.4" y2="631.0" class="axis"/>
<text x="690.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="769.4" y1="626.0" x2="769.4" y2="631.0" class="axis"/>
<text x="769.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="852.4" y1="626.0" x2="852.4" y2="631.0" class="axis"/>
<text x="852.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="939.4" y1="626.0" x2="939.4" y2="631.0" class="axis"/>
<text x="939.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1022.4" y1="626.0" x2="1022.4" y2="631.0" class="axis"/>
<text x="1022.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="469.1" y1="56.0" x2="469.1" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="475.1" y="68.0" font-size="10.5" fill="var(--down)">2026-02-10 FY2026 가이던스 실망 급락</text>
<line x1="923.6" y1="56.0" x2="923.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="929.6" y="68.0" font-size="10.5" fill="var(--down)">2026-07-28 2분기 EPS 미스</text>
<line x1="62.0" y1="78.6" x2="62.0" y2="101.5" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="86.2" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="65.9" y1="86.3" x2="65.9" y2="100.8" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="93.2" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="69.9" y1="103.2" x2="69.9" y2="120.5" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="106.9" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="73.8" y1="87.6" x2="73.8" y2="109.3" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="97.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="77.8" y1="99.7" x2="77.8" y2="226.3" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="102.3" width="2.45" height="109.3" fill="var(--down)"/>
<line x1="81.7" y1="204.7" x2="81.7" y2="227.9" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="211.6" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="85.7" y1="191.8" x2="85.7" y2="218.9" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="209.9" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="89.6" y1="214.1" x2="89.6" y2="257.7" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="218.5" width="2.45" height="27.6" fill="var(--down)"/>
<line x1="93.6" y1="256.5" x2="93.6" y2="281.5" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="259.2" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="97.5" y1="265.0" x2="97.5" y2="291.1" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="269.3" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="101.5" y1="264.2" x2="101.5" y2="281.7" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="273.5" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="105.5" y1="254.8" x2="105.5" y2="272.3" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="261.1" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="109.4" y1="261.5" x2="109.4" y2="285.3" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="261.5" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="113.4" y1="265.2" x2="113.4" y2="297.7" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="270.7" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="117.3" y1="284.9" x2="117.3" y2="314.8" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="298.4" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="121.3" y1="291.3" x2="121.3" y2="314.8" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="299.1" width="2.45" height="13.4" fill="var(--up)"/>
<line x1="125.2" y1="297.0" x2="125.2" y2="316.4" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="297.7" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="129.2" y1="282.5" x2="129.2" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="283.9" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="133.1" y1="278.5" x2="133.1" y2="305.0" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="287.2" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="137.1" y1="261.0" x2="137.1" y2="283.2" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="274.7" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="141.0" y1="253.4" x2="141.0" y2="282.0" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="260.1" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="145.0" y1="266.3" x2="145.0" y2="324.2" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="280.0" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="148.9" y1="272.6" x2="148.9" y2="307.9" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="277.6" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="152.9" y1="263.1" x2="152.9" y2="293.7" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="276.9" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="156.8" y1="283.7" x2="156.8" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="288.0" width="2.45" height="35.4" fill="var(--down)"/>
<line x1="160.8" y1="309.6" x2="160.8" y2="328.9" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="318.7" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="164.7" y1="304.4" x2="164.7" y2="320.9" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="306.0" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="168.7" y1="280.7" x2="168.7" y2="306.2" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="286.6" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="172.6" y1="280.2" x2="172.6" y2="303.8" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="292.0" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="176.6" y1="288.3" x2="176.6" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="290.0" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="180.5" y1="260.3" x2="180.5" y2="284.2" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="268.9" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="184.5" y1="243.5" x2="184.5" y2="262.8" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="246.5" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="188.4" y1="241.5" x2="188.4" y2="259.0" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="250.5" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="192.4" y1="267.2" x2="192.4" y2="326.7" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="269.2" width="2.45" height="51.0" fill="var(--down)"/>
<line x1="196.4" y1="235.2" x2="196.4" y2="278.8" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="262.3" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="200.3" y1="242.2" x2="200.3" y2="281.1" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="254.8" width="2.45" height="21.1" fill="var(--down)"/>
<line x1="204.3" y1="244.4" x2="204.3" y2="286.7" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="245.3" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="208.2" y1="234.9" x2="208.2" y2="251.6" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="238.4" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="212.2" y1="234.8" x2="212.2" y2="251.8" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="245.0" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="216.1" y1="244.6" x2="216.1" y2="271.0" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="251.6" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="220.1" y1="247.2" x2="220.1" y2="279.7" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="247.2" width="2.45" height="24.9" fill="var(--up)"/>
<line x1="224.0" y1="251.8" x2="224.0" y2="274.8" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="255.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="228.0" y1="240.2" x2="228.0" y2="256.1" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="243.1" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="231.9" y1="230.3" x2="231.9" y2="250.1" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="243.0" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="235.9" y1="216.4" x2="235.9" y2="262.1" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="226.7" width="2.45" height="35.4" fill="var(--up)"/>
<line x1="239.8" y1="223.8" x2="239.8" y2="255.9" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="229.6" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="243.8" y1="256.3" x2="243.8" y2="274.7" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="259.4" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="247.7" y1="259.7" x2="247.7" y2="278.9" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="266.4" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="251.7" y1="257.8" x2="251.7" y2="273.7" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="264.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="255.6" y1="241.2" x2="255.6" y2="270.5" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="255.3" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="259.6" y1="245.3" x2="259.6" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="254.5" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="263.5" y1="254.0" x2="263.5" y2="270.9" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="254.7" width="2.45" height="14.9" fill="var(--down)"/>
<line x1="267.5" y1="246.8" x2="267.5" y2="269.6" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="254.1" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="271.4" y1="240.8" x2="271.4" y2="267.2" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="249.7" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="275.4" y1="235.4" x2="275.4" y2="249.5" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="239.6" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="279.3" y1="234.6" x2="279.3" y2="252.3" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="250.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="283.3" y1="246.8" x2="283.3" y2="264.7" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="251.9" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="287.3" y1="230.5" x2="287.3" y2="261.6" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="236.3" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="291.2" y1="229.4" x2="291.2" y2="252.8" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="238.7" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="295.2" y1="230.5" x2="295.2" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="240.6" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="299.1" y1="244.5" x2="299.1" y2="268.8" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="246.2" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="303.1" y1="250.2" x2="303.1" y2="266.9" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="258.8" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="307.0" y1="258.3" x2="307.0" y2="282.0" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="263.1" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="311.0" y1="240.3" x2="311.0" y2="260.7" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="243.6" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="314.9" y1="223.7" x2="314.9" y2="242.0" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="232.7" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="318.9" y1="225.7" x2="318.9" y2="243.2" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="228.1" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="322.8" y1="225.1" x2="322.8" y2="251.6" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="236.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="326.8" y1="197.2" x2="326.8" y2="235.2" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="202.9" width="2.45" height="30.2" fill="var(--up)"/>
<line x1="330.7" y1="186.4" x2="330.7" y2="217.3" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="202.1" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="334.7" y1="196.2" x2="334.7" y2="216.9" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="196.6" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="338.6" y1="158.9" x2="338.6" y2="205.0" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="167.5" width="2.45" height="36.5" fill="var(--up)"/>
<line x1="342.6" y1="151.4" x2="342.6" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="157.4" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="346.5" y1="149.7" x2="346.5" y2="160.3" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="155.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="350.5" y1="143.3" x2="350.5" y2="158.7" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="143.9" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="354.4" y1="134.5" x2="354.4" y2="145.3" stroke="var(--up)" class="wick"/>
<rect x="353.21" y="141.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="358.4" y1="136.0" x2="358.4" y2="151.7" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="149.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="362.3" y1="148.6" x2="362.3" y2="165.8" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="153.8" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="366.3" y1="159.2" x2="366.3" y2="200.6" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="167.8" width="2.45" height="28.6" fill="var(--down)"/>
<line x1="370.2" y1="118.2" x2="370.2" y2="200.0" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="133.1" width="2.45" height="65.4" fill="var(--up)"/>
<line x1="374.2" y1="105.4" x2="374.2" y2="135.5" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="112.0" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="378.2" y1="100.2" x2="378.2" y2="120.3" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="107.7" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="382.1" y1="93.0" x2="382.1" y2="123.6" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="106.0" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="386.1" y1="88.0" x2="386.1" y2="105.8" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="99.0" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="390.0" y1="96.6" x2="390.0" y2="115.3" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="96.9" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="394.0" y1="93.5" x2="394.0" y2="122.3" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="95.5" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="397.9" y1="89.1" x2="397.9" y2="111.9" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="95.3" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="401.9" y1="72.6" x2="401.9" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="93.9" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="405.8" y1="83.3" x2="405.8" y2="101.2" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="91.1" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="409.8" y1="95.3" x2="409.8" y2="178.7" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="116.1" width="2.45" height="60.3" fill="var(--down)"/>
<line x1="413.7" y1="133.5" x2="413.7" y2="171.4" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="138.6" width="2.45" height="32.9" fill="var(--up)"/>
<line x1="417.7" y1="109.2" x2="417.7" y2="138.4" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="111.5" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="421.6" y1="106.1" x2="421.6" y2="143.3" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="111.0" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="425.6" y1="114.6" x2="425.6" y2="141.6" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="125.8" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="429.5" y1="122.9" x2="429.5" y2="154.4" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="132.0" width="2.45" height="20.6" fill="var(--down)"/>
<line x1="433.5" y1="134.5" x2="433.5" y2="163.9" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="148.1" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="437.4" y1="135.0" x2="437.4" y2="169.8" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="146.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="441.4" y1="135.0" x2="441.4" y2="164.0" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="149.1" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="445.3" y1="137.7" x2="445.3" y2="162.4" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="149.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="449.3" y1="214.5" x2="449.3" y2="346.5" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="226.6" width="2.45" height="108.8" fill="var(--down)"/>
<line x1="453.2" y1="327.6" x2="453.2" y2="397.0" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="343.8" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="457.2" y1="317.2" x2="457.2" y2="426.0" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="329.7" width="2.45" height="57.2" fill="var(--down)"/>
<line x1="461.1" y1="356.3" x2="461.1" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="385.5" width="2.45" height="40.3" fill="var(--down)"/>
<line x1="465.1" y1="405.9" x2="465.1" y2="435.8" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="410.4" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="469.1" y1="471.1" x2="469.1" y2="561.5" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="489.3" width="2.45" height="55.9" fill="var(--down)"/>
<line x1="473.0" y1="504.8" x2="473.0" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="527.6" width="2.45" height="49.9" fill="var(--down)"/>
<line x1="477.0" y1="548.7" x2="477.0" y2="606.1" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="557.3" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="480.9" y1="516.1" x2="480.9" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="518.8" width="2.45" height="32.5" fill="var(--up)"/>
<line x1="484.9" y1="478.5" x2="484.9" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="498.6" width="2.45" height="17.4" fill="var(--down)"/>
<line x1="488.8" y1="477.9" x2="488.8" y2="507.4" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="488.0" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="492.8" y1="484.8" x2="492.8" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="491.9" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="496.7" y1="490.4" x2="496.7" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="493.9" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="500.7" y1="493.7" x2="500.7" y2="535.3" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="506.5" width="2.45" height="27.2" fill="var(--down)"/>
<line x1="504.6" y1="487.1" x2="504.6" y2="547.0" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="491.5" width="2.45" height="49.9" fill="var(--up)"/>
<line x1="508.6" y1="466.1" x2="508.6" y2="490.6" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="474.8" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="512.5" y1="426.1" x2="512.5" y2="465.4" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="431.4" width="2.45" height="34.0" fill="var(--up)"/>
<line x1="516.5" y1="412.6" x2="516.5" y2="443.6" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="417.7" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="520.4" y1="409.5" x2="520.4" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="413.9" width="2.45" height="31.5" fill="var(--up)"/>
<line x1="524.4" y1="399.7" x2="524.4" y2="436.8" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="411.1" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="528.3" y1="391.6" x2="528.3" y2="419.4" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="406.3" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="532.3" y1="387.1" x2="532.3" y2="414.7" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="388.8" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="536.2" y1="383.9" x2="536.2" y2="411.9" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="384.9" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="540.2" y1="393.6" x2="540.2" y2="450.4" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="396.7" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="544.1" y1="407.8" x2="544.1" y2="448.5" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="410.1" width="2.45" height="27.7" fill="var(--down)"/>
<line x1="548.1" y1="425.7" x2="548.1" y2="498.8" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="437.6" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="552.0" y1="458.7" x2="552.0" y2="491.3" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="459.5" width="2.45" height="27.5" fill="var(--down)"/>
<line x1="556.0" y1="462.5" x2="556.0" y2="488.8" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="473.9" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="560.0" y1="458.6" x2="560.0" y2="471.4" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="465.5" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="563.9" y1="436.1" x2="563.9" y2="457.7" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="445.6" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="567.9" y1="452.1" x2="567.9" y2="467.3" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="458.9" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="571.8" y1="461.1" x2="571.8" y2="489.2" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="466.9" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="575.8" y1="460.2" x2="575.8" y2="481.9" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="466.2" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="579.7" y1="443.5" x2="579.7" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="456.3" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="583.7" y1="467.3" x2="583.7" y2="513.9" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="470.5" width="2.45" height="43.1" fill="var(--down)"/>
<line x1="587.6" y1="488.1" x2="587.6" y2="532.9" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="493.2" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="591.6" y1="500.6" x2="591.6" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="509.7" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="595.5" y1="516.5" x2="595.5" y2="538.0" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="523.6" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="599.5" y1="489.5" x2="599.5" y2="520.6" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="493.6" width="2.45" height="20.9" fill="var(--up)"/>
<line x1="603.4" y1="464.5" x2="603.4" y2="495.4" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="469.4" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="607.4" y1="462.1" x2="607.4" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="468.5" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="611.3" y1="443.8" x2="611.3" y2="485.7" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="451.2" width="2.45" height="30.2" fill="var(--up)"/>
<line x1="615.3" y1="437.0" x2="615.3" y2="457.3" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="441.9" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="619.2" y1="433.0" x2="619.2" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="445.4" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="623.2" y1="417.3" x2="623.2" y2="437.3" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="431.0" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="627.1" y1="438.3" x2="627.1" y2="497.2" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="444.9" width="2.45" height="27.6" fill="var(--down)"/>
<line x1="631.1" y1="473.6" x2="631.1" y2="521.3" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="480.0" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="635.0" y1="454.2" x2="635.0" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="454.5" width="2.45" height="41.5" fill="var(--up)"/>
<line x1="639.0" y1="438.3" x2="639.0" y2="472.2" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="451.4" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="642.9" y1="439.2" x2="642.9" y2="464.2" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="453.0" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="646.9" y1="422.1" x2="646.9" y2="438.2" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="431.4" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="650.9" y1="407.1" x2="650.9" y2="431.3" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="414.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="654.8" y1="412.0" x2="654.8" y2="426.6" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="415.0" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="658.8" y1="381.0" x2="658.8" y2="413.7" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="408.9" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="662.7" y1="371.3" x2="662.7" y2="403.1" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="391.6" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="666.7" y1="400.8" x2="666.7" y2="445.4" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="407.9" width="2.45" height="18.6" fill="var(--down)"/>
<line x1="670.6" y1="418.4" x2="670.6" y2="441.8" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="423.5" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="674.6" y1="424.1" x2="674.6" y2="443.4" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="432.2" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="678.5" y1="379.9" x2="678.5" y2="445.1" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="416.8" width="2.45" height="27.1" fill="var(--down)"/>
<line x1="682.5" y1="439.1" x2="682.5" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="444.8" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="686.4" y1="442.1" x2="686.4" y2="465.2" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="451.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="690.4" y1="427.0" x2="690.4" y2="468.6" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="437.7" width="2.45" height="29.4" fill="var(--down)"/>
<line x1="694.3" y1="450.6" x2="694.3" y2="475.7" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="471.2" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="698.3" y1="453.5" x2="698.3" y2="497.9" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="469.7" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="702.2" y1="464.4" x2="702.2" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="474.9" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="706.2" y1="445.2" x2="706.2" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="458.9" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="710.1" y1="462.7" x2="710.1" y2="497.7" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="468.9" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="714.1" y1="477.6" x2="714.1" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="482.9" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="718.0" y1="454.4" x2="718.0" y2="482.4" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="473.0" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="722.0" y1="485.8" x2="722.0" y2="545.5" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="487.8" width="2.45" height="40.3" fill="var(--down)"/>
<line x1="725.9" y1="506.2" x2="725.9" y2="540.9" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="520.4" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="729.9" y1="512.4" x2="729.9" y2="544.0" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="529.8" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="733.8" y1="487.3" x2="733.8" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="494.2" width="2.45" height="41.9" fill="var(--up)"/>
<line x1="737.8" y1="478.2" x2="737.8" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="488.2" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="741.8" y1="494.7" x2="741.8" y2="536.7" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="495.4" width="2.45" height="27.7" fill="var(--up)"/>
<line x1="745.7" y1="494.1" x2="745.7" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="499.4" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="749.7" y1="481.1" x2="749.7" y2="501.7" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="493.6" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="753.6" y1="496.5" x2="753.6" y2="521.5" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="509.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="757.6" y1="489.0" x2="757.6" y2="513.2" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="499.2" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="761.5" y1="482.3" x2="761.5" y2="506.8" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="493.3" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="765.5" y1="459.6" x2="765.5" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="473.6" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="769.4" y1="452.0" x2="769.4" y2="483.3" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="459.3" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="773.4" y1="463.9" x2="773.4" y2="508.3" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="463.9" width="2.45" height="30.1" fill="var(--down)"/>
<line x1="777.3" y1="497.6" x2="777.3" y2="525.7" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="503.9" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="781.3" y1="467.6" x2="781.3" y2="492.3" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="485.7" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="785.2" y1="463.4" x2="785.2" y2="484.3" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="472.2" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="789.2" y1="474.4" x2="789.2" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="481.1" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="793.1" y1="465.2" x2="793.1" y2="508.6" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="471.0" width="2.45" height="30.3" fill="var(--up)"/>
<line x1="797.1" y1="454.0" x2="797.1" y2="482.8" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="466.1" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="801.0" y1="467.3" x2="801.0" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="471.3" width="2.45" height="35.6" fill="var(--down)"/>
<line x1="805.0" y1="486.1" x2="805.0" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="489.5" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="808.9" y1="456.7" x2="808.9" y2="492.3" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="473.3" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="812.9" y1="434.9" x2="812.9" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="444.6" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="816.8" y1="442.0" x2="816.8" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="459.6" width="2.45" height="32.7" fill="var(--down)"/>
<line x1="820.8" y1="492.3" x2="820.8" y2="523.6" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="492.3" width="2.45" height="22.1" fill="var(--down)"/>
<line x1="824.7" y1="512.0" x2="824.7" y2="538.7" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="525.5" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="828.7" y1="501.7" x2="828.7" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="510.7" width="2.45" height="37.4" fill="var(--down)"/>
<line x1="832.7" y1="533.0" x2="832.7" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="541.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="836.6" y1="507.9" x2="836.6" y2="564.2" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="540.7" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="840.6" y1="498.4" x2="840.6" y2="570.4" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="523.1" width="2.45" height="40.7" fill="var(--up)"/>
<line x1="844.5" y1="504.2" x2="844.5" y2="532.4" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="509.6" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="848.5" y1="509.5" x2="848.5" y2="540.5" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="525.9" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="852.4" y1="412.0" x2="852.4" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="427.8" width="2.45" height="50.9" fill="var(--up)"/>
<line x1="856.4" y1="345.1" x2="856.4" y2="402.7" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="345.5" width="2.45" height="55.0" fill="var(--up)"/>
<line x1="860.3" y1="319.7" x2="860.3" y2="385.6" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="321.3" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="864.3" y1="311.0" x2="864.3" y2="343.2" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="321.0" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="868.2" y1="335.5" x2="868.2" y2="376.3" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="338.6" width="2.45" height="37.0" fill="var(--down)"/>
<line x1="872.2" y1="367.1" x2="872.2" y2="402.3" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="368.4" width="2.45" height="20.9" fill="var(--up)"/>
<line x1="876.1" y1="343.1" x2="876.1" y2="387.9" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="350.6" width="2.45" height="25.9" fill="var(--down)"/>
<line x1="880.1" y1="346.1" x2="880.1" y2="368.3" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="352.3" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="884.0" y1="346.0" x2="884.0" y2="392.3" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="348.9" width="2.45" height="34.3" fill="var(--up)"/>
<line x1="888.0" y1="310.0" x2="888.0" y2="347.8" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="330.3" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="891.9" y1="287.1" x2="891.9" y2="329.9" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="287.7" width="2.45" height="32.3" fill="var(--up)"/>
<line x1="895.9" y1="272.4" x2="895.9" y2="317.1" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="291.4" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="899.8" y1="301.9" x2="899.8" y2="335.8" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="302.4" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="903.8" y1="341.1" x2="903.8" y2="386.0" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="366.5" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="907.7" y1="359.3" x2="907.7" y2="383.0" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="359.7" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="911.7" y1="393.1" x2="911.7" y2="415.5" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="395.7" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="915.6" y1="385.9" x2="915.6" y2="411.2" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="390.1" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="919.6" y1="335.3" x2="919.6" y2="372.2" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="345.7" width="2.45" height="22.6" fill="var(--up)"/>
<line x1="923.6" y1="358.5" x2="923.6" y2="457.5" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="396.8" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="927.5" y1="397.0" x2="927.5" y2="427.8" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="408.2" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="931.5" y1="414.7" x2="931.5" y2="462.3" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="426.6" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="935.4" y1="420.2" x2="935.4" y2="446.3" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="425.3" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="939.4" y1="404.6" x2="939.4" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="423.6" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="943.3" y1="415.1" x2="943.3" y2="438.1" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="435.9" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="947.3" y1="407.3" x2="947.3" y2="448.9" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="415.7" width="2.45" height="28.5" fill="var(--down)"/>
<line x1="951.2" y1="439.9" x2="951.2" y2="465.9" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="450.5" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="955.2" y1="433.7" x2="955.2" y2="463.4" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="450.2" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="959.1" y1="435.3" x2="959.1" y2="459.9" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="441.2" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="963.1" y1="436.1" x2="963.1" y2="452.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="441.8" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="967.0" y1="440.1" x2="967.0" y2="462.5" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="443.9" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="971.0" y1="396.9" x2="971.0" y2="440.6" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="402.4" width="2.45" height="28.6" fill="var(--up)"/>
<line x1="974.9" y1="400.6" x2="974.9" y2="430.3" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="404.6" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="978.9" y1="412.0" x2="978.9" y2="444.8" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="424.1" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="982.8" y1="401.4" x2="982.8" y2="437.6" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="417.7" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="986.8" y1="366.4" x2="986.8" y2="414.7" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="389.2" width="2.45" height="25.4" fill="var(--up)"/>
<line x1="990.7" y1="365.5" x2="990.7" y2="392.5" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="371.0" width="2.45" height="20.4" fill="var(--up)"/>
<line x1="994.7" y1="360.8" x2="994.7" y2="383.3" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="366.9" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="998.6" y1="348.4" x2="998.6" y2="373.2" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="360.3" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="1002.6" y1="363.6" x2="1002.6" y2="398.4" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="368.3" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="1006.5" y1="347.8" x2="1006.5" y2="377.6" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="356.7" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="1010.5" y1="329.2" x2="1010.5" y2="361.3" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="356.7" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="1014.5" y1="330.1" x2="1014.5" y2="358.3" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="335.6" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="1018.4" y1="338.5" x2="1018.4" y2="360.2" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="345.1" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="1022.4" y1="295.8" x2="1022.4" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="344.4" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="1026.3" y1="339.8" x2="1026.3" y2="373.8" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="351.7" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="1030.3" y1="309.9" x2="1030.3" y2="352.8" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="310.2" width="2.45" height="38.9" fill="var(--up)"/>
<line x1="1034.2" y1="330.9" x2="1034.2" y2="352.0" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="333.5" width="2.45" height="16.9" fill="var(--up)"/>
<line x1="1038.2" y1="336.8" x2="1038.2" y2="381.2" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="344.9" width="2.45" height="35.5" fill="var(--down)"/>
<line x1="1042.1" y1="372.8" x2="1042.1" y2="417.0" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="384.8" width="2.45" height="31.9" fill="var(--down)"/>
<line x1="1046.1" y1="410.6" x2="1046.1" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="421.2" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="1050.0" y1="423.2" x2="1050.0" y2="452.7" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="433.4" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="60" y1="434.7" x2="1052" y2="434.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="438.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$413 R1</text>
<text x="1058" y="450.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="377.6" x2="1052" y2="377.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="381.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$430 R2</text>
<text x="1058" y="393.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="293.1" x2="1052" y2="293.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="296.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$456 R3</text>
<text x="1058" y="308.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="487.6" x2="1052" y2="487.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="481.6" font-size="11.5" fill="var(--support)" font-weight="600">$397 S1</text>
<text x="1058" y="493.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="541.3" x2="1052" y2="541.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="535.3" font-size="11.5" fill="var(--support)" font-weight="600">$381 S2</text>
<text x="1058" y="547.3" font-size="9.5" fill="var(--muted)">터치 6회</text>
<circle cx="1052.0" cy="441.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="433.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $411 (2026-09-11)</text>
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
| R3 | $456 | 3 | 2026-07-07·07-17·09-01 — Mobility 분사 직후 반등 국면의 고점대 |
| R2 | $430 | 2 | 2026-03-06·04-22 — 2월 급락 이후 1차 반등이 멈춘 자리 |
| R1 | $413 | 3 | 2026-04-08·06-01·06-16 — 봄~초여름 내내 반복 시험된 구간. 현재가 바로 위 |
| **현재가** | **$410.71** (2026-09-11 종가) | — | R1과 S1 사이 |
| S1 | $397 | 3 | 2026-03-11·05-05·08-06 — 2월 저점 이후 반등의 하단, 가장 가까운 지지 |
| S2 | $381 | 6 | 2026-02-24·03-27·04-10·05-13·06-03·06-26 — 터치 6회로 이 구간 최대 밀집대 |
| 참고선 | $361.03 | — | 2026-02-12 장중 52주 최저. 단일 이벤트성 저점이라 클러스터를 이루지 않아 근시일 지지로 보지 않는다 |
| 참고선 | $522.47 | — | 2026-01-15 장중 52주 최고. 현재가와 27% 떨어져 있어 근시일 저항으로 보지 않는다 |

비고 열의 시기는 `--emit dates` 출력을 그대로 옮긴 것이며, 그때 무슨 일이 있었는지는 아래 3. 관측된 특이 구간에서 다룬다.

---

## 3. 관측된 특이 구간

이 1년 구간에는 가격대를 구조적으로 재설정한 사건이 **두 번** 있었고, 둘 다 2026년 2월 초순에 몰려 있다. 특징은 **첫 번째가 이 회사 뉴스가 아니었다는 점**이다.

### 3-1. 2026-02-03 — 동종사(Gartner) 가이던스 쇼크에 따른 동반 급락

- 계기: IT 리서치 기업 Gartner가 FY2026 매출을 전년 대비 −0.6%로 제시하며 "AI 영향으로 고객이 의사결정을 미루고 있다"고 언급, 당일 −31%(시가 기준) 급락([최근 뉴스 / 이슈](./08_news.md) 로그).
- S&P Global은 이날 **자체 발표가 전혀 없었는데도** 종가 기준 전일 대비 **−11.3%** ($499.22 → $442.96)로 최근 1년 중 최대 낙폭을 기록했다. 거래량은 평소(일 217만 주 내외) 대비 약 3.3배인 **712만 주**.
- 같은 날 Moody's −8.9%, FactSet −10%가 뒤따랐다. 즉 이 하락은 회사 고유 사건이 아니라 **정보 서비스 산업 전체의 재평가**였고, 이후 가격대의 기준선이 $500대에서 $400대로 내려앉았다.

### 3-2. 2026-02-10 — FY2026 가이던스 실망

- 계기: FY2026 Adjusted EPS 가이던스 $19.40~$19.65(당시 Mobility 포함 기준)가 컨센서스 $19.96을 하회.
- 종가 기준 전일 대비 **−9.7%** ($420.28 → $379.45), 거래량은 평소 대비 약 **5.3배인 1,151만 주**로 이 구간 최대. 이틀 뒤 장중 $361.03으로 52주 최저를 기록했다.
- 두 사건을 거치며 거래 레짐이 달라졌다 — 2월 이전의 스윙 레벨($500 이상)은 위 표에서 **참고선으로만** 처리했다. 두 달 사이에 −28% 하락한 뒤 형성된 $380~$460 밴드가 그 이후 반년간 실제로 작동한 구간이기 때문이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-12~2026-09-11. 수집 시점: 2026-09-13. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py SPGI --name "S&P Global" --event 2026-02-10:"FY2026 가이던스 실망 급락" --event 2026-07-28:"2분기 EPS 미스" --close-on 2026-09-11 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **가격 연속성 주의 — 2026-07-01 Mobility 분사가 1057:1000 분할로 처리됐다.** 데이터 제공처가 분사를 주식분할과 동일하게 취급해 **그 이전 모든 가격을 약 5.4% 하향 소급조정**했다. 따라서 위 차트의 2026-06-30 이전 가격은 당시 실제 체결가가 아니며, 2월 급락 당시의 실제 종가는 표시된 값보다 약 5% 높았다. 분사 전후 가격이 연속적으로 보이는 것은 이 조정 덕분이고, **레벨 간 상대 위치는 유효하지만 과거 절대 가격을 인용할 때는 이 점을 밝혀야 한다.**
    - 기간 내 배당이 4회 있었으나 원주가(배당 미반영) 기준이므로 차트에 반영되지 않았다.
    - 유효 클러스터가 5개(R3~S2)로 잡혀 템플릿의 3+3 구성과 다르다 — 터치 2회 미만 구간을 억지로 채우지 않았고, 52주 최고·최저는 클러스터를 이루지 않아 참고선으로 분리했다.

---

*작성일: 2026-09-13*
