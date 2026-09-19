# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **이 차트의 마지막 봉은 2026-09-17(종가 $88.33)이고, [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 기준 종가는 2026-09-18의 $87.49다 — 하루 어긋난다.** 9월 18일 세션은 정상 체결됐으나 조회 시점(2026-09-19)에 Yahoo 일봉 시계열의 해당 봉 종가가 비어 있었다(시가·고가·저가는 있고 종가만 `null`). 같은 주의 [주봉 차트](./10_technical_weekly.md)는 그 세션을 포함해 종가 $87.49로 마감돼 있어, **두 차트를 나란히 보면 값이 다른 것이 정상**이다.
- 가격 계보에도 주의가 필요하다 — **2024-10-02 이전 구간은 Chesapeake Energy(CHK) 시절 주가**이며, 사명·티커 변경은 분할이 아니므로 소급조정 대상이 아니다(이 1년 창에는 해당 구간이 없다).

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-19 ~ 2026-09-17)

<style>
.exe-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .exe-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.exe-chart svg { width:100%; height:auto; display:block; }
.exe-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.exe-chart .title { fill: var(--ink); font-weight:600; }
.exe-chart .grid { stroke: var(--grid); stroke-width:1; }
.exe-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="exe-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Expand Energy(EXE) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Expand Energy (EXE) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-19 ~ 2026-09-17 · 마지막 종가 $88.33 (2026-09-17) · 단위 USD</text>
<line x1="60" y1="542.7" x2="1052" y2="542.7" class="grid"/>
<text x="52" y="546.7" font-size="11" text-anchor="end" fill="var(--muted)">90</text>
<line x1="60" y1="414.7" x2="1052" y2="414.7" class="grid"/>
<text x="52" y="418.7" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="286.6" x2="1052" y2="286.6" class="grid"/>
<text x="52" y="290.6" font-size="11" text-anchor="end" fill="var(--muted)">110</text>
<line x1="60" y1="158.5" x2="1052" y2="158.5" class="grid"/>
<text x="52" y="162.5" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="93.7" y1="626.0" x2="93.7" y2="631.0" class="axis"/>
<text x="93.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="185.0" y1="626.0" x2="185.0" y2="631.0" class="axis"/>
<text x="185.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="260.4" y1="626.0" x2="260.4" y2="631.0" class="axis"/>
<text x="260.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="347.7" y1="626.0" x2="347.7" y2="631.0" class="axis"/>
<text x="347.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="427.0" y1="626.0" x2="427.0" y2="631.0" class="axis"/>
<text x="427.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="502.4" y1="626.0" x2="502.4" y2="631.0" class="axis"/>
<text x="502.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="589.7" y1="626.0" x2="589.7" y2="631.0" class="axis"/>
<text x="589.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="673.1" y1="626.0" x2="673.1" y2="631.0" class="axis"/>
<text x="673.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="752.4" y1="626.0" x2="752.4" y2="631.0" class="axis"/>
<text x="752.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="835.7" y1="626.0" x2="835.7" y2="631.0" class="axis"/>
<text x="835.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="923.0" y1="626.0" x2="923.0" y2="631.0" class="axis"/>
<text x="923.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1006.4" y1="626.0" x2="1006.4" y2="631.0" class="axis"/>
<text x="1006.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="426.4" x2="62.0" y2="448.1" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="429.8" width="2.46" height="4.1" fill="var(--down)"/>
<line x1="66.0" y1="432.7" x2="66.0" y2="464.4" stroke="var(--up)" class="wick"/>
<rect x="64.72" y="436.9" width="2.46" height="4.4" fill="var(--up)"/>
<line x1="69.9" y1="397.5" x2="69.9" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="68.69" y="405.4" width="2.46" height="29.1" fill="var(--up)"/>
<line x1="73.9" y1="355.6" x2="73.9" y2="401.8" stroke="var(--up)" class="wick"/>
<rect x="72.66" y="374.9" width="2.46" height="26.9" fill="var(--up)"/>
<line x1="77.9" y1="352.9" x2="77.9" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="76.63" y="358.5" width="2.46" height="12.2" fill="var(--up)"/>
<line x1="81.8" y1="334.9" x2="81.8" y2="356.2" stroke="var(--up)" class="wick"/>
<rect x="80.59" y="340.7" width="2.46" height="10.8" fill="var(--up)"/>
<line x1="85.8" y1="312.2" x2="85.8" y2="348.6" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="327.4" width="2.46" height="17.5" fill="var(--up)"/>
<line x1="89.8" y1="307.6" x2="89.8" y2="335.5" stroke="var(--down)" class="wick"/>
<rect x="88.53" y="330.1" width="2.46" height="4.6" fill="var(--down)"/>
<line x1="93.7" y1="282.0" x2="93.7" y2="349.8" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="297.1" width="2.46" height="52.8" fill="var(--up)"/>
<line x1="97.7" y1="285.4" x2="97.7" y2="321.8" stroke="var(--down)" class="wick"/>
<rect x="96.47" y="300.4" width="2.46" height="13.6" fill="var(--down)"/>
<line x1="101.7" y1="305.8" x2="101.7" y2="329.2" stroke="var(--down)" class="wick"/>
<rect x="100.43" y="312.1" width="2.46" height="7.3" fill="var(--down)"/>
<line x1="105.6" y1="286.6" x2="105.6" y2="322.2" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="302.2" width="2.46" height="13.4" fill="var(--down)"/>
<line x1="109.6" y1="295.0" x2="109.6" y2="324.7" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="299.2" width="2.46" height="21.5" fill="var(--up)"/>
<line x1="113.6" y1="287.5" x2="113.6" y2="322.7" stroke="var(--down)" class="wick"/>
<rect x="112.34" y="290.1" width="2.46" height="13.3" fill="var(--down)"/>
<line x1="117.5" y1="291.7" x2="117.5" y2="349.2" stroke="var(--down)" class="wick"/>
<rect x="116.31" y="294.9" width="2.46" height="43.2" fill="var(--down)"/>
<line x1="121.5" y1="332.3" x2="121.5" y2="392.9" stroke="var(--down)" class="wick"/>
<rect x="120.27" y="345.7" width="2.46" height="46.4" fill="var(--down)"/>
<line x1="125.5" y1="375.3" x2="125.5" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="124.24" y="380.3" width="2.46" height="1.5" fill="var(--up)"/>
<line x1="129.4" y1="371.6" x2="129.4" y2="431.2" stroke="var(--up)" class="wick"/>
<rect x="128.21" y="397.2" width="2.46" height="8.6" fill="var(--up)"/>
<line x1="133.4" y1="362.8" x2="133.4" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="132.18" y="374.0" width="2.46" height="17.3" fill="var(--up)"/>
<line x1="137.4" y1="362.6" x2="137.4" y2="445.8" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="372.0" width="2.46" height="60.7" fill="var(--down)"/>
<line x1="141.3" y1="402.2" x2="141.3" y2="442.3" stroke="var(--up)" class="wick"/>
<rect x="140.11" y="404.7" width="2.46" height="24.0" fill="var(--up)"/>
<line x1="145.3" y1="318.1" x2="145.3" y2="383.4" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="326.3" width="2.46" height="50.0" fill="var(--up)"/>
<line x1="149.3" y1="305.5" x2="149.3" y2="343.9" stroke="var(--down)" class="wick"/>
<rect x="148.05" y="328.2" width="2.46" height="8.3" fill="var(--down)"/>
<line x1="153.2" y1="319.1" x2="153.2" y2="377.4" stroke="var(--down)" class="wick"/>
<rect x="152.02" y="319.1" width="2.46" height="39.3" fill="var(--down)"/>
<line x1="157.2" y1="319.1" x2="157.2" y2="377.7" stroke="var(--down)" class="wick"/>
<rect x="155.99" y="334.6" width="2.46" height="22.9" fill="var(--down)"/>
<line x1="161.2" y1="336.3" x2="161.2" y2="378.3" stroke="var(--down)" class="wick"/>
<rect x="159.95" y="339.3" width="2.46" height="27.0" fill="var(--down)"/>
<line x1="165.2" y1="352.0" x2="165.2" y2="381.6" stroke="var(--down)" class="wick"/>
<rect x="163.92" y="354.2" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="169.1" y1="364.7" x2="169.1" y2="404.7" stroke="var(--down)" class="wick"/>
<rect x="167.89" y="365.0" width="2.46" height="36.9" fill="var(--down)"/>
<line x1="173.1" y1="366.7" x2="173.1" y2="431.8" stroke="var(--down)" class="wick"/>
<rect x="171.86" y="371.6" width="2.46" height="37.8" fill="var(--down)"/>
<line x1="177.1" y1="389.3" x2="177.1" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="175.83" y="408.0" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="181.0" y1="363.1" x2="181.0" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="372.3" width="2.46" height="17.9" fill="var(--up)"/>
<line x1="185.0" y1="282.1" x2="185.0" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="285.5" width="2.46" height="81.3" fill="var(--up)"/>
<line x1="189.0" y1="263.9" x2="189.0" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="187.73" y="285.9" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="192.9" y1="255.3" x2="192.9" y2="302.7" stroke="var(--up)" class="wick"/>
<rect x="191.70" y="285.9" width="2.46" height="8.1" fill="var(--up)"/>
<line x1="196.9" y1="252.9" x2="196.9" y2="298.1" stroke="var(--down)" class="wick"/>
<rect x="195.67" y="275.3" width="2.46" height="3.3" fill="var(--down)"/>
<line x1="200.9" y1="249.2" x2="200.9" y2="299.4" stroke="var(--up)" class="wick"/>
<rect x="199.63" y="255.2" width="2.46" height="33.8" fill="var(--up)"/>
<line x1="204.8" y1="219.4" x2="204.8" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="203.60" y="224.7" width="2.46" height="20.1" fill="var(--up)"/>
<line x1="208.8" y1="172.6" x2="208.8" y2="225.1" stroke="var(--up)" class="wick"/>
<rect x="207.57" y="175.9" width="2.46" height="43.2" fill="var(--up)"/>
<line x1="212.8" y1="154.6" x2="212.8" y2="189.6" stroke="var(--up)" class="wick"/>
<rect x="211.54" y="165.4" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="216.7" y1="158.5" x2="216.7" y2="189.2" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="168.7" width="2.46" height="15.9" fill="var(--down)"/>
<line x1="220.7" y1="187.1" x2="220.7" y2="251.1" stroke="var(--up)" class="wick"/>
<rect x="219.47" y="193.3" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="224.7" y1="184.7" x2="224.7" y2="220.2" stroke="var(--down)" class="wick"/>
<rect x="223.44" y="195.1" width="2.46" height="2.0" fill="var(--down)"/>
<line x1="228.6" y1="187.8" x2="228.6" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="227.41" y="194.8" width="2.46" height="19.3" fill="var(--up)"/>
<line x1="232.6" y1="188.1" x2="232.6" y2="217.0" stroke="var(--up)" class="wick"/>
<rect x="231.38" y="193.4" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="236.6" y1="143.2" x2="236.6" y2="230.7" stroke="var(--down)" class="wick"/>
<rect x="235.35" y="188.2" width="2.46" height="40.7" fill="var(--down)"/>
<line x1="240.5" y1="208.6" x2="240.5" y2="255.3" stroke="var(--up)" class="wick"/>
<rect x="239.31" y="222.6" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="244.5" y1="191.2" x2="244.5" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="243.28" y="202.7" width="2.46" height="20.0" fill="var(--up)"/>
<line x1="248.5" y1="202.8" x2="248.5" y2="228.9" stroke="var(--up)" class="wick"/>
<rect x="247.25" y="209.6" width="2.46" height="9.2" fill="var(--up)"/>
<line x1="252.4" y1="162.3" x2="252.4" y2="203.5" stroke="var(--up)" class="wick"/>
<rect x="251.22" y="174.2" width="2.46" height="23.8" fill="var(--up)"/>
<line x1="256.4" y1="123.9" x2="256.4" y2="167.1" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="133.8" width="2.46" height="29.1" fill="var(--up)"/>
<line x1="260.4" y1="123.9" x2="260.4" y2="156.0" stroke="var(--down)" class="wick"/>
<rect x="259.15" y="126.5" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="264.4" y1="138.9" x2="264.4" y2="188.7" stroke="var(--down)" class="wick"/>
<rect x="263.12" y="142.5" width="2.46" height="45.2" fill="var(--down)"/>
<line x1="268.3" y1="117.7" x2="268.3" y2="186.1" stroke="var(--up)" class="wick"/>
<rect x="267.09" y="121.5" width="2.46" height="58.0" fill="var(--up)"/>
<line x1="272.3" y1="95.8" x2="272.3" y2="137.8" stroke="var(--down)" class="wick"/>
<rect x="271.06" y="120.2" width="2.46" height="11.5" fill="var(--down)"/>
<line x1="276.3" y1="73.7" x2="276.3" y2="122.6" stroke="var(--down)" class="wick"/>
<rect x="275.03" y="110.2" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="280.2" y1="127.7" x2="280.2" y2="181.9" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="132.3" width="2.46" height="38.0" fill="var(--down)"/>
<line x1="284.2" y1="163.9" x2="284.2" y2="194.3" stroke="var(--down)" class="wick"/>
<rect x="282.96" y="170.4" width="2.46" height="20.6" fill="var(--down)"/>
<line x1="288.2" y1="184.5" x2="288.2" y2="219.7" stroke="var(--down)" class="wick"/>
<rect x="286.93" y="184.5" width="2.46" height="16.4" fill="var(--down)"/>
<line x1="292.1" y1="204.8" x2="292.1" y2="244.0" stroke="var(--down)" class="wick"/>
<rect x="290.90" y="216.0" width="2.46" height="15.1" fill="var(--down)"/>
<line x1="296.1" y1="222.9" x2="296.1" y2="268.6" stroke="var(--down)" class="wick"/>
<rect x="294.87" y="231.4" width="2.46" height="19.5" fill="var(--down)"/>
<line x1="300.1" y1="251.1" x2="300.1" y2="301.4" stroke="var(--down)" class="wick"/>
<rect x="298.83" y="251.1" width="2.46" height="28.6" fill="var(--down)"/>
<line x1="304.0" y1="296.2" x2="304.0" y2="337.9" stroke="var(--down)" class="wick"/>
<rect x="302.80" y="296.2" width="2.46" height="34.2" fill="var(--down)"/>
<line x1="308.0" y1="288.7" x2="308.0" y2="323.8" stroke="var(--up)" class="wick"/>
<rect x="306.77" y="292.5" width="2.46" height="25.2" fill="var(--up)"/>
<line x1="312.0" y1="279.6" x2="312.0" y2="316.9" stroke="var(--down)" class="wick"/>
<rect x="310.74" y="291.8" width="2.46" height="23.7" fill="var(--down)"/>
<line x1="315.9" y1="290.3" x2="315.9" y2="321.8" stroke="var(--up)" class="wick"/>
<rect x="314.71" y="302.7" width="2.46" height="7.0" fill="var(--up)"/>
<line x1="319.9" y1="292.2" x2="319.9" y2="318.8" stroke="var(--down)" class="wick"/>
<rect x="318.67" y="298.5" width="2.46" height="15.8" fill="var(--down)"/>
<line x1="323.9" y1="267.2" x2="323.9" y2="306.1" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="271.6" width="2.46" height="31.5" fill="var(--up)"/>
<line x1="327.8" y1="278.5" x2="327.8" y2="297.8" stroke="var(--down)" class="wick"/>
<rect x="326.61" y="291.0" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="331.8" y1="287.8" x2="331.8" y2="304.0" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="290.9" width="2.46" height="2.2" fill="var(--down)"/>
<line x1="335.8" y1="259.7" x2="335.8" y2="290.7" stroke="var(--up)" class="wick"/>
<rect x="334.55" y="263.8" width="2.46" height="21.3" fill="var(--up)"/>
<line x1="339.7" y1="242.8" x2="339.7" y2="260.9" stroke="var(--down)" class="wick"/>
<rect x="338.51" y="250.1" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="343.7" y1="262.8" x2="343.7" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="342.48" y="267.0" width="2.46" height="15.0" fill="var(--down)"/>
<line x1="347.7" y1="282.4" x2="347.7" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="346.45" y="286.8" width="2.46" height="2.7" fill="var(--down)"/>
<line x1="351.6" y1="308.5" x2="351.6" y2="377.8" stroke="var(--down)" class="wick"/>
<rect x="350.42" y="308.7" width="2.46" height="18.6" fill="var(--down)"/>
<line x1="355.6" y1="331.3" x2="355.6" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="354.39" y="341.8" width="2.46" height="3.3" fill="var(--down)"/>
<line x1="359.6" y1="308.5" x2="359.6" y2="348.7" stroke="var(--up)" class="wick"/>
<rect x="358.35" y="329.3" width="2.46" height="15.8" fill="var(--up)"/>
<line x1="363.6" y1="320.8" x2="363.6" y2="379.6" stroke="var(--down)" class="wick"/>
<rect x="362.32" y="335.9" width="2.46" height="23.7" fill="var(--down)"/>
<line x1="367.5" y1="349.7" x2="367.5" y2="401.3" stroke="var(--down)" class="wick"/>
<rect x="366.29" y="366.2" width="2.46" height="27.5" fill="var(--down)"/>
<line x1="371.5" y1="364.2" x2="371.5" y2="394.2" stroke="var(--up)" class="wick"/>
<rect x="370.26" y="378.3" width="2.46" height="5.6" fill="var(--up)"/>
<line x1="375.5" y1="348.6" x2="375.5" y2="385.3" stroke="var(--down)" class="wick"/>
<rect x="374.23" y="365.2" width="2.46" height="11.3" fill="var(--down)"/>
<line x1="379.4" y1="383.4" x2="379.4" y2="408.6" stroke="var(--down)" class="wick"/>
<rect x="378.19" y="388.8" width="2.46" height="7.2" fill="var(--down)"/>
<line x1="383.4" y1="389.8" x2="383.4" y2="424.0" stroke="var(--down)" class="wick"/>
<rect x="382.16" y="398.9" width="2.46" height="21.9" fill="var(--down)"/>
<line x1="387.4" y1="408.1" x2="387.4" y2="432.6" stroke="var(--up)" class="wick"/>
<rect x="386.13" y="416.2" width="2.46" height="14.5" fill="var(--up)"/>
<line x1="391.3" y1="326.3" x2="391.3" y2="374.4" stroke="var(--down)" class="wick"/>
<rect x="390.10" y="339.8" width="2.46" height="14.0" fill="var(--down)"/>
<line x1="395.3" y1="264.9" x2="395.3" y2="321.9" stroke="var(--up)" class="wick"/>
<rect x="394.07" y="293.0" width="2.46" height="27.8" fill="var(--up)"/>
<line x1="399.3" y1="274.8" x2="399.3" y2="313.3" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="286.6" width="2.46" height="6.5" fill="var(--down)"/>
<line x1="403.2" y1="264.5" x2="403.2" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="402.00" y="269.3" width="2.46" height="23.8" fill="var(--down)"/>
<line x1="407.2" y1="232.4" x2="407.2" y2="299.4" stroke="var(--up)" class="wick"/>
<rect x="405.97" y="256.3" width="2.46" height="10.9" fill="var(--up)"/>
<line x1="411.2" y1="252.0" x2="411.2" y2="322.3" stroke="var(--down)" class="wick"/>
<rect x="409.94" y="256.8" width="2.46" height="44.8" fill="var(--down)"/>
<line x1="415.1" y1="282.8" x2="415.1" y2="314.7" stroke="var(--up)" class="wick"/>
<rect x="413.91" y="290.9" width="2.46" height="10.8" fill="var(--up)"/>
<line x1="419.1" y1="263.7" x2="419.1" y2="298.7" stroke="var(--down)" class="wick"/>
<rect x="417.87" y="269.8" width="2.46" height="18.1" fill="var(--down)"/>
<line x1="423.1" y1="232.9" x2="423.1" y2="280.0" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="255.7" width="2.46" height="21.1" fill="var(--up)"/>
<line x1="427.0" y1="295.4" x2="427.0" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="425.81" y="304.0" width="2.46" height="21.8" fill="var(--down)"/>
<line x1="431.0" y1="304.8" x2="431.0" y2="341.5" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="305.8" width="2.46" height="22.0" fill="var(--up)"/>
<line x1="435.0" y1="278.5" x2="435.0" y2="320.1" stroke="var(--down)" class="wick"/>
<rect x="433.75" y="285.2" width="2.46" height="11.8" fill="var(--down)"/>
<line x1="438.9" y1="280.0" x2="438.9" y2="316.5" stroke="var(--up)" class="wick"/>
<rect x="437.71" y="294.6" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="442.9" y1="257.4" x2="442.9" y2="293.0" stroke="var(--up)" class="wick"/>
<rect x="441.68" y="281.8" width="2.46" height="5.3" fill="var(--up)"/>
<line x1="446.9" y1="331.4" x2="446.9" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="445.65" y="356.9" width="2.46" height="16.3" fill="var(--down)"/>
<line x1="450.8" y1="357.0" x2="450.8" y2="394.4" stroke="var(--down)" class="wick"/>
<rect x="449.62" y="364.2" width="2.46" height="22.2" fill="var(--down)"/>
<line x1="454.8" y1="350.9" x2="454.8" y2="379.0" stroke="var(--up)" class="wick"/>
<rect x="453.59" y="370.7" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="458.8" y1="360.9" x2="458.8" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="457.55" y="366.7" width="2.46" height="3.8" fill="var(--down)"/>
<line x1="462.8" y1="347.6" x2="462.8" y2="389.0" stroke="var(--up)" class="wick"/>
<rect x="461.52" y="362.8" width="2.46" height="16.9" fill="var(--up)"/>
<line x1="466.7" y1="359.9" x2="466.7" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="465.49" y="369.6" width="2.46" height="9.9" fill="var(--down)"/>
<line x1="470.7" y1="351.5" x2="470.7" y2="435.8" stroke="var(--down)" class="wick"/>
<rect x="469.46" y="361.2" width="2.46" height="59.6" fill="var(--down)"/>
<line x1="474.7" y1="364.7" x2="474.7" y2="411.7" stroke="var(--up)" class="wick"/>
<rect x="473.43" y="365.3" width="2.46" height="30.5" fill="var(--up)"/>
<line x1="478.6" y1="296.9" x2="478.6" y2="368.8" stroke="var(--up)" class="wick"/>
<rect x="477.39" y="311.4" width="2.46" height="47.2" fill="var(--up)"/>
<line x1="482.6" y1="290.4" x2="482.6" y2="386.9" stroke="var(--down)" class="wick"/>
<rect x="481.36" y="312.2" width="2.46" height="61.7" fill="var(--down)"/>
<line x1="486.6" y1="372.6" x2="486.6" y2="403.8" stroke="var(--up)" class="wick"/>
<rect x="485.33" y="373.9" width="2.46" height="3.8" fill="var(--up)"/>
<line x1="490.5" y1="332.6" x2="490.5" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="489.30" y="337.2" width="2.46" height="18.2" fill="var(--up)"/>
<line x1="494.5" y1="321.1" x2="494.5" y2="354.4" stroke="var(--up)" class="wick"/>
<rect x="493.27" y="334.1" width="2.46" height="18.7" fill="var(--up)"/>
<line x1="498.5" y1="289.5" x2="498.5" y2="328.2" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="313.2" width="2.46" height="7.9" fill="var(--up)"/>
<line x1="502.4" y1="269.0" x2="502.4" y2="329.6" stroke="var(--down)" class="wick"/>
<rect x="501.20" y="276.4" width="2.46" height="29.5" fill="var(--down)"/>
<line x1="506.4" y1="276.2" x2="506.4" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="505.17" y="276.2" width="2.46" height="36.1" fill="var(--down)"/>
<line x1="510.4" y1="319.5" x2="510.4" y2="351.7" stroke="var(--down)" class="wick"/>
<rect x="509.14" y="328.3" width="2.46" height="11.0" fill="var(--down)"/>
<line x1="514.3" y1="318.6" x2="514.3" y2="345.5" stroke="var(--up)" class="wick"/>
<rect x="513.11" y="329.2" width="2.46" height="15.5" fill="var(--up)"/>
<line x1="518.3" y1="302.8" x2="518.3" y2="337.2" stroke="var(--down)" class="wick"/>
<rect x="517.07" y="312.8" width="2.46" height="14.2" fill="var(--down)"/>
<line x1="522.3" y1="297.3" x2="522.3" y2="328.7" stroke="var(--down)" class="wick"/>
<rect x="521.04" y="313.6" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="526.2" y1="316.3" x2="526.2" y2="358.8" stroke="var(--down)" class="wick"/>
<rect x="525.01" y="323.7" width="2.46" height="31.1" fill="var(--down)"/>
<line x1="530.2" y1="294.2" x2="530.2" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="528.98" y="304.8" width="2.46" height="43.6" fill="var(--up)"/>
<line x1="534.2" y1="298.1" x2="534.2" y2="327.7" stroke="var(--down)" class="wick"/>
<rect x="532.95" y="300.4" width="2.46" height="14.0" fill="var(--down)"/>
<line x1="538.1" y1="289.0" x2="538.1" y2="328.8" stroke="var(--down)" class="wick"/>
<rect x="536.91" y="315.6" width="2.46" height="9.1" fill="var(--down)"/>
<line x1="542.1" y1="287.8" x2="542.1" y2="333.2" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="315.9" width="2.46" height="7.7" fill="var(--up)"/>
<line x1="546.1" y1="293.0" x2="546.1" y2="334.0" stroke="var(--down)" class="wick"/>
<rect x="544.85" y="302.4" width="2.46" height="30.2" fill="var(--down)"/>
<line x1="550.0" y1="329.7" x2="550.0" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="333.6" width="2.46" height="10.4" fill="var(--down)"/>
<line x1="554.0" y1="263.8" x2="554.0" y2="331.6" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="312.8" width="2.46" height="15.6" fill="var(--up)"/>
<line x1="558.0" y1="300.1" x2="558.0" y2="334.9" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="309.7" width="2.46" height="11.1" fill="var(--down)"/>
<line x1="562.0" y1="302.1" x2="562.0" y2="360.0" stroke="var(--up)" class="wick"/>
<rect x="560.72" y="316.8" width="2.46" height="41.0" fill="var(--up)"/>
<line x1="565.9" y1="254.7" x2="565.9" y2="310.5" stroke="var(--up)" class="wick"/>
<rect x="564.69" y="290.5" width="2.46" height="19.9" fill="var(--up)"/>
<line x1="569.9" y1="234.0" x2="569.9" y2="289.1" stroke="var(--up)" class="wick"/>
<rect x="568.66" y="236.4" width="2.46" height="43.9" fill="var(--up)"/>
<line x1="573.9" y1="225.0" x2="573.9" y2="276.8" stroke="var(--down)" class="wick"/>
<rect x="572.63" y="242.0" width="2.46" height="31.1" fill="var(--down)"/>
<line x1="577.8" y1="229.4" x2="577.8" y2="268.8" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="241.7" width="2.46" height="27.0" fill="var(--up)"/>
<line x1="581.8" y1="229.0" x2="581.8" y2="280.5" stroke="var(--down)" class="wick"/>
<rect x="580.56" y="233.0" width="2.46" height="35.0" fill="var(--down)"/>
<line x1="585.8" y1="242.0" x2="585.8" y2="305.3" stroke="var(--down)" class="wick"/>
<rect x="584.53" y="255.7" width="2.46" height="33.7" fill="var(--down)"/>
<line x1="589.7" y1="291.8" x2="589.7" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="588.50" y="307.8" width="2.46" height="29.7" fill="var(--down)"/>
<line x1="593.7" y1="323.2" x2="593.7" y2="369.2" stroke="var(--down)" class="wick"/>
<rect x="592.47" y="327.2" width="2.46" height="37.7" fill="var(--down)"/>
<line x1="597.7" y1="357.0" x2="597.7" y2="379.8" stroke="var(--up)" class="wick"/>
<rect x="596.43" y="369.2" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="601.6" y1="354.3" x2="601.6" y2="394.2" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="368.2" width="2.46" height="21.8" fill="var(--down)"/>
<line x1="605.6" y1="409.7" x2="605.6" y2="446.2" stroke="var(--up)" class="wick"/>
<rect x="604.37" y="412.2" width="2.46" height="5.6" fill="var(--up)"/>
<line x1="609.6" y1="404.0" x2="609.6" y2="437.8" stroke="var(--up)" class="wick"/>
<rect x="608.34" y="421.1" width="2.46" height="2.2" fill="var(--up)"/>
<line x1="613.5" y1="417.8" x2="613.5" y2="449.4" stroke="var(--up)" class="wick"/>
<rect x="612.31" y="427.6" width="2.46" height="17.7" fill="var(--up)"/>
<line x1="617.5" y1="413.6" x2="617.5" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="420.5" width="2.46" height="22.5" fill="var(--down)"/>
<line x1="621.5" y1="446.0" x2="621.5" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="620.24" y="450.9" width="2.46" height="19.0" fill="var(--down)"/>
<line x1="625.4" y1="456.5" x2="625.4" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="624.21" y="465.2" width="2.46" height="9.0" fill="var(--up)"/>
<line x1="629.4" y1="442.3" x2="629.4" y2="466.8" stroke="var(--up)" class="wick"/>
<rect x="628.18" y="448.5" width="2.46" height="16.8" fill="var(--up)"/>
<line x1="633.4" y1="457.0" x2="633.4" y2="479.1" stroke="var(--up)" class="wick"/>
<rect x="632.15" y="468.2" width="2.46" height="7.8" fill="var(--up)"/>
<line x1="637.3" y1="448.6" x2="637.3" y2="479.2" stroke="var(--down)" class="wick"/>
<rect x="636.11" y="460.1" width="2.46" height="12.6" fill="var(--down)"/>
<line x1="641.3" y1="463.2" x2="641.3" y2="494.7" stroke="var(--down)" class="wick"/>
<rect x="640.08" y="469.7" width="2.46" height="18.4" fill="var(--down)"/>
<line x1="645.3" y1="459.2" x2="645.3" y2="480.1" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="461.3" width="2.46" height="9.7" fill="var(--up)"/>
<line x1="649.2" y1="440.4" x2="649.2" y2="472.3" stroke="var(--down)" class="wick"/>
<rect x="648.02" y="453.6" width="2.46" height="8.5" fill="var(--down)"/>
<line x1="653.2" y1="458.2" x2="653.2" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="651.99" y="460.3" width="2.46" height="6.8" fill="var(--up)"/>
<line x1="657.2" y1="430.4" x2="657.2" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="454.4" width="2.46" height="7.7" fill="var(--down)"/>
<line x1="661.2" y1="438.1" x2="661.2" y2="460.6" stroke="var(--down)" class="wick"/>
<rect x="659.92" y="448.5" width="2.46" height="5.1" fill="var(--down)"/>
<line x1="665.1" y1="398.1" x2="665.1" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="663.89" y="402.0" width="2.46" height="23.8" fill="var(--up)"/>
<line x1="669.1" y1="376.7" x2="669.1" y2="426.9" stroke="var(--up)" class="wick"/>
<rect x="667.86" y="387.1" width="2.46" height="36.1" fill="var(--up)"/>
<line x1="673.1" y1="392.3" x2="673.1" y2="430.7" stroke="var(--down)" class="wick"/>
<rect x="671.83" y="393.9" width="2.46" height="19.2" fill="var(--down)"/>
<line x1="677.0" y1="391.2" x2="677.0" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="675.79" y="404.8" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="681.0" y1="407.9" x2="681.0" y2="430.5" stroke="var(--up)" class="wick"/>
<rect x="679.76" y="417.7" width="2.46" height="1.3" fill="var(--up)"/>
<line x1="685.0" y1="430.5" x2="685.0" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="683.73" y="449.9" width="2.46" height="4.1" fill="var(--down)"/>
<line x1="688.9" y1="443.5" x2="688.9" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="687.70" y="447.7" width="2.46" height="21.1" fill="var(--up)"/>
<line x1="692.9" y1="438.0" x2="692.9" y2="467.2" stroke="var(--down)" class="wick"/>
<rect x="691.67" y="444.4" width="2.46" height="22.3" fill="var(--down)"/>
<line x1="696.9" y1="448.2" x2="696.9" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="695.63" y="451.5" width="2.46" height="5.4" fill="var(--down)"/>
<line x1="700.8" y1="447.8" x2="700.8" y2="480.1" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="449.4" width="2.46" height="11.0" fill="var(--down)"/>
<line x1="704.8" y1="460.4" x2="704.8" y2="483.4" stroke="var(--down)" class="wick"/>
<rect x="703.57" y="460.4" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="708.8" y1="449.5" x2="708.8" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="707.54" y="456.9" width="2.46" height="28.6" fill="var(--up)"/>
<line x1="712.7" y1="442.6" x2="712.7" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="711.51" y="448.6" width="2.46" height="8.5" fill="var(--down)"/>
<line x1="716.7" y1="429.8" x2="716.7" y2="462.0" stroke="var(--up)" class="wick"/>
<rect x="715.47" y="434.5" width="2.46" height="18.6" fill="var(--up)"/>
<line x1="720.7" y1="402.5" x2="720.7" y2="431.6" stroke="var(--up)" class="wick"/>
<rect x="719.44" y="403.3" width="2.46" height="22.7" fill="var(--up)"/>
<line x1="724.6" y1="403.3" x2="724.6" y2="438.7" stroke="var(--down)" class="wick"/>
<rect x="723.41" y="406.6" width="2.46" height="22.8" fill="var(--down)"/>
<line x1="728.6" y1="418.4" x2="728.6" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="727.38" y="418.4" width="2.46" height="27.1" fill="var(--down)"/>
<line x1="732.6" y1="439.5" x2="732.6" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="731.35" y="441.0" width="2.46" height="8.2" fill="var(--up)"/>
<line x1="736.5" y1="450.6" x2="736.5" y2="487.3" stroke="var(--down)" class="wick"/>
<rect x="735.31" y="456.9" width="2.46" height="27.5" fill="var(--down)"/>
<line x1="740.5" y1="483.8" x2="740.5" y2="510.2" stroke="var(--down)" class="wick"/>
<rect x="739.28" y="492.3" width="2.46" height="16.7" fill="var(--down)"/>
<line x1="744.5" y1="493.7" x2="744.5" y2="516.5" stroke="var(--up)" class="wick"/>
<rect x="743.25" y="496.8" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="748.4" y1="490.2" x2="748.4" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="747.22" y="493.7" width="2.46" height="10.9" fill="var(--down)"/>
<line x1="752.4" y1="499.1" x2="752.4" y2="519.8" stroke="var(--down)" class="wick"/>
<rect x="751.19" y="504.4" width="2.46" height="11.5" fill="var(--down)"/>
<line x1="756.4" y1="510.0" x2="756.4" y2="525.5" stroke="var(--down)" class="wick"/>
<rect x="755.15" y="521.1" width="2.46" height="1.9" fill="var(--down)"/>
<line x1="760.4" y1="511.4" x2="760.4" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="759.12" y="517.1" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="764.3" y1="494.8" x2="764.3" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="763.09" y="499.2" width="2.46" height="26.3" fill="var(--up)"/>
<line x1="768.3" y1="487.3" x2="768.3" y2="516.9" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="495.7" width="2.46" height="20.5" fill="var(--down)"/>
<line x1="772.3" y1="513.7" x2="772.3" y2="538.8" stroke="var(--down)" class="wick"/>
<rect x="771.03" y="516.2" width="2.46" height="21.1" fill="var(--down)"/>
<line x1="776.2" y1="538.5" x2="776.2" y2="563.8" stroke="var(--down)" class="wick"/>
<rect x="774.99" y="539.9" width="2.46" height="18.4" fill="var(--down)"/>
<line x1="780.2" y1="539.2" x2="780.2" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="778.96" y="550.0" width="2.46" height="11.1" fill="var(--down)"/>
<line x1="784.2" y1="554.3" x2="784.2" y2="583.7" stroke="var(--down)" class="wick"/>
<rect x="782.93" y="561.7" width="2.46" height="18.4" fill="var(--down)"/>
<line x1="788.1" y1="550.2" x2="788.1" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="786.90" y="558.4" width="2.46" height="21.8" fill="var(--up)"/>
<line x1="792.1" y1="546.5" x2="792.1" y2="579.4" stroke="var(--up)" class="wick"/>
<rect x="790.87" y="569.6" width="2.46" height="9.1" fill="var(--up)"/>
<line x1="796.1" y1="553.0" x2="796.1" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="794.83" y="563.7" width="2.46" height="12.0" fill="var(--up)"/>
<line x1="800.0" y1="560.2" x2="800.0" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="798.80" y="574.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="804.0" y1="562.6" x2="804.0" y2="589.2" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="578.4" width="2.46" height="3.1" fill="var(--down)"/>
<line x1="808.0" y1="559.3" x2="808.0" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="806.74" y="562.7" width="2.46" height="15.9" fill="var(--up)"/>
<line x1="811.9" y1="551.7" x2="811.9" y2="575.4" stroke="var(--down)" class="wick"/>
<rect x="810.71" y="558.9" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="815.9" y1="555.9" x2="815.9" y2="574.1" stroke="var(--up)" class="wick"/>
<rect x="814.67" y="560.7" width="2.46" height="8.2" fill="var(--up)"/>
<line x1="819.9" y1="549.1" x2="819.9" y2="566.5" stroke="var(--down)" class="wick"/>
<rect x="818.64" y="552.0" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="823.8" y1="530.2" x2="823.8" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="822.61" y="558.4" width="2.46" height="4.0" fill="var(--down)"/>
<line x1="827.8" y1="556.3" x2="827.8" y2="577.4" stroke="var(--down)" class="wick"/>
<rect x="826.58" y="567.2" width="2.46" height="7.0" fill="var(--down)"/>
<line x1="831.8" y1="504.2" x2="831.8" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="830.55" y="527.5" width="2.46" height="37.7" fill="var(--up)"/>
<line x1="835.7" y1="518.3" x2="835.7" y2="549.1" stroke="var(--down)" class="wick"/>
<rect x="834.51" y="525.4" width="2.46" height="22.8" fill="var(--down)"/>
<line x1="839.7" y1="528.8" x2="839.7" y2="545.3" stroke="var(--up)" class="wick"/>
<rect x="838.48" y="533.5" width="2.46" height="11.8" fill="var(--up)"/>
<line x1="843.7" y1="536.6" x2="843.7" y2="558.4" stroke="var(--down)" class="wick"/>
<rect x="842.45" y="544.9" width="2.46" height="12.0" fill="var(--down)"/>
<line x1="847.6" y1="542.0" x2="847.6" y2="562.7" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="548.4" width="2.46" height="4.6" fill="var(--up)"/>
<line x1="851.6" y1="535.1" x2="851.6" y2="562.0" stroke="var(--down)" class="wick"/>
<rect x="850.39" y="538.9" width="2.46" height="2.6" fill="var(--down)"/>
<line x1="855.6" y1="542.2" x2="855.6" y2="562.0" stroke="var(--down)" class="wick"/>
<rect x="854.35" y="548.0" width="2.46" height="7.9" fill="var(--down)"/>
<line x1="859.6" y1="555.2" x2="859.6" y2="607.0" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="560.0" width="2.46" height="17.9" fill="var(--down)"/>
<line x1="863.5" y1="562.5" x2="863.5" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="862.29" y="572.3" width="2.46" height="7.6" fill="var(--down)"/>
<line x1="867.5" y1="567.6" x2="867.5" y2="596.2" stroke="var(--up)" class="wick"/>
<rect x="866.26" y="570.8" width="2.46" height="9.1" fill="var(--up)"/>
<line x1="871.5" y1="542.7" x2="871.5" y2="580.4" stroke="var(--down)" class="wick"/>
<rect x="870.23" y="565.7" width="2.46" height="7.4" fill="var(--down)"/>
<line x1="875.4" y1="557.6" x2="875.4" y2="574.4" stroke="var(--up)" class="wick"/>
<rect x="874.19" y="566.1" width="2.46" height="2.4" fill="var(--up)"/>
<line x1="879.4" y1="542.9" x2="879.4" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="878.16" y="558.9" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="883.4" y1="565.2" x2="883.4" y2="588.7" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="565.2" width="2.46" height="16.6" fill="var(--down)"/>
<line x1="887.3" y1="558.8" x2="887.3" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="886.10" y="560.9" width="2.46" height="20.2" fill="var(--up)"/>
<line x1="891.3" y1="499.1" x2="891.3" y2="540.4" stroke="var(--up)" class="wick"/>
<rect x="890.07" y="502.1" width="2.46" height="32.5" fill="var(--up)"/>
<line x1="895.3" y1="487.7" x2="895.3" y2="523.8" stroke="var(--down)" class="wick"/>
<rect x="894.03" y="497.1" width="2.46" height="23.4" fill="var(--down)"/>
<line x1="899.2" y1="499.7" x2="899.2" y2="524.2" stroke="var(--down)" class="wick"/>
<rect x="898.00" y="513.0" width="2.46" height="10.2" fill="var(--down)"/>
<line x1="903.2" y1="513.5" x2="903.2" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="518.7" width="2.46" height="17.5" fill="var(--down)"/>
<line x1="907.2" y1="521.4" x2="907.2" y2="567.1" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="524.8" width="2.46" height="36.9" fill="var(--down)"/>
<line x1="911.1" y1="503.3" x2="911.1" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="909.91" y="511.2" width="2.46" height="6.4" fill="var(--up)"/>
<line x1="915.1" y1="497.1" x2="915.1" y2="535.2" stroke="var(--up)" class="wick"/>
<rect x="913.87" y="511.7" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="919.1" y1="489.3" x2="919.1" y2="516.4" stroke="var(--up)" class="wick"/>
<rect x="917.84" y="491.1" width="2.46" height="19.6" fill="var(--up)"/>
<line x1="923.0" y1="472.2" x2="923.0" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="921.81" y="483.1" width="2.46" height="7.0" fill="var(--up)"/>
<line x1="927.0" y1="491.6" x2="927.0" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="925.78" y="503.4" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="931.0" y1="492.3" x2="931.0" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="929.75" y="498.6" width="2.46" height="33.7" fill="var(--down)"/>
<line x1="934.9" y1="505.7" x2="934.9" y2="529.1" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="511.5" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="938.9" y1="493.8" x2="938.9" y2="522.2" stroke="var(--up)" class="wick"/>
<rect x="937.68" y="506.4" width="2.46" height="14.7" fill="var(--up)"/>
<line x1="942.9" y1="445.5" x2="942.9" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="941.65" y="445.9" width="2.46" height="45.2" fill="var(--up)"/>
<line x1="946.8" y1="429.0" x2="946.8" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="945.62" y="437.2" width="2.46" height="9.6" fill="var(--up)"/>
<line x1="950.8" y1="438.5" x2="950.8" y2="464.1" stroke="var(--down)" class="wick"/>
<rect x="949.59" y="443.1" width="2.46" height="19.2" fill="var(--down)"/>
<line x1="954.8" y1="472.8" x2="954.8" y2="488.8" stroke="var(--down)" class="wick"/>
<rect x="953.55" y="482.7" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="958.8" y1="469.9" x2="958.8" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="957.52" y="473.4" width="2.46" height="8.1" fill="var(--down)"/>
<line x1="962.7" y1="483.4" x2="962.7" y2="509.1" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="485.9" width="2.46" height="3.4" fill="var(--down)"/>
<line x1="966.7" y1="468.8" x2="966.7" y2="486.8" stroke="var(--up)" class="wick"/>
<rect x="965.46" y="472.9" width="2.46" height="2.7" fill="var(--up)"/>
<line x1="970.7" y1="452.4" x2="970.7" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="969.43" y="464.7" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="974.6" y1="449.5" x2="974.6" y2="494.8" stroke="var(--down)" class="wick"/>
<rect x="973.39" y="456.8" width="2.46" height="8.2" fill="var(--down)"/>
<line x1="978.6" y1="448.2" x2="978.6" y2="478.5" stroke="var(--up)" class="wick"/>
<rect x="977.36" y="464.7" width="2.46" height="6.7" fill="var(--up)"/>
<line x1="982.6" y1="454.4" x2="982.6" y2="485.7" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="461.7" width="2.46" height="2.8" fill="var(--up)"/>
<line x1="986.5" y1="466.1" x2="986.5" y2="484.2" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="482.9" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="990.5" y1="436.1" x2="990.5" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="989.27" y="458.6" width="2.46" height="17.3" fill="var(--up)"/>
<line x1="994.5" y1="436.2" x2="994.5" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="440.3" width="2.46" height="20.8" fill="var(--up)"/>
<line x1="998.4" y1="422.0" x2="998.4" y2="445.2" stroke="var(--down)" class="wick"/>
<rect x="997.20" y="436.4" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="1002.4" y1="419.6" x2="1002.4" y2="443.1" stroke="var(--down)" class="wick"/>
<rect x="1001.17" y="430.4" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="1006.4" y1="413.0" x2="1006.4" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="1005.14" y="414.9" width="2.46" height="20.9" fill="var(--up)"/>
<line x1="1010.3" y1="413.2" x2="1010.3" y2="426.8" stroke="var(--down)" class="wick"/>
<rect x="1009.11" y="417.3" width="2.46" height="6.0" fill="var(--down)"/>
<line x1="1014.3" y1="412.9" x2="1014.3" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="1013.07" y="419.1" width="2.46" height="7.7" fill="var(--down)"/>
<line x1="1018.3" y1="421.1" x2="1018.3" y2="449.4" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="421.1" width="2.46" height="20.4" fill="var(--down)"/>
<line x1="1022.2" y1="419.6" x2="1022.2" y2="456.3" stroke="var(--down)" class="wick"/>
<rect x="1021.01" y="433.9" width="2.46" height="4.0" fill="var(--down)"/>
<line x1="1026.2" y1="433.9" x2="1026.2" y2="464.2" stroke="var(--down)" class="wick"/>
<rect x="1024.98" y="436.0" width="2.46" height="21.9" fill="var(--down)"/>
<line x1="1030.2" y1="444.0" x2="1030.2" y2="481.3" stroke="var(--down)" class="wick"/>
<rect x="1028.95" y="444.8" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="1034.1" y1="455.6" x2="1034.1" y2="490.5" stroke="var(--down)" class="wick"/>
<rect x="1032.91" y="460.1" width="2.46" height="20.8" fill="var(--down)"/>
<line x1="1038.1" y1="459.1" x2="1038.1" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="1036.88" y="461.7" width="2.46" height="37.5" fill="var(--down)"/>
<line x1="1042.1" y1="472.8" x2="1042.1" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="1040.85" y="488.6" width="2.46" height="3.3" fill="var(--up)"/>
<line x1="1046.0" y1="495.7" x2="1046.0" y2="561.1" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="501.9" width="2.46" height="57.0" fill="var(--down)"/>
<line x1="1050.0" y1="557.1" x2="1050.0" y2="570.3" stroke="var(--up)" class="wick"/>
<rect x="1048.79" y="564.1" width="2.46" height="3.1" fill="var(--up)"/>
<line x1="60" y1="493.0" x2="1052" y2="493.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="496.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$94 R1</text>
<text x="1058" y="508.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="414.8" x2="1052" y2="414.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="418.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$100 R2</text>
<text x="1058" y="430.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="285.5" x2="1052" y2="285.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="289.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$110 R3</text>
<text x="1058" y="301.0" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="598.1" x2="1052" y2="598.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="592.1" font-size="11.5" fill="var(--support)" font-weight="600">$86 S1</text>
<text x="1058" y="604.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="564.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="556.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $88 (2026-09-17)</text>
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
| ------ | ------ | ----------- | ------ |
| R3 | $110 | 3 | 2025-10-01·10-21, 2026-03-02 고점대 — 1년 최고($126.62)와 현재가 사이의 중간 저항 |
| R2 | $100 | 3 | 2026-05-19·08-11·09-03 고점대 — **9월 하락 직전에 마지막으로 눌린 자리** |
| R1 | $94 | 3 | 2026-06-05·06-30·07-23 고점대 — 2026년 여름 박스 상단 |
| **현재가** | **$88.33** (2026-09-17 종가) | — | R1($94)과 S1($86) 사이. R1까지 +6.4%, S1까지 −2.6%로 **지지선에 더 가깝다** |
| S1 | $86 | 2 | 2026-06-18·07-10 저점대 — 터치 2회로 얇다. 1년 최저($84.99)와 1%밖에 떨어져 있지 않다 |
| 참고선 | $126.62 / $84.99 | — | 최근 1년 최고·최저. 최고가는 2026년 3월 구간이라 근시일 저항으로 보지 않고, 최저가는 S1과 사실상 같은 자리다 |

