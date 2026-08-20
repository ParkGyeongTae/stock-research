# 물가연동국채 ETF (TIP) (주봉 5년)

!!! note ""
    최근 5년 iShares 물가연동국채(TIPS) ETF(`TIP`) 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. TIPS는 원금이 CPI에 연동돼 조정되는 국채라, TLT(명목 장기국채) 대비 상대 강도를 보면 시장이 반영하는 **기대인플레이션의 대략적인 방향**을 가늠하는 실마리가 된다.

    ⚠️ **정밀한 기대인플레이션(breakeven inflation) 수치가 아니다** — 실제 BEI는 만기가 일치하는 명목채·물가연동채 수익률을 빼서 계산하며(예: FRED `T10YIE`), 이 문서는 그 계산을 하지 않는다. 이 문서와 TLT의 방향을 정성적으로 비교하는 용도로만 쓴다.

---

## 1. 차트 — 최근 5년 주봉

<div class="tip-chart">
<style>
.tip-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .tip-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-19 · 마지막 종가 $107.51 (2026-08-19) · 단위 USD</text>
<line x1="60" y1="545.8" x2="1052" y2="545.8" class="grid"/>
<text x="52" y="549.8" font-size="11" text-anchor="end" fill="var(--muted)">105</text>
<line x1="60" y1="456.8" x2="1052" y2="456.8" class="grid"/>
<text x="52" y="460.8" font-size="11" text-anchor="end" fill="var(--muted)">110</text>
<line x1="60" y1="367.7" x2="1052" y2="367.7" class="grid"/>
<text x="52" y="371.7" font-size="11" text-anchor="end" fill="var(--muted)">115</text>
<line x1="60" y1="278.7" x2="1052" y2="278.7" class="grid"/>
<text x="52" y="282.7" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="189.6" x2="1052" y2="189.6" class="grid"/>
<text x="52" y="193.6" font-size="11" text-anchor="end" fill="var(--muted)">125</text>
<line x1="60" y1="100.5" x2="1052" y2="100.5" class="grid"/>
<text x="52" y="104.5" font-size="11" text-anchor="end" fill="var(--muted)">130</text>
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
<line x1="61.9" y1="115.7" x2="61.9" y2="123.2" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="116.9" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="65.7" y1="100.4" x2="65.7" y2="120.5" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="100.7" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="69.4" y1="96.6" x2="69.4" y2="128.9" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="97.9" width="2.34" height="27.3" fill="var(--down)"/>
<line x1="73.2" y1="108.9" x2="73.2" y2="132.1" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="115.9" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="77.0" y1="109.1" x2="77.0" y2="124.8" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="110.1" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="80.7" y1="119.4" x2="80.7" y2="141.5" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="120.8" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="84.5" y1="135.3" x2="84.5" y2="146.8" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="139.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="88.3" y1="135.4" x2="88.3" y2="145.4" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="140.1" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="92.1" y1="121.2" x2="92.1" y2="142.0" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="126.2" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="95.8" y1="120.5" x2="95.8" y2="139.0" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="122.6" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="99.6" y1="96.6" x2="99.6" y2="133.7" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="122.4" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="103.4" y1="104.5" x2="103.4" y2="138.6" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="106.4" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="107.1" y1="76.1" x2="107.1" y2="104.3" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="93.1" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="110.9" y1="83.4" x2="110.9" y2="100.5" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="90.7" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="114.7" y1="102.7" x2="114.7" y2="128.5" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="103.4" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="118.5" y1="96.6" x2="118.5" y2="126.0" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="105.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="122.2" y1="101.6" x2="122.2" y2="126.5" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="103.2" width="2.34" height="22.6" fill="var(--down)"/>
<line x1="126.0" y1="116.4" x2="126.0" y2="143.8" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="121.4" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="129.8" y1="123.5" x2="129.8" y2="143.3" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="132.1" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="133.6" y1="111.9" x2="133.6" y2="135.8" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="114.8" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="137.3" y1="123.5" x2="137.3" y2="171.8" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="123.9" width="2.34" height="43.8" fill="var(--down)"/>
<line x1="141.1" y1="149.0" x2="141.1" y2="174.5" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="171.2" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="144.9" y1="170.9" x2="144.9" y2="188.7" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="172.1" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="148.6" y1="163.1" x2="148.6" y2="187.1" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="168.2" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="152.4" y1="162.2" x2="152.4" y2="211.3" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="170.4" width="2.34" height="38.7" fill="var(--down)"/>
<line x1="156.2" y1="202.6" x2="156.2" y2="226.6" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="206.5" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="160.0" y1="204.6" x2="160.0" y2="224.0" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="204.9" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="163.7" y1="162.9" x2="163.7" y2="206.2" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="189.4" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="167.5" y1="127.6" x2="167.5" y2="174.8" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="138.8" width="2.34" height="35.8" fill="var(--up)"/>
<line x1="171.3" y1="109.8" x2="171.3" y2="157.9" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="127.2" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="175.0" y1="140.3" x2="175.0" y2="197.6" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="140.3" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="178.8" y1="160.7" x2="178.8" y2="194.4" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="169.6" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="182.6" y1="180.3" x2="182.6" y2="233.4" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="189.2" width="2.34" height="34.4" fill="var(--down)"/>
<line x1="186.4" y1="219.9" x2="186.4" y2="260.1" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="221.1" width="2.34" height="28.5" fill="var(--down)"/>
<line x1="190.1" y1="240.9" x2="190.1" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="257.8" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="193.9" y1="236.8" x2="193.9" y2="271.0" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="253.4" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="197.7" y1="238.8" x2="197.7" y2="264.1" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="246.8" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="201.4" y1="277.9" x2="201.4" y2="318.9" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="286.7" width="2.34" height="24.4" fill="var(--down)"/>
<line x1="205.2" y1="295.2" x2="205.2" y2="331.7" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="301.6" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="209.0" y1="287.2" x2="209.0" y2="313.4" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="296.6" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="212.8" y1="281.1" x2="212.8" y2="311.4" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="282.4" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="216.5" y1="288.5" x2="216.5" y2="332.3" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="288.6" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="220.3" y1="312.9" x2="220.3" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="314.1" width="2.34" height="18.2" fill="var(--down)"/>
<line x1="224.1" y1="352.2" x2="224.1" y2="403.2" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="356.5" width="2.34" height="16.0" fill="var(--down)"/>
<line x1="227.8" y1="353.5" x2="227.8" y2="381.4" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="359.9" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="231.6" y1="360.6" x2="231.6" y2="391.1" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="364.7" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="235.4" y1="361.5" x2="235.4" y2="397.3" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="362.4" width="2.34" height="31.9" fill="var(--down)"/>
<line x1="239.2" y1="372.9" x2="239.2" y2="395.0" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="374.5" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="242.9" y1="347.8" x2="242.9" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="351.2" width="2.34" height="22.4" fill="var(--up)"/>
<line x1="246.7" y1="305.7" x2="246.7" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="310.2" width="2.34" height="47.2" fill="var(--up)"/>
<line x1="250.5" y1="326.4" x2="250.5" y2="366.3" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="331.4" width="2.34" height="33.3" fill="var(--down)"/>
<line x1="254.3" y1="349.6" x2="254.3" y2="368.6" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="354.4" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="258.0" y1="352.0" x2="258.0" y2="369.5" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="358.1" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="261.8" y1="352.9" x2="261.8" y2="365.8" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="357.4" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="265.6" y1="363.3" x2="265.6" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="363.6" width="2.34" height="52.5" fill="var(--down)"/>
<line x1="269.3" y1="423.3" x2="269.3" y2="441.6" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="424.5" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="273.1" y1="434.3" x2="273.1" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="435.4" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="276.9" y1="464.8" x2="276.9" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="468.7" width="2.34" height="31.9" fill="var(--down)"/>
<line x1="280.7" y1="503.5" x2="280.7" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="504.0" width="2.34" height="43.6" fill="var(--down)"/>
<line x1="284.4" y1="509.3" x2="284.4" y2="543.4" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="535.0" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="288.2" y1="529.6" x2="288.2" y2="549.6" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="533.6" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="292.0" y1="519.8" x2="292.0" y2="549.9" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="523.6" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="295.7" y1="511.6" x2="295.7" y2="541.4" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="518.4" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="299.5" y1="508.6" x2="299.5" y2="547.4" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="521.4" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="303.3" y1="507.0" x2="303.3" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="508.6" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="307.1" y1="503.6" x2="307.1" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="512.9" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="310.8" y1="500.1" x2="310.8" y2="526.1" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="501.8" width="2.34" height="19.4" fill="var(--up)"/>
<line x1="314.6" y1="453.2" x2="314.6" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="453.6" width="2.34" height="47.9" fill="var(--up)"/>
<line x1="318.4" y1="464.8" x2="318.4" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="466.4" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="322.1" y1="469.1" x2="322.1" y2="501.7" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="479.8" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="325.9" y1="494.2" x2="325.9" y2="514.9" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="501.3" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="329.7" y1="511.5" x2="329.7" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="514.9" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="333.5" y1="493.3" x2="333.5" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="494.2" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="337.2" y1="474.1" x2="337.2" y2="498.8" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="489.4" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="341.0" y1="469.4" x2="341.0" y2="495.4" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="480.8" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="344.8" y1="463.7" x2="344.8" y2="483.5" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="472.1" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="348.5" y1="460.2" x2="348.5" y2="489.4" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="475.7" width="2.34" height="13.0" fill="var(--down)"/>
<line x1="352.3" y1="478.9" x2="352.3" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="496.0" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="356.1" y1="492.2" x2="356.1" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="497.6" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="359.9" y1="501.1" x2="359.9" y2="521.8" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="508.4" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="363.6" y1="492.2" x2="363.6" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="492.2" width="2.34" height="22.1" fill="var(--up)"/>
<line x1="367.4" y1="490.8" x2="367.4" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="490.8" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="371.2" y1="456.6" x2="371.2" y2="487.6" stroke="var(--down)" class="wick"/>
<rect x="370.01" y="476.6" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="375.0" y1="447.7" x2="375.0" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="458.6" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="378.7" y1="448.9" x2="378.7" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="452.3" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="382.5" y1="434.3" x2="382.5" y2="454.6" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="436.3" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="386.3" y1="440.2" x2="386.3" y2="460.7" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="447.3" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="390.0" y1="457.1" x2="390.0" y2="471.4" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="459.8" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="393.8" y1="441.1" x2="393.8" y2="458.4" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="453.6" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="397.6" y1="448.2" x2="397.6" y2="482.6" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="460.7" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="401.4" y1="457.0" x2="401.4" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="467.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="405.1" y1="467.3" x2="405.1" y2="489.0" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="468.2" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="408.9" y1="481.0" x2="408.9" y2="502.7" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="485.5" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="412.7" y1="485.3" x2="412.7" y2="499.5" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="492.9" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="416.4" y1="492.8" x2="416.4" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="500.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="420.2" y1="489.2" x2="420.2" y2="509.5" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="496.5" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="424.0" y1="488.3" x2="424.0" y2="499.7" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="494.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="427.8" y1="488.3" x2="427.8" y2="510.0" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="490.4" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="431.5" y1="502.7" x2="431.5" y2="535.3" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="505.6" width="2.34" height="25.1" fill="var(--down)"/>
<line x1="435.3" y1="497.8" x2="435.3" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="507.9" width="2.34" height="21.2" fill="var(--up)"/>
<line x1="439.1" y1="495.4" x2="439.1" y2="508.4" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="499.4" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="442.8" y1="497.2" x2="442.8" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="499.5" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="446.6" y1="504.7" x2="446.6" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="508.6" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="450.4" y1="511.8" x2="450.4" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="520.4" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="454.2" y1="530.7" x2="454.2" y2="551.0" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="532.1" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="457.9" y1="529.3" x2="457.9" y2="553.5" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="538.2" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="461.7" y1="525.7" x2="461.7" y2="542.6" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="535.2" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="465.5" y1="534.6" x2="465.5" y2="549.6" stroke="var(--up)" class="wick"/>
<rect x="464.31" y="537.8" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="469.2" y1="533.9" x2="469.2" y2="544.6" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="541.4" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="473.0" y1="539.4" x2="473.0" y2="559.6" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="544.4" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="476.8" y1="558.0" x2="476.8" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="561.9" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="480.6" y1="575.1" x2="480.6" y2="603.9" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="577.2" width="2.34" height="19.9" fill="var(--down)"/>
<line x1="484.3" y1="566.1" x2="484.3" y2="588.8" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="570.1" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="488.1" y1="574.5" x2="488.1" y2="592.5" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="576.8" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="491.9" y1="577.2" x2="491.9" y2="593.6" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="577.5" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="495.7" y1="552.4" x2="495.7" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="559.4" width="2.34" height="24.6" fill="var(--up)"/>
<line x1="499.4" y1="554.8" x2="499.4" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="562.4" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="503.2" y1="552.3" x2="503.2" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="555.5" width="2.34" height="20.7" fill="var(--up)"/>
<line x1="507.0" y1="549.6" x2="507.0" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="558.3" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="510.7" y1="536.4" x2="510.7" y2="559.2" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="537.5" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="514.5" y1="529.8" x2="514.5" y2="547.1" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="537.1" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="518.3" y1="491.3" x2="518.3" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="499.0" width="2.34" height="42.9" fill="var(--up)"/>
<line x1="522.1" y1="494.0" x2="522.1" y2="504.7" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="502.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="525.8" y1="491.5" x2="525.8" y2="503.8" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="501.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="529.6" y1="500.6" x2="529.6" y2="515.9" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="507.4" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="533.4" y1="495.3" x2="533.4" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="496.1" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="537.1" y1="499.0" x2="537.1" y2="516.1" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="501.3" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="540.9" y1="506.7" x2="540.9" y2="519.8" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="509.9" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="544.7" y1="482.8" x2="544.7" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="510.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="548.5" y1="511.5" x2="548.5" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="517.2" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="552.2" y1="519.7" x2="552.2" y2="533.7" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="522.0" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="556.0" y1="521.8" x2="556.0" y2="532.1" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="523.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="559.8" y1="507.5" x2="559.8" y2="527.7" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="508.1" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="563.5" y1="495.6" x2="563.5" y2="513.2" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="499.7" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="567.3" y1="499.0" x2="567.3" y2="522.3" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="499.0" width="2.34" height="23.3" fill="var(--down)"/>
<line x1="571.1" y1="501.7" x2="571.1" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="504.0" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="574.9" y1="500.4" x2="574.9" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="502.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="578.6" y1="508.6" x2="578.6" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="509.9" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="582.4" y1="511.6" x2="582.4" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="519.1" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="586.2" y1="529.5" x2="586.2" y2="540.3" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="532.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="589.9" y1="527.0" x2="589.9" y2="541.4" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="532.0" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="593.7" y1="525.9" x2="593.7" y2="551.7" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="529.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="597.5" y1="522.9" x2="597.5" y2="531.8" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="527.1" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="601.3" y1="511.6" x2="601.3" y2="527.3" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="517.7" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="605.0" y1="513.1" x2="605.0" y2="523.8" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="519.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="608.8" y1="515.2" x2="608.8" y2="534.1" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="515.6" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="612.6" y1="509.9" x2="612.6" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="527.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="616.3" y1="510.2" x2="616.3" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="512.0" width="2.34" height="16.4" fill="var(--up)"/>
<line x1="620.1" y1="503.6" x2="620.1" y2="517.9" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="509.5" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="623.9" y1="503.5" x2="623.9" y2="514.5" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="509.0" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="627.7" y1="507.7" x2="627.7" y2="530.7" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="509.9" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="631.4" y1="501.0" x2="631.4" y2="515.7" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="501.1" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="635.2" y1="494.2" x2="635.2" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="502.7" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="639.0" y1="502.4" x2="639.0" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="503.1" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="642.8" y1="478.0" x2="642.8" y2="502.7" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="480.5" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="646.5" y1="472.3" x2="646.5" y2="498.6" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="479.6" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="650.3" y1="475.5" x2="650.3" y2="491.3" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="485.5" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="654.1" y1="465.9" x2="654.1" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="468.0" width="2.34" height="17.8" fill="var(--up)"/>
<line x1="657.8" y1="463.7" x2="657.8" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="464.6" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="661.6" y1="457.0" x2="661.6" y2="474.6" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="465.9" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="665.4" y1="447.3" x2="665.4" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="448.9" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="669.2" y1="437.9" x2="669.2" y2="451.8" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="445.0" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="672.9" y1="440.9" x2="672.9" y2="454.8" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="447.2" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="676.7" y1="438.4" x2="676.7" y2="468.0" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="447.0" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="680.5" y1="462.5" x2="680.5" y2="474.4" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="466.0" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="684.2" y1="463.0" x2="684.2" y2="473.0" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="468.2" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="688.0" y1="473.0" x2="688.0" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="473.5" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="691.8" y1="478.9" x2="691.8" y2="498.3" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="488.7" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="695.6" y1="480.1" x2="695.6" y2="503.5" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="482.3" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="699.3" y1="486.5" x2="699.3" y2="509.2" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="487.4" width="2.34" height="14.8" fill="var(--down)"/>
<line x1="703.1" y1="490.6" x2="703.1" y2="503.6" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="496.5" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="706.9" y1="478.7" x2="706.9" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="478.9" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="710.6" y1="472.6" x2="710.6" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="477.6" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="714.4" y1="479.4" x2="714.4" y2="497.2" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="479.8" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="718.2" y1="494.4" x2="718.2" y2="527.3" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="495.1" width="2.34" height="23.3" fill="var(--down)"/>
<line x1="722.0" y1="515.4" x2="722.0" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="519.1" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="725.7" y1="510.8" x2="725.7" y2="519.5" stroke="var(--down)" class="wick"/>
<rect x="724.56" y="514.9" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="729.5" y1="515.2" x2="729.5" y2="526.4" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="520.9" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="733.3" y1="504.2" x2="733.3" y2="526.4" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="507.0" width="2.34" height="15.0" fill="var(--up)"/>
<line x1="737.0" y1="502.2" x2="737.0" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="502.6" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="740.8" y1="490.4" x2="740.8" y2="501.0" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="492.2" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="744.6" y1="474.9" x2="744.6" y2="494.9" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="480.8" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="748.4" y1="478.3" x2="748.4" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="481.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="752.1" y1="472.5" x2="752.1" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="476.0" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="755.9" y1="449.5" x2="755.9" y2="476.9" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="450.7" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="759.7" y1="440.7" x2="759.7" y2="471.0" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="450.4" width="2.34" height="16.0" fill="var(--down)"/>
<line x1="763.5" y1="454.1" x2="763.5" y2="468.5" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="457.3" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="767.2" y1="448.2" x2="767.2" y2="467.6" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="455.0" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="771.0" y1="443.1" x2="771.0" y2="461.1" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="445.2" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="774.8" y1="429.9" x2="774.8" y2="455.2" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="437.7" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="778.5" y1="448.1" x2="778.5" y2="519.7" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="451.4" width="2.34" height="41.5" fill="var(--down)"/>
<line x1="782.3" y1="473.0" x2="782.3" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="474.1" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="786.1" y1="457.3" x2="786.1" y2="484.7" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="460.0" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="789.9" y1="445.6" x2="789.9" y2="474.8" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="458.9" width="2.34" height="15.0" fill="var(--down)"/>
<line x1="793.6" y1="463.4" x2="793.6" y2="480.5" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="473.2" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="797.4" y1="474.6" x2="797.4" y2="491.0" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="476.7" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="801.2" y1="475.5" x2="801.2" y2="492.8" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="482.4" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="804.9" y1="468.2" x2="804.9" y2="483.0" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="469.4" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="808.7" y1="473.0" x2="808.7" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="481.0" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="812.5" y1="473.9" x2="812.5" y2="491.0" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="481.7" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="816.3" y1="467.8" x2="816.3" y2="484.6" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="469.4" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="820.0" y1="456.1" x2="820.0" y2="472.3" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="461.1" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="823.8" y1="453.9" x2="823.8" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="456.8" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="827.6" y1="464.8" x2="827.6" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="468.7" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="831.3" y1="458.9" x2="831.3" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="462.1" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="835.1" y1="453.4" x2="835.1" y2="469.2" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="457.1" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="838.9" y1="451.8" x2="838.9" y2="462.8" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="453.8" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="842.7" y1="446.4" x2="842.7" y2="455.4" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="450.5" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="846.4" y1="445.2" x2="846.4" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="449.1" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="850.2" y1="439.9" x2="850.2" y2="460.5" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="440.4" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="854.0" y1="432.7" x2="854.0" y2="444.8" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="435.9" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="857.7" y1="430.8" x2="857.7" y2="448.9" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="430.8" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="861.5" y1="421.9" x2="861.5" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="427.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="865.3" y1="416.5" x2="865.3" y2="433.4" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="425.8" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="869.1" y1="430.6" x2="869.1" y2="440.0" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="433.1" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="872.8" y1="431.8" x2="872.8" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="435.2" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="876.6" y1="427.2" x2="876.6" y2="441.8" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="429.9" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="880.4" y1="422.6" x2="880.4" y2="431.0" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="426.9" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="884.2" y1="416.9" x2="884.2" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="421.7" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="887.9" y1="420.4" x2="887.9" y2="436.3" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="422.6" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="891.7" y1="437.4" x2="891.7" y2="447.0" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="440.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="895.5" y1="432.4" x2="895.5" y2="443.8" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="441.1" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="899.2" y1="438.1" x2="899.2" y2="445.2" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="438.6" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="903.0" y1="429.7" x2="903.0" y2="438.6" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="434.3" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="906.8" y1="442.4" x2="906.8" y2="448.8" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="445.7" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="910.6" y1="444.7" x2="910.6" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="448.9" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="914.3" y1="447.7" x2="914.3" y2="459.1" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="450.5" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="918.1" y1="453.2" x2="918.1" y2="464.4" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="455.9" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="921.9" y1="452.9" x2="921.9" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="454.3" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="925.6" y1="451.3" x2="925.6" y2="458.0" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="453.6" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="929.4" y1="447.2" x2="929.4" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="454.1" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="933.2" y1="452.1" x2="933.2" y2="462.5" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="452.7" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="937.0" y1="444.5" x2="937.0" y2="452.5" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="448.2" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="940.7" y1="444.8" x2="940.7" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="444.8" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="944.5" y1="431.1" x2="944.5" y2="447.0" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="432.0" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="948.3" y1="432.9" x2="948.3" y2="439.1" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="433.3" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="952.0" y1="421.5" x2="952.0" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="423.3" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="955.8" y1="424.2" x2="955.8" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="424.2" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="959.6" y1="426.5" x2="959.6" y2="445.0" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="429.7" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="963.4" y1="429.0" x2="963.4" y2="453.4" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="438.6" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="967.1" y1="449.8" x2="967.1" y2="464.3" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="455.2" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="970.9" y1="442.0" x2="970.9" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="442.4" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="974.7" y1="437.0" x2="974.7" y2="449.8" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="438.6" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="978.4" y1="429.3" x2="978.4" y2="438.3" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="430.4" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="982.2" y1="424.0" x2="982.2" y2="435.9" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="424.7" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="986.0" y1="423.3" x2="986.0" y2="435.2" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="426.0" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="989.8" y1="431.1" x2="989.8" y2="439.9" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="431.8" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="993.5" y1="432.2" x2="993.5" y2="448.4" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="432.7" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="997.3" y1="445.0" x2="997.3" y2="457.8" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="446.4" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="1001.1" y1="433.8" x2="1001.1" y2="445.6" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="435.2" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="1004.9" y1="454.6" x2="1004.9" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="459.1" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="1008.6" y1="462.8" x2="1008.6" y2="472.5" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="463.7" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="1012.4" y1="459.1" x2="1012.4" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="461.9" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="1016.2" y1="461.1" x2="1016.2" y2="476.7" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="462.1" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="1019.9" y1="458.4" x2="1019.9" y2="489.6" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="460.7" width="2.34" height="25.8" fill="var(--down)"/>
<line x1="1023.7" y1="483.7" x2="1023.7" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="484.7" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="1027.5" y1="485.8" x2="1027.5" y2="495.6" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="487.6" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="1031.3" y1="488.5" x2="1031.3" y2="501.7" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="489.0" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="1035.0" y1="492.2" x2="1035.0" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="499.0" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="1038.8" y1="507.7" x2="1038.8" y2="514.5" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="508.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="1042.6" y1="504.7" x2="1042.6" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="510.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1046.3" y1="501.0" x2="1046.3" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="501.1" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="1050.1" y1="501.0" x2="1050.1" y2="505.0" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="501.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="60" y1="448.9" x2="1052" y2="448.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="452.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$110 R1</text>
<text x="1058" y="464.4" font-size="9.5" fill="var(--muted)">터치 13회</text>
<line x1="60" y1="93.0" x2="1052" y2="93.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="96.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$130 R2</text>
<text x="1058" y="108.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="526.5" x2="1052" y2="526.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="520.5" font-size="11.5" fill="var(--support)" font-weight="600">$106 S1</text>
<text x="1058" y="532.5" font-size="9.5" fill="var(--muted)">터치 10회</text>
<circle cx="1052.0" cy="501.1" r="3" fill="var(--ink)"/>
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

- **상승**: TIPS 원금이 CPI에 연동돼 조정되므로, 명목채(TLT) 대비 상대 강도가 강해지면 기대인플레이션 상승 신호로 흔히 해석된다.
- **하락**: 명목채 대비 상대 강도가 약해지면 기대인플레이션 하락(또는 실질금리 상승) 신호로 흔히 해석된다.
- 정밀한 기대인플레이션(breakeven inflation) 수치가 아니다 — 실제 BEI는 만기가 일치하는 명목채·물가연동채 수익률을 빼서 계산한다(예: FRED `T10YIE`). 이 문서는 TLT와의 방향을 정성적으로 비교하는 용도로만 쓴다.

---

## 관련 문서

- [20년+ 장기국채 ETF (TLT)](./tlt.md) — 명목채 짝 지표, 상대 강도로 기대인플레이션 방향을 가늠
- [거시경제 개념 정리](../../concepts/macroeconomics.md) — "인플레이션" 절
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — iShares TIPS Bond ETF (TIP)](https://finance.yahoo.com/quote/TIP/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
