# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 이 차트의 마지막 봉은 **2026-08-27 종가 $347.55**인데, [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 기준일은 **2026-08-28 종가 $340.39**다. **수정주가 차이가 아니라 수집 시점(2026-08-29)에 제공처가 2026-08-28 일봉을 아직 확정하지 않았기 때문**이며, 같은 제공처의 주봉 시계열과 정규장 마감 시세에는 2026-08-28 종가 $340.39가 들어 있다([기술적 분석 — 주봉·5년](./10_technical_weekly.md)이 그 값을 쓴다). 따라서 아래 2. 지지선 / 저항선 요약의 "현재가"는 다른 문서보다 **하루 앞선 시점**이고, 하루 뒤 종가는 그보다 **2.06% 낮다**.
    - 이 기간에 주식분할·병합은 없었고 배당도 없다([핵심 지표](./04_metrics.md) A.4 — DPS 전 기간 $0). 따라서 원주가와 수정주가가 같다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

<div class="cdns-chart">
<style>
.cdns-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .cdns-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .cdns-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.cdns-chart svg { width:100%; height:auto; display:block; }
.cdns-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.cdns-chart .title { fill: var(--ink); font-weight:600; }
.cdns-chart .grid { stroke: var(--grid); stroke-width:1; }
.cdns-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cadence Design Systems(CDNS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Cadence Design Systems (CDNS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $347.55 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="565.5" x2="1052" y2="565.5" class="grid"/>
<text x="52" y="569.5" font-size="11" text-anchor="end" fill="var(--muted)">275</text>
<line x1="60" y1="479.2" x2="1052" y2="479.2" class="grid"/>
<text x="52" y="483.2" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="392.8" x2="1052" y2="392.8" class="grid"/>
<text x="52" y="396.8" font-size="11" text-anchor="end" fill="var(--muted)">325</text>
<line x1="60" y1="306.5" x2="1052" y2="306.5" class="grid"/>
<text x="52" y="310.5" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="220.1" x2="1052" y2="220.1" class="grid"/>
<text x="52" y="224.1" font-size="11" text-anchor="end" fill="var(--muted)">375</text>
<line x1="60" y1="133.7" x2="1052" y2="133.7" class="grid"/>
<text x="52" y="137.7" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="66.0" y1="626.0" x2="66.0" y2="631.0" class="axis"/>
<text x="66.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="149.3" y1="626.0" x2="149.3" y2="631.0" class="axis"/>
<text x="149.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="240.5" y1="626.0" x2="240.5" y2="631.0" class="axis"/>
<text x="240.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="315.9" y1="626.0" x2="315.9" y2="631.0" class="axis"/>
<text x="315.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="403.2" y1="626.0" x2="403.2" y2="631.0" class="axis"/>
<text x="403.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="482.6" y1="626.0" x2="482.6" y2="631.0" class="axis"/>
<text x="482.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="558.0" y1="626.0" x2="558.0" y2="631.0" class="axis"/>
<text x="558.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="645.3" y1="626.0" x2="645.3" y2="631.0" class="axis"/>
<text x="645.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="728.6" y1="626.0" x2="728.6" y2="631.0" class="axis"/>
<text x="728.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="808.0" y1="626.0" x2="808.0" y2="631.0" class="axis"/>
<text x="808.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="891.3" y1="626.0" x2="891.3" y2="631.0" class="axis"/>
<text x="891.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="978.6" y1="626.0" x2="978.6" y2="631.0" class="axis"/>
<text x="978.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="76.1" x2="1052" y2="76.1" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="79.1" font-size="10.5" fill="var(--muted)">$417 52주 최고</text>
<line x1="808.0" y1="56.0" x2="808.0" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="814.0" y="68.0" font-size="10.5" fill="var(--down)">2026-06-01 Computex ChipStack 발표 급등</text>
<line x1="934.9" y1="56.0" x2="934.9" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="940.9" y="68.0" font-size="10.5" fill="var(--down)">2026-07-17 AI 서사發 급락</text>
<line x1="62.0" y1="288.4" x2="62.0" y2="319.6" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="294.0" width="2.46" height="11.0" fill="var(--down)"/>
<line x1="66.0" y1="317.3" x2="66.0" y2="338.7" stroke="var(--down)" class="wick"/>
<rect x="64.72" y="327.4" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="69.9" y1="315.3" x2="69.9" y2="339.0" stroke="var(--up)" class="wick"/>
<rect x="68.69" y="315.7" width="2.46" height="22.2" fill="var(--up)"/>
<line x1="73.9" y1="306.0" x2="73.9" y2="325.7" stroke="var(--up)" class="wick"/>
<rect x="72.66" y="308.8" width="2.46" height="8.3" fill="var(--up)"/>
<line x1="77.9" y1="288.1" x2="77.9" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="76.63" y="296.0" width="2.46" height="7.0" fill="var(--down)"/>
<line x1="81.8" y1="267.2" x2="81.8" y2="296.1" stroke="var(--up)" class="wick"/>
<rect x="80.59" y="269.7" width="2.46" height="24.1" fill="var(--up)"/>
<line x1="85.8" y1="262.5" x2="85.8" y2="284.3" stroke="var(--down)" class="wick"/>
<rect x="84.56" y="265.0" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="89.8" y1="311.5" x2="89.8" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="88.53" y="311.6" width="2.46" height="34.4" fill="var(--down)"/>
<line x1="93.7" y1="279.6" x2="93.7" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="290.2" width="2.46" height="42.6" fill="var(--up)"/>
<line x1="97.7" y1="288.9" x2="97.7" y2="333.8" stroke="var(--down)" class="wick"/>
<rect x="96.47" y="294.5" width="2.46" height="34.5" fill="var(--down)"/>
<line x1="101.7" y1="299.5" x2="101.7" y2="333.2" stroke="var(--up)" class="wick"/>
<rect x="100.43" y="301.2" width="2.46" height="28.8" fill="var(--up)"/>
<line x1="105.6" y1="297.6" x2="105.6" y2="313.5" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="305.9" width="2.46" height="4.0" fill="var(--down)"/>
<line x1="109.6" y1="306.9" x2="109.6" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="108.37" y="306.9" width="2.46" height="9.0" fill="var(--down)"/>
<line x1="113.6" y1="251.0" x2="113.6" y2="284.2" stroke="var(--up)" class="wick"/>
<rect x="112.34" y="255.1" width="2.46" height="18.6" fill="var(--up)"/>
<line x1="117.5" y1="222.5" x2="117.5" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="116.31" y="225.8" width="2.46" height="21.0" fill="var(--up)"/>
<line x1="121.5" y1="223.9" x2="121.5" y2="255.7" stroke="var(--up)" class="wick"/>
<rect x="120.27" y="225.7" width="2.46" height="11.6" fill="var(--up)"/>
<line x1="125.5" y1="231.0" x2="125.5" y2="258.2" stroke="var(--down)" class="wick"/>
<rect x="124.24" y="234.0" width="2.46" height="16.2" fill="var(--down)"/>
<line x1="129.4" y1="248.7" x2="129.4" y2="286.4" stroke="var(--down)" class="wick"/>
<rect x="128.21" y="248.7" width="2.46" height="33.7" fill="var(--down)"/>
<line x1="133.4" y1="289.1" x2="133.4" y2="306.4" stroke="var(--down)" class="wick"/>
<rect x="132.18" y="297.7" width="2.46" height="5.0" fill="var(--down)"/>
<line x1="137.4" y1="302.7" x2="137.4" y2="316.9" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="306.1" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="141.3" y1="296.5" x2="141.3" y2="314.0" stroke="var(--down)" class="wick"/>
<rect x="140.11" y="296.5" width="2.46" height="15.1" fill="var(--down)"/>
<line x1="145.3" y1="299.4" x2="145.3" y2="317.1" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="302.1" width="2.46" height="7.1" fill="var(--up)"/>
<line x1="149.3" y1="288.7" x2="149.3" y2="315.4" stroke="var(--up)" class="wick"/>
<rect x="148.05" y="299.6" width="2.46" height="12.8" fill="var(--up)"/>
<line x1="153.2" y1="288.7" x2="153.2" y2="319.1" stroke="var(--down)" class="wick"/>
<rect x="152.02" y="290.7" width="2.46" height="25.3" fill="var(--down)"/>
<line x1="157.2" y1="295.6" x2="157.2" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="155.99" y="315.9" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="161.2" y1="289.7" x2="161.2" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="159.95" y="294.8" width="2.46" height="11.6" fill="var(--up)"/>
<line x1="165.2" y1="295.0" x2="165.2" y2="333.8" stroke="var(--down)" class="wick"/>
<rect x="163.92" y="297.1" width="2.46" height="24.9" fill="var(--down)"/>
<line x1="169.1" y1="291.7" x2="169.1" y2="320.0" stroke="var(--up)" class="wick"/>
<rect x="167.89" y="306.5" width="2.46" height="13.6" fill="var(--up)"/>
<line x1="173.1" y1="310.7" x2="173.1" y2="328.6" stroke="var(--up)" class="wick"/>
<rect x="171.86" y="311.0" width="2.46" height="1.5" fill="var(--up)"/>
<line x1="177.1" y1="305.6" x2="177.1" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="175.83" y="313.0" width="2.46" height="72.9" fill="var(--down)"/>
<line x1="181.0" y1="361.0" x2="181.0" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="367.8" width="2.46" height="8.6" fill="var(--up)"/>
<line x1="185.0" y1="376.1" x2="185.0" y2="416.9" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="390.2" width="2.46" height="4.3" fill="var(--up)"/>
<line x1="189.0" y1="373.3" x2="189.0" y2="405.3" stroke="var(--down)" class="wick"/>
<rect x="187.73" y="373.3" width="2.46" height="22.6" fill="var(--down)"/>
<line x1="192.9" y1="385.7" x2="192.9" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="191.70" y="388.7" width="2.46" height="6.7" fill="var(--down)"/>
<line x1="196.9" y1="381.7" x2="196.9" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="195.67" y="388.9" width="2.46" height="12.2" fill="var(--up)"/>
<line x1="200.9" y1="371.7" x2="200.9" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="199.63" y="376.8" width="2.46" height="6.4" fill="var(--up)"/>
<line x1="204.8" y1="357.9" x2="204.8" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="203.60" y="363.6" width="2.46" height="20.5" fill="var(--up)"/>
<line x1="208.8" y1="353.1" x2="208.8" y2="388.8" stroke="var(--down)" class="wick"/>
<rect x="207.57" y="363.7" width="2.46" height="10.1" fill="var(--down)"/>
<line x1="212.8" y1="347.3" x2="212.8" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="211.54" y="350.4" width="2.46" height="27.5" fill="var(--up)"/>
<line x1="216.7" y1="302.6" x2="216.7" y2="341.8" stroke="var(--up)" class="wick"/>
<rect x="215.51" y="323.4" width="2.46" height="18.4" fill="var(--up)"/>
<line x1="220.7" y1="280.4" x2="220.7" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="219.47" y="280.4" width="2.46" height="21.2" fill="var(--down)"/>
<line x1="224.7" y1="313.1" x2="224.7" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="223.44" y="336.5" width="2.46" height="7.9" fill="var(--up)"/>
<line x1="228.6" y1="316.8" x2="228.6" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="227.41" y="336.1" width="2.46" height="14.3" fill="var(--up)"/>
<line x1="232.6" y1="333.4" x2="232.6" y2="363.8" stroke="var(--down)" class="wick"/>
<rect x="231.38" y="341.0" width="2.46" height="13.5" fill="var(--down)"/>
<line x1="236.6" y1="338.5" x2="236.6" y2="354.1" stroke="var(--down)" class="wick"/>
<rect x="235.35" y="345.4" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="240.5" y1="335.1" x2="240.5" y2="372.1" stroke="var(--down)" class="wick"/>
<rect x="239.31" y="335.1" width="2.46" height="21.8" fill="var(--down)"/>
<line x1="244.5" y1="354.6" x2="244.5" y2="390.8" stroke="var(--up)" class="wick"/>
<rect x="243.28" y="364.4" width="2.46" height="10.9" fill="var(--up)"/>
<line x1="248.5" y1="366.7" x2="248.5" y2="395.5" stroke="var(--down)" class="wick"/>
<rect x="247.25" y="368.8" width="2.46" height="14.9" fill="var(--down)"/>
<line x1="252.4" y1="385.0" x2="252.4" y2="415.0" stroke="var(--down)" class="wick"/>
<rect x="251.22" y="393.0" width="2.46" height="1.7" fill="var(--down)"/>
<line x1="256.4" y1="387.3" x2="256.4" y2="412.9" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="392.6" width="2.46" height="1.9" fill="var(--up)"/>
<line x1="260.4" y1="372.6" x2="260.4" y2="398.6" stroke="var(--up)" class="wick"/>
<rect x="259.15" y="379.2" width="2.46" height="8.2" fill="var(--up)"/>
<line x1="264.4" y1="386.6" x2="264.4" y2="423.1" stroke="var(--down)" class="wick"/>
<rect x="263.12" y="387.5" width="2.46" height="27.7" fill="var(--down)"/>
<line x1="268.3" y1="404.5" x2="268.3" y2="428.2" stroke="var(--down)" class="wick"/>
<rect x="267.09" y="406.9" width="2.46" height="18.6" fill="var(--down)"/>
<line x1="272.3" y1="418.8" x2="272.3" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="271.06" y="423.9" width="2.46" height="3.8" fill="var(--up)"/>
<line x1="276.3" y1="411.3" x2="276.3" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="275.03" y="427.6" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="280.2" y1="424.5" x2="280.2" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="432.4" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="284.2" y1="443.5" x2="284.2" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="282.96" y="452.5" width="2.46" height="15.6" fill="var(--down)"/>
<line x1="288.2" y1="444.2" x2="288.2" y2="470.8" stroke="var(--up)" class="wick"/>
<rect x="286.93" y="455.8" width="2.46" height="8.8" fill="var(--up)"/>
<line x1="292.1" y1="421.5" x2="292.1" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="290.90" y="437.2" width="2.46" height="34.6" fill="var(--down)"/>
<line x1="296.1" y1="465.7" x2="296.1" y2="495.8" stroke="var(--down)" class="wick"/>
<rect x="294.87" y="472.5" width="2.46" height="4.6" fill="var(--down)"/>
<line x1="300.1" y1="459.4" x2="300.1" y2="480.4" stroke="var(--up)" class="wick"/>
<rect x="298.83" y="463.7" width="2.46" height="3.8" fill="var(--up)"/>
<line x1="304.0" y1="459.3" x2="304.0" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="302.80" y="466.5" width="2.46" height="10.1" fill="var(--up)"/>
<line x1="308.0" y1="450.9" x2="308.0" y2="465.3" stroke="var(--down)" class="wick"/>
<rect x="306.77" y="454.8" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="312.0" y1="437.9" x2="312.0" y2="457.3" stroke="var(--up)" class="wick"/>
<rect x="310.74" y="438.3" width="2.46" height="9.6" fill="var(--up)"/>
<line x1="315.9" y1="434.1" x2="315.9" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="314.71" y="435.5" width="2.46" height="10.4" fill="var(--down)"/>
<line x1="319.9" y1="413.3" x2="319.9" y2="440.4" stroke="var(--up)" class="wick"/>
<rect x="318.67" y="417.2" width="2.46" height="22.2" fill="var(--up)"/>
<line x1="323.9" y1="347.9" x2="323.9" y2="425.0" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="354.4" width="2.46" height="70.2" fill="var(--up)"/>
<line x1="327.8" y1="342.4" x2="327.8" y2="360.6" stroke="var(--up)" class="wick"/>
<rect x="326.61" y="350.3" width="2.46" height="1.5" fill="var(--up)"/>
<line x1="331.8" y1="337.4" x2="331.8" y2="354.3" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="346.4" width="2.46" height="3.1" fill="var(--down)"/>
<line x1="335.8" y1="338.1" x2="335.8" y2="353.0" stroke="var(--down)" class="wick"/>
<rect x="334.55" y="347.9" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="339.7" y1="347.8" x2="339.7" y2="363.6" stroke="var(--down)" class="wick"/>
<rect x="338.51" y="353.9" width="2.46" height="4.1" fill="var(--down)"/>
<line x1="343.7" y1="336.5" x2="343.7" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="342.48" y="347.7" width="2.46" height="12.5" fill="var(--up)"/>
<line x1="347.7" y1="347.9" x2="347.7" y2="377.8" stroke="var(--down)" class="wick"/>
<rect x="346.45" y="348.1" width="2.46" height="8.7" fill="var(--down)"/>
<line x1="351.6" y1="357.4" x2="351.6" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="350.42" y="359.6" width="2.46" height="39.4" fill="var(--down)"/>
<line x1="355.6" y1="383.2" x2="355.6" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="354.39" y="396.0" width="2.46" height="19.5" fill="var(--down)"/>
<line x1="359.6" y1="399.7" x2="359.6" y2="422.5" stroke="var(--up)" class="wick"/>
<rect x="358.35" y="411.7" width="2.46" height="3.4" fill="var(--up)"/>
<line x1="363.6" y1="410.5" x2="363.6" y2="441.4" stroke="var(--down)" class="wick"/>
<rect x="362.32" y="413.5" width="2.46" height="20.7" fill="var(--down)"/>
<line x1="367.5" y1="401.8" x2="367.5" y2="429.6" stroke="var(--down)" class="wick"/>
<rect x="366.29" y="415.7" width="2.46" height="11.4" fill="var(--down)"/>
<line x1="371.5" y1="412.6" x2="371.5" y2="431.6" stroke="var(--down)" class="wick"/>
<rect x="370.26" y="427.0" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="375.5" y1="415.8" x2="375.5" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="374.23" y="418.5" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="379.4" y1="419.1" x2="379.4" y2="429.0" stroke="var(--up)" class="wick"/>
<rect x="378.19" y="420.7" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="383.4" y1="416.6" x2="383.4" y2="426.1" stroke="var(--up)" class="wick"/>
<rect x="382.16" y="417.8" width="2.46" height="7.1" fill="var(--up)"/>
<line x1="387.4" y1="412.5" x2="387.4" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="386.13" y="413.9" width="2.46" height="3.1" fill="var(--up)"/>
<line x1="391.3" y1="404.3" x2="391.3" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="390.10" y="417.5" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="395.3" y1="413.5" x2="395.3" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="394.07" y="421.0" width="2.46" height="4.2" fill="var(--down)"/>
<line x1="399.3" y1="423.9" x2="399.3" y2="437.5" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="424.7" width="2.46" height="11.1" fill="var(--down)"/>
<line x1="403.2" y1="423.9" x2="403.2" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="402.00" y="424.9" width="2.46" height="18.3" fill="var(--down)"/>
<line x1="407.2" y1="430.2" x2="407.2" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="405.97" y="439.6" width="2.46" height="35.4" fill="var(--down)"/>
<line x1="411.2" y1="423.8" x2="411.2" y2="476.1" stroke="var(--up)" class="wick"/>
<rect x="409.94" y="428.6" width="2.46" height="45.4" fill="var(--up)"/>
<line x1="415.1" y1="393.8" x2="415.1" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="413.91" y="408.2" width="2.46" height="21.2" fill="var(--up)"/>
<line x1="419.1" y1="412.0" x2="419.1" y2="434.4" stroke="var(--up)" class="wick"/>
<rect x="417.87" y="414.2" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="423.1" y1="380.4" x2="423.1" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="384.8" width="2.46" height="25.6" fill="var(--up)"/>
<line x1="427.0" y1="380.7" x2="427.0" y2="406.6" stroke="var(--down)" class="wick"/>
<rect x="425.81" y="389.8" width="2.46" height="1.3" fill="var(--down)"/>
<line x1="431.0" y1="383.6" x2="431.0" y2="417.0" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="399.5" width="2.46" height="1.5" fill="var(--up)"/>
<line x1="435.0" y1="408.3" x2="435.0" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="433.75" y="411.8" width="2.46" height="21.9" fill="var(--down)"/>
<line x1="438.9" y1="380.2" x2="438.9" y2="423.9" stroke="var(--up)" class="wick"/>
<rect x="437.71" y="408.0" width="2.46" height="10.9" fill="var(--up)"/>
<line x1="442.9" y1="401.6" x2="442.9" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="441.68" y="403.8" width="2.46" height="15.1" fill="var(--down)"/>
<line x1="446.9" y1="439.6" x2="446.9" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="445.65" y="442.7" width="2.46" height="12.3" fill="var(--down)"/>
<line x1="450.8" y1="423.4" x2="450.8" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="449.62" y="431.4" width="2.46" height="21.8" fill="var(--up)"/>
<line x1="454.8" y1="417.6" x2="454.8" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="453.59" y="420.1" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="458.8" y1="397.9" x2="458.8" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="457.55" y="415.9" width="2.46" height="9.7" fill="var(--up)"/>
<line x1="462.8" y1="397.6" x2="462.8" y2="430.6" stroke="var(--up)" class="wick"/>
<rect x="461.52" y="403.1" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="466.7" y1="399.7" x2="466.7" y2="419.7" stroke="var(--down)" class="wick"/>
<rect x="465.49" y="404.2" width="2.46" height="11.5" fill="var(--down)"/>
<line x1="470.7" y1="392.2" x2="470.7" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="469.46" y="404.5" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="474.7" y1="420.5" x2="474.7" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="473.43" y="421.8" width="2.46" height="48.2" fill="var(--down)"/>
<line x1="478.6" y1="483.1" x2="478.6" y2="501.2" stroke="var(--down)" class="wick"/>
<rect x="477.39" y="484.5" width="2.46" height="7.3" fill="var(--down)"/>
<line x1="482.6" y1="491.8" x2="482.6" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="481.36" y="496.1" width="2.46" height="20.4" fill="var(--down)"/>
<line x1="486.6" y1="527.6" x2="486.6" y2="607.9" stroke="var(--down)" class="wick"/>
<rect x="485.33" y="535.0" width="2.46" height="53.0" fill="var(--down)"/>
<line x1="490.5" y1="564.5" x2="490.5" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="489.30" y="577.9" width="2.46" height="5.4" fill="var(--up)"/>
<line x1="494.5" y1="560.7" x2="494.5" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="493.27" y="577.0" width="2.46" height="5.3" fill="var(--down)"/>
<line x1="498.5" y1="529.8" x2="498.5" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="536.1" width="2.46" height="25.4" fill="var(--up)"/>
<line x1="502.4" y1="507.6" x2="502.4" y2="549.8" stroke="var(--up)" class="wick"/>
<rect x="501.20" y="510.3" width="2.46" height="25.9" fill="var(--up)"/>
<line x1="506.4" y1="475.5" x2="506.4" y2="503.4" stroke="var(--up)" class="wick"/>
<rect x="505.17" y="482.6" width="2.46" height="16.7" fill="var(--up)"/>
<line x1="510.4" y1="471.4" x2="510.4" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="509.14" y="475.1" width="2.46" height="5.3" fill="var(--down)"/>
<line x1="514.3" y1="470.3" x2="514.3" y2="522.3" stroke="var(--down)" class="wick"/>
<rect x="513.11" y="483.6" width="2.46" height="35.9" fill="var(--down)"/>
<line x1="518.3" y1="476.7" x2="518.3" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="517.07" y="481.0" width="2.46" height="41.5" fill="var(--up)"/>
<line x1="522.3" y1="492.3" x2="522.3" y2="538.0" stroke="var(--down)" class="wick"/>
<rect x="521.04" y="497.2" width="2.46" height="39.1" fill="var(--down)"/>
<line x1="526.2" y1="438.8" x2="526.2" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="525.01" y="461.9" width="2.46" height="7.1" fill="var(--up)"/>
<line x1="530.2" y1="450.4" x2="530.2" y2="506.3" stroke="var(--down)" class="wick"/>
<rect x="528.98" y="450.4" width="2.46" height="40.6" fill="var(--down)"/>
<line x1="534.2" y1="467.3" x2="534.2" y2="505.4" stroke="var(--up)" class="wick"/>
<rect x="532.95" y="492.0" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="538.1" y1="501.3" x2="538.1" y2="551.3" stroke="var(--down)" class="wick"/>
<rect x="536.91" y="508.8" width="2.46" height="40.2" fill="var(--down)"/>
<line x1="542.1" y1="500.4" x2="542.1" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="511.6" width="2.46" height="44.3" fill="var(--up)"/>
<line x1="546.1" y1="469.6" x2="546.1" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="544.85" y="472.8" width="2.46" height="25.4" fill="var(--up)"/>
<line x1="550.0" y1="458.6" x2="550.0" y2="503.7" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="461.9" width="2.46" height="25.5" fill="var(--down)"/>
<line x1="554.0" y1="472.6" x2="554.0" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="474.3" width="2.46" height="43.7" fill="var(--up)"/>
<line x1="558.0" y1="462.7" x2="558.0" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="467.6" width="2.46" height="19.3" fill="var(--up)"/>
<line x1="562.0" y1="463.7" x2="562.0" y2="494.7" stroke="var(--up)" class="wick"/>
<rect x="560.72" y="477.0" width="2.46" height="14.8" fill="var(--up)"/>
<line x1="565.9" y1="449.5" x2="565.9" y2="492.6" stroke="var(--up)" class="wick"/>
<rect x="564.69" y="460.4" width="2.46" height="18.1" fill="var(--up)"/>
<line x1="569.9" y1="440.4" x2="569.9" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="468.8" width="2.46" height="10.9" fill="var(--down)"/>
<line x1="573.9" y1="472.2" x2="573.9" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="572.63" y="489.8" width="2.46" height="6.9" fill="var(--up)"/>
<line x1="577.8" y1="478.2" x2="577.8" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="485.9" width="2.46" height="14.8" fill="var(--up)"/>
<line x1="581.8" y1="482.4" x2="581.8" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="580.56" y="482.4" width="2.46" height="19.9" fill="var(--down)"/>
<line x1="585.8" y1="493.0" x2="585.8" y2="524.1" stroke="var(--down)" class="wick"/>
<rect x="584.53" y="497.2" width="2.46" height="2.2" fill="var(--down)"/>
<line x1="589.7" y1="491.2" x2="589.7" y2="516.5" stroke="var(--down)" class="wick"/>
<rect x="588.50" y="510.5" width="2.46" height="2.1" fill="var(--down)"/>
<line x1="593.7" y1="506.7" x2="593.7" y2="536.7" stroke="var(--down)" class="wick"/>
<rect x="592.47" y="511.0" width="2.46" height="13.0" fill="var(--down)"/>
<line x1="597.7" y1="495.0" x2="597.7" y2="520.6" stroke="var(--up)" class="wick"/>
<rect x="596.43" y="504.3" width="2.46" height="11.7" fill="var(--up)"/>
<line x1="601.6" y1="475.9" x2="601.6" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="500.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="605.6" y1="495.4" x2="605.6" y2="515.5" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="507.1" width="2.46" height="7.9" fill="var(--down)"/>
<line x1="609.6" y1="504.7" x2="609.6" y2="533.2" stroke="var(--down)" class="wick"/>
<rect x="608.34" y="517.5" width="2.46" height="5.3" fill="var(--down)"/>
<line x1="613.5" y1="522.7" x2="613.5" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="526.1" width="2.46" height="8.7" fill="var(--down)"/>
<line x1="617.5" y1="481.6" x2="617.5" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="616.27" y="505.0" width="2.46" height="11.5" fill="var(--up)"/>
<line x1="621.5" y1="512.0" x2="621.5" y2="558.6" stroke="var(--down)" class="wick"/>
<rect x="620.24" y="515.4" width="2.46" height="17.9" fill="var(--down)"/>
<line x1="625.4" y1="512.4" x2="625.4" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="624.21" y="518.3" width="2.46" height="25.2" fill="var(--down)"/>
<line x1="629.4" y1="533.9" x2="629.4" y2="555.2" stroke="var(--up)" class="wick"/>
<rect x="628.18" y="546.1" width="2.46" height="9.1" fill="var(--up)"/>
<line x1="633.4" y1="546.8" x2="633.4" y2="579.2" stroke="var(--down)" class="wick"/>
<rect x="632.15" y="554.3" width="2.46" height="22.4" fill="var(--down)"/>
<line x1="637.3" y1="560.8" x2="637.3" y2="587.0" stroke="var(--down)" class="wick"/>
<rect x="636.11" y="575.3" width="2.46" height="4.5" fill="var(--down)"/>
<line x1="641.3" y1="553.1" x2="641.3" y2="577.3" stroke="var(--up)" class="wick"/>
<rect x="640.08" y="555.6" width="2.46" height="15.9" fill="var(--up)"/>
<line x1="645.3" y1="542.7" x2="645.3" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="547.6" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="649.2" y1="547.4" x2="649.2" y2="578.2" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="552.7" width="2.46" height="17.4" fill="var(--up)"/>
<line x1="653.2" y1="549.1" x2="653.2" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="651.99" y="550.4" width="2.46" height="4.8" fill="var(--up)"/>
<line x1="657.2" y1="548.3" x2="657.2" y2="569.3" stroke="var(--up)" class="wick"/>
<rect x="655.95" y="550.1" width="2.46" height="5.0" fill="var(--up)"/>
<line x1="661.2" y1="509.1" x2="661.2" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="659.92" y="513.8" width="2.46" height="1.7" fill="var(--down)"/>
<line x1="665.1" y1="520.0" x2="665.1" y2="557.1" stroke="var(--down)" class="wick"/>
<rect x="663.89" y="521.9" width="2.46" height="22.8" fill="var(--down)"/>
<line x1="669.1" y1="543.4" x2="669.1" y2="605.7" stroke="var(--down)" class="wick"/>
<rect x="667.86" y="545.8" width="2.46" height="52.1" fill="var(--down)"/>
<line x1="673.1" y1="519.5" x2="673.1" y2="599.3" stroke="var(--up)" class="wick"/>
<rect x="671.83" y="519.9" width="2.46" height="76.5" fill="var(--up)"/>
<line x1="677.0" y1="488.9" x2="677.0" y2="512.8" stroke="var(--down)" class="wick"/>
<rect x="675.79" y="502.3" width="2.46" height="3.2" fill="var(--down)"/>
<line x1="681.0" y1="453.4" x2="681.0" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="679.76" y="465.0" width="2.46" height="31.4" fill="var(--up)"/>
<line x1="685.0" y1="434.7" x2="685.0" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="683.73" y="446.5" width="2.46" height="8.6" fill="var(--down)"/>
<line x1="688.9" y1="417.0" x2="688.9" y2="450.2" stroke="var(--down)" class="wick"/>
<rect x="687.70" y="422.8" width="2.46" height="18.3" fill="var(--down)"/>
<line x1="692.9" y1="406.7" x2="692.9" y2="446.0" stroke="var(--up)" class="wick"/>
<rect x="691.67" y="415.3" width="2.46" height="20.4" fill="var(--up)"/>
<line x1="696.9" y1="371.3" x2="696.9" y2="413.9" stroke="var(--up)" class="wick"/>
<rect x="695.63" y="389.9" width="2.46" height="21.0" fill="var(--up)"/>
<line x1="700.8" y1="361.7" x2="700.8" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="365.7" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="704.8" y1="386.0" x2="704.8" y2="441.2" stroke="var(--down)" class="wick"/>
<rect x="703.57" y="389.8" width="2.46" height="39.8" fill="var(--down)"/>
<line x1="708.8" y1="358.9" x2="708.8" y2="412.3" stroke="var(--up)" class="wick"/>
<rect x="707.54" y="365.6" width="2.46" height="44.3" fill="var(--up)"/>
<line x1="712.7" y1="347.3" x2="712.7" y2="375.5" stroke="var(--up)" class="wick"/>
<rect x="711.51" y="353.0" width="2.46" height="19.8" fill="var(--up)"/>
<line x1="716.7" y1="346.0" x2="716.7" y2="420.2" stroke="var(--down)" class="wick"/>
<rect x="715.47" y="376.6" width="2.46" height="15.2" fill="var(--down)"/>
<line x1="720.7" y1="370.8" x2="720.7" y2="425.6" stroke="var(--up)" class="wick"/>
<rect x="719.44" y="375.7" width="2.46" height="21.6" fill="var(--up)"/>
<line x1="724.6" y1="375.3" x2="724.6" y2="410.9" stroke="var(--up)" class="wick"/>
<rect x="723.41" y="377.0" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="728.6" y1="332.8" x2="728.6" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="727.38" y="337.8" width="2.46" height="15.3" fill="var(--up)"/>
<line x1="732.6" y1="303.0" x2="732.6" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="731.35" y="308.1" width="2.46" height="24.6" fill="var(--up)"/>
<line x1="736.5" y1="289.6" x2="736.5" y2="319.8" stroke="var(--up)" class="wick"/>
<rect x="735.31" y="293.9" width="2.46" height="8.0" fill="var(--up)"/>
<line x1="740.5" y1="287.5" x2="740.5" y2="315.1" stroke="var(--up)" class="wick"/>
<rect x="739.28" y="289.5" width="2.46" height="4.8" fill="var(--up)"/>
<line x1="744.5" y1="262.5" x2="744.5" y2="289.6" stroke="var(--down)" class="wick"/>
<rect x="743.25" y="278.8" width="2.46" height="3.8" fill="var(--down)"/>
<line x1="748.4" y1="254.6" x2="748.4" y2="295.5" stroke="var(--up)" class="wick"/>
<rect x="747.22" y="262.6" width="2.46" height="22.9" fill="var(--up)"/>
<line x1="752.4" y1="254.6" x2="752.4" y2="278.7" stroke="var(--up)" class="wick"/>
<rect x="751.19" y="257.4" width="2.46" height="17.7" fill="var(--up)"/>
<line x1="756.4" y1="265.0" x2="756.4" y2="287.2" stroke="var(--down)" class="wick"/>
<rect x="755.15" y="268.1" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="760.4" y1="268.4" x2="760.4" y2="304.6" stroke="var(--down)" class="wick"/>
<rect x="759.12" y="275.2" width="2.46" height="15.5" fill="var(--down)"/>
<line x1="764.3" y1="288.5" x2="764.3" y2="311.8" stroke="var(--up)" class="wick"/>
<rect x="763.09" y="296.6" width="2.46" height="9.7" fill="var(--up)"/>
<line x1="768.3" y1="299.5" x2="768.3" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="300.2" width="2.46" height="15.8" fill="var(--down)"/>
<line x1="772.3" y1="306.2" x2="772.3" y2="335.9" stroke="var(--down)" class="wick"/>
<rect x="771.03" y="317.1" width="2.46" height="3.2" fill="var(--down)"/>
<line x1="776.2" y1="312.9" x2="776.2" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="774.99" y="331.8" width="2.46" height="15.7" fill="var(--down)"/>
<line x1="780.2" y1="301.7" x2="780.2" y2="370.2" stroke="var(--up)" class="wick"/>
<rect x="778.96" y="303.4" width="2.46" height="53.5" fill="var(--up)"/>
<line x1="784.2" y1="264.3" x2="784.2" y2="314.9" stroke="var(--up)" class="wick"/>
<rect x="782.93" y="277.2" width="2.46" height="29.6" fill="var(--up)"/>
<line x1="788.1" y1="197.5" x2="788.1" y2="266.6" stroke="var(--up)" class="wick"/>
<rect x="786.90" y="225.0" width="2.46" height="40.5" fill="var(--up)"/>
<line x1="792.1" y1="191.6" x2="792.1" y2="238.7" stroke="var(--up)" class="wick"/>
<rect x="790.87" y="196.8" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="796.1" y1="189.7" x2="796.1" y2="236.2" stroke="var(--down)" class="wick"/>
<rect x="794.83" y="206.4" width="2.46" height="16.9" fill="var(--down)"/>
<line x1="800.0" y1="206.1" x2="800.0" y2="247.8" stroke="var(--down)" class="wick"/>
<rect x="798.80" y="220.5" width="2.46" height="3.6" fill="var(--down)"/>
<line x1="804.0" y1="209.6" x2="804.0" y2="229.5" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="220.1" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="808.0" y1="82.2" x2="808.0" y2="189.2" stroke="var(--up)" class="wick"/>
<rect x="806.74" y="84.8" width="2.46" height="73.1" fill="var(--up)"/>
<line x1="811.9" y1="76.1" x2="811.9" y2="130.1" stroke="var(--up)" class="wick"/>
<rect x="810.71" y="77.1" width="2.46" height="36.0" fill="var(--up)"/>
<line x1="815.9" y1="95.6" x2="815.9" y2="130.2" stroke="var(--down)" class="wick"/>
<rect x="814.67" y="99.2" width="2.46" height="6.9" fill="var(--down)"/>
<line x1="819.9" y1="79.0" x2="819.9" y2="127.1" stroke="var(--up)" class="wick"/>
<rect x="818.64" y="93.4" width="2.46" height="13.6" fill="var(--up)"/>
<line x1="823.8" y1="109.5" x2="823.8" y2="225.1" stroke="var(--down)" class="wick"/>
<rect x="822.61" y="126.8" width="2.46" height="89.2" fill="var(--down)"/>
<line x1="827.8" y1="145.1" x2="827.8" y2="196.4" stroke="var(--up)" class="wick"/>
<rect x="826.58" y="153.6" width="2.46" height="38.8" fill="var(--up)"/>
<line x1="831.8" y1="110.7" x2="831.8" y2="212.8" stroke="var(--down)" class="wick"/>
<rect x="830.55" y="145.3" width="2.46" height="19.9" fill="var(--down)"/>
<line x1="835.7" y1="136.4" x2="835.7" y2="195.9" stroke="var(--up)" class="wick"/>
<rect x="834.51" y="185.1" width="2.46" height="5.8" fill="var(--up)"/>
<line x1="839.7" y1="169.9" x2="839.7" y2="212.5" stroke="var(--up)" class="wick"/>
<rect x="838.48" y="189.9" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="843.7" y1="169.0" x2="843.7" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="842.45" y="185.7" width="2.46" height="12.9" fill="var(--up)"/>
<line x1="847.6" y1="141.3" x2="847.6" y2="170.6" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="152.7" width="2.46" height="12.1" fill="var(--up)"/>
<line x1="851.6" y1="139.7" x2="851.6" y2="178.0" stroke="var(--up)" class="wick"/>
<rect x="850.39" y="175.7" width="2.46" height="2.3" fill="var(--up)"/>
<line x1="855.6" y1="122.1" x2="855.6" y2="180.5" stroke="var(--up)" class="wick"/>
<rect x="854.35" y="169.7" width="2.46" height="4.0" fill="var(--up)"/>
<line x1="859.6" y1="129.7" x2="859.6" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="164.5" width="2.46" height="12.8" fill="var(--down)"/>
<line x1="863.5" y1="161.4" x2="863.5" y2="209.0" stroke="var(--down)" class="wick"/>
<rect x="862.29" y="161.4" width="2.46" height="10.2" fill="var(--down)"/>
<line x1="867.5" y1="180.2" x2="867.5" y2="212.0" stroke="var(--down)" class="wick"/>
<rect x="866.26" y="191.9" width="2.46" height="14.2" fill="var(--down)"/>
<line x1="871.5" y1="204.1" x2="871.5" y2="231.9" stroke="var(--down)" class="wick"/>
<rect x="870.23" y="217.7" width="2.46" height="11.4" fill="var(--down)"/>
<line x1="875.4" y1="208.0" x2="875.4" y2="259.0" stroke="var(--down)" class="wick"/>
<rect x="874.19" y="208.0" width="2.46" height="35.4" fill="var(--down)"/>
<line x1="879.4" y1="196.3" x2="879.4" y2="276.2" stroke="var(--up)" class="wick"/>
<rect x="878.16" y="212.2" width="2.46" height="51.9" fill="var(--up)"/>
<line x1="883.4" y1="178.0" x2="883.4" y2="232.6" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="197.7" width="2.46" height="30.3" fill="var(--down)"/>
<line x1="887.3" y1="197.4" x2="887.3" y2="242.8" stroke="var(--up)" class="wick"/>
<rect x="886.10" y="219.0" width="2.46" height="13.2" fill="var(--up)"/>
<line x1="891.3" y1="179.5" x2="891.3" y2="214.6" stroke="var(--down)" class="wick"/>
<rect x="890.07" y="189.4" width="2.46" height="21.2" fill="var(--down)"/>
<line x1="895.3" y1="196.7" x2="895.3" y2="235.6" stroke="var(--down)" class="wick"/>
<rect x="894.03" y="219.1" width="2.46" height="7.4" fill="var(--down)"/>
<line x1="899.2" y1="210.2" x2="899.2" y2="245.8" stroke="var(--up)" class="wick"/>
<rect x="898.00" y="217.4" width="2.46" height="21.3" fill="var(--up)"/>
<line x1="903.2" y1="202.9" x2="903.2" y2="252.5" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="217.2" width="2.46" height="16.5" fill="var(--down)"/>
<line x1="907.2" y1="222.0" x2="907.2" y2="250.8" stroke="var(--up)" class="wick"/>
<rect x="905.94" y="223.3" width="2.46" height="23.2" fill="var(--up)"/>
<line x1="911.1" y1="180.9" x2="911.1" y2="243.1" stroke="var(--up)" class="wick"/>
<rect x="909.91" y="182.3" width="2.46" height="54.6" fill="var(--up)"/>
<line x1="915.1" y1="170.0" x2="915.1" y2="202.1" stroke="var(--down)" class="wick"/>
<rect x="913.87" y="175.4" width="2.46" height="13.0" fill="var(--down)"/>
<line x1="919.1" y1="164.8" x2="919.1" y2="219.7" stroke="var(--down)" class="wick"/>
<rect x="917.84" y="166.1" width="2.46" height="43.9" fill="var(--down)"/>
<line x1="923.0" y1="192.5" x2="923.0" y2="234.3" stroke="var(--up)" class="wick"/>
<rect x="921.81" y="213.9" width="2.46" height="20.2" fill="var(--up)"/>
<line x1="927.0" y1="184.5" x2="927.0" y2="240.6" stroke="var(--down)" class="wick"/>
<rect x="925.78" y="191.2" width="2.46" height="41.0" fill="var(--down)"/>
<line x1="931.0" y1="240.4" x2="931.0" y2="276.3" stroke="var(--down)" class="wick"/>
<rect x="929.75" y="251.1" width="2.46" height="4.7" fill="var(--down)"/>
<line x1="934.9" y1="333.1" x2="934.9" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="359.8" width="2.46" height="15.4" fill="var(--down)"/>
<line x1="938.9" y1="344.1" x2="938.9" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="937.68" y="365.1" width="2.46" height="10.7" fill="var(--down)"/>
<line x1="942.9" y1="316.4" x2="942.9" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="941.65" y="325.0" width="2.46" height="56.2" fill="var(--up)"/>
<line x1="946.8" y1="319.1" x2="946.8" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="945.62" y="344.2" width="2.46" height="7.1" fill="var(--down)"/>
<line x1="950.8" y1="340.0" x2="950.8" y2="379.4" stroke="var(--down)" class="wick"/>
<rect x="949.59" y="357.6" width="2.46" height="16.4" fill="var(--down)"/>
<line x1="954.8" y1="356.4" x2="954.8" y2="389.5" stroke="var(--down)" class="wick"/>
<rect x="953.55" y="357.4" width="2.46" height="31.1" fill="var(--down)"/>
<line x1="958.8" y1="333.2" x2="958.8" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="345.8" width="2.46" height="7.3" fill="var(--up)"/>
<line x1="962.7" y1="287.1" x2="962.7" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="961.49" y="324.7" width="2.46" height="33.0" fill="var(--up)"/>
<line x1="966.7" y1="303.0" x2="966.7" y2="366.7" stroke="var(--down)" class="wick"/>
<rect x="965.46" y="309.9" width="2.46" height="56.1" fill="var(--down)"/>
<line x1="970.7" y1="332.4" x2="970.7" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="969.43" y="352.7" width="2.46" height="13.1" fill="var(--down)"/>
<line x1="974.6" y1="324.5" x2="974.6" y2="360.9" stroke="var(--up)" class="wick"/>
<rect x="973.39" y="340.9" width="2.46" height="16.4" fill="var(--up)"/>
<line x1="978.6" y1="325.6" x2="978.6" y2="369.7" stroke="var(--down)" class="wick"/>
<rect x="977.36" y="327.9" width="2.46" height="26.4" fill="var(--down)"/>
<line x1="982.6" y1="309.5" x2="982.6" y2="343.5" stroke="var(--down)" class="wick"/>
<rect x="981.33" y="338.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="986.5" y1="313.5" x2="986.5" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="313.5" width="2.46" height="37.6" fill="var(--down)"/>
<line x1="990.5" y1="335.0" x2="990.5" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="989.27" y="346.5" width="2.46" height="9.9" fill="var(--up)"/>
<line x1="994.5" y1="312.9" x2="994.5" y2="356.3" stroke="var(--down)" class="wick"/>
<rect x="993.23" y="330.6" width="2.46" height="13.0" fill="var(--down)"/>
<line x1="998.4" y1="334.0" x2="998.4" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="997.20" y="350.3" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="1002.4" y1="371.2" x2="1002.4" y2="399.1" stroke="var(--down)" class="wick"/>
<rect x="1001.17" y="373.6" width="2.46" height="10.5" fill="var(--down)"/>
<line x1="1006.4" y1="363.7" x2="1006.4" y2="402.8" stroke="var(--down)" class="wick"/>
<rect x="1005.14" y="375.5" width="2.46" height="23.8" fill="var(--down)"/>
<line x1="1010.3" y1="381.4" x2="1010.3" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="1009.11" y="396.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="1014.3" y1="386.4" x2="1014.3" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="1013.07" y="393.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="1018.3" y1="363.5" x2="1018.3" y2="399.5" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="397.0" width="2.46" height="1.1" fill="var(--down)"/>
<line x1="1022.2" y1="397.6" x2="1022.2" y2="426.6" stroke="var(--down)" class="wick"/>
<rect x="1021.01" y="404.9" width="2.46" height="17.2" fill="var(--down)"/>
<line x1="1026.2" y1="415.3" x2="1026.2" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="1024.98" y="423.6" width="2.46" height="3.8" fill="var(--down)"/>
<line x1="1030.2" y1="418.7" x2="1030.2" y2="439.6" stroke="var(--down)" class="wick"/>
<rect x="1028.95" y="425.7" width="2.46" height="6.5" fill="var(--down)"/>
<line x1="1034.1" y1="410.9" x2="1034.1" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="1032.91" y="413.5" width="2.46" height="15.6" fill="var(--up)"/>
<line x1="1038.1" y1="419.3" x2="1038.1" y2="439.7" stroke="var(--up)" class="wick"/>
<rect x="1036.88" y="424.2" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="1042.1" y1="364.0" x2="1042.1" y2="419.8" stroke="var(--up)" class="wick"/>
<rect x="1040.85" y="369.0" width="2.46" height="46.5" fill="var(--up)"/>
<line x1="1046.0" y1="339.9" x2="1046.0" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="1044.82" y="359.4" width="2.46" height="21.3" fill="var(--up)"/>
<line x1="1050.0" y1="314.3" x2="1050.0" y2="373.8" stroke="var(--up)" class="wick"/>
<rect x="1048.79" y="314.9" width="2.46" height="25.9" fill="var(--up)"/>
<line x1="60" y1="271.2" x2="1052" y2="271.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="274.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$360 R1</text>
<text x="1058" y="286.7" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="379.2" x2="1052" y2="379.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="373.2" font-size="11.5" fill="var(--support)" font-weight="600">$329 S1</text>
<text x="1058" y="385.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="422.7" x2="1052" y2="422.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="416.7" font-size="11.5" fill="var(--support)" font-weight="600">$316 S2</text>
<text x="1058" y="428.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="478.6" x2="1052" y2="478.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="472.6" font-size="11.5" fill="var(--support)" font-weight="600">$300 S3</text>
<text x="1058" y="484.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="314.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="306.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $348 (2026-08-27)</text>
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
| R1 | $360 | 4 | 2025-09-09 · 2025-10-27 · 2026-05-08 · 2026-07-28. **이 1년에서 가장 자주 부딪힌 상단**이며 11개월에 걸쳐 네 번 확인됐다. 2025-10-27은 FY2025 3분기 실적일, 2026-07-28은 가이던스 상향 발표 직후다 — 두 번 다 호재 당일에도 이 대역을 넘지 못했다. 현재가 대비 **+3.6%** |
| **현재가** | **$347.55** (2026-08-27 종가) | — | R1과 S1 사이. **다른 문서가 쓰는 기준일은 하루 뒤인 2026-08-28($340.39)이며, 그 값 기준이면 R1까지 +5.8% · S1까지 −3.3%다**(위 데이터 출처 note 참고) |
| S1 | $329 | 2 | 2025-09-10 · 2026-05-20. 2025-09-10은 Synopsys가 FY2025 3분기 실적으로 하루 −35.8% 빠진 날로, Cadence도 같은 날 −6.42%($361.77 → $338.53) 밀리며 이 대역을 만들었다. 현재가 대비 **−5.3%** |
| S2 | $316 | 3 | 2025-10-14 · 2025-12-17 · 2026-07-17. 2026-07-17은 아래 3-3의 −9.47% 급락일 장중 저가다 — 하루짜리 사건이 아니라 **세 차례 확인된 대역**이라는 점에서 S1보다 표본이 낫다. 현재가 대비 **−9.1%** |
| S3 | $300 | 3 | 2025-11-21 · 2026-01-05 · 2026-01-21. $300 라운드넘버 부근에 저점 세 개가 두 달 사이 모였고, 2026-02-03에 한 번 아래로 관통됐다가 되돌렸다(3-1). 현재가 대비 **−13.7%** |
| 참고선 | $416.69 | — | **52주(그리고 5년) 최고**, 2026-06-02 장중. 3-2의 하루짜리 급등 직후 찍은 단일 고점이라 스윙 클러스터를 만들지 못했다 — 저항선으로 취급하지 않는다 |
| 참고선 | $262.75 | — | **52주 최저**, 2026-02-03 장중. S3($300)를 아래로 관통한 유일한 자리이나 재확인 없이 한 번만 닿았고, 3주 만에 위로 되돌렸다 — 지지선으로 취급하지 않는다 |

레벨이 저항 1개 · 지지 3개로 비대칭인 것은 현재가가 **1년 레인지($262.75~$416.69)의 상단 쪽**에 있기 때문이다. 위쪽에는 클러스터를 만들 만큼 반복된 스윙 고점이 $360 대역 하나뿐이다.

---

## 3. 관측된 특이 구간

이 1년 구간에는 가격대가 구조적으로 재설정된 사건이 셋 있다. **아래는 가격·거래량에 대한 사실 서술이며, 각 사건의 투자 판단상 의미는 [투자 판단](./07_investment.md)에서 다룬다.**

### 3-1. 2026-02-18 — FY2025 연간 실적 갭업

- 2026-02-17 장 마감 후 발표된 FY2025 연간 실적이 계기였다.
- 종가 기준 전일 대비 **+7.60%** ($283.46 → $305.01), 시가 $302.96로 **갭 +6.88%**. 거래량은 평소(일 220만 주 내외) 대비 약 **1.8배**인 **395만 주**.
- 직전 2주 사이 주가는 2026-02-03에 하루 −7.15%로 **52주 최저 $262.75**를 찍은 상태였다. **그 급락의 계기는 이 저장소가 확인하지 못했다(확인 필요)** — [최근 뉴스 / 이슈](./08_news.md) 로그에도 해당 항목이 없다. 이 갭업으로 $300 대역(S3)이 다시 위로 회복됐고, 이후 이 차트 구간에서 종가가 $300 아래로 내려간 적은 없다.

### 3-2. 2026-06-01 — Computex ChipStack 발표 급등

- Computex에서 칩 검증 시간을 5주에서 24시간 이내로 줄이는 ChipStack AI Super Agent를 공개하고 Samsung Foundry와의 2nm·3D-IC 협력 확대를 발표한 것이 계기다([최근 뉴스 / 이슈](./08_news.md)).
- 종가 기준 전일 대비 **+10.46%** ($374.93 → $414.16), 시가 $393.00로 갭 +4.82%. 거래량 **452만 주**(평소의 약 **2.1배**). 익일 2026-06-02 장중 $416.69로 52주 최고를 경신했다.
- **이 상승은 나흘 만에 되밀렸다** — 2026-06-05 하루 −8.62%($411.68 → $376.19). $400 위 구간은 머문 기간이 짧아 스윙 클러스터를 만들지 못했고, 그래서 위 표에 $360 위의 레벨이 없다.

### 3-3. 2026-07-17 — AI 서사發 급락, 6거래일 연속 하락

- 중국 Moonshot AI의 Kimi K3 공개로 "저비용 오픈웨이트 모델이 AI 인프라 투자 수익률을 훼손한다"는 우려가 확산된 것이 계기다([최근 뉴스 / 이슈](./08_news.md)).
- 종가 기준 전일 대비 **−9.47%** ($364.65 → $330.11), 시가 $334.56로 **갭 −8.25%**. 거래량 **519만 주**(평소의 약 **2.4배**). 장중 저가가 S2($316) 대역을 만들었고, 이후 6거래일 연속 하락으로 누적 약 −14%였다.
- **Cadence 고유 악재가 아니라 EDA 업종 공통 재평가였다** — 같은 날 [Synopsys](../synopsys/09_technical_daily.md)도 −7.85%로 52주 최저를 찍었다. 열흘 뒤 2026-07-27 가이던스 상향 발표로 되돌려 2026-07-28에 R1($360) 대역을 다시 찍었다(위 표 R1의 네 번째 터치).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-29. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py` (`CDNS --name "Cadence Design Systems" --event 2026-06-01:"Computex ChipStack 발표 급등" --event 2026-07-17:"AI 서사發 급락" --ref-line 416.69:"52주 최고" --close-on 2026-08-27 --close-on 2026-08-28 --emit all`)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **차트의 마지막 봉이 2026-08-27이라 이 문서의 "현재가"만 하루 앞선다.** 수집 시점에 제공처가 2026-08-28 일봉을 확정하지 않았기 때문이며(`--close-on 2026-08-28`은 "거래일 아님"으로 반환됐다), 다른 문서와의 대조 결과는 상단 note에 남겼다. **다음 회차에 재생성하면 이 하루가 채워지면서 레벨이 미세하게 달라질 수 있다.**
    - **레벨이 저항 1개 · 지지 3개로 비대칭이다.** 자동 기준(터치 2회 이상)을 그대로 적용한 결과이며 억지로 3개씩 맞추지 않았다. 52주 최고·최저는 각각 터치 1회라 참고선으로만 뒀다 — **터치 1회짜리 가격은 통계적 강도가 없으므로 레벨과 같은 무게로 읽지 말 것.**
    - **3-2의 $400 돌파 구간(2026-06-01~06-05)이 표본을 왜곡할 수 있다.** 나흘 만에 되밀린 탓에 그 구간에 스윙 클러스터가 없어, 위 레벨은 사실상 **"$262.75~$416.69 중 $300~$360 대역"의 구조**만 설명한다. 현재가가 R1 위로 올라서면 이 표에는 참고할 저항이 남지 않는다.
    - 이 기간에 주식분할·유상증자 등 가격 연속성을 깨는 이벤트는 없었다. Hexagon D&E 인수 대가로 발행한 신주(2026-02)는 발행주식수를 늘렸으나 **주가 시계열의 소급 조정 사유가 아니다**([핵심 지표](./04_metrics.md) A.4 주10).

Sources: [Cadence Design Systems (CDNS) Shares Drop Amid AI Model Concerns — GuruFocus](https://www.gurufocus.com/news/8965307/cadence-design-systems-cdns-shares-drop-amid-ai-model-concerns?mobile=true) · [Cadence Design Systems Stock Slides 14% Over 6 Straight Down Days — Trefis](https://www.trefis.com/stock/cdns/articles/607964/cadence-design-systems-stock-slides-14-over-6-straight-down-days/2026-07-20) · [Cadence Design Systems Inc (CDNS) Shares Surge 10.5% — GuruFocus](https://www.gurufocus.com/news/8894566/cadence-design-systems-inc-cdns-shares-surge-105-what-gf-score-of-99-tells-investors)

---

*작성일: 2026-08-29*