> 검출된 저항이 3개(R1~R3)인데 지지는 1개(S1)뿐이고 그 터치 횟수도 2회로 얇다. **현재가가 1년 저점권($84.99)에 붙어 있어 아래쪽에는 이 1년 창 안에 표본이 거의 없다는 뜻**이다. 더 아래 구조는 [주봉·5년 차트](./10_technical_weekly.md)에서 본다.

---

## 3. 관측된 특이 구간 — 2026-09-16 인수 종결 당일의 하락

- 9월 15일 종가 $94.23에서 16일 **$88.73**으로 하루 **−5.8%**, 9월 초 $96 부근에서 2026-09-18 종가 $87.49까지 약 **−9.5%**다.
- **같은 날 공시된 Twin Eagle 인수 종결은 호재성 발표였다** — 즉 이 하락은 회사 고유 악재 때문이 아니다. 동종 애팔래치아 E&P(Antero −2.1%·Range −1.7%)와 [EQT](../eqt/09_technical_daily.md)(−3.8%)가 함께 빠졌고, 가스 가격 약세發 섹터 디레이팅으로 읽는다([최근 뉴스 / 이슈](./08_news.md)).
- 이 하락으로 주가가 R1($94) 아래에서 S1($86) 쪽으로 내려붙었다. **거래 레짐이 재설정됐다고 볼 근거(갭·거래량 급증)는 확인되지 않아 기존 스윙 레벨을 참고선으로 격하하지 않고 그대로 뒀다.**

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-09-19~2026-09-17. 수집 시점: 2026-09-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py EXE --name "Expand Energy" --close-on 2026-09-17 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **마지막 봉이 2026-09-17이다.** 9월 18일 세션의 종가가 원자료에 아직 채워지지 않아 `--close-on 2026-09-17`로 고정했다 — 위 데이터 출처 블록 참고. 이 문서의 현재가($88.33)를 다른 문서의 기준 종가($87.49)로 옮겨 적지 말 것.
    - **S1의 터치 횟수가 2회로 표본이 얇다** — 이 레벨을 R1~R3와 같은 강도로 읽지 말 것.
    - 기간 내 배당이 4회 있었으나 **원주가(배당 미반영)**라 차트에 반영되지 않았다. 배당수익률이 연 2.6% 수준으로 EQT(1.3%)보다 높아, 총수익 관점에서는 이 차트가 실제 성과를 더 크게 과소평가한다.

---

*작성일: 2026-09-19*
