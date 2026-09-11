# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-11 종가 **$465.09**는 핵심 지표·밸류에이션 / 적정주가에 인용된 기준 종가와 일치한다. ⚠️ 같은 날 종가를 수집 시점에 따라 $464.58~$465.29 범위로 받은 적이 있다(집계 지연으로 보인다) — 이 회사 폴더 전체는 위 값 하나로 통일했다.

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-11 ~ 2026-09-11)

<div class="lin-chart">
<style>
.lin-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .lin-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .lin-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lin-chart svg { width:100%; height:auto; display:block; }
.lin-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lin-chart .title { fill: var(--ink); font-weight:600; }
.lin-chart .grid { stroke: var(--grid); stroke-width:1; }
.lin-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Linde(LIN) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Linde (LIN) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-11 ~ 2026-09-11 · 마지막 종가 $465.09 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="568.2" x2="1052" y2="568.2" class="grid"/>
<text x="52" y="572.2" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="485.6" x2="1052" y2="485.6" class="grid"/>
<text x="52" y="489.6" font-size="11" text-anchor="end" fill="var(--muted)">425</text>
<line x1="60" y1="403.0" x2="1052" y2="403.0" class="grid"/>
<text x="52" y="407.0" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="320.3" x2="1052" y2="320.3" class="grid"/>
<text x="52" y="324.3" font-size="11" text-anchor="end" fill="var(--muted)">475</text>
<line x1="60" y1="237.7" x2="1052" y2="237.7" class="grid"/>
<text x="52" y="241.7" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="155.1" x2="1052" y2="155.1" class="grid"/>
<text x="52" y="159.1" font-size="11" text-anchor="end" fill="var(--muted)">525</text>
<line x1="60" y1="72.5" x2="1052" y2="72.5" class="grid"/>
<text x="52" y="76.5" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
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
<line x1="935.9" y1="56.0" x2="935.9" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="941.9" y="68.0" font-size="10.5" fill="var(--down)">2026-07-31 Q2 실적·Lincare 우려 갭다운</text>
<line x1="62.0" y1="289.2" x2="62.0" y2="328.7" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="292.0" width="2.44" height="35.3" fill="var(--up)"/>
<line x1="65.9" y1="290.9" x2="65.9" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="297.1" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="69.8" y1="292.9" x2="69.8" y2="318.6" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="299.3" width="2.44" height="15.4" fill="var(--down)"/>
<line x1="73.8" y1="309.0" x2="73.8" y2="333.9" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="315.6" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="77.7" y1="299.3" x2="77.7" y2="330.2" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="304.3" width="2.44" height="19.7" fill="var(--up)"/>
<line x1="81.7" y1="304.0" x2="81.7" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="307.5" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="85.6" y1="300.9" x2="85.6" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="84.37" y="307.1" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="89.5" y1="308.2" x2="89.5" y2="322.7" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="311.2" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="93.5" y1="294.0" x2="93.5" y2="321.5" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="304.0" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="97.4" y1="298.1" x2="97.4" y2="325.9" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="305.1" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="101.3" y1="315.9" x2="101.3" y2="337.2" stroke="var(--down)" class="wick"/>
<rect x="100.11" y="323.2" width="2.44" height="1.2" fill="var(--down)"/>
<line x1="105.3" y1="319.8" x2="105.3" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="322.3" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="109.2" y1="314.7" x2="109.2" y2="332.2" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="315.4" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="113.1" y1="307.9" x2="113.1" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="320.3" width="2.44" height="4.3" fill="var(--up)"/>
<line x1="117.1" y1="320.1" x2="117.1" y2="367.3" stroke="var(--down)" class="wick"/>
<rect x="115.86" y="327.7" width="2.44" height="19.7" fill="var(--down)"/>
<line x1="121.0" y1="335.9" x2="121.0" y2="360.2" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="338.6" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="125.0" y1="338.8" x2="125.0" y2="360.0" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="346.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="128.9" y1="335.0" x2="128.9" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="127.67" y="341.7" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="132.8" y1="335.0" x2="132.8" y2="350.5" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="335.6" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="136.8" y1="331.3" x2="136.8" y2="345.0" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="335.8" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="140.7" y1="336.9" x2="140.7" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="344.0" width="2.44" height="32.0" fill="var(--down)"/>
<line x1="144.6" y1="359.9" x2="144.6" y2="393.3" stroke="var(--down)" class="wick"/>
<rect x="143.41" y="376.3" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="148.6" y1="370.6" x2="148.6" y2="386.4" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="381.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="152.5" y1="363.1" x2="152.5" y2="392.8" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="372.4" width="2.44" height="19.8" fill="var(--up)"/>
<line x1="156.4" y1="364.9" x2="156.4" y2="400.3" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="373.1" width="2.44" height="25.1" fill="var(--down)"/>
<line x1="160.4" y1="394.8" x2="160.4" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="396.2" width="2.44" height="25.8" fill="var(--down)"/>
<line x1="164.3" y1="398.6" x2="164.3" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="400.0" width="2.44" height="22.1" fill="var(--up)"/>
<line x1="168.3" y1="385.6" x2="168.3" y2="403.9" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="395.2" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="172.2" y1="394.9" x2="172.2" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="170.97" y="401.1" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="176.1" y1="386.2" x2="176.1" y2="410.4" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="401.9" width="2.44" height="1.4" fill="var(--down)"/>
<line x1="180.1" y1="394.1" x2="180.1" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="394.4" width="2.44" height="8.3" fill="var(--down)"/>
<line x1="184.0" y1="401.6" x2="184.0" y2="417.5" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="404.5" width="2.44" height="11.7" fill="var(--down)"/>
<line x1="187.9" y1="402.5" x2="187.9" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="186.72" y="410.7" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="191.9" y1="412.1" x2="191.9" y2="429.4" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="417.9" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="195.8" y1="437.9" x2="195.8" y2="465.0" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="440.0" width="2.44" height="22.4" fill="var(--down)"/>
<line x1="199.7" y1="451.9" x2="199.7" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="460.9" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="203.7" y1="480.9" x2="203.7" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="485.6" width="2.44" height="22.1" fill="var(--down)"/>
<line x1="207.6" y1="494.7" x2="207.6" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="494.7" width="2.44" height="33.3" fill="var(--down)"/>
<line x1="211.6" y1="497.7" x2="211.6" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="508.9" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="215.5" y1="502.8" x2="215.5" y2="518.6" stroke="var(--up)" class="wick"/>
<rect x="214.27" y="507.9" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="219.4" y1="503.8" x2="219.4" y2="523.3" stroke="var(--down)" class="wick"/>
<rect x="218.21" y="514.1" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="223.4" y1="492.8" x2="223.4" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="500.4" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="227.3" y1="494.9" x2="227.3" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="226.08" y="499.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="231.2" y1="474.3" x2="231.2" y2="495.7" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="480.1" width="2.44" height="3.0" fill="var(--up)"/>
<line x1="235.2" y1="463.9" x2="235.2" y2="485.9" stroke="var(--up)" class="wick"/>
<rect x="233.95" y="472.5" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="239.1" y1="472.3" x2="239.1" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="237.89" y="473.5" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="243.0" y1="468.7" x2="243.0" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="473.5" width="2.44" height="17.3" fill="var(--down)"/>
<line x1="247.0" y1="490.9" x2="247.0" y2="510.1" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="496.8" width="2.44" height="12.4" fill="var(--down)"/>
<line x1="250.9" y1="504.1" x2="250.9" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="506.3" width="2.44" height="13.3" fill="var(--down)"/>
<line x1="254.9" y1="515.1" x2="254.9" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="519.5" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="258.8" y1="515.5" x2="258.8" y2="541.0" stroke="var(--down)" class="wick"/>
<rect x="257.57" y="519.9" width="2.44" height="20.1" fill="var(--down)"/>
<line x1="262.7" y1="513.9" x2="262.7" y2="547.0" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="526.1" width="2.44" height="17.7" fill="var(--up)"/>
<line x1="266.7" y1="527.0" x2="266.7" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="265.45" y="534.3" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="270.6" y1="525.6" x2="270.6" y2="548.1" stroke="var(--down)" class="wick"/>
<rect x="269.38" y="529.6" width="2.44" height="12.6" fill="var(--down)"/>
<line x1="274.5" y1="533.5" x2="274.5" y2="544.9" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="542.1" width="2.44" height="1.3" fill="var(--up)"/>
<line x1="278.5" y1="529.9" x2="278.5" y2="546.8" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="534.1" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="282.4" y1="529.9" x2="282.4" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="281.19" y="535.1" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="286.3" y1="530.8" x2="286.3" y2="554.1" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="539.1" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="290.3" y1="531.8" x2="290.3" y2="548.3" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="537.9" width="2.44" height="2.7" fill="var(--up)"/>
<line x1="294.2" y1="539.3" x2="294.2" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="543.0" width="2.44" height="12.8" fill="var(--down)"/>
<line x1="298.2" y1="552.9" x2="298.2" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="555.1" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="302.1" y1="570.1" x2="302.1" y2="608.6" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="572.3" width="2.44" height="31.0" fill="var(--down)"/>
<line x1="306.0" y1="578.6" x2="306.0" y2="600.9" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="597.2" width="2.44" height="2.7" fill="var(--down)"/>
<line x1="310.0" y1="586.8" x2="310.0" y2="604.5" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="592.4" width="2.44" height="10.1" fill="var(--up)"/>
<line x1="313.9" y1="554.0" x2="313.9" y2="585.1" stroke="var(--up)" class="wick"/>
<rect x="312.68" y="557.3" width="2.44" height="26.6" fill="var(--up)"/>
<line x1="317.8" y1="508.6" x2="317.8" y2="545.9" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="514.5" width="2.44" height="31.4" fill="var(--up)"/>
<line x1="321.8" y1="497.1" x2="321.8" y2="535.1" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="510.6" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="325.7" y1="487.4" x2="325.7" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="490.5" width="2.44" height="16.5" fill="var(--up)"/>
<line x1="329.7" y1="487.5" x2="329.7" y2="499.5" stroke="var(--down)" class="wick"/>
<rect x="328.43" y="492.2" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="333.6" y1="487.3" x2="333.6" y2="507.1" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="497.0" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="337.5" y1="490.9" x2="337.5" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="497.4" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="341.5" y1="484.6" x2="341.5" y2="500.3" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="490.5" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="345.4" y1="484.5" x2="345.4" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="344.18" y="485.2" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="349.3" y1="480.2" x2="349.3" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="485.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="353.3" y1="482.3" x2="353.3" y2="490.8" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="484.2" width="2.44" height="2.1" fill="var(--down)"/>
<line x1="357.2" y1="478.0" x2="357.2" y2="489.7" stroke="var(--up)" class="wick"/>
<rect x="355.99" y="480.5" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="361.1" y1="470.8" x2="361.1" y2="490.9" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="474.5" width="2.44" height="14.4" fill="var(--up)"/>
<line x1="365.1" y1="472.3" x2="365.1" y2="481.3" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="478.6" width="2.44" height="2.4" fill="var(--down)"/>
<line x1="369.0" y1="466.4" x2="369.0" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="472.0" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="373.0" y1="455.9" x2="373.0" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="458.8" width="2.44" height="24.7" fill="var(--up)"/>
<line x1="376.9" y1="439.3" x2="376.9" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="375.67" y="445.4" width="2.44" height="10.2" fill="var(--up)"/>
<line x1="380.8" y1="439.2" x2="380.8" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="446.2" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="384.8" y1="428.0" x2="384.8" y2="461.1" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="437.0" width="2.44" height="20.7" fill="var(--up)"/>
<line x1="388.7" y1="419.3" x2="388.7" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="422.5" width="2.44" height="20.7" fill="var(--up)"/>
<line x1="392.6" y1="416.2" x2="392.6" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="424.0" width="2.44" height="4.1" fill="var(--up)"/>
<line x1="396.6" y1="420.6" x2="396.6" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="395.35" y="422.9" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="400.5" y1="421.6" x2="400.5" y2="442.9" stroke="var(--down)" class="wick"/>
<rect x="399.29" y="430.0" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="404.4" y1="422.8" x2="404.4" y2="443.5" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="430.1" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="408.4" y1="434.2" x2="408.4" y2="450.3" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="437.8" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="412.3" y1="452.8" x2="412.3" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="454.8" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="416.3" y1="432.9" x2="416.3" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="438.1" width="2.44" height="19.4" fill="var(--up)"/>
<line x1="420.2" y1="411.9" x2="420.2" y2="436.5" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="417.4" width="2.44" height="19.1" fill="var(--up)"/>
<line x1="424.1" y1="396.4" x2="424.1" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="397.8" width="2.44" height="27.5" fill="var(--up)"/>
<line x1="428.1" y1="384.5" x2="428.1" y2="395.9" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="386.3" width="2.44" height="7.9" fill="var(--up)"/>
<line x1="432.0" y1="379.8" x2="432.0" y2="394.9" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="386.3" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="435.9" y1="391.4" x2="435.9" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="434.72" y="394.1" width="2.44" height="3.9" fill="var(--down)"/>
<line x1="439.9" y1="383.0" x2="439.9" y2="409.0" stroke="var(--up)" class="wick"/>
<rect x="438.65" y="386.4" width="2.44" height="6.9" fill="var(--up)"/>
<line x1="443.8" y1="378.6" x2="443.8" y2="397.7" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="379.9" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="447.7" y1="362.1" x2="447.7" y2="376.5" stroke="var(--up)" class="wick"/>
<rect x="446.53" y="369.4" width="2.44" height="2.7" fill="var(--up)"/>
<line x1="451.7" y1="347.4" x2="451.7" y2="375.6" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="358.1" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="455.6" y1="312.6" x2="455.6" y2="351.3" stroke="var(--up)" class="wick"/>
<rect x="454.40" y="325.9" width="2.44" height="23.5" fill="var(--up)"/>
<line x1="459.6" y1="322.4" x2="459.6" y2="372.4" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="333.3" width="2.44" height="37.6" fill="var(--down)"/>
<line x1="463.5" y1="376.6" x2="463.5" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="383.5" width="2.44" height="25.3" fill="var(--down)"/>
<line x1="467.4" y1="378.2" x2="467.4" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="466.21" y="382.0" width="2.44" height="27.0" fill="var(--up)"/>
<line x1="471.4" y1="356.2" x2="471.4" y2="389.1" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="368.2" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="475.3" y1="344.6" x2="475.3" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="345.1" width="2.44" height="30.0" fill="var(--up)"/>
<line x1="479.2" y1="311.9" x2="479.2" y2="338.6" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="327.4" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="483.2" y1="275.6" x2="483.2" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="300.5" width="2.44" height="22.6" fill="var(--up)"/>
<line x1="487.1" y1="291.4" x2="487.1" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="296.5" width="2.44" height="10.2" fill="var(--up)"/>
<line x1="491.0" y1="276.5" x2="491.0" y2="295.2" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="286.4" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="495.0" y1="269.0" x2="495.0" y2="296.6" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="270.4" width="2.44" height="17.2" fill="var(--up)"/>
<line x1="498.9" y1="243.2" x2="498.9" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="249.3" width="2.44" height="27.3" fill="var(--up)"/>
<line x1="502.9" y1="235.9" x2="502.9" y2="261.6" stroke="var(--up)" class="wick"/>
<rect x="501.64" y="243.7" width="2.44" height="15.3" fill="var(--up)"/>
<line x1="506.8" y1="222.9" x2="506.8" y2="255.7" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="224.5" width="2.44" height="20.3" fill="var(--up)"/>
<line x1="510.7" y1="206.0" x2="510.7" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="210.4" width="2.44" height="4.7" fill="var(--up)"/>
<line x1="514.7" y1="202.5" x2="514.7" y2="246.2" stroke="var(--down)" class="wick"/>
<rect x="513.45" y="215.0" width="2.44" height="27.7" fill="var(--down)"/>
<line x1="518.6" y1="206.2" x2="518.6" y2="243.5" stroke="var(--up)" class="wick"/>
<rect x="517.38" y="211.0" width="2.44" height="32.4" fill="var(--up)"/>
<line x1="522.5" y1="204.5" x2="522.5" y2="239.3" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="206.9" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="526.5" y1="225.7" x2="526.5" y2="265.5" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="232.2" width="2.44" height="5.6" fill="var(--up)"/>
<line x1="530.4" y1="224.6" x2="530.4" y2="246.5" stroke="var(--down)" class="wick"/>
<rect x="529.19" y="230.4" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="534.3" y1="246.8" x2="534.3" y2="275.6" stroke="var(--down)" class="wick"/>
<rect x="533.13" y="252.3" width="2.44" height="18.3" fill="var(--down)"/>
<line x1="538.3" y1="276.4" x2="538.3" y2="304.9" stroke="var(--down)" class="wick"/>
<rect x="537.07" y="277.4" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="542.2" y1="282.2" x2="542.2" y2="307.7" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="291.9" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="546.2" y1="293.8" x2="546.2" y2="321.6" stroke="var(--down)" class="wick"/>
<rect x="544.94" y="301.2" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="550.1" y1="297.1" x2="550.1" y2="333.1" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="298.7" width="2.44" height="14.5" fill="var(--up)"/>
<line x1="554.0" y1="261.5" x2="554.0" y2="312.0" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="269.4" width="2.44" height="33.1" fill="var(--up)"/>
<line x1="558.0" y1="237.7" x2="558.0" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="244.3" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="561.9" y1="242.8" x2="561.9" y2="267.8" stroke="var(--up)" class="wick"/>
<rect x="560.68" y="246.3" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="565.8" y1="236.6" x2="565.8" y2="260.1" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="246.3" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="569.8" y1="256.0" x2="569.8" y2="276.1" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="266.0" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="573.7" y1="264.9" x2="573.7" y2="292.4" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="271.4" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="577.7" y1="251.6" x2="577.7" y2="289.5" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="261.2" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="581.6" y1="269.9" x2="581.6" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="274.5" width="2.44" height="35.7" fill="var(--down)"/>
<line x1="585.5" y1="281.2" x2="585.5" y2="325.5" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="304.4" width="2.44" height="19.5" fill="var(--up)"/>
<line x1="589.5" y1="262.8" x2="589.5" y2="297.4" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="263.1" width="2.44" height="30.4" fill="var(--up)"/>
<line x1="593.4" y1="236.7" x2="593.4" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="592.18" y="252.6" width="2.44" height="14.0" fill="var(--up)"/>
<line x1="597.3" y1="243.5" x2="597.3" y2="282.6" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="245.6" width="2.44" height="21.4" fill="var(--down)"/>
<line x1="601.3" y1="225.7" x2="601.3" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="240.2" width="2.44" height="11.3" fill="var(--up)"/>
<line x1="605.2" y1="236.8" x2="605.2" y2="264.5" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="250.5" width="2.44" height="1.3" fill="var(--down)"/>
<line x1="609.1" y1="256.1" x2="609.1" y2="275.8" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="258.1" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="613.1" y1="228.8" x2="613.1" y2="256.3" stroke="var(--up)" class="wick"/>
<rect x="611.86" y="229.1" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="617.0" y1="225.6" x2="617.0" y2="246.8" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="225.6" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="621.0" y1="236.1" x2="621.0" y2="270.2" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="238.4" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="624.9" y1="234.9" x2="624.9" y2="294.7" stroke="var(--up)" class="wick"/>
<rect x="623.67" y="236.2" width="2.44" height="41.2" fill="var(--up)"/>
<line x1="628.8" y1="214.0" x2="628.8" y2="245.9" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="226.8" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="632.8" y1="216.8" x2="632.8" y2="238.6" stroke="var(--down)" class="wick"/>
<rect x="631.54" y="218.1" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="636.7" y1="207.2" x2="636.7" y2="228.5" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="208.4" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="640.6" y1="226.6" x2="640.6" y2="255.4" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="229.5" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="644.6" y1="238.9" x2="644.6" y2="267.8" stroke="var(--up)" class="wick"/>
<rect x="643.35" y="244.5" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="648.5" y1="235.4" x2="648.5" y2="254.1" stroke="var(--up)" class="wick"/>
<rect x="647.29" y="240.3" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="652.4" y1="244.5" x2="652.4" y2="277.4" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="249.1" width="2.44" height="14.3" fill="var(--down)"/>
<line x1="656.4" y1="233.2" x2="656.4" y2="262.5" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="243.9" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="660.3" y1="244.3" x2="660.3" y2="263.1" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="252.4" width="2.44" height="2.4" fill="var(--down)"/>
<line x1="664.3" y1="233.7" x2="664.3" y2="257.8" stroke="var(--down)" class="wick"/>
<rect x="663.03" y="249.4" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="668.2" y1="210.4" x2="668.2" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="666.97" y="211.1" width="2.44" height="29.8" fill="var(--up)"/>
<line x1="672.1" y1="202.5" x2="672.1" y2="231.9" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="203.7" width="2.44" height="10.2" fill="var(--up)"/>
<line x1="676.1" y1="194.9" x2="676.1" y2="216.2" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="202.2" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="680.0" y1="186.1" x2="680.0" y2="208.0" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="194.8" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="683.9" y1="208.0" x2="683.9" y2="226.3" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="210.6" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="687.9" y1="212.5" x2="687.9" y2="238.9" stroke="var(--down)" class="wick"/>
<rect x="686.65" y="231.2" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="691.8" y1="167.4" x2="691.8" y2="231.1" stroke="var(--up)" class="wick"/>
<rect x="690.59" y="211.6" width="2.44" height="15.1" fill="var(--up)"/>
<line x1="695.7" y1="216.9" x2="695.7" y2="262.5" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="225.9" width="2.44" height="33.1" fill="var(--down)"/>
<line x1="699.7" y1="227.1" x2="699.7" y2="269.5" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="236.8" width="2.44" height="18.8" fill="var(--up)"/>
<line x1="703.6" y1="220.7" x2="703.6" y2="247.4" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="231.6" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="707.6" y1="225.4" x2="707.6" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="234.7" width="2.44" height="23.4" fill="var(--down)"/>
<line x1="711.5" y1="245.7" x2="711.5" y2="263.3" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="257.6" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="715.4" y1="217.2" x2="715.4" y2="258.1" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="223.2" width="2.44" height="34.7" fill="var(--up)"/>
<line x1="719.4" y1="218.6" x2="719.4" y2="248.5" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="223.9" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="723.3" y1="185.7" x2="723.3" y2="225.6" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="193.9" width="2.44" height="29.9" fill="var(--up)"/>
<line x1="727.2" y1="188.9" x2="727.2" y2="210.3" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="191.3" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="731.2" y1="181.5" x2="731.2" y2="224.1" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="182.3" width="2.44" height="35.2" fill="var(--down)"/>
<line x1="735.1" y1="191.0" x2="735.1" y2="222.4" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="201.9" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="739.0" y1="203.5" x2="739.0" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="209.0" width="2.44" height="8.7" fill="var(--down)"/>
<line x1="743.0" y1="196.8" x2="743.0" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="215.8" width="2.44" height="20.9" fill="var(--up)"/>
<line x1="746.9" y1="183.1" x2="746.9" y2="218.7" stroke="var(--up)" class="wick"/>
<rect x="745.70" y="189.8" width="2.44" height="16.7" fill="var(--up)"/>
<line x1="750.9" y1="167.6" x2="750.9" y2="188.2" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="179.6" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="754.8" y1="174.7" x2="754.8" y2="195.8" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="178.8" width="2.44" height="9.5" fill="var(--down)"/>
<line x1="758.7" y1="185.4" x2="758.7" y2="212.3" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="194.8" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="762.7" y1="210.5" x2="762.7" y2="242.4" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="211.8" width="2.44" height="19.4" fill="var(--down)"/>
<line x1="766.6" y1="229.4" x2="766.6" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="237.7" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="770.5" y1="243.2" x2="770.5" y2="274.5" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="246.3" width="2.44" height="4.2" fill="var(--up)"/>
<line x1="774.5" y1="238.4" x2="774.5" y2="269.3" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="251.3" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="778.4" y1="197.4" x2="778.4" y2="250.5" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="212.7" width="2.44" height="31.1" fill="var(--up)"/>
<line x1="782.3" y1="197.6" x2="782.3" y2="222.8" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="209.3" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="786.3" y1="179.5" x2="786.3" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="197.1" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="790.2" y1="203.8" x2="790.2" y2="237.9" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="214.2" width="2.44" height="17.2" fill="var(--down)"/>
<line x1="794.2" y1="181.3" x2="794.2" y2="216.7" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="186.2" width="2.44" height="25.2" fill="var(--up)"/>
<line x1="798.1" y1="162.1" x2="798.1" y2="221.3" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="164.2" width="2.44" height="43.3" fill="var(--down)"/>
<line x1="802.0" y1="176.3" x2="802.0" y2="198.1" stroke="var(--up)" class="wick"/>
<rect x="800.81" y="186.7" width="2.44" height="4.7" fill="var(--up)"/>
<line x1="806.0" y1="152.4" x2="806.0" y2="180.9" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="159.9" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="809.9" y1="152.3" x2="809.9" y2="179.0" stroke="var(--up)" class="wick"/>
<rect x="808.68" y="166.8" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="813.8" y1="159.6" x2="813.8" y2="192.9" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="169.8" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="817.8" y1="173.0" x2="817.8" y2="200.0" stroke="var(--up)" class="wick"/>
<rect x="816.56" y="185.4" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="821.7" y1="175.5" x2="821.7" y2="200.9" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="184.7" width="2.44" height="12.9" fill="var(--down)"/>
<line x1="825.7" y1="178.3" x2="825.7" y2="214.2" stroke="var(--up)" class="wick"/>
<rect x="824.43" y="182.5" width="2.44" height="28.9" fill="var(--up)"/>
<line x1="829.6" y1="158.8" x2="829.6" y2="208.9" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="158.8" width="2.44" height="38.4" fill="var(--down)"/>
<line x1="833.5" y1="162.8" x2="833.5" y2="190.2" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="185.8" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="837.5" y1="145.4" x2="837.5" y2="192.1" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="164.1" width="2.44" height="23.1" fill="var(--up)"/>
<line x1="841.4" y1="155.1" x2="841.4" y2="177.1" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="168.3" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="845.3" y1="172.7" x2="845.3" y2="215.3" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="174.6" width="2.44" height="26.6" fill="var(--down)"/>
<line x1="849.3" y1="163.1" x2="849.3" y2="199.5" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="175.2" width="2.44" height="21.7" fill="var(--up)"/>
<line x1="853.2" y1="109.0" x2="853.2" y2="181.6" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="126.9" width="2.44" height="27.2" fill="var(--up)"/>
<line x1="857.1" y1="81.7" x2="857.1" y2="128.8" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="83.6" width="2.44" height="37.0" fill="var(--up)"/>
<line x1="861.1" y1="92.0" x2="861.1" y2="134.6" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="93.3" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="865.0" y1="78.5" x2="865.0" y2="120.9" stroke="var(--down)" class="wick"/>
<rect x="863.80" y="82.5" width="2.44" height="28.9" fill="var(--down)"/>
<line x1="869.0" y1="115.3" x2="869.0" y2="151.2" stroke="var(--down)" class="wick"/>
<rect x="867.73" y="118.4" width="2.44" height="27.9" fill="var(--down)"/>
<line x1="872.9" y1="145.7" x2="872.9" y2="174.9" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="151.8" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="876.8" y1="129.7" x2="876.8" y2="160.2" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="139.3" width="2.44" height="15.6" fill="var(--up)"/>
<line x1="880.8" y1="130.5" x2="880.8" y2="166.8" stroke="var(--down)" class="wick"/>
<rect x="879.54" y="135.6" width="2.44" height="22.7" fill="var(--down)"/>
<line x1="884.7" y1="133.3" x2="884.7" y2="168.3" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="157.1" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="888.6" y1="168.0" x2="888.6" y2="193.5" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="176.1" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="892.6" y1="164.5" x2="892.6" y2="202.5" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="169.2" width="2.44" height="24.8" fill="var(--up)"/>
<line x1="896.5" y1="147.0" x2="896.5" y2="199.1" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="164.4" width="2.44" height="29.6" fill="var(--down)"/>
<line x1="900.4" y1="183.2" x2="900.4" y2="201.6" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="192.9" width="2.44" height="5.1" fill="var(--down)"/>
<line x1="904.4" y1="195.3" x2="904.4" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="198.4" width="2.44" height="22.7" fill="var(--down)"/>
<line x1="908.3" y1="201.5" x2="908.3" y2="220.9" stroke="var(--up)" class="wick"/>
<rect x="907.10" y="209.1" width="2.44" height="6.0" fill="var(--up)"/>
<line x1="912.3" y1="201.7" x2="912.3" y2="230.8" stroke="var(--up)" class="wick"/>
<rect x="911.03" y="216.9" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="916.2" y1="195.0" x2="916.2" y2="221.6" stroke="var(--up)" class="wick"/>
<rect x="914.97" y="197.2" width="2.44" height="22.6" fill="var(--up)"/>
<line x1="920.1" y1="188.2" x2="920.1" y2="216.4" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="193.7" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="924.1" y1="165.0" x2="924.1" y2="204.7" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="197.9" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="928.0" y1="192.6" x2="928.0" y2="220.8" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="198.8" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="931.9" y1="188.9" x2="931.9" y2="229.1" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="203.3" width="2.44" height="5.9" fill="var(--down)"/>
<line x1="935.9" y1="290.8" x2="935.9" y2="347.2" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="309.2" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="939.8" y1="287.3" x2="939.8" y2="315.7" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="293.7" width="2.44" height="8.6" fill="var(--down)"/>
<line x1="943.7" y1="285.3" x2="943.7" y2="308.8" stroke="var(--up)" class="wick"/>
<rect x="942.53" y="288.5" width="2.44" height="8.8" fill="var(--up)"/>
<line x1="947.7" y1="255.2" x2="947.7" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="267.3" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="951.6" y1="240.4" x2="951.6" y2="272.9" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="244.6" width="2.44" height="25.8" fill="var(--down)"/>
<line x1="955.6" y1="260.7" x2="955.6" y2="283.3" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="270.8" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="959.5" y1="262.3" x2="959.5" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="262.7" width="2.44" height="10.5" fill="var(--up)"/>
<line x1="963.4" y1="251.1" x2="963.4" y2="270.8" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="267.3" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="967.4" y1="269.7" x2="967.4" y2="308.0" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="277.9" width="2.44" height="27.8" fill="var(--down)"/>
<line x1="971.3" y1="293.0" x2="971.3" y2="317.9" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="304.3" width="2.44" height="5.5" fill="var(--down)"/>
<line x1="975.2" y1="292.3" x2="975.2" y2="313.3" stroke="var(--up)" class="wick"/>
<rect x="974.02" y="294.8" width="2.44" height="12.1" fill="var(--up)"/>
<line x1="979.2" y1="296.0" x2="979.2" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="297.2" width="2.44" height="25.3" fill="var(--down)"/>
<line x1="983.1" y1="292.3" x2="983.1" y2="311.4" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="298.3" width="2.44" height="9.8" fill="var(--down)"/>
<line x1="987.0" y1="290.7" x2="987.0" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="300.1" width="2.44" height="8.7" fill="var(--up)"/>
<line x1="991.0" y1="271.4" x2="991.0" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="299.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="994.9" y1="264.9" x2="994.9" y2="295.7" stroke="var(--up)" class="wick"/>
<rect x="993.70" y="278.8" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="998.9" y1="265.9" x2="998.9" y2="287.3" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="270.7" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="1002.8" y1="268.7" x2="1002.8" y2="286.9" stroke="var(--down)" class="wick"/>
<rect x="1001.57" y="273.4" width="2.44" height="6.6" fill="var(--down)"/>
<line x1="1006.7" y1="255.9" x2="1006.7" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="1005.51" y="269.7" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="1010.7" y1="281.7" x2="1010.7" y2="300.5" stroke="var(--up)" class="wick"/>
<rect x="1009.45" y="286.1" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="1014.6" y1="272.1" x2="1014.6" y2="281.7" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="272.4" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="1018.5" y1="262.6" x2="1018.5" y2="282.5" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="272.2" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="1022.5" y1="274.2" x2="1022.5" y2="296.7" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="275.7" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="1026.4" y1="267.5" x2="1026.4" y2="285.6" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="277.4" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="1030.3" y1="264.2" x2="1030.3" y2="303.7" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="277.7" width="2.44" height="18.9" fill="var(--down)"/>
<line x1="1034.3" y1="294.0" x2="1034.3" y2="315.5" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="306.3" width="2.44" height="5.6" fill="var(--down)"/>
<line x1="1038.2" y1="323.6" x2="1038.2" y2="350.1" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="323.6" width="2.44" height="18.6" fill="var(--down)"/>
<line x1="1042.2" y1="342.2" x2="1042.2" y2="358.8" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="342.2" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="1046.1" y1="346.4" x2="1046.1" y2="369.3" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="352.0" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="1050.0" y1="350.2" x2="1050.0" y2="367.6" stroke="var(--up)" class="wick"/>
<rect x="1048.81" y="353.1" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="60" y1="303.3" x2="1052" y2="303.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="306.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$480 R1</text>
<text x="1058" y="318.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="225.6" x2="1052" y2="225.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="229.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$504 R2</text>
<text x="1058" y="241.1" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="163.1" x2="1052" y2="163.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="166.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$523 R3</text>
<text x="1058" y="178.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="427.8" x2="1052" y2="427.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="421.8" font-size="11.5" fill="var(--support)" font-weight="600">$442 S1</text>
<text x="1058" y="433.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="483.5" x2="1052" y2="483.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="477.5" font-size="11.5" fill="var(--support)" font-weight="600">$426 S2</text>
<text x="1058" y="489.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="353.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="345.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $465 (2026-09-11)</text>
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
| R3 | $523 | 4 | 2026-05-01·05-22·06-15·07-28 — 실적 갭다운 직전까지 넉 달간 반복 확인된 상단대. 52주 최고($548.20)는 이 위 |
| R2 | $504 | 4 | 2026-02-26·03-17·04-13·08-26 — 갭다운 전후 모두에서 확인된 대역. 8월 회복 국면의 상단이었다 |
| R1 | $480 | 2 | 2025-09-23·2026-02-04 — 현재가 바로 위. 9월 조정으로 이 대역 아래로 내려왔다 |
| **현재가** | **$465.09** (2026-09-11 종가) | — | R1과 S1 사이 |
| S1 | $442 | 2 | 2025-10-16·2026-02-09 — 현재가에 가장 근접한 지지 |
| S2 | $426 | 2 | 2026-01-02·01-20 — 2025년 말 종가($426.39)와 겹치는 대역 |

