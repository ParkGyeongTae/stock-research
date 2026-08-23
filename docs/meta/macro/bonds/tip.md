# 물가연동국채 ETF (TIP)

!!! note ""
    최근 5년간 iShares 물가연동국채(TIPS) ETF(`TIP`)의 주간 가격을 지지선·저항선과 함께 정리한 참고 자료다. TIPS는 원금이 소비자물가지수(CPI)에 맞춰 자동으로 조정되는 국채다. TLT(명목 장기국채, 물가에 연동되지 않는 일반 국채) 대비 이 ETF가 상대적으로 강한지 약한지를 보면, 시장이 앞으로의 물가 상승(기대인플레이션)을 어느 방향으로 예상하는지 대략 가늠할 수 있다.

    ⚠️ **정밀한 기대인플레이션(breakeven inflation, BEI) 수치는 아니다** — 실제 BEI는 만기가 같은 명목채와 물가연동채의 수익률을 서로 빼서 계산하는데(예: FRED `T10YIE`), 이 문서는 그런 계산을 하지 않는다. 이 문서는 TLT와 비교했을 때 방향이 어느 쪽인지 대략적으로만 참고하는 용도로 쓴다.

---

## 1. 차트 — 최근 5년 주봉

<div class="tip-chart">
<style>
.tip-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .tip-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .tip-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.tip-chart svg { width:100%; height:auto; display:block; }
.tip-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.tip-chart .title { fill: var(--ink); font-weight:600; }
.tip-chart .grid { stroke: var(--grid); stroke-width:1; }
.tip-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="물가연동국채 ETF(TIP) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">물가연동국채 ETF (TIP) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 $107.13 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="545.8" x2="1052" y2="545.8" class="grid"/>
<text x="52" y="549.8" font-size="11" text-anchor="end" fill="var(--muted)">105.00</text>
<line x1="60" y1="456.8" x2="1052" y2="456.8" class="grid"/>
<text x="52" y="460.8" font-size="11" text-anchor="end" fill="var(--muted)">110.00</text>
<line x1="60" y1="367.7" x2="1052" y2="367.7" class="grid"/>
<text x="52" y="371.7" font-size="11" text-anchor="end" fill="var(--muted)">115.00</text>
<line x1="60" y1="278.7" x2="1052" y2="278.7" class="grid"/>
<text x="52" y="282.7" font-size="11" text-anchor="end" fill="var(--muted)">120.00</text>
<line x1="60" y1="189.6" x2="1052" y2="189.6" class="grid"/>
<text x="52" y="193.6" font-size="11" text-anchor="end" fill="var(--muted)">125.00</text>
<line x1="60" y1="100.5" x2="1052" y2="100.5" class="grid"/>
<text x="52" y="104.5" font-size="11" text-anchor="end" fill="var(--muted)">130.00</text>
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
<line x1="61.9" y1="100.4" x2="61.9" y2="120.5" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="100.7" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="65.7" y1="96.6" x2="65.7" y2="128.9" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="97.9" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="69.5" y1="108.9" x2="69.5" y2="132.1" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="115.9" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="73.3" y1="109.1" x2="73.3" y2="124.8" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="110.1" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="77.0" y1="119.4" x2="77.0" y2="141.5" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="120.8" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="80.8" y1="135.3" x2="80.8" y2="146.8" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="139.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="84.6" y1="135.4" x2="84.6" y2="145.4" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="140.1" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="88.4" y1="121.2" x2="88.4" y2="142.0" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="126.2" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="92.2" y1="120.5" x2="92.2" y2="139.0" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="122.6" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="96.0" y1="96.6" x2="96.0" y2="133.7" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="122.4" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="99.8" y1="104.5" x2="99.8" y2="138.6" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="106.4" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="103.5" y1="76.1" x2="103.5" y2="104.3" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="93.1" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="107.3" y1="83.4" x2="107.3" y2="100.5" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="90.7" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="111.1" y1="102.7" x2="111.1" y2="128.5" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="103.4" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="114.9" y1="96.6" x2="114.9" y2="126.0" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="105.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="118.7" y1="101.6" x2="118.7" y2="126.5" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="103.2" width="2.35" height="22.6" fill="var(--down)"/>
<line x1="122.5" y1="116.4" x2="122.5" y2="143.8" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="121.4" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="126.3" y1="123.5" x2="126.3" y2="143.3" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="132.1" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="130.0" y1="111.9" x2="130.0" y2="135.8" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="114.8" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="133.8" y1="123.5" x2="133.8" y2="171.8" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="123.9" width="2.35" height="43.8" fill="var(--down)"/>
<line x1="137.6" y1="149.0" x2="137.6" y2="174.5" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="171.2" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="141.4" y1="170.9" x2="141.4" y2="188.7" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="172.1" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="145.2" y1="163.1" x2="145.2" y2="187.1" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="168.2" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="149.0" y1="162.2" x2="149.0" y2="211.3" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="170.4" width="2.35" height="38.7" fill="var(--down)"/>
<line x1="152.8" y1="202.6" x2="152.8" y2="226.6" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="206.5" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="156.5" y1="204.6" x2="156.5" y2="224.0" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="204.9" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="160.3" y1="162.9" x2="160.3" y2="206.2" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="189.4" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="164.1" y1="127.6" x2="164.1" y2="174.8" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="138.8" width="2.35" height="35.8" fill="var(--up)"/>
<line x1="167.9" y1="109.8" x2="167.9" y2="157.9" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="127.2" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="171.7" y1="140.3" x2="171.7" y2="197.6" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="140.3" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="175.5" y1="160.7" x2="175.5" y2="194.4" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="169.6" width="2.35" height="20.8" fill="var(--down)"/>
<line x1="179.3" y1="180.3" x2="179.3" y2="233.4" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="189.2" width="2.35" height="34.4" fill="var(--down)"/>
<line x1="183.1" y1="219.9" x2="183.1" y2="260.1" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="221.1" width="2.35" height="28.5" fill="var(--down)"/>
<line x1="186.8" y1="240.9" x2="186.8" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="257.8" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="190.6" y1="236.8" x2="190.6" y2="271.0" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="253.4" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="194.4" y1="238.8" x2="194.4" y2="264.1" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="246.8" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="198.2" y1="277.9" x2="198.2" y2="318.9" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="286.7" width="2.35" height="24.4" fill="var(--down)"/>
<line x1="202.0" y1="295.2" x2="202.0" y2="331.7" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="301.6" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="205.8" y1="287.2" x2="205.8" y2="313.4" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="296.6" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="209.6" y1="281.1" x2="209.6" y2="311.4" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="282.4" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="213.3" y1="288.5" x2="213.3" y2="332.3" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="288.6" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="217.1" y1="312.9" x2="217.1" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="314.1" width="2.35" height="18.2" fill="var(--down)"/>
<line x1="220.9" y1="352.2" x2="220.9" y2="403.2" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="356.5" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="224.7" y1="353.5" x2="224.7" y2="381.4" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="359.9" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="228.5" y1="360.6" x2="228.5" y2="391.1" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="364.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="232.3" y1="361.5" x2="232.3" y2="397.3" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="362.4" width="2.35" height="31.9" fill="var(--down)"/>
<line x1="236.1" y1="372.9" x2="236.1" y2="395.0" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="374.5" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="239.8" y1="347.8" x2="239.8" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="351.2" width="2.35" height="22.4" fill="var(--up)"/>
<line x1="243.6" y1="305.7" x2="243.6" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="310.2" width="2.35" height="47.2" fill="var(--up)"/>
<line x1="247.4" y1="326.4" x2="247.4" y2="366.3" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="331.4" width="2.35" height="33.3" fill="var(--down)"/>
<line x1="251.2" y1="349.6" x2="251.2" y2="368.6" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="354.4" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="255.0" y1="352.0" x2="255.0" y2="369.5" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="358.1" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="258.8" y1="352.9" x2="258.8" y2="365.8" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="357.4" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="262.6" y1="363.3" x2="262.6" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="363.6" width="2.35" height="52.5" fill="var(--down)"/>
<line x1="266.4" y1="423.3" x2="266.4" y2="441.6" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="424.5" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="270.1" y1="434.3" x2="270.1" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="435.4" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="273.9" y1="464.8" x2="273.9" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="468.7" width="2.35" height="31.9" fill="var(--down)"/>
<line x1="277.7" y1="503.5" x2="277.7" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="504.0" width="2.35" height="43.6" fill="var(--down)"/>
<line x1="281.5" y1="509.3" x2="281.5" y2="543.4" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="535.0" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="285.3" y1="529.6" x2="285.3" y2="549.6" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="533.6" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="289.1" y1="519.8" x2="289.1" y2="549.9" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="523.6" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="292.9" y1="511.6" x2="292.9" y2="541.4" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="518.4" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="296.6" y1="508.6" x2="296.6" y2="547.4" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="521.4" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="300.4" y1="507.0" x2="300.4" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="508.6" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="304.2" y1="503.6" x2="304.2" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="512.9" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="308.0" y1="500.1" x2="308.0" y2="526.1" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="501.8" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="311.8" y1="453.2" x2="311.8" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="453.6" width="2.35" height="47.9" fill="var(--up)"/>
<line x1="315.6" y1="464.8" x2="315.6" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="466.4" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="319.4" y1="469.1" x2="319.4" y2="501.7" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="479.8" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="323.1" y1="494.2" x2="323.1" y2="514.9" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="501.3" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="326.9" y1="511.5" x2="326.9" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="514.9" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="330.7" y1="493.3" x2="330.7" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="494.2" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="334.5" y1="474.1" x2="334.5" y2="498.8" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="489.4" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="338.3" y1="469.4" x2="338.3" y2="495.4" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="480.8" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="342.1" y1="463.7" x2="342.1" y2="483.5" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="472.1" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="345.9" y1="460.2" x2="345.9" y2="489.4" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="475.7" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="349.6" y1="478.9" x2="349.6" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="496.0" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="353.4" y1="492.2" x2="353.4" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="497.6" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="357.2" y1="501.1" x2="357.2" y2="521.8" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="508.4" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="361.0" y1="492.2" x2="361.0" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="492.2" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="364.8" y1="490.8" x2="364.8" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="490.8" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="368.6" y1="456.6" x2="368.6" y2="487.6" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="476.6" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="372.4" y1="447.7" x2="372.4" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="458.6" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="376.2" y1="448.9" x2="376.2" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="452.3" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="379.9" y1="434.3" x2="379.9" y2="454.6" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="436.3" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="383.7" y1="440.2" x2="383.7" y2="460.7" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="447.3" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="387.5" y1="457.1" x2="387.5" y2="471.4" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="459.8" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="391.3" y1="441.1" x2="391.3" y2="458.4" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="453.6" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="395.1" y1="448.2" x2="395.1" y2="482.6" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="460.7" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="398.9" y1="457.0" x2="398.9" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="467.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="402.7" y1="467.3" x2="402.7" y2="489.0" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="468.2" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="406.4" y1="481.0" x2="406.4" y2="502.7" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="485.5" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="410.2" y1="485.3" x2="410.2" y2="499.5" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="492.9" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="414.0" y1="492.8" x2="414.0" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="500.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="417.8" y1="489.2" x2="417.8" y2="509.5" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="496.5" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="421.6" y1="488.3" x2="421.6" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="494.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="425.4" y1="488.3" x2="425.4" y2="510.0" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="490.4" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="429.2" y1="502.7" x2="429.2" y2="535.3" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="505.6" width="2.35" height="25.1" fill="var(--down)"/>
<line x1="432.9" y1="497.8" x2="432.9" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="507.9" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="436.7" y1="495.4" x2="436.7" y2="508.4" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="499.4" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="440.5" y1="497.2" x2="440.5" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="499.5" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="444.3" y1="504.7" x2="444.3" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="508.6" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="448.1" y1="511.8" x2="448.1" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="520.4" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="451.9" y1="530.7" x2="451.9" y2="551.0" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="532.1" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="455.7" y1="529.3" x2="455.7" y2="553.5" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="538.2" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="459.5" y1="525.7" x2="459.5" y2="542.6" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="535.2" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="463.2" y1="534.6" x2="463.2" y2="549.6" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="537.8" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="467.0" y1="533.9" x2="467.0" y2="544.6" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="541.4" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="470.8" y1="539.4" x2="470.8" y2="559.6" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="544.4" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="474.6" y1="558.0" x2="474.6" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="561.9" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="478.4" y1="575.1" x2="478.4" y2="603.9" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="577.2" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="482.2" y1="566.1" x2="482.2" y2="588.8" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="570.1" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="486.0" y1="574.5" x2="486.0" y2="592.5" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="576.8" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="489.7" y1="577.2" x2="489.7" y2="593.6" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="577.5" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="493.5" y1="552.4" x2="493.5" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="559.4" width="2.35" height="24.6" fill="var(--up)"/>
<line x1="497.3" y1="554.8" x2="497.3" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="562.4" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="501.1" y1="552.3" x2="501.1" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="555.5" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="504.9" y1="549.6" x2="504.9" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="558.3" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="508.7" y1="536.4" x2="508.7" y2="559.2" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="537.5" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="512.5" y1="529.8" x2="512.5" y2="547.1" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="537.1" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="516.2" y1="491.3" x2="516.2" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="499.0" width="2.35" height="42.9" fill="var(--up)"/>
<line x1="520.0" y1="494.0" x2="520.0" y2="504.7" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="502.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="523.8" y1="491.5" x2="523.8" y2="503.8" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="501.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="527.6" y1="500.6" x2="527.6" y2="515.9" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="507.4" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="531.4" y1="495.3" x2="531.4" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="496.1" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="535.2" y1="499.0" x2="535.2" y2="516.1" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="501.3" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="539.0" y1="506.7" x2="539.0" y2="519.8" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="509.9" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="542.7" y1="482.8" x2="542.7" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="510.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="546.5" y1="511.5" x2="546.5" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="517.2" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="550.3" y1="519.7" x2="550.3" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="522.0" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="554.1" y1="521.8" x2="554.1" y2="532.1" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="523.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="557.9" y1="507.5" x2="557.9" y2="527.7" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="508.1" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="561.7" y1="495.6" x2="561.7" y2="513.2" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="499.7" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="565.5" y1="499.0" x2="565.5" y2="522.3" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="499.0" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="569.3" y1="501.7" x2="569.3" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="504.0" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="573.0" y1="500.4" x2="573.0" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="502.9" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="576.8" y1="508.6" x2="576.8" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="509.9" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="580.6" y1="511.6" x2="580.6" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="519.1" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="584.4" y1="529.5" x2="584.4" y2="540.3" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="532.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="588.2" y1="527.0" x2="588.2" y2="541.4" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="532.0" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="592.0" y1="525.9" x2="592.0" y2="551.7" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="529.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="595.8" y1="522.9" x2="595.8" y2="531.8" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="527.1" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="599.5" y1="511.6" x2="599.5" y2="527.3" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="517.7" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="603.3" y1="513.1" x2="603.3" y2="523.8" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="519.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="607.1" y1="515.2" x2="607.1" y2="534.1" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="515.6" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="610.9" y1="509.9" x2="610.9" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="527.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="614.7" y1="510.2" x2="614.7" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="512.0" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="618.5" y1="503.6" x2="618.5" y2="517.9" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="509.5" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="622.3" y1="503.5" x2="622.3" y2="514.5" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="509.0" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="626.0" y1="507.7" x2="626.0" y2="530.7" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="509.9" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="629.8" y1="501.0" x2="629.8" y2="515.7" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="501.1" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="633.6" y1="494.2" x2="633.6" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="502.7" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="637.4" y1="502.4" x2="637.4" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="503.1" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="641.2" y1="478.0" x2="641.2" y2="502.7" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="480.5" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="645.0" y1="472.3" x2="645.0" y2="498.6" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="479.6" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="648.8" y1="475.5" x2="648.8" y2="491.3" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="485.5" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="652.5" y1="465.9" x2="652.5" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="468.0" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="656.3" y1="463.7" x2="656.3" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="464.6" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="660.1" y1="457.0" x2="660.1" y2="474.6" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="465.9" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="663.9" y1="447.3" x2="663.9" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="448.9" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="667.7" y1="437.9" x2="667.7" y2="451.8" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="445.0" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="671.5" y1="440.9" x2="671.5" y2="454.8" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="447.2" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="675.3" y1="438.4" x2="675.3" y2="468.0" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="447.0" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="679.1" y1="462.5" x2="679.1" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="466.0" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="682.8" y1="463.0" x2="682.8" y2="473.0" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="468.2" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="686.6" y1="473.0" x2="686.6" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="473.5" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="690.4" y1="478.9" x2="690.4" y2="498.3" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="488.7" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="694.2" y1="480.1" x2="694.2" y2="503.5" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="482.3" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="698.0" y1="486.5" x2="698.0" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="487.4" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="701.8" y1="490.6" x2="701.8" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="496.5" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="705.6" y1="478.7" x2="705.6" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="478.9" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="709.3" y1="472.6" x2="709.3" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="477.6" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="713.1" y1="479.4" x2="713.1" y2="497.2" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="479.8" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="716.9" y1="494.4" x2="716.9" y2="527.3" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="495.1" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="720.7" y1="515.4" x2="720.7" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="519.1" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="724.5" y1="510.8" x2="724.5" y2="519.5" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="514.9" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="728.3" y1="515.2" x2="728.3" y2="526.4" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="520.9" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="732.1" y1="504.2" x2="732.1" y2="526.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="507.0" width="2.35" height="15.0" fill="var(--up)"/>
<line x1="735.8" y1="502.2" x2="735.8" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="502.6" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="739.6" y1="490.4" x2="739.6" y2="501.0" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="492.2" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="743.4" y1="474.9" x2="743.4" y2="494.9" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="480.8" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="747.2" y1="478.3" x2="747.2" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="481.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="751.0" y1="472.5" x2="751.0" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="476.0" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="754.8" y1="449.5" x2="754.8" y2="476.9" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="450.7" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="758.6" y1="440.7" x2="758.6" y2="471.0" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="450.4" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="762.4" y1="454.1" x2="762.4" y2="468.5" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="457.3" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="766.1" y1="448.2" x2="766.1" y2="467.6" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="455.0" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="769.9" y1="443.1" x2="769.9" y2="461.1" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="445.2" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="773.7" y1="429.9" x2="773.7" y2="455.2" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="437.7" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="777.5" y1="448.1" x2="777.5" y2="519.7" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="451.4" width="2.35" height="41.5" fill="var(--down)"/>
<line x1="781.3" y1="473.0" x2="781.3" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="474.1" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="785.1" y1="457.3" x2="785.1" y2="484.7" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="460.0" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="788.9" y1="445.6" x2="788.9" y2="474.8" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="458.9" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="792.6" y1="463.4" x2="792.6" y2="480.5" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="473.2" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="796.4" y1="474.6" x2="796.4" y2="491.0" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="476.7" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="800.2" y1="475.5" x2="800.2" y2="492.8" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="482.4" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="804.0" y1="468.2" x2="804.0" y2="483.0" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="469.4" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="807.8" y1="473.0" x2="807.8" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="481.0" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="811.6" y1="473.9" x2="811.6" y2="491.0" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="481.7" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="815.4" y1="467.8" x2="815.4" y2="484.6" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="469.4" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="819.1" y1="456.1" x2="819.1" y2="472.3" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="461.1" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="822.9" y1="453.9" x2="822.9" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="456.8" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="826.7" y1="464.8" x2="826.7" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="468.7" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="830.5" y1="458.9" x2="830.5" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="462.1" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="834.3" y1="453.4" x2="834.3" y2="469.2" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="457.1" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="838.1" y1="451.8" x2="838.1" y2="462.8" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="453.8" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="841.9" y1="446.4" x2="841.9" y2="455.4" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="450.5" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="845.6" y1="445.2" x2="845.6" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="449.1" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="849.4" y1="439.9" x2="849.4" y2="460.5" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="440.4" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="853.2" y1="432.7" x2="853.2" y2="444.8" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="435.9" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="857.0" y1="430.8" x2="857.0" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="430.8" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="860.8" y1="421.9" x2="860.8" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="427.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="864.6" y1="416.5" x2="864.6" y2="433.4" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="425.8" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="868.4" y1="430.6" x2="868.4" y2="440.0" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="433.1" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="872.2" y1="431.8" x2="872.2" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="435.2" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="875.9" y1="427.2" x2="875.9" y2="441.8" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="429.9" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="879.7" y1="422.6" x2="879.7" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="426.9" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="883.5" y1="416.9" x2="883.5" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="421.7" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="887.3" y1="420.4" x2="887.3" y2="436.3" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="422.6" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="891.1" y1="437.4" x2="891.1" y2="447.0" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="440.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="894.9" y1="432.4" x2="894.9" y2="443.8" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="441.1" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="898.7" y1="438.1" x2="898.7" y2="445.2" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="438.6" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="902.4" y1="429.7" x2="902.4" y2="438.6" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="434.3" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="906.2" y1="442.4" x2="906.2" y2="448.8" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="445.7" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="910.0" y1="444.7" x2="910.0" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="448.9" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="913.8" y1="447.7" x2="913.8" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="450.5" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="917.6" y1="453.2" x2="917.6" y2="464.4" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="455.9" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="921.4" y1="452.9" x2="921.4" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="454.3" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="925.2" y1="451.3" x2="925.2" y2="458.0" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="453.6" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="928.9" y1="447.2" x2="928.9" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="454.1" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="932.7" y1="452.1" x2="932.7" y2="462.5" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="452.7" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="936.5" y1="444.5" x2="936.5" y2="452.5" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="448.2" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="940.3" y1="444.8" x2="940.3" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="444.8" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="944.1" y1="431.1" x2="944.1" y2="447.0" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="432.0" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="947.9" y1="432.9" x2="947.9" y2="439.1" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="433.3" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="951.7" y1="421.5" x2="951.7" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="423.3" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="955.5" y1="424.2" x2="955.5" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="424.2" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="959.2" y1="426.5" x2="959.2" y2="445.0" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="429.7" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="963.0" y1="429.0" x2="963.0" y2="453.4" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="438.6" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="966.8" y1="449.8" x2="966.8" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="455.2" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="970.6" y1="442.0" x2="970.6" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="442.4" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="974.4" y1="437.0" x2="974.4" y2="449.8" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="438.6" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="978.2" y1="429.3" x2="978.2" y2="438.3" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="430.4" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="982.0" y1="424.0" x2="982.0" y2="435.9" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="424.7" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="985.7" y1="423.3" x2="985.7" y2="435.2" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="426.0" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="989.5" y1="431.1" x2="989.5" y2="439.9" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="431.8" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="993.3" y1="432.2" x2="993.3" y2="448.4" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="432.7" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="997.1" y1="445.0" x2="997.1" y2="457.8" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="446.4" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="1000.9" y1="433.8" x2="1000.9" y2="445.6" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="435.2" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="1004.7" y1="454.6" x2="1004.7" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="459.1" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="1008.5" y1="462.8" x2="1008.5" y2="472.5" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="463.7" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="1012.2" y1="459.1" x2="1012.2" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="461.9" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="1016.0" y1="461.1" x2="1016.0" y2="476.7" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="462.1" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="1019.8" y1="458.4" x2="1019.8" y2="489.6" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="460.7" width="2.35" height="25.8" fill="var(--down)"/>
<line x1="1023.6" y1="483.7" x2="1023.6" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="484.7" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="1027.4" y1="485.8" x2="1027.4" y2="495.6" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="487.6" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="1031.2" y1="488.5" x2="1031.2" y2="501.7" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="489.0" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="1035.0" y1="492.2" x2="1035.0" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="499.0" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="1038.7" y1="507.7" x2="1038.7" y2="514.5" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="508.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="1042.5" y1="504.7" x2="1042.5" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="510.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1046.3" y1="500.8" x2="1046.3" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="507.9" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="1050.1" y1="504.8" x2="1050.1" y2="508.8" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="505.2" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="60" y1="448.9" x2="1052" y2="448.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="452.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$110.44 R1</text>
<text x="1058" y="464.4" font-size="9.5" fill="var(--muted)">터치 13회</text>
<line x1="60" y1="93.0" x2="1052" y2="93.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="96.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$130.42 R2</text>
<text x="1058" y="108.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="526.5" x2="1052" y2="526.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="520.5" font-size="11.5" fill="var(--support)" font-weight="600">$106.09 S1</text>
<text x="1058" y="532.5" font-size="9.5" fill="var(--muted)">터치 10회</text>
<circle cx="1052.0" cy="507.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="499.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $107.13 (2026-08-21)</text>
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

