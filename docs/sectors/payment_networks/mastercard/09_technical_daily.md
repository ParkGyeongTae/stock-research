# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-01 종가 **$581.10**은 [핵심 지표](./04_metrics.md) A.2의 "현재" 주가 및 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치**한다. 세 문서 모두 배당 미반영 원주가 기준이며, 이 기간에 주식분할은 없었다.

---

## 1. 차트 — 최근 1년 일봉 (2025-09-02 ~ 2026-09-01)

<div class="ma-chart">
<style>
.ma-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ma-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ma-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ma-chart svg { width:100%; height:auto; display:block; }
.ma-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ma-chart .title { fill: var(--ink); font-weight:600; }
.ma-chart .grid { stroke: var(--grid); stroke-width:1; }
.ma-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mastercard(MA) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Mastercard (MA) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-02 ~ 2026-09-01 · 마지막 종가 $581.10 (2026-09-01) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">460</text>
<line x1="60" y1="548.7" x2="1052" y2="548.7" class="grid"/>
<text x="52" y="552.7" font-size="11" text-anchor="end" fill="var(--muted)">480</text>
<line x1="60" y1="471.4" x2="1052" y2="471.4" class="grid"/>
<text x="52" y="475.4" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="394.1" x2="1052" y2="394.1" class="grid"/>
<text x="52" y="398.1" font-size="11" text-anchor="end" fill="var(--muted)">520</text>
<line x1="60" y1="316.8" x2="1052" y2="316.8" class="grid"/>
<text x="52" y="320.8" font-size="11" text-anchor="end" fill="var(--muted)">540</text>
<line x1="60" y1="239.6" x2="1052" y2="239.6" class="grid"/>
<text x="52" y="243.6" font-size="11" text-anchor="end" fill="var(--muted)">560</text>
<line x1="60" y1="162.3" x2="1052" y2="162.3" class="grid"/>
<text x="52" y="166.3" font-size="11" text-anchor="end" fill="var(--muted)">580</text>
<line x1="60" y1="85.0" x2="1052" y2="85.0" class="grid"/>
<text x="52" y="89.0" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="145.0" y1="626.0" x2="145.0" y2="631.0" class="axis"/>
<text x="145.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="235.9" y1="626.0" x2="235.9" y2="631.0" class="axis"/>
<text x="235.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="311.0" y1="626.0" x2="311.0" y2="631.0" class="axis"/>
<text x="311.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="397.9" y1="626.0" x2="397.9" y2="631.0" class="axis"/>
<text x="397.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="477.0" y1="626.0" x2="477.0" y2="631.0" class="axis"/>
<text x="477.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="552.0" y1="626.0" x2="552.0" y2="631.0" class="axis"/>
<text x="552.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="639.0" y1="626.0" x2="639.0" y2="631.0" class="axis"/>
<text x="639.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="722.0" y1="626.0" x2="722.0" y2="631.0" class="axis"/>
<text x="722.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="801.0" y1="626.0" x2="801.0" y2="631.0" class="axis"/>
<text x="801.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="884.0" y1="626.0" x2="884.0" y2="631.0" class="axis"/>
<text x="884.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="971.0" y1="626.0" x2="971.0" y2="631.0" class="axis"/>
<text x="971.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1050.0" y1="626.0" x2="1050.0" y2="631.0" class="axis"/>
<text x="1050.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="101.9" x2="62.0" y2="139.1" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="101.9" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="65.9" y1="108.2" x2="65.9" y2="127.6" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="111.0" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="69.9" y1="100.9" x2="69.9" y2="126.4" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="101.8" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="73.8" y1="90.5" x2="73.8" y2="166.0" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="102.5" width="2.45" height="43.5" fill="var(--down)"/>
<line x1="77.8" y1="124.4" x2="77.8" y2="159.6" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="136.8" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="81.7" y1="119.1" x2="81.7" y2="149.5" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="146.8" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="85.7" y1="154.0" x2="85.7" y2="197.1" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="154.0" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="89.6" y1="123.7" x2="89.6" y2="162.2" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="128.5" width="2.45" height="30.3" fill="var(--up)"/>
<line x1="93.6" y1="126.7" x2="93.6" y2="162.3" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="137.4" width="2.45" height="23.3" fill="var(--down)"/>
<line x1="97.5" y1="137.2" x2="97.5" y2="156.5" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="150.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="101.5" y1="130.9" x2="101.5" y2="174.5" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="137.5" width="2.45" height="32.5" fill="var(--up)"/>
<line x1="105.5" y1="89.3" x2="105.5" y2="133.5" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="90.3" width="2.45" height="42.2" fill="var(--up)"/>
<line x1="109.4" y1="78.7" x2="109.4" y2="139.5" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="100.1" width="2.45" height="38.8" fill="var(--down)"/>
<line x1="113.4" y1="128.0" x2="113.4" y2="156.4" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="129.0" width="2.45" height="17.2" fill="var(--down)"/>
<line x1="117.3" y1="133.9" x2="117.3" y2="161.7" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="144.9" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="121.3" y1="135.8" x2="121.3" y2="207.7" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="141.2" width="2.45" height="59.8" fill="var(--down)"/>
<line x1="125.2" y1="194.5" x2="125.2" y2="220.4" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="196.0" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="129.2" y1="191.7" x2="129.2" y2="221.9" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="211.3" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="133.1" y1="202.2" x2="133.1" y2="223.9" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="214.0" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="137.1" y1="203.5" x2="137.1" y2="229.9" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="208.1" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="141.0" y1="198.5" x2="141.0" y2="225.5" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="205.5" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="145.0" y1="179.8" x2="145.0" y2="220.2" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="186.3" width="2.45" height="31.3" fill="var(--up)"/>
<line x1="148.9" y1="162.9" x2="148.9" y2="197.9" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="172.6" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="152.9" y1="149.8" x2="152.9" y2="176.1" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="160.5" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="156.8" y1="157.9" x2="156.8" y2="203.8" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="165.2" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="160.8" y1="138.8" x2="160.8" y2="166.5" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="162.9" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="164.7" y1="150.4" x2="164.7" y2="177.4" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="157.2" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="168.7" y1="164.6" x2="168.7" y2="229.9" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="172.9" width="2.45" height="49.0" fill="var(--down)"/>
<line x1="172.6" y1="203.2" x2="172.6" y2="252.4" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="210.3" width="2.45" height="39.0" fill="var(--down)"/>
<line x1="176.6" y1="220.2" x2="176.6" y2="266.6" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="242.5" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="180.5" y1="201.6" x2="180.5" y2="255.0" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="209.0" width="2.45" height="46.1" fill="var(--up)"/>
<line x1="184.5" y1="206.0" x2="184.5" y2="241.9" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="222.9" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="188.4" y1="221.6" x2="188.4" y2="288.3" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="228.7" width="2.45" height="49.9" fill="var(--down)"/>
<line x1="192.4" y1="228.7" x2="192.4" y2="270.4" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="235.8" width="2.45" height="32.8" fill="var(--up)"/>
<line x1="196.4" y1="210.9" x2="196.4" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="215.0" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="200.3" y1="177.8" x2="200.3" y2="236.6" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="193.1" width="2.45" height="38.1" fill="var(--up)"/>
<line x1="204.3" y1="176.1" x2="204.3" y2="206.4" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="195.7" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="208.2" y1="173.9" x2="208.2" y2="194.5" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="184.1" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="212.2" y1="159.1" x2="212.2" y2="189.0" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="172.9" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="216.1" y1="178.8" x2="216.1" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="178.8" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="220.1" y1="185.5" x2="220.1" y2="218.5" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="189.0" width="2.45" height="27.6" fill="var(--down)"/>
<line x1="224.0" y1="213.2" x2="224.0" y2="273.5" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="233.3" width="2.45" height="27.2" fill="var(--down)"/>
<line x1="228.0" y1="228.3" x2="228.0" y2="295.1" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="264.0" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="231.9" y1="261.1" x2="231.9" y2="303.2" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="270.5" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="235.9" y1="274.3" x2="235.9" y2="315.5" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="278.2" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="239.8" y1="262.6" x2="239.8" y2="307.3" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="267.6" width="2.45" height="30.6" fill="var(--up)"/>
<line x1="243.8" y1="253.7" x2="243.8" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="265.4" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="247.7" y1="258.9" x2="247.7" y2="286.5" stroke="var(--up)" class="wick"/>
<rect x="246.50" y="265.5" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="251.7" y1="244.7" x2="251.7" y2="275.6" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="263.5" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="255.6" y1="260.0" x2="255.6" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="266.8" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="259.6" y1="245.2" x2="259.6" y2="285.9" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="245.9" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="263.5" y1="216.7" x2="263.5" y2="245.7" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="234.8" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="267.5" y1="225.6" x2="267.5" y2="259.4" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="240.0" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="271.4" y1="251.2" x2="271.4" y2="301.2" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="254.9" width="2.45" height="39.8" fill="var(--down)"/>
<line x1="275.4" y1="280.8" x2="275.4" y2="331.5" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="293.7" width="2.45" height="35.4" fill="var(--down)"/>
<line x1="279.3" y1="332.3" x2="279.3" y2="376.0" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="341.7" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="283.3" y1="351.6" x2="283.3" y2="374.9" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="354.1" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="287.3" y1="322.8" x2="287.3" y2="366.4" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="342.8" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="291.2" y1="299.8" x2="291.2" y2="349.0" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="315.3" width="2.45" height="30.4" fill="var(--up)"/>
<line x1="295.2" y1="301.2" x2="295.2" y2="335.7" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="303.6" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="299.1" y1="276.7" x2="299.1" y2="320.7" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="291.8" width="2.45" height="19.2" fill="var(--up)"/>
<line x1="303.1" y1="283.3" x2="303.1" y2="300.7" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="284.1" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="307.0" y1="272.8" x2="307.0" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="276.2" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="311.0" y1="279.1" x2="311.0" y2="303.7" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="287.3" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="314.9" y1="259.8" x2="314.9" y2="312.8" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="288.7" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="318.9" y1="258.6" x2="318.9" y2="291.7" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="263.8" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="322.8" y1="243.4" x2="322.8" y2="318.5" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="251.0" width="2.45" height="56.9" fill="var(--down)"/>
<line x1="326.8" y1="276.5" x2="326.8" y2="312.0" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="295.5" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="330.7" y1="288.5" x2="330.7" y2="326.9" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="290.9" width="2.45" height="24.3" fill="var(--down)"/>
<line x1="334.7" y1="309.5" x2="334.7" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="321.8" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="338.6" y1="297.7" x2="338.6" y2="326.5" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="321.3" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="342.6" y1="219.7" x2="342.6" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="226.5" width="2.45" height="79.6" fill="var(--up)"/>
<line x1="346.5" y1="186.6" x2="346.5" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="193.5" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="350.5" y1="188.2" x2="350.5" y2="211.9" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="189.8" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="354.4" y1="197.1" x2="354.4" y2="230.0" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="198.2" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="358.4" y1="194.1" x2="358.4" y2="225.8" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="218.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="362.3" y1="204.3" x2="362.3" y2="227.8" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="215.6" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="366.3" y1="189.6" x2="366.3" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="192.3" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="370.2" y1="164.4" x2="370.2" y2="197.1" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="178.9" width="2.45" height="13.4" fill="var(--up)"/>
<line x1="374.2" y1="155.6" x2="374.2" y2="178.7" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="176.4" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="378.2" y1="153.4" x2="378.2" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="164.4" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="382.1" y1="157.6" x2="382.1" y2="167.4" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="163.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="386.1" y1="154.6" x2="386.1" y2="172.3" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="163.8" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="390.0" y1="170.9" x2="390.0" y2="184.5" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="172.2" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="394.0" y1="170.1" x2="394.0" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="175.6" width="2.45" height="21.9" fill="var(--down)"/>
<line x1="397.9" y1="197.5" x2="397.9" y2="241.5" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="198.2" width="2.45" height="29.3" fill="var(--down)"/>
<line x1="401.9" y1="176.7" x2="401.9" y2="245.5" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="206.4" width="2.45" height="34.6" fill="var(--up)"/>
<line x1="405.8" y1="157.0" x2="405.8" y2="208.9" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="161.0" width="2.45" height="43.8" fill="var(--up)"/>
<line x1="409.8" y1="141.9" x2="409.8" y2="171.5" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="162.6" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="413.7" y1="124.9" x2="413.7" y2="187.4" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="162.0" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="417.7" y1="157.2" x2="417.7" y2="180.3" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="169.6" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="421.6" y1="209.1" x2="421.6" y2="255.4" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="215.3" width="2.45" height="8.7" fill="var(--up)"/>
<line x1="425.6" y1="243.6" x2="425.6" y2="341.2" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="243.6" width="2.45" height="53.9" fill="var(--down)"/>
<line x1="429.5" y1="283.7" x2="429.5" y2="324.0" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="290.5" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="433.5" y1="278.7" x2="433.5" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="283.9" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="437.4" y1="301.3" x2="437.4" y2="321.9" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="315.9" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="441.4" y1="330.7" x2="441.4" y2="361.2" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="348.8" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="445.3" y1="326.9" x2="445.3" y2="375.7" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="341.9" width="2.45" height="23.0" fill="var(--down)"/>
<line x1="449.3" y1="343.2" x2="449.3" y2="379.4" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="344.4" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="453.2" y1="347.2" x2="453.2" y2="393.5" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="350.0" width="2.45" height="25.8" fill="var(--down)"/>
<line x1="457.2" y1="354.0" x2="457.2" y2="383.9" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="365.7" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="461.1" y1="358.9" x2="461.1" y2="395.9" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="364.6" width="2.45" height="28.0" fill="var(--down)"/>
<line x1="465.1" y1="379.3" x2="465.1" y2="400.8" stroke="var(--down)" class="wick"/>
<rect x="463.87" y="386.6" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="469.1" y1="300.5" x2="469.1" y2="393.7" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="302.4" width="2.45" height="46.1" fill="var(--up)"/>
<line x1="473.0" y1="302.3" x2="473.0" y2="335.3" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="312.9" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="477.0" y1="250.7" x2="477.0" y2="313.2" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="257.5" width="2.45" height="55.6" fill="var(--up)"/>
<line x1="480.9" y1="239.1" x2="480.9" y2="282.0" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="261.5" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="484.9" y1="252.7" x2="484.9" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="264.6" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="488.8" y1="232.1" x2="488.8" y2="278.4" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="259.5" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="492.8" y1="252.0" x2="492.8" y2="317.6" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="266.3" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="496.7" y1="291.5" x2="496.7" y2="339.3" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="302.5" width="2.45" height="32.4" fill="var(--down)"/>
<line x1="500.7" y1="289.8" x2="500.7" y2="336.2" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="315.3" width="2.45" height="15.9" fill="var(--up)"/>
<line x1="504.6" y1="314.1" x2="504.6" y2="343.5" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="324.0" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="508.6" y1="305.3" x2="508.6" y2="366.5" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="317.1" width="2.45" height="48.2" fill="var(--down)"/>
<line x1="512.5" y1="340.1" x2="512.5" y2="409.5" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="359.1" width="2.45" height="41.3" fill="var(--down)"/>
<line x1="516.5" y1="371.5" x2="516.5" y2="413.5" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="386.7" width="2.45" height="26.8" fill="var(--up)"/>
<line x1="520.4" y1="352.6" x2="520.4" y2="396.5" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="363.3" width="2.45" height="21.2" fill="var(--up)"/>
<line x1="524.4" y1="368.9" x2="524.4" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="375.5" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="528.3" y1="365.2" x2="528.3" y2="399.6" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="369.4" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="532.3" y1="383.6" x2="532.3" y2="510.1" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="392.3" width="2.45" height="94.4" fill="var(--down)"/>
<line x1="536.2" y1="474.3" x2="536.2" y2="505.2" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="479.2" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="540.2" y1="430.7" x2="540.2" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="435.1" width="2.45" height="25.4" fill="var(--up)"/>
<line x1="544.1" y1="394.5" x2="544.1" y2="436.6" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="414.3" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="548.1" y1="398.9" x2="548.1" y2="445.3" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="404.9" width="2.45" height="29.9" fill="var(--up)"/>
<line x1="552.0" y1="370.3" x2="552.0" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="390.3" width="2.45" height="44.5" fill="var(--up)"/>
<line x1="556.0" y1="367.9" x2="556.0" y2="421.2" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="377.4" width="2.45" height="41.4" fill="var(--up)"/>
<line x1="560.0" y1="370.3" x2="560.0" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="378.1" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="563.9" y1="373.6" x2="563.9" y2="422.2" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="376.1" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="567.9" y1="384.3" x2="567.9" y2="424.3" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="385.1" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="571.8" y1="390.7" x2="571.8" y2="436.2" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="402.9" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="575.8" y1="396.7" x2="575.8" y2="428.9" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="405.9" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="579.7" y1="412.3" x2="579.7" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="420.9" width="2.45" height="35.1" fill="var(--down)"/>
<line x1="583.7" y1="449.7" x2="583.7" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="471.4" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="587.6" y1="464.2" x2="587.6" y2="489.2" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="479.2" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="591.6" y1="438.3" x2="591.6" y2="476.8" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="438.6" width="2.45" height="38.2" fill="var(--up)"/>
<line x1="595.5" y1="405.9" x2="595.5" y2="446.3" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="430.7" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="599.5" y1="456.9" x2="599.5" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="456.9" width="2.45" height="59.0" fill="var(--down)"/>
<line x1="603.4" y1="482.7" x2="603.4" y2="520.5" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="505.7" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="607.4" y1="474.4" x2="607.4" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="606.15" y="485.6" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="611.3" y1="444.2" x2="611.3" y2="470.0" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="448.0" width="2.45" height="21.9" fill="var(--down)"/>
<line x1="615.3" y1="460.9" x2="615.3" y2="497.5" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="475.6" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="619.2" y1="447.3" x2="619.2" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="460.8" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="623.2" y1="452.9" x2="623.2" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="468.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="627.1" y1="471.2" x2="627.1" y2="546.8" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="473.5" width="2.45" height="58.8" fill="var(--down)"/>
<line x1="631.1" y1="488.7" x2="631.1" y2="521.7" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="494.6" width="2.45" height="23.1" fill="var(--up)"/>
<line x1="635.0" y1="466.0" x2="635.0" y2="507.8" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="471.4" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="639.0" y1="459.8" x2="639.0" y2="526.9" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="462.8" width="2.45" height="40.9" fill="var(--down)"/>
<line x1="642.9" y1="471.9" x2="642.9" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="641.72" y="496.8" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="646.9" y1="464.0" x2="646.9" y2="505.5" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="465.6" width="2.45" height="29.9" fill="var(--up)"/>
<line x1="650.9" y1="461.4" x2="650.9" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="478.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="654.8" y1="425.7" x2="654.8" y2="448.8" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="440.5" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="658.8" y1="445.6" x2="658.8" y2="480.1" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="454.2" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="662.7" y1="454.5" x2="662.7" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="463.7" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="666.7" y1="437.1" x2="666.7" y2="490.7" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="438.3" width="2.45" height="47.7" fill="var(--up)"/>
<line x1="670.6" y1="417.4" x2="670.6" y2="445.6" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="420.6" width="2.45" height="19.9" fill="var(--up)"/>
<line x1="674.6" y1="384.7" x2="674.6" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="394.3" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="678.5" y1="385.5" x2="678.5" y2="405.7" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="399.8" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="682.5" y1="365.3" x2="682.5" y2="399.0" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="388.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="686.4" y1="376.8" x2="686.4" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="685.20" y="391.2" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="690.4" y1="382.1" x2="690.4" y2="432.1" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="406.0" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="694.3" y1="418.1" x2="694.3" y2="449.3" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="424.8" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="698.3" y1="434.1" x2="698.3" y2="477.7" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="442.9" width="2.45" height="19.3" fill="var(--down)"/>
<line x1="702.2" y1="449.7" x2="702.2" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="455.3" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="706.2" y1="436.5" x2="706.2" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="446.6" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="710.1" y1="405.7" x2="710.1" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="708.91" y="424.1" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="714.1" y1="339.2" x2="714.1" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="355.5" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="718.0" y1="416.7" x2="718.0" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="454.0" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="722.0" y1="436.6" x2="722.0" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="448.2" width="2.45" height="40.7" fill="var(--down)"/>
<line x1="725.9" y1="443.3" x2="725.9" y2="495.1" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="453.1" width="2.45" height="37.6" fill="var(--up)"/>
<line x1="729.9" y1="456.4" x2="729.9" y2="497.5" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="467.4" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="733.8" y1="468.6" x2="733.8" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="474.7" width="2.45" height="28.0" fill="var(--down)"/>
<line x1="737.8" y1="457.8" x2="737.8" y2="499.6" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="467.8" width="2.45" height="31.8" fill="var(--up)"/>
<line x1="741.8" y1="469.8" x2="741.8" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="470.9" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="745.7" y1="465.0" x2="745.7" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="479.9" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="749.7" y1="447.0" x2="749.7" y2="472.4" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="469.1" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="753.6" y1="476.8" x2="753.6" y2="508.8" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="488.4" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="757.6" y1="492.7" x2="757.6" y2="517.8" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="505.1" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="761.5" y1="462.6" x2="761.5" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="493.8" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="765.5" y1="447.3" x2="765.5" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="449.0" width="2.45" height="55.3" fill="var(--up)"/>
<line x1="769.4" y1="421.6" x2="769.4" y2="477.2" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="442.2" width="2.45" height="30.4" fill="var(--down)"/>
<line x1="773.4" y1="472.6" x2="773.4" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="479.0" width="2.45" height="17.5" fill="var(--up)"/>
<line x1="777.3" y1="466.1" x2="777.3" y2="509.8" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="472.9" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="781.3" y1="455.0" x2="781.3" y2="481.8" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="474.9" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="785.2" y1="483.6" x2="785.2" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="486.9" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="789.2" y1="473.9" x2="789.2" y2="500.4" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="490.6" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="793.1" y1="492.4" x2="793.1" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="495.6" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="797.1" y1="471.0" x2="797.1" y2="499.1" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="492.7" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="801.0" y1="482.5" x2="801.0" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="489.8" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="805.0" y1="494.6" x2="805.0" y2="557.7" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="498.2" width="2.45" height="59.4" fill="var(--down)"/>
<line x1="808.9" y1="541.1" x2="808.9" y2="608.5" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="559.0" width="2.45" height="22.4" fill="var(--down)"/>
<line x1="812.9" y1="515.7" x2="812.9" y2="558.5" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="541.9" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="816.8" y1="494.6" x2="816.8" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="505.9" width="2.45" height="27.4" fill="var(--up)"/>
<line x1="820.8" y1="511.9" x2="820.8" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="819.57" y="522.6" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="824.7" y1="489.1" x2="824.7" y2="541.0" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="489.8" width="2.45" height="43.9" fill="var(--up)"/>
<line x1="828.7" y1="476.1" x2="828.7" y2="523.6" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="481.2" width="2.45" height="32.4" fill="var(--down)"/>
<line x1="832.7" y1="504.4" x2="832.7" y2="531.7" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="515.2" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="836.6" y1="500.9" x2="836.6" y2="531.2" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="510.1" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="840.6" y1="496.3" x2="840.6" y2="523.0" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="507.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="844.5" y1="465.6" x2="844.5" y2="512.0" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="466.3" width="2.45" height="36.6" fill="var(--up)"/>
<line x1="848.5" y1="453.5" x2="848.5" y2="500.8" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="460.1" width="2.45" height="38.4" fill="var(--down)"/>
<line x1="852.4" y1="486.9" x2="852.4" y2="514.3" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="491.6" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="856.4" y1="488.2" x2="856.4" y2="536.6" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="517.2" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="860.3" y1="504.0" x2="860.3" y2="531.6" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="514.6" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="864.3" y1="477.5" x2="864.3" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="493.0" width="2.45" height="24.5" fill="var(--up)"/>
<line x1="868.2" y1="452.9" x2="868.2" y2="515.3" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="486.9" width="2.45" height="27.4" fill="var(--down)"/>
<line x1="872.2" y1="454.6" x2="872.2" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="475.2" width="2.45" height="40.3" fill="var(--up)"/>
<line x1="876.1" y1="411.7" x2="876.1" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="434.2" width="2.45" height="27.6" fill="var(--up)"/>
<line x1="880.1" y1="417.3" x2="880.1" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="418.9" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="884.0" y1="353.9" x2="884.0" y2="419.6" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="384.7" width="2.45" height="20.1" fill="var(--up)"/>
<line x1="888.0" y1="318.3" x2="888.0" y2="370.7" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="319.2" width="2.45" height="37.3" fill="var(--up)"/>
<line x1="891.9" y1="309.5" x2="891.9" y2="383.8" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="314.0" width="2.45" height="29.5" fill="var(--down)"/>
<line x1="895.9" y1="302.7" x2="895.9" y2="355.5" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="340.7" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="899.8" y1="349.2" x2="899.8" y2="404.9" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="351.2" width="2.45" height="43.5" fill="var(--down)"/>
<line x1="903.8" y1="381.7" x2="903.8" y2="413.0" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="381.8" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="907.7" y1="359.6" x2="907.7" y2="395.5" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="366.1" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="911.7" y1="317.1" x2="911.7" y2="352.7" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="325.7" width="2.45" height="27.0" fill="var(--up)"/>
<line x1="915.6" y1="303.5" x2="915.6" y2="347.5" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="324.5" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="919.6" y1="312.1" x2="919.6" y2="359.0" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="322.5" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="923.6" y1="271.7" x2="923.6" y2="318.0" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="272.3" width="2.45" height="38.8" fill="var(--up)"/>
<line x1="927.5" y1="271.6" x2="927.5" y2="316.0" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="276.3" width="2.45" height="26.7" fill="var(--down)"/>
<line x1="931.5" y1="286.3" x2="931.5" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="288.1" width="2.45" height="28.8" fill="var(--up)"/>
<line x1="935.4" y1="300.1" x2="935.4" y2="329.0" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="302.3" width="2.45" height="21.1" fill="var(--down)"/>
<line x1="939.4" y1="316.8" x2="939.4" y2="352.7" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="320.9" width="2.45" height="26.9" fill="var(--down)"/>
<line x1="943.3" y1="352.1" x2="943.3" y2="380.2" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="354.4" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="947.3" y1="316.8" x2="947.3" y2="356.7" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="318.2" width="2.45" height="31.7" fill="var(--up)"/>
<line x1="951.2" y1="263.2" x2="951.2" y2="309.0" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="271.6" width="2.45" height="33.0" fill="var(--up)"/>
<line x1="955.2" y1="221.7" x2="955.2" y2="249.5" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="228.9" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="959.1" y1="201.0" x2="959.1" y2="259.2" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="226.7" width="2.45" height="31.9" fill="var(--up)"/>
<line x1="963.1" y1="152.1" x2="963.1" y2="210.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="172.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="967.0" y1="180.0" x2="967.0" y2="226.3" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="188.9" width="2.45" height="20.9" fill="var(--up)"/>
<line x1="971.0" y1="147.9" x2="971.0" y2="197.9" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="162.3" width="2.45" height="34.9" fill="var(--down)"/>
<line x1="974.9" y1="188.0" x2="974.9" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="196.7" width="2.45" height="15.9" fill="var(--up)"/>
<line x1="978.9" y1="169.0" x2="978.9" y2="206.3" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="178.7" width="2.45" height="20.3" fill="var(--down)"/>
<line x1="982.8" y1="176.3" x2="982.8" y2="214.9" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="177.9" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="986.8" y1="189.4" x2="986.8" y2="233.3" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="191.0" width="2.45" height="37.2" fill="var(--down)"/>
<line x1="990.7" y1="213.4" x2="990.7" y2="242.0" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="227.3" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="994.7" y1="210.1" x2="994.7" y2="239.6" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="229.1" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="998.6" y1="225.8" x2="998.6" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="240.6" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="1002.6" y1="207.6" x2="1002.6" y2="248.4" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="212.4" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="1006.5" y1="198.3" x2="1006.5" y2="222.4" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="203.7" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="1010.5" y1="203.7" x2="1010.5" y2="234.7" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="219.3" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="1014.5" y1="168.1" x2="1014.5" y2="227.3" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="184.3" width="2.45" height="40.3" fill="var(--up)"/>
<line x1="1018.4" y1="150.9" x2="1018.4" y2="199.6" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="186.5" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="1022.4" y1="163.8" x2="1022.4" y2="194.0" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="186.0" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="1026.3" y1="153.5" x2="1026.3" y2="189.2" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="159.8" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="1030.3" y1="85.0" x2="1030.3" y2="146.0" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="85.5" width="2.45" height="57.4" fill="var(--up)"/>
<line x1="1034.2" y1="80.2" x2="1034.2" y2="103.0" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="87.4" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="1038.2" y1="83.1" x2="1038.2" y2="105.4" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="87.4" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="1042.1" y1="108.1" x2="1042.1" y2="130.9" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="109.1" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="1046.1" y1="103.6" x2="1046.1" y2="129.9" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="109.9" width="2.45" height="16.3" fill="var(--down)"/>
<line x1="1050.0" y1="113.4" x2="1050.0" y2="158.9" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="125.0" width="2.45" height="33.0" fill="var(--down)"/>
<line x1="60" y1="227.2" x2="1052" y2="227.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="221.2" font-size="11.5" fill="var(--support)" font-weight="600">$563 S1</text>
<text x="1058" y="233.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="312.1" x2="1052" y2="312.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="306.1" font-size="11.5" fill="var(--support)" font-weight="600">$541 S2</text>
<text x="1058" y="318.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="385.7" x2="1052" y2="385.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="379.7" font-size="11.5" fill="var(--support)" font-weight="600">$522 S3</text>
<text x="1058" y="391.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="158.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="150.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $581 (2026-09-01)</text>
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
| **현재가** | **$581.10** (2026-09-01 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $563 | 3 | 2025-09-10·2025-09-29·2026-08-12 저점대. 현재가에 가장 근접한 지지로, 최근 신고가 랠리의 출발점이기도 하다 |
| S2 | $541 | 3 | 2025-10-16·2025-11-03·2025-12-09 저점대. 2025년 4분기 내내 눌린 구간 |
| S3 | $522 | 3 | 2025-11-18·2026-01-28·2026-07-23 저점대. 1년 중 세 차례 다른 국면에서 반복 확인된 가장 두꺼운 지지 |
| 참고선 | $464.52 | — | 최근 1년 최저가. 현재가에서 20% 아래라 근시일 지지로 보지 않는다 |

> **저항 레벨이 하나도 없다.** 2026-09-01 종가 $581.10이 최근 1년 최고가($601.62) 부근이라 위쪽에 스윙 고점 클러스터가 만들어지지 않았다 — 레벨 개수를 3개로 채우지 않고 지지 3개만 둔 이유다.

---

## 3. 관측된 특이 구간 — 2026-07-30 2분기 실적 발표

- [2026년 2분기 실적](./08_news.md) 발표(순매출 +14%, 조정 EPS +21%, 영업이익률 60.2%)를 기점으로 주가가 $520~$560 박스를 벗어나 신고가 구간으로 올라섰다.
- 그 직전 스윙 저점이 2026-07-23의 S3($522) 부근이었고, 8월 중순 조정에서도 S1($563)에서 멈춰 **직전 박스 상단이 지지로 바뀌는 전형적 전환**이 관측된다(2026-08-12 스윙 저점).
- **다만 개별 발표일의 종가 변동폭·거래량은 이 차트 데이터로 확인하지 않았다** — 갭 크기와 거래량 배수는 기재하지 않는다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-02~2026-09-01. 수집 시점: 2026-09-02. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py MA --name Mastercard --close-on 2026-09-01 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 기간 내 배당이 4회 지급됐으나 **원주가(배당 미반영)** 기준이라 실제 총수익률과는 다르다.
    - 현재가가 1년 최고가 부근이라 **위쪽 레벨이 없다는 것은 저항이 없다는 뜻이 아니라 표본이 없다는 뜻**이다. 다년 구조는 주봉 문서를 함께 볼 것.
    - 기간 내 주식분할·대규모 유상증자는 없었다.

---

*작성일: 2026-09-02*
