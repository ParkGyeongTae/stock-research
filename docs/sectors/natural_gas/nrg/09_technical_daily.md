# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-18 종가 $103.66은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.**

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-19 ~ 2026-09-18)

<style>
.nrg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .nrg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.nrg-chart svg { width:100%; height:auto; display:block; }
.nrg-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.nrg-chart .title { fill: var(--ink); font-weight:600; }
.nrg-chart .grid { stroke: var(--grid); stroke-width:1; }
.nrg-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="nrg-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="NRG Energy(NRG) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">NRG Energy (NRG) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-19 ~ 2026-09-18 · 마지막 종가 $103.66 (2026-09-18) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="504.7" x2="1052" y2="504.7" class="grid"/>
<text x="52" y="508.7" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="383.4" x2="1052" y2="383.4" class="grid"/>
<text x="52" y="387.4" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="262.2" x2="1052" y2="262.2" class="grid"/>
<text x="52" y="266.2" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="140.9" x2="1052" y2="140.9" class="grid"/>
<text x="52" y="144.9" font-size="11" text-anchor="end" fill="var(--muted)">180</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="93.6" y1="626.0" x2="93.6" y2="631.0" class="axis"/>
<text x="93.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="184.5" y1="626.0" x2="184.5" y2="631.0" class="axis"/>
<text x="184.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="259.6" y1="626.0" x2="259.6" y2="631.0" class="axis"/>
<text x="259.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="346.5" y1="626.0" x2="346.5" y2="631.0" class="axis"/>
<text x="346.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="425.6" y1="626.0" x2="425.6" y2="631.0" class="axis"/>
<text x="425.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="500.7" y1="626.0" x2="500.7" y2="631.0" class="axis"/>
<text x="500.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="587.6" y1="626.0" x2="587.6" y2="631.0" class="axis"/>
<text x="587.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="670.6" y1="626.0" x2="670.6" y2="631.0" class="axis"/>
<text x="670.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="749.7" y1="626.0" x2="749.7" y2="631.0" class="axis"/>
<text x="749.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="832.7" y1="626.0" x2="832.7" y2="631.0" class="axis"/>
<text x="832.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="919.6" y1="626.0" x2="919.6" y2="631.0" class="axis"/>
<text x="919.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1002.6" y1="626.0" x2="1002.6" y2="631.0" class="axis"/>
<text x="1002.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="227.1" x2="62.0" y2="250.7" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="231.6" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="65.9" y1="189.2" x2="65.9" y2="240.9" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="195.6" width="2.45" height="36.5" fill="var(--up)"/>
<line x1="69.9" y1="192.0" x2="69.9" y2="230.8" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="194.5" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="73.8" y1="206.7" x2="73.8" y2="228.8" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="215.4" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="77.8" y1="232.1" x2="77.8" y2="274.9" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="244.2" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="81.7" y1="204.9" x2="81.7" y2="244.6" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="210.2" width="2.45" height="29.0" fill="var(--up)"/>
<line x1="85.7" y1="200.9" x2="85.7" y2="233.9" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="205.7" width="2.45" height="24.1" fill="var(--down)"/>
<line x1="89.6" y1="226.8" x2="89.6" y2="255.8" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="229.4" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="93.6" y1="229.1" x2="93.6" y2="258.7" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="250.6" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="97.5" y1="210.1" x2="97.5" y2="247.1" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="217.9" width="2.45" height="26.3" fill="var(--up)"/>
<line x1="101.5" y1="188.1" x2="101.5" y2="226.8" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="212.3" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="105.5" y1="201.7" x2="105.5" y2="243.4" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="207.8" width="2.45" height="30.4" fill="var(--down)"/>
<line x1="109.4" y1="227.0" x2="109.4" y2="249.6" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="236.0" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="113.4" y1="205.6" x2="113.4" y2="240.9" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="216.6" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="117.3" y1="201.6" x2="117.3" y2="220.2" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="212.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="121.3" y1="208.6" x2="121.3" y2="259.9" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="215.4" width="2.45" height="44.2" fill="var(--down)"/>
<line x1="125.2" y1="208.9" x2="125.2" y2="236.9" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="209.0" width="2.45" height="27.8" fill="var(--up)"/>
<line x1="129.2" y1="207.7" x2="129.2" y2="243.4" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="228.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="133.1" y1="181.2" x2="133.1" y2="214.5" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="193.5" width="2.45" height="19.0" fill="var(--up)"/>
<line x1="137.1" y1="177.3" x2="137.1" y2="227.4" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="182.8" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="141.0" y1="187.0" x2="141.0" y2="226.5" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="209.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="145.0" y1="183.9" x2="145.0" y2="223.9" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="190.6" width="2.45" height="29.1" fill="var(--down)"/>
<line x1="148.9" y1="214.2" x2="148.9" y2="261.0" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="222.6" width="2.45" height="17.8" fill="var(--down)"/>
<line x1="152.9" y1="229.6" x2="152.9" y2="272.4" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="237.8" width="2.45" height="21.8" fill="var(--down)"/>
<line x1="156.8" y1="238.0" x2="156.8" y2="260.3" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="239.1" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="160.8" y1="198.1" x2="160.8" y2="219.2" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="199.3" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="164.7" y1="181.2" x2="164.7" y2="202.7" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="185.8" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="168.7" y1="177.9" x2="168.7" y2="226.8" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="180.3" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="172.6" y1="137.6" x2="172.6" y2="198.5" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="150.0" width="2.45" height="29.2" fill="var(--up)"/>
<line x1="176.6" y1="140.4" x2="176.6" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="162.5" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="180.5" y1="159.2" x2="180.5" y2="199.3" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="169.5" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="184.5" y1="160.5" x2="184.5" y2="194.4" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="174.4" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="188.4" y1="189.3" x2="188.4" y2="220.3" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="191.5" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="192.4" y1="169.6" x2="192.4" y2="216.9" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="182.2" width="2.45" height="33.3" fill="var(--up)"/>
<line x1="196.4" y1="158.5" x2="196.4" y2="232.2" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="200.9" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="200.3" y1="186.4" x2="200.3" y2="250.0" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="186.4" width="2.45" height="45.6" fill="var(--up)"/>
<line x1="204.3" y1="160.7" x2="204.3" y2="237.3" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="167.3" width="2.45" height="54.1" fill="var(--down)"/>
<line x1="208.2" y1="218.8" x2="208.2" y2="257.6" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="235.1" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="212.2" y1="204.8" x2="212.2" y2="244.6" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="208.6" width="2.45" height="29.0" fill="var(--up)"/>
<line x1="216.1" y1="206.2" x2="216.1" y2="232.2" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="215.2" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="220.1" y1="194.3" x2="220.1" y2="261.8" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="230.7" width="2.45" height="23.9" fill="var(--up)"/>
<line x1="224.0" y1="206.1" x2="224.0" y2="248.6" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="230.7" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="228.0" y1="209.4" x2="228.0" y2="255.3" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="223.1" width="2.45" height="30.9" fill="var(--up)"/>
<line x1="231.9" y1="180.2" x2="231.9" y2="224.2" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="208.8" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="235.9" y1="172.9" x2="235.9" y2="260.0" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="177.6" width="2.45" height="81.8" fill="var(--down)"/>
<line x1="239.8" y1="253.7" x2="239.8" y2="290.1" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="259.0" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="243.8" y1="213.8" x2="243.8" y2="268.5" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="220.6" width="2.45" height="39.5" fill="var(--up)"/>
<line x1="247.7" y1="211.7" x2="247.7" y2="256.1" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="218.6" width="2.45" height="20.5" fill="var(--down)"/>
<line x1="251.7" y1="202.1" x2="251.7" y2="228.2" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="210.4" width="2.45" height="16.1" fill="var(--up)"/>
<line x1="255.6" y1="190.8" x2="255.6" y2="211.2" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="201.5" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="259.6" y1="216.3" x2="259.6" y2="239.4" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="216.4" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="263.5" y1="213.2" x2="263.5" y2="245.4" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="220.1" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="267.5" y1="219.7" x2="267.5" y2="260.8" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="221.1" width="2.45" height="18.3" fill="var(--up)"/>
<line x1="271.4" y1="200.4" x2="271.4" y2="225.8" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="205.4" width="2.45" height="19.5" fill="var(--up)"/>
<line x1="275.4" y1="200.0" x2="275.4" y2="245.3" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="208.4" width="2.45" height="35.6" fill="var(--down)"/>
<line x1="279.3" y1="218.6" x2="279.3" y2="248.8" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="236.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="283.3" y1="192.0" x2="283.3" y2="236.0" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="221.2" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="287.3" y1="201.2" x2="287.3" y2="242.5" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="212.7" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="291.2" y1="196.4" x2="291.2" y2="236.3" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="197.7" width="2.45" height="34.1" fill="var(--up)"/>
<line x1="295.2" y1="187.0" x2="295.2" y2="258.7" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="189.4" width="2.45" height="64.0" fill="var(--down)"/>
<line x1="299.1" y1="243.6" x2="299.1" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="250.7" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="303.1" y1="248.4" x2="303.1" y2="277.6" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="261.3" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="307.0" y1="255.6" x2="307.0" y2="335.1" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="258.9" width="2.45" height="67.1" fill="var(--down)"/>
<line x1="311.0" y1="273.0" x2="311.0" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="294.7" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="314.9" y1="276.8" x2="314.9" y2="294.3" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="285.2" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="318.9" y1="273.7" x2="318.9" y2="296.4" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="273.7" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="322.8" y1="263.9" x2="322.8" y2="282.5" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="273.6" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="326.8" y1="255.3" x2="326.8" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="258.8" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="330.7" y1="253.0" x2="330.7" y2="271.9" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="256.8" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="334.7" y1="237.6" x2="334.7" y2="260.0" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="256.3" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="338.6" y1="250.0" x2="338.6" y2="264.8" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="253.4" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="342.6" y1="254.9" x2="342.6" y2="267.1" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="257.1" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="346.5" y1="221.8" x2="346.5" y2="256.3" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="224.8" width="2.45" height="27.8" fill="var(--up)"/>
<line x1="350.5" y1="200.1" x2="350.5" y2="268.2" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="210.7" width="2.45" height="41.8" fill="var(--down)"/>
<line x1="354.4" y1="254.8" x2="354.4" y2="287.5" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="254.8" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="358.4" y1="275.0" x2="358.4" y2="333.7" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="277.3" width="2.45" height="52.1" fill="var(--down)"/>
<line x1="362.3" y1="328.9" x2="362.3" y2="371.5" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="334.6" width="2.45" height="27.5" fill="var(--down)"/>
<line x1="366.3" y1="312.0" x2="366.3" y2="337.2" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="318.9" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="370.2" y1="324.4" x2="370.2" y2="347.1" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="329.5" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="374.2" y1="308.6" x2="374.2" y2="332.6" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="319.2" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="378.2" y1="319.0" x2="378.2" y2="337.9" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="323.8" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="382.1" y1="266.7" x2="382.1" y2="314.3" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="271.3" width="2.45" height="39.2" fill="var(--up)"/>
<line x1="386.1" y1="281.7" x2="386.1" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="300.1" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="390.0" y1="307.1" x2="390.0" y2="350.0" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="329.4" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="394.0" y1="311.2" x2="394.0" y2="339.5" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="315.2" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="397.9" y1="301.2" x2="397.9" y2="325.5" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="305.7" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="401.9" y1="309.2" x2="401.9" y2="341.5" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="316.9" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="405.8" y1="314.7" x2="405.8" y2="328.9" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="321.5" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="409.8" y1="283.9" x2="409.8" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="286.2" width="2.45" height="40.7" fill="var(--up)"/>
<line x1="413.7" y1="277.3" x2="413.7" y2="304.6" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="280.4" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="417.7" y1="279.1" x2="417.7" y2="315.7" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="290.1" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="421.6" y1="280.5" x2="421.6" y2="317.5" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="303.9" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="425.6" y1="302.7" x2="425.6" y2="331.4" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="310.0" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="429.5" y1="295.2" x2="429.5" y2="336.6" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="309.6" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="433.5" y1="301.8" x2="433.5" y2="380.5" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="311.2" width="2.45" height="48.0" fill="var(--down)"/>
<line x1="437.4" y1="338.2" x2="437.4" y2="372.5" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="356.5" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="441.4" y1="301.2" x2="441.4" y2="334.9" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="302.7" width="2.45" height="26.4" fill="var(--up)"/>
<line x1="445.3" y1="272.2" x2="445.3" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="288.1" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="449.3" y1="270.1" x2="449.3" y2="298.5" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="280.2" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="453.2" y1="256.3" x2="453.2" y2="282.7" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="258.3" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="457.2" y1="224.3" x2="457.2" y2="271.5" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="248.8" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="461.1" y1="185.3" x2="461.1" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="187.3" width="2.45" height="64.6" fill="var(--up)"/>
<line x1="465.1" y1="154.8" x2="465.1" y2="196.3" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="180.6" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="469.1" y1="162.5" x2="469.1" y2="198.2" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="174.2" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="473.0" y1="169.5" x2="473.0" y2="203.6" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="171.2" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="477.0" y1="140.2" x2="477.0" y2="177.3" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="145.9" width="2.45" height="24.5" fill="var(--up)"/>
<line x1="480.9" y1="128.5" x2="480.9" y2="170.5" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="155.8" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="484.9" y1="111.5" x2="484.9" y2="239.4" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="116.5" width="2.45" height="65.2" fill="var(--up)"/>
<line x1="488.8" y1="80.5" x2="488.8" y2="135.5" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="101.1" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="492.8" y1="118.6" x2="492.8" y2="179.8" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="122.7" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="496.7" y1="134.3" x2="496.7" y2="176.0" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="141.0" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="500.7" y1="131.3" x2="500.7" y2="177.0" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="167.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="504.6" y1="237.6" x2="504.6" y2="274.3" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="244.9" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="508.6" y1="223.2" x2="508.6" y2="250.6" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="240.7" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="512.5" y1="230.9" x2="512.5" y2="274.1" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="250.0" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="516.5" y1="265.6" x2="516.5" y2="297.2" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="269.5" width="2.45" height="27.1" fill="var(--down)"/>
<line x1="520.4" y1="288.9" x2="520.4" y2="328.9" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="289.9" width="2.45" height="28.7" fill="var(--up)"/>
<line x1="524.4" y1="266.0" x2="524.4" y2="292.5" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="286.4" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="528.3" y1="295.5" x2="528.3" y2="337.8" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="297.3" width="2.45" height="33.8" fill="var(--down)"/>
<line x1="532.3" y1="307.6" x2="532.3" y2="345.5" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="310.1" width="2.45" height="33.4" fill="var(--up)"/>
<line x1="536.2" y1="293.9" x2="536.2" y2="315.2" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="295.3" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="540.2" y1="277.0" x2="540.2" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="286.4" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="544.1" y1="287.6" x2="544.1" y2="306.9" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="294.0" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="548.1" y1="247.5" x2="548.1" y2="280.4" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="267.6" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="552.0" y1="244.1" x2="552.0" y2="293.7" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="253.7" width="2.45" height="28.9" fill="var(--up)"/>
<line x1="556.0" y1="247.0" x2="556.0" y2="355.6" stroke="var(--down)" class="wick"/>
<rect x="554.77" y="253.0" width="2.45" height="95.3" fill="var(--down)"/>
<line x1="560.0" y1="294.3" x2="560.0" y2="341.1" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="312.1" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="563.9" y1="292.1" x2="563.9" y2="320.3" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="316.0" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="567.9" y1="293.6" x2="567.9" y2="320.6" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="306.8" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="571.8" y1="319.5" x2="571.8" y2="356.9" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="329.4" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="575.8" y1="319.4" x2="575.8" y2="347.0" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="336.5" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="579.7" y1="315.2" x2="579.7" y2="384.1" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="319.8" width="2.45" height="56.2" fill="var(--down)"/>
<line x1="583.7" y1="341.7" x2="583.7" y2="374.4" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="346.2" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="587.6" y1="317.5" x2="587.6" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="323.4" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="591.6" y1="305.8" x2="591.6" y2="348.0" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="306.5" width="2.45" height="41.5" fill="var(--up)"/>
<line x1="595.5" y1="299.7" x2="595.5" y2="324.3" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="308.0" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="599.5" y1="303.0" x2="599.5" y2="327.7" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="304.3" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="603.4" y1="255.6" x2="603.4" y2="278.2" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="259.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="607.4" y1="219.4" x2="607.4" y2="258.0" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="251.4" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="611.3" y1="220.4" x2="611.3" y2="250.0" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="237.5" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="615.3" y1="198.9" x2="615.3" y2="256.8" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="200.1" width="2.45" height="50.1" fill="var(--up)"/>
<line x1="619.2" y1="168.1" x2="619.2" y2="205.5" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="189.2" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="623.2" y1="198.7" x2="623.2" y2="226.9" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="201.0" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="627.1" y1="195.2" x2="627.1" y2="223.8" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="209.4" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="631.1" y1="193.3" x2="631.1" y2="224.0" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="207.6" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="635.0" y1="202.9" x2="635.0" y2="284.9" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="206.7" width="2.45" height="72.5" fill="var(--down)"/>
<line x1="639.0" y1="271.3" x2="639.0" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="281.9" width="2.45" height="41.8" fill="var(--down)"/>
<line x1="642.9" y1="304.1" x2="642.9" y2="329.1" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="312.0" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="646.9" y1="295.3" x2="646.9" y2="330.1" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="295.3" width="2.45" height="26.4" fill="var(--up)"/>
<line x1="650.9" y1="258.1" x2="650.9" y2="298.6" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="263.3" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="654.8" y1="253.9" x2="654.8" y2="278.0" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="256.8" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="658.8" y1="266.7" x2="658.8" y2="294.2" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="283.0" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="662.7" y1="285.5" x2="662.7" y2="331.0" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="293.6" width="2.45" height="35.2" fill="var(--down)"/>
<line x1="666.7" y1="287.3" x2="666.7" y2="317.8" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="289.0" width="2.45" height="27.6" fill="var(--up)"/>
<line x1="670.6" y1="280.4" x2="670.6" y2="309.8" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="293.6" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="674.6" y1="284.2" x2="674.6" y2="308.6" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="293.6" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="678.5" y1="266.7" x2="678.5" y2="285.9" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="277.8" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="682.5" y1="275.3" x2="682.5" y2="328.9" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="303.5" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="686.4" y1="314.7" x2="686.4" y2="374.0" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="317.6" width="2.45" height="54.6" fill="var(--down)"/>
<line x1="690.4" y1="353.4" x2="690.4" y2="397.0" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="361.9" width="2.45" height="33.0" fill="var(--down)"/>
<line x1="694.3" y1="388.8" x2="694.3" y2="401.8" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="395.3" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="698.3" y1="393.1" x2="698.3" y2="419.6" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="399.6" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="702.2" y1="395.6" x2="702.2" y2="448.7" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="400.7" width="2.45" height="36.8" fill="var(--down)"/>
<line x1="706.2" y1="414.4" x2="706.2" y2="439.8" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="415.5" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="710.1" y1="430.4" x2="710.1" y2="458.4" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="432.0" width="2.45" height="25.4" fill="var(--down)"/>
<line x1="714.1" y1="456.9" x2="714.1" y2="479.5" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="460.1" width="2.45" height="11.3" fill="var(--down)"/>
<line x1="718.0" y1="479.5" x2="718.0" y2="497.3" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="480.5" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="722.0" y1="418.4" x2="722.0" y2="462.3" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="420.0" width="2.45" height="41.3" fill="var(--up)"/>
<line x1="725.9" y1="400.5" x2="725.9" y2="428.1" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="402.1" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="729.9" y1="384.4" x2="729.9" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="397.7" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="733.8" y1="364.8" x2="733.8" y2="390.2" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="380.8" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="737.8" y1="374.2" x2="737.8" y2="407.2" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="385.3" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="741.8" y1="389.8" x2="741.8" y2="413.3" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="398.6" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="745.7" y1="394.2" x2="745.7" y2="420.4" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="407.6" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="749.7" y1="434.1" x2="749.7" y2="461.6" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="437.5" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="753.6" y1="408.6" x2="753.6" y2="449.5" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="422.8" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="757.6" y1="402.0" x2="757.6" y2="432.1" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="421.3" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="761.5" y1="414.7" x2="761.5" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="422.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="765.5" y1="431.0" x2="765.5" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="434.4" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="769.4" y1="446.0" x2="769.4" y2="460.4" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="448.1" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="773.4" y1="435.5" x2="773.4" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="444.3" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="777.3" y1="455.7" x2="777.3" y2="504.1" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="460.5" width="2.45" height="40.3" fill="var(--down)"/>
<line x1="781.3" y1="478.3" x2="781.3" y2="501.4" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="482.3" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="785.2" y1="444.1" x2="785.2" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="471.6" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="789.2" y1="435.4" x2="789.2" y2="465.7" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="441.7" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="793.1" y1="410.5" x2="793.1" y2="441.0" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="431.4" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="797.1" y1="412.4" x2="797.1" y2="439.1" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="431.2" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="801.0" y1="380.1" x2="801.0" y2="424.7" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="413.4" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="805.0" y1="389.3" x2="805.0" y2="411.7" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="390.1" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="808.9" y1="390.3" x2="808.9" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="397.6" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="812.9" y1="365.4" x2="812.9" y2="402.5" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="370.0" width="2.45" height="27.4" fill="var(--up)"/>
<line x1="816.8" y1="338.7" x2="816.8" y2="362.2" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="340.3" width="2.45" height="19.6" fill="var(--up)"/>
<line x1="820.8" y1="319.7" x2="820.8" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="326.7" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="824.7" y1="316.9" x2="824.7" y2="346.0" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="325.6" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="828.7" y1="318.2" x2="828.7" y2="352.1" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="327.8" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="832.7" y1="348.0" x2="832.7" y2="398.7" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="349.7" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="836.6" y1="371.0" x2="836.6" y2="412.8" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="378.5" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="840.6" y1="371.0" x2="840.6" y2="395.6" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="377.3" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="844.5" y1="374.7" x2="844.5" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="377.8" width="2.45" height="17.7" fill="var(--down)"/>
<line x1="848.5" y1="391.1" x2="848.5" y2="412.4" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="396.4" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="852.4" y1="364.1" x2="852.4" y2="387.1" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="380.5" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="856.4" y1="362.4" x2="856.4" y2="382.1" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="373.9" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="860.3" y1="381.4" x2="860.3" y2="398.2" stroke="var(--up)" class="wick"/>
<rect x="859.09" y="386.6" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="864.3" y1="354.8" x2="864.3" y2="402.5" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="367.3" width="2.45" height="26.1" fill="var(--down)"/>
<line x1="868.2" y1="362.0" x2="868.2" y2="404.6" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="379.6" width="2.45" height="16.6" fill="var(--down)"/>
<line x1="872.2" y1="391.0" x2="872.2" y2="436.1" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="401.6" width="2.45" height="25.8" fill="var(--down)"/>
<line x1="876.1" y1="430.1" x2="876.1" y2="453.1" stroke="var(--down)" class="wick"/>
<rect x="874.90" y="440.7" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="880.1" y1="432.8" x2="880.1" y2="449.1" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="440.6" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="884.0" y1="417.6" x2="884.0" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="428.7" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="888.0" y1="379.9" x2="888.0" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="383.6" width="2.45" height="53.8" fill="var(--up)"/>
<line x1="891.9" y1="364.1" x2="891.9" y2="396.5" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="365.3" width="2.45" height="25.2" fill="var(--up)"/>
<line x1="895.9" y1="358.0" x2="895.9" y2="388.1" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="366.6" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="899.8" y1="371.2" x2="899.8" y2="411.3" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="371.4" width="2.45" height="33.3" fill="var(--down)"/>
<line x1="903.8" y1="410.2" x2="903.8" y2="463.5" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="415.4" width="2.45" height="43.5" fill="var(--down)"/>
<line x1="907.7" y1="452.6" x2="907.7" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="462.9" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="911.7" y1="410.6" x2="911.7" y2="452.0" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="420.0" width="2.45" height="30.1" fill="var(--up)"/>
<line x1="915.6" y1="395.9" x2="915.6" y2="430.7" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="404.2" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="919.6" y1="379.1" x2="919.6" y2="434.8" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="392.7" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="923.6" y1="383.3" x2="923.6" y2="550.2" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="383.4" width="2.45" height="139.2" fill="var(--down)"/>
<line x1="927.5" y1="476.2" x2="927.5" y2="518.2" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="500.3" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="931.5" y1="486.7" x2="931.5" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="497.0" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="935.4" y1="484.7" x2="935.4" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="510.8" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="939.4" y1="496.0" x2="939.4" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="938.14" y="511.3" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="943.3" y1="490.1" x2="943.3" y2="508.1" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="506.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="947.3" y1="479.3" x2="947.3" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="492.6" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="951.2" y1="492.2" x2="951.2" y2="508.3" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="504.7" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="955.2" y1="466.7" x2="955.2" y2="504.7" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="466.9" width="2.45" height="37.8" fill="var(--up)"/>
<line x1="959.1" y1="459.1" x2="959.1" y2="496.4" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="459.9" width="2.45" height="30.5" fill="var(--down)"/>
<line x1="963.1" y1="489.4" x2="963.1" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="493.1" width="2.45" height="38.6" fill="var(--down)"/>
<line x1="967.0" y1="499.9" x2="967.0" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="501.2" width="2.45" height="26.6" fill="var(--up)"/>
<line x1="971.0" y1="498.1" x2="971.0" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="505.0" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="974.9" y1="521.5" x2="974.9" y2="546.8" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="525.5" width="2.45" height="21.0" fill="var(--down)"/>
<line x1="978.9" y1="538.3" x2="978.9" y2="557.5" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="545.2" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="982.8" y1="531.2" x2="982.8" y2="547.8" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="541.0" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="986.8" y1="520.6" x2="986.8" y2="541.2" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="528.1" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="990.7" y1="521.0" x2="990.7" y2="545.7" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="528.0" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="994.7" y1="534.5" x2="994.7" y2="561.4" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="536.9" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="998.6" y1="559.4" x2="998.6" y2="574.2" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="563.5" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="1002.6" y1="552.3" x2="1002.6" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="568.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1006.5" y1="553.7" x2="1006.5" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="558.8" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="1010.5" y1="541.1" x2="1010.5" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="551.8" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="1014.5" y1="509.3" x2="1014.5" y2="557.5" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="510.7" width="2.45" height="46.9" fill="var(--up)"/>
<line x1="1018.4" y1="494.5" x2="1018.4" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="499.1" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="1022.4" y1="511.2" x2="1022.4" y2="537.5" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="513.5" width="2.45" height="19.3" fill="var(--down)"/>
<line x1="1026.3" y1="535.3" x2="1026.3" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="538.9" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="1030.3" y1="535.1" x2="1030.3" y2="552.2" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="543.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1034.2" y1="556.4" x2="1034.2" y2="581.1" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="565.4" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="1038.2" y1="567.5" x2="1038.2" y2="594.9" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="568.8" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="1042.1" y1="572.6" x2="1042.1" y2="587.6" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="578.2" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="1046.1" y1="557.8" x2="1046.1" y2="589.4" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="566.9" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="1050.0" y1="582.9" x2="1050.0" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="591.3" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="60" y1="359.2" x2="1052" y2="359.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="362.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$144 R1</text>
<text x="1058" y="374.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="270.3" x2="1052" y2="270.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="273.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$159 R2</text>
<text x="1058" y="285.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="182.2" x2="1052" y2="182.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="185.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$173 R3</text>
<text x="1058" y="197.7" font-size="9.5" fill="var(--muted)">터치 6회</text>
<circle cx="1052.0" cy="603.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="595.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $104 (2026-09-18)</text>
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
| R3 | $173 | 6 | 2025년 10월~2026년 1월 및 2026-04-14의 스윙 고점대(6회). **AI 전력 수요 재평가가 정점이던 구간**이며, 52주 최고 $189.96도 이 시기에 나왔다 |
| R2 | $159 | 3 | 2026-01-15·2026-01-28·2026-05-05 스윙 고점대(3회). **LS Power 인수 종결(2026-01-29) 전후**에 몰려 있다 |
| R1 | $144 | 3 | 2026-05-26·2026-07-14·2026-07-24 스윙 고점대(3회). 2분기 실적발표(2026-08-03) 직전까지 유지되던 가격대 |
| **현재가** | **$103.66** (2026-09-18 종가) | — | **기간 내 하단 스윙 저점 없음(신저가 구간)** — 가장 가까운 레벨은 40% 위의 R1이다. 52주 최저 $103.49에서 0.2% 위 |

