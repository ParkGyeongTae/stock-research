# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: 야후 파이낸스 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: ⚠️ **이 문서의 현재가만 다른 문서와 하루 어긋난다.** 야후 파이낸스 일봉 계열은 2026-08-28 봉이 비어 있어 마지막 완전한 일봉이 **2026-08-27 종가 $934.66**이다. 반면 주봉 계열·stockanalysis.com·[밸류에이션 / 적정주가](./06_valuation.md)는 **2026-08-28 종가 $945.47**을 쓴다(전일 대비 +1.16%로 두 값이 정합하므로 데이터 누락이지 계보 차이가 아니다). 차이는 1.2%로 아래 레벨 해석을 바꾸지 않는다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

<div class="cost-chart">
<style>
.cost-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .cost-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .cost-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.cost-chart svg { width:100%; height:auto; display:block; }
.cost-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.cost-chart .title { fill: var(--ink); font-weight:600; }
.cost-chart .grid { stroke: var(--grid); stroke-width:1; }
.cost-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Costco(COST) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Costco (COST) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $934.66 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="594.3" x2="1052" y2="594.3" class="grid"/>
<text x="52" y="598.3" font-size="11" text-anchor="end" fill="var(--muted)">850</text>
<line x1="60" y1="488.8" x2="1052" y2="488.8" class="grid"/>
<text x="52" y="492.8" font-size="11" text-anchor="end" fill="var(--muted)">900</text>
<line x1="60" y1="383.2" x2="1052" y2="383.2" class="grid"/>
<text x="52" y="387.2" font-size="11" text-anchor="end" fill="var(--muted)">950</text>
<line x1="60" y1="277.7" x2="1052" y2="277.7" class="grid"/>
<text x="52" y="281.7" font-size="11" text-anchor="end" fill="var(--muted)">1,000</text>
<line x1="60" y1="172.1" x2="1052" y2="172.1" class="grid"/>
<text x="52" y="176.1" font-size="11" text-anchor="end" fill="var(--muted)">1,050</text>
<line x1="60" y1="66.6" x2="1052" y2="66.6" class="grid"/>
<text x="52" y="70.6" font-size="11" text-anchor="end" fill="var(--muted)">1,100</text>
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
<line x1="62.0" y1="386.2" x2="62.0" y2="403.4" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="393.8" width="2.46" height="3.5" fill="var(--down)"/>
<line x1="66.0" y1="394.8" x2="66.0" y2="411.6" stroke="var(--up)" class="wick"/>
<rect x="64.72" y="406.8" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="69.9" y1="383.0" x2="69.9" y2="411.7" stroke="var(--up)" class="wick"/>
<rect x="68.69" y="383.7" width="2.46" height="22.8" fill="var(--up)"/>
<line x1="73.9" y1="363.2" x2="73.9" y2="380.9" stroke="var(--up)" class="wick"/>
<rect x="72.66" y="370.8" width="2.46" height="5.3" fill="var(--up)"/>
<line x1="77.9" y1="342.0" x2="77.9" y2="370.1" stroke="var(--up)" class="wick"/>
<rect x="76.63" y="354.8" width="2.46" height="10.1" fill="var(--up)"/>
<line x1="81.8" y1="336.1" x2="81.8" y2="365.1" stroke="var(--up)" class="wick"/>
<rect x="80.59" y="337.1" width="2.46" height="17.1" fill="var(--up)"/>
<line x1="85.8" y1="320.2" x2="85.8" y2="355.5" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="321.5" width="2.46" height="19.5" fill="var(--up)"/>
<line x1="89.8" y1="317.8" x2="89.8" y2="374.9" stroke="var(--down)" class="wick"/>
<rect x="88.53" y="327.5" width="2.46" height="42.4" fill="var(--down)"/>
<line x1="93.7" y1="351.2" x2="93.7" y2="374.2" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="353.0" width="2.46" height="13.8" fill="var(--up)"/>
<line x1="97.7" y1="341.9" x2="97.7" y2="362.1" stroke="var(--up)" class="wick"/>
<rect x="96.47" y="345.4" width="2.46" height="16.1" fill="var(--up)"/>
<line x1="101.7" y1="341.5" x2="101.7" y2="362.7" stroke="var(--down)" class="wick"/>
<rect x="100.43" y="345.6" width="2.46" height="16.3" fill="var(--down)"/>
<line x1="105.6" y1="363.0" x2="105.6" y2="381.5" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="364.0" width="2.46" height="14.8" fill="var(--down)"/>
<line x1="109.6" y1="353.7" x2="109.6" y2="375.9" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="355.7" width="2.46" height="20.1" fill="var(--up)"/>
<line x1="113.6" y1="356.7" x2="113.6" y2="381.8" stroke="var(--down)" class="wick"/>
<rect x="112.34" y="367.7" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="117.5" y1="367.5" x2="117.5" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="116.31" y="372.7" width="2.46" height="8.1" fill="var(--down)"/>
<line x1="121.5" y1="383.2" x2="121.5" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="120.27" y="388.8" width="2.46" height="8.7" fill="var(--down)"/>
<line x1="125.5" y1="393.8" x2="125.5" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="124.24" y="396.7" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="129.4" y1="375.5" x2="129.4" y2="397.8" stroke="var(--up)" class="wick"/>
<rect x="128.21" y="393.2" width="2.46" height="2.1" fill="var(--up)"/>
<line x1="133.4" y1="376.9" x2="133.4" y2="413.6" stroke="var(--down)" class="wick"/>
<rect x="132.18" y="378.0" width="2.46" height="19.3" fill="var(--down)"/>
<line x1="137.4" y1="430.4" x2="137.4" y2="478.1" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="434.8" width="2.46" height="20.3" fill="var(--down)"/>
<line x1="141.3" y1="452.4" x2="141.3" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="140.11" y="453.2" width="2.46" height="1.1" fill="var(--up)"/>
<line x1="145.3" y1="424.4" x2="145.3" y2="460.6" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="434.7" width="2.46" height="19.8" fill="var(--up)"/>
<line x1="149.3" y1="438.1" x2="149.3" y2="465.2" stroke="var(--down)" class="wick"/>
<rect x="148.05" y="440.2" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="153.2" y1="449.7" x2="153.2" y2="467.6" stroke="var(--up)" class="wick"/>
<rect x="152.02" y="453.4" width="2.46" height="8.9" fill="var(--up)"/>
<line x1="157.2" y1="450.6" x2="157.2" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="155.99" y="455.9" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="161.2" y1="455.5" x2="161.2" y2="479.8" stroke="var(--down)" class="wick"/>
<rect x="159.95" y="456.1" width="2.46" height="9.6" fill="var(--down)"/>
<line x1="165.2" y1="451.5" x2="165.2" y2="480.6" stroke="var(--up)" class="wick"/>
<rect x="163.92" y="457.5" width="2.46" height="12.8" fill="var(--up)"/>
<line x1="169.1" y1="454.2" x2="169.1" y2="465.6" stroke="var(--up)" class="wick"/>
<rect x="167.89" y="457.5" width="2.46" height="4.8" fill="var(--up)"/>
<line x1="173.1" y1="396.4" x2="173.1" y2="431.2" stroke="var(--up)" class="wick"/>
<rect x="171.86" y="398.2" width="2.46" height="22.3" fill="var(--up)"/>
<line x1="177.1" y1="392.8" x2="177.1" y2="427.6" stroke="var(--down)" class="wick"/>
<rect x="175.83" y="395.0" width="2.46" height="30.4" fill="var(--down)"/>
<line x1="181.0" y1="412.8" x2="181.0" y2="440.2" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="413.7" width="2.46" height="13.8" fill="var(--up)"/>
<line x1="185.0" y1="388.7" x2="185.0" y2="412.9" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="390.6" width="2.46" height="13.2" fill="var(--up)"/>
<line x1="189.0" y1="353.7" x2="189.0" y2="393.2" stroke="var(--up)" class="wick"/>
<rect x="187.73" y="372.7" width="2.46" height="19.0" fill="var(--up)"/>
<line x1="192.9" y1="366.5" x2="192.9" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="191.70" y="371.5" width="2.46" height="63.2" fill="var(--down)"/>
<line x1="196.9" y1="406.8" x2="196.9" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="195.67" y="412.1" width="2.46" height="14.3" fill="var(--up)"/>
<line x1="200.9" y1="404.8" x2="200.9" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="199.63" y="412.4" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="204.8" y1="397.2" x2="204.8" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="203.60" y="409.6" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="208.8" y1="376.9" x2="208.8" y2="420.2" stroke="var(--up)" class="wick"/>
<rect x="207.57" y="394.5" width="2.46" height="9.9" fill="var(--up)"/>
<line x1="212.8" y1="392.8" x2="212.8" y2="416.0" stroke="var(--down)" class="wick"/>
<rect x="211.54" y="392.8" width="2.46" height="7.2" fill="var(--down)"/>
<line x1="216.7" y1="398.0" x2="216.7" y2="425.1" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="404.3" width="2.46" height="16.6" fill="var(--down)"/>
<line x1="220.7" y1="418.7" x2="220.7" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="219.47" y="425.0" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="224.7" y1="423.9" x2="224.7" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="223.44" y="432.1" width="2.46" height="5.7" fill="var(--down)"/>
<line x1="228.6" y1="446.8" x2="228.6" y2="469.1" stroke="var(--down)" class="wick"/>
<rect x="227.41" y="448.7" width="2.46" height="13.9" fill="var(--down)"/>
<line x1="232.6" y1="440.2" x2="232.6" y2="466.9" stroke="var(--up)" class="wick"/>
<rect x="231.38" y="446.2" width="2.46" height="15.8" fill="var(--up)"/>
<line x1="236.6" y1="446.6" x2="236.6" y2="468.3" stroke="var(--down)" class="wick"/>
<rect x="235.35" y="454.6" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="240.5" y1="427.2" x2="240.5" y2="471.1" stroke="var(--up)" class="wick"/>
<rect x="239.31" y="429.6" width="2.46" height="33.0" fill="var(--up)"/>
<line x1="244.5" y1="401.9" x2="244.5" y2="427.6" stroke="var(--up)" class="wick"/>
<rect x="243.28" y="402.8" width="2.46" height="15.9" fill="var(--up)"/>
<line x1="248.5" y1="393.2" x2="248.5" y2="430.8" stroke="var(--down)" class="wick"/>
<rect x="247.25" y="404.3" width="2.46" height="10.5" fill="var(--down)"/>
<line x1="252.4" y1="436.0" x2="252.4" y2="471.3" stroke="var(--down)" class="wick"/>
<rect x="251.22" y="437.4" width="2.46" height="1.6" fill="var(--down)"/>
<line x1="256.4" y1="410.7" x2="256.4" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="255.19" y="426.4" width="2.46" height="14.3" fill="var(--down)"/>
<line x1="260.4" y1="442.3" x2="260.4" y2="469.6" stroke="var(--down)" class="wick"/>
<rect x="259.15" y="448.7" width="2.46" height="7.3" fill="var(--down)"/>
<line x1="264.4" y1="448.9" x2="264.4" y2="461.3" stroke="var(--down)" class="wick"/>
<rect x="263.12" y="453.9" width="2.46" height="5.6" fill="var(--down)"/>
<line x1="268.3" y1="450.6" x2="268.3" y2="464.1" stroke="var(--down)" class="wick"/>
<rect x="267.09" y="456.1" width="2.46" height="3.1" fill="var(--down)"/>
<line x1="272.3" y1="432.3" x2="272.3" y2="464.0" stroke="var(--up)" class="wick"/>
<rect x="271.06" y="435.8" width="2.46" height="18.4" fill="var(--up)"/>
<line x1="276.3" y1="427.8" x2="276.3" y2="456.9" stroke="var(--down)" class="wick"/>
<rect x="275.03" y="431.5" width="2.46" height="8.8" fill="var(--down)"/>
<line x1="280.2" y1="436.2" x2="280.2" y2="470.2" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="442.3" width="2.46" height="19.9" fill="var(--down)"/>
<line x1="284.2" y1="448.9" x2="284.2" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="282.96" y="462.2" width="2.46" height="37.0" fill="var(--down)"/>
<line x1="288.2" y1="499.3" x2="288.2" y2="543.7" stroke="var(--down)" class="wick"/>
<rect x="286.93" y="499.3" width="2.46" height="9.3" fill="var(--down)"/>
<line x1="292.1" y1="479.1" x2="292.1" y2="507.8" stroke="var(--down)" class="wick"/>
<rect x="290.90" y="502.5" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="296.1" y1="477.5" x2="296.1" y2="505.4" stroke="var(--up)" class="wick"/>
<rect x="294.87" y="490.9" width="2.46" height="9.5" fill="var(--up)"/>
<line x1="300.1" y1="485.9" x2="300.1" y2="528.2" stroke="var(--down)" class="wick"/>
<rect x="298.83" y="490.9" width="2.46" height="27.2" fill="var(--down)"/>
<line x1="304.0" y1="497.8" x2="304.0" y2="520.2" stroke="var(--up)" class="wick"/>
<rect x="302.80" y="500.7" width="2.46" height="16.2" fill="var(--up)"/>
<line x1="308.0" y1="463.4" x2="308.0" y2="498.0" stroke="var(--up)" class="wick"/>
<rect x="306.77" y="471.3" width="2.46" height="25.8" fill="var(--up)"/>
<line x1="312.0" y1="458.8" x2="312.0" y2="482.4" stroke="var(--up)" class="wick"/>
<rect x="310.74" y="460.1" width="2.46" height="18.1" fill="var(--up)"/>
<line x1="315.9" y1="449.6" x2="315.9" y2="475.7" stroke="var(--down)" class="wick"/>
<rect x="314.71" y="460.9" width="2.46" height="2.6" fill="var(--down)"/>
<line x1="319.9" y1="440.2" x2="319.9" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="318.67" y="442.3" width="2.46" height="21.3" fill="var(--up)"/>
<line x1="323.9" y1="433.2" x2="323.9" y2="455.0" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="441.8" width="2.46" height="3.1" fill="var(--up)"/>
<line x1="327.8" y1="472.0" x2="327.8" y2="513.9" stroke="var(--down)" class="wick"/>
<rect x="326.61" y="473.9" width="2.46" height="23.6" fill="var(--down)"/>
<line x1="331.8" y1="476.3" x2="331.8" y2="503.6" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="494.6" width="2.46" height="5.4" fill="var(--down)"/>
<line x1="335.8" y1="501.4" x2="335.8" y2="524.9" stroke="var(--down)" class="wick"/>
<rect x="334.55" y="502.5" width="2.46" height="12.6" fill="var(--down)"/>
<line x1="339.7" y1="512.0" x2="339.7" y2="527.8" stroke="var(--up)" class="wick"/>
<rect x="338.51" y="513.2" width="2.46" height="3.4" fill="var(--up)"/>
<line x1="343.7" y1="510.8" x2="343.7" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="342.48" y="514.5" width="2.46" height="28.3" fill="var(--down)"/>
<line x1="347.7" y1="518.3" x2="347.7" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="346.45" y="521.5" width="2.46" height="18.2" fill="var(--up)"/>
<line x1="351.6" y1="512.8" x2="351.6" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="350.42" y="521.6" width="2.46" height="2.5" fill="var(--up)"/>
<line x1="355.6" y1="515.2" x2="355.6" y2="591.4" stroke="var(--down)" class="wick"/>
<rect x="354.39" y="526.5" width="2.46" height="45.5" fill="var(--down)"/>
<line x1="359.6" y1="565.6" x2="359.6" y2="606.9" stroke="var(--up)" class="wick"/>
<rect x="358.35" y="572.4" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="363.6" y1="555.1" x2="363.6" y2="577.0" stroke="var(--up)" class="wick"/>
<rect x="362.32" y="567.6" width="2.46" height="8.8" fill="var(--up)"/>
<line x1="367.5" y1="566.6" x2="367.5" y2="589.0" stroke="var(--down)" class="wick"/>
<rect x="366.29" y="572.6" width="2.46" height="5.7" fill="var(--down)"/>
<line x1="371.5" y1="576.5" x2="371.5" y2="595.8" stroke="var(--down)" class="wick"/>
<rect x="370.26" y="580.5" width="2.46" height="2.0" fill="var(--down)"/>
<line x1="375.5" y1="582.7" x2="375.5" y2="600.0" stroke="var(--down)" class="wick"/>
<rect x="374.23" y="585.9" width="2.46" height="8.4" fill="var(--down)"/>
<line x1="379.4" y1="583.8" x2="379.4" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="378.19" y="584.2" width="2.46" height="12.0" fill="var(--up)"/>
<line x1="383.4" y1="539.4" x2="383.4" y2="576.7" stroke="var(--up)" class="wick"/>
<rect x="382.16" y="548.2" width="2.46" height="28.0" fill="var(--up)"/>
<line x1="387.4" y1="536.1" x2="387.4" y2="554.2" stroke="var(--up)" class="wick"/>
<rect x="386.13" y="545.0" width="2.46" height="5.7" fill="var(--up)"/>
<line x1="391.3" y1="542.6" x2="391.3" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="390.10" y="545.2" width="2.46" height="11.5" fill="var(--down)"/>
<line x1="395.3" y1="556.7" x2="395.3" y2="570.2" stroke="var(--up)" class="wick"/>
<rect x="394.07" y="561.3" width="2.46" height="3.5" fill="var(--up)"/>
<line x1="399.3" y1="556.3" x2="399.3" y2="570.4" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="563.6" width="2.46" height="4.7" fill="var(--down)"/>
<line x1="403.2" y1="566.7" x2="403.2" y2="589.1" stroke="var(--down)" class="wick"/>
<rect x="402.00" y="570.8" width="2.46" height="14.0" fill="var(--down)"/>
<line x1="407.2" y1="533.6" x2="407.2" y2="571.4" stroke="var(--up)" class="wick"/>
<rect x="405.97" y="540.0" width="2.46" height="24.9" fill="var(--up)"/>
<line x1="411.2" y1="501.3" x2="411.2" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="409.94" y="511.8" width="2.46" height="27.8" fill="var(--up)"/>
<line x1="415.1" y1="502.3" x2="415.1" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="413.91" y="505.7" width="2.46" height="19.9" fill="var(--down)"/>
<line x1="419.1" y1="421.9" x2="419.1" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="417.87" y="456.5" width="2.46" height="29.9" fill="var(--up)"/>
<line x1="423.1" y1="425.8" x2="423.1" y2="464.9" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="436.3" width="2.46" height="18.8" fill="var(--up)"/>
<line x1="427.0" y1="394.1" x2="427.0" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="425.81" y="397.8" width="2.46" height="47.9" fill="var(--up)"/>
<line x1="431.0" y1="398.2" x2="431.0" y2="426.3" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="400.3" width="2.46" height="8.3" fill="var(--up)"/>
<line x1="435.0" y1="371.4" x2="435.0" y2="407.9" stroke="var(--up)" class="wick"/>
<rect x="433.75" y="381.2" width="2.46" height="26.7" fill="var(--up)"/>
<line x1="438.9" y1="365.7" x2="438.9" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="437.71" y="369.0" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="442.9" y1="351.6" x2="442.9" y2="381.1" stroke="var(--up)" class="wick"/>
<rect x="441.68" y="354.5" width="2.46" height="3.4" fill="var(--up)"/>
<line x1="446.9" y1="341.2" x2="446.9" y2="374.5" stroke="var(--up)" class="wick"/>
<rect x="445.65" y="353.1" width="2.46" height="12.4" fill="var(--up)"/>
<line x1="450.8" y1="299.5" x2="450.8" y2="363.0" stroke="var(--up)" class="wick"/>
<rect x="449.62" y="313.9" width="2.46" height="49.1" fill="var(--up)"/>
<line x1="454.8" y1="311.4" x2="454.8" y2="337.7" stroke="var(--down)" class="wick"/>
<rect x="453.59" y="324.3" width="2.46" height="3.6" fill="var(--down)"/>
<line x1="458.8" y1="309.7" x2="458.8" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="457.55" y="313.0" width="2.46" height="24.9" fill="var(--up)"/>
<line x1="462.8" y1="292.4" x2="462.8" y2="327.6" stroke="var(--down)" class="wick"/>
<rect x="461.52" y="306.3" width="2.46" height="18.5" fill="var(--down)"/>
<line x1="466.7" y1="324.1" x2="466.7" y2="358.5" stroke="var(--down)" class="wick"/>
<rect x="465.49" y="324.8" width="2.46" height="15.6" fill="var(--down)"/>
<line x1="470.7" y1="340.8" x2="470.7" y2="371.4" stroke="var(--down)" class="wick"/>
<rect x="469.46" y="342.0" width="2.46" height="18.4" fill="var(--down)"/>
<line x1="474.7" y1="361.5" x2="474.7" y2="386.4" stroke="var(--down)" class="wick"/>
<rect x="473.43" y="366.4" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="478.6" y1="380.9" x2="478.6" y2="424.8" stroke="var(--down)" class="wick"/>
<rect x="477.39" y="385.7" width="2.46" height="18.1" fill="var(--down)"/>
<line x1="482.6" y1="340.3" x2="482.6" y2="422.8" stroke="var(--up)" class="wick"/>
<rect x="481.36" y="344.5" width="2.46" height="50.9" fill="var(--up)"/>
<line x1="486.6" y1="297.4" x2="486.6" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="485.33" y="324.3" width="2.46" height="28.6" fill="var(--up)"/>
<line x1="490.5" y1="289.1" x2="490.5" y2="330.0" stroke="var(--down)" class="wick"/>
<rect x="489.30" y="312.9" width="2.46" height="10.5" fill="var(--down)"/>
<line x1="494.5" y1="275.7" x2="494.5" y2="304.4" stroke="var(--down)" class="wick"/>
<rect x="493.27" y="287.2" width="2.46" height="13.1" fill="var(--down)"/>
<line x1="498.5" y1="274.8" x2="498.5" y2="312.5" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="275.2" width="2.46" height="27.5" fill="var(--up)"/>
<line x1="502.4" y1="257.4" x2="502.4" y2="293.1" stroke="var(--down)" class="wick"/>
<rect x="501.20" y="274.9" width="2.46" height="7.9" fill="var(--down)"/>
<line x1="506.4" y1="283.0" x2="506.4" y2="343.1" stroke="var(--down)" class="wick"/>
<rect x="505.17" y="286.1" width="2.46" height="52.3" fill="var(--down)"/>
<line x1="510.4" y1="299.7" x2="510.4" y2="347.1" stroke="var(--up)" class="wick"/>
<rect x="509.14" y="323.8" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="514.3" y1="258.2" x2="514.3" y2="323.8" stroke="var(--up)" class="wick"/>
<rect x="513.11" y="280.1" width="2.46" height="42.5" fill="var(--up)"/>
<line x1="518.3" y1="229.4" x2="518.3" y2="290.8" stroke="var(--up)" class="wick"/>
<rect x="517.07" y="238.7" width="2.46" height="39.0" fill="var(--up)"/>
<line x1="522.3" y1="217.6" x2="522.3" y2="255.5" stroke="var(--down)" class="wick"/>
<rect x="521.04" y="230.5" width="2.46" height="21.7" fill="var(--down)"/>
<line x1="526.2" y1="243.9" x2="526.2" y2="291.4" stroke="var(--down)" class="wick"/>
<rect x="525.01" y="256.6" width="2.46" height="29.4" fill="var(--down)"/>
<line x1="530.2" y1="261.1" x2="530.2" y2="311.2" stroke="var(--down)" class="wick"/>
<rect x="528.98" y="293.9" width="2.46" height="9.5" fill="var(--down)"/>
<line x1="534.2" y1="304.3" x2="534.2" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="532.95" y="308.8" width="2.46" height="4.5" fill="var(--up)"/>
<line x1="538.1" y1="296.0" x2="538.1" y2="324.0" stroke="var(--up)" class="wick"/>
<rect x="536.91" y="307.2" width="2.46" height="8.9" fill="var(--up)"/>
<line x1="542.1" y1="280.0" x2="542.1" y2="309.2" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="281.0" width="2.46" height="25.4" fill="var(--up)"/>
<line x1="546.1" y1="272.4" x2="546.1" y2="295.7" stroke="var(--down)" class="wick"/>
<rect x="544.85" y="282.6" width="2.46" height="6.2" fill="var(--down)"/>
<line x1="550.0" y1="266.0" x2="550.0" y2="312.4" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="284.2" width="2.46" height="21.5" fill="var(--down)"/>
<line x1="554.0" y1="247.7" x2="554.0" y2="299.7" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="254.9" width="2.46" height="42.8" fill="var(--up)"/>
<line x1="558.0" y1="233.7" x2="558.0" y2="272.4" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="254.6" width="2.46" height="17.2" fill="var(--down)"/>
<line x1="562.0" y1="244.4" x2="562.0" y2="276.3" stroke="var(--up)" class="wick"/>
<rect x="560.72" y="261.3" width="2.46" height="11.0" fill="var(--up)"/>
<line x1="565.9" y1="248.1" x2="565.9" y2="284.0" stroke="var(--up)" class="wick"/>
<rect x="564.69" y="263.4" width="2.46" height="3.7" fill="var(--up)"/>
<line x1="569.9" y1="279.2" x2="569.9" y2="322.4" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="285.1" width="2.46" height="29.4" fill="var(--down)"/>
<line x1="573.9" y1="272.4" x2="573.9" y2="361.1" stroke="var(--up)" class="wick"/>
<rect x="572.63" y="281.7" width="2.46" height="65.6" fill="var(--up)"/>
<line x1="577.8" y1="262.0" x2="577.8" y2="303.0" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="266.5" width="2.46" height="12.0" fill="var(--up)"/>
<line x1="581.8" y1="256.3" x2="581.8" y2="286.1" stroke="var(--down)" class="wick"/>
<rect x="580.56" y="276.6" width="2.46" height="6.6" fill="var(--down)"/>
<line x1="585.8" y1="283.2" x2="585.8" y2="303.2" stroke="var(--down)" class="wick"/>
<rect x="584.53" y="285.4" width="2.46" height="8.6" fill="var(--down)"/>
<line x1="589.7" y1="264.6" x2="589.7" y2="311.4" stroke="var(--up)" class="wick"/>
<rect x="588.50" y="270.7" width="2.46" height="31.1" fill="var(--up)"/>
<line x1="593.7" y1="250.6" x2="593.7" y2="273.4" stroke="var(--up)" class="wick"/>
<rect x="592.47" y="259.9" width="2.46" height="5.3" fill="var(--up)"/>
<line x1="597.7" y1="251.0" x2="597.7" y2="287.3" stroke="var(--down)" class="wick"/>
<rect x="596.43" y="255.5" width="2.46" height="18.5" fill="var(--down)"/>
<line x1="601.6" y1="260.6" x2="601.6" y2="288.8" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="264.0" width="2.46" height="21.8" fill="var(--down)"/>
<line x1="605.6" y1="290.4" x2="605.6" y2="323.8" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="298.0" width="2.46" height="22.1" fill="var(--down)"/>
<line x1="609.6" y1="301.3" x2="609.6" y2="340.1" stroke="var(--down)" class="wick"/>
<rect x="608.34" y="307.6" width="2.46" height="23.3" fill="var(--down)"/>
<line x1="613.5" y1="318.3" x2="613.5" y2="339.9" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="330.3" width="2.46" height="5.8" fill="var(--down)"/>
<line x1="617.5" y1="305.9" x2="617.5" y2="352.5" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="307.9" width="2.46" height="42.1" fill="var(--down)"/>
<line x1="621.5" y1="317.2" x2="621.5" y2="360.0" stroke="var(--up)" class="wick"/>
<rect x="620.24" y="332.9" width="2.46" height="24.8" fill="var(--up)"/>
<line x1="625.4" y1="318.2" x2="625.4" y2="345.1" stroke="var(--down)" class="wick"/>
<rect x="624.21" y="324.1" width="2.46" height="6.6" fill="var(--down)"/>
<line x1="629.4" y1="304.7" x2="629.4" y2="335.3" stroke="var(--up)" class="wick"/>
<rect x="628.18" y="320.6" width="2.46" height="8.4" fill="var(--up)"/>
<line x1="633.4" y1="304.9" x2="633.4" y2="323.9" stroke="var(--up)" class="wick"/>
<rect x="632.15" y="311.7" width="2.46" height="3.9" fill="var(--up)"/>
<line x1="637.3" y1="266.0" x2="637.3" y2="309.3" stroke="var(--up)" class="wick"/>
<rect x="636.11" y="284.9" width="2.46" height="18.9" fill="var(--up)"/>
<line x1="641.3" y1="259.5" x2="641.3" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="640.08" y="284.0" width="2.46" height="1.2" fill="var(--down)"/>
<line x1="645.3" y1="271.1" x2="645.3" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="284.9" width="2.46" height="3.2" fill="var(--up)"/>
<line x1="649.2" y1="243.9" x2="649.2" y2="279.3" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="246.1" width="2.46" height="14.7" fill="var(--up)"/>
<line x1="653.2" y1="234.0" x2="653.2" y2="269.2" stroke="var(--up)" class="wick"/>
<rect x="651.99" y="238.5" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="657.2" y1="233.6" x2="657.2" y2="267.4" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="234.9" width="2.46" height="14.9" fill="var(--down)"/>
<line x1="661.2" y1="213.4" x2="661.2" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="659.92" y="213.8" width="2.46" height="54.5" fill="var(--up)"/>
<line x1="665.1" y1="202.0" x2="665.1" y2="224.8" stroke="var(--up)" class="wick"/>
<rect x="663.89" y="210.0" width="2.46" height="5.4" fill="var(--up)"/>
<line x1="669.1" y1="216.4" x2="669.1" y2="287.2" stroke="var(--down)" class="wick"/>
<rect x="667.86" y="221.7" width="2.46" height="59.2" fill="var(--down)"/>
<line x1="673.1" y1="277.6" x2="673.1" y2="321.2" stroke="var(--down)" class="wick"/>
<rect x="671.83" y="280.9" width="2.46" height="37.2" fill="var(--down)"/>
<line x1="677.0" y1="324.9" x2="677.0" y2="349.4" stroke="var(--up)" class="wick"/>
<rect x="675.79" y="330.9" width="2.46" height="2.4" fill="var(--up)"/>
<line x1="681.0" y1="308.5" x2="681.0" y2="344.6" stroke="var(--up)" class="wick"/>
<rect x="679.76" y="309.9" width="2.46" height="30.5" fill="var(--up)"/>
<line x1="685.0" y1="286.6" x2="685.0" y2="316.5" stroke="var(--up)" class="wick"/>
<rect x="683.73" y="304.7" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="688.9" y1="276.3" x2="688.9" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="687.70" y="277.9" width="2.46" height="31.4" fill="var(--up)"/>
<line x1="692.9" y1="253.8" x2="692.9" y2="290.0" stroke="var(--down)" class="wick"/>
<rect x="691.67" y="269.5" width="2.46" height="12.7" fill="var(--down)"/>
<line x1="696.9" y1="263.9" x2="696.9" y2="305.7" stroke="var(--up)" class="wick"/>
<rect x="695.63" y="265.4" width="2.46" height="24.2" fill="var(--up)"/>
<line x1="700.8" y1="260.5" x2="700.8" y2="281.3" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="267.2" width="2.46" height="2.7" fill="var(--down)"/>
<line x1="704.8" y1="242.6" x2="704.8" y2="262.8" stroke="var(--up)" class="wick"/>
<rect x="703.57" y="247.3" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="708.8" y1="249.3" x2="708.8" y2="272.4" stroke="var(--down)" class="wick"/>
<rect x="707.54" y="252.3" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="712.7" y1="247.2" x2="712.7" y2="284.8" stroke="var(--down)" class="wick"/>
<rect x="711.51" y="259.4" width="2.46" height="22.4" fill="var(--down)"/>
<line x1="716.7" y1="251.0" x2="716.7" y2="307.2" stroke="var(--down)" class="wick"/>
<rect x="715.47" y="255.5" width="2.46" height="34.8" fill="var(--down)"/>
<line x1="720.7" y1="279.8" x2="720.7" y2="309.1" stroke="var(--up)" class="wick"/>
<rect x="719.44" y="280.5" width="2.46" height="21.7" fill="var(--up)"/>
<line x1="724.6" y1="240.3" x2="724.6" y2="285.4" stroke="var(--up)" class="wick"/>
<rect x="723.41" y="247.0" width="2.46" height="38.2" fill="var(--up)"/>
<line x1="728.6" y1="211.7" x2="728.6" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="727.38" y="245.2" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="732.6" y1="225.5" x2="732.6" y2="273.0" stroke="var(--up)" class="wick"/>
<rect x="731.35" y="250.7" width="2.46" height="12.2" fill="var(--up)"/>
<line x1="736.5" y1="233.8" x2="736.5" y2="258.5" stroke="var(--up)" class="wick"/>
<rect x="735.31" y="243.0" width="2.46" height="12.5" fill="var(--up)"/>
<line x1="740.5" y1="251.8" x2="740.5" y2="293.7" stroke="var(--down)" class="wick"/>
<rect x="739.28" y="253.8" width="2.46" height="32.8" fill="var(--down)"/>
<line x1="744.5" y1="250.9" x2="744.5" y2="297.4" stroke="var(--up)" class="wick"/>
<rect x="743.25" y="252.2" width="2.46" height="39.2" fill="var(--up)"/>
<line x1="748.4" y1="243.9" x2="748.4" y2="266.9" stroke="var(--down)" class="wick"/>
<rect x="747.22" y="252.9" width="2.46" height="6.2" fill="var(--down)"/>
<line x1="752.4" y1="262.9" x2="752.4" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="751.19" y="265.4" width="2.46" height="13.4" fill="var(--down)"/>
<line x1="756.4" y1="222.8" x2="756.4" y2="275.3" stroke="var(--up)" class="wick"/>
<rect x="755.15" y="231.5" width="2.46" height="40.8" fill="var(--up)"/>
<line x1="760.4" y1="187.9" x2="760.4" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="759.12" y="207.8" width="2.46" height="32.0" fill="var(--up)"/>
<line x1="764.3" y1="189.4" x2="764.3" y2="222.6" stroke="var(--up)" class="wick"/>
<rect x="763.09" y="190.6" width="2.46" height="13.3" fill="var(--up)"/>
<line x1="768.3" y1="156.3" x2="768.3" y2="194.9" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="173.5" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="772.3" y1="109.1" x2="772.3" y2="182.7" stroke="var(--up)" class="wick"/>
<rect x="771.03" y="116.2" width="2.46" height="55.9" fill="var(--up)"/>
<line x1="776.2" y1="73.9" x2="776.2" y2="125.5" stroke="var(--up)" class="wick"/>
<rect x="774.99" y="78.5" width="2.46" height="36.6" fill="var(--up)"/>
<line x1="780.2" y1="88.2" x2="780.2" y2="125.7" stroke="var(--down)" class="wick"/>
<rect x="778.96" y="89.0" width="2.46" height="32.4" fill="var(--down)"/>
<line x1="784.2" y1="141.0" x2="784.2" y2="195.3" stroke="var(--down)" class="wick"/>
<rect x="782.93" y="143.8" width="2.46" height="27.4" fill="var(--down)"/>
<line x1="788.1" y1="181.3" x2="788.1" y2="224.5" stroke="var(--down)" class="wick"/>
<rect x="786.90" y="193.2" width="2.46" height="24.8" fill="var(--down)"/>
<line x1="792.1" y1="219.6" x2="792.1" y2="285.8" stroke="var(--down)" class="wick"/>
<rect x="790.87" y="222.5" width="2.46" height="49.0" fill="var(--down)"/>
<line x1="796.1" y1="249.1" x2="796.1" y2="278.3" stroke="var(--down)" class="wick"/>
<rect x="794.83" y="269.5" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="800.0" y1="252.3" x2="800.0" y2="289.8" stroke="var(--down)" class="wick"/>
<rect x="798.80" y="253.2" width="2.46" height="34.6" fill="var(--down)"/>
<line x1="804.0" y1="280.2" x2="804.0" y2="392.8" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="306.0" width="2.46" height="63.9" fill="var(--down)"/>
<line x1="808.0" y1="363.8" x2="808.0" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="806.74" y="372.7" width="2.46" height="18.8" fill="var(--down)"/>
<line x1="811.9" y1="371.8" x2="811.9" y2="405.5" stroke="var(--up)" class="wick"/>
<rect x="810.71" y="374.2" width="2.46" height="25.3" fill="var(--up)"/>
<line x1="815.9" y1="342.7" x2="815.9" y2="379.0" stroke="var(--up)" class="wick"/>
<rect x="814.67" y="358.2" width="2.46" height="18.9" fill="var(--up)"/>
<line x1="819.9" y1="298.8" x2="819.9" y2="344.8" stroke="var(--down)" class="wick"/>
<rect x="818.64" y="305.2" width="2.46" height="30.8" fill="var(--down)"/>
<line x1="823.8" y1="283.1" x2="823.8" y2="337.6" stroke="var(--down)" class="wick"/>
<rect x="822.61" y="325.2" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="827.8" y1="322.0" x2="827.8" y2="360.0" stroke="var(--up)" class="wick"/>
<rect x="826.58" y="331.0" width="2.46" height="23.8" fill="var(--up)"/>
<line x1="831.8" y1="315.7" x2="831.8" y2="351.7" stroke="var(--down)" class="wick"/>
<rect x="830.55" y="332.1" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="835.7" y1="308.8" x2="835.7" y2="353.0" stroke="var(--up)" class="wick"/>
<rect x="834.51" y="312.8" width="2.46" height="12.5" fill="var(--up)"/>
<line x1="839.7" y1="300.6" x2="839.7" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="838.48" y="305.3" width="2.46" height="23.7" fill="var(--down)"/>
<line x1="843.7" y1="309.8" x2="843.7" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="842.45" y="314.9" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="847.6" y1="305.1" x2="847.6" y2="345.2" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="321.0" width="2.46" height="11.1" fill="var(--up)"/>
<line x1="851.6" y1="287.4" x2="851.6" y2="334.3" stroke="var(--up)" class="wick"/>
<rect x="850.39" y="305.8" width="2.46" height="13.3" fill="var(--up)"/>
<line x1="855.6" y1="312.1" x2="855.6" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="854.35" y="319.9" width="2.46" height="30.4" fill="var(--down)"/>
<line x1="859.6" y1="353.7" x2="859.6" y2="386.8" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="356.4" width="2.46" height="23.8" fill="var(--down)"/>
<line x1="863.5" y1="370.1" x2="863.5" y2="399.0" stroke="var(--up)" class="wick"/>
<rect x="862.29" y="380.4" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="867.5" y1="348.6" x2="867.5" y2="375.9" stroke="var(--down)" class="wick"/>
<rect x="866.26" y="352.6" width="2.46" height="14.4" fill="var(--down)"/>
<line x1="871.5" y1="345.3" x2="871.5" y2="368.4" stroke="var(--down)" class="wick"/>
<rect x="870.23" y="357.8" width="2.46" height="2.0" fill="var(--down)"/>
<line x1="875.4" y1="371.1" x2="875.4" y2="407.3" stroke="var(--down)" class="wick"/>
<rect x="874.19" y="384.1" width="2.46" height="15.5" fill="var(--down)"/>
<line x1="879.4" y1="358.6" x2="879.4" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="878.16" y="376.4" width="2.46" height="1.5" fill="var(--down)"/>
<line x1="883.4" y1="341.3" x2="883.4" y2="399.3" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="365.2" width="2.46" height="25.1" fill="var(--down)"/>
<line x1="887.3" y1="391.7" x2="887.3" y2="420.4" stroke="var(--down)" class="wick"/>
<rect x="886.10" y="400.1" width="2.46" height="13.8" fill="var(--down)"/>
<line x1="891.3" y1="403.4" x2="891.3" y2="445.4" stroke="var(--down)" class="wick"/>
<rect x="890.07" y="403.4" width="2.46" height="33.3" fill="var(--down)"/>
<line x1="895.3" y1="377.6" x2="895.3" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="894.03" y="379.7" width="2.46" height="52.1" fill="var(--up)"/>
<line x1="899.2" y1="371.6" x2="899.2" y2="401.4" stroke="var(--up)" class="wick"/>
<rect x="898.00" y="382.7" width="2.46" height="2.4" fill="var(--up)"/>
<line x1="903.2" y1="343.1" x2="903.2" y2="393.1" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="346.2" width="2.46" height="42.3" fill="var(--down)"/>
<line x1="907.2" y1="348.4" x2="907.2" y2="387.4" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="364.2" width="2.46" height="12.4" fill="var(--down)"/>
<line x1="911.1" y1="414.9" x2="911.1" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="909.91" y="415.0" width="2.46" height="46.4" fill="var(--down)"/>
<line x1="915.1" y1="453.5" x2="915.1" y2="473.6" stroke="var(--up)" class="wick"/>
<rect x="913.87" y="454.5" width="2.46" height="5.3" fill="var(--up)"/>
<line x1="919.1" y1="423.4" x2="919.1" y2="453.1" stroke="var(--up)" class="wick"/>
<rect x="917.84" y="433.0" width="2.46" height="16.9" fill="var(--up)"/>
<line x1="923.0" y1="426.7" x2="923.0" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="921.81" y="442.9" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="927.0" y1="430.6" x2="927.0" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="925.78" y="451.3" width="2.46" height="2.6" fill="var(--down)"/>
<line x1="931.0" y1="392.2" x2="931.0" y2="443.4" stroke="var(--up)" class="wick"/>
<rect x="929.75" y="392.6" width="2.46" height="45.5" fill="var(--up)"/>
<line x1="934.9" y1="353.0" x2="934.9" y2="417.5" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="358.9" width="2.46" height="43.6" fill="var(--down)"/>
<line x1="938.9" y1="389.6" x2="938.9" y2="421.2" stroke="var(--down)" class="wick"/>
<rect x="937.68" y="407.0" width="2.46" height="6.2" fill="var(--down)"/>
<line x1="942.9" y1="421.2" x2="942.9" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="941.65" y="424.9" width="2.46" height="2.2" fill="var(--down)"/>
<line x1="946.8" y1="417.8" x2="946.8" y2="444.5" stroke="var(--down)" class="wick"/>
<rect x="945.62" y="423.6" width="2.46" height="7.5" fill="var(--down)"/>
<line x1="950.8" y1="432.8" x2="950.8" y2="453.4" stroke="var(--up)" class="wick"/>
<rect x="949.59" y="433.8" width="2.46" height="11.7" fill="var(--up)"/>
<line x1="954.8" y1="411.4" x2="954.8" y2="443.9" stroke="var(--up)" class="wick"/>
<rect x="953.55" y="414.8" width="2.46" height="21.2" fill="var(--up)"/>
<line x1="958.8" y1="369.3" x2="958.8" y2="411.4" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="379.9" width="2.46" height="28.4" fill="var(--up)"/>
<line x1="962.7" y1="304.0" x2="962.7" y2="349.7" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="339.8" width="2.46" height="8.4" fill="var(--down)"/>
<line x1="966.7" y1="322.4" x2="966.7" y2="355.8" stroke="var(--up)" class="wick"/>
<rect x="965.46" y="332.5" width="2.46" height="12.6" fill="var(--up)"/>
<line x1="970.7" y1="360.5" x2="970.7" y2="383.9" stroke="var(--down)" class="wick"/>
<rect x="969.43" y="372.6" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="974.6" y1="371.5" x2="974.6" y2="409.6" stroke="var(--up)" class="wick"/>
<rect x="973.39" y="379.2" width="2.46" height="13.0" fill="var(--up)"/>
<line x1="978.6" y1="345.3" x2="978.6" y2="385.9" stroke="var(--down)" class="wick"/>
<rect x="977.36" y="351.2" width="2.46" height="23.4" fill="var(--down)"/>
<line x1="982.6" y1="381.4" x2="982.6" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="387.8" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="986.5" y1="368.5" x2="986.5" y2="414.4" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="368.5" width="2.46" height="31.7" fill="var(--down)"/>
<line x1="990.5" y1="349.1" x2="990.5" y2="400.6" stroke="var(--down)" class="wick"/>
<rect x="989.27" y="363.1" width="2.46" height="22.0" fill="var(--down)"/>
<line x1="994.5" y1="383.7" x2="994.5" y2="409.6" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="387.8" width="2.46" height="9.1" fill="var(--up)"/>
<line x1="998.4" y1="377.1" x2="998.4" y2="403.2" stroke="var(--up)" class="wick"/>
<rect x="997.20" y="377.4" width="2.46" height="21.7" fill="var(--up)"/>
<line x1="1002.4" y1="372.9" x2="1002.4" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="1001.17" y="383.1" width="2.46" height="12.1" fill="var(--down)"/>
<line x1="1006.4" y1="380.3" x2="1006.4" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="1005.14" y="384.1" width="2.46" height="25.7" fill="var(--up)"/>
<line x1="1010.3" y1="356.7" x2="1010.3" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="1009.11" y="358.2" width="2.46" height="16.0" fill="var(--up)"/>
<line x1="1014.3" y1="350.8" x2="1014.3" y2="366.9" stroke="var(--up)" class="wick"/>
<rect x="1013.07" y="359.8" width="2.46" height="2.3" fill="var(--up)"/>
<line x1="1018.3" y1="369.0" x2="1018.3" y2="384.4" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="373.0" width="2.46" height="2.8" fill="var(--down)"/>
<line x1="1022.2" y1="336.9" x2="1022.2" y2="372.6" stroke="var(--down)" class="wick"/>
<rect x="1021.01" y="349.2" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="1026.2" y1="322.6" x2="1026.2" y2="370.6" stroke="var(--down)" class="wick"/>
<rect x="1024.98" y="361.6" width="2.46" height="6.8" fill="var(--down)"/>
<line x1="1030.2" y1="395.4" x2="1030.2" y2="434.4" stroke="var(--up)" class="wick"/>
<rect x="1028.95" y="418.0" width="2.46" height="5.0" fill="var(--up)"/>
<line x1="1034.1" y1="383.4" x2="1034.1" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="1032.91" y="388.0" width="2.46" height="17.1" fill="var(--up)"/>
<line x1="1038.1" y1="331.5" x2="1038.1" y2="380.3" stroke="var(--up)" class="wick"/>
<rect x="1036.88" y="338.0" width="2.46" height="38.8" fill="var(--up)"/>
<line x1="1042.1" y1="343.0" x2="1042.1" y2="362.3" stroke="var(--down)" class="wick"/>
<rect x="1040.85" y="349.7" width="2.46" height="12.3" fill="var(--down)"/>
<line x1="1046.0" y1="352.7" x2="1046.0" y2="373.6" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="360.9" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="1050.0" y1="385.7" x2="1050.0" y2="418.6" stroke="var(--down)" class="wick"/>
<rect x="1048.79" y="386.9" width="2.46" height="28.7" fill="var(--down)"/>
<line x1="60" y1="413.2" x2="1052" y2="413.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="416.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$936 R1</text>
<text x="1058" y="428.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="321.5" x2="1052" y2="321.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="325.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$979 R2</text>
<text x="1058" y="337.0" font-size="9.5" fill="var(--muted)">터치 8회</text>
<line x1="60" y1="223.1" x2="1052" y2="223.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="226.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,026 R3</text>
<text x="1058" y="238.6" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="449.0" x2="1052" y2="449.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="443.0" font-size="11.5" fill="var(--support)" font-weight="600">$919 S1</text>
<text x="1058" y="455.0" font-size="9.5" fill="var(--muted)">터치 10회</text>
<line x1="60" y1="598.0" x2="1052" y2="598.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="592.0" font-size="11.5" fill="var(--support)" font-weight="600">$848 S2</text>
<text x="1058" y="604.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="415.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="407.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $935 (2026-08-27)</text>
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
| R3 | $1,026 | 5 | 2026-02~05 고점대 — FY26 Q2 실적 직후 형성된 연중 최고 구간(2026-02-17·03-02·03-13·04-09·05-01) |
| R2 | $979 | 8 | 2025-09~2026-08에 걸쳐 반복 확인된 최다 저항대(2025-09-10·10-15, 2026-01-26·06-16·06-29·07-17·08-19) |
| R1 | $936 | 2 | 2025-11~12 고점대(2025-11-05·12-03). 현재가 바로 위 0.1%p 지점 |
| **현재가** | **$934.66** (2026-08-27 종가) | — | R1 바로 아래, S1 위 1.7%p |
| S1 | $919 | 10 | 최다 터치 지지대. 2025-09~2026-08 전 구간에 분산(2025-09-29·10-07·10-16·11-06, 2026-01-30·06-01·07-10·07-23·08-12·08-20) |
| S2 | $848 | 2 | 2025-12~2026-01 저점대(2025-12-16·2026-01-02). 연중 최저 $844와 인접 |
| 참고선 | $1,096.50 | — | 최근 1년 최고가(2026-02~05 구간). 단일 고점이라 클러스터로 잡히지 않아 저항으로 보지 않는다 |
| 참고선 | $844.06 | — | 최근 1년 최저가. S2($848)와 사실상 같은 가격대라 별도 레벨로 두지 않았다 |

**현재가 $934.66은 R1($936)과 S1($919) 사이의 좁은 구간에 있다.** 위아래로 각각 0.1%p·1.7%p 거리라 방향성이 없는 위치이며, 의미 있는 저항은 R2($979, 터치 8회)와 지지는 S1($919, 터치 10회)이다. **터치 횟수가 가장 많은 두 레벨(S1 10회 · R2 8회)이 현재가를 위아래로 감싸고 있어**, 최근 1년의 거래는 사실상 $919~$979 박스에 갇혀 있었다고 읽을 수 있다.

---

## 3. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py COST --name "Costco" --close-on 2026-08-27 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **가격 연속성을 깨는 이벤트는 이 기간에 없었다.** 최근 1년 중 전일 대비 ±4.5% 이상 움직인 거래일이 하나도 없어 "관측된 특이 구간" 절을 두지 않았다 — 실적 발표일에도 갭이 크지 않은 종목이다.
    - 코스트코는 2000-01 이후 주식분할이 없어 소급조정 이슈가 없다. 다만 위 데이터는 **원주가(배당 미반영)**이므로, 이 기간 4회 지급된 배당(분기 $1.30~$1.47)만큼 총수익률과는 차이가 난다.

---

*작성일: 2026-08-30*
