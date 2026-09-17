# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-11 종가 **$293.11**은 핵심 지표·밸류에이션 / 적정주가에 인용된 기준 종가와 일치한다. ⚠️ 같은 날 종가를 수집 시점에 따라 $292.74~$293.11 범위로 받은 적이 있다(집계 지연으로 보인다) — 이 회사 폴더 전체는 위 값 하나로 통일했다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-11 ~ 2026-09-11)

<style>
.apd-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .apd-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.apd-chart svg { width:100%; height:auto; display:block; }
.apd-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.apd-chart .title { fill: var(--ink); font-weight:600; }
.apd-chart .grid { stroke: var(--grid); stroke-width:1; }
.apd-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="apd-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Air Products(APD) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Air Products (APD) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-11 ~ 2026-09-11 · 마지막 종가 $293.11 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="539.3" x2="1052" y2="539.3" class="grid"/>
<text x="52" y="543.3" font-size="11" text-anchor="end" fill="var(--muted)">240</text>
<line x1="60" y1="415.3" x2="1052" y2="415.3" class="grid"/>
<text x="52" y="419.3" font-size="11" text-anchor="end" fill="var(--muted)">260</text>
<line x1="60" y1="291.4" x2="1052" y2="291.4" class="grid"/>
<text x="52" y="295.4" font-size="11" text-anchor="end" fill="var(--muted)">280</text>
<line x1="60" y1="167.5" x2="1052" y2="167.5" class="grid"/>
<text x="52" y="171.5" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="117.1" y1="626.0" x2="117.1" y2="631.0" class="axis"/>
<text x="117.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="207.6" y1="626.0" x2="207.6" y2="631.0" class="axis"/>
<text x="207.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="282.4" y1="626.0" x2="282.4" y2="631.0" class="axis"/>
<text x="282.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="369.0" y1="626.0" x2="369.0" y2="631.0" class="axis"/>
<text x="369.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="447.7" y1="626.0" x2="447.7" y2="631.0" class="axis"/>
<text x="447.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="522.5" y1="626.0" x2="522.5" y2="631.0" class="axis"/>
<text x="522.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="609.1" y1="626.0" x2="609.1" y2="631.0" class="axis"/>
<text x="609.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="691.8" y1="626.0" x2="691.8" y2="631.0" class="axis"/>
<text x="691.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="770.5" y1="626.0" x2="770.5" y2="631.0" class="axis"/>
<text x="770.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="853.2" y1="626.0" x2="853.2" y2="631.0" class="axis"/>
<text x="853.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="939.8" y1="626.0" x2="939.8" y2="631.0" class="axis"/>
<text x="939.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1022.5" y1="626.0" x2="1022.5" y2="631.0" class="axis"/>
<text x="1022.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="849.3" y1="56.0" x2="849.3" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="855.3" y="68.0" font-size="10.5" fill="var(--down)">2026-06-30 청정에너지 철수 발표</text>
<line x1="931.9" y1="56.0" x2="931.9" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="937.9" y="68.0" font-size="10.5" fill="var(--down)">2026-07-30 Q3 실적·가이던스 상향</text>
<line x1="62.0" y1="199.2" x2="62.0" y2="249.5" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="201.5" width="2.44" height="40.4" fill="var(--up)"/>
<line x1="65.9" y1="178.0" x2="65.9" y2="212.4" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="194.2" width="2.44" height="17.8" fill="var(--down)"/>
<line x1="69.8" y1="188.0" x2="69.8" y2="233.0" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="204.3" width="2.44" height="28.1" fill="var(--down)"/>
<line x1="73.8" y1="227.2" x2="73.8" y2="275.1" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="239.2" width="2.44" height="21.6" fill="var(--down)"/>
<line x1="77.7" y1="200.3" x2="77.7" y2="264.4" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="225.6" width="2.44" height="25.7" fill="var(--up)"/>
<line x1="81.7" y1="210.5" x2="81.7" y2="241.8" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="214.3" width="2.44" height="13.4" fill="var(--up)"/>
<line x1="85.6" y1="210.5" x2="85.6" y2="237.7" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="210.9" width="2.44" height="17.7" fill="var(--down)"/>
<line x1="89.5" y1="223.5" x2="89.5" y2="252.4" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="242.4" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="93.5" y1="238.4" x2="93.5" y2="324.2" stroke="var(--down)" class="wick"/>
<rect x="92.24" y="241.5" width="2.44" height="71.1" fill="var(--down)"/>
<line x1="97.4" y1="303.2" x2="97.4" y2="345.3" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="303.2" width="2.44" height="36.1" fill="var(--down)"/>
<line x1="101.3" y1="342.8" x2="101.3" y2="382.4" stroke="var(--down)" class="wick"/>
<rect x="100.11" y="345.6" width="2.44" height="34.0" fill="var(--down)"/>
<line x1="105.3" y1="358.3" x2="105.3" y2="383.7" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="371.2" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="109.2" y1="331.6" x2="109.2" y2="375.6" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="350.4" width="2.44" height="16.9" fill="var(--up)"/>
<line x1="113.1" y1="335.5" x2="113.1" y2="362.0" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="336.5" width="2.44" height="17.2" fill="var(--up)"/>
<line x1="117.1" y1="338.8" x2="117.1" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="115.86" y="356.7" width="2.44" height="4.7" fill="var(--down)"/>
<line x1="121.0" y1="323.5" x2="121.0" y2="367.8" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="349.7" width="2.44" height="18.1" fill="var(--up)"/>
<line x1="125.0" y1="340.9" x2="125.0" y2="364.1" stroke="var(--up)" class="wick"/>
<rect x="123.73" y="344.3" width="2.44" height="10.2" fill="var(--up)"/>
<line x1="128.9" y1="331.0" x2="128.9" y2="352.5" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="345.0" width="2.44" height="2.5" fill="var(--down)"/>
<line x1="132.8" y1="333.8" x2="132.8" y2="357.8" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="347.9" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="136.8" y1="352.8" x2="136.8" y2="367.4" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="354.6" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="140.7" y1="356.7" x2="140.7" y2="405.4" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="364.9" width="2.44" height="33.6" fill="var(--down)"/>
<line x1="144.6" y1="390.1" x2="144.6" y2="434.2" stroke="var(--down)" class="wick"/>
<rect x="143.41" y="397.2" width="2.44" height="36.2" fill="var(--down)"/>
<line x1="148.6" y1="399.9" x2="148.6" y2="423.2" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="410.0" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="152.5" y1="377.6" x2="152.5" y2="427.7" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="403.0" width="2.44" height="24.2" fill="var(--up)"/>
<line x1="156.4" y1="387.1" x2="156.4" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="398.1" width="2.44" height="33.3" fill="var(--down)"/>
<line x1="160.4" y1="433.9" x2="160.4" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="439.6" width="2.44" height="18.0" fill="var(--down)"/>
<line x1="164.3" y1="443.5" x2="164.3" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="163.10" y="452.4" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="168.3" y1="444.3" x2="168.3" y2="459.7" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="451.1" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="172.2" y1="434.9" x2="172.2" y2="455.2" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="448.1" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="176.1" y1="445.0" x2="176.1" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="452.3" width="2.44" height="5.5" fill="var(--down)"/>
<line x1="180.1" y1="441.4" x2="180.1" y2="466.6" stroke="var(--up)" class="wick"/>
<rect x="178.84" y="446.8" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="184.0" y1="434.6" x2="184.0" y2="455.1" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="444.0" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="187.9" y1="431.1" x2="187.9" y2="448.8" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="441.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="191.9" y1="434.3" x2="191.9" y2="453.7" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="441.7" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="195.8" y1="451.7" x2="195.8" y2="490.7" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="454.8" width="2.44" height="32.8" fill="var(--down)"/>
<line x1="199.7" y1="485.4" x2="199.7" y2="512.0" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="496.9" width="2.44" height="13.4" fill="var(--down)"/>
<line x1="203.7" y1="514.4" x2="203.7" y2="545.3" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="514.4" width="2.44" height="8.9" fill="var(--down)"/>
<line x1="207.6" y1="526.4" x2="207.6" y2="564.2" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="527.4" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="211.6" y1="531.2" x2="211.6" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="534.5" width="2.44" height="14.0" fill="var(--up)"/>
<line x1="215.5" y1="530.1" x2="215.5" y2="566.8" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="534.5" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="219.4" y1="388.6" x2="219.4" y2="481.7" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="422.8" width="2.44" height="58.2" fill="var(--up)"/>
<line x1="223.4" y1="410.8" x2="223.4" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="417.0" width="2.44" height="19.2" fill="var(--up)"/>
<line x1="227.3" y1="409.0" x2="227.3" y2="437.3" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="411.9" width="2.44" height="13.1" fill="var(--down)"/>
<line x1="231.2" y1="383.9" x2="231.2" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="401.5" width="2.44" height="16.9" fill="var(--up)"/>
<line x1="235.2" y1="379.5" x2="235.2" y2="408.2" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="399.7" width="2.44" height="6.0" fill="var(--down)"/>
<line x1="239.1" y1="388.7" x2="239.1" y2="415.3" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="396.6" width="2.44" height="18.8" fill="var(--up)"/>
<line x1="243.0" y1="395.8" x2="243.0" y2="423.5" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="403.0" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="247.0" y1="423.8" x2="247.0" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="426.0" width="2.44" height="32.2" fill="var(--down)"/>
<line x1="250.9" y1="452.5" x2="250.9" y2="482.3" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="463.9" width="2.44" height="5.2" fill="var(--up)"/>
<line x1="254.9" y1="454.1" x2="254.9" y2="477.1" stroke="var(--up)" class="wick"/>
<rect x="253.64" y="457.2" width="2.44" height="3.9" fill="var(--up)"/>
<line x1="258.8" y1="424.3" x2="258.8" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="257.57" y="452.1" width="2.44" height="18.5" fill="var(--down)"/>
<line x1="262.7" y1="429.2" x2="262.7" y2="468.8" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="431.6" width="2.44" height="31.9" fill="var(--up)"/>
<line x1="266.7" y1="432.0" x2="266.7" y2="460.5" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="436.5" width="2.44" height="1.2" fill="var(--up)"/>
<line x1="270.6" y1="416.1" x2="270.6" y2="433.9" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="422.0" width="2.44" height="2.8" fill="var(--up)"/>
<line x1="274.5" y1="410.2" x2="274.5" y2="430.4" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="421.8" width="2.44" height="4.1" fill="var(--up)"/>
<line x1="278.5" y1="401.2" x2="278.5" y2="421.7" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="408.8" width="2.44" height="5.5" fill="var(--up)"/>
<line x1="282.4" y1="396.3" x2="282.4" y2="418.4" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="410.0" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="286.3" y1="408.5" x2="286.3" y2="438.7" stroke="var(--down)" class="wick"/>
<rect x="285.13" y="410.1" width="2.44" height="25.2" fill="var(--down)"/>
<line x1="290.3" y1="405.7" x2="290.3" y2="429.8" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="413.2" width="2.44" height="15.7" fill="var(--up)"/>
<line x1="294.2" y1="399.6" x2="294.2" y2="427.7" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="405.3" width="2.44" height="7.7" fill="var(--up)"/>
<line x1="298.2" y1="381.1" x2="298.2" y2="413.3" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="405.9" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="302.1" y1="435.7" x2="302.1" y2="599.0" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="446.2" width="2.44" height="117.5" fill="var(--down)"/>
<line x1="306.0" y1="538.1" x2="306.0" y2="600.9" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="560.9" width="2.44" height="35.6" fill="var(--down)"/>
<line x1="310.0" y1="556.4" x2="310.0" y2="606.7" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="559.6" width="2.44" height="42.7" fill="var(--up)"/>
<line x1="313.9" y1="515.7" x2="313.9" y2="551.0" stroke="var(--up)" class="wick"/>
<rect x="312.68" y="516.2" width="2.44" height="29.3" fill="var(--up)"/>
<line x1="317.8" y1="511.4" x2="317.8" y2="539.7" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="520.7" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="321.8" y1="507.6" x2="321.8" y2="539.7" stroke="var(--up)" class="wick"/>
<rect x="320.56" y="508.2" width="2.44" height="25.3" fill="var(--up)"/>
<line x1="325.7" y1="506.8" x2="325.7" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="324.49" y="518.9" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="329.7" y1="491.4" x2="329.7" y2="529.3" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="499.7" width="2.44" height="25.6" fill="var(--up)"/>
<line x1="333.6" y1="482.4" x2="333.6" y2="516.6" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="490.6" width="2.44" height="25.4" fill="var(--down)"/>
<line x1="337.5" y1="517.7" x2="337.5" y2="547.9" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="529.3" width="2.44" height="10.2" fill="var(--down)"/>
<line x1="341.5" y1="503.9" x2="341.5" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="509.6" width="2.44" height="29.9" fill="var(--up)"/>
<line x1="345.4" y1="505.1" x2="345.4" y2="525.5" stroke="var(--up)" class="wick"/>
<rect x="344.18" y="509.7" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="349.3" y1="500.5" x2="349.3" y2="513.5" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="503.1" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="353.3" y1="490.1" x2="353.3" y2="508.3" stroke="var(--up)" class="wick"/>
<rect x="352.05" y="493.3" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="357.2" y1="484.7" x2="357.2" y2="501.8" stroke="var(--up)" class="wick"/>
<rect x="355.99" y="490.6" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="361.1" y1="479.8" x2="361.1" y2="498.6" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="484.6" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="365.1" y1="479.7" x2="365.1" y2="496.4" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="486.7" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="369.0" y1="468.4" x2="369.0" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="474.4" width="2.44" height="32.2" fill="var(--up)"/>
<line x1="373.0" y1="440.3" x2="373.0" y2="493.1" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="453.5" width="2.44" height="37.4" fill="var(--up)"/>
<line x1="376.9" y1="414.4" x2="376.9" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="375.67" y="425.5" width="2.44" height="25.6" fill="var(--up)"/>
<line x1="380.8" y1="398.2" x2="380.8" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="379.61" y="403.8" width="2.44" height="24.2" fill="var(--up)"/>
<line x1="384.8" y1="383.4" x2="384.8" y2="421.2" stroke="var(--down)" class="wick"/>
<rect x="383.54" y="397.9" width="2.44" height="9.9" fill="var(--down)"/>
<line x1="388.7" y1="380.0" x2="388.7" y2="415.0" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="392.3" width="2.44" height="21.4" fill="var(--up)"/>
<line x1="392.6" y1="367.8" x2="392.6" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="371.7" width="2.44" height="21.9" fill="var(--up)"/>
<line x1="396.6" y1="362.2" x2="396.6" y2="387.8" stroke="var(--down)" class="wick"/>
<rect x="395.35" y="373.5" width="2.44" height="3.6" fill="var(--down)"/>
<line x1="400.5" y1="347.9" x2="400.5" y2="378.7" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="370.4" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="404.4" y1="355.4" x2="404.4" y2="387.8" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="365.8" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="408.4" y1="366.7" x2="408.4" y2="390.6" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="368.7" width="2.44" height="21.9" fill="var(--up)"/>
<line x1="412.3" y1="379.1" x2="412.3" y2="436.5" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="390.6" width="2.44" height="36.0" fill="var(--down)"/>
<line x1="416.3" y1="388.3" x2="416.3" y2="424.3" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="396.1" width="2.44" height="11.9" fill="var(--up)"/>
<line x1="420.2" y1="370.6" x2="420.2" y2="398.4" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="390.3" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="424.1" y1="389.3" x2="424.1" y2="417.8" stroke="var(--down)" class="wick"/>
<rect x="422.91" y="390.1" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="428.1" y1="385.2" x2="428.1" y2="403.3" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="396.8" width="2.44" height="2.4" fill="var(--down)"/>
<line x1="432.0" y1="393.7" x2="432.0" y2="424.5" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="406.1" width="2.44" height="14.7" fill="var(--down)"/>
<line x1="435.9" y1="412.1" x2="435.9" y2="452.9" stroke="var(--down)" class="wick"/>
<rect x="434.72" y="419.5" width="2.44" height="21.3" fill="var(--down)"/>
<line x1="439.9" y1="425.6" x2="439.9" y2="451.3" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="437.9" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="443.8" y1="329.2" x2="443.8" y2="398.8" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="337.9" width="2.44" height="31.9" fill="var(--up)"/>
<line x1="447.7" y1="321.4" x2="447.7" y2="366.2" stroke="var(--up)" class="wick"/>
<rect x="446.53" y="347.3" width="2.44" height="6.1" fill="var(--up)"/>
<line x1="451.7" y1="303.6" x2="451.7" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="304.1" width="2.44" height="38.2" fill="var(--up)"/>
<line x1="455.6" y1="249.9" x2="455.6" y2="293.7" stroke="var(--up)" class="wick"/>
<rect x="454.40" y="250.6" width="2.44" height="40.9" fill="var(--up)"/>
<line x1="459.6" y1="243.0" x2="459.6" y2="278.0" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="246.6" width="2.44" height="23.1" fill="var(--down)"/>
<line x1="463.5" y1="249.7" x2="463.5" y2="282.8" stroke="var(--up)" class="wick"/>
<rect x="462.27" y="272.1" width="2.44" height="3.0" fill="var(--up)"/>
<line x1="467.4" y1="249.1" x2="467.4" y2="287.3" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="252.0" width="2.44" height="26.6" fill="var(--up)"/>
<line x1="471.4" y1="210.1" x2="471.4" y2="252.7" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="224.7" width="2.44" height="28.0" fill="var(--up)"/>
<line x1="475.3" y1="200.5" x2="475.3" y2="235.2" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="210.0" width="2.44" height="18.8" fill="var(--up)"/>
<line x1="479.2" y1="189.5" x2="479.2" y2="231.0" stroke="var(--down)" class="wick"/>
<rect x="478.02" y="204.1" width="2.44" height="16.0" fill="var(--down)"/>
<line x1="483.2" y1="249.1" x2="483.2" y2="328.1" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="267.3" width="2.44" height="25.8" fill="var(--down)"/>
<line x1="487.1" y1="280.6" x2="487.1" y2="317.9" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="280.6" width="2.44" height="25.2" fill="var(--down)"/>
<line x1="491.0" y1="274.0" x2="491.0" y2="300.0" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="276.6" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="495.0" y1="275.9" x2="495.0" y2="298.7" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="283.0" width="2.44" height="4.0" fill="var(--down)"/>
<line x1="498.9" y1="268.0" x2="498.9" y2="298.9" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="284.1" width="2.44" height="7.7" fill="var(--up)"/>
<line x1="502.9" y1="263.6" x2="502.9" y2="285.5" stroke="var(--up)" class="wick"/>
<rect x="501.64" y="271.3" width="2.44" height="10.8" fill="var(--up)"/>
<line x1="506.8" y1="261.5" x2="506.8" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="505.57" y="263.2" width="2.44" height="31.5" fill="var(--down)"/>
<line x1="510.7" y1="273.3" x2="510.7" y2="313.2" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="284.4" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="514.7" y1="275.7" x2="514.7" y2="327.3" stroke="var(--down)" class="wick"/>
<rect x="513.45" y="283.5" width="2.44" height="31.3" fill="var(--down)"/>
<line x1="518.6" y1="303.5" x2="518.6" y2="334.0" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="314.8" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="522.5" y1="308.3" x2="522.5" y2="346.1" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="313.6" width="2.44" height="15.7" fill="var(--up)"/>
<line x1="526.5" y1="325.1" x2="526.5" y2="365.0" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="334.6" width="2.44" height="12.6" fill="var(--up)"/>
<line x1="530.4" y1="322.7" x2="530.4" y2="348.1" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="327.4" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="534.3" y1="303.0" x2="534.3" y2="337.9" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="314.0" width="2.44" height="22.8" fill="var(--up)"/>
<line x1="538.3" y1="314.5" x2="538.3" y2="345.3" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="314.5" width="2.44" height="25.3" fill="var(--down)"/>
<line x1="542.2" y1="314.7" x2="542.2" y2="339.9" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="326.1" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="546.2" y1="309.1" x2="546.2" y2="350.0" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="321.7" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="550.1" y1="302.2" x2="550.1" y2="346.1" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="305.7" width="2.44" height="19.1" fill="var(--up)"/>
<line x1="554.0" y1="213.4" x2="554.0" y2="289.4" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="226.5" width="2.44" height="53.9" fill="var(--up)"/>
<line x1="558.0" y1="187.2" x2="558.0" y2="248.9" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="193.9" width="2.44" height="48.1" fill="var(--down)"/>
<line x1="561.9" y1="227.7" x2="561.9" y2="257.2" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="228.2" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="565.8" y1="217.0" x2="565.8" y2="256.9" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="219.2" width="2.44" height="34.1" fill="var(--down)"/>
<line x1="569.8" y1="237.5" x2="569.8" y2="283.2" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="255.8" width="2.44" height="26.8" fill="var(--down)"/>
<line x1="573.7" y1="243.3" x2="573.7" y2="297.6" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="265.7" width="2.44" height="27.8" fill="var(--up)"/>
<line x1="577.7" y1="247.6" x2="577.7" y2="296.7" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="247.6" width="2.44" height="37.5" fill="var(--down)"/>
<line x1="581.6" y1="260.7" x2="581.6" y2="306.9" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="265.8" width="2.44" height="34.0" fill="var(--down)"/>
<line x1="585.5" y1="241.6" x2="585.5" y2="311.5" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="252.7" width="2.44" height="58.4" fill="var(--up)"/>
<line x1="589.5" y1="225.3" x2="589.5" y2="268.4" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="228.9" width="2.44" height="12.9" fill="var(--up)"/>
<line x1="593.4" y1="197.0" x2="593.4" y2="231.2" stroke="var(--up)" class="wick"/>
<rect x="592.18" y="209.8" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="597.3" y1="200.2" x2="597.3" y2="227.1" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="212.8" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="601.3" y1="189.8" x2="601.3" y2="220.7" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="204.1" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="605.2" y1="198.7" x2="605.2" y2="244.1" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="214.3" width="2.44" height="12.1" fill="var(--down)"/>
<line x1="609.1" y1="228.9" x2="609.1" y2="264.1" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="233.0" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="613.1" y1="189.5" x2="613.1" y2="225.5" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="207.5" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="617.0" y1="203.6" x2="617.0" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="615.80" y="204.0" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="621.0" y1="189.9" x2="621.0" y2="221.2" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="200.7" width="2.44" height="13.9" fill="var(--down)"/>
<line x1="624.9" y1="188.5" x2="624.9" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="623.67" y="188.5" width="2.44" height="68.2" fill="var(--up)"/>
<line x1="628.8" y1="159.8" x2="628.8" y2="206.4" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="181.5" width="2.44" height="17.0" fill="var(--up)"/>
<line x1="632.8" y1="169.6" x2="632.8" y2="194.2" stroke="var(--down)" class="wick"/>
<rect x="631.54" y="173.7" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="636.7" y1="161.3" x2="636.7" y2="186.4" stroke="var(--down)" class="wick"/>
<rect x="635.48" y="173.0" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="640.6" y1="183.0" x2="640.6" y2="213.8" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="183.0" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="644.6" y1="186.2" x2="644.6" y2="209.1" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="191.0" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="648.5" y1="176.2" x2="648.5" y2="193.4" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="184.6" width="2.44" height="7.7" fill="var(--up)"/>
<line x1="652.4" y1="199.1" x2="652.4" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="651.22" y="218.3" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="656.4" y1="176.1" x2="656.4" y2="204.7" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="191.4" width="2.44" height="7.3" fill="var(--up)"/>
<line x1="660.3" y1="174.0" x2="660.3" y2="208.0" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="192.3" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="664.3" y1="182.9" x2="664.3" y2="202.4" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="187.6" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="668.2" y1="142.7" x2="668.2" y2="184.1" stroke="var(--up)" class="wick"/>
<rect x="666.97" y="144.9" width="2.44" height="25.5" fill="var(--up)"/>
<line x1="672.1" y1="139.2" x2="672.1" y2="162.0" stroke="var(--down)" class="wick"/>
<rect x="670.91" y="150.2" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="676.1" y1="122.4" x2="676.1" y2="160.0" stroke="var(--down)" class="wick"/>
<rect x="674.84" y="133.4" width="2.44" height="19.3" fill="var(--down)"/>
<line x1="680.0" y1="129.7" x2="680.0" y2="171.4" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="136.1" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="683.9" y1="138.8" x2="683.9" y2="177.4" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="146.8" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="687.9" y1="152.0" x2="687.9" y2="203.9" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="167.2" width="2.44" height="6.5" fill="var(--up)"/>
<line x1="691.8" y1="140.1" x2="691.8" y2="175.9" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="142.7" width="2.44" height="18.2" fill="var(--down)"/>
<line x1="695.7" y1="162.9" x2="695.7" y2="196.0" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="167.4" width="2.44" height="10.3" fill="var(--down)"/>
<line x1="699.7" y1="134.1" x2="699.7" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="143.2" width="2.44" height="32.5" fill="var(--up)"/>
<line x1="703.6" y1="143.9" x2="703.6" y2="169.1" stroke="var(--down)" class="wick"/>
<rect x="702.40" y="157.9" width="2.44" height="8.3" fill="var(--down)"/>
<line x1="707.6" y1="173.4" x2="707.6" y2="220.1" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="177.6" width="2.44" height="21.0" fill="var(--down)"/>
<line x1="711.5" y1="170.6" x2="711.5" y2="197.0" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="193.7" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="715.4" y1="137.0" x2="715.4" y2="183.3" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="139.6" width="2.44" height="43.6" fill="var(--up)"/>
<line x1="719.4" y1="131.1" x2="719.4" y2="177.4" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="136.5" width="2.44" height="8.7" fill="var(--down)"/>
<line x1="723.3" y1="118.2" x2="723.3" y2="153.5" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="129.1" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="727.2" y1="124.4" x2="727.2" y2="179.9" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="125.3" width="2.44" height="43.0" fill="var(--down)"/>
<line x1="731.2" y1="152.0" x2="731.2" y2="213.3" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="164.8" width="2.44" height="31.3" fill="var(--down)"/>
<line x1="735.1" y1="188.1" x2="735.1" y2="214.0" stroke="var(--down)" class="wick"/>
<rect x="733.89" y="197.3" width="2.44" height="11.7" fill="var(--down)"/>
<line x1="739.0" y1="208.2" x2="739.0" y2="231.8" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="210.7" width="2.44" height="7.8" fill="var(--down)"/>
<line x1="743.0" y1="208.4" x2="743.0" y2="257.6" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="234.5" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="746.9" y1="217.6" x2="746.9" y2="253.5" stroke="var(--up)" class="wick"/>
<rect x="745.70" y="228.3" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="750.9" y1="204.8" x2="750.9" y2="239.5" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="217.2" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="754.8" y1="223.8" x2="754.8" y2="247.6" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="232.0" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="758.7" y1="238.3" x2="758.7" y2="261.6" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="238.3" width="2.44" height="17.7" fill="var(--down)"/>
<line x1="762.7" y1="243.4" x2="762.7" y2="280.4" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="259.7" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="766.6" y1="264.3" x2="766.6" y2="303.9" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="278.2" width="2.44" height="21.7" fill="var(--down)"/>
<line x1="770.5" y1="294.3" x2="770.5" y2="321.2" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="298.3" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="774.5" y1="284.5" x2="774.5" y2="305.7" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="295.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="778.4" y1="259.4" x2="778.4" y2="309.1" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="277.4" width="2.44" height="24.3" fill="var(--up)"/>
<line x1="782.3" y1="257.4" x2="782.3" y2="279.9" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="273.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="786.3" y1="244.3" x2="786.3" y2="278.3" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="272.3" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="790.2" y1="263.7" x2="790.2" y2="326.3" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="279.5" width="2.44" height="31.9" fill="var(--down)"/>
<line x1="794.2" y1="272.0" x2="794.2" y2="303.7" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="273.0" width="2.44" height="25.8" fill="var(--up)"/>
<line x1="798.1" y1="252.8" x2="798.1" y2="313.9" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="262.4" width="2.44" height="50.7" fill="var(--down)"/>
<line x1="802.0" y1="280.5" x2="802.0" y2="305.3" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="295.2" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="806.0" y1="247.6" x2="806.0" y2="294.1" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="281.4" width="2.44" height="10.0" fill="var(--up)"/>
<line x1="809.9" y1="266.7" x2="809.9" y2="312.1" stroke="var(--up)" class="wick"/>
<rect x="808.68" y="273.1" width="2.44" height="18.3" fill="var(--up)"/>
<line x1="813.8" y1="261.4" x2="813.8" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="272.4" width="2.44" height="16.0" fill="var(--down)"/>
<line x1="817.8" y1="269.3" x2="817.8" y2="295.4" stroke="var(--up)" class="wick"/>
<rect x="816.56" y="280.6" width="2.44" height="14.0" fill="var(--up)"/>
<line x1="821.7" y1="267.6" x2="821.7" y2="300.0" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="270.4" width="2.44" height="19.8" fill="var(--down)"/>
<line x1="825.7" y1="261.3" x2="825.7" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="272.2" width="2.44" height="23.2" fill="var(--up)"/>
<line x1="829.6" y1="263.2" x2="829.6" y2="293.7" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="276.3" width="2.44" height="6.3" fill="var(--up)"/>
<line x1="833.5" y1="275.5" x2="833.5" y2="319.3" stroke="var(--down)" class="wick"/>
<rect x="832.30" y="279.0" width="2.44" height="20.3" fill="var(--down)"/>
<line x1="837.5" y1="275.1" x2="837.5" y2="314.1" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="291.9" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="841.4" y1="277.4" x2="841.4" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="295.8" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="845.3" y1="296.5" x2="845.3" y2="352.7" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="307.5" width="2.44" height="37.5" fill="var(--down)"/>
<line x1="849.3" y1="138.0" x2="849.3" y2="225.8" stroke="var(--down)" class="wick"/>
<rect x="848.05" y="192.6" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="853.2" y1="119.4" x2="853.2" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="127.9" width="2.44" height="93.2" fill="var(--up)"/>
<line x1="857.1" y1="79.0" x2="857.1" y2="143.8" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="79.6" width="2.44" height="47.9" fill="var(--up)"/>
<line x1="861.1" y1="75.4" x2="861.1" y2="136.4" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="78.9" width="2.44" height="33.7" fill="var(--down)"/>
<line x1="865.0" y1="95.7" x2="865.0" y2="136.7" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="105.6" width="2.44" height="30.7" fill="var(--down)"/>
<line x1="869.0" y1="144.5" x2="869.0" y2="188.6" stroke="var(--down)" class="wick"/>
<rect x="867.73" y="144.5" width="2.44" height="43.1" fill="var(--down)"/>
<line x1="872.9" y1="181.5" x2="872.9" y2="211.3" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="193.2" width="2.44" height="6.3" fill="var(--up)"/>
<line x1="876.8" y1="159.4" x2="876.8" y2="190.5" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="170.4" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="880.8" y1="140.8" x2="880.8" y2="173.7" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="155.4" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="884.7" y1="123.4" x2="884.7" y2="180.0" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="144.7" width="2.44" height="26.6" fill="var(--down)"/>
<line x1="888.6" y1="173.2" x2="888.6" y2="213.4" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="181.3" width="2.44" height="25.3" fill="var(--down)"/>
<line x1="892.6" y1="178.2" x2="892.6" y2="227.5" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="184.3" width="2.44" height="31.4" fill="var(--up)"/>
<line x1="896.5" y1="139.6" x2="896.5" y2="199.0" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="181.2" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="900.4" y1="174.6" x2="900.4" y2="215.7" stroke="var(--up)" class="wick"/>
<rect x="899.22" y="188.4" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="904.4" y1="155.3" x2="904.4" y2="191.8" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="168.0" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="908.3" y1="165.7" x2="908.3" y2="192.2" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="179.3" width="2.44" height="6.8" fill="var(--down)"/>
<line x1="912.3" y1="168.9" x2="912.3" y2="204.2" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="188.5" width="2.44" height="14.4" fill="var(--down)"/>
<line x1="916.2" y1="175.2" x2="916.2" y2="204.8" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="180.7" width="2.44" height="19.2" fill="var(--up)"/>
<line x1="920.1" y1="184.0" x2="920.1" y2="220.9" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="189.2" width="2.44" height="24.3" fill="var(--down)"/>
<line x1="924.1" y1="179.3" x2="924.1" y2="213.5" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="210.2" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="928.0" y1="195.2" x2="928.0" y2="219.9" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="199.7" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="931.9" y1="98.9" x2="931.9" y2="183.9" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="114.4" width="2.44" height="51.9" fill="var(--down)"/>
<line x1="935.9" y1="156.7" x2="935.9" y2="220.9" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="170.2" width="2.44" height="29.0" fill="var(--down)"/>
<line x1="939.8" y1="192.2" x2="939.8" y2="228.2" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="197.6" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="943.7" y1="186.5" x2="943.7" y2="241.9" stroke="var(--up)" class="wick"/>
<rect x="942.53" y="200.3" width="2.44" height="23.6" fill="var(--up)"/>
<line x1="947.7" y1="185.7" x2="947.7" y2="208.2" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="195.8" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="951.6" y1="167.6" x2="951.6" y2="194.3" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="168.0" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="955.6" y1="144.8" x2="955.6" y2="193.2" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="146.2" width="2.44" height="38.4" fill="var(--up)"/>
<line x1="959.5" y1="116.4" x2="959.5" y2="159.2" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="116.8" width="2.44" height="26.0" fill="var(--up)"/>
<line x1="963.4" y1="96.2" x2="963.4" y2="122.6" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="109.8" width="2.44" height="8.2" fill="var(--up)"/>
<line x1="967.4" y1="114.5" x2="967.4" y2="149.3" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="115.7" width="2.44" height="26.6" fill="var(--down)"/>
<line x1="971.3" y1="122.0" x2="971.3" y2="151.0" stroke="var(--up)" class="wick"/>
<rect x="970.08" y="133.3" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="975.2" y1="110.5" x2="975.2" y2="141.7" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="111.9" width="2.44" height="19.0" fill="var(--up)"/>
<line x1="979.2" y1="118.0" x2="979.2" y2="170.6" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="118.6" width="2.44" height="43.6" fill="var(--down)"/>
<line x1="983.1" y1="136.7" x2="983.1" y2="153.6" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="147.5" width="2.44" height="3.5" fill="var(--up)"/>
<line x1="987.0" y1="129.5" x2="987.0" y2="152.0" stroke="var(--down)" class="wick"/>
<rect x="985.83" y="142.0" width="2.44" height="5.6" fill="var(--down)"/>
<line x1="991.0" y1="99.4" x2="991.0" y2="180.8" stroke="var(--down)" class="wick"/>
<rect x="989.76" y="152.2" width="2.44" height="13.3" fill="var(--down)"/>
<line x1="994.9" y1="118.0" x2="994.9" y2="168.1" stroke="var(--up)" class="wick"/>
<rect x="993.70" y="135.9" width="2.44" height="24.7" fill="var(--up)"/>
<line x1="998.9" y1="127.9" x2="998.9" y2="155.4" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="128.9" width="2.44" height="10.5" fill="var(--up)"/>
<line x1="1002.8" y1="126.8" x2="1002.8" y2="152.8" stroke="var(--down)" class="wick"/>
<rect x="1001.57" y="137.0" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="1006.7" y1="112.8" x2="1006.7" y2="150.5" stroke="var(--up)" class="wick"/>
<rect x="1005.51" y="126.3" width="2.44" height="19.5" fill="var(--up)"/>
<line x1="1010.7" y1="127.1" x2="1010.7" y2="151.7" stroke="var(--up)" class="wick"/>
<rect x="1009.45" y="133.6" width="2.44" height="7.2" fill="var(--up)"/>
<line x1="1014.6" y1="115.7" x2="1014.6" y2="135.4" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="117.4" width="2.44" height="6.5" fill="var(--up)"/>
<line x1="1018.5" y1="81.2" x2="1018.5" y2="126.5" stroke="var(--down)" class="wick"/>
<rect x="1017.32" y="105.8" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="1022.5" y1="112.4" x2="1022.5" y2="143.1" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="118.0" width="2.44" height="16.6" fill="var(--down)"/>
<line x1="1026.4" y1="94.4" x2="1026.4" y2="129.2" stroke="var(--up)" class="wick"/>
<rect x="1025.19" y="109.0" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="1030.3" y1="94.9" x2="1030.3" y2="151.6" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="98.7" width="2.44" height="42.6" fill="var(--down)"/>
<line x1="1034.3" y1="140.3" x2="1034.3" y2="166.2" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="153.5" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="1038.2" y1="150.0" x2="1038.2" y2="184.9" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="174.6" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="1042.2" y1="173.5" x2="1042.2" y2="204.1" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="181.6" width="2.44" height="15.4" fill="var(--down)"/>
<line x1="1046.1" y1="184.4" x2="1046.1" y2="214.1" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="193.9" width="2.44" height="12.9" fill="var(--down)"/>
<line x1="1050.0" y1="195.3" x2="1050.0" y2="216.7" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="204.1" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="60" y1="178.8" x2="1052" y2="178.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="182.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$298 R1</text>
<text x="1058" y="194.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="98.8" x2="1052" y2="98.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="102.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$311 R2</text>
<text x="1058" y="114.3" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="242.2" x2="1052" y2="242.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="236.2" font-size="11.5" fill="var(--support)" font-weight="600">$288 S1</text>
<text x="1058" y="248.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="344.6" x2="1052" y2="344.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="338.6" font-size="11.5" fill="var(--support)" font-weight="600">$271 S2</text>
<text x="1058" y="350.6" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="460.4" x2="1052" y2="460.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="454.4" font-size="11.5" fill="var(--support)" font-weight="600">$253 S3</text>
<text x="1058" y="466.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="210.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="202.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $293 (2026-09-11)</text>
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
| R2 | $311 | 7 | 2026-04-27·05-13·07-06·07-30·08-11·08-20·08-31 — 청정에너지 철수 발표 이후 다섯 달째 되밀린 상단대 |
| R1 | $298 | 3 | 2026-02-12·03-13·04-09 — 철수 발표 전 상단. 발표 후에는 이 대역이 지지로 바뀌었다가 9월 들어 다시 위로 올라섰다 |
| **현재가** | **$293.11** (2026-09-11 종가) | — | R1과 S1 사이 |
| S1 | $288 | 5 | 2026-04-08·04-17·05-07·07-16·08-04 — 현재가에 가장 근접한 지지. 최근 5개월간 반복적으로 되돌려진 대역 |
| S2 | $271 | 6 | 2025-09-26·2026-02-13·03-03·03-24·06-08·06-29 — 철수 발표 직전의 바닥권(2026-06-29 $271.35) |
| S3 | $253 | 4 | 2025-10-17·11-18·2026-01-20·01-28 — 2025년 4분기~2026년 1월 저점대. 현 레짐과 5개월 이상 떨어져 있다 |

