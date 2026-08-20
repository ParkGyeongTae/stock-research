# 필라델피아 반도체지수 (SOX) — 기술적 참고 (주봉 5년)

> 최근 5년 필라델피아 반도체지수(`^SOX`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다른 macro 문서(원달러·국채금리 등)와 달리 이 지표는 **범용 거시지표가 아니라 이 레포의 특정 섹터 벤치마크**다 — [`sectors/electronic_design_automation/`](../../../sectors/electronic_design_automation/00_overview.md)(EDA)·[`sectors/automated_test_equipment/`](../../../sectors/automated_test_equipment/00_overview.md)(ATE) 소속 회사가 개별 종목의 주가 흐름을 **섹터 전체 대비**로 볼 때 인용한다.
>
> **어떻게 쓰나**: 개별 회사 주가가 SOX 대비 초과 상승/하락하고 있다면, 그 회사 고유의 이슈(펀더멘털)인지 반도체 업황 전체(사이클)의 문제인지 구분하는 첫 단서가 된다. 두 09/10_technical_*.md(개별 회사 차트)와 이 문서를 같은 기간으로 나란히 보는 방식을 권한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="sox-chart">
<style>
.sox-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .sox-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-19 · 마지막 종가 11,738.23 (2026-08-19) · 단위 지수</text>
<line x1="60" y1="605.3" x2="1052" y2="605.3" class="grid"/>
<text x="52" y="609.3" font-size="11" text-anchor="end" fill="var(--muted)">2,000</text>
<line x1="60" y1="522.4" x2="1052" y2="522.4" class="grid"/>
<text x="52" y="526.4" font-size="11" text-anchor="end" fill="var(--muted)">4,000</text>
<line x1="60" y1="439.5" x2="1052" y2="439.5" class="grid"/>
<text x="52" y="443.5" font-size="11" text-anchor="end" fill="var(--muted)">6,000</text>
<line x1="60" y1="356.5" x2="1052" y2="356.5" class="grid"/>
<text x="52" y="360.5" font-size="11" text-anchor="end" fill="var(--muted)">8,000</text>
<line x1="60" y1="273.6" x2="1052" y2="273.6" class="grid"/>
<text x="52" y="277.6" font-size="11" text-anchor="end" fill="var(--muted)">10,000</text>
<line x1="60" y1="190.7" x2="1052" y2="190.7" class="grid"/>
<text x="52" y="194.7" font-size="11" text-anchor="end" fill="var(--muted)">12,000</text>
<line x1="60" y1="107.8" x2="1052" y2="107.8" class="grid"/>
<text x="52" y="111.8" font-size="11" text-anchor="end" fill="var(--muted)">14,000</text>
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
<line x1="61.9" y1="552.9" x2="61.9" y2="556.9" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="553.2" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="65.7" y1="545.5" x2="65.7" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="545.7" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="69.4" y1="544.0" x2="69.4" y2="547.6" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="544.7" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="73.2" y1="544.4" x2="73.2" y2="549.3" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="545.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="77.0" y1="543.7" x2="77.0" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="545.1" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="80.7" y1="544.4" x2="80.7" y2="551.8" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="545.0" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="84.5" y1="544.8" x2="84.5" y2="555.2" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="546.5" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="88.3" y1="550.6" x2="88.3" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="553.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="92.1" y1="550.3" x2="92.1" y2="557.0" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="550.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="95.8" y1="546.1" x2="95.8" y2="552.3" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="548.5" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="99.6" y1="545.0" x2="99.6" y2="549.2" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="545.1" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="103.4" y1="531.1" x2="103.4" y2="545.1" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="532.5" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="107.1" y1="529.1" x2="107.1" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="530.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="110.9" y1="525.0" x2="110.9" y2="532.3" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="526.0" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="114.7" y1="523.1" x2="114.7" y2="533.3" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="525.3" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="118.5" y1="524.1" x2="118.5" y2="533.0" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="529.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="122.2" y1="522.3" x2="122.2" y2="535.3" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="525.9" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="126.0" y1="523.9" x2="126.0" y2="533.9" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="525.2" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="129.8" y1="524.2" x2="129.8" y2="535.2" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="525.2" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="133.6" y1="520.1" x2="133.6" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="524.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="137.3" y1="519.5" x2="137.3" y2="531.2" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="523.4" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="141.1" y1="522.7" x2="141.1" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="526.5" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="144.9" y1="529.0" x2="144.9" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="529.0" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="148.6" y1="541.4" x2="148.6" y2="557.7" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="548.8" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="152.4" y1="538.9" x2="152.4" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="545.0" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="156.2" y1="535.9" x2="156.2" y2="549.6" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="544.3" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="160.0" y1="540.3" x2="160.0" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="547.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="163.7" y1="545.0" x2="163.7" y2="557.5" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="545.1" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="167.5" y1="544.7" x2="167.5" y2="554.7" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="546.6" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="171.3" y1="551.2" x2="171.3" y2="561.0" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="552.5" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="175.0" y1="545.4" x2="175.0" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="545.9" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="178.8" y1="541.6" x2="178.8" y2="548.9" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="542.0" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="182.6" y1="537.6" x2="182.6" y2="550.6" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="543.0" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="186.4" y1="546.0" x2="186.4" y2="559.0" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="548.0" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="190.1" y1="557.8" x2="190.1" y2="562.7" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="561.0" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="193.9" y1="554.4" x2="193.9" y2="564.3" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="563.1" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="197.7" y1="560.2" x2="197.7" y2="569.0" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="565.3" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="201.4" y1="556.9" x2="201.4" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="564.6" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="205.2" y1="564.3" x2="205.2" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="565.0" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="209.0" y1="560.9" x2="209.0" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="566.7" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="212.8" y1="558.8" x2="212.8" y2="572.2" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="559.0" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="216.5" y1="557.2" x2="216.5" y2="563.4" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="559.3" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="220.3" y1="558.3" x2="220.3" y2="570.9" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="558.8" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="224.1" y1="572.9" x2="224.1" y2="583.6" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="574.5" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="227.8" y1="575.4" x2="227.8" y2="581.9" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="575.5" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="231.6" y1="573.8" x2="231.6" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="574.4" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="235.4" y1="579.1" x2="235.4" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="579.7" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="239.2" y1="576.5" x2="239.2" y2="584.3" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="576.5" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="242.9" y1="567.2" x2="242.9" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="570.4" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="246.7" y1="564.8" x2="246.7" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="565.2" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="250.5" y1="560.2" x2="250.5" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="561.6" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="254.3" y1="560.8" x2="254.3" y2="570.8" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="561.0" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="258.0" y1="560.3" x2="258.0" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="561.6" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="261.8" y1="564.9" x2="261.8" y2="572.2" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="568.3" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="265.6" y1="572.0" x2="265.6" y2="582.5" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="573.1" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="269.3" y1="574.9" x2="269.3" y2="582.4" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="575.4" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="273.1" y1="574.4" x2="273.1" y2="584.3" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="575.2" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="276.9" y1="579.3" x2="276.9" y2="590.0" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="583.2" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="280.7" y1="587.0" x2="280.7" y2="592.6" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="588.4" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="284.4" y1="581.9" x2="284.4" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="590.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="288.2" y1="590.9" x2="288.2" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="590.9" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="292.0" y1="591.2" x2="292.0" y2="597.7" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="591.3" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="295.7" y1="587.2" x2="295.7" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="587.3" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="299.5" y1="586.1" x2="299.5" y2="594.5" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="588.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="303.3" y1="573.4" x2="303.3" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="574.0" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="307.1" y1="570.1" x2="307.1" y2="579.0" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="574.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="310.8" y1="571.5" x2="310.8" y2="577.5" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="574.1" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="314.6" y1="570.4" x2="314.6" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="573.3" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="318.4" y1="573.1" x2="318.4" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="573.9" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="322.1" y1="567.4" x2="322.1" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="575.8" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="325.9" y1="578.2" x2="325.9" y2="585.3" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="579.0" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="329.7" y1="582.8" x2="329.7" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="583.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="333.5" y1="578.4" x2="333.5" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="578.9" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="337.2" y1="571.8" x2="337.2" y2="577.8" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="572.1" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="341.0" y1="569.9" x2="341.0" y2="576.1" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="572.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="344.8" y1="565.0" x2="344.8" y2="571.3" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="566.1" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="348.5" y1="556.8" x2="348.5" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="560.4" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="352.3" y1="558.0" x2="352.3" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="562.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="356.1" y1="558.2" x2="356.1" y2="564.6" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="562.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="359.9" y1="563.7" x2="359.9" y2="569.0" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="565.4" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="363.6" y1="562.5" x2="363.6" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="562.6" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="367.4" y1="560.3" x2="367.4" y2="567.6" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="562.3" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="371.2" y1="558.5" x2="371.2" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="560.4" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="375.0" y1="554.9" x2="375.0" y2="561.3" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="558.8" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="378.7" y1="554.1" x2="378.7" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="554.2" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="382.5" y1="554.6" x2="382.5" y2="562.4" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="555.1" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="386.3" y1="557.8" x2="386.3" y2="562.3" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="560.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="390.0" y1="559.0" x2="390.0" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="562.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="393.8" y1="562.5" x2="393.8" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="563.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="397.6" y1="562.4" x2="397.6" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="563.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="401.4" y1="562.7" x2="401.4" y2="566.1" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="563.4" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="405.1" y1="554.3" x2="405.1" y2="565.0" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="555.4" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="408.9" y1="540.5" x2="408.9" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="541.2" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="412.7" y1="537.1" x2="412.7" y2="545.7" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="537.8" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="416.4" y1="539.8" x2="416.4" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="542.1" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="420.2" y1="533.0" x2="420.2" y2="540.4" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="535.9" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="424.0" y1="535.1" x2="424.0" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="536.2" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="427.8" y1="535.4" x2="427.8" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="535.9" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="431.5" y1="534.2" x2="431.5" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="535.2" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="435.3" y1="529.5" x2="435.3" y2="539.5" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="532.7" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="439.1" y1="528.4" x2="439.1" y2="537.0" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="532.5" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="442.8" y1="528.1" x2="442.8" y2="536.4" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="528.5" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="446.6" y1="527.5" x2="446.6" y2="536.5" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="527.9" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="450.4" y1="533.1" x2="450.4" y2="542.9" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="533.5" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="454.2" y1="538.3" x2="454.2" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="543.4" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="457.9" y1="536.3" x2="457.9" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="543.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="461.7" y1="534.6" x2="461.7" y2="543.0" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="535.5" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="465.5" y1="534.3" x2="465.5" y2="541.6" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="536.1" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="469.2" y1="538.6" x2="469.2" y2="544.7" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="538.7" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="473.0" y1="542.9" x2="473.0" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="545.3" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="476.8" y1="543.8" x2="476.8" y2="551.0" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="545.8" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="480.6" y1="543.4" x2="480.6" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="544.1" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="484.3" y1="539.1" x2="484.3" y2="546.6" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="545.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="488.1" y1="542.6" x2="488.1" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="544.7" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="491.9" y1="549.0" x2="491.9" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="551.4" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="495.7" y1="544.0" x2="495.7" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="545.0" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="499.4" y1="538.9" x2="499.4" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="539.3" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="503.2" y1="532.5" x2="503.2" y2="541.6" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="532.8" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="507.0" y1="529.9" x2="507.0" y2="534.2" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="532.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="510.7" y1="530.3" x2="510.7" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="533.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="514.5" y1="531.0" x2="514.5" y2="537.3" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="531.7" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="518.3" y1="515.7" x2="518.3" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="517.5" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="522.1" y1="516.0" x2="522.1" y2="522.1" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="516.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="525.8" y1="512.7" x2="525.8" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="515.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="529.6" y1="518.0" x2="529.6" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="518.2" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="533.4" y1="518.4" x2="533.4" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="520.2" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="537.1" y1="506.6" x2="537.1" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="506.8" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="540.9" y1="498.9" x2="540.9" y2="508.6" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="505.4" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="544.7" y1="506.3" x2="544.7" y2="513.2" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="507.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="548.5" y1="498.5" x2="548.5" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="498.8" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="552.2" y1="495.7" x2="552.2" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="498.9" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="556.0" y1="493.0" x2="556.0" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="496.9" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="559.8" y1="483.0" x2="559.8" y2="498.2" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="483.8" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="563.5" y1="471.9" x2="563.5" y2="488.0" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="482.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="567.3" y1="481.2" x2="567.3" y2="492.5" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="485.5" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="571.1" y1="481.6" x2="571.1" y2="496.6" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="484.7" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="574.9" y1="483.3" x2="574.9" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="484.8" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="578.6" y1="479.6" x2="578.6" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="484.2" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="582.4" y1="484.6" x2="582.4" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="487.2" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="586.2" y1="488.0" x2="586.2" y2="510.4" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="489.0" width="2.34" height="20.6" fill="var(--down)"/>
<line x1="589.9" y1="491.0" x2="589.9" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="491.9" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="593.7" y1="489.1" x2="593.7" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="491.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="597.5" y1="486.8" x2="597.5" y2="491.8" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="488.9" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="601.3" y1="477.4" x2="601.3" y2="488.7" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="481.6" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="605.0" y1="470.3" x2="605.0" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="471.8" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="608.8" y1="466.7" x2="608.8" y2="481.4" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="469.1" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="612.6" y1="466.3" x2="612.6" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="469.0" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="616.3" y1="455.0" x2="616.3" y2="471.0" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="456.1" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="620.1" y1="448.0" x2="620.1" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="454.4" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="623.9" y1="456.7" x2="623.9" y2="465.9" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="460.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="627.7" y1="451.7" x2="627.7" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="453.7" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="631.4" y1="442.3" x2="631.4" y2="452.6" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="448.8" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="635.2" y1="445.5" x2="635.2" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="447.6" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="639.0" y1="460.9" x2="639.0" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="465.1" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="642.8" y1="470.9" x2="642.8" y2="499.9" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="474.4" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="646.5" y1="491.4" x2="646.5" y2="510.3" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="493.0" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="650.3" y1="473.0" x2="650.3" y2="493.8" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="473.9" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="654.1" y1="467.8" x2="654.1" y2="477.9" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="471.4" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="657.8" y1="471.4" x2="657.8" y2="480.7" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="472.7" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="661.6" y1="478.5" x2="661.6" y2="501.3" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="478.5" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="665.4" y1="481.3" x2="665.4" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="481.7" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="669.2" y1="475.3" x2="669.2" y2="487.1" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="480.9" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="672.9" y1="466.2" x2="672.9" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="471.9" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="676.7" y1="471.1" x2="676.7" y2="481.4" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="472.3" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="680.5" y1="466.3" x2="680.5" y2="474.2" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="467.0" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="684.2" y1="462.5" x2="684.2" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="465.2" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="688.0" y1="469.0" x2="688.0" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="472.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="691.8" y1="466.1" x2="691.8" y2="484.6" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="472.6" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="695.6" y1="466.9" x2="695.6" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="468.9" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="699.3" y1="470.9" x2="699.3" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="470.9" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="703.1" y1="481.3" x2="703.1" y2="489.0" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="482.7" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="706.9" y1="479.4" x2="706.9" y2="490.4" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="480.9" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="710.6" y1="474.9" x2="710.6" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="478.4" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="714.4" y1="473.2" x2="714.4" y2="486.6" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="474.7" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="718.2" y1="469.3" x2="718.2" y2="487.0" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="473.6" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="722.0" y1="472.3" x2="722.0" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="475.8" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="725.7" y1="473.7" x2="725.7" y2="482.5" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="474.1" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="729.5" y1="465.1" x2="729.5" y2="480.9" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="469.1" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="733.3" y1="467.7" x2="733.3" y2="483.8" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="468.1" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="737.0" y1="459.1" x2="737.0" y2="468.2" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="466.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="740.8" y1="474.2" x2="740.8" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="480.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="744.6" y1="475.5" x2="744.6" y2="487.2" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="480.5" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="748.4" y1="473.6" x2="748.4" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="474.2" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="752.1" y1="465.7" x2="752.1" y2="475.9" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="472.2" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="755.9" y1="474.0" x2="755.9" y2="496.0" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="474.5" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="759.7" y1="488.1" x2="759.7" y2="503.5" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="488.5" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="763.5" y1="497.1" x2="763.5" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="497.5" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="767.2" y1="493.0" x2="767.2" y2="502.3" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="498.0" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="771.0" y1="492.4" x2="771.0" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="494.9" width="2.34" height="15.7" fill="var(--down)"/>
<line x1="774.8" y1="506.8" x2="774.8" y2="541.9" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="514.3" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="778.5" y1="511.4" x2="778.5" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="522.7" width="2.34" height="22.0" fill="var(--up)"/>
<line x1="782.3" y1="518.3" x2="782.3" y2="533.4" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="518.4" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="786.1" y1="510.8" x2="786.1" y2="535.6" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="511.9" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="789.9" y1="504.5" x2="789.9" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="505.9" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="793.6" y1="501.0" x2="793.6" y2="511.9" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="503.0" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="797.4" y1="481.1" x2="797.4" y2="493.0" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="484.1" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="801.2" y1="483.0" x2="801.2" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="488.7" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="804.9" y1="482.7" x2="804.9" y2="494.4" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="489.4" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="808.7" y1="476.3" x2="808.7" y2="490.9" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="479.3" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="812.5" y1="468.4" x2="812.5" y2="477.5" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="476.3" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="816.3" y1="468.0" x2="816.3" y2="475.0" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="472.1" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="820.0" y1="456.5" x2="820.0" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="458.3" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="823.8" y1="453.2" x2="823.8" y2="463.1" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="454.1" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="827.6" y1="450.9" x2="827.6" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="452.0" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="831.3" y1="448.1" x2="831.3" y2="457.7" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="450.5" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="835.1" y1="447.4" x2="835.1" y2="457.5" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="449.6" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="838.9" y1="446.9" x2="838.9" y2="463.6" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="451.7" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="842.7" y1="451.8" x2="842.7" y2="461.2" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="452.8" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="846.4" y1="443.3" x2="846.4" y2="453.5" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="449.7" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="850.2" y1="447.0" x2="850.2" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="449.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="854.0" y1="444.1" x2="854.0" y2="454.1" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="449.5" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="857.7" y1="448.0" x2="857.7" y2="460.1" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="449.3" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="861.5" y1="438.1" x2="861.5" y2="448.7" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="439.4" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="865.3" y1="426.5" x2="865.3" y2="440.3" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="429.8" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="869.1" y1="423.9" x2="869.1" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="426.8" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="872.8" y1="411.1" x2="872.8" y2="427.5" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="415.3" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="876.6" y1="402.9" x2="876.6" y2="422.7" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="404.1" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="880.4" y1="403.0" x2="880.4" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="407.2" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="884.2" y1="397.1" x2="884.2" y2="416.8" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="399.0" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="887.9" y1="381.7" x2="887.9" y2="394.6" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="388.5" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="891.7" y1="383.3" x2="891.7" y2="410.9" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="383.8" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="895.5" y1="390.6" x2="895.5" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="392.3" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="899.2" y1="402.7" x2="899.2" y2="432.8" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="408.1" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="903.0" y1="396.8" x2="903.0" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="397.0" width="2.34" height="22.0" fill="var(--up)"/>
<line x1="906.8" y1="382.4" x2="906.8" y2="401.3" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="385.8" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="910.6" y1="377.7" x2="910.6" y2="397.9" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="383.2" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="914.3" y1="392.8" x2="914.3" y2="411.2" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="394.0" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="918.1" y1="388.3" x2="918.1" y2="394.2" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="389.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="921.9" y1="380.7" x2="921.9" y2="394.6" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="382.8" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="925.6" y1="369.9" x2="925.6" y2="382.5" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="371.5" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="929.4" y1="356.2" x2="929.4" y2="374.5" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="359.6" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="933.2" y1="348.7" x2="933.2" y2="366.2" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="358.3" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="937.0" y1="340.5" x2="937.0" y2="361.5" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="356.6" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="940.7" y1="346.6" x2="940.7" y2="378.9" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="354.5" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="944.5" y1="340.0" x2="944.5" y2="358.7" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="350.8" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="948.3" y1="343.8" x2="948.3" y2="359.6" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="345.7" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="952.0" y1="335.9" x2="952.0" y2="356.2" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="346.2" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="955.8" y1="350.6" x2="955.8" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="359.9" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="959.6" y1="355.8" x2="959.6" y2="382.9" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="371.2" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="963.4" y1="360.1" x2="963.4" y2="375.3" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="362.9" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="967.1" y1="355.5" x2="967.1" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="363.8" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="970.9" y1="360.9" x2="970.9" y2="394.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="363.5" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="974.7" y1="316.6" x2="974.7" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="319.7" width="2.34" height="40.3" fill="var(--up)"/>
<line x1="978.4" y1="292.0" x2="978.4" y2="321.8" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="292.0" width="2.34" height="28.3" fill="var(--up)"/>
<line x1="982.2" y1="250.3" x2="982.2" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="252.3" width="2.34" height="37.7" fill="var(--up)"/>
<line x1="986.0" y1="247.8" x2="986.0" y2="279.2" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="249.0" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="989.8" y1="200.0" x2="989.8" y2="255.8" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="200.0" width="2.34" height="46.4" fill="var(--up)"/>
<line x1="993.5" y1="184.9" x2="993.5" y2="221.3" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="195.9" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="997.3" y1="178.1" x2="997.3" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="182.3" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="1001.1" y1="144.5" x2="1001.1" y2="172.0" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="156.3" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="1004.9" y1="107.9" x2="1004.9" y2="181.7" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="161.4" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="1008.6" y1="128.0" x2="1008.6" y2="199.3" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="133.9" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="1012.4" y1="88.7" x2="1012.4" y2="137.2" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="93.6" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="1016.2" y1="80.7" x2="1016.2" y2="144.5" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="82.7" width="2.34" height="58.2" fill="var(--down)"/>
<line x1="1019.9" y1="94.0" x2="1019.9" y2="175.2" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="139.2" width="2.34" height="25.5" fill="var(--down)"/>
<line x1="1023.7" y1="138.8" x2="1023.7" y2="192.4" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="150.6" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="1027.5" y1="155.6" x2="1027.5" y2="224.1" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="167.4" width="2.34" height="36.9" fill="var(--down)"/>
<line x1="1031.3" y1="168.9" x2="1031.3" y2="202.7" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="192.7" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="1035.0" y1="192.8" x2="1035.0" y2="255.2" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="195.3" width="2.34" height="24.0" fill="var(--down)"/>
<line x1="1038.8" y1="173.1" x2="1038.8" y2="235.4" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="175.9" width="2.34" height="54.3" fill="var(--up)"/>
<line x1="1042.6" y1="161.5" x2="1042.6" y2="191.0" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="173.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1046.3" y1="158.8" x2="1046.3" y2="205.9" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="165.2" width="2.34" height="36.4" fill="var(--down)"/>
<line x1="1050.1" y1="185.0" x2="1050.1" y2="205.9" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="188.1" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="60" y1="510.4" x2="1052" y2="510.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="504.4" font-size="11.5" fill="var(--support)" font-weight="600">4,289 S1</text>
<text x="1058" y="516.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="547.4" x2="1052" y2="547.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="541.4" font-size="11.5" fill="var(--support)" font-weight="600">3,397 S2</text>
<text x="1058" y="553.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="557.4" x2="1052" y2="557.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="551.4" font-size="11.5" fill="var(--support)" font-weight="600">3,155 S3</text>
<text x="1058" y="563.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="201.6" r="3" fill="var(--ink)"/>
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

- **상승**: 반도체 업황 사이클 확장 기대(수요 회복, 재고 조정 마무리 등) 신호로 흔히 해석된다.
- **하락**: 반도체 업황 둔화 우려(수요 위축, 재고 과잉) 신호로 흔히 해석된다.
- 시가총액 가중 지수라 대형 회원사(엔비디아 등) 몇 곳의 움직임이 지수 전체를 좌우할 수 있다 — "반도체 업황 전체"로 곧장 일반화하지 말고 지수 구성 상위 종목의 비중을 함께 확인한다.

---

## 관련 문서

- [반도체 설계 자동화 (EDA) 섹터 개요](../../../sectors/electronic_design_automation/00_overview.md)
- [반도체 테스트 장비 (ATE) 섹터 개요](../../../sectors/automated_test_equipment/00_overview.md)
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — PHLX Semiconductor (^SOX)](https://finance.yahoo.com/quote/%5ESOX/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
