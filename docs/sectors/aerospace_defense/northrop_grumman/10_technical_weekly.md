# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉으로 다년 구조를 보는 참고 자료. 최근 1년의 세부 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)을 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 일봉 문서와 같은 계보이며, [핵심 지표](./04_metrics.md)의 재무 원자료와는 계보가 다르다.
    - **대조 결과**: **2026-09-03 종가 $528.24**는 일봉 문서·[밸류에이션 / 적정주가](./06_valuation.md)와 **일치**한다. 원주가(배당 미반영) 기준이라 [핵심 지표](./04_metrics.md) A.2의 회계연도 말 종가(FY2023 $468.14 / FY2024 $469.29 / FY2025 $570.21)와도 같은 계열이다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-09-03)

<div class="noc-chart">
<style>
.noc-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .noc-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .noc-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.noc-chart svg { width:100%; height:auto; display:block; }
.noc-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.noc-chart .title { fill: var(--ink); font-weight:600; }
.noc-chart .grid { stroke: var(--grid); stroke-width:1; }
.noc-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="노스롭 그루먼(NOC) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">노스롭 그루먼 (NOC) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-09-03 · 마지막 종가 $528.24 (2026-09-03) · 단위 USD</text>
<line x1="60" y1="539.3" x2="1052" y2="539.3" class="grid"/>
<text x="52" y="543.3" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="415.3" x2="1052" y2="415.3" class="grid"/>
<text x="52" y="419.3" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="291.4" x2="1052" y2="291.4" class="grid"/>
<text x="52" y="295.4" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="60" y1="167.5" x2="1052" y2="167.5" class="grid"/>
<text x="52" y="171.5" font-size="11" text-anchor="end" fill="var(--muted)">700</text>
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
<line x1="60" y1="75.8" x2="1052" y2="75.8" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="78.8" font-size="10.5" fill="var(--muted)">$774 2026년 최고</text>
<line x1="61.9" y1="578.6" x2="61.9" y2="582.1" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="579.2" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="65.7" y1="582.0" x2="65.7" y2="597.7" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="584.4" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="69.4" y1="591.9" x2="69.4" y2="604.9" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="594.1" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="73.2" y1="592.4" x2="73.2" y2="607.5" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="594.2" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="77.0" y1="581.4" x2="77.0" y2="594.0" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="587.7" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="80.7" y1="550.5" x2="80.7" y2="587.0" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="552.0" width="2.34" height="34.8" fill="var(--up)"/>
<line x1="84.5" y1="543.3" x2="84.5" y2="559.6" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="545.0" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="88.3" y1="531.4" x2="88.3" y2="548.5" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="531.6" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="92.1" y1="529.3" x2="92.1" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="532.3" width="2.34" height="60.0" fill="var(--down)"/>
<line x1="95.8" y1="580.7" x2="95.8" y2="601.8" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="583.4" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="99.6" y1="580.3" x2="99.6" y2="592.5" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="582.6" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="103.4" y1="586.9" x2="103.4" y2="606.3" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="588.2" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="107.1" y1="578.5" x2="107.1" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="595.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="110.9" y1="590.3" x2="110.9" y2="606.3" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="591.5" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="114.7" y1="574.1" x2="114.7" y2="588.8" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="575.1" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="118.5" y1="560.2" x2="118.5" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="567.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="122.2" y1="558.9" x2="122.2" y2="580.2" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="562.6" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="126.0" y1="553.9" x2="126.0" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="555.3" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="129.8" y1="537.8" x2="129.8" y2="560.6" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="538.7" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="133.6" y1="530.8" x2="133.6" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="533.1" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="137.3" y1="528.1" x2="137.3" y2="544.4" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="535.1" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="141.1" y1="528.4" x2="141.1" y2="577.3" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="541.7" width="2.34" height="22.1" fill="var(--down)"/>
<line x1="144.9" y1="566.3" x2="144.9" y2="583.1" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="568.1" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="148.6" y1="537.7" x2="148.6" y2="578.7" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="540.1" width="2.34" height="35.7" fill="var(--up)"/>
<line x1="152.4" y1="537.6" x2="152.4" y2="563.7" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="543.0" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="156.2" y1="525.5" x2="156.2" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="527.3" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="160.0" y1="448.9" x2="160.0" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="454.3" width="2.34" height="67.2" fill="var(--up)"/>
<line x1="163.7" y1="426.7" x2="163.7" y2="495.0" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="449.5" width="2.34" height="44.8" fill="var(--down)"/>
<line x1="167.5" y1="479.3" x2="167.5" y2="519.1" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="490.6" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="171.3" y1="464.4" x2="171.3" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="467.2" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="175.0" y1="467.5" x2="175.0" y2="500.4" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="471.4" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="178.8" y1="443.5" x2="178.8" y2="484.3" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="460.4" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="182.6" y1="451.3" x2="182.6" y2="465.8" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="456.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="186.4" y1="447.8" x2="186.4" y2="485.9" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="456.0" width="2.34" height="24.5" fill="var(--down)"/>
<line x1="190.1" y1="474.2" x2="190.1" y2="499.1" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="484.8" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="193.9" y1="452.2" x2="193.9" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="454.1" width="2.34" height="39.1" fill="var(--up)"/>
<line x1="197.7" y1="456.3" x2="197.7" y2="486.3" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="457.5" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="201.4" y1="462.1" x2="201.4" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="472.8" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="205.2" y1="444.5" x2="205.2" y2="481.9" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="451.6" width="2.34" height="29.9" fill="var(--up)"/>
<line x1="209.0" y1="441.9" x2="209.0" y2="477.7" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="442.2" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="212.8" y1="424.9" x2="212.8" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="441.0" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="216.5" y1="457.8" x2="216.5" y2="494.6" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="465.2" width="2.34" height="19.6" fill="var(--down)"/>
<line x1="220.3" y1="459.0" x2="220.3" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="460.3" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="224.1" y1="430.3" x2="224.1" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="432.2" width="2.34" height="31.0" fill="var(--up)"/>
<line x1="227.8" y1="431.6" x2="227.8" y2="470.5" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="439.6" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="231.6" y1="437.9" x2="231.6" y2="471.4" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="441.8" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="235.4" y1="459.5" x2="235.4" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="461.2" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="239.2" y1="440.4" x2="239.2" y2="497.3" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="441.5" width="2.34" height="33.5" fill="var(--up)"/>
<line x1="242.9" y1="429.8" x2="242.9" y2="453.3" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="438.4" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="246.7" y1="437.4" x2="246.7" y2="457.8" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="440.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="250.5" y1="418.8" x2="250.5" y2="446.2" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="426.8" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="254.3" y1="419.4" x2="254.3" y2="440.5" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="430.2" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="258.0" y1="428.8" x2="258.0" y2="446.6" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="440.1" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="261.8" y1="421.1" x2="261.8" y2="445.1" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="426.0" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="265.6" y1="426.4" x2="265.6" y2="458.4" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="426.4" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="269.3" y1="396.2" x2="269.3" y2="447.5" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="436.2" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="273.1" y1="432.9" x2="273.1" y2="459.6" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="443.4" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="276.9" y1="418.9" x2="276.9" y2="447.6" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="420.2" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="280.7" y1="397.3" x2="280.7" y2="461.1" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="416.8" width="2.34" height="42.9" fill="var(--down)"/>
<line x1="284.4" y1="383.9" x2="284.4" y2="457.2" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="387.3" width="2.34" height="68.7" fill="var(--up)"/>
<line x1="288.2" y1="345.6" x2="288.2" y2="405.4" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="355.7" width="2.34" height="25.4" fill="var(--up)"/>
<line x1="292.0" y1="348.9" x2="292.0" y2="402.9" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="359.8" width="2.34" height="27.3" fill="var(--down)"/>
<line x1="295.7" y1="361.8" x2="295.7" y2="427.5" stroke="var(--down)" class="wick"/>
<rect x="294.57" y="386.8" width="2.34" height="37.6" fill="var(--down)"/>
<line x1="299.5" y1="384.6" x2="299.5" y2="442.0" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="390.0" width="2.34" height="30.3" fill="var(--up)"/>
<line x1="303.3" y1="373.5" x2="303.3" y2="392.6" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="380.9" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="307.1" y1="353.6" x2="307.1" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="358.8" width="2.34" height="25.9" fill="var(--up)"/>
<line x1="310.8" y1="357.4" x2="310.8" y2="380.2" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="366.4" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="314.6" y1="368.7" x2="314.6" y2="388.6" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="377.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="318.4" y1="363.2" x2="318.4" y2="382.7" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="372.3" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="322.1" y1="357.3" x2="322.1" y2="369.5" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="358.8" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="325.9" y1="356.1" x2="325.9" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="359.7" width="2.34" height="29.1" fill="var(--down)"/>
<line x1="329.7" y1="393.0" x2="329.7" y2="471.4" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="393.0" width="2.34" height="70.1" fill="var(--down)"/>
<line x1="333.5" y1="458.4" x2="333.5" y2="489.6" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="460.8" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="337.2" y1="448.6" x2="337.2" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="474.9" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="341.0" y1="471.8" x2="341.0" y2="495.1" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="483.5" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="344.8" y1="459.5" x2="344.8" y2="486.0" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="460.1" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="348.5" y1="451.3" x2="348.5" y2="469.4" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="451.7" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="352.3" y1="437.2" x2="352.3" y2="454.3" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="446.6" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="356.1" y1="447.4" x2="356.1" y2="465.8" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="451.7" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="359.9" y1="445.1" x2="359.9" y2="468.4" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="456.7" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="363.6" y1="461.4" x2="363.6" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="471.5" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="367.4" y1="469.6" x2="367.4" y2="488.8" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="470.8" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="371.2" y1="460.8" x2="371.2" y2="470.9" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="462.8" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="375.0" y1="444.8" x2="375.0" y2="461.6" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="452.0" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="378.7" y1="442.4" x2="378.7" y2="457.4" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="449.3" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="382.5" y1="435.9" x2="382.5" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="448.8" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="386.3" y1="449.3" x2="386.3" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="451.1" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="390.0" y1="457.4" x2="390.0" y2="495.6" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="462.5" width="2.34" height="18.8" fill="var(--down)"/>
<line x1="393.8" y1="476.1" x2="393.8" y2="498.1" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="479.4" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="397.6" y1="479.3" x2="397.6" y2="495.3" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="485.6" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="401.4" y1="481.8" x2="401.4" y2="503.2" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="487.1" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="405.1" y1="480.9" x2="405.1" y2="499.2" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="484.9" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="408.9" y1="465.3" x2="408.9" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="472.0" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="412.7" y1="466.3" x2="412.7" y2="483.3" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="467.0" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="416.4" y1="461.7" x2="416.4" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="466.2" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="420.2" y1="465.5" x2="420.2" y2="488.9" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="470.1" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="424.0" y1="464.1" x2="424.0" y2="476.4" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="473.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="427.8" y1="462.4" x2="427.8" y2="477.6" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="474.1" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="431.5" y1="464.1" x2="431.5" y2="491.4" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="473.1" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="435.3" y1="465.1" x2="435.3" y2="500.1" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="472.5" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="439.1" y1="476.7" x2="439.1" y2="492.6" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="476.7" width="2.34" height="14.8" fill="var(--down)"/>
<line x1="442.8" y1="490.5" x2="442.8" y2="502.5" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="492.3" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="446.6" y1="492.7" x2="446.6" y2="512.3" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="500.6" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="450.4" y1="489.7" x2="450.4" y2="503.9" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="502.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="454.2" y1="492.9" x2="454.2" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="495.1" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="457.9" y1="494.8" x2="457.9" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="495.9" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="461.7" y1="495.0" x2="461.7" y2="518.6" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="497.8" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="465.5" y1="484.9" x2="465.5" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="494.8" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="469.2" y1="485.7" x2="469.2" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="489.5" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="473.0" y1="482.6" x2="473.0" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="489.2" width="2.34" height="21.3" fill="var(--down)"/>
<line x1="476.8" y1="426.5" x2="476.8" y2="478.9" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="427.6" width="2.34" height="49.8" fill="var(--up)"/>
<line x1="480.6" y1="419.2" x2="480.6" y2="436.9" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="425.0" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="484.3" y1="425.3" x2="484.3" y2="453.9" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="432.4" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="488.1" y1="443.8" x2="488.1" y2="460.3" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="448.0" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="491.9" y1="447.1" x2="491.9" y2="468.4" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="449.3" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="495.7" y1="454.2" x2="495.7" y2="464.2" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="459.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="499.4" y1="448.0" x2="499.4" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="450.6" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="503.2" y1="439.4" x2="503.2" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="440.3" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="507.0" y1="435.6" x2="507.0" y2="446.4" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="442.0" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="510.7" y1="432.2" x2="510.7" y2="471.1" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="443.9" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="514.5" y1="455.8" x2="514.5" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="461.0" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="518.3" y1="453.8" x2="518.3" y2="461.9" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="454.8" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="522.1" y1="435.4" x2="522.1" y2="456.0" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="452.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="525.8" y1="438.3" x2="525.8" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="438.8" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="529.6" y1="436.5" x2="529.6" y2="454.4" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="438.3" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="533.4" y1="448.8" x2="533.4" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="453.2" width="2.34" height="39.0" fill="var(--down)"/>
<line x1="537.1" y1="477.7" x2="537.1" y2="495.7" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="481.5" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="540.9" y1="470.4" x2="540.9" y2="489.4" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="471.2" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="544.7" y1="470.3" x2="544.7" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="471.1" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="548.5" y1="463.0" x2="548.5" y2="475.4" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="463.5" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="552.2" y1="457.8" x2="552.2" y2="472.6" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="462.1" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="556.0" y1="459.2" x2="556.0" y2="473.4" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="465.5" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="559.8" y1="459.5" x2="559.8" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="462.7" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="563.5" y1="448.1" x2="563.5" y2="466.1" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="454.1" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="567.3" y1="439.2" x2="567.3" y2="455.1" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="441.8" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="571.1" y1="441.6" x2="571.1" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="442.1" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="574.9" y1="454.7" x2="574.9" y2="477.6" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="469.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="578.6" y1="459.2" x2="578.6" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="461.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="582.4" y1="427.0" x2="582.4" y2="462.3" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="439.6" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="586.2" y1="427.4" x2="586.2" y2="458.4" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="438.3" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="589.9" y1="444.7" x2="589.9" y2="455.9" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="446.6" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="593.7" y1="439.2" x2="593.7" y2="457.1" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="446.1" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="597.5" y1="445.9" x2="597.5" y2="458.9" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="450.2" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="601.3" y1="458.6" x2="601.3" y2="483.7" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="458.6" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="605.0" y1="473.1" x2="605.0" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="478.3" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="608.8" y1="487.4" x2="608.8" y2="516.2" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="489.7" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="612.6" y1="493.7" x2="612.6" y2="511.8" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="499.5" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="616.3" y1="492.0" x2="616.3" y2="505.7" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="494.7" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="620.1" y1="489.1" x2="620.1" y2="499.0" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="492.7" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="623.9" y1="492.6" x2="623.9" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="495.7" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="627.7" y1="482.4" x2="627.7" y2="500.8" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="492.2" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="631.4" y1="434.6" x2="631.4" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="439.8" width="2.34" height="52.9" fill="var(--up)"/>
<line x1="635.2" y1="409.2" x2="635.2" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="422.1" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="639.0" y1="406.9" x2="639.0" y2="439.3" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="418.5" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="642.8" y1="405.8" x2="642.8" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="407.1" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="646.5" y1="400.6" x2="646.5" y2="414.7" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="403.8" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="650.3" y1="386.1" x2="650.3" y2="405.4" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="386.6" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="654.1" y1="379.7" x2="654.1" y2="397.1" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="387.3" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="657.8" y1="381.9" x2="657.8" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="390.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="661.6" y1="381.3" x2="661.6" y2="399.0" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="384.2" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="665.4" y1="372.5" x2="665.4" y2="388.1" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="382.2" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="669.2" y1="346.5" x2="669.2" y2="388.2" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="369.8" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="672.9" y1="366.7" x2="672.9" y2="383.3" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="370.4" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="676.7" y1="370.6" x2="676.7" y2="387.9" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="377.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="680.5" y1="369.6" x2="680.5" y2="396.2" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="373.6" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="684.2" y1="391.5" x2="684.2" y2="413.1" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="391.5" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="688.0" y1="376.6" x2="688.0" y2="412.7" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="379.4" width="2.34" height="26.3" fill="var(--up)"/>
<line x1="691.8" y1="366.1" x2="691.8" y2="426.7" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="374.5" width="2.34" height="48.3" fill="var(--down)"/>
<line x1="695.6" y1="415.3" x2="695.6" y2="430.9" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="419.2" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="699.3" y1="422.8" x2="699.3" y2="442.1" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="423.4" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="703.1" y1="428.8" x2="703.1" y2="451.8" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="431.5" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="706.9" y1="432.4" x2="706.9" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="440.1" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="710.6" y1="431.6" x2="710.6" y2="461.4" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="441.6" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="714.4" y1="446.8" x2="714.4" y2="459.8" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="450.8" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="718.2" y1="445.0" x2="718.2" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="455.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="722.0" y1="457.2" x2="722.0" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="458.4" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="725.7" y1="435.9" x2="725.7" y2="466.5" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="437.2" width="2.34" height="29.4" fill="var(--up)"/>
<line x1="729.5" y1="405.8" x2="729.5" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="419.0" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="733.3" y1="406.2" x2="733.3" y2="452.9" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="412.4" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="737.0" y1="423.6" x2="737.0" y2="462.1" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="429.7" width="2.34" height="24.6" fill="var(--down)"/>
<line x1="740.8" y1="443.3" x2="740.8" y2="496.9" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="452.8" width="2.34" height="38.3" fill="var(--down)"/>
<line x1="744.6" y1="476.0" x2="744.6" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="479.8" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="748.4" y1="458.8" x2="748.4" y2="478.3" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="462.8" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="752.1" y1="426.4" x2="752.1" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="432.1" width="2.34" height="25.0" fill="var(--up)"/>
<line x1="755.9" y1="402.7" x2="755.9" y2="450.2" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="432.2" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="759.7" y1="418.2" x2="759.7" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="426.8" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="763.5" y1="392.2" x2="763.5" y2="428.9" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="400.2" width="2.34" height="26.3" fill="var(--up)"/>
<line x1="767.2" y1="384.4" x2="767.2" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="400.5" width="2.34" height="32.8" fill="var(--down)"/>
<line x1="771.0" y1="368.6" x2="771.0" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="373.2" width="2.34" height="66.7" fill="var(--up)"/>
<line x1="774.8" y1="359.9" x2="774.8" y2="383.5" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="365.3" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="778.5" y1="365.8" x2="778.5" y2="477.1" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="365.8" width="2.34" height="82.8" fill="var(--down)"/>
<line x1="782.3" y1="417.2" x2="782.3" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="426.0" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="786.1" y1="420.0" x2="786.1" y2="445.2" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="423.3" width="2.34" height="13.6" fill="var(--down)"/>
<line x1="789.9" y1="436.7" x2="789.9" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="440.2" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="793.6" y1="438.8" x2="793.6" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="444.9" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="797.4" y1="432.7" x2="797.4" y2="454.4" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="434.2" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="801.2" y1="420.4" x2="801.2" y2="441.5" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="428.5" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="804.9" y1="391.3" x2="804.9" y2="450.0" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="394.6" width="2.34" height="33.1" fill="var(--up)"/>
<line x1="808.7" y1="396.8" x2="808.7" y2="430.2" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="402.0" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="812.5" y1="405.0" x2="812.5" y2="438.5" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="414.3" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="816.3" y1="408.9" x2="816.3" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="410.1" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="820.0" y1="396.5" x2="820.0" y2="414.3" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="397.3" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="823.8" y1="380.3" x2="823.8" y2="398.8" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="391.8" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="827.6" y1="320.1" x2="827.6" y2="397.5" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="328.9" width="2.34" height="63.7" fill="var(--up)"/>
<line x1="831.3" y1="306.5" x2="831.3" y2="336.5" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="308.2" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="835.1" y1="298.0" x2="835.1" y2="317.3" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="309.2" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="838.9" y1="307.7" x2="838.9" y2="321.9" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="311.3" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="842.7" y1="290.2" x2="842.7" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="300.8" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="846.4" y1="296.6" x2="846.4" y2="315.1" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="301.3" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="850.2" y1="296.2" x2="850.2" y2="322.6" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="301.5" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="854.0" y1="309.1" x2="854.0" y2="328.6" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="321.2" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="857.7" y1="307.2" x2="857.7" y2="334.2" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="323.7" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="861.5" y1="297.7" x2="861.5" y2="328.3" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="298.2" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="865.3" y1="278.0" x2="865.3" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="279.6" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="869.1" y1="240.8" x2="869.1" y2="280.3" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="262.3" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="872.8" y1="257.5" x2="872.8" y2="301.7" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="266.7" width="2.34" height="31.6" fill="var(--down)"/>
<line x1="876.6" y1="279.3" x2="876.6" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="284.5" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="880.4" y1="284.4" x2="880.4" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="285.4" width="2.34" height="26.5" fill="var(--down)"/>
<line x1="884.2" y1="314.7" x2="884.2" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="315.7" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="887.9" y1="327.6" x2="887.9" y2="349.2" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="335.1" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="891.7" y1="324.5" x2="891.7" y2="345.6" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="332.7" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="895.5" y1="313.0" x2="895.5" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="325.8" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="899.2" y1="330.5" x2="899.2" y2="361.2" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="331.4" width="2.34" height="23.2" fill="var(--down)"/>
<line x1="903.0" y1="326.6" x2="903.0" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="328.9" width="2.34" height="25.7" fill="var(--up)"/>
<line x1="906.8" y1="321.4" x2="906.8" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="329.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="910.6" y1="307.2" x2="910.6" y2="330.0" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="319.5" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="914.3" y1="309.0" x2="914.3" y2="335.4" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="309.2" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="918.1" y1="243.3" x2="918.1" y2="323.0" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="268.1" width="2.34" height="30.8" fill="var(--up)"/>
<line x1="921.9" y1="205.1" x2="921.9" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="208.5" width="2.34" height="53.6" fill="var(--up)"/>
<line x1="925.6" y1="195.7" x2="925.6" y2="225.7" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="201.0" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="929.4" y1="160.8" x2="929.4" y2="246.8" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="177.1" width="2.34" height="27.6" fill="var(--up)"/>
<line x1="933.2" y1="152.8" x2="933.2" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="156.2" width="2.34" height="29.9" fill="var(--up)"/>
<line x1="937.0" y1="148.2" x2="937.0" y2="198.8" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="152.5" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="940.7" y1="111.1" x2="940.7" y2="169.1" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="138.3" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="944.5" y1="124.7" x2="944.5" y2="178.6" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="137.3" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="948.3" y1="75.8" x2="948.3" y2="124.9" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="98.0" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="952.0" y1="86.3" x2="952.0" y2="134.6" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="89.5" width="2.34" height="36.3" fill="var(--down)"/>
<line x1="955.8" y1="121.2" x2="955.8" y2="166.3" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="126.0" width="2.34" height="32.9" fill="var(--down)"/>
<line x1="959.6" y1="159.2" x2="959.6" y2="206.9" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="160.3" width="2.34" height="33.3" fill="var(--down)"/>
<line x1="963.4" y1="156.9" x2="963.4" y2="212.2" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="164.4" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="967.1" y1="163.7" x2="967.1" y2="210.9" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="166.3" width="2.34" height="33.8" fill="var(--down)"/>
<line x1="970.9" y1="187.5" x2="970.9" y2="213.3" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="195.1" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="974.7" y1="200.6" x2="974.7" y2="329.8" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="208.4" width="2.34" height="113.9" fill="var(--down)"/>
<line x1="978.4" y1="306.0" x2="978.4" y2="331.9" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="319.9" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="982.2" y1="319.3" x2="982.2" y2="360.5" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="331.9" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="986.0" y1="341.7" x2="986.0" y2="366.8" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="358.3" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="989.8" y1="343.9" x2="989.8" y2="367.0" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="346.5" width="2.34" height="19.3" fill="var(--up)"/>
<line x1="993.5" y1="336.1" x2="993.5" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="336.4" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="997.3" y1="341.1" x2="997.3" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="341.1" width="2.34" height="19.2" fill="var(--down)"/>
<line x1="1001.1" y1="341.4" x2="1001.1" y2="376.3" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="353.0" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="1004.9" y1="342.5" x2="1004.9" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="362.9" width="2.34" height="25.8" fill="var(--down)"/>
<line x1="1008.6" y1="391.0" x2="1008.6" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="396.0" width="2.34" height="19.3" fill="var(--down)"/>
<line x1="1012.4" y1="354.6" x2="1012.4" y2="423.0" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="354.6" width="2.34" height="58.3" fill="var(--up)"/>
<line x1="1016.2" y1="350.1" x2="1016.2" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="357.1" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="1019.9" y1="358.9" x2="1019.9" y2="394.1" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="365.1" width="2.34" height="23.5" fill="var(--down)"/>
<line x1="1023.7" y1="357.4" x2="1023.7" y2="441.3" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="363.0" width="2.34" height="23.2" fill="var(--up)"/>
<line x1="1027.5" y1="334.3" x2="1027.5" y2="390.9" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="362.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1031.3" y1="325.2" x2="1031.3" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="326.7" width="2.34" height="31.7" fill="var(--up)"/>
<line x1="1035.0" y1="308.3" x2="1035.0" y2="329.2" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="308.9" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="1038.8" y1="298.2" x2="1038.8" y2="353.2" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="313.9" width="2.34" height="38.2" fill="var(--down)"/>
<line x1="1042.6" y1="348.9" x2="1042.6" y2="365.7" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="349.7" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="1046.3" y1="353.7" x2="1046.3" y2="386.0" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="366.2" width="2.34" height="19.6" fill="var(--down)"/>
<line x1="1050.1" y1="372.3" x2="1050.1" y2="388.5" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="379.2" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="60" y1="354.8" x2="1052" y2="354.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="358.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$549 R1</text>
<text x="1058" y="370.3" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="479.3" x2="1052" y2="479.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="473.3" font-size="11.5" fill="var(--support)" font-weight="600">$448 S1</text>
<text x="1058" y="485.3" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="505.2" x2="1052" y2="505.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="499.2" font-size="11.5" fill="var(--support)" font-weight="600">$427 S2</text>
<text x="1058" y="511.2" font-size="9.5" fill="var(--muted)">터치 9회</text>
<circle cx="1052.0" cy="380.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="372.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $528 (2026-09-03)</text>
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
| R1 | $549 | 5 | 2022-10-24·2023-01-02·2024-09-30·2024-11-11·2025-04-14 — 2022~2025년 내내 반복해서 막힌 다년 상단대 |
| **현재가** | **$528.24** (2026-09-03 종가) | — | R1과 S1 사이 |
| S1 | $448 | 5 | 2023-03-13·2023-12-11·2024-04-15·2025-01-06·2025-04-21 — 2023~2025년 조정 때마다 받쳐준 1차 지지대 |
| S2 | $427 | 9 | 2022-05-02·2022-06-13·2022-07-25·2023-01-23·2023-05-22·2023-10-02·2024-01-22·2024-06-10·2025-02-17 — 5년 중 터치 9회로 가장 두꺼운 지지대 |
| 참고선 | $774 | — | 2026년 최고(2026-03-02 전후 장중 $774.00). 5년 통틀어 단 한 번의 스윙이라 클러스터가 형성되지 않았고, 근시일 저항으로 보지 않는다 |

