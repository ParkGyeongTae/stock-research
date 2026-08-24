# 코스피

!!! note ""
    최근 5년간 코스피 지수(한국거래소 유가증권시장, `^KS11`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 원/달러 환율 문서와 함께 보면 원화 가치와 한국 증시가 지금 어떤 국면인지 종합적으로 파악하는 데 도움이 된다.

---

## 1. 차트 — 최근 5년 주봉

<div class="ks11-chart">
<style>
.ks11-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ks11-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ks11-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ks11-chart svg { width:100%; height:auto; display:block; }
.ks11-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ks11-chart .title { fill: var(--ink); font-weight:600; }
.ks11-chart .grid { stroke: var(--grid); stroke-width:1; }
.ks11-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="코스피(^KS11) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">코스피 (^KS11) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 6,912.95 (2026-08-21) · 단위 지수</text>
<line x1="60" y1="618.7" x2="1052" y2="618.7" class="grid"/>
<text x="52" y="622.7" font-size="11" text-anchor="end" fill="var(--muted)">2,000.00</text>
<line x1="60" y1="545.6" x2="1052" y2="545.6" class="grid"/>
<text x="52" y="549.6" font-size="11" text-anchor="end" fill="var(--muted)">3,000.00</text>
<line x1="60" y1="472.5" x2="1052" y2="472.5" class="grid"/>
<text x="52" y="476.5" font-size="11" text-anchor="end" fill="var(--muted)">4,000.00</text>
<line x1="60" y1="399.5" x2="1052" y2="399.5" class="grid"/>
<text x="52" y="403.5" font-size="11" text-anchor="end" fill="var(--muted)">5,000.00</text>
<line x1="60" y1="326.4" x2="1052" y2="326.4" class="grid"/>
<text x="52" y="330.4" font-size="11" text-anchor="end" fill="var(--muted)">6,000.00</text>
<line x1="60" y1="253.3" x2="1052" y2="253.3" class="grid"/>
<text x="52" y="257.3" font-size="11" text-anchor="end" fill="var(--muted)">7,000.00</text>
<line x1="60" y1="180.2" x2="1052" y2="180.2" class="grid"/>
<text x="52" y="184.2" font-size="11" text-anchor="end" fill="var(--muted)">8,000.00</text>
<line x1="60" y1="107.2" x2="1052" y2="107.2" class="grid"/>
<text x="52" y="111.2" font-size="11" text-anchor="end" fill="var(--muted)">9,000.00</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="133.8" y1="56.0" x2="133.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="133.8" y1="626.0" x2="133.8" y2="631.0" class="axis"/>
<text x="133.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="330.7" y1="56.0" x2="330.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="330.7" y1="626.0" x2="330.7" y2="631.0" class="axis"/>
<text x="330.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="527.6" y1="56.0" x2="527.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="527.6" y1="626.0" x2="527.6" y2="631.0" class="axis"/>
<text x="527.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="728.3" y1="56.0" x2="728.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="728.3" y1="626.0" x2="728.3" y2="631.0" class="axis"/>
<text x="728.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.2" y1="56.0" x2="925.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="925.2" y1="626.0" x2="925.2" y2="631.0" class="axis"/>
<text x="925.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="533.9" x2="61.9" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="535.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="65.7" y1="529.9" x2="65.7" y2="536.1" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="530.9" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="69.5" y1="530.5" x2="69.5" y2="538.1" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="531.3" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="73.3" y1="533.4" x2="73.3" y2="537.6" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="535.3" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="77.0" y1="534.9" x2="77.0" y2="537.7" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="536.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="80.8" y1="534.9" x2="80.8" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="536.7" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="84.6" y1="545.7" x2="84.6" y2="552.3" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="545.7" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="88.4" y1="544.0" x2="88.4" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="544.5" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="92.2" y1="542.2" x2="92.2" y2="546.3" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="544.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="96.0" y1="541.8" x2="96.0" y2="548.1" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="545.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="99.8" y1="543.1" x2="99.8" y2="549.0" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="546.8" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="103.5" y1="546.5" x2="103.5" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="547.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="107.3" y1="544.7" x2="107.3" y2="550.2" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="546.4" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="111.1" y1="544.3" x2="111.1" y2="550.7" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="546.8" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="114.9" y1="547.4" x2="114.9" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="547.9" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="118.7" y1="543.0" x2="118.7" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="544.9" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="122.5" y1="542.4" x2="122.5" y2="547.6" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="544.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="126.3" y1="543.7" x2="126.3" y2="548.8" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="544.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="130.0" y1="544.1" x2="130.0" y2="547.4" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="544.6" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="133.8" y1="544.8" x2="133.8" y2="551.8" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="545.7" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="137.6" y1="546.9" x2="137.6" y2="552.2" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="549.5" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="141.4" y1="551.5" x2="141.4" y2="559.0" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="551.6" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="145.2" y1="558.2" x2="145.2" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="558.5" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="149.0" y1="563.8" x2="149.0" y2="567.3" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="563.9" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="152.8" y1="561.1" x2="152.8" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="563.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="156.5" y1="562.4" x2="156.5" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="564.3" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="160.3" y1="564.1" x2="160.3" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="567.1" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="164.1" y1="564.0" x2="164.1" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="566.6" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="167.9" y1="568.8" x2="167.9" y2="574.4" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="569.0" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="171.7" y1="566.5" x2="171.7" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="567.0" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="175.5" y1="564.4" x2="175.5" y2="568.7" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="565.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="179.3" y1="562.8" x2="179.3" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="564.6" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="183.1" y1="562.5" x2="183.1" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="565.4" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="186.8" y1="566.1" x2="186.8" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="567.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="190.6" y1="564.8" x2="190.6" y2="568.9" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="567.2" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="194.4" y1="567.8" x2="194.4" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="567.9" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="198.2" y1="567.4" x2="198.2" y2="572.2" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="569.8" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="202.0" y1="571.7" x2="202.0" y2="578.7" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="572.3" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="205.8" y1="571.6" x2="205.8" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="572.0" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="209.6" y1="570.9" x2="209.6" y2="574.7" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="571.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="213.3" y1="568.6" x2="213.3" y2="570.9" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="569.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="217.1" y1="570.3" x2="217.1" y2="576.0" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="570.5" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="220.9" y1="578.5" x2="220.9" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="578.5" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="224.7" y1="585.8" x2="224.7" y2="596.3" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="585.8" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="228.5" y1="587.8" x2="228.5" y2="597.4" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="590.7" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="232.3" y1="591.8" x2="232.3" y2="598.5" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="593.1" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="236.1" y1="592.1" x2="236.1" y2="597.2" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="592.6" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="239.8" y1="588.2" x2="239.8" y2="593.5" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="590.0" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="243.6" y1="584.9" x2="243.6" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="585.7" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="247.4" y1="582.3" x2="247.4" y2="587.4" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="582.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="251.2" y1="579.7" x2="251.2" y2="583.8" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="580.1" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="255.0" y1="578.8" x2="255.0" y2="583.0" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="579.0" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="258.8" y1="582.3" x2="258.8" y2="587.2" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="583.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="262.6" y1="584.1" x2="262.6" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="587.1" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="266.4" y1="587.7" x2="266.4" y2="592.0" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="588.7" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="270.1" y1="585.5" x2="270.1" y2="591.6" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="588.1" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="273.9" y1="590.2" x2="273.9" y2="597.8" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="590.3" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="277.7" y1="599.6" x2="277.7" y2="608.8" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="599.6" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="281.5" y1="600.1" x2="281.5" y2="605.5" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="601.7" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="285.3" y1="602.6" x2="285.3" y2="606.8" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="603.2" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="289.1" y1="599.2" x2="289.1" y2="605.7" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="603.1" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="292.9" y1="597.3" x2="292.9" y2="601.9" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="599.1" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="296.6" y1="593.2" x2="296.6" y2="598.7" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="593.2" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="300.4" y1="583.1" x2="300.4" y2="592.8" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="583.4" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="304.2" y1="582.2" x2="304.2" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="583.2" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="308.0" y1="585.8" x2="308.0" y2="589.4" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="586.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="311.8" y1="582.0" x2="311.8" y2="589.4" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="587.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="315.6" y1="586.4" x2="315.6" y2="592.6" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="586.4" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="319.4" y1="589.4" x2="319.4" y2="594.8" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="591.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="323.1" y1="592.5" x2="323.1" y2="595.9" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="593.1" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="326.9" y1="594.1" x2="326.9" y2="601.4" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="595.9" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="330.7" y1="596.7" x2="330.7" y2="605.5" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="597.5" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="334.5" y1="589.7" x2="334.5" y2="595.9" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="590.5" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="338.3" y1="588.7" x2="338.3" y2="592.8" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="589.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="342.1" y1="582.3" x2="342.1" y2="587.9" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="583.3" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="345.9" y1="582.8" x2="345.9" y2="587.8" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="583.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="349.6" y1="583.1" x2="349.6" y2="587.1" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="584.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="353.4" y1="583.6" x2="353.4" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="584.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="357.2" y1="584.6" x2="357.2" y2="588.3" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="585.6" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="361.0" y1="586.4" x2="361.0" y2="590.6" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="587.1" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="364.8" y1="583.9" x2="364.8" y2="590.7" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="585.6" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="368.6" y1="588.5" x2="368.6" y2="593.4" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="589.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="372.4" y1="587.7" x2="372.4" y2="591.0" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="588.4" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="376.2" y1="583.5" x2="376.2" y2="589.8" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="583.8" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="379.9" y1="582.3" x2="379.9" y2="585.2" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="582.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="383.7" y1="576.2" x2="383.7" y2="582.9" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="576.9" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="387.5" y1="576.1" x2="387.5" y2="579.8" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="577.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="391.3" y1="579.1" x2="391.3" y2="584.7" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="579.4" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="395.1" y1="580.4" x2="395.1" y2="583.2" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="581.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="398.9" y1="580.3" x2="398.9" y2="584.2" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="580.8" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="402.7" y1="579.4" x2="402.7" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="579.4" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="406.4" y1="576.5" x2="406.4" y2="579.7" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="577.9" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="410.2" y1="574.7" x2="410.2" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="574.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="414.0" y1="571.6" x2="414.0" y2="575.2" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="571.8" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="417.8" y1="571.2" x2="417.8" y2="574.7" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="571.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="421.6" y1="573.4" x2="421.6" y2="577.2" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="573.5" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="425.4" y1="575.5" x2="425.4" y2="579.1" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="577.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="429.2" y1="574.3" x2="429.2" y2="581.1" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="576.2" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="432.9" y1="572.8" x2="432.9" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="572.8" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="436.7" y1="572.9" x2="436.7" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="573.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="440.5" y1="571.4" x2="440.5" y2="576.2" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="574.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="444.3" y1="569.9" x2="444.3" y2="575.5" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="572.7" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="448.1" y1="573.6" x2="448.1" y2="577.2" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="575.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="451.9" y1="575.4" x2="451.9" y2="583.5" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="575.8" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="455.7" y1="579.3" x2="455.7" y2="582.2" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="580.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="459.5" y1="576.4" x2="459.5" y2="580.8" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="577.5" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="463.2" y1="575.8" x2="463.2" y2="580.0" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="577.3" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="467.0" y1="574.0" x2="467.0" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="574.8" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="470.8" y1="575.1" x2="470.8" y2="583.2" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="575.7" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="474.6" y1="581.5" x2="474.6" y2="586.1" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="581.9" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="478.4" y1="586.8" x2="478.4" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="586.8" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="482.2" y1="583.6" x2="482.2" y2="589.3" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="585.4" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="486.0" y1="584.6" x2="486.0" y2="592.1" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="586.4" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="489.7" y1="590.2" x2="489.7" y2="597.3" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="591.6" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="493.5" y1="591.6" x2="493.5" y2="598.7" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="591.8" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="497.3" y1="582.0" x2="497.3" y2="589.9" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="588.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="501.1" y1="582.7" x2="501.1" y2="589.5" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="584.4" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="504.9" y1="580.5" x2="504.9" y2="584.8" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="582.4" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="508.7" y1="579.6" x2="508.7" y2="582.9" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="581.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="512.5" y1="580.3" x2="512.5" y2="583.5" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="580.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="516.2" y1="576.7" x2="516.2" y2="581.4" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="577.5" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="520.0" y1="573.3" x2="520.0" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="574.9" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="523.8" y1="570.8" x2="523.8" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="570.8" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="527.6" y1="569.3" x2="527.6" y2="576.8" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="571.5" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="531.4" y1="574.9" x2="531.4" y2="580.9" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="576.0" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="535.2" y1="579.5" x2="535.2" y2="587.3" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="580.3" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="539.0" y1="582.0" x2="539.0" y2="585.6" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="582.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="542.7" y1="573.7" x2="542.7" y2="583.3" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="573.7" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="546.5" y1="572.7" x2="546.5" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="573.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="550.3" y1="570.7" x2="550.3" y2="574.7" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="571.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="554.1" y1="567.9" x2="554.1" y2="571.6" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="569.9" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="557.9" y1="570.5" x2="557.9" y2="573.4" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="570.7" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="561.7" y1="568.4" x2="561.7" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="569.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="565.5" y1="566.2" x2="565.5" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="570.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="569.3" y1="562.9" x2="569.3" y2="571.5" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="564.0" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="573.0" y1="561.7" x2="573.0" y2="565.2" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="563.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="576.8" y1="562.4" x2="576.8" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="562.7" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="580.6" y1="564.5" x2="580.6" y2="570.3" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="566.2" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="584.4" y1="569.5" x2="584.4" y2="578.2" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="570.4" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="588.2" y1="569.2" x2="588.2" y2="574.5" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="570.7" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="592.0" y1="566.8" x2="592.0" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="569.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="595.8" y1="563.9" x2="595.8" y2="566.8" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="565.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="599.5" y1="562.2" x2="599.5" y2="566.5" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="565.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="603.3" y1="563.4" x2="603.3" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="564.5" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="607.1" y1="565.3" x2="607.1" y2="572.3" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="567.7" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="610.9" y1="565.4" x2="610.9" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="565.9" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="614.7" y1="561.9" x2="614.7" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="563.3" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="618.5" y1="559.3" x2="618.5" y2="564.5" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="561.4" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="622.3" y1="560.4" x2="622.3" y2="563.3" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="560.4" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="626.0" y1="555.0" x2="626.0" y2="562.1" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="555.7" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="629.8" y1="553.2" x2="629.8" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="555.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="633.6" y1="554.9" x2="633.6" y2="561.9" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="555.2" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="637.4" y1="560.5" x2="637.4" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="560.9" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="641.2" y1="560.7" x2="641.2" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="564.0" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="645.0" y1="574.0" x2="645.0" y2="590.4" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="574.0" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="648.8" y1="567.6" x2="648.8" y2="574.7" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="567.7" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="652.5" y1="566.6" x2="652.5" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="567.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="656.3" y1="566.2" x2="656.3" y2="571.2" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="566.3" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="660.1" y1="567.9" x2="660.1" y2="580.0" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="568.7" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="663.9" y1="576.0" x2="663.9" y2="582.8" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="576.6" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="667.7" y1="573.4" x2="667.7" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="575.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="671.5" y1="568.9" x2="671.5" y2="575.7" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="571.2" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="675.3" y1="569.8" x2="675.3" y2="578.1" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="570.1" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="679.1" y1="573.2" x2="679.1" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="575.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="682.8" y1="572.3" x2="682.8" y2="575.7" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="574.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="686.6" y1="573.5" x2="686.6" y2="577.4" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="574.8" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="690.4" y1="573.5" x2="690.4" y2="579.5" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="575.7" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="694.2" y1="575.3" x2="694.2" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="577.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="698.0" y1="577.6" x2="698.0" y2="590.2" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="577.6" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="701.8" y1="581.3" x2="701.8" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="582.1" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="705.6" y1="579.1" x2="705.6" y2="586.0" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="580.4" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="709.3" y1="582.1" x2="709.3" y2="589.6" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="583.7" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="713.1" y1="582.1" x2="713.1" y2="592.4" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="582.6" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="716.9" y1="581.0" x2="716.9" y2="590.2" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="581.3" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="720.7" y1="585.6" x2="720.7" y2="590.3" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="587.8" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="724.5" y1="585.5" x2="724.5" y2="590.4" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="586.4" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="728.3" y1="579.5" x2="728.3" y2="586.0" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="581.0" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="732.1" y1="579.7" x2="732.1" y2="583.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="580.4" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="735.8" y1="578.3" x2="735.8" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="579.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="739.6" y1="579.4" x2="739.6" y2="582.4" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="579.6" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="743.4" y1="579.4" x2="743.4" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="580.6" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="747.2" y1="574.8" x2="747.2" y2="582.2" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="575.5" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="751.0" y1="568.9" x2="751.0" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="570.9" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="754.8" y1="571.3" x2="754.8" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="572.2" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="758.6" y1="576.0" x2="758.6" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="577.5" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="762.4" y1="574.8" x2="762.4" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="577.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="766.1" y1="571.1" x2="766.1" y2="575.8" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="571.7" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="769.9" y1="570.9" x2="769.9" y2="578.6" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="572.2" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="773.7" y1="579.8" x2="773.7" y2="586.7" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="581.2" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="777.5" y1="586.2" x2="777.5" y2="597.9" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="587.1" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="781.3" y1="583.1" x2="781.3" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="583.4" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="785.1" y1="578.3" x2="785.1" y2="583.9" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="578.8" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="788.9" y1="576.9" x2="788.9" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="577.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="792.6" y1="575.5" x2="792.6" y2="577.8" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="576.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="796.4" y1="571.5" x2="796.4" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="572.9" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="800.2" y1="572.4" x2="800.2" y2="575.7" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="573.8" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="804.0" y1="566.0" x2="804.0" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="567.7" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="807.8" y1="558.0" x2="807.8" y2="568.6" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="559.4" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="811.6" y1="550.4" x2="811.6" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="553.3" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="815.4" y1="544.0" x2="815.4" y2="553.9" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="544.0" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="819.1" y1="536.2" x2="819.1" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="541.5" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="822.9" y1="535.9" x2="822.9" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="540.3" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="826.7" y1="529.8" x2="826.7" y2="543.2" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="532.8" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="830.5" y1="529.8" x2="830.5" y2="534.5" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="531.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="834.3" y1="528.2" x2="834.3" y2="535.2" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="531.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="838.1" y1="524.6" x2="838.1" y2="537.0" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="528.9" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="841.9" y1="529.0" x2="841.9" y2="537.9" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="530.3" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="845.6" y1="527.9" x2="845.6" y2="531.8" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="529.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="849.4" y1="530.5" x2="849.4" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="530.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="853.2" y1="530.1" x2="853.2" y2="533.6" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="531.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="857.0" y1="529.9" x2="857.0" y2="535.7" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="530.6" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="860.8" y1="516.7" x2="860.8" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="516.7" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="864.6" y1="511.4" x2="864.6" y2="517.0" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="513.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="868.4" y1="509.2" x2="868.4" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="511.7" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="872.2" y1="504.3" x2="872.2" y2="515.4" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="505.5" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="875.9" y1="500.5" x2="875.9" y2="504.0" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="501.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="879.7" y1="487.5" x2="879.7" y2="507.4" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="490.9" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="883.5" y1="476.1" x2="883.5" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="476.8" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="887.3" y1="461.8" x2="887.3" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="464.7" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="891.1" y1="456.0" x2="891.1" y2="482.2" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="463.5" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="894.9" y1="458.8" x2="894.9" y2="473.7" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="471.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="898.7" y1="466.0" x2="898.7" y2="484.3" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="466.8" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="902.4" y1="470.8" x2="902.4" y2="484.7" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="477.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="906.2" y1="465.2" x2="906.2" y2="480.4" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="465.2" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="910.0" y1="459.9" x2="910.0" y2="466.6" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="460.3" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="913.8" y1="463.5" x2="913.8" y2="474.3" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="468.6" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="917.6" y1="462.1" x2="917.6" y2="466.5" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="463.1" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="921.4" y1="449.6" x2="921.4" y2="461.8" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="449.9" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="925.2" y1="427.1" x2="925.2" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="429.7" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="928.9" y1="410.0" x2="928.9" y2="431.1" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="411.1" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="932.7" y1="397.9" x2="932.7" y2="413.6" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="400.2" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="936.5" y1="376.0" x2="936.5" y2="407.4" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="383.1" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="940.3" y1="371.9" x2="940.3" y2="406.8" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="390.5" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="944.1" y1="356.8" x2="944.1" y2="380.6" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="362.4" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="947.9" y1="340.3" x2="947.9" y2="354.5" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="340.4" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="951.7" y1="301.0" x2="951.7" y2="342.8" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="308.5" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="955.5" y1="313.2" x2="955.5" y2="395.1" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="314.3" width="2.35" height="42.4" fill="var(--down)"/>
<line x1="959.2" y1="344.9" x2="959.2" y2="392.4" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="363.9" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="963.0" y1="331.2" x2="963.0" y2="366.7" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="342.4" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="966.8" y1="345.3" x2="966.8" y2="383.4" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="357.1" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="970.6" y1="357.5" x2="970.6" y2="396.3" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="371.9" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="974.4" y1="332.3" x2="974.4" y2="369.9" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="336.7" width="2.35" height="31.8" fill="var(--up)"/>
<line x1="978.2" y1="309.5" x2="978.2" y2="346.1" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="312.4" width="2.35" height="33.2" fill="var(--up)"/>
<line x1="982.0" y1="285.6" x2="982.0" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="291.6" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="985.7" y1="271.6" x2="985.7" y2="287.7" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="282.6" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="989.5" y1="214.4" x2="989.5" y2="272.2" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="216.9" width="2.35" height="52.3" fill="var(--up)"/>
<line x1="993.3" y1="176.8" x2="993.3" y2="226.1" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="196.7" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="997.1" y1="188.5" x2="997.1" y2="249.4" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="191.4" width="2.35" height="29.6" fill="var(--up)"/>
<line x1="1000.9" y1="145.4" x2="1000.9" y2="191.8" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="145.4" width="2.35" height="29.6" fill="var(--up)"/>
<line x1="1004.7" y1="112.0" x2="1004.7" y2="177.4" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="144.7" width="2.35" height="23.8" fill="var(--down)"/>
<line x1="1008.5" y1="148.5" x2="1008.5" y2="224.5" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="171.2" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="1012.2" y1="79.0" x2="1012.2" y2="147.3" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="103.3" width="2.35" height="38.5" fill="var(--up)"/>
<line x1="1016.0" y1="88.7" x2="1016.0" y2="174.3" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="110.5" width="2.35" height="39.7" fill="var(--down)"/>
<line x1="1019.8" y1="131.4" x2="1019.8" y2="225.7" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="151.4" width="2.35" height="22.4" fill="var(--down)"/>
<line x1="1023.6" y1="156.3" x2="1023.6" y2="248.6" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="166.6" width="2.35" height="51.9" fill="var(--down)"/>
<line x1="1027.4" y1="214.6" x2="1027.4" y2="293.6" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="223.2" width="2.35" height="43.2" fill="var(--down)"/>
<line x1="1031.2" y1="241.2" x2="1031.2" y2="295.0" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="275.9" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="1035.0" y1="267.5" x2="1035.0" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="267.5" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="1038.7" y1="277.1" x2="1038.7" y2="320.5" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="300.2" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="1042.5" y1="252.5" x2="1042.5" y2="310.8" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="254.9" width="2.35" height="49.1" fill="var(--up)"/>
<line x1="1046.3" y1="237.5" x2="1046.3" y2="297.1" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="244.0" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="1050.1" y1="256.7" x2="1050.1" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="259.7" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="60" y1="575.8" x2="1052" y2="575.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="569.8" font-size="11.5" fill="var(--support)" font-weight="600">2,586.63 S1</text>
<text x="1058" y="581.8" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="584.5" x2="1052" y2="584.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="578.5" font-size="11.5" fill="var(--support)" font-weight="600">2,468.53 S2</text>
<text x="1058" y="590.5" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="592.1" x2="1052" y2="592.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="586.1" font-size="11.5" fill="var(--support)" font-weight="600">2,364.42 S3</text>
<text x="1058" y="598.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="259.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="251.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 6,912.95 (2026-08-21)</text>
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

- **상승**: 한국 대형·수출기업의 실적 기대가 좋아졌거나, 외국인 투자자의 자금이 들어오고 있다는 신호로 흔히 해석한다.
- **하락**: 수출 경기가 둔화될 것이라는 우려나, 외국인 자금이 빠져나가고 있다는 신호로 흔히 해석한다.
- 원/달러 환율과 반대로 움직이는 경우가 많다(원화가 강해지면 외국인 자금이 더 들어오기 쉬워지기 때문이다) — 두 문서를 함께 보면 지금 국면을 더 잘 가늠할 수 있다.
- **왜 외국인 자금 흐름에 유독 민감한가**: 코스피에는 시가총액은 크지만 실제로 시장에서 거래 가능한 물량(유동주식)이 적은 대형주가 많고, 반도체 등 특정 업종에 쏠려 있다. MSCI·FTSE 같은 글로벌 지수에서 한국의 비중을 조정하는 이벤트가 있을 때마다, 그 지수를 따라가는 자금(패시브 자금)이 한꺼번에 크게 사고팔면서 지수를 흔드는 경우도 잦다.

---

## 관련 문서

- [원/달러 환율](../foreign_exchange/usd_krw.md)
- [코스닥](./kosdaq.md)
- [코스피·코스닥 비교 (지수화)](./kr_comparison.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md)
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — KOSPI Composite Index (^KS11)](https://finance.yahoo.com/quote/%5EKS11/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
