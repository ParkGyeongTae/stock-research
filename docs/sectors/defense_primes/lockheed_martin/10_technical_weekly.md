# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉으로 다년 구조를 본 참고 자료. 1년 단위 흐름은 [기술적 분석 — 일봉](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 2026-09-11 종가 **$524.19**는 [기술적 분석 — 일봉](./09_technical_daily.md)·[밸류에이션 / 적정주가](./06_valuation.md)의 값과 일치한다.
- **최근 5년 범위**: 최고 $692.00 · 최저 $324.23 · 주평균 거래량 6,711,602주.

:::

---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-11)

<style>
.lmt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .lmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lmt-chart svg { width:100%; height:auto; display:block; }
.lmt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lmt-chart .title { fill: var(--ink); font-weight:600; }
.lmt-chart .grid { stroke: var(--grid); stroke-width:1; }
.lmt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="lmt-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="록히드마틴(LMT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">록히드마틴 (LMT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-11 · 마지막 종가 $524.19 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="568.3" x2="1052" y2="568.3" class="grid"/>
<text x="52" y="572.3" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="496.1" x2="1052" y2="496.1" class="grid"/>
<text x="52" y="500.1" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="424.0" x2="1052" y2="424.0" class="grid"/>
<text x="52" y="428.0" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="351.8" x2="1052" y2="351.8" class="grid"/>
<text x="52" y="355.8" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="279.7" x2="1052" y2="279.7" class="grid"/>
<text x="52" y="283.7" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="207.5" x2="1052" y2="207.5" class="grid"/>
<text x="52" y="211.5" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="135.4" x2="1052" y2="135.4" class="grid"/>
<text x="52" y="139.4" font-size="11" text-anchor="end" fill="var(--muted)">650</text>
<line x1="60" y1="63.2" x2="1052" y2="63.2" class="grid"/>
<text x="52" y="67.2" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="122.5" y1="56.0" x2="122.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="122.5" y1="626.0" x2="122.5" y2="631.0" class="axis"/>
<text x="122.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="319.4" y1="56.0" x2="319.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="319.4" y1="626.0" x2="319.4" y2="631.0" class="axis"/>
<text x="319.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="516.2" y1="56.0" x2="516.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="516.2" y1="626.0" x2="516.2" y2="631.0" class="axis"/>
<text x="516.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.9" y1="56.0" x2="716.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.9" y1="626.0" x2="716.9" y2="631.0" class="axis"/>
<text x="716.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.8" y1="56.0" x2="913.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.8" y1="626.0" x2="913.8" y2="631.0" class="axis"/>
<text x="913.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="569.3" x2="61.9" y2="583.9" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="571.3" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="65.7" y1="564.0" x2="65.7" y2="589.8" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="569.0" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="69.5" y1="557.8" x2="69.5" y2="578.7" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="565.2" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="73.3" y1="560.8" x2="73.3" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="562.9" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="77.0" y1="544.8" x2="77.0" y2="563.3" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="545.7" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="80.8" y1="529.3" x2="80.8" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="532.8" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="84.6" y1="527.7" x2="84.6" y2="604.2" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="530.9" width="2.35" height="62.9" fill="var(--down)"/>
<line x1="88.4" y1="582.0" x2="88.4" y2="605.5" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="582.9" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="92.2" y1="578.4" x2="92.2" y2="592.4" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="580.4" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="96.0" y1="577.5" x2="96.0" y2="583.6" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="580.6" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="99.8" y1="571.0" x2="99.8" y2="585.5" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="578.8" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="103.5" y1="576.1" x2="103.5" y2="599.7" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="576.9" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="107.3" y1="572.3" x2="107.3" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="575.7" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="111.1" y1="570.6" x2="111.1" y2="582.7" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="576.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="114.9" y1="570.7" x2="114.9" y2="592.2" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="572.6" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="118.7" y1="557.0" x2="118.7" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="560.5" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="122.5" y1="548.1" x2="122.5" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="553.6" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="126.3" y1="535.1" x2="126.3" y2="554.6" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="535.6" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="130.0" y1="522.9" x2="130.0" y2="541.1" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="537.7" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="133.8" y1="502.5" x2="133.8" y2="546.1" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="506.0" width="2.35" height="34.1" fill="var(--up)"/>
<line x1="137.6" y1="506.5" x2="137.6" y2="518.2" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="509.8" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="141.4" y1="497.8" x2="141.4" y2="519.3" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="501.6" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="145.2" y1="502.6" x2="145.2" y2="527.4" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="504.8" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="149.0" y1="475.3" x2="149.0" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="482.4" width="2.35" height="26.3" fill="var(--up)"/>
<line x1="152.8" y1="405.7" x2="152.8" y2="476.6" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="412.2" width="2.35" height="64.0" fill="var(--up)"/>
<line x1="156.5" y1="380.7" x2="156.5" y2="449.3" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="405.2" width="2.35" height="34.6" fill="var(--down)"/>
<line x1="160.3" y1="423.4" x2="160.3" y2="479.7" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="424.8" width="2.35" height="33.6" fill="var(--down)"/>
<line x1="164.1" y1="413.1" x2="164.1" y2="450.5" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="418.7" width="2.35" height="31.8" fill="var(--up)"/>
<line x1="167.9" y1="423.3" x2="167.9" y2="453.8" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="425.0" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="171.7" y1="392.8" x2="171.7" y2="439.1" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="407.4" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="175.5" y1="388.5" x2="175.5" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="398.5" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="179.3" y1="387.2" x2="179.3" y2="440.7" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="399.4" width="2.35" height="30.6" fill="var(--down)"/>
<line x1="183.1" y1="420.6" x2="183.1" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="434.1" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="186.8" y1="424.6" x2="186.8" y2="458.4" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="424.8" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="190.6" y1="425.7" x2="190.6" y2="455.2" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="428.3" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="194.4" y1="435.2" x2="194.4" y2="471.2" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="445.6" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="198.2" y1="418.1" x2="198.2" y2="456.5" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="423.2" width="2.35" height="33.4" fill="var(--up)"/>
<line x1="202.0" y1="428.9" x2="202.0" y2="452.2" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="434.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="205.8" y1="414.3" x2="205.8" y2="459.0" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="432.9" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="209.6" y1="455.2" x2="209.6" y2="503.8" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="460.9" width="2.35" height="29.4" fill="var(--down)"/>
<line x1="213.3" y1="466.5" x2="213.3" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="468.7" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="217.1" y1="445.7" x2="217.1" y2="472.4" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="447.8" width="2.35" height="20.9" fill="var(--up)"/>
<line x1="220.9" y1="455.7" x2="220.9" y2="485.7" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="460.4" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="224.7" y1="462.9" x2="224.7" y2="499.7" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="470.3" width="2.35" height="28.2" fill="var(--down)"/>
<line x1="228.5" y1="493.3" x2="228.5" y2="534.1" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="496.2" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="232.3" y1="475.7" x2="232.3" y2="505.3" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="476.2" width="2.35" height="28.1" fill="var(--up)"/>
<line x1="236.1" y1="446.1" x2="236.1" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="458.0" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="239.8" y1="446.6" x2="239.8" y2="464.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="446.7" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="243.6" y1="430.5" x2="243.6" y2="453.0" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="438.4" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="247.4" y1="434.4" x2="247.4" y2="452.4" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="440.6" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="251.2" y1="447.2" x2="251.2" y2="470.8" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="456.2" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="255.0" y1="462.0" x2="255.0" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="465.1" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="258.8" y1="465.1" x2="258.8" y2="485.5" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="465.8" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="262.6" y1="447.4" x2="262.6" y2="485.2" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="475.9" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="266.4" y1="478.5" x2="266.4" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="479.3" width="2.35" height="36.7" fill="var(--down)"/>
<line x1="270.1" y1="484.8" x2="270.1" y2="511.9" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="490.4" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="273.9" y1="469.2" x2="273.9" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="485.2" width="2.35" height="26.2" fill="var(--down)"/>
<line x1="277.7" y1="417.2" x2="277.7" y2="507.5" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="417.3" width="2.35" height="88.9" fill="var(--up)"/>
<line x1="281.5" y1="364.6" x2="281.5" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="373.7" width="2.35" height="37.2" fill="var(--up)"/>
<line x1="285.3" y1="364.6" x2="285.3" y2="391.4" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="378.3" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="289.1" y1="359.5" x2="289.1" y2="405.8" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="377.1" width="2.35" height="26.9" fill="var(--down)"/>
<line x1="292.9" y1="379.4" x2="292.9" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="385.3" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="296.6" y1="374.2" x2="296.6" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="375.7" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="300.4" y1="353.3" x2="300.4" y2="384.0" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="357.3" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="304.2" y1="359.1" x2="304.2" y2="380.0" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="365.0" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="308.0" y1="365.7" x2="308.0" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="373.5" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="311.8" y1="364.2" x2="311.8" y2="389.4" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="375.9" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="315.6" y1="366.5" x2="315.6" y2="378.9" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="371.3" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="319.4" y1="369.1" x2="319.4" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="375.8" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="323.1" y1="394.0" x2="323.1" y2="431.6" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="398.3" width="2.35" height="25.9" fill="var(--down)"/>
<line x1="326.9" y1="418.9" x2="326.9" y2="441.8" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="423.5" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="330.7" y1="399.9" x2="330.7" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="410.1" width="2.35" height="23.8" fill="var(--up)"/>
<line x1="334.5" y1="399.9" x2="334.5" y2="418.3" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="406.7" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="338.3" y1="378.0" x2="338.3" y2="405.6" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="379.5" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="342.1" y1="367.0" x2="342.1" y2="400.7" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="373.2" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="345.9" y1="376.2" x2="345.9" y2="387.6" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="379.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="349.6" y1="374.8" x2="349.6" y2="393.3" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="379.9" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="353.4" y1="369.7" x2="353.4" y2="388.7" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="385.3" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="357.2" y1="378.9" x2="357.2" y2="404.8" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="392.4" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="361.0" y1="381.8" x2="361.0" y2="402.0" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="388.6" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="364.8" y1="384.2" x2="364.8" y2="394.1" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="384.9" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="368.6" y1="356.2" x2="368.6" y2="391.1" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="366.0" width="2.35" height="24.8" fill="var(--up)"/>
<line x1="372.4" y1="354.1" x2="372.4" y2="378.2" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="363.7" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="376.2" y1="340.1" x2="376.2" y2="379.8" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="371.2" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="379.9" y1="375.6" x2="379.9" y2="410.1" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="377.2" width="2.35" height="25.9" fill="var(--down)"/>
<line x1="383.7" y1="393.6" x2="383.7" y2="429.4" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="402.3" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="387.5" y1="412.0" x2="387.5" y2="427.1" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="414.6" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="391.3" y1="411.8" x2="391.3" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="417.5" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="395.1" y1="413.3" x2="395.1" y2="438.8" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="418.2" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="398.9" y1="414.8" x2="398.9" y2="434.1" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="417.5" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="402.7" y1="400.3" x2="402.7" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="405.7" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="406.4" y1="405.4" x2="406.4" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="405.5" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="410.2" y1="399.2" x2="410.2" y2="413.2" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="410.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="414.0" y1="405.7" x2="414.0" y2="428.8" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="409.0" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="417.8" y1="404.7" x2="417.8" y2="413.1" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="409.5" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="421.6" y1="398.8" x2="421.6" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="403.3" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="425.4" y1="381.4" x2="425.4" y2="426.7" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="400.5" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="429.2" y1="412.5" x2="429.2" y2="430.7" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="415.3" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="432.9" y1="419.5" x2="432.9" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="424.4" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="436.7" y1="418.1" x2="436.7" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="418.1" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="440.5" y1="415.9" x2="440.5" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="417.4" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="444.3" y1="412.9" x2="444.3" y2="425.4" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="422.4" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="448.1" y1="415.4" x2="448.1" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="422.8" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="451.9" y1="426.4" x2="451.9" y2="464.4" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="426.9" width="2.35" height="35.9" fill="var(--down)"/>
<line x1="455.7" y1="454.5" x2="455.7" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="461.4" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="459.5" y1="450.7" x2="459.5" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="456.2" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="463.2" y1="476.0" x2="463.2" y2="487.9" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="477.0" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="467.0" y1="480.3" x2="467.0" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="483.2" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="470.8" y1="433.9" x2="470.8" y2="462.4" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="436.9" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="474.6" y1="419.9" x2="474.6" y2="446.5" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="432.4" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="478.4" y1="421.0" x2="478.4" y2="438.1" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="432.3" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="482.2" y1="412.1" x2="482.2" y2="434.4" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="419.2" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="486.0" y1="417.0" x2="486.0" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="417.0" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="489.7" y1="426.0" x2="489.7" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="431.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="493.5" y1="420.2" x2="493.5" y2="437.3" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="421.1" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="497.3" y1="419.9" x2="497.3" y2="434.8" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="421.3" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="501.1" y1="422.0" x2="501.1" y2="430.5" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="426.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="504.9" y1="417.9" x2="504.9" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="421.3" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="508.7" y1="421.5" x2="508.7" y2="435.1" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="426.5" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="512.5" y1="418.9" x2="512.5" y2="427.1" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="419.3" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="516.2" y1="403.6" x2="516.2" y2="419.3" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="414.6" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="520.0" y1="404.7" x2="520.0" y2="424.9" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="405.0" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="523.8" y1="400.5" x2="523.8" y2="418.9" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="400.5" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="527.6" y1="408.3" x2="527.6" y2="459.0" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="413.0" width="2.35" height="39.9" fill="var(--down)"/>
<line x1="531.4" y1="447.5" x2="531.4" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="451.4" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="535.2" y1="452.4" x2="535.2" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="457.9" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="539.0" y1="450.1" x2="539.0" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="457.5" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="542.7" y1="450.8" x2="542.7" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="451.2" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="546.5" y1="445.6" x2="546.5" y2="461.5" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="450.7" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="550.3" y1="444.2" x2="550.3" y2="457.2" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="448.7" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="554.1" y1="441.0" x2="554.1" y2="449.4" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="444.4" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="557.9" y1="429.4" x2="557.9" y2="450.4" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="429.9" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="561.7" y1="413.7" x2="561.7" y2="431.5" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="416.9" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="565.5" y1="415.3" x2="565.5" y2="428.1" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="416.2" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="569.3" y1="412.5" x2="569.3" y2="434.3" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="415.3" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="573.0" y1="401.8" x2="573.0" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="404.0" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="576.8" y1="390.0" x2="576.8" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="402.0" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="580.6" y1="398.0" x2="580.6" y2="413.6" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="406.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="584.4" y1="394.2" x2="584.4" y2="409.3" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="396.7" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="588.2" y1="391.7" x2="588.2" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="395.3" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="592.0" y1="395.3" x2="592.0" y2="402.4" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="398.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="595.8" y1="394.6" x2="595.8" y2="421.4" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="394.6" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="599.5" y1="387.5" x2="599.5" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="394.9" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="603.3" y1="394.0" x2="603.3" y2="417.6" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="394.0" width="2.35" height="17.9" fill="var(--down)"/>
<line x1="607.1" y1="395.4" x2="607.1" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="398.6" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="610.9" y1="386.9" x2="610.9" y2="404.2" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="396.6" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="614.7" y1="392.7" x2="614.7" y2="410.0" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="394.0" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="618.5" y1="401.2" x2="618.5" y2="415.2" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="404.2" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="622.3" y1="379.4" x2="622.3" y2="405.5" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="388.0" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="626.0" y1="310.5" x2="626.0" y2="391.0" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="316.0" width="2.35" height="71.9" fill="var(--up)"/>
<line x1="629.8" y1="263.6" x2="629.8" y2="324.0" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="281.4" width="2.35" height="37.2" fill="var(--up)"/>
<line x1="633.6" y1="261.5" x2="633.6" y2="298.8" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="275.1" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="637.4" y1="259.2" x2="637.4" y2="279.1" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="265.1" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="641.2" y1="261.3" x2="641.2" y2="278.3" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="272.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="645.0" y1="252.1" x2="645.0" y2="270.9" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="253.6" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="648.8" y1="238.2" x2="648.8" y2="258.9" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="254.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="652.5" y1="239.3" x2="652.5" y2="263.7" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="250.9" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="656.3" y1="240.7" x2="656.3" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="244.4" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="660.1" y1="230.5" x2="660.1" y2="249.6" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="233.0" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="663.9" y1="190.9" x2="663.9" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="200.1" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="667.7" y1="190.8" x2="667.7" y2="213.0" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="197.4" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="671.5" y1="186.4" x2="671.5" y2="203.7" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="190.5" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="675.3" y1="180.2" x2="675.3" y2="263.7" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="184.9" width="2.35" height="77.0" fill="var(--down)"/>
<line x1="679.1" y1="260.7" x2="679.1" y2="290.2" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="260.9" width="2.35" height="25.5" fill="var(--down)"/>
<line x1="682.8" y1="255.4" x2="682.8" y2="294.1" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="258.7" width="2.35" height="27.2" fill="var(--up)"/>
<line x1="686.6" y1="241.5" x2="686.6" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="250.5" width="2.35" height="51.1" fill="var(--down)"/>
<line x1="690.4" y1="285.4" x2="690.4" y2="310.3" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="290.9" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="694.2" y1="302.5" x2="694.2" y2="330.3" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="304.2" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="698.0" y1="313.2" x2="698.0" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="315.4" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="701.8" y1="328.2" x2="701.8" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="335.7" width="2.35" height="23.9" fill="var(--down)"/>
<line x1="705.6" y1="359.3" x2="705.6" y2="384.6" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="359.3" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="709.3" y1="361.2" x2="709.3" y2="378.0" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="367.7" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="713.1" y1="366.7" x2="713.1" y2="379.4" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="372.0" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="716.9" y1="380.7" x2="716.9" y2="407.8" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="382.5" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="720.7" y1="363.3" x2="720.7" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="365.8" width="2.35" height="30.8" fill="var(--up)"/>
<line x1="724.5" y1="338.0" x2="724.5" y2="360.5" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="356.2" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="728.3" y1="341.6" x2="728.3" y2="424.8" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="351.7" width="2.35" height="53.6" fill="var(--down)"/>
<line x1="732.1" y1="407.6" x2="732.1" y2="433.0" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="411.3" width="2.35" height="20.8" fill="var(--down)"/>
<line x1="735.8" y1="421.4" x2="735.8" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="431.5" width="2.35" height="31.2" fill="var(--down)"/>
<line x1="739.6" y1="433.0" x2="739.6" y2="462.2" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="437.4" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="743.4" y1="421.6" x2="743.4" y2="440.5" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="423.4" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="747.2" y1="384.3" x2="747.2" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="389.8" width="2.35" height="30.0" fill="var(--up)"/>
<line x1="751.0" y1="360.2" x2="751.0" y2="415.3" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="387.2" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="754.8" y1="378.5" x2="754.8" y2="449.2" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="404.0" width="2.35" height="34.8" fill="var(--down)"/>
<line x1="758.6" y1="422.2" x2="758.6" y2="461.1" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="436.3" width="2.35" height="22.9" fill="var(--up)"/>
<line x1="762.4" y1="406.8" x2="762.4" y2="449.8" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="436.1" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="766.1" y1="383.3" x2="766.1" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="388.0" width="2.35" height="76.0" fill="var(--up)"/>
<line x1="769.9" y1="376.6" x2="769.9" y2="426.3" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="391.1" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="773.7" y1="382.9" x2="773.7" y2="435.0" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="384.1" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="777.5" y1="364.7" x2="777.5" y2="398.7" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="381.7" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="781.3" y1="382.1" x2="781.3" y2="404.6" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="389.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="785.1" y1="386.9" x2="785.1" y2="431.1" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="390.1" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="788.9" y1="379.3" x2="788.9" y2="401.5" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="396.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="792.6" y1="377.2" x2="792.6" y2="401.9" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="377.2" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="796.4" y1="370.8" x2="796.4" y2="392.6" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="378.2" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="800.2" y1="368.7" x2="800.2" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="371.4" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="804.0" y1="376.7" x2="804.0" y2="407.9" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="377.8" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="807.8" y1="377.3" x2="807.8" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="390.9" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="811.6" y1="395.9" x2="811.6" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="405.9" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="815.4" y1="394.3" x2="815.4" y2="415.3" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="398.7" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="819.1" y1="388.2" x2="819.1" y2="408.1" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="395.1" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="822.9" y1="398.9" x2="822.9" y2="481.5" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="402.8" width="2.35" height="62.7" fill="var(--down)"/>
<line x1="826.7" y1="454.5" x2="826.7" y2="478.0" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="458.8" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="830.5" y1="443.3" x2="830.5" y2="468.7" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="459.1" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="834.3" y1="432.8" x2="834.3" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="441.9" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="838.1" y1="420.3" x2="838.1" y2="440.4" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="429.5" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="841.9" y1="409.7" x2="841.9" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="415.9" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="845.6" y1="403.8" x2="845.6" y2="428.8" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="403.9" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="849.4" y1="390.8" x2="849.4" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="393.2" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="853.2" y1="382.9" x2="853.2" y2="398.0" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="390.9" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="857.0" y1="358.7" x2="857.0" y2="390.8" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="369.9" width="2.35" height="19.9" fill="var(--up)"/>
<line x1="860.8" y1="342.0" x2="860.8" y2="367.4" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="345.3" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="864.6" y1="328.7" x2="864.6" y2="351.0" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="342.3" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="868.4" y1="341.1" x2="868.4" y2="372.8" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="348.5" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="872.2" y1="342.3" x2="872.2" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="357.0" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="875.9" y1="359.8" x2="875.9" y2="380.9" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="363.5" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="879.7" y1="364.1" x2="879.7" y2="415.0" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="364.8" width="2.35" height="47.1" fill="var(--down)"/>
<line x1="883.5" y1="400.3" x2="883.5" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="401.2" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="887.3" y1="373.5" x2="887.3" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="399.0" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="891.1" y1="407.8" x2="891.1" y2="426.2" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="410.4" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="894.9" y1="418.1" x2="894.9" y2="442.4" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="419.2" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="898.7" y1="379.5" x2="898.7" y2="421.8" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="380.3" width="2.35" height="38.6" fill="var(--up)"/>
<line x1="902.4" y1="373.8" x2="902.4" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="382.1" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="906.2" y1="364.6" x2="906.2" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="376.3" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="910.0" y1="355.9" x2="910.0" y2="385.7" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="356.1" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="913.8" y1="285.3" x2="913.8" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="289.9" width="2.35" height="56.3" fill="var(--up)"/>
<line x1="917.6" y1="232.2" x2="917.6" y2="293.7" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="232.9" width="2.35" height="48.3" fill="var(--up)"/>
<line x1="921.4" y1="213.0" x2="921.4" y2="245.9" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="220.8" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="925.2" y1="141.6" x2="925.2" y2="245.3" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="158.1" width="2.35" height="63.8" fill="var(--up)"/>
<line x1="928.9" y1="140.3" x2="928.9" y2="214.7" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="173.5" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="932.7" y1="126.2" x2="932.7" y2="176.2" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="131.6" width="2.35" height="39.4" fill="var(--up)"/>
<line x1="936.5" y1="106.9" x2="936.5" y2="146.9" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="123.4" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="940.3" y1="107.8" x2="940.3" y2="158.4" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="123.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="944.1" y1="74.8" x2="944.1" y2="139.4" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="84.1" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="947.9" y1="97.7" x2="947.9" y2="149.1" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="98.5" width="2.35" height="42.7" fill="var(--down)"/>
<line x1="951.7" y1="133.1" x2="951.7" y2="175.2" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="142.3" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="955.5" y1="160.0" x2="955.5" y2="200.3" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="165.6" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="959.2" y1="169.3" x2="959.2" y2="216.4" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="174.6" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="963.0" y1="152.8" x2="963.0" y2="199.6" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="174.2" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="966.8" y1="175.0" x2="966.8" y2="224.2" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="181.7" width="2.35" height="37.1" fill="var(--down)"/>
<line x1="970.6" y1="210.4" x2="970.6" y2="346.6" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="216.8" width="2.35" height="115.7" fill="var(--down)"/>
<line x1="974.4" y1="311.9" x2="974.4" y2="349.0" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="331.5" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="978.2" y1="316.5" x2="978.2" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="332.5" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="982.0" y1="315.8" x2="982.0" y2="348.3" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="328.7" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="985.7" y1="302.4" x2="985.7" y2="333.4" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="303.9" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="989.5" y1="292.4" x2="989.5" y2="316.8" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="299.9" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="993.3" y1="311.4" x2="993.3" y2="337.2" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="317.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="997.1" y1="278.2" x2="997.1" y2="327.5" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="293.6" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="1000.9" y1="294.9" x2="1000.9" y2="344.3" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="300.7" width="2.35" height="35.3" fill="var(--down)"/>
<line x1="1004.7" y1="325.5" x2="1004.7" y2="366.2" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="339.6" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="1008.5" y1="285.5" x2="1008.5" y2="354.3" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="285.6" width="2.35" height="54.0" fill="var(--up)"/>
<line x1="1012.2" y1="283.3" x2="1012.2" y2="331.9" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="286.9" width="2.35" height="31.4" fill="var(--down)"/>
<line x1="1016.0" y1="312.2" x2="1016.0" y2="340.7" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="315.7" width="2.35" height="23.4" fill="var(--down)"/>
<line x1="1019.8" y1="224.2" x2="1019.8" y2="370.4" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="232.6" width="2.35" height="103.9" fill="var(--up)"/>
<line x1="1023.6" y1="216.5" x2="1023.6" y2="270.2" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="232.4" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="1027.4" y1="216.6" x2="1027.4" y2="240.7" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="224.9" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="1031.2" y1="192.6" x2="1031.2" y2="224.8" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="195.0" width="2.35" height="24.4" fill="var(--up)"/>
<line x1="1035.0" y1="189.1" x2="1035.0" y2="260.8" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="199.6" width="2.35" height="60.5" fill="var(--down)"/>
<line x1="1038.7" y1="250.9" x2="1038.7" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="259.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1042.5" y1="258.1" x2="1042.5" y2="317.1" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="259.9" width="2.35" height="55.5" fill="var(--down)"/>
<line x1="1046.3" y1="288.9" x2="1046.3" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="305.6" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="1050.1" y1="302.8" x2="1050.1" y2="320.2" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="305.3" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="60" y1="184.6" x2="1052" y2="184.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="188.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$616 R1</text>
<text x="1058" y="200.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="413.1" x2="1052" y2="413.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="407.1" font-size="11.5" fill="var(--support)" font-weight="600">$458 S1</text>
<text x="1058" y="419.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="439.4" x2="1052" y2="439.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="433.4" font-size="11.5" fill="var(--support)" font-weight="600">$439 S2</text>
<text x="1058" y="445.4" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="473.5" x2="1052" y2="473.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="467.5" font-size="11.5" fill="var(--support)" font-weight="600">$416 S3</text>
<text x="1058" y="479.5" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="316.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="308.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $524 (2026-09-11)</text>
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

각 레벨은 "전후 일정 기간 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $616 | 2 | 2024-10-21·2026-08-17 — 5년 중 유일한 저항 클러스터(2회). 2024년 가을 고점과 2026년 8월 반등 상단이 거의 같은 자리에서 만났다 |
| **현재가** | **$524.19** (2026-09-11 종가) | — | R1 $616과 S1 $458 사이. **5년 구조에서는 중상단**이며, 아래 지지 세 개가 $416~$458에 촘촘히 몰려 있다 |
| S1 | $458 | 2 | 2023-03-13·2024-05-27 — 2023~2024년의 중간 지지. 현재가에서 −12.6% |
| S2 | $439 | 5 | 2023-01-16·2023-05-22·2023-12-11·2025-06-09·2025-12-01 — 5회 터치. **2025-07-22 손실충당 급락($410.74) 직전과 직후를 감싸는 대역** |
| S3 | $416 | 4 | 2024-02-12·2025-02-10·2025-04-07·2025-07-21 — 4회 터치. 5년 중 가장 낮은 지지대이며, 2025년에만 세 번 닿았다 |

---

## 3. 관측된 특이 구간 — 2025-07-22 손실충당 급락과 그 이후의 복원

- 2025-07-22에 세전 $1,681M 손실충당(기밀 항공 $950M · CMHP $570M · TUHP $95M · 고정자산 상각 $66M)이 발표되며 하루 **−10.8%**($460.53 → $410.74), 거래량 8.9백만 주(평소의 약 6배)를 기록했다([최근 뉴스 / 이슈](./08_news.md)). 이는 5년 차트에서 가장 큰 단일 하락이다.
- **그 저점대가 지금의 S3 $416**이고, 2025년에만 세 번(2·4·7월) 닿았다. 즉 $416 대역은 **손실충당 국면의 가격 기억**이 만든 자리다.
- 그 뒤 1년간 주가는 $416 → 2026년 3월 $692.00까지 올랐다가 현재 $524.19로 되돌렸다. **5년 구조에서 보면 현재가는 손실충당 저점과 2026년 고점의 거의 중간 지점**이다.
- 이 관찰은 **가격 구조에 대한 서술일 뿐 방향 예측이 아니다.** 같은 기간 수주잔고는 $176B에서 $230B로 늘었으므로, 과거 가격대를 그대로 현재의 적정 범위로 읽으면 안 된다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-13~2026-09-11. 수집 시점: 2026-09-12. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `uv run python scripts/gen_technical_chart.py LMT --name "록히드마틴" --interval 1wk --close-on 2026-09-11 --emit all`

- **이번 재생성에서 차트를 다시 뽑지 않은 이유**: 이 문서를 재생성한 2026-09-14는 미 증시 정규장이 아직 마감하지 않은 시점이었다. `gen_technical_chart.py`에는 시계열 종료일을 고정하는 옵션이 없어 지금 다시 실행하면 **미완성 장중 봉이 마지막 캔들로 섞이고 그 값이 "종가"로 표기된다**(실제로 재실행 시 `2026-09-14 종가`로 장중 가격이 나왔다). 그래서 **마지막으로 완료된 거래일(2026-09-11)까지를 담은 직전 생성 결과를 그대로 유지**했다. 다음 갱신은 정규장 마감 이후에 재실행할 것.
- **한계**: 원주가 기준이라 기간 내 배당 20회가 반영돼 있지 않다 — 배당수익률 2.6~2.8%대가 5년 누적되면 총수익률과의 괴리가 13%p를 넘는다. 또한 이 차트에는 **저항 클러스터가 하나뿐**(R1 $616)인데, 2026년 상반기의 $692까지 오른 구간이 짧아 스윙이 클러스터로 묶이지 않은 결과다 — 위쪽 참고선으로는 5년 최고 $692.00을 쓰는 편이 낫다.

---

*작성일: 2026-09-14*