- **상승**: TIPS 원금은 CPI에 맞춰 조정되므로, 명목채(TLT) 대비 이 ETF가 더 강해지면 기대인플레이션이 올라가고 있다는 신호로 흔히 해석한다.
- **하락**: 명목채 대비 이 ETF가 더 약해지면 기대인플레이션이 내려가고 있다는(또는 실질금리가 올라가고 있다는) 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: TIPS는 원금이 CPI-U(소비자물가지수)에 맞춰 조정되기 때문에, 물가가 오르면 원금과 이자 지급액도 함께 늘어난다 — 그래서 TIPS 가격은 명목채와 달리 실질금리에 직접 영향을 받는다. TLT(명목채) 대비 이 ETF가 상대적으로 강해진다는 것은, 시장이 "앞으로 물가가 오른 만큼 더 보상받아야 한다"고 가격에 반영하기 시작했다는(기대인플레이션이 올라가고 있다는) 뜻으로 읽는다.
- 정밀한 기대인플레이션(breakeven inflation) 수치는 아니다 — 실제 BEI는 만기가 같은 명목채와 물가연동채 수익률을 빼서 계산한다(예: FRED `T10YIE`). 이 문서는 TLT와의 방향을 대략적으로 비교하는 용도로만 쓴다.

---

## 관련 문서

- [20년+ 장기국채 ETF (TLT)](./tlt.md)
- [하이일드 회사채 ETF (HYG)](./hyg.md)
- [채권 3종 비교 (지수화)](./comparison.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md)
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — iShares TIPS Bond ETF (TIP)](https://finance.yahoo.com/quote/TIP/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