> 유효 클러스터가 5개(R3~S2)라 S3 행은 두지 않았다 — 52주 최저($387.78)는 2025년 10월 이전 레짐의 값이라 터치 2회 기준을 채우지 못하고 현재가와도 17% 떨어져 있다. **현재가($465.09)는 R1($480)과 S1($442) 사이의 빈 구간에 있어 근접한 레벨이 없다** — 9월 조정이 이 구간을 빠르게 통과한 결과다.

---

## 3. 관측된 특이 구간 — 2026-07-31 Q2 실적 갭다운

- 매출·Adjusted EPS가 컨센서스를 상회했음에도 Adjusted 영업이익률 60bp 하락과 미국 홈케어(Lincare) 부진이 부각된 날이다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **−5.9%** ($508.64 → $478.38), 거래량은 평소(일 240만 주 내외) 대비 약 2.2배인 **522만 주**.
- 이 갭다운 이후 8월 내내 $480~$490대로 되돌렸으나(2026-08-28 $489.51), **9월 들어 증권사 목표주가 하향이 이어지며 다시 −5.0% 밀려 $465선까지 내려왔다.** 그 결과 갭다운 이전 레짐에서 만들어진 R3($523)는 현재가와 12% 떨어져 근시일 저항으로 보기 어렵고, 실질적인 상단은 R1($480)이다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-09-11~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py LIN --name Linde --event 2026-07-31:"Q2 실적·Lincare 우려 갭다운" --close-on 2026-09-11 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간의 2026-07-31 갭다운이 가격대를 재설정했다 — R3·R2는 그 이전 레짐에서 형성된 레벨이므로 현재가와의 거리만으로 해석하지 말 것.
    - 기간 내 주식분할·유상증자는 없었다. 분기배당 4회가 있었으나 원주가(배당 미반영) 기준이라 배당락만큼 차트가 낮게 찍혀 있다.

---

*작성일: 2026-09-12*
