# 필라델피아 반도체지수 (SOX)

!!! note ""
    최근 5년간 필라델피아 반도체지수(`^SOX`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 시장 전체를 대표하는 지표가 아니라, 반도체를 설계·제조하거나 관련 장비를 만드는 회사들로만 구성된 **업종(섹터) 지수**다.

    **어떻게 쓰나**: 어떤 회사의 주가가 SOX 지수보다 유독 더 오르거나 내렸다면, 그 회사만의 특별한 이유(펀더멘털) 때문인지 반도체 업황 전체(사이클)의 문제인지 구분하는 첫 단서가 된다. 그 회사의 기술적 차트와 SOX 차트를 같은 기간으로 나란히 놓고 비교해 보는 방법을 권한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="sox-chart">
<style>
.sox-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .sox-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .sox-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.sox-chart svg { width:100%; height:auto; display:block; }
.sox-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.sox-chart .title { fill: var(--ink); font-weight:600; }
.sox-chart .grid { stroke: var(--grid); stroke-width:1; }
.sox-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="필라델피아 반도체지수(^SOX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">필라델피아 반도체지수 (^SOX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 11,740.37 (2026-08-21) · 단위 지수</text>
<line x1="60" y1="605.3" x2="1052" y2="605.3" class="grid"/>
<text x="52" y="609.3" font-size="11" text-anchor="end" fill="var(--muted)">2,000.00</text>
<line x1="60" y1="522.4" x2="1052" y2="522.4" class="grid"/>
<text x="52" y="526.4" font-size="11" text-anchor="end" fill="var(--muted)">4,000.00</text>
<line x1="60" y1="439.5" x2="1052" y2="439.5" class="grid"/>
<text x="52" y="443.5" font-size="11" text-anchor="end" fill="var(--muted)">6,000.00</text>
<line x1="60" y1="356.5" x2="1052" y2="356.5" class="grid"/>
<text x="52" y="360.5" font-size="11" text-anchor="end" fill="var(--muted)">8,000.00</text>
<line x1="60" y1="273.6" x2="1052" y2="273.6" class="grid"/>
<text x="52" y="277.6" font-size="11" text-anchor="end" fill="var(--muted)">10,000.00</text>
<line x1="60" y1="190.7" x2="1052" y2="190.7" class="grid"/>
<text x="52" y="194.7" font-size="11" text-anchor="end" fill="var(--muted)">12,000.00</text>
<line x1="60" y1="107.8" x2="1052" y2="107.8" class="grid"/>
<text x="52" y="111.8" font-size="11" text-anchor="end" fill="var(--muted)">14,000.00</text>
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
<line x1="61.9" y1="545.5" x2="61.9" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="545.7" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="65.7" y1="544.0" x2="65.7" y2="547.6" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="544.7" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="69.5" y1="544.4" x2="69.5" y2="549.3" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="545.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="73.3" y1="543.7" x2="73.3" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="545.1" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="77.0" y1="544.4" x2="77.0" y2="551.8" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="545.0" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="80.8" y1="544.8" x2="80.8" y2="555.2" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="546.5" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="84.6" y1="550.6" x2="84.6" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="553.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="88.4" y1="550.3" x2="88.4" y2="557.0" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="550.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="92.2" y1="546.1" x2="92.2" y2="552.3" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="548.5" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="96.0" y1="545.0" x2="96.0" y2="549.2" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="545.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="99.8" y1="531.1" x2="99.8" y2="545.1" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="532.5" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="103.5" y1="529.1" x2="103.5" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="530.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="107.3" y1="525.0" x2="107.3" y2="532.3" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="526.0" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="111.1" y1="523.1" x2="111.1" y2="533.3" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="525.3" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="114.9" y1="524.1" x2="114.9" y2="533.0" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="529.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="118.7" y1="522.3" x2="118.7" y2="535.3" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="525.9" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="122.5" y1="523.9" x2="122.5" y2="533.9" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="525.2" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="126.3" y1="524.2" x2="126.3" y2="535.2" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="525.2" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="130.0" y1="520.1" x2="130.0" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="524.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="133.8" y1="519.5" x2="133.8" y2="531.2" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="523.4" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="137.6" y1="522.7" x2="137.6" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="526.5" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="141.4" y1="529.0" x2="141.4" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="529.0" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="145.2" y1="541.4" x2="145.2" y2="557.7" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="548.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="149.0" y1="538.9" x2="149.0" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="545.0" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="152.8" y1="535.9" x2="152.8" y2="549.6" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="544.3" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="156.5" y1="540.3" x2="156.5" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="547.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="160.3" y1="545.0" x2="160.3" y2="557.5" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="545.1" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="164.1" y1="544.7" x2="164.1" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="546.6" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="167.9" y1="551.2" x2="167.9" y2="561.0" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="552.5" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="171.7" y1="545.4" x2="171.7" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="545.9" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="175.5" y1="541.6" x2="175.5" y2="548.9" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="542.0" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="179.3" y1="537.6" x2="179.3" y2="550.6" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="543.0" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="183.1" y1="546.0" x2="183.1" y2="559.0" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="548.0" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="186.8" y1="557.8" x2="186.8" y2="562.7" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="561.0" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="190.6" y1="554.4" x2="190.6" y2="564.3" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="563.1" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="194.4" y1="560.2" x2="194.4" y2="569.0" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="565.3" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="198.2" y1="556.9" x2="198.2" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="564.6" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="202.0" y1="564.3" x2="202.0" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="565.0" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="205.8" y1="560.9" x2="205.8" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="566.7" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="209.6" y1="558.8" x2="209.6" y2="572.2" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="559.0" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="213.3" y1="557.2" x2="213.3" y2="563.4" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="559.3" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="217.1" y1="558.3" x2="217.1" y2="570.9" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="558.8" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="220.9" y1="572.9" x2="220.9" y2="583.6" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="574.5" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="224.7" y1="575.4" x2="224.7" y2="581.9" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="575.5" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="228.5" y1="573.8" x2="228.5" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="574.4" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="232.3" y1="579.1" x2="232.3" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="579.7" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="236.1" y1="576.5" x2="236.1" y2="584.3" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="576.5" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="239.8" y1="567.2" x2="239.8" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="570.4" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="243.6" y1="564.8" x2="243.6" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="565.2" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="247.4" y1="560.2" x2="247.4" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="561.6" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="251.2" y1="560.8" x2="251.2" y2="570.8" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="561.0" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="255.0" y1="560.3" x2="255.0" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="561.6" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="258.8" y1="564.9" x2="258.8" y2="572.2" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="568.3" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="262.6" y1="572.0" x2="262.6" y2="582.5" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="573.1" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="266.4" y1="574.9" x2="266.4" y2="582.4" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="575.4" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="270.1" y1="574.4" x2="270.1" y2="584.3" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="575.2" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="273.9" y1="579.3" x2="273.9" y2="590.0" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="583.2" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="277.7" y1="587.0" x2="277.7" y2="592.6" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="588.4" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="281.5" y1="581.9" x2="281.5" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="590.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="285.3" y1="590.9" x2="285.3" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="590.9" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="289.1" y1="591.2" x2="289.1" y2="597.7" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="591.3" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="292.9" y1="587.2" x2="292.9" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="587.3" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="296.6" y1="586.1" x2="296.6" y2="594.5" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="588.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="300.4" y1="573.4" x2="300.4" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="574.0" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="304.2" y1="570.1" x2="304.2" y2="579.0" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="574.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="308.0" y1="571.5" x2="308.0" y2="577.5" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="574.1" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="311.8" y1="570.4" x2="311.8" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="573.3" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="315.6" y1="573.1" x2="315.6" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="573.9" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="319.4" y1="567.4" x2="319.4" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="575.8" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="323.1" y1="578.2" x2="323.1" y2="585.3" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="579.0" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="326.9" y1="582.8" x2="326.9" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="583.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="330.7" y1="578.4" x2="330.7" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="578.9" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="334.5" y1="571.8" x2="334.5" y2="577.8" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="572.1" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="338.3" y1="569.9" x2="338.3" y2="576.1" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="572.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="342.1" y1="565.0" x2="342.1" y2="571.3" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="566.1" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="345.9" y1="556.8" x2="345.9" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="560.4" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="349.6" y1="558.0" x2="349.6" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="562.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="353.4" y1="558.2" x2="353.4" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="562.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="357.2" y1="563.7" x2="357.2" y2="569.0" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="565.4" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="361.0" y1="562.5" x2="361.0" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="562.6" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="364.8" y1="560.3" x2="364.8" y2="567.6" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="562.3" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="368.6" y1="558.5" x2="368.6" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="560.4" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="372.4" y1="554.9" x2="372.4" y2="561.3" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="558.8" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="376.2" y1="554.1" x2="376.2" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="554.2" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="379.9" y1="554.6" x2="379.9" y2="562.4" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="555.1" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="383.7" y1="557.8" x2="383.7" y2="562.3" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="560.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="387.5" y1="559.0" x2="387.5" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="562.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="391.3" y1="562.5" x2="391.3" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="563.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="395.1" y1="562.4" x2="395.1" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="563.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="398.9" y1="562.7" x2="398.9" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="563.4" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="402.7" y1="554.3" x2="402.7" y2="565.0" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="555.4" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="406.4" y1="540.5" x2="406.4" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="541.2" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="410.2" y1="537.1" x2="410.2" y2="545.7" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="537.8" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="414.0" y1="539.8" x2="414.0" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="542.1" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="417.8" y1="533.0" x2="417.8" y2="540.4" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="535.9" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="421.6" y1="535.1" x2="421.6" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="536.2" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="425.4" y1="535.4" x2="425.4" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="535.9" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="429.2" y1="534.2" x2="429.2" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="535.2" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="432.9" y1="529.5" x2="432.9" y2="539.5" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="532.7" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="436.7" y1="528.4" x2="436.7" y2="537.0" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="532.5" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="440.5" y1="528.1" x2="440.5" y2="536.4" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="528.5" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="444.3" y1="527.5" x2="444.3" y2="536.5" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="527.9" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="448.1" y1="533.1" x2="448.1" y2="542.9" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="533.5" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="451.9" y1="538.3" x2="451.9" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="543.4" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="455.7" y1="536.3" x2="455.7" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="543.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="459.5" y1="534.6" x2="459.5" y2="543.0" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="535.5" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="463.2" y1="534.3" x2="463.2" y2="541.6" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="536.1" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="467.0" y1="538.6" x2="467.0" y2="544.7" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="538.7" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="470.8" y1="542.9" x2="470.8" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="545.3" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="474.6" y1="543.8" x2="474.6" y2="551.0" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="545.8" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="478.4" y1="543.4" x2="478.4" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="544.1" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="482.2" y1="539.1" x2="482.2" y2="546.6" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="545.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="486.0" y1="542.6" x2="486.0" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="544.7" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="489.7" y1="549.0" x2="489.7" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="551.4" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="493.5" y1="544.0" x2="493.5" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="545.0" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="497.3" y1="538.9" x2="497.3" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="539.3" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="501.1" y1="532.5" x2="501.1" y2="541.6" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="532.8" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="504.9" y1="529.9" x2="504.9" y2="534.2" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="532.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="508.7" y1="530.3" x2="508.7" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="533.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="512.5" y1="531.0" x2="512.5" y2="537.3" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="531.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="516.2" y1="515.7" x2="516.2" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="517.5" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="520.0" y1="516.0" x2="520.0" y2="522.1" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="516.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="523.8" y1="512.7" x2="523.8" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="515.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="527.6" y1="518.0" x2="527.6" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="518.2" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="531.4" y1="518.4" x2="531.4" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="520.2" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="535.2" y1="506.6" x2="535.2" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="506.8" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="539.0" y1="498.9" x2="539.0" y2="508.6" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="505.4" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="542.7" y1="506.3" x2="542.7" y2="513.2" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="507.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="546.5" y1="498.5" x2="546.5" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="498.8" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="550.3" y1="495.7" x2="550.3" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="498.9" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="554.1" y1="493.0" x2="554.1" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="496.9" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="557.9" y1="483.0" x2="557.9" y2="498.2" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="483.8" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="561.7" y1="471.9" x2="561.7" y2="488.0" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="482.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="565.5" y1="481.2" x2="565.5" y2="492.5" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="485.5" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="569.3" y1="481.6" x2="569.3" y2="496.6" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="484.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="573.0" y1="483.3" x2="573.0" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="484.8" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="576.8" y1="479.6" x2="576.8" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="484.2" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="580.6" y1="484.6" x2="580.6" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="487.2" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="584.4" y1="488.0" x2="584.4" y2="510.4" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="489.0" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="588.2" y1="491.0" x2="588.2" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="491.9" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="592.0" y1="489.1" x2="592.0" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="491.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="595.8" y1="486.8" x2="595.8" y2="491.8" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="488.9" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="599.5" y1="477.4" x2="599.5" y2="488.7" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="481.6" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="603.3" y1="470.3" x2="603.3" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="471.8" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="607.1" y1="466.7" x2="607.1" y2="481.4" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="469.1" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="610.9" y1="466.3" x2="610.9" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="469.0" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="614.7" y1="455.0" x2="614.7" y2="471.0" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="456.1" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="618.5" y1="448.0" x2="618.5" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="454.4" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="622.3" y1="456.7" x2="622.3" y2="465.9" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="460.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="626.0" y1="451.7" x2="626.0" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="453.7" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="629.8" y1="442.3" x2="629.8" y2="452.6" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="448.8" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="633.6" y1="445.5" x2="633.6" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="447.6" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="637.4" y1="460.9" x2="637.4" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="465.1" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="641.2" y1="470.9" x2="641.2" y2="499.9" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="474.4" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="645.0" y1="491.4" x2="645.0" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="493.0" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="648.8" y1="473.0" x2="648.8" y2="493.8" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="473.9" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="652.5" y1="467.8" x2="652.5" y2="477.9" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="471.4" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="656.3" y1="471.4" x2="656.3" y2="480.7" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="472.7" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="660.1" y1="478.5" x2="660.1" y2="501.3" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="478.5" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="663.9" y1="481.3" x2="663.9" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="481.7" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="667.7" y1="475.3" x2="667.7" y2="487.1" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="480.9" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="671.5" y1="466.2" x2="671.5" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="471.9" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="675.3" y1="471.1" x2="675.3" y2="481.4" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="472.3" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="679.1" y1="466.3" x2="679.1" y2="474.2" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="467.0" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="682.8" y1="462.5" x2="682.8" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="465.2" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="686.6" y1="469.0" x2="686.6" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="472.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="690.4" y1="466.1" x2="690.4" y2="484.6" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="472.6" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="694.2" y1="466.9" x2="694.2" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="468.9" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="698.0" y1="470.9" x2="698.0" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="470.9" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="701.8" y1="481.3" x2="701.8" y2="489.0" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="482.7" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="705.6" y1="479.4" x2="705.6" y2="490.4" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="480.9" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="709.3" y1="474.9" x2="709.3" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="478.4" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="713.1" y1="473.2" x2="713.1" y2="486.6" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="474.7" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="716.9" y1="469.3" x2="716.9" y2="487.0" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="473.6" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="720.7" y1="472.3" x2="720.7" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="475.8" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="724.5" y1="473.7" x2="724.5" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="474.1" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="728.3" y1="465.1" x2="728.3" y2="480.9" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="469.1" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="732.1" y1="467.7" x2="732.1" y2="483.8" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="468.1" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="735.8" y1="459.1" x2="735.8" y2="468.2" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="466.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="739.6" y1="474.2" x2="739.6" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="480.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="743.4" y1="475.5" x2="743.4" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="480.5" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="747.2" y1="473.6" x2="747.2" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="474.2" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="751.0" y1="465.7" x2="751.0" y2="475.9" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="472.2" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="754.8" y1="474.0" x2="754.8" y2="496.0" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="474.5" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="758.6" y1="488.1" x2="758.6" y2="503.5" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="488.5" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="762.4" y1="497.1" x2="762.4" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="497.5" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="766.1" y1="493.0" x2="766.1" y2="502.3" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="498.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="769.9" y1="492.4" x2="769.9" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="494.9" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="773.7" y1="506.8" x2="773.7" y2="541.9" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="514.3" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="777.5" y1="511.4" x2="777.5" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="522.7" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="781.3" y1="518.3" x2="781.3" y2="533.4" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="518.4" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="785.1" y1="510.8" x2="785.1" y2="535.6" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="511.9" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="788.9" y1="504.5" x2="788.9" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="505.9" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="792.6" y1="501.0" x2="792.6" y2="511.9" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="503.0" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="796.4" y1="481.1" x2="796.4" y2="493.0" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="484.1" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="800.2" y1="483.0" x2="800.2" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="488.7" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="804.0" y1="482.7" x2="804.0" y2="494.4" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="489.4" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="807.8" y1="476.3" x2="807.8" y2="490.9" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="479.3" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="811.6" y1="468.4" x2="811.6" y2="477.5" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="476.3" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="815.4" y1="468.0" x2="815.4" y2="475.0" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="472.1" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="819.1" y1="456.5" x2="819.1" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="458.3" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="822.9" y1="453.2" x2="822.9" y2="463.1" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="454.1" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="826.7" y1="450.9" x2="826.7" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="452.0" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="830.5" y1="448.1" x2="830.5" y2="457.7" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="450.5" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="834.3" y1="447.4" x2="834.3" y2="457.5" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="449.6" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="838.1" y1="446.9" x2="838.1" y2="463.6" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="451.7" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="841.9" y1="451.8" x2="841.9" y2="461.2" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="452.8" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="845.6" y1="443.3" x2="845.6" y2="453.5" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="449.7" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="849.4" y1="447.0" x2="849.4" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="449.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="853.2" y1="444.1" x2="853.2" y2="454.1" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="449.5" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="857.0" y1="448.0" x2="857.0" y2="460.1" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="449.3" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="860.8" y1="438.1" x2="860.8" y2="448.7" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="439.4" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="864.6" y1="426.5" x2="864.6" y2="440.3" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="429.8" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="868.4" y1="423.9" x2="868.4" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="426.8" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="872.2" y1="411.1" x2="872.2" y2="427.5" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="415.3" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="875.9" y1="402.9" x2="875.9" y2="422.7" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="404.1" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="879.7" y1="403.0" x2="879.7" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="407.2" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="883.5" y1="397.1" x2="883.5" y2="416.8" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="399.0" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="887.3" y1="381.7" x2="887.3" y2="394.6" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="388.5" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="891.1" y1="383.3" x2="891.1" y2="410.9" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="383.8" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="894.9" y1="390.6" x2="894.9" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="392.3" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="898.7" y1="402.7" x2="898.7" y2="432.8" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="408.1" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="902.4" y1="396.8" x2="902.4" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="397.0" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="906.2" y1="382.4" x2="906.2" y2="401.3" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="385.8" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="910.0" y1="377.7" x2="910.0" y2="397.9" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="383.2" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="913.8" y1="392.8" x2="913.8" y2="411.2" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="394.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="917.6" y1="388.3" x2="917.6" y2="394.2" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="389.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="921.4" y1="380.7" x2="921.4" y2="394.6" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="382.8" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="925.2" y1="369.9" x2="925.2" y2="382.5" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="371.5" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="928.9" y1="356.2" x2="928.9" y2="374.5" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="359.6" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="932.7" y1="348.7" x2="932.7" y2="366.2" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="358.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="936.5" y1="340.5" x2="936.5" y2="361.5" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="356.6" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="940.3" y1="346.6" x2="940.3" y2="378.9" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="354.5" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="944.1" y1="340.0" x2="944.1" y2="358.7" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="350.8" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="947.9" y1="343.8" x2="947.9" y2="359.6" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="345.7" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="951.7" y1="335.9" x2="951.7" y2="356.2" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="346.2" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="955.5" y1="350.6" x2="955.5" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="359.9" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="959.2" y1="355.8" x2="959.2" y2="382.9" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="371.2" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="963.0" y1="360.1" x2="963.0" y2="375.3" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="362.9" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="966.8" y1="355.5" x2="966.8" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="363.8" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="970.6" y1="360.9" x2="970.6" y2="394.5" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="363.5" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="974.4" y1="316.6" x2="974.4" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="319.7" width="2.35" height="40.3" fill="var(--up)"/>
<line x1="978.2" y1="292.0" x2="978.2" y2="321.8" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="292.0" width="2.35" height="28.3" fill="var(--up)"/>
<line x1="982.0" y1="250.3" x2="982.0" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="252.3" width="2.35" height="37.7" fill="var(--up)"/>
<line x1="985.7" y1="247.8" x2="985.7" y2="279.2" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="249.0" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="989.5" y1="200.0" x2="989.5" y2="255.8" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="200.0" width="2.35" height="46.4" fill="var(--up)"/>
<line x1="993.3" y1="184.9" x2="993.3" y2="221.3" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="195.9" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="997.1" y1="178.1" x2="997.1" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="182.3" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="1000.9" y1="144.5" x2="1000.9" y2="172.0" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="156.3" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="1004.7" y1="107.9" x2="1004.7" y2="181.7" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="161.4" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="1008.5" y1="128.0" x2="1008.5" y2="199.3" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="133.9" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="1012.2" y1="88.7" x2="1012.2" y2="137.2" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="93.6" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="1016.0" y1="80.7" x2="1016.0" y2="144.5" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="82.7" width="2.35" height="58.2" fill="var(--down)"/>
<line x1="1019.8" y1="94.0" x2="1019.8" y2="175.2" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="139.2" width="2.35" height="25.5" fill="var(--down)"/>
<line x1="1023.6" y1="138.8" x2="1023.6" y2="192.4" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="150.6" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="1027.4" y1="155.6" x2="1027.4" y2="224.1" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="167.4" width="2.35" height="36.9" fill="var(--down)"/>
<line x1="1031.2" y1="168.9" x2="1031.2" y2="202.7" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="192.7" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="1035.0" y1="192.8" x2="1035.0" y2="255.2" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="195.3" width="2.35" height="24.0" fill="var(--down)"/>
<line x1="1038.7" y1="173.1" x2="1038.7" y2="235.4" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="175.9" width="2.35" height="54.3" fill="var(--up)"/>
<line x1="1042.5" y1="161.5" x2="1042.5" y2="191.0" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="173.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1046.3" y1="158.8" x2="1046.3" y2="206.0" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="165.2" width="2.35" height="36.3" fill="var(--down)"/>
<line x1="1050.1" y1="193.1" x2="1050.1" y2="206.0" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="194.8" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="60" y1="510.4" x2="1052" y2="510.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="504.4" font-size="11.5" fill="var(--support)" font-weight="600">4,289.18 S1</text>
<text x="1058" y="516.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="547.4" x2="1052" y2="547.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="541.4" font-size="11.5" fill="var(--support)" font-weight="600">3,396.99 S2</text>
<text x="1058" y="553.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="557.4" x2="1052" y2="557.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="551.4" font-size="11.5" fill="var(--support)" font-weight="600">3,154.61 S3</text>
<text x="1058" y="563.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="201.5" r="3" fill="var(--ink)"/>
<text x="1046.0" y="193.5" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 11,740.37 (2026-08-21)</text>
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

- **상승**: 반도체 업황 사이클이 확장 국면(수요 회복, 재고 조정 마무리 등)에 들어섰다는 신호로 흔히 해석한다.
- **하락**: 반도체 업황이 둔화(수요 위축, 재고 과잉)될 것이라는 우려 신호로 흔히 해석한다.
- 시가총액을 기준으로 비중을 매기는 지수라서, 비중 상위 회원사 몇 곳의 움직임이 지수 전체를 좌우할 수 있다 — 지수가 움직였다고 "반도체 업황 전체"가 그렇다고 곧바로 일반화하지 말고, 그 시점에 지수에서 비중이 큰 종목이 무엇인지 함께 확인한다.
- **왜 반도체는 사이클을 타나**: 반도체 공장(팹) 하나를 새로 짓거나 늘리는 데는 보통 1~2년이라는 긴 시간이 걸린다. 그래서 공급이 수요 변화에 곧바로 맞춰 움직이지 못한다 — 수요가 몰리면 공급이 부족해지고(붐), 그 뒤 너도나도 투자를 늘리면 다시 재고가 쌓이는(버스트) 일이 반복되는 구조다. 이 지수는 설계(EDA)·파운드리(위탁생산)·장비·메모리 등 반도체 밸류체인 전반을 담고 있어 이런 사이클을 보여주는 대표 지표로 쓰인다.

---

## 관련 문서

- [반도체 설계 자동화 (EDA) 섹터 개요](../../../sectors/electronic_design_automation/00_overview.md)
- [반도체 테스트 장비 (ATE) 섹터 개요](../../../sectors/automated_test_equipment/00_overview.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md)
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — PHLX Semiconductor (^SOX)](https://finance.yahoo.com/quote/%5ESOX/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-25)*
