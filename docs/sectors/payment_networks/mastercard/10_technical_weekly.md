# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-01 종가 **$581.10**은 일봉 차트·[핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)의 값과 **일치**한다. 모두 배당 미반영 원주가 기준이다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-09-01)

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
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mastercard(MA) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Mastercard (MA) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-09-01 · 마지막 종가 $581.10 (2026-09-01) · 단위 USD</text>
<line x1="60" y1="569.0" x2="1052" y2="569.0" class="grid"/>
<text x="52" y="573.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="487.6" x2="1052" y2="487.6" class="grid"/>
<text x="52" y="491.6" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="406.1" x2="1052" y2="406.1" class="grid"/>
<text x="52" y="410.1" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="324.7" x2="1052" y2="324.7" class="grid"/>
<text x="52" y="328.7" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="243.3" x2="1052" y2="243.3" class="grid"/>
<text x="52" y="247.3" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="161.9" x2="1052" y2="161.9" class="grid"/>
<text x="52" y="165.9" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="80.4" x2="1052" y2="80.4" class="grid"/>
<text x="52" y="84.4" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
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
<line x1="61.9" y1="484.2" x2="61.9" y2="505.6" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="491.8" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="65.7" y1="479.4" x2="65.7" y2="498.9" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="491.8" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="69.4" y1="484.3" x2="69.4" y2="502.6" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="487.6" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="73.2" y1="471.4" x2="73.2" y2="511.0" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="474.3" width="2.34" height="32.3" fill="var(--up)"/>
<line x1="77.0" y1="466.1" x2="77.0" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="471.0" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="80.7" y1="470.2" x2="80.7" y2="505.3" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="471.4" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="84.5" y1="476.8" x2="84.5" y2="508.8" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="477.8" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="88.3" y1="467.2" x2="88.3" y2="492.0" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="473.5" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="92.1" y1="459.3" x2="92.1" y2="522.0" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="467.3" width="2.34" height="43.9" fill="var(--down)"/>
<line x1="95.8" y1="487.3" x2="95.8" y2="531.0" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="489.5" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="99.6" y1="465.0" x2="99.6" y2="504.4" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="465.6" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="103.4" y1="453.2" x2="103.4" y2="505.3" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="462.9" width="2.34" height="41.4" fill="var(--down)"/>
<line x1="107.1" y1="501.4" x2="107.1" y2="538.1" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="504.2" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="110.9" y1="517.2" x2="110.9" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="520.1" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="114.7" y1="487.2" x2="114.7" y2="533.2" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="487.7" width="2.34" height="41.0" fill="var(--up)"/>
<line x1="118.5" y1="481.4" x2="118.5" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="488.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="122.2" y1="467.3" x2="122.2" y2="510.0" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="470.3" width="2.34" height="31.5" fill="var(--up)"/>
<line x1="126.0" y1="463.7" x2="126.0" y2="478.5" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="471.3" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="129.8" y1="434.6" x2="129.8" y2="472.5" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="455.6" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="133.6" y1="442.5" x2="133.6" y2="489.6" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="451.5" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="137.3" y1="450.0" x2="137.3" y2="480.9" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="453.7" width="2.34" height="25.6" fill="var(--down)"/>
<line x1="141.1" y1="434.2" x2="141.1" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="434.6" width="2.34" height="65.0" fill="var(--up)"/>
<line x1="144.9" y1="406.3" x2="144.9" y2="444.8" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="435.1" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="148.6" y1="425.0" x2="148.6" y2="458.8" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="435.1" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="152.4" y1="430.6" x2="152.4" y2="460.3" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="455.1" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="156.2" y1="448.0" x2="156.2" y2="501.7" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="456.5" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="160.0" y1="462.6" x2="160.0" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="467.7" width="2.34" height="51.2" fill="var(--down)"/>
<line x1="163.7" y1="518.6" x2="163.7" y2="559.9" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="520.8" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="167.5" y1="483.1" x2="167.5" y2="524.6" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="487.4" width="2.34" height="34.2" fill="var(--up)"/>
<line x1="171.3" y1="481.2" x2="171.3" y2="502.7" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="489.2" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="175.0" y1="453.8" x2="175.0" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="464.8" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="178.8" y1="455.4" x2="178.8" y2="494.7" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="464.4" width="2.34" height="19.5" fill="var(--down)"/>
<line x1="182.6" y1="466.5" x2="182.6" y2="499.2" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="474.8" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="186.4" y1="446.5" x2="186.4" y2="486.6" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="481.1" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="190.1" y1="435.5" x2="190.1" y2="498.0" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="465.8" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="193.9" y1="456.2" x2="193.9" y2="502.6" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="466.4" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="197.7" y1="500.0" x2="197.7" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="502.2" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="201.4" y1="501.3" x2="201.4" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="510.1" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="205.2" y1="474.9" x2="205.2" y2="510.4" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="474.9" width="2.34" height="30.5" fill="var(--up)"/>
<line x1="209.0" y1="463.1" x2="209.0" y2="485.7" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="474.8" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="212.8" y1="457.8" x2="212.8" y2="512.7" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="468.0" width="2.34" height="44.4" fill="var(--down)"/>
<line x1="216.5" y1="518.7" x2="216.5" y2="563.1" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="533.2" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="220.3" y1="518.8" x2="220.3" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="519.3" width="2.34" height="23.5" fill="var(--up)"/>
<line x1="224.1" y1="508.5" x2="224.1" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="516.9" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="227.8" y1="528.3" x2="227.8" y2="553.6" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="531.4" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="231.6" y1="511.1" x2="231.6" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="516.0" width="2.34" height="21.5" fill="var(--up)"/>
<line x1="235.4" y1="485.8" x2="235.4" y2="520.5" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="497.5" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="239.2" y1="476.5" x2="239.2" y2="518.1" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="481.4" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="242.9" y1="473.5" x2="242.9" y2="497.4" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="475.3" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="246.7" y1="472.9" x2="246.7" y2="495.1" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="472.9" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="250.5" y1="468.1" x2="250.5" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="480.6" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="254.3" y1="485.9" x2="254.3" y2="517.4" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="487.6" width="2.34" height="29.4" fill="var(--down)"/>
<line x1="258.0" y1="515.3" x2="258.0" y2="537.7" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="520.2" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="261.8" y1="508.7" x2="261.8" y2="535.5" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="510.6" width="2.34" height="21.7" fill="var(--up)"/>
<line x1="265.6" y1="504.7" x2="265.6" y2="554.2" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="507.0" width="2.34" height="37.4" fill="var(--down)"/>
<line x1="269.3" y1="543.8" x2="269.3" y2="584.9" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="549.5" width="2.34" height="29.9" fill="var(--down)"/>
<line x1="273.1" y1="572.4" x2="273.1" y2="598.8" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="585.2" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="276.9" y1="558.3" x2="276.9" y2="593.6" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="577.2" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="280.7" y1="571.2" x2="280.7" y2="606.7" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="573.8" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="284.4" y1="563.0" x2="284.4" y2="583.1" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="565.1" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="288.2" y1="517.2" x2="288.2" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="521.0" width="2.34" height="40.6" fill="var(--up)"/>
<line x1="292.0" y1="514.2" x2="292.0" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="522.0" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="295.7" y1="499.6" x2="295.7" y2="544.3" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="505.0" width="2.34" height="27.4" fill="var(--up)"/>
<line x1="299.5" y1="485.6" x2="299.5" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="497.8" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="303.3" y1="485.3" x2="303.3" y2="507.8" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="485.5" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="307.1" y1="467.6" x2="307.1" y2="502.6" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="471.2" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="310.8" y1="473.1" x2="310.8" y2="501.5" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="477.8" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="314.6" y1="456.2" x2="314.6" y2="499.7" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="487.1" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="318.4" y1="491.5" x2="318.4" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="495.1" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="322.1" y1="488.0" x2="322.1" y2="501.0" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="491.3" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="325.9" y1="457.1" x2="325.9" y2="497.4" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="458.8" width="2.34" height="28.8" fill="var(--up)"/>
<line x1="329.7" y1="436.9" x2="329.7" y2="459.5" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="446.0" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="333.5" y1="441.4" x2="333.5" y2="465.4" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="444.8" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="337.2" y1="422.4" x2="337.2" y2="450.1" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="444.0" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="341.0" y1="437.9" x2="341.0" y2="459.9" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="448.6" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="344.8" y1="443.5" x2="344.8" y2="466.5" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="455.0" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="348.5" y1="449.4" x2="348.5" y2="471.6" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="457.3" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="352.3" y1="468.4" x2="352.3" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="476.6" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="356.1" y1="468.5" x2="356.1" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="468.8" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="359.9" y1="456.4" x2="359.9" y2="495.3" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="468.3" width="2.34" height="24.0" fill="var(--down)"/>
<line x1="363.6" y1="477.6" x2="363.6" y2="503.5" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="488.1" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="367.4" y1="471.3" x2="367.4" y2="493.6" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="484.9" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="371.2" y1="465.3" x2="371.2" y2="483.0" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="465.7" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="375.0" y1="456.4" x2="375.0" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="467.0" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="378.7" y1="449.5" x2="378.7" y2="475.2" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="451.0" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="382.5" y1="442.9" x2="382.5" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="446.5" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="386.3" y1="435.6" x2="386.3" y2="469.7" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="438.7" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="390.0" y1="430.3" x2="390.0" y2="453.5" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="431.1" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="393.8" y1="426.6" x2="393.8" y2="442.5" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="432.2" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="397.6" y1="418.8" x2="397.6" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="429.6" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="401.4" y1="426.7" x2="401.4" y2="463.3" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="430.6" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="405.1" y1="444.2" x2="405.1" y2="474.8" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="444.8" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="408.9" y1="437.9" x2="408.9" y2="461.8" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="450.5" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="412.7" y1="434.0" x2="412.7" y2="455.3" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="444.4" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="416.4" y1="436.9" x2="416.4" y2="449.8" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="439.0" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="420.2" y1="414.0" x2="420.2" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="417.1" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="424.0" y1="413.9" x2="424.0" y2="427.1" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="420.2" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="427.8" y1="400.5" x2="427.8" y2="425.7" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="402.1" width="2.34" height="22.8" fill="var(--up)"/>
<line x1="431.5" y1="399.6" x2="431.5" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="403.0" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="435.3" y1="397.7" x2="435.3" y2="424.3" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="410.2" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="439.1" y1="410.5" x2="439.1" y2="428.3" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="416.0" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="442.8" y1="405.1" x2="442.8" y2="422.2" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="414.3" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="446.6" y1="407.4" x2="446.6" y2="424.3" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="411.9" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="450.4" y1="398.6" x2="450.4" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="401.4" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="454.2" y1="377.2" x2="454.2" y2="401.0" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="380.8" width="2.34" height="18.8" fill="var(--up)"/>
<line x1="457.9" y1="379.5" x2="457.9" y2="391.7" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="382.0" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="461.7" y1="375.9" x2="461.7" y2="393.5" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="378.7" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="465.5" y1="377.0" x2="465.5" y2="403.6" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="383.5" width="2.34" height="19.0" fill="var(--down)"/>
<line x1="469.2" y1="400.9" x2="469.2" y2="420.0" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="405.2" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="473.0" y1="404.5" x2="473.0" y2="424.7" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="409.4" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="476.8" y1="397.4" x2="476.8" y2="423.1" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="409.4" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="480.6" y1="398.9" x2="480.6" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="405.8" width="2.34" height="25.8" fill="var(--down)"/>
<line x1="484.3" y1="423.4" x2="484.3" y2="471.7" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="435.0" width="2.34" height="29.7" fill="var(--down)"/>
<line x1="488.1" y1="425.0" x2="488.1" y2="463.6" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="428.9" width="2.34" height="31.8" fill="var(--up)"/>
<line x1="491.9" y1="414.1" x2="491.9" y2="431.9" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="415.3" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="495.7" y1="403.4" x2="495.7" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="405.7" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="499.4" y1="385.0" x2="499.4" y2="409.0" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="385.8" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="503.2" y1="379.1" x2="503.2" y2="394.0" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="382.8" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="507.0" y1="382.0" x2="507.0" y2="399.1" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="383.6" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="510.7" y1="363.2" x2="510.7" y2="387.3" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="375.9" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="514.5" y1="361.2" x2="514.5" y2="374.8" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="366.9" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="518.3" y1="360.0" x2="518.3" y2="368.8" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="363.0" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="522.1" y1="366.6" x2="522.1" y2="378.5" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="366.9" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="525.8" y1="354.4" x2="525.8" y2="379.2" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="358.8" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="529.6" y1="345.8" x2="529.6" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="346.2" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="533.4" y1="339.5" x2="533.4" y2="356.2" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="342.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="537.1" y1="302.2" x2="537.1" y2="349.7" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="307.5" width="2.34" height="40.4" fill="var(--up)"/>
<line x1="540.9" y1="304.8" x2="540.9" y2="316.0" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="309.2" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="544.7" y1="285.4" x2="544.7" y2="314.9" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="295.2" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="548.5" y1="283.7" x2="548.5" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="286.6" width="2.34" height="33.6" fill="var(--up)"/>
<line x1="552.2" y1="277.3" x2="552.2" y2="292.2" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="281.3" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="556.0" y1="281.3" x2="556.0" y2="300.9" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="282.9" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="559.8" y1="272.6" x2="559.8" y2="300.8" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="282.6" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="563.5" y1="259.6" x2="563.5" y2="281.3" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="273.1" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="567.3" y1="271.9" x2="567.3" y2="288.4" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="273.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="571.1" y1="270.5" x2="571.1" y2="293.8" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="274.8" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="574.9" y1="276.4" x2="574.9" y2="305.0" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="281.7" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="578.6" y1="290.5" x2="578.6" y2="320.5" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="291.8" width="2.34" height="24.2" fill="var(--down)"/>
<line x1="582.4" y1="295.2" x2="582.4" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="304.5" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="586.2" y1="305.8" x2="586.2" y2="346.0" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="306.9" width="2.34" height="28.3" fill="var(--down)"/>
<line x1="589.9" y1="310.7" x2="589.9" y2="331.9" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="313.3" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="593.7" y1="300.4" x2="593.7" y2="325.9" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="308.0" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="597.5" y1="304.4" x2="597.5" y2="324.2" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="309.3" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="601.3" y1="323.7" x2="601.3" y2="342.2" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="324.7" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="605.0" y1="319.8" x2="605.0" y2="344.4" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="325.1" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="608.8" y1="320.6" x2="608.8" y2="342.1" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="327.3" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="612.6" y1="316.1" x2="612.6" y2="338.3" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="316.8" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="616.3" y1="303.4" x2="616.3" y2="343.1" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="316.7" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="620.1" y1="324.8" x2="620.1" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="325.5" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="623.9" y1="323.7" x2="623.9" y2="358.8" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="325.9" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="627.7" y1="315.9" x2="627.7" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="335.0" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="631.4" y1="326.6" x2="631.4" y2="359.1" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="332.2" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="635.2" y1="285.6" x2="635.2" y2="348.5" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="305.1" width="2.34" height="37.8" fill="var(--up)"/>
<line x1="639.0" y1="306.3" x2="639.0" y2="341.7" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="313.7" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="642.8" y1="291.7" x2="642.8" y2="318.4" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="294.0" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="646.5" y1="290.7" x2="646.5" y2="305.3" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="293.8" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="650.3" y1="266.5" x2="650.3" y2="297.0" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="270.4" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="654.1" y1="265.0" x2="654.1" y2="287.1" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="271.8" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="657.8" y1="248.4" x2="657.8" y2="279.4" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="254.1" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="661.6" y1="240.4" x2="661.6" y2="265.7" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="250.9" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="665.4" y1="247.0" x2="665.4" y2="270.1" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="253.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="669.2" y1="244.8" x2="669.2" y2="260.1" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="247.0" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="672.9" y1="238.5" x2="672.9" y2="258.4" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="239.6" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="676.7" y1="214.0" x2="676.7" y2="239.9" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="216.7" width="2.34" height="19.5" fill="var(--up)"/>
<line x1="680.5" y1="212.6" x2="680.5" y2="234.1" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="215.6" width="2.34" height="15.7" fill="var(--down)"/>
<line x1="684.2" y1="197.8" x2="684.2" y2="245.7" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="230.1" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="688.0" y1="196.3" x2="688.0" y2="238.4" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="203.0" width="2.34" height="25.4" fill="var(--up)"/>
<line x1="691.8" y1="187.9" x2="691.8" y2="216.5" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="196.3" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="695.6" y1="205.0" x2="695.6" y2="225.4" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="209.3" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="699.3" y1="185.0" x2="699.3" y2="209.1" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="189.6" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="703.1" y1="186.6" x2="703.1" y2="213.7" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="189.7" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="706.9" y1="183.4" x2="706.9" y2="210.4" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="196.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="710.6" y1="182.8" x2="710.6" y2="211.7" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="191.2" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="714.4" y1="181.9" x2="714.4" y2="208.9" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="190.8" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="718.2" y1="193.5" x2="718.2" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="199.3" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="722.0" y1="208.5" x2="722.0" y2="237.8" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="209.1" width="2.34" height="26.5" fill="var(--down)"/>
<line x1="725.7" y1="197.5" x2="725.7" y2="243.4" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="203.1" width="2.34" height="38.6" fill="var(--up)"/>
<line x1="729.5" y1="184.6" x2="729.5" y2="201.5" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="188.7" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="733.3" y1="118.0" x2="733.3" y2="191.7" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="153.0" width="2.34" height="35.6" fill="var(--up)"/>
<line x1="737.0" y1="126.0" x2="737.0" y2="160.1" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="141.1" width="2.34" height="16.5" fill="var(--up)"/>
<line x1="740.8" y1="130.5" x2="740.8" y2="146.8" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="137.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="744.6" y1="128.1" x2="744.6" y2="151.1" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="137.6" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="748.4" y1="118.8" x2="748.4" y2="157.5" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="119.0" width="2.34" height="29.1" fill="var(--up)"/>
<line x1="752.1" y1="109.4" x2="752.1" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="117.3" width="2.34" height="49.8" fill="var(--down)"/>
<line x1="755.9" y1="164.2" x2="755.9" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="181.2" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="759.7" y1="177.3" x2="759.7" y2="208.3" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="185.2" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="763.5" y1="142.6" x2="763.5" y2="181.0" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="177.1" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="767.2" y1="159.5" x2="767.2" y2="262.4" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="190.9" width="2.34" height="69.0" fill="var(--down)"/>
<line x1="771.0" y1="213.1" x2="771.0" y2="299.3" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="227.4" width="2.34" height="50.9" fill="var(--up)"/>
<line x1="774.8" y1="204.2" x2="774.8" y2="229.4" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="215.1" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="778.5" y1="171.7" x2="778.5" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="188.8" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="782.3" y1="141.7" x2="782.3" y2="195.2" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="146.6" width="2.34" height="38.0" fill="var(--up)"/>
<line x1="786.1" y1="123.0" x2="786.1" y2="152.3" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="131.5" width="2.34" height="17.6" fill="var(--up)"/>
<line x1="789.9" y1="106.0" x2="789.9" y2="135.1" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="107.7" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="793.6" y1="99.2" x2="793.6" y2="141.5" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="111.3" width="2.34" height="28.4" fill="var(--down)"/>
<line x1="797.4" y1="103.9" x2="797.4" y2="135.0" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="103.9" width="2.34" height="30.6" fill="var(--up)"/>
<line x1="801.2" y1="94.8" x2="801.2" y2="123.7" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="96.5" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="804.9" y1="89.0" x2="804.9" y2="157.8" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="98.8" width="2.34" height="43.5" fill="var(--down)"/>
<line x1="808.7" y1="121.1" x2="808.7" y2="198.8" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="139.2" width="2.34" height="50.4" fill="var(--down)"/>
<line x1="812.5" y1="138.9" x2="812.5" y2="198.4" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="161.3" width="2.34" height="30.8" fill="var(--up)"/>
<line x1="816.3" y1="129.8" x2="816.3" y2="158.8" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="130.5" width="2.34" height="27.3" fill="var(--up)"/>
<line x1="820.0" y1="128.1" x2="820.0" y2="168.6" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="128.2" width="2.34" height="33.4" fill="var(--down)"/>
<line x1="823.8" y1="147.1" x2="823.8" y2="165.5" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="157.5" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="827.6" y1="129.4" x2="827.6" y2="158.5" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="132.2" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="831.3" y1="113.9" x2="831.3" y2="153.4" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="133.6" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="835.1" y1="119.3" x2="835.1" y2="155.6" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="122.3" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="838.9" y1="97.4" x2="838.9" y2="130.2" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="110.2" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="842.7" y1="77.5" x2="842.7" y2="111.9" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="82.1" width="2.34" height="27.6" fill="var(--up)"/>
<line x1="846.4" y1="82.0" x2="846.4" y2="102.8" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="84.0" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="850.2" y1="82.7" x2="850.2" y2="114.6" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="87.6" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="854.0" y1="94.8" x2="854.0" y2="127.7" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="108.7" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="857.7" y1="77.8" x2="857.7" y2="118.2" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="106.2" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="861.5" y1="101.0" x2="861.5" y2="139.0" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="111.4" width="2.34" height="25.8" fill="var(--down)"/>
<line x1="865.3" y1="107.8" x2="865.3" y2="141.5" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="112.3" width="2.34" height="23.5" fill="var(--up)"/>
<line x1="869.1" y1="103.1" x2="869.1" y2="151.0" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="114.3" width="2.34" height="35.4" fill="var(--down)"/>
<line x1="872.8" y1="129.6" x2="872.8" y2="166.1" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="144.0" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="876.6" y1="111.7" x2="876.6" y2="155.7" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="123.3" width="2.34" height="19.5" fill="var(--up)"/>
<line x1="880.4" y1="120.0" x2="880.4" y2="172.4" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="120.0" width="2.34" height="38.6" fill="var(--down)"/>
<line x1="884.2" y1="147.7" x2="884.2" y2="177.6" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="158.6" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="887.9" y1="135.9" x2="887.9" y2="171.5" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="158.1" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="891.7" y1="163.0" x2="891.7" y2="203.1" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="168.4" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="895.5" y1="159.6" x2="895.5" y2="186.1" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="161.0" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="899.2" y1="147.2" x2="899.2" y2="178.9" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="165.7" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="903.0" y1="123.2" x2="903.0" y2="184.8" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="126.1" width="2.34" height="41.1" fill="var(--up)"/>
<line x1="906.8" y1="123.9" x2="906.8" y2="141.5" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="124.6" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="910.6" y1="109.3" x2="910.6" y2="127.7" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="113.7" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="914.3" y1="109.8" x2="914.3" y2="146.4" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="113.7" width="2.34" height="26.8" fill="var(--down)"/>
<line x1="918.1" y1="97.3" x2="918.1" y2="148.1" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="120.3" width="2.34" height="25.9" fill="var(--up)"/>
<line x1="921.9" y1="132.7" x2="921.9" y2="188.4" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="139.0" width="2.34" height="40.0" fill="var(--down)"/>
<line x1="925.6" y1="182.4" x2="925.6" y2="210.5" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="193.5" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="929.4" y1="171.2" x2="929.4" y2="213.5" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="180.1" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="933.2" y1="142.4" x2="933.2" y2="178.5" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="163.9" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="937.0" y1="166.7" x2="937.0" y2="217.2" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="172.1" width="2.34" height="41.3" fill="var(--down)"/>
<line x1="940.7" y1="193.2" x2="940.7" y2="218.9" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="200.3" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="944.5" y1="206.3" x2="944.5" y2="259.6" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="209.9" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="948.3" y1="199.6" x2="948.3" y2="231.3" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="206.9" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="952.0" y1="209.3" x2="952.0" y2="250.8" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="216.8" width="2.34" height="29.8" fill="var(--down)"/>
<line x1="955.8" y1="215.7" x2="955.8" y2="264.0" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="245.5" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="959.6" y1="231.8" x2="959.6" y2="275.0" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="233.4" width="2.34" height="35.5" fill="var(--down)"/>
<line x1="963.4" y1="238.4" x2="963.4" y2="266.7" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="254.0" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="967.1" y1="224.0" x2="967.1" y2="257.6" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="245.5" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="970.9" y1="198.5" x2="970.9" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="208.6" width="2.34" height="40.8" fill="var(--up)"/>
<line x1="974.7" y1="203.4" x2="974.7" y2="250.4" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="209.5" width="2.34" height="27.0" fill="var(--down)"/>
<line x1="978.4" y1="187.6" x2="978.4" y2="256.1" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="242.0" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="982.2" y1="231.4" x2="982.2" y2="260.0" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="250.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="986.0" y1="233.0" x2="986.0" y2="262.8" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="251.4" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="989.8" y1="222.3" x2="989.8" y2="259.5" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="245.7" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="993.5" y1="243.1" x2="993.5" y2="265.5" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="249.8" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="997.3" y1="248.0" x2="997.3" y2="301.1" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="252.6" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="1001.1" y1="245.2" x2="1001.1" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="259.6" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="1004.9" y1="235.7" x2="1004.9" y2="265.0" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="258.8" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="1008.6" y1="235.5" x2="1008.6" y2="270.7" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="244.9" width="2.34" height="17.7" fill="var(--up)"/>
<line x1="1012.4" y1="178.7" x2="1012.4" y2="239.2" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="179.1" width="2.34" height="60.1" fill="var(--up)"/>
<line x1="1016.2" y1="172.2" x2="1016.2" y2="218.7" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="176.9" width="2.34" height="22.8" fill="var(--down)"/>
<line x1="1019.9" y1="159.1" x2="1019.9" y2="195.9" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="172.3" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="1023.7" y1="165.3" x2="1023.7" y2="204.8" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="178.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1027.5" y1="108.7" x2="1027.5" y2="174.9" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="124.2" width="2.34" height="48.7" fill="var(--up)"/>
<line x1="1031.3" y1="107.0" x2="1031.3" y2="142.9" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="113.0" width="2.34" height="27.8" fill="var(--down)"/>
<line x1="1035.0" y1="128.2" x2="1035.0" y2="152.0" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="130.4" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="1038.8" y1="108.2" x2="1038.8" y2="143.5" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="112.0" width="2.34" height="25.1" fill="var(--up)"/>
<line x1="1042.6" y1="78.4" x2="1042.6" y2="106.1" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="93.9" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="1046.3" y1="88.3" x2="1046.3" y2="111.6" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="90.9" width="2.34" height="20.3" fill="var(--down)"/>
<line x1="1050.1" y1="92.4" x2="1050.1" y2="111.5" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="97.3" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="60" y1="103.4" x2="1052" y2="103.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="106.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$586 R1</text>
<text x="1058" y="118.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="200.9" x2="1052" y2="200.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="194.9" font-size="11.5" fill="var(--support)" font-weight="600">$526 S1</text>
<text x="1058" y="206.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="300.2" x2="1052" y2="300.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="294.2" font-size="11.5" fill="var(--support)" font-weight="600">$465 S2</text>
<text x="1058" y="306.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="352.6" x2="1052" y2="352.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="346.6" font-size="11.5" fill="var(--support)" font-weight="600">$433 S3</text>
<text x="1058" y="358.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="111.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="103.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $581 (2026-09-01)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). **일봉 문서의 레벨(전후 5거래일)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다** — 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $586 | 4 | 2025-01-27·2025-03-03·2025-06-09·2026-01-05 주의 고점대. 2025년 내내 네 차례 막힌 뒤 2026년 8월에야 넘어선 5년 최대 저항 |
| **현재가** | **$581.10** (2026-09-01 종가) | — | R1과 S1 사이 |
| S1 | $526 | 2 | 2025-06-16·2025-11-17 주의 저점대 |
| S2 | $465 | 2 | 2025-04-07·2026-06-01 주의 저점대. 1년 이상 떨어진 두 시점에서만 확인돼 강도는 약하다 |
| S3 | $433 | 2 | 2024-04-29·2024-07-22 주의 저점대. 2년 전 가격대라 현재 펀더멘털과의 연결은 약하다 |
| 참고선 | $276.87 | — | 5년 최저(2021년 하반기). 매출이 그 뒤 두 배 이상 늘어 지지선으로 보지 않는다 |