> 유효 클러스터가 5개(R2~S3)라 R3 행은 두지 않았다 — 52주 최고($314.87)는 2026-07-02 단 하루의 고점이라 터치 2회 기준을 채우지 못한다. 현재가는 R1($298)과 S1($288)의 좁은 구간 안에 있다.

---

## 3. 관측된 특이 구간 — 2026-06-30 청정에너지 프로젝트 철수 발표

- 루이지애나 청정에너지 단지·애리조나 Casa Grande 그린수소 철수와 세전 약 $2.9B 손상 발표일이다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **+8.0%** ($271.35 → $293.18), 거래량은 평소(일 133만 주 내외) 대비 약 2.6배인 **351만 주**. 이틀 뒤 2026-07-02에는 52주 최고 $314.87까지 올랐다.
- **손상차손 발표에 주가가 급등한 것이 이 구간의 핵심**이다 — 시장은 $2.9B 상각을 손실이 아니라 "현금 유출이 이어지던 프로젝트의 종료"로 읽었다. 이 사건 이후 거래 레짐이 한 단계 위로 옮겨져, 발표 전 상단이던 $298 대역이 이후 지지 역할을 하고 상단은 $311로 재설정됐다. S3($253)처럼 그 이전 레짐에서 만들어진 레벨은 참고 이상의 의미를 두지 않는다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-11~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py APD --name "Air Products" --event 2026-06-30:"청정에너지 철수 발표" --event 2026-07-30:"Q3 실적·가이던스 상향" --close-on 2026-09-11 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간의 2026-06-30 갭업이 가격대를 구조적으로 재설정했다 — 그 이전 구간에서 만들어진 S2·S3는 같은 레짐의 레벨이 아니므로 현재가와의 거리만으로 해석하지 말 것.
    - 기간 내 주식분할·유상증자는 없었다. 분기배당 4회가 있었으나 원주가(배당 미반영) 기준이라 배당락만큼 차트가 낮게 찍혀 있다.

---

*작성일: 2026-09-12*