5년 구조에서 눈에 띄는 것은 **레벨이 전부 현재가 아래이거나 바로 위에 몰려 있다**는 점이다. R1($549)은 2022년부터 2025년까지 네 번 막힌 다년 상단인데, 2026년 상반기에 이 대역을 크게 뚫고 $774까지 올라갔다가 다시 아래로 돌아왔다. **즉 지금 주가는 4년간의 박스 상단을 한 번 이탈했다가 되돌아온 자리**이며, R1이 다시 저항이 될지 지지로 바뀔지는 이 차트만으로 판단할 수 없다.

---

## 3. 관측된 특이 구간 — 2026년 상반기 레짐 전환

- 2026년 1~3월에 주가가 2025년 말 $570.21에서 **$768.02(2026-03-02 종가, 장중 $774.00)**까지 올랐다. 5년 통틀어 R1($549) 대역을 이만큼 크게 넘어선 구간은 이때뿐이다.
- 이후 4~6월에 걸쳐 **$496.02(2026-06-29 종가)**까지 −35% 되돌렸다. 되돌림의 계기는 4월 실적 발표 후 −6.98% 갭과 6월의 섹터 동반 하락이며, 둘 다 [기술적 분석 — 일봉](./09_technical_daily.md) 3절에 정리돼 있다.
- **이 왕복 때문에 $549~$774 구간에는 주봉 스윙이 거의 쌓이지 않았다** — 빠르게 올라갔다 빠르게 내려온 구간이라 클러스터가 형성되지 않았고, 그래서 R1 위쪽에 저항 레벨이 하나도 잡히지 않는다. 위가 비어 있다는 뜻이 아니라 **표본이 없다**는 뜻으로 읽어야 한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-30~2026-09-03. 수집 시점: 2026-09-04. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py NOC --name "노스롭 그루먼" --interval 1wk --close-on 2026-09-03 --ref-line 774:"2026년 최고" --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 위 3절대로 **$549 위쪽 구간은 스윙 표본이 없어 저항 레벨이 산출되지 않았다.** 유효 클러스터가 3개(R1·S1·S2)뿐인 이유이며, 레벨 개수를 억지로 채우지 않았다.
    - 기간 중 주식분할·유상증자는 없었다. 분기배당은 원주가 기준이라 반영하지 않았다.

---

*작성일: 2026-09-04*
