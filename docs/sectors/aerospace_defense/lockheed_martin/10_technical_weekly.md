# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉으로 다년 가격 구조를 정리한 참고 자료. 최근 1년의 세부 흐름은 [기술적 분석 — 일봉](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: **2026-09-03 종가 $532.95는 [일봉 차트](./09_technical_daily.md)·[핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)의 기준 종가와 모두 일치**한다. 네 문서 전부 원주가(분할 소급 반영·배당 미반영) 기준이다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-09-03)

<div class="lmt-chart">
<style>
.lmt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .lmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .lmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lmt-chart svg { width:100%; height:auto; display:block; }
.lmt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lmt-chart .title { fill: var(--ink); font-weight:600; }
.lmt-chart .grid { stroke: var(--grid); stroke-width:1; }
.lmt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="록히드마틴(LMT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">록히드마틴 (LMT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-09-03 · 마지막 종가 $532.95 (2026-09-03) · 단위 USD</text>
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
<line x1="129.8" y1="56.0" x2="129.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="129.8" y1="626.0" x2="129.8" y2="631.0" class="axis"/>
<text x="129.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="325.9" y1="56.0" x2="325.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="325.9" y1="626.0" x2="325.9" y2="631.0" class="axis"/>
<text x="325.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="522.1" y1="56.0" x2="522.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="522.1" y1="626.0" x2="522.1" y2="631.0" class="axis"/>
<text x="522.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="722.0" y1="56.0" x2="722.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="722.0" y1="626.0" x2="722.0" y2="631.0" class="axis"/>
<text x="722.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="918.1" y1="56.0" x2="918.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="918.1" y1="626.0" x2="918.1" y2="631.0" class="axis"/>
<text x="918.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="556.3" x2="61.9" y2="560.2" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="556.7" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="65.7" y1="561.5" x2="65.7" y2="574.3" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="561.5" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="69.4" y1="569.3" x2="69.4" y2="583.9" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="571.3" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="73.2" y1="564.0" x2="73.2" y2="589.8" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="569.0" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="77.0" y1="557.8" x2="77.0" y2="578.7" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="565.2" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="80.7" y1="560.8" x2="80.7" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="562.9" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="84.5" y1="544.8" x2="84.5" y2="563.3" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="545.7" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="88.3" y1="529.3" x2="88.3" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="532.8" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="92.1" y1="527.7" x2="92.1" y2="604.2" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="530.9" width="2.34" height="62.9" fill="var(--down)"/>
<line x1="95.8" y1="582.0" x2="95.8" y2="605.5" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="582.9" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="99.6" y1="578.4" x2="99.6" y2="592.4" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="580.4" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="103.4" y1="577.5" x2="103.4" y2="583.6" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="580.6" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="107.1" y1="571.0" x2="107.1" y2="585.5" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="578.8" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="110.9" y1="576.1" x2="110.9" y2="599.7" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="576.9" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="114.7" y1="572.3" x2="114.7" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="575.7" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="118.5" y1="570.6" x2="118.5" y2="582.7" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="576.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="122.2" y1="570.7" x2="122.2" y2="592.2" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="572.6" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="126.0" y1="557.0" x2="126.0" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="560.5" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="129.8" y1="548.1" x2="129.8" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="553.6" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="133.6" y1="535.1" x2="133.6" y2="554.6" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="535.6" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="137.3" y1="522.9" x2="137.3" y2="541.1" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="537.7" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="141.1" y1="502.5" x2="141.1" y2="546.1" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="506.0" width="2.34" height="34.1" fill="var(--up)"/>
<line x1="144.9" y1="506.5" x2="144.9" y2="518.2" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="509.8" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="148.6" y1="497.8" x2="148.6" y2="519.3" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="501.6" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="152.4" y1="502.6" x2="152.4" y2="527.4" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="504.8" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="156.2" y1="475.3" x2="156.2" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="482.4" width="2.34" height="26.3" fill="var(--up)"/>
<line x1="160.0" y1="405.7" x2="160.0" y2="476.6" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="412.2" width="2.34" height="64.0" fill="var(--up)"/>
<line x1="163.7" y1="380.7" x2="163.7" y2="449.3" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="405.2" width="2.34" height="34.6" fill="var(--down)"/>
<line x1="167.5" y1="423.4" x2="167.5" y2="479.7" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="424.8" width="2.34" height="33.6" fill="var(--down)"/>
<line x1="171.3" y1="413.1" x2="171.3" y2="450.5" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="418.7" width="2.34" height="31.8" fill="var(--up)"/>
<line x1="175.0" y1="423.3" x2="175.0" y2="453.8" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="425.0" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="178.8" y1="392.8" x2="178.8" y2="439.1" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="407.4" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="182.6" y1="388.5" x2="182.6" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="398.5" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="186.4" y1="387.2" x2="186.4" y2="440.7" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="399.4" width="2.34" height="30.6" fill="var(--down)"/>
<line x1="190.1" y1="420.6" x2="190.1" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="434.1" width="2.34" height="15.7" fill="var(--down)"/>
<line x1="193.9" y1="424.6" x2="193.9" y2="458.4" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="424.8" width="2.34" height="28.6" fill="var(--up)"/>
<line x1="197.7" y1="425.7" x2="197.7" y2="455.2" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="428.3" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="201.4" y1="435.2" x2="201.4" y2="471.2" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="445.6" width="2.34" height="15.7" fill="var(--down)"/>
<line x1="205.2" y1="418.1" x2="205.2" y2="456.5" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="423.2" width="2.34" height="33.4" fill="var(--up)"/>
<line x1="209.0" y1="428.9" x2="209.0" y2="452.2" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="434.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="212.8" y1="414.3" x2="212.8" y2="459.0" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="432.9" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="216.5" y1="455.2" x2="216.5" y2="503.8" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="460.9" width="2.34" height="29.4" fill="var(--down)"/>
<line x1="220.3" y1="466.5" x2="220.3" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="468.7" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="224.1" y1="445.7" x2="224.1" y2="472.4" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="447.8" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="227.8" y1="455.7" x2="227.8" y2="485.7" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="460.4" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="231.6" y1="462.9" x2="231.6" y2="499.7" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="470.3" width="2.34" height="28.2" fill="var(--down)"/>
<line x1="235.4" y1="493.3" x2="235.4" y2="534.1" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="496.2" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="239.2" y1="475.7" x2="239.2" y2="505.3" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="476.2" width="2.34" height="28.1" fill="var(--up)"/>
<line x1="242.9" y1="446.1" x2="242.9" y2="472.1" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="458.0" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="246.7" y1="446.6" x2="246.7" y2="464.8" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="446.7" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="250.5" y1="430.5" x2="250.5" y2="453.0" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="438.4" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="254.3" y1="434.4" x2="254.3" y2="452.4" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="440.6" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="258.0" y1="447.2" x2="258.0" y2="470.8" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="456.2" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="261.8" y1="462.0" x2="261.8" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="465.1" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="265.6" y1="465.1" x2="265.6" y2="485.5" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="465.8" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="269.3" y1="447.4" x2="269.3" y2="485.2" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="475.9" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="273.1" y1="478.5" x2="273.1" y2="522.8" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="479.3" width="2.34" height="36.7" fill="var(--down)"/>
<line x1="276.9" y1="484.8" x2="276.9" y2="511.9" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="490.4" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="280.7" y1="469.2" x2="280.7" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="485.2" width="2.34" height="26.2" fill="var(--down)"/>
<line x1="284.4" y1="417.2" x2="284.4" y2="507.5" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="417.3" width="2.34" height="88.9" fill="var(--up)"/>
<line x1="288.2" y1="364.6" x2="288.2" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="373.7" width="2.34" height="37.2" fill="var(--up)"/>
<line x1="292.0" y1="364.6" x2="292.0" y2="391.4" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="378.3" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="295.7" y1="359.5" x2="295.7" y2="405.8" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="377.1" width="2.34" height="26.9" fill="var(--down)"/>
<line x1="299.5" y1="379.4" x2="299.5" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="385.3" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="303.3" y1="374.2" x2="303.3" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="375.7" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="307.1" y1="353.3" x2="307.1" y2="384.0" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="357.3" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="310.8" y1="359.1" x2="310.8" y2="380.0" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="365.0" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="314.6" y1="365.7" x2="314.6" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="373.5" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="318.4" y1="364.2" x2="318.4" y2="389.4" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="375.9" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="322.1" y1="366.5" x2="322.1" y2="378.9" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="371.3" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="325.9" y1="369.1" x2="325.9" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="375.8" width="2.34" height="14.6" fill="var(--down)"/>
<line x1="329.7" y1="394.0" x2="329.7" y2="431.6" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="398.3" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="333.5" y1="418.9" x2="333.5" y2="441.8" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="423.5" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="337.2" y1="399.9" x2="337.2" y2="441.7" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="410.1" width="2.34" height="23.8" fill="var(--up)"/>
<line x1="341.0" y1="399.9" x2="341.0" y2="418.3" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="406.7" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="344.8" y1="378.0" x2="344.8" y2="405.6" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="379.5" width="2.34" height="24.9" fill="var(--up)"/>
<line x1="348.5" y1="367.0" x2="348.5" y2="400.7" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="373.2" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="352.3" y1="376.2" x2="352.3" y2="387.6" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="379.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="356.1" y1="374.8" x2="356.1" y2="393.3" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="379.9" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="359.9" y1="369.7" x2="359.9" y2="388.7" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="385.3" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="363.6" y1="378.9" x2="363.6" y2="404.8" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="392.4" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="367.4" y1="381.8" x2="367.4" y2="402.0" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="388.6" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="371.2" y1="384.2" x2="371.2" y2="394.1" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="384.9" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="375.0" y1="356.2" x2="375.0" y2="391.1" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="366.0" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="378.7" y1="354.1" x2="378.7" y2="378.2" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="363.7" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="382.5" y1="340.1" x2="382.5" y2="379.8" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="371.2" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="386.3" y1="375.6" x2="386.3" y2="410.1" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="377.2" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="390.0" y1="393.6" x2="390.0" y2="429.4" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="402.3" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="393.8" y1="412.0" x2="393.8" y2="427.1" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="414.6" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="397.6" y1="411.8" x2="397.6" y2="427.4" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="417.5" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="401.4" y1="413.3" x2="401.4" y2="438.8" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="418.2" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="405.1" y1="414.8" x2="405.1" y2="434.1" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="417.5" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="408.9" y1="400.3" x2="408.9" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="405.7" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="412.7" y1="405.4" x2="412.7" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="405.5" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="416.4" y1="399.2" x2="416.4" y2="413.2" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="410.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="420.2" y1="405.7" x2="420.2" y2="428.8" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="409.0" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="424.0" y1="404.7" x2="424.0" y2="413.1" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="409.5" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="427.8" y1="398.8" x2="427.8" y2="412.4" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="403.3" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="431.5" y1="381.4" x2="431.5" y2="426.7" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="400.5" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="435.3" y1="412.5" x2="435.3" y2="430.7" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="415.3" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="439.1" y1="419.5" x2="439.1" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="424.4" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="442.8" y1="418.1" x2="442.8" y2="429.3" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="418.1" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="446.6" y1="415.9" x2="446.6" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="417.4" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="450.4" y1="412.9" x2="450.4" y2="425.4" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="422.4" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="454.2" y1="415.4" x2="454.2" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="422.8" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="457.9" y1="426.4" x2="457.9" y2="464.4" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="426.9" width="2.34" height="35.9" fill="var(--down)"/>
<line x1="461.7" y1="454.5" x2="461.7" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="461.4" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="465.5" y1="450.7" x2="465.5" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="456.2" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="469.2" y1="476.0" x2="469.2" y2="487.9" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="477.0" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="473.0" y1="480.3" x2="473.0" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="483.2" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="476.8" y1="433.9" x2="476.8" y2="462.4" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="436.9" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="480.6" y1="419.9" x2="480.6" y2="446.5" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="432.4" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="484.3" y1="421.0" x2="484.3" y2="438.1" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="432.3" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="488.1" y1="412.1" x2="488.1" y2="434.4" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="419.2" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="491.9" y1="417.0" x2="491.9" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="417.0" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="495.7" y1="426.0" x2="495.7" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="494.48" y="431.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="499.4" y1="420.2" x2="499.4" y2="437.3" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="421.1" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="503.2" y1="419.9" x2="503.2" y2="434.8" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="421.3" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="507.0" y1="422.0" x2="507.0" y2="430.5" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="426.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="510.7" y1="417.9" x2="510.7" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="421.3" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="514.5" y1="421.5" x2="514.5" y2="435.1" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="426.5" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="518.3" y1="418.9" x2="518.3" y2="427.1" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="419.3" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="522.1" y1="403.6" x2="522.1" y2="419.3" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="414.6" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="525.8" y1="404.7" x2="525.8" y2="424.9" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="405.0" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="529.6" y1="400.5" x2="529.6" y2="418.9" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="400.5" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="533.4" y1="408.3" x2="533.4" y2="459.0" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="413.0" width="2.34" height="39.9" fill="var(--down)"/>
<line x1="537.1" y1="447.5" x2="537.1" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="451.4" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="540.9" y1="452.4" x2="540.9" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="457.9" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="544.7" y1="450.1" x2="544.7" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="457.5" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="548.5" y1="450.8" x2="548.5" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="451.2" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="552.2" y1="445.6" x2="552.2" y2="461.5" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="450.7" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="556.0" y1="444.2" x2="556.0" y2="457.2" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="448.7" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="559.8" y1="441.0" x2="559.8" y2="449.4" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="444.4" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="563.5" y1="429.4" x2="563.5" y2="450.4" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="429.9" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="567.3" y1="413.7" x2="567.3" y2="431.5" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="416.9" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="571.1" y1="415.3" x2="571.1" y2="428.1" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="416.2" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="574.9" y1="412.5" x2="574.9" y2="434.3" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="415.3" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="578.6" y1="401.8" x2="578.6" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="404.0" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="582.4" y1="390.0" x2="582.4" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="402.0" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="586.2" y1="398.0" x2="586.2" y2="413.6" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="406.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="589.9" y1="394.2" x2="589.9" y2="409.3" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="396.7" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="593.7" y1="391.7" x2="593.7" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="395.3" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="597.5" y1="395.3" x2="597.5" y2="402.4" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="398.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="601.3" y1="394.6" x2="601.3" y2="421.4" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="394.6" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="605.0" y1="387.5" x2="605.0" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="394.9" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="608.8" y1="394.0" x2="608.8" y2="417.6" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="394.0" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="612.6" y1="395.4" x2="612.6" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="398.6" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="616.3" y1="386.9" x2="616.3" y2="404.2" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="396.6" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="620.1" y1="392.7" x2="620.1" y2="410.0" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="394.0" width="2.34" height="12.4" fill="var(--down)"/>
<line x1="623.9" y1="401.2" x2="623.9" y2="415.2" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="404.2" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="627.7" y1="379.4" x2="627.7" y2="405.5" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="388.0" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="631.4" y1="310.5" x2="631.4" y2="391.0" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="316.0" width="2.34" height="71.9" fill="var(--up)"/>
<line x1="635.2" y1="263.6" x2="635.2" y2="324.0" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="281.4" width="2.34" height="37.2" fill="var(--up)"/>
<line x1="639.0" y1="261.5" x2="639.0" y2="298.8" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="275.1" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="642.8" y1="259.2" x2="642.8" y2="279.1" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="265.1" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="646.5" y1="261.3" x2="646.5" y2="278.3" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="272.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="650.3" y1="252.1" x2="650.3" y2="270.9" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="253.6" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="654.1" y1="238.2" x2="654.1" y2="258.9" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="254.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="657.8" y1="239.3" x2="657.8" y2="263.7" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="250.9" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="661.6" y1="240.7" x2="661.6" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="244.4" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="665.4" y1="230.5" x2="665.4" y2="249.6" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="233.0" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="669.2" y1="190.9" x2="669.2" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="200.1" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="672.9" y1="190.8" x2="672.9" y2="213.0" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="197.4" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="676.7" y1="186.4" x2="676.7" y2="203.7" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="190.5" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="680.5" y1="180.2" x2="680.5" y2="263.7" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="184.9" width="2.34" height="77.0" fill="var(--down)"/>
<line x1="684.2" y1="260.7" x2="684.2" y2="290.2" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="260.9" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="688.0" y1="255.4" x2="688.0" y2="294.1" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="258.7" width="2.34" height="27.2" fill="var(--up)"/>
<line x1="691.8" y1="241.5" x2="691.8" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="250.5" width="2.34" height="51.1" fill="var(--down)"/>
<line x1="695.6" y1="285.4" x2="695.6" y2="310.3" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="290.9" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="699.3" y1="302.5" x2="699.3" y2="330.3" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="304.2" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="703.1" y1="313.2" x2="703.1" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="315.4" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="706.9" y1="328.2" x2="706.9" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="335.7" width="2.34" height="23.9" fill="var(--down)"/>
<line x1="710.6" y1="359.3" x2="710.6" y2="384.6" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="359.3" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="714.4" y1="361.2" x2="714.4" y2="378.0" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="367.7" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="718.2" y1="366.7" x2="718.2" y2="379.4" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="372.0" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="722.0" y1="380.7" x2="722.0" y2="407.8" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="382.5" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="725.7" y1="363.3" x2="725.7" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="365.8" width="2.34" height="30.8" fill="var(--up)"/>
<line x1="729.5" y1="338.0" x2="729.5" y2="360.5" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="356.2" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="733.3" y1="341.6" x2="733.3" y2="424.8" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="351.7" width="2.34" height="53.6" fill="var(--down)"/>
<line x1="737.0" y1="407.6" x2="737.0" y2="433.0" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="411.3" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="740.8" y1="421.4" x2="740.8" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="431.5" width="2.34" height="31.2" fill="var(--down)"/>
<line x1="744.6" y1="433.0" x2="744.6" y2="462.2" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="437.4" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="748.4" y1="421.6" x2="748.4" y2="440.5" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="423.4" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="752.1" y1="384.3" x2="752.1" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="389.8" width="2.34" height="30.0" fill="var(--up)"/>
<line x1="755.9" y1="360.2" x2="755.9" y2="415.3" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="387.2" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="759.7" y1="378.5" x2="759.7" y2="449.2" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="404.0" width="2.34" height="34.8" fill="var(--down)"/>
<line x1="763.5" y1="422.2" x2="763.5" y2="461.1" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="436.3" width="2.34" height="22.9" fill="var(--up)"/>
<line x1="767.2" y1="406.8" x2="767.2" y2="449.8" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="436.1" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="771.0" y1="383.3" x2="771.0" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="388.0" width="2.34" height="76.0" fill="var(--up)"/>
<line x1="774.8" y1="376.6" x2="774.8" y2="426.3" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="391.1" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="778.5" y1="382.9" x2="778.5" y2="435.0" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="384.1" width="2.34" height="26.5" fill="var(--up)"/>
<line x1="782.3" y1="364.7" x2="782.3" y2="398.7" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="381.7" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="786.1" y1="382.1" x2="786.1" y2="404.6" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="389.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="789.9" y1="386.9" x2="789.9" y2="431.1" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="390.1" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="793.6" y1="379.3" x2="793.6" y2="401.5" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="396.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="797.4" y1="377.2" x2="797.4" y2="401.9" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="377.2" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="801.2" y1="370.8" x2="801.2" y2="392.6" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="378.2" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="804.9" y1="368.7" x2="804.9" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="371.4" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="808.7" y1="376.7" x2="808.7" y2="407.9" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="377.8" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="812.5" y1="377.3" x2="812.5" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="390.9" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="816.3" y1="395.9" x2="816.3" y2="412.6" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="405.9" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="820.0" y1="394.3" x2="820.0" y2="415.3" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="398.7" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="823.8" y1="388.2" x2="823.8" y2="408.1" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="395.1" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="827.6" y1="398.9" x2="827.6" y2="481.5" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="402.8" width="2.34" height="62.7" fill="var(--down)"/>
<line x1="831.3" y1="454.5" x2="831.3" y2="478.0" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="458.8" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="835.1" y1="443.3" x2="835.1" y2="468.7" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="459.1" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="838.9" y1="432.8" x2="838.9" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="441.9" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="842.7" y1="420.3" x2="842.7" y2="440.4" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="429.5" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="846.4" y1="409.7" x2="846.4" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="415.9" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="850.2" y1="403.8" x2="850.2" y2="428.8" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="403.9" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="854.0" y1="390.8" x2="854.0" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="393.2" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="857.7" y1="382.9" x2="857.7" y2="398.0" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="390.9" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="861.5" y1="358.7" x2="861.5" y2="390.8" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="369.9" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="865.3" y1="342.0" x2="865.3" y2="367.4" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="345.3" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="869.1" y1="328.7" x2="869.1" y2="351.0" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="342.3" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="872.8" y1="341.1" x2="872.8" y2="372.8" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="348.5" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="876.6" y1="342.3" x2="876.6" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="357.0" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="880.4" y1="359.8" x2="880.4" y2="380.9" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="363.5" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="884.2" y1="364.1" x2="884.2" y2="415.0" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="364.8" width="2.34" height="47.1" fill="var(--down)"/>
<line x1="887.9" y1="400.3" x2="887.9" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="401.2" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="891.7" y1="373.5" x2="891.7" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="399.0" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="895.5" y1="407.8" x2="895.5" y2="426.2" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="410.4" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="899.2" y1="418.1" x2="899.2" y2="442.4" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="419.2" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="903.0" y1="379.5" x2="903.0" y2="421.8" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="380.3" width="2.34" height="38.6" fill="var(--up)"/>
<line x1="906.8" y1="373.8" x2="906.8" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="382.1" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="910.6" y1="364.6" x2="910.6" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="376.3" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="914.3" y1="355.9" x2="914.3" y2="385.7" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="356.1" width="2.34" height="19.1" fill="var(--up)"/>
<line x1="918.1" y1="285.3" x2="918.1" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="289.9" width="2.34" height="56.3" fill="var(--up)"/>
<line x1="921.9" y1="232.2" x2="921.9" y2="293.7" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="232.9" width="2.34" height="48.3" fill="var(--up)"/>
<line x1="925.6" y1="213.0" x2="925.6" y2="245.9" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="220.8" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="929.4" y1="141.6" x2="929.4" y2="245.3" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="158.1" width="2.34" height="63.8" fill="var(--up)"/>
<line x1="933.2" y1="140.3" x2="933.2" y2="214.7" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="173.5" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="937.0" y1="126.2" x2="937.0" y2="176.2" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="131.6" width="2.34" height="39.4" fill="var(--up)"/>
<line x1="940.7" y1="106.9" x2="940.7" y2="146.9" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="123.4" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="944.5" y1="107.8" x2="944.5" y2="158.4" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="123.7" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="948.3" y1="74.8" x2="948.3" y2="139.4" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="84.1" width="2.34" height="19.8" fill="var(--down)"/>
<line x1="952.0" y1="97.7" x2="952.0" y2="149.1" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="98.5" width="2.34" height="42.7" fill="var(--down)"/>
<line x1="955.8" y1="133.1" x2="955.8" y2="175.2" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="142.3" width="2.34" height="25.7" fill="var(--down)"/>
<line x1="959.6" y1="160.0" x2="959.6" y2="200.3" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="165.6" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="963.4" y1="169.3" x2="963.4" y2="216.4" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="174.6" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="967.1" y1="152.8" x2="967.1" y2="199.6" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="174.2" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="970.9" y1="175.0" x2="970.9" y2="224.2" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="181.7" width="2.34" height="37.1" fill="var(--down)"/>
<line x1="974.7" y1="210.4" x2="974.7" y2="346.6" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="216.8" width="2.34" height="115.7" fill="var(--down)"/>
<line x1="978.4" y1="311.9" x2="978.4" y2="349.0" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="331.5" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="982.2" y1="316.5" x2="982.2" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="332.5" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="986.0" y1="315.8" x2="986.0" y2="348.3" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="328.7" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="989.8" y1="302.4" x2="989.8" y2="333.4" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="303.9" width="2.34" height="22.3" fill="var(--up)"/>
<line x1="993.5" y1="292.4" x2="993.5" y2="316.8" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="299.9" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="997.3" y1="311.4" x2="997.3" y2="337.2" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="317.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1001.1" y1="278.2" x2="1001.1" y2="327.5" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="293.6" width="2.34" height="25.0" fill="var(--up)"/>
<line x1="1004.9" y1="294.9" x2="1004.9" y2="344.3" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="300.7" width="2.34" height="35.3" fill="var(--down)"/>
<line x1="1008.6" y1="325.5" x2="1008.6" y2="366.2" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="339.6" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="1012.4" y1="285.5" x2="1012.4" y2="354.3" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="285.6" width="2.34" height="54.0" fill="var(--up)"/>
<line x1="1016.2" y1="283.3" x2="1016.2" y2="331.9" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="286.9" width="2.34" height="31.4" fill="var(--down)"/>
<line x1="1019.9" y1="312.2" x2="1019.9" y2="340.7" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="315.7" width="2.34" height="23.4" fill="var(--down)"/>
<line x1="1023.7" y1="224.2" x2="1023.7" y2="370.4" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="232.6" width="2.34" height="103.9" fill="var(--up)"/>
<line x1="1027.5" y1="216.5" x2="1027.5" y2="270.2" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="232.4" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="1031.3" y1="216.6" x2="1031.3" y2="240.7" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="224.9" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="1035.0" y1="192.6" x2="1035.0" y2="224.8" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="195.0" width="2.34" height="24.4" fill="var(--up)"/>
<line x1="1038.8" y1="189.1" x2="1038.8" y2="260.8" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="199.6" width="2.34" height="60.5" fill="var(--down)"/>
<line x1="1042.6" y1="250.9" x2="1042.6" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="259.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1046.3" y1="258.1" x2="1046.3" y2="308.3" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="259.9" width="2.34" height="46.4" fill="var(--down)"/>
<line x1="1050.1" y1="297.1" x2="1050.1" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="299.9" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="60" y1="413.1" x2="1052" y2="413.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="407.1" font-size="11.5" fill="var(--support)" font-weight="600">$458 S1</text>
<text x="1058" y="419.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="439.4" x2="1052" y2="439.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="433.4" font-size="11.5" fill="var(--support)" font-weight="600">$439 S2</text>
<text x="1058" y="445.4" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="473.5" x2="1052" y2="473.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="467.5" font-size="11.5" fill="var(--support)" font-weight="600">$416 S3</text>
<text x="1058" y="479.5" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="304.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="296.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $533 (2026-09-03)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$532.95** (2026-09-03 종가) | — | **5년 구간 안에 상단 저항 클러스터가 없다** — 아래 서술 참고 |
| S1 | $458 | 2 | 2023-03-13 · 2024-05-27 — 현재가에서 **−14.1%**. 2023~2024년 횡보 구간의 상단부 저점대 |
| S2 | $439 | 5 | 2023-01-16 · 2023-05-22 · 2023-12-11 · 2025-06-09 · 2025-12-01 — **터치 5회로 5년 구간 전체에서 가장 두터운 레벨**. 2023년과 2025년, 서로 다른 두 국면에서 반복적으로 지지했다. 현재가에서 −17.6% |
| S3 | $416 | 4 | 2024-02-12 · 2025-02-10 · 2025-04-07 · 2025-07-21 — 현재가에서 −21.9%. **마지막 터치(2025-07-21)가 아래 3절의 손실충당 급락 주간**이다 |
| 참고선 | $692.00 | — | 5년 최고가(2026-03-02 주간). 단일 고점이라 클러스터를 이루지 않았고 현재가에서 **+29.8%** 떨어져 있다 |
| 참고선 | $324.23 | — | 5년 최저가(2022년 초). 4년 전 가격이고 그 사이 EPS·배당이 크게 달라져 현재 지지선으로 보지 않는다 |

**상단에 저항 클러스터가 하나도 잡히지 않은 이유**는 신고가 구간이어서가 아니라, **2026년 상승분이 너무 빨라 그 가격대에서 스윙 고점이 두 번 이상 형성될 시간이 없었기 때문**이다. 2026년 1월 $500 → 3월 $692 → 9월 $533의 급등·급락 궤적에서 $547·$642는 [일봉 차트](./09_technical_daily.md)에서만 클러스터로 잡힌다. **주봉 기준으로는 현재가 위쪽이 사실상 미검증 구간**이라는 뜻이며, 이는 저항이 없다는 것이 아니라 근거로 삼을 관측치가 없다는 뜻이다.

유효한 클러스터가 하방 3개뿐이라 R1~R3는 만들지 않았다. `--force-level`은 쓰지 않았다.

---

## 3. 관측된 특이 구간 — 2025-07-21 주간, 손실충당 발표

- 2025년 2분기 실적 발표(2025-07-22)에서 세전 $1,681M 손실충당을 인식했다([최근 뉴스 / 이슈](./08_news.md) 로그, [핵심 지표](./04_metrics.md) warning 1번).
- 종가 기준 **하루 −10.8%** ($460.53 → $410.74), 거래량 **889만 주**로 평소(주평균 668만 주를 5거래일로 나누면 일 134만 주 내외) 대비 약 **6.6배**. 5년 구간에서 **두 번째로 큰 하락일**이다(1위는 2021-10-26의 −11.8%).
- 이 주간이 S3($416) 클러스터의 마지막 터치를 만들었고, 그 뒤 5개월간 $410~$480 박스에서 바닥을 다졌다. **2026년 1월 실적 발표를 계기로 이 박스를 위로 이탈**하면서 3월 $692까지 갔다 — 즉 현재 형성된 하방 클러스터 3개(S1·S2·S3)는 **전부 이 손실충당 국면 전후에 만들어진 가격대**다.

**참고 — 5년 최대 하락일**: 2021-10-26 **−11.8%**($376.33 → $331.91). 2021년 3분기 실적에서 향후 매출 전망을 하향한 날로, 이 차트 구간의 시작 부근이다. 그 이후 러시아·우크라이나 전쟁으로 방산 재평가가 시작되며 2022년 내내 반등했다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-30~2026-09-03. 수집 시점: 2026-09-04. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py LMT --name "록히드마틴" --interval 1wk --close-on 2026-09-03 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **기간 내 배당 20회가 반영되지 않은 원주가**다. 5년 누적 배당은 약 $60(현재가의 11%)이므로, 배당을 반영한 총수익 기준으로 보면 위 레벨들은 실제보다 아래로 눌려 있다. 특히 5년 전 가격($324~376)과 현재가를 직접 비교할 때 오차가 크다.
    - 3절의 −10.8% 급락은 **가격대를 구조적으로 재설정한 사건**이다. 그 이전(2021~2025 상반기)의 스윙 저점과 이후의 저점을 같은 클러스터로 묶어도 되는지에 대한 판단은 스크립트가 하지 않는다 — S2($439)가 2023년과 2025년 두 국면에 걸쳐 있는 것이 그 사례이며, **서로 다른 실적 체력의 시기를 한 레벨로 묶은 값**이라는 점을 감안해서 읽어야 한다.
    - 이 기간에 주식분할·대규모 유상증자는 없었다. 자사주매입(5년 누적 $20B 이상)은 주식수를 줄여 EPS를 밀어올렸지만 가격 연속성은 깨지 않는다.

---

*작성일: 2026-09-04*