---

## 3. 관측된 특이 구간 — 2025년 상반기 R1($586) 형성

- 2025-01-27·2025-03-03·2025-06-09 세 차례에 걸쳐 $586 부근에서 막히며 **5년 구간 최대 저항이 만들어졌고**, 2026-01-05 주에 한 번 더 확인된 뒤에야 2026년 8월에 넘어섰다. 네 번 시도해 넘은 레벨이라 이후 지지로 작동하는지가 관전 포인트다.
- 같은 기간 밸류에이션 배수는 압축됐다 — FY2023~FY2025 조정 EPS가 누적 +38.7% 늘 때 주가는 +33.9% 오르는 데 그쳤다([밸류에이션 / 적정주가](./06_valuation.md) 2절). **가격이 1년 넘게 한 레벨에 묶여 있는 동안 이익이 먼저 올라온 구간**으로, 기술적 레벨과 펀더멘털이 같은 이야기를 하고 있다.
- 5년 구간 안에서 사업 구조를 바꾼 인수는 Recorded Future(2024-12, $26.5억)와 BVNK(2026-08, $18억)다. 둘 다 매출 규모 대비 크지 않아 과거 레벨의 연속성을 깨지는 않았다고 본다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-30~2026-09-01. 수집 시점: 2026-09-02. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py MA --name Mastercard --interval 1wk --close-on 2026-09-01 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 기간 내 배당이 20회 지급됐으나 **원주가(배당 미반영)** 기준이라 실제 총수익률과는 다르다.
    - S3($433)는 2024년 상반기 저점대로, 그 사이 매출이 $25.1B에서 $32.8B로 늘어 **현재 펀더멘털과의 연결이 약하다** — 위 표에서 터치 2회의 약한 레벨로만 취급한다.
    - 기간 내 주식분할·대규모 유상증자는 없었다.

---

*작성일: 2026-09-02*
