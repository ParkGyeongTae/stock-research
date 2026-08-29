# 다우존스산업지수

!!! note ""
    최근 5년간 다우존스산업지수(미국 우량주 30종목, `^DJI`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 이 지수는 회사 규모(시가총액)가 아니라 **주가 자체**를 기준으로 비중을 매기는 방식이라, 시가총액 기준인 S&P 500·나스닥종합지수와 계산 방법 자체가 다르다. 담긴 종목이 30개로 적고 전통 산업재·금융 회사 비중이 커서, 성장주 중심인 나스닥과 다르게 움직일 때가 있다.

---

## 1. 차트 — 최근 5년 주봉

<div class="dji-chart">
<style>
.dji-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .dji-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 53,559.99 (2026-08-28) · 단위 지수</text>
<line x1="60" y1="576.0" x2="1052" y2="576.0" class="grid"/>
<text x="52" y="580.0" font-size="11" text-anchor="end" fill="var(--muted)">30,000.00</text>
<line x1="60" y1="476.0" x2="1052" y2="476.0" class="grid"/>
<text x="52" y="480.0" font-size="11" text-anchor="end" fill="var(--muted)">35,000.00</text>
<line x1="60" y1="376.0" x2="1052" y2="376.0" class="grid"/>
<text x="52" y="380.0" font-size="11" text-anchor="end" fill="var(--muted)">40,000.00</text>
<line x1="60" y1="276.0" x2="1052" y2="276.0" class="grid"/>
<text x="52" y="280.0" font-size="11" text-anchor="end" fill="var(--muted)">45,000.00</text>
<line x1="60" y1="176.0" x2="1052" y2="176.0" class="grid"/>
<text x="52" y="180.0" font-size="11" text-anchor="end" fill="var(--muted)">50,000.00</text>
<line x1="60" y1="76.0" x2="1052" y2="76.0" class="grid"/>
<text x="52" y="80.0" font-size="11" text-anchor="end" fill="var(--muted)">55,000.00</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="130.0" y1="56.0" x2="130.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="130.0" y1="626.0" x2="130.0" y2="631.0" class="axis"/>
<text x="130.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="326.9" y1="56.0" x2="326.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="326.9" y1="626.0" x2="326.9" y2="631.0" class="axis"/>
<text x="326.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="523.8" y1="56.0" x2="523.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="523.8" y1="626.0" x2="523.8" y2="631.0" class="axis"/>
<text x="523.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="724.5" y1="56.0" x2="724.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="724.5" y1="626.0" x2="724.5" y2="631.0" class="axis"/>
<text x="724.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.4" y1="56.0" x2="921.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.4" y1="626.0" x2="921.4" y2="631.0" class="axis"/>
<text x="921.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="465.8" x2="61.9" y2="470.6" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="466.6" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="65.7" y1="468.5" x2="65.7" y2="484.0" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="468.5" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="69.5" y1="476.2" x2="69.5" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="482.7" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="73.3" y1="478.4" x2="73.3" y2="503.7" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="480.0" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="77.0" y1="474.8" x2="77.0" y2="500.3" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="481.2" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="80.8" y1="476.5" x2="80.8" y2="499.6" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="481.1" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="84.6" y1="469.6" x2="84.6" y2="493.7" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="470.1" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="88.4" y1="460.7" x2="88.4" y2="475.3" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="462.5" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="92.2" y1="458.1" x2="92.2" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="459.6" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="96.0" y1="446.3" x2="96.0" y2="460.0" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="449.4" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="99.8" y1="444.7" x2="99.8" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="447.7" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="103.5" y1="449.7" x2="103.5" y2="464.9" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="453.4" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="107.3" y1="457.4" x2="107.3" y2="481.0" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="463.4" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="111.1" y1="470.2" x2="111.1" y2="495.9" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="475.6" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="114.9" y1="456.3" x2="114.9" y2="483.3" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="456.6" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="118.7" y1="452.2" x2="118.7" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="456.8" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="122.5" y1="454.8" x2="122.5" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="457.0" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="126.3" y1="442.4" x2="126.3" y2="456.9" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="449.2" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="130.0" y1="436.9" x2="130.0" y2="453.8" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="449.6" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="133.8" y1="445.7" x2="133.8" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="452.5" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="137.6" y1="462.8" x2="137.6" y2="491.4" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="462.8" width="2.35" height="27.9" fill="var(--down)"/>
<line x1="141.4" y1="479.7" x2="141.4" y2="513.0" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="481.5" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="145.2" y1="462.4" x2="145.2" y2="486.1" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="474.2" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="149.0" y1="459.5" x2="149.0" y2="483.6" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="473.8" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="152.8" y1="475.0" x2="152.8" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="482.1" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="156.5" y1="494.1" x2="156.5" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="494.8" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="160.3" y1="492.4" x2="160.3" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="498.6" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="164.1" y1="504.4" x2="164.1" y2="524.4" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="504.4" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="167.9" y1="480.9" x2="167.9" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="480.9" width="2.35" height="35.1" fill="var(--up)"/>
<line x1="171.7" y1="477.1" x2="171.7" y2="489.2" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="478.8" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="175.5" y1="468.6" x2="175.5" y2="485.2" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="479.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="179.3" y1="473.8" x2="179.3" y2="492.2" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="480.0" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="183.1" y1="478.2" x2="183.1" y2="493.9" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="483.4" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="186.8" y1="466.2" x2="186.8" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="487.8" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="190.6" y1="493.9" x2="190.6" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="501.4" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="194.4" y1="493.6" x2="194.4" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="516.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="198.2" y1="521.0" x2="198.2" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="522.3" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="202.0" y1="522.2" x2="202.0" y2="563.3" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="533.0" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="205.8" y1="511.7" x2="205.8" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="511.7" width="2.35" height="36.3" fill="var(--up)"/>
<line x1="209.6" y1="510.6" x2="209.6" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="512.8" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="213.3" y1="511.3" x2="213.3" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="515.4" width="2.35" height="32.8" fill="var(--down)"/>
<line x1="217.1" y1="553.1" x2="217.1" y2="582.9" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="553.1" width="2.35" height="25.1" fill="var(--down)"/>
<line x1="220.9" y1="545.7" x2="220.9" y2="574.5" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="546.0" width="2.35" height="28.5" fill="var(--up)"/>
<line x1="224.7" y1="538.3" x2="224.7" y2="567.4" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="545.3" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="228.5" y1="545.8" x2="228.5" y2="568.9" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="549.2" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="232.3" y1="548.6" x2="232.3" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="550.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="236.1" y1="531.6" x2="236.1" y2="556.3" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="538.0" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="239.8" y1="517.8" x2="239.8" y2="541.9" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="519.1" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="243.6" y1="516.6" x2="243.6" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="519.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="247.4" y1="500.7" x2="247.4" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="500.8" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="251.2" y1="490.4" x2="251.2" y2="504.3" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="501.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="255.0" y1="504.3" x2="255.0" y2="530.4" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="504.3" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="258.8" y1="529.5" x2="258.8" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="532.2" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="262.6" y1="531.4" x2="262.6" y2="555.0" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="533.0" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="266.4" y1="525.9" x2="266.4" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="532.8" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="270.1" y1="555.5" x2="270.1" y2="591.0" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="561.5" width="2.35" height="22.6" fill="var(--down)"/>
<line x1="273.9" y1="579.8" x2="273.9" y2="601.7" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="585.3" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="277.7" y1="566.9" x2="277.7" y2="598.9" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="590.1" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="281.5" y1="567.4" x2="281.5" y2="602.8" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="583.3" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="285.3" y1="553.6" x2="285.3" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="554.3" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="289.1" y1="518.2" x2="289.1" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="518.8" width="2.35" height="33.5" fill="var(--up)"/>
<line x1="292.9" y1="514.6" x2="292.9" y2="541.5" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="520.9" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="296.6" y1="499.6" x2="296.6" y2="527.5" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="501.0" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="300.4" y1="496.3" x2="300.4" y2="511.2" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="501.1" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="304.2" y1="488.3" x2="304.2" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="489.1" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="308.0" y1="484.1" x2="308.0" y2="504.3" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="487.4" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="311.8" y1="489.3" x2="311.8" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="489.3" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="315.6" y1="481.8" x2="315.6" y2="522.9" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="505.6" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="319.4" y1="507.2" x2="319.4" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="511.9" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="323.1" y1="508.2" x2="323.1" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="511.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="326.9" y1="501.8" x2="326.9" y2="519.8" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="503.4" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="330.7" y1="489.2" x2="330.7" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="489.9" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="334.5" y1="490.6" x2="334.5" y2="517.0" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="491.6" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="338.3" y1="492.7" x2="338.3" y2="510.5" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="496.4" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="342.1" y1="489.3" x2="342.1" y2="504.4" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="497.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="345.9" y1="490.9" x2="345.9" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="498.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="349.6" y1="489.4" x2="349.6" y2="505.6" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="498.3" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="353.4" y1="502.0" x2="353.4" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="502.0" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="357.2" y1="507.9" x2="357.2" y2="526.0" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="508.2" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="361.0" y1="504.6" x2="361.0" y2="540.3" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="507.5" width="2.35" height="30.3" fill="var(--down)"/>
<line x1="364.8" y1="529.9" x2="364.8" y2="547.4" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="538.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="368.6" y1="520.8" x2="368.6" y2="539.9" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="531.2" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="372.4" y1="510.2" x2="372.4" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="510.5" width="2.35" height="19.9" fill="var(--up)"/>
<line x1="376.2" y1="503.3" x2="376.2" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="506.3" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="379.9" y1="494.3" x2="379.9" y2="509.1" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="498.3" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="383.7" y1="495.6" x2="383.7" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="497.4" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="387.5" y1="493.9" x2="387.5" y2="511.3" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="494.0" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="391.3" y1="490.8" x2="391.3" y2="517.2" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="493.7" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="395.1" y1="500.6" x2="395.1" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="501.7" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="398.9" y1="502.9" x2="398.9" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="507.5" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="402.7" y1="505.8" x2="402.7" y2="524.3" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="507.8" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="406.4" y1="499.9" x2="406.4" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="500.7" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="410.2" y1="496.5" x2="410.2" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="498.5" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="414.0" y1="484.2" x2="414.0" y2="500.3" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="490.0" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="417.8" y1="491.9" x2="417.8" y2="503.1" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="491.9" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="421.6" y1="486.7" x2="421.6" y2="503.8" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="487.8" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="425.4" y1="486.7" x2="425.4" y2="501.7" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="488.6" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="429.2" y1="484.2" x2="429.2" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="485.8" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="432.9" y1="468.5" x2="432.9" y2="487.6" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="471.4" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="436.7" y1="463.1" x2="436.7" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="466.8" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="440.5" y1="462.4" x2="440.5" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="466.7" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="444.3" y1="464.4" x2="444.3" y2="475.9" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="470.4" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="448.1" y1="469.3" x2="448.1" y2="490.7" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="470.5" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="451.9" y1="482.1" x2="451.9" y2="495.4" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="485.4" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="455.7" y1="474.6" x2="455.7" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="479.2" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="459.5" y1="478.6" x2="459.5" y2="490.2" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="479.1" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="463.2" y1="476.4" x2="463.2" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="483.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="467.0" y1="480.5" x2="467.0" y2="497.1" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="483.8" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="470.8" y1="495.6" x2="470.8" y2="509.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="497.8" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="474.6" y1="504.8" x2="474.6" y2="519.1" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="506.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="478.4" y1="496.8" x2="478.4" y2="510.9" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="502.6" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="482.2" y1="493.0" x2="482.2" y2="513.6" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="499.4" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="486.0" y1="510.6" x2="486.0" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="516.1" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="489.7" y1="492.7" x2="489.7" y2="525.2" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="494.8" width="2.35" height="30.5" fill="var(--up)"/>
<line x1="493.5" y1="489.8" x2="493.5" y2="498.8" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="490.3" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="497.3" y1="475.0" x2="497.3" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="477.1" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="501.1" y1="468.0" x2="501.1" y2="477.8" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="468.2" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="504.9" y1="450.7" x2="504.9" y2="470.4" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="451.1" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="508.7" y1="450.1" x2="508.7" y2="455.8" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="451.0" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="512.5" y1="429.0" x2="512.5" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="429.9" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="516.2" y1="423.2" x2="516.2" y2="434.5" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="428.3" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="520.0" y1="420.4" x2="520.0" y2="428.6" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="422.2" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="523.8" y1="420.2" x2="523.8" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="424.7" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="527.6" y1="419.5" x2="527.6" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="424.1" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="531.4" y1="417.3" x2="531.4" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="418.7" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="535.2" y1="411.7" x2="535.2" y2="420.1" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="413.8" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="539.0" y1="400.3" x2="539.0" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="402.9" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="542.7" y1="400.9" x2="542.7" y2="411.6" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="402.6" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="546.5" y1="397.5" x2="546.5" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="402.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="550.3" y1="390.4" x2="550.3" y2="409.2" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="393.4" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="554.1" y1="391.1" x2="554.1" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="393.1" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="557.9" y1="394.2" x2="557.9" y2="406.8" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="396.6" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="561.7" y1="392.0" x2="561.7" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="401.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="565.5" y1="378.2" x2="565.5" y2="400.8" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="386.5" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="569.3" y1="378.6" x2="569.3" y2="390.5" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="379.9" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="573.0" y1="379.7" x2="573.0" y2="404.8" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="379.8" width="2.35" height="18.1" fill="var(--down)"/>
<line x1="576.8" y1="395.7" x2="576.8" y2="418.5" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="397.7" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="580.6" y1="408.3" x2="580.6" y2="423.8" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="414.5" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="584.4" y1="404.8" x2="584.4" y2="420.9" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="411.2" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="588.2" y1="399.8" x2="588.2" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="402.5" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="592.0" y1="384.4" x2="592.0" y2="402.2" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="385.7" width="2.35" height="15.0" fill="var(--up)"/>
<line x1="595.8" y1="375.0" x2="595.8" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="375.9" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="599.5" y1="374.5" x2="599.5" y2="395.6" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="376.2" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="603.3" y1="395.4" x2="603.3" y2="416.0" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="395.4" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="607.1" y1="393.9" x2="607.1" y2="411.1" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="400.0" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="610.9" y1="393.6" x2="610.9" y2="409.9" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="400.3" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="614.7" y1="390.9" x2="614.7" y2="407.4" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="393.0" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="618.5" y1="384.6" x2="618.5" y2="397.8" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="392.3" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="622.3" y1="387.2" x2="622.3" y2="395.2" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="388.5" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="626.0" y1="370.9" x2="626.0" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="376.0" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="629.8" y1="348.5" x2="629.8" y2="373.3" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="370.2" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="633.6" y1="360.9" x2="633.6" y2="379.9" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="364.2" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="637.4" y1="352.0" x2="637.4" y2="388.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="362.7" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="641.2" y1="383.4" x2="641.2" y2="406.0" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="386.0" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="645.0" y1="361.5" x2="645.0" y2="391.0" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="362.8" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="648.8" y1="351.8" x2="648.8" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="352.5" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="652.5" y1="344.3" x2="652.5" y2="359.2" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="344.7" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="656.3" y1="346.2" x2="656.3" y2="370.1" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="346.2" width="2.35" height="22.9" fill="var(--down)"/>
<line x1="660.1" y1="345.3" x2="660.1" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="348.1" width="2.35" height="16.8" fill="var(--up)"/>
<line x1="663.9" y1="332.8" x2="663.9" y2="347.3" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="334.7" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="667.7" y1="323.4" x2="667.7" y2="338.8" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="329.7" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="671.5" y1="328.8" x2="671.5" y2="339.0" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="328.9" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="675.3" y1="318.0" x2="675.3" y2="339.4" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="318.7" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="679.1" y1="309.5" x2="679.1" y2="322.2" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="310.5" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="682.8" y1="309.8" x2="682.8" y2="335.0" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="311.6" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="686.6" y1="326.2" x2="686.6" y2="341.9" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="330.7" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="690.4" y1="292.9" x2="690.4" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="296.2" width="2.35" height="39.7" fill="var(--up)"/>
<line x1="694.2" y1="286.3" x2="694.2" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="294.8" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="698.0" y1="289.5" x2="698.0" y2="317.2" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="290.1" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="701.8" y1="274.6" x2="701.8" y2="288.3" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="277.8" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="705.6" y1="274.5" x2="705.6" y2="284.5" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="277.5" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="709.3" y1="281.4" x2="709.3" y2="300.2" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="283.2" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="713.1" y1="297.0" x2="713.1" y2="333.1" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="299.5" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="716.9" y1="308.5" x2="716.9" y2="325.7" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="316.2" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="720.7" y1="317.9" x2="720.7" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="318.7" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="724.5" y1="313.7" x2="724.5" y2="338.5" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="319.3" width="2.35" height="17.9" fill="var(--down)"/>
<line x1="728.3" y1="302.9" x2="728.3" y2="339.1" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="306.2" width="2.35" height="31.3" fill="var(--up)"/>
<line x1="732.1" y1="284.7" x2="732.1" y2="305.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="287.5" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="735.8" y1="274.9" x2="735.8" y2="295.5" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="285.1" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="739.6" y1="276.7" x2="739.6" y2="298.4" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="289.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="743.4" y1="280.6" x2="743.4" y2="293.9" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="285.1" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="747.2" y1="283.3" x2="747.2" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="284.3" width="2.35" height="23.1" fill="var(--down)"/>
<line x1="751.0" y1="298.3" x2="751.0" y2="314.0" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="299.2" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="754.8" y1="295.3" x2="754.8" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="298.0" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="758.6" y1="325.2" x2="758.6" y2="362.8" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="325.8" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="762.4" y1="331.0" x2="762.4" y2="347.7" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="336.3" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="766.1" y1="319.6" x2="766.1" y2="345.4" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="332.4" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="769.9" y1="328.4" x2="769.9" y2="410.7" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="348.3" width="2.35" height="61.4" fill="var(--down)"/>
<line x1="773.7" y1="360.4" x2="773.7" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="371.7" width="2.35" height="46.7" fill="var(--up)"/>
<line x1="777.5" y1="360.2" x2="777.5" y2="397.0" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="365.1" width="2.35" height="28.1" fill="var(--down)"/>
<line x1="781.3" y1="368.5" x2="781.3" y2="419.4" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="373.7" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="785.1" y1="348.3" x2="785.1" y2="381.1" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="349.7" width="2.35" height="22.9" fill="var(--up)"/>
<line x1="788.9" y1="340.5" x2="788.9" y2="360.8" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="351.0" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="792.6" y1="322.7" x2="792.6" y2="340.4" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="322.9" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="796.4" y1="319.2" x2="796.4" y2="348.9" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="325.1" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="800.2" y1="327.0" x2="800.2" y2="339.4" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="330.6" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="804.0" y1="317.5" x2="804.0" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="320.7" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="807.8" y1="313.7" x2="807.8" y2="334.4" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="320.3" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="811.6" y1="321.8" x2="811.6" y2="334.2" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="330.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="815.4" y1="296.7" x2="815.4" y2="336.4" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="299.6" width="2.35" height="32.8" fill="var(--up)"/>
<line x1="819.1" y1="278.3" x2="819.1" y2="298.2" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="279.4" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="822.9" y1="279.9" x2="822.9" y2="292.8" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="279.9" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="826.7" y1="284.6" x2="826.7" y2="300.8" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="289.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="830.5" y1="275.7" x2="830.5" y2="290.5" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="278.0" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="834.3" y1="277.1" x2="834.3" y2="309.2" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="277.1" width="2.35" height="27.2" fill="var(--down)"/>
<line x1="838.1" y1="286.0" x2="838.1" y2="301.5" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="292.5" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="841.9" y1="271.9" x2="841.9" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="277.1" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="845.6" y1="260.8" x2="845.6" y2="284.4" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="263.4" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="849.4" y1="262.3" x2="849.4" y2="272.2" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="263.9" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="853.2" y1="260.6" x2="853.2" y2="277.0" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="268.0" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="857.0" y1="253.3" x2="857.0" y2="270.4" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="259.3" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="860.8" y1="248.1" x2="860.8" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="249.7" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="864.6" y1="241.7" x2="864.6" y2="260.3" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="251.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="868.4" y1="235.0" x2="868.4" y2="253.9" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="240.8" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="872.2" y1="238.6" x2="872.2" y2="266.6" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="240.5" width="2.35" height="25.9" fill="var(--down)"/>
<line x1="875.9" y1="242.1" x2="875.9" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="252.2" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="879.7" y1="229.5" x2="879.7" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="231.9" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="883.5" y1="215.2" x2="883.5" y2="229.1" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="224.7" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="887.3" y1="222.1" x2="887.3" y2="246.1" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="222.1" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="891.1" y1="207.4" x2="891.1" y2="238.7" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="233.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="894.9" y1="231.9" x2="894.9" y2="261.4" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="234.6" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="898.7" y1="221.0" x2="898.7" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="221.7" width="2.35" height="27.3" fill="var(--up)"/>
<line x1="902.4" y1="213.3" x2="902.4" y2="230.7" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="216.9" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="906.2" y1="198.3" x2="906.2" y2="226.7" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="206.8" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="910.0" y1="202.4" x2="910.0" y2="219.0" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="204.1" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="913.8" y1="200.4" x2="913.8" y2="212.0" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="201.8" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="917.6" y1="201.9" x2="917.6" y2="218.9" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="203.3" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="921.4" y1="183.6" x2="921.4" y2="207.0" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="185.9" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="925.2" y1="183.3" x2="925.2" y2="199.0" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="186.0" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="928.9" y1="183.9" x2="928.9" y2="207.4" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="194.0" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="932.7" y1="186.2" x2="932.7" y2="206.8" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="193.2" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="936.5" y1="172.6" x2="936.5" y2="202.5" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="173.7" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="940.3" y1="165.7" x2="940.3" y2="194.3" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="175.0" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="944.1" y1="178.1" x2="944.1" y2="192.8" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="183.5" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="947.9" y1="179.7" x2="947.9" y2="202.4" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="185.3" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="951.7" y1="194.7" x2="951.7" y2="235.8" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="200.1" width="2.35" height="25.9" fill="var(--down)"/>
<line x1="955.5" y1="211.6" x2="955.5" y2="246.1" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="228.6" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="959.2" y1="227.4" x2="959.2" y2="268.6" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="241.9" width="2.35" height="22.6" fill="var(--down)"/>
<line x1="963.0" y1="241.6" x2="963.0" y2="274.7" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="259.9" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="966.8" y1="239.9" x2="966.8" y2="274.9" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="245.9" width="2.35" height="24.4" fill="var(--up)"/>
<line x1="970.6" y1="209.5" x2="970.6" y2="251.7" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="217.7" width="2.35" height="28.9" fill="var(--up)"/>
<line x1="974.4" y1="181.6" x2="974.4" y2="225.9" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="187.1" width="2.35" height="34.6" fill="var(--up)"/>
<line x1="978.2" y1="179.0" x2="978.2" y2="198.8" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="187.6" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="982.0" y1="176.2" x2="982.0" y2="201.8" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="186.0" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="985.7" y1="173.4" x2="985.7" y2="197.7" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="183.8" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="989.5" y1="172.0" x2="989.5" y2="189.8" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="185.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="993.3" y1="159.4" x2="993.3" y2="191.3" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="164.4" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="997.1" y1="154.1" x2="997.1" y2="169.7" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="155.4" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="1000.9" y1="142.8" x2="1000.9" y2="162.3" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="152.8" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="1004.7" y1="147.8" x2="1004.7" y2="177.8" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="152.0" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="1008.5" y1="130.4" x2="1008.5" y2="148.7" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="144.7" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="1012.2" y1="122.9" x2="1012.2" y2="150.0" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="138.5" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="1016.0" y1="117.9" x2="1016.0" y2="137.0" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="118.0" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="1019.8" y1="110.2" x2="1019.8" y2="134.6" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="119.4" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="1023.6" y1="117.5" x2="1023.6" y2="136.3" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="122.5" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="1027.4" y1="125.8" x2="1027.4" y2="145.2" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="132.9" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="1031.2" y1="118.0" x2="1031.2" y2="145.0" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="126.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="1035.0" y1="81.1" x2="1035.0" y2="120.8" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="95.3" width="2.35" height="25.6" fill="var(--up)"/>
<line x1="1038.7" y1="91.5" x2="1038.7" y2="103.6" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="94.5" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="1042.5" y1="101.8" x2="1042.5" y2="120.9" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="102.7" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="1046.3" y1="101.8" x2="1046.3" y2="110.8" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="104.6" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="1050.1" y1="99.6" x2="1050.1" y2="106.2" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="103.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="60" y1="267.7" x2="1052" y2="267.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="261.7" font-size="11.5" fill="var(--support)" font-weight="600">45,412.75 S1</text>
<text x="1058" y="273.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="341.1" x2="1052" y2="341.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="335.1" font-size="11.5" fill="var(--support)" font-weight="600">41,746.10 S2</text>
<text x="1058" y="347.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="414.9" x2="1052" y2="414.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="408.9" font-size="11.5" fill="var(--support)" font-weight="600">38,055.41 S3</text>
<text x="1058" y="420.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="104.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="96.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 53,559.99 (2026-08-28)</text>
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

## 2. 해석

- **상승**: 대형 우량주를 중심으로 미국 경기에 대한 기대가 좋아졌거나, 투자자들이 위험을 더 감수하려는 신호로 흔히 해석한다.
- **하락**: 경기가 둔화될 것이라는 우려나, 위험을 피하려는 심리가 커졌다는 신호로 흔히 해석한다.
- **주가 가중 지수**라는 점을 꼭 기억해야 한다 — 회사의 실제 규모(시가총액)와 상관없이, 주가 자체가 높은 종목의 움직임이 지수에 더 크게 반영된다. 그래서 시가총액을 기준으로 비중을 매기는 S&P 500·나스닥종합지수와 같은 감각으로 해석하면 안 된다.
- **왜 이런 방식을 쓰나**: 1896년 다우존스가 지수를 처음 만들 때는 계산을 사람이 손으로 해야 했던 시절이라, 단순히 주가를 더해서 나누는 방식이 가장 계산하기 쉬웠다. 오늘날 기관들이 벤치마크로 쓸 때는 시가총액 가중 지수(S&P 500)를 훨씬 더 널리 쓰는데, 이것도 이 계산 방식의 한계 때문이다.

---

*작성일: 2026-08-29*
