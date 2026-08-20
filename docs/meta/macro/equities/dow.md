# 다우존스산업지수

!!! note ""
    최근 5년 다우존스산업지수(우량주 30종목, `^DJI`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 시가총액 가중이 아니라 **주가 가중** 방식이라 S&P 500·나스닥종합지수와 계산 방식 자체가 다르다 — 종목 수가 적고(30개) 전통 산업재·금융 비중이 커서, 성장주 중심의 나스닥과는 다른 흐름을 보일 때가 있다.

---

## 1. 차트 — 최근 5년 주봉

<div class="dji-chart">
<style>
.dji-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dji-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .dji-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.dji-chart svg { width:100%; height:auto; display:block; }
.dji-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.dji-chart .title { fill: var(--ink); font-weight:600; }
.dji-chart .grid { stroke: var(--grid); stroke-width:1; }
.dji-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="다우존스산업지수(^DJI) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">다우존스산업지수 (^DJI) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-19 · 마지막 종가 53,463.05 (2026-08-19) · 단위 지수</text>
<line x1="60" y1="576.0" x2="1052" y2="576.0" class="grid"/>
<text x="52" y="580.0" font-size="11" text-anchor="end" fill="var(--muted)">30,000</text>
<line x1="60" y1="476.0" x2="1052" y2="476.0" class="grid"/>
<text x="52" y="480.0" font-size="11" text-anchor="end" fill="var(--muted)">35,000</text>
<line x1="60" y1="376.0" x2="1052" y2="376.0" class="grid"/>
<text x="52" y="380.0" font-size="11" text-anchor="end" fill="var(--muted)">40,000</text>
<line x1="60" y1="276.0" x2="1052" y2="276.0" class="grid"/>
<text x="52" y="280.0" font-size="11" text-anchor="end" fill="var(--muted)">45,000</text>
<line x1="60" y1="176.0" x2="1052" y2="176.0" class="grid"/>
<text x="52" y="180.0" font-size="11" text-anchor="end" fill="var(--muted)">50,000</text>
<line x1="60" y1="76.0" x2="1052" y2="76.0" class="grid"/>
<text x="52" y="80.0" font-size="11" text-anchor="end" fill="var(--muted)">55,000</text>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.3" y1="626.0" x2="137.3" y2="631.0" class="axis"/>
<text x="137.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="333.5" y1="626.0" x2="333.5" y2="631.0" class="axis"/>
<text x="333.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="529.6" y1="626.0" x2="529.6" y2="631.0" class="axis"/>
<text x="529.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="729.5" y1="626.0" x2="729.5" y2="631.0" class="axis"/>
<text x="729.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.6" y1="626.0" x2="925.6" y2="631.0" class="axis"/>
<text x="925.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="472.5" x2="61.9" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="473.6" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="65.7" y1="466.0" x2="65.7" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="466.9" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="69.4" y1="465.8" x2="69.4" y2="470.6" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="466.6" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="73.2" y1="468.5" x2="73.2" y2="484.0" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="468.5" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="77.0" y1="476.2" x2="77.0" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="482.7" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="80.7" y1="478.4" x2="80.7" y2="503.7" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="480.0" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="84.5" y1="474.8" x2="84.5" y2="500.3" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="481.2" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="88.3" y1="476.5" x2="88.3" y2="499.6" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="481.1" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="92.1" y1="469.6" x2="92.1" y2="493.7" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="470.1" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="95.8" y1="460.7" x2="95.8" y2="475.3" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="462.5" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="99.6" y1="458.1" x2="99.6" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="459.6" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="103.4" y1="446.3" x2="103.4" y2="460.0" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="449.4" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="107.1" y1="444.7" x2="107.1" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="447.7" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="110.9" y1="449.7" x2="110.9" y2="464.9" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="453.4" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="114.7" y1="457.4" x2="114.7" y2="481.0" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="463.4" width="2.34" height="14.6" fill="var(--down)"/>
<line x1="118.5" y1="470.2" x2="118.5" y2="495.9" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="475.6" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="122.2" y1="456.3" x2="122.2" y2="483.3" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="456.6" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="126.0" y1="452.2" x2="126.0" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="456.8" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="129.8" y1="454.8" x2="129.8" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="457.0" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="133.6" y1="442.4" x2="133.6" y2="456.9" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="449.2" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="137.3" y1="436.9" x2="137.3" y2="453.8" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="449.6" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="141.1" y1="445.7" x2="141.1" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="452.5" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="144.9" y1="462.8" x2="144.9" y2="491.4" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="462.8" width="2.34" height="27.9" fill="var(--down)"/>
<line x1="148.6" y1="479.7" x2="148.6" y2="513.0" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="481.5" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="152.4" y1="462.4" x2="152.4" y2="486.1" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="474.2" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="156.2" y1="459.5" x2="156.2" y2="483.6" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="473.8" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="160.0" y1="475.0" x2="160.0" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="482.1" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="163.7" y1="494.1" x2="163.7" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="494.8" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="167.5" y1="492.4" x2="167.5" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="498.6" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="171.3" y1="504.4" x2="171.3" y2="524.4" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="504.4" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="175.0" y1="480.9" x2="175.0" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="480.9" width="2.34" height="35.1" fill="var(--up)"/>
<line x1="178.8" y1="477.1" x2="178.8" y2="489.2" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="478.8" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="182.6" y1="468.6" x2="182.6" y2="485.2" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="479.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="186.4" y1="473.8" x2="186.4" y2="492.2" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="480.0" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="190.1" y1="478.2" x2="190.1" y2="493.9" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="483.4" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="193.9" y1="466.2" x2="193.9" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="487.8" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="197.7" y1="493.9" x2="197.7" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="501.4" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="201.4" y1="493.6" x2="201.4" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="516.4" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="205.2" y1="521.0" x2="205.2" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="522.3" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="209.0" y1="522.2" x2="209.0" y2="563.3" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="533.0" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="212.8" y1="511.7" x2="212.8" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="511.7" width="2.34" height="36.3" fill="var(--up)"/>
<line x1="216.5" y1="510.6" x2="216.5" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="512.8" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="220.3" y1="511.3" x2="220.3" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="515.4" width="2.34" height="32.8" fill="var(--down)"/>
<line x1="224.1" y1="553.1" x2="224.1" y2="582.9" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="553.1" width="2.34" height="25.1" fill="var(--down)"/>
<line x1="227.8" y1="545.7" x2="227.8" y2="574.5" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="546.0" width="2.34" height="28.5" fill="var(--up)"/>
<line x1="231.6" y1="538.3" x2="231.6" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="545.3" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="235.4" y1="545.8" x2="235.4" y2="568.9" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="549.2" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="239.2" y1="548.6" x2="239.2" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="550.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="242.9" y1="531.6" x2="242.9" y2="556.3" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="538.0" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="246.7" y1="517.8" x2="246.7" y2="541.9" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="519.1" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="250.5" y1="516.6" x2="250.5" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="519.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="254.3" y1="500.7" x2="254.3" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="500.8" width="2.34" height="17.7" fill="var(--up)"/>
<line x1="258.0" y1="490.4" x2="258.0" y2="504.3" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="501.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="261.8" y1="504.3" x2="261.8" y2="530.4" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="504.3" width="2.34" height="26.1" fill="var(--down)"/>
<line x1="265.6" y1="529.5" x2="265.6" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="532.2" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="269.3" y1="531.4" x2="269.3" y2="555.0" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="533.0" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="273.1" y1="525.9" x2="273.1" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="532.8" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="276.9" y1="555.5" x2="276.9" y2="591.0" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="561.5" width="2.34" height="22.6" fill="var(--down)"/>
<line x1="280.7" y1="579.8" x2="280.7" y2="601.7" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="585.3" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="284.4" y1="566.9" x2="284.4" y2="598.9" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="590.1" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="288.2" y1="567.4" x2="288.2" y2="602.8" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="583.3" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="292.0" y1="553.6" x2="292.0" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="554.3" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="295.7" y1="518.2" x2="295.7" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="518.8" width="2.34" height="33.5" fill="var(--up)"/>
<line x1="299.5" y1="514.6" x2="299.5" y2="541.5" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="520.9" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="303.3" y1="499.6" x2="303.3" y2="527.5" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="501.0" width="2.34" height="25.9" fill="var(--up)"/>
<line x1="307.1" y1="496.3" x2="307.1" y2="511.2" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="501.1" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="310.8" y1="488.3" x2="310.8" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="489.1" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="314.6" y1="484.1" x2="314.6" y2="504.3" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="487.4" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="318.4" y1="489.3" x2="318.4" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="489.3" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="322.1" y1="481.8" x2="322.1" y2="522.9" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="505.6" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="325.9" y1="507.2" x2="325.9" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="511.9" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="329.7" y1="508.2" x2="329.7" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="511.5" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="333.5" y1="501.8" x2="333.5" y2="519.8" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="503.4" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="337.2" y1="489.2" x2="337.2" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="489.9" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="341.0" y1="490.6" x2="341.0" y2="517.0" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="491.6" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="344.8" y1="492.7" x2="344.8" y2="510.5" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="496.4" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="348.5" y1="489.3" x2="348.5" y2="504.4" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="497.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="352.3" y1="490.9" x2="352.3" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="498.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="356.1" y1="489.4" x2="356.1" y2="505.6" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="498.3" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="359.9" y1="502.0" x2="359.9" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="502.0" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="363.6" y1="507.9" x2="363.6" y2="526.0" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="508.2" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="367.4" y1="504.6" x2="367.4" y2="540.3" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="507.5" width="2.34" height="30.3" fill="var(--down)"/>
<line x1="371.2" y1="529.9" x2="371.2" y2="547.4" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="538.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="375.0" y1="520.8" x2="375.0" y2="539.9" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="531.2" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="378.7" y1="510.2" x2="378.7" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="510.5" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="382.5" y1="503.3" x2="382.5" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="506.3" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="386.3" y1="494.3" x2="386.3" y2="509.1" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="498.3" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="390.0" y1="495.6" x2="390.0" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="497.4" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="393.8" y1="493.9" x2="393.8" y2="511.3" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="494.0" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="397.6" y1="490.8" x2="397.6" y2="517.2" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="493.7" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="401.4" y1="500.6" x2="401.4" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="501.7" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="405.1" y1="502.9" x2="405.1" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="507.5" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="408.9" y1="505.8" x2="408.9" y2="524.3" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="507.8" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="412.7" y1="499.9" x2="412.7" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="500.7" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="416.4" y1="496.5" x2="416.4" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="498.5" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="420.2" y1="484.2" x2="420.2" y2="500.3" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="490.0" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="424.0" y1="491.9" x2="424.0" y2="503.1" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="491.9" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="427.8" y1="486.7" x2="427.8" y2="503.8" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="487.8" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="431.5" y1="486.7" x2="431.5" y2="501.7" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="488.6" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="435.3" y1="484.2" x2="435.3" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="485.8" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="439.1" y1="468.5" x2="439.1" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="471.4" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="442.8" y1="463.1" x2="442.8" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="466.8" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="446.6" y1="462.4" x2="446.6" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="466.7" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="450.4" y1="464.4" x2="450.4" y2="475.9" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="470.4" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="454.2" y1="469.3" x2="454.2" y2="490.7" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="470.5" width="2.34" height="15.5" fill="var(--down)"/>
<line x1="457.9" y1="482.1" x2="457.9" y2="495.4" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="485.4" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="461.7" y1="474.6" x2="461.7" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="479.2" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="465.5" y1="478.6" x2="465.5" y2="490.2" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="479.1" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="469.2" y1="476.4" x2="469.2" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="483.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="473.0" y1="480.5" x2="473.0" y2="497.1" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="483.8" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="476.8" y1="495.6" x2="476.8" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="497.8" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="480.6" y1="504.8" x2="480.6" y2="519.1" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="506.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="484.3" y1="496.8" x2="484.3" y2="510.9" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="502.6" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="488.1" y1="493.0" x2="488.1" y2="513.6" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="499.4" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="491.9" y1="510.6" x2="491.9" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="516.1" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="495.7" y1="492.7" x2="495.7" y2="525.2" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="494.8" width="2.34" height="30.5" fill="var(--up)"/>
<line x1="499.4" y1="489.8" x2="499.4" y2="498.8" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="490.3" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="503.2" y1="475.0" x2="503.2" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="477.1" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="507.0" y1="468.0" x2="507.0" y2="477.8" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="468.2" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="510.7" y1="450.7" x2="510.7" y2="470.4" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="451.1" width="2.34" height="17.4" fill="var(--up)"/>
<line x1="514.5" y1="450.1" x2="514.5" y2="455.8" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="451.0" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="518.3" y1="429.0" x2="518.3" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="429.9" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="522.1" y1="423.2" x2="522.1" y2="434.5" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="428.3" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="525.8" y1="420.4" x2="525.8" y2="428.6" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="422.2" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="529.6" y1="420.2" x2="529.6" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="424.7" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="533.4" y1="419.5" x2="533.4" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="424.1" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="537.1" y1="417.3" x2="537.1" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="418.7" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="540.9" y1="411.7" x2="540.9" y2="420.1" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="413.8" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="544.7" y1="400.3" x2="544.7" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="402.9" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="548.5" y1="400.9" x2="548.5" y2="411.6" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="402.6" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="552.2" y1="397.5" x2="552.2" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="402.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="556.0" y1="390.4" x2="556.0" y2="409.2" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="393.4" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="559.8" y1="391.1" x2="559.8" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="393.1" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="563.5" y1="394.2" x2="563.5" y2="406.8" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="396.6" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="567.3" y1="392.0" x2="567.3" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="401.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="571.1" y1="378.2" x2="571.1" y2="400.8" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="386.5" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="574.9" y1="378.6" x2="574.9" y2="390.5" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="379.9" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="578.6" y1="379.7" x2="578.6" y2="404.8" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="379.8" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="582.4" y1="395.7" x2="582.4" y2="418.5" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="397.7" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="586.2" y1="408.3" x2="586.2" y2="423.8" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="414.5" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="589.9" y1="404.8" x2="589.9" y2="420.9" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="411.2" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="593.7" y1="399.8" x2="593.7" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="402.5" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="597.5" y1="384.4" x2="597.5" y2="402.2" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="385.7" width="2.34" height="15.0" fill="var(--up)"/>
<line x1="601.3" y1="375.0" x2="601.3" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="375.9" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="605.0" y1="374.5" x2="605.0" y2="395.6" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="376.2" width="2.34" height="18.4" fill="var(--down)"/>
<line x1="608.8" y1="395.4" x2="608.8" y2="416.0" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="395.4" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="612.6" y1="393.9" x2="612.6" y2="411.1" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="400.0" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="616.3" y1="393.6" x2="616.3" y2="409.9" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="400.3" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="620.1" y1="390.9" x2="620.1" y2="407.4" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="393.0" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="623.9" y1="384.6" x2="623.9" y2="397.8" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="392.3" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="627.7" y1="387.2" x2="627.7" y2="395.2" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="388.5" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="631.4" y1="370.9" x2="631.4" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="376.0" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="635.2" y1="348.5" x2="635.2" y2="373.3" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="370.2" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="639.0" y1="360.9" x2="639.0" y2="379.9" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="364.2" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="642.8" y1="352.0" x2="642.8" y2="388.8" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="362.7" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="646.5" y1="383.4" x2="646.5" y2="406.0" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="386.0" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="650.3" y1="361.5" x2="650.3" y2="391.0" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="362.8" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="654.1" y1="351.8" x2="654.1" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="352.5" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="657.8" y1="344.3" x2="657.8" y2="359.2" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="344.7" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="661.6" y1="346.2" x2="661.6" y2="370.1" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="346.2" width="2.34" height="22.9" fill="var(--down)"/>
<line x1="665.4" y1="345.3" x2="665.4" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="348.1" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="669.2" y1="332.8" x2="669.2" y2="347.3" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="334.7" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="672.9" y1="323.4" x2="672.9" y2="338.8" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="329.7" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="676.7" y1="328.8" x2="676.7" y2="339.0" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="328.9" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="680.5" y1="318.0" x2="680.5" y2="339.4" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="318.7" width="2.34" height="11.5" fill="var(--up)"/>
<line x1="684.2" y1="309.5" x2="684.2" y2="322.2" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="310.5" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="688.0" y1="309.8" x2="688.0" y2="335.0" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="311.6" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="691.8" y1="326.2" x2="691.8" y2="341.9" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="330.7" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="695.6" y1="292.9" x2="695.6" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="296.2" width="2.34" height="39.7" fill="var(--up)"/>
<line x1="699.3" y1="286.3" x2="699.3" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="294.8" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="703.1" y1="289.5" x2="703.1" y2="317.2" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="290.1" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="706.9" y1="274.6" x2="706.9" y2="288.3" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="277.8" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="710.6" y1="274.5" x2="710.6" y2="284.5" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="277.5" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="714.4" y1="281.4" x2="714.4" y2="300.2" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="283.2" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="718.2" y1="297.0" x2="718.2" y2="333.1" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="299.5" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="722.0" y1="308.5" x2="722.0" y2="325.7" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="316.2" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="725.7" y1="317.9" x2="725.7" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="318.7" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="729.5" y1="313.7" x2="729.5" y2="338.5" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="319.3" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="733.3" y1="302.9" x2="733.3" y2="339.1" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="306.2" width="2.34" height="31.3" fill="var(--up)"/>
<line x1="737.0" y1="284.7" x2="737.0" y2="305.4" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="287.5" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="740.8" y1="274.9" x2="740.8" y2="295.5" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="285.1" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="744.6" y1="276.7" x2="744.6" y2="298.4" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="289.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="748.4" y1="280.6" x2="748.4" y2="293.9" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="285.1" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="752.1" y1="283.3" x2="752.1" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="284.3" width="2.34" height="23.1" fill="var(--down)"/>
<line x1="755.9" y1="298.3" x2="755.9" y2="314.0" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="299.2" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="759.7" y1="295.3" x2="759.7" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="298.0" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="763.5" y1="325.2" x2="763.5" y2="362.8" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="325.8" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="767.2" y1="331.0" x2="767.2" y2="347.7" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="336.3" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="771.0" y1="319.6" x2="771.0" y2="345.4" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="332.4" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="774.8" y1="328.4" x2="774.8" y2="410.7" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="348.3" width="2.34" height="61.4" fill="var(--down)"/>
<line x1="778.5" y1="360.4" x2="778.5" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="371.7" width="2.34" height="46.7" fill="var(--up)"/>
<line x1="782.3" y1="360.2" x2="782.3" y2="397.0" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="365.1" width="2.34" height="28.1" fill="var(--down)"/>
<line x1="786.1" y1="368.5" x2="786.1" y2="419.4" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="373.7" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="789.9" y1="348.3" x2="789.9" y2="381.1" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="349.7" width="2.34" height="22.9" fill="var(--up)"/>
<line x1="793.6" y1="340.5" x2="793.6" y2="360.8" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="351.0" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="797.4" y1="322.7" x2="797.4" y2="340.4" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="322.9" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="801.2" y1="319.2" x2="801.2" y2="348.9" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="325.1" width="2.34" height="18.8" fill="var(--down)"/>
<line x1="804.9" y1="327.0" x2="804.9" y2="339.4" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="330.6" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="808.7" y1="317.5" x2="808.7" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="320.7" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="812.5" y1="313.7" x2="812.5" y2="334.4" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="320.3" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="816.3" y1="321.8" x2="816.3" y2="334.2" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="330.0" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="820.0" y1="296.7" x2="820.0" y2="336.4" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="299.6" width="2.34" height="32.8" fill="var(--up)"/>
<line x1="823.8" y1="278.3" x2="823.8" y2="298.2" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="279.4" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="827.6" y1="279.9" x2="827.6" y2="292.8" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="279.9" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="831.3" y1="284.6" x2="831.3" y2="300.8" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="289.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="835.1" y1="275.7" x2="835.1" y2="290.5" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="278.0" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="838.9" y1="277.1" x2="838.9" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="277.1" width="2.34" height="27.2" fill="var(--down)"/>
<line x1="842.7" y1="286.0" x2="842.7" y2="301.5" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="292.5" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="846.4" y1="271.9" x2="846.4" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="277.1" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="850.2" y1="260.8" x2="850.2" y2="284.4" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="263.4" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="854.0" y1="262.3" x2="854.0" y2="272.2" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="263.9" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="857.7" y1="260.6" x2="857.7" y2="277.0" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="268.0" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="861.5" y1="253.3" x2="861.5" y2="270.4" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="259.3" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="865.3" y1="248.1" x2="865.3" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="249.7" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="869.1" y1="241.7" x2="869.1" y2="260.3" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="251.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="872.8" y1="235.0" x2="872.8" y2="253.9" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="240.8" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="876.6" y1="238.6" x2="876.6" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="240.5" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="880.4" y1="242.1" x2="880.4" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="252.2" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="884.2" y1="229.5" x2="884.2" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="231.9" width="2.34" height="17.9" fill="var(--up)"/>
<line x1="887.9" y1="215.2" x2="887.9" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="224.7" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="891.7" y1="222.1" x2="891.7" y2="246.1" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="222.1" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="895.5" y1="207.4" x2="895.5" y2="238.7" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="233.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="899.2" y1="231.9" x2="899.2" y2="261.4" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="234.6" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="903.0" y1="221.0" x2="903.0" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="221.7" width="2.34" height="27.3" fill="var(--up)"/>
<line x1="906.8" y1="213.3" x2="906.8" y2="230.7" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="216.9" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="910.6" y1="198.3" x2="910.6" y2="226.7" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="206.8" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="914.3" y1="202.4" x2="914.3" y2="219.0" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="204.1" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="918.1" y1="200.4" x2="918.1" y2="212.0" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="201.8" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="921.9" y1="201.9" x2="921.9" y2="218.9" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="203.3" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="925.6" y1="183.6" x2="925.6" y2="207.0" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="185.9" width="2.34" height="20.6" fill="var(--up)"/>
<line x1="929.4" y1="183.3" x2="929.4" y2="199.0" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="186.0" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="933.2" y1="183.9" x2="933.2" y2="207.4" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="194.0" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="937.0" y1="186.2" x2="937.0" y2="206.8" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="193.2" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="940.7" y1="172.6" x2="940.7" y2="202.5" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="173.7" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="944.5" y1="165.7" x2="944.5" y2="194.3" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="175.0" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="948.3" y1="178.1" x2="948.3" y2="192.8" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="183.5" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="952.0" y1="179.7" x2="952.0" y2="202.4" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="185.3" width="2.34" height="11.2" fill="var(--down)"/>
<line x1="955.8" y1="194.7" x2="955.8" y2="235.8" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="200.1" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="959.6" y1="211.6" x2="959.6" y2="246.1" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="228.6" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="963.4" y1="227.4" x2="963.4" y2="268.6" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="241.9" width="2.34" height="22.6" fill="var(--down)"/>
<line x1="967.1" y1="241.6" x2="967.1" y2="274.7" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="259.9" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="970.9" y1="239.9" x2="970.9" y2="274.9" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="245.9" width="2.34" height="24.4" fill="var(--up)"/>
<line x1="974.7" y1="209.5" x2="974.7" y2="251.7" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="217.7" width="2.34" height="28.9" fill="var(--up)"/>
<line x1="978.4" y1="181.6" x2="978.4" y2="225.9" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="187.1" width="2.34" height="34.6" fill="var(--up)"/>
<line x1="982.2" y1="179.0" x2="982.2" y2="198.8" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="187.6" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="986.0" y1="176.2" x2="986.0" y2="201.8" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="186.0" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="989.8" y1="173.4" x2="989.8" y2="197.7" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="183.8" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="993.5" y1="172.0" x2="993.5" y2="189.8" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="185.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="997.3" y1="159.4" x2="997.3" y2="191.3" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="164.4" width="2.34" height="22.0" fill="var(--up)"/>
<line x1="1001.1" y1="154.1" x2="1001.1" y2="169.7" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="155.4" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="1004.9" y1="142.8" x2="1004.9" y2="162.3" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="152.8" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="1008.6" y1="147.8" x2="1008.6" y2="177.8" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="152.0" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="1012.4" y1="130.4" x2="1012.4" y2="148.7" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="144.7" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="1016.2" y1="122.9" x2="1016.2" y2="150.0" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="138.5" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="1019.9" y1="117.9" x2="1019.9" y2="137.0" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="118.0" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="1023.7" y1="110.2" x2="1023.7" y2="134.6" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="119.4" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="1027.5" y1="117.5" x2="1027.5" y2="136.3" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="122.5" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="1031.3" y1="125.8" x2="1031.3" y2="145.2" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="132.9" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="1035.0" y1="118.0" x2="1035.0" y2="145.0" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="126.3" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="1038.8" y1="81.1" x2="1038.8" y2="120.8" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="95.3" width="2.34" height="25.6" fill="var(--up)"/>
<line x1="1042.6" y1="91.5" x2="1042.6" y2="103.6" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="94.5" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="1046.3" y1="101.8" x2="1046.3" y2="110.9" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="102.7" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="1050.1" y1="101.8" x2="1050.1" y2="108.0" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="106.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="60" y1="267.7" x2="1052" y2="267.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="261.7" font-size="11.5" fill="var(--support)" font-weight="600">45,413 S1</text>
<text x="1058" y="273.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="341.1" x2="1052" y2="341.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="335.1" font-size="11.5" fill="var(--support)" font-weight="600">41,746 S2</text>
<text x="1058" y="347.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="414.9" x2="1052" y2="414.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="408.9" font-size="11.5" fill="var(--support)" font-weight="600">38,055 S3</text>
<text x="1058" y="420.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="106.7" r="3" fill="var(--ink)"/>
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

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **상승**: 대형 우량주 중심의 미국 경기 심리 개선, 위험선호 확대 신호로 흔히 해석된다.
- **하락**: 경기 둔화 우려 또는 위험회피 심리 확대 신호로 흔히 해석된다.
- **주가 가중 지수**라 시가총액과 무관하게 주가 자체가 높은 종목의 움직임이 과대 반영된다 — 시가총액 가중 지수인 S&P 500·나스닥종합지수와 같은 비중으로 해석하지 않는다.

---

## 관련 문서

- [S&P 500](./sp500.md) · [나스닥종합지수](./nasdaq.md) — 시가총액 가중 비교군
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Dow Jones Industrial Average (^DJI)](https://finance.yahoo.com/quote/%5EDJI/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