> **지지선이 하나도 없다는 것이 이 표의 결론이다.** 최근 1년 안에 현재가 아래에서 형성된 스윙 저점 클러스터가 존재하지 않으므로 S1·S2·S3 행 자체를 두지 않았다 — 억지로 채우면 없는 레벨을 만들어내는 것이 된다. **현재가는 1년치 거래 범위의 맨 아래**이며, 이 아래의 참고 가격대를 보려면 [주봉·5년](./10_technical_weekly.md)로 내려가야 한다.
>
> 참고선으로 둘 만한 것은 **52주 최고 $189.96**(현재가 대비 +83%)인데, R3($173)보다 위에 단독으로 찍힌 값이라 클러스터를 이루지 않았다 — 근시일 저항으로 보기 어렵고 구간 상단의 기록으로만 읽는다.

---

## 3. 관측된 특이 구간 — 2026년 하반기의 계단식 하락

**단일 이벤트로 인한 갭이 아니라 3개월에 걸친 연속 하락**이라, 이 절은 특정 날짜가 아니라 구간을 다룬다.

- R1($144) 부근에서 마지막으로 버틴 것이 2026-07-24이고, **2026-08-03 2분기 실적발표 이후 반등 없이 내려왔다.** 실적 자체는 Adjusted EBITDA +34%·가이던스 재확인으로 나쁘지 않았으나 **Adjusted EPS가 전년 대비 −13.9%**였고, 같은 날 상반기 누계가 −32.4%임이 확인됐다([최근 뉴스 / 이슈](./08_news.md)).
- 이후 9월 들어 하락이 가팔라졌다 — **ERCOT 2027년 선도 전력가격 약세와 미국 10년물 국채금리 5%대 진입**이 겹친 구간이며([미국 10년물 국채금리](../../../macro/rates/treasury_10y.md)), 9월 한 달만 −11%다.
- **거래 레짐이 달라진 흔적은 레벨 분포 자체에 남아 있다.** R3(6회)·R2(3회)·R1(3회)로 저항은 촘촘한데 지지는 하나도 없다 — **위쪽에만 매물대가 쌓인 전형적인 하락 추세 구조**이며, 반등 시 R1($144, +39%)까지 빈 구간이 넓다는 것은 양방향 모두에 해당한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-19~2026-09-18. 수집 시점: 2026-09-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py NRG --name "NRG Energy" --close-on 2026-09-18 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨을 3개만 쓴 것이 아니라 3개밖에 나오지 않았다.** 현재가 아래에 유효한 스윙 저점 클러스터가 없어 지지선 행을 두지 않았고, `--force-level`로 억지로 만들지도 않았다.
    - **기간 내 배당 4회가 반영되지 않은 원주가다.** 연 $1.88 수준이라 1년 총수익률과 차트상 하락률이 약 1.8%p 어긋난다.
    - **2026-01-29 LS Power 인수는 주가 연속성을 깨는 이벤트가 아니다**(주식분할·액면변경이 아니라 신주 발행이므로 주가는 연속). 다만 인수 대가로 희석주식수가 6.5% 늘어 **주가 흐름과 시가총액 흐름이 그만큼 다르게 움직인다**는 점은 [핵심 지표](./04_metrics.md) A.2와 함께 봐야 한다.

---

*작성일: 2026-09-19*
