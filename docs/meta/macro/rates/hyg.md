# 하이일드 회사채 ETF (HYG)

!!! note ""
    최근 5년 iShares 하이일드 회사채 ETF(`HYG`) 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 신용등급이 낮은(투기등급) 회사채를 담은 ETF로, 가격이 하락(=수익률 상승)하면 **신용스프레드가 벌어지고 있다**, 즉 시장이 저신용 기업의 자금조달 리스크를 더 크게 보고 있다는 신호로 흔히 읽힌다.

    ⚠️ **정확한 신용스프레드가 아니다** — 이 문서는 ETF **가격**이지, FRED의 ICE BofA 하이일드 스프레드(`BAMLH0A0HYM2`) 같은 실제 스프레드 지표가 아니다. 가격 방향이 대체로 스프레드와 반대로 움직이는 프록시일 뿐, 정밀한 스프레드 수치가 필요하면 원출처를 따로 확인한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="hyg-chart">
<style>
.hyg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .hyg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .hyg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.hyg-chart svg { width:100%; height:auto; display:block; }
.hyg-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.hyg-chart .title { fill: var(--ink); font-weight:600; }
.hyg-chart .grid { stroke: var(--grid); stroke-width:1; }
.hyg-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="하이일드 회사채 ETF(HYG) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">하이일드 회사채 ETF (HYG) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-19 · 마지막 종가 $79.71 (2026-08-19) · 단위 USD</text>
<line x1="60" y1="618.5" x2="1052" y2="618.5" class="grid"/>
<text x="52" y="622.5" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="543.5" x2="1052" y2="543.5" class="grid"/>
<text x="52" y="547.5" font-size="11" text-anchor="end" fill="var(--muted)">72</text>
<line x1="60" y1="468.5" x2="1052" y2="468.5" class="grid"/>
<text x="52" y="472.5" font-size="11" text-anchor="end" fill="var(--muted)">75</text>
<line x1="60" y1="393.5" x2="1052" y2="393.5" class="grid"/>
<text x="52" y="397.5" font-size="11" text-anchor="end" fill="var(--muted)">78</text>
<line x1="60" y1="318.5" x2="1052" y2="318.5" class="grid"/>
<text x="52" y="322.5" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="243.5" x2="1052" y2="243.5" class="grid"/>
<text x="52" y="247.5" font-size="11" text-anchor="end" fill="var(--muted)">82</text>
<line x1="60" y1="168.5" x2="1052" y2="168.5" class="grid"/>
<text x="52" y="172.5" font-size="11" text-anchor="end" fill="var(--muted)">85</text>
<line x1="60" y1="93.5" x2="1052" y2="93.5" class="grid"/>
<text x="52" y="97.5" font-size="11" text-anchor="end" fill="var(--muted)">88</text>
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
<line x1="61.9" y1="98.6" x2="61.9" y2="110.0" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="99.8" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="65.7" y1="78.8" x2="65.7" y2="96.2" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="79.7" width="2.34" height="16.5" fill="var(--up)"/>
<line x1="69.4" y1="75.5" x2="69.4" y2="83.9" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="78.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="73.2" y1="75.8" x2="73.2" y2="87.2" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="78.8" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="77.0" y1="74.3" x2="77.0" y2="81.8" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="78.5" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="80.7" y1="73.7" x2="80.7" y2="92.0" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="81.2" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="84.5" y1="81.8" x2="84.5" y2="104.3" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="85.7" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="88.3" y1="97.1" x2="88.3" y2="115.7" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="98.0" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="92.1" y1="96.8" x2="92.1" y2="123.8" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="101.9" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="95.8" y1="99.8" x2="95.8" y2="114.5" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="107.9" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="99.6" y1="102.5" x2="99.6" y2="115.4" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="110.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="103.4" y1="91.7" x2="103.4" y2="122.0" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="93.5" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="107.1" y1="90.2" x2="107.1" y2="113.9" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="90.8" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="110.9" y1="110.9" x2="110.9" y2="121.7" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="111.2" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="114.7" y1="118.4" x2="114.7" y2="158.3" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="119.3" width="2.34" height="35.1" fill="var(--down)"/>
<line x1="118.5" y1="134.6" x2="118.5" y2="158.9" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="138.5" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="122.2" y1="106.4" x2="122.2" y2="138.5" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="119.6" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="126.0" y1="113.3" x2="126.0" y2="132.2" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="119.6" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="129.8" y1="102.2" x2="129.8" y2="135.8" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="103.7" width="2.34" height="30.9" fill="var(--up)"/>
<line x1="133.6" y1="98.9" x2="133.6" y2="109.1" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="103.4" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="137.3" y1="108.5" x2="137.3" y2="142.7" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="110.9" width="2.34" height="31.5" fill="var(--down)"/>
<line x1="141.1" y1="122.9" x2="141.1" y2="157.4" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="135.8" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="144.9" y1="139.4" x2="144.9" y2="158.6" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="143.3" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="148.6" y1="142.4" x2="148.6" y2="200.0" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="162.8" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="152.4" y1="169.7" x2="152.4" y2="222.5" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="183.5" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="156.2" y1="194.9" x2="156.2" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="212.3" width="2.34" height="26.4" fill="var(--down)"/>
<line x1="160.0" y1="223.1" x2="160.0" y2="251.9" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="231.8" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="163.7" y1="209.6" x2="163.7" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="210.2" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="167.5" y1="202.1" x2="167.5" y2="252.2" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="221.9" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="171.3" y1="246.2" x2="171.3" y2="292.7" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="246.8" width="2.34" height="43.8" fill="var(--down)"/>
<line x1="175.0" y1="242.3" x2="175.0" y2="322.1" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="242.6" width="2.34" height="50.4" fill="var(--up)"/>
<line x1="178.8" y1="245.0" x2="178.8" y2="280.7" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="246.8" width="2.34" height="32.1" fill="var(--down)"/>
<line x1="182.6" y1="232.7" x2="182.6" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="260.0" width="2.34" height="20.1" fill="var(--up)"/>
<line x1="186.4" y1="241.1" x2="186.4" y2="311.6" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="257.9" width="2.34" height="53.4" fill="var(--down)"/>
<line x1="190.1" y1="291.8" x2="190.1" y2="331.1" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="311.3" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="193.9" y1="302.3" x2="193.9" y2="343.4" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="313.7" width="2.34" height="27.0" fill="var(--down)"/>
<line x1="197.7" y1="318.5" x2="197.7" y2="364.1" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="336.5" width="2.34" height="26.1" fill="var(--down)"/>
<line x1="201.4" y1="329.0" x2="201.4" y2="396.2" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="373.7" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="205.2" y1="392.6" x2="205.2" y2="426.5" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="404.6" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="209.0" y1="409.7" x2="209.0" y2="442.4" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="413.3" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="212.8" y1="312.8" x2="212.8" y2="422.0" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="312.8" width="2.34" height="106.5" fill="var(--up)"/>
<line x1="216.5" y1="322.7" x2="216.5" y2="362.9" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="326.3" width="2.34" height="33.0" fill="var(--down)"/>
<line x1="220.3" y1="354.5" x2="220.3" y2="460.1" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="355.1" width="2.34" height="94.5" fill="var(--down)"/>
<line x1="224.1" y1="456.8" x2="224.1" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="491.0" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="227.8" y1="457.7" x2="227.8" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="467.3" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="231.6" y1="465.5" x2="231.6" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="465.5" width="2.34" height="33.6" fill="var(--down)"/>
<line x1="235.4" y1="469.7" x2="235.4" y2="527.6" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="471.8" width="2.34" height="41.4" fill="var(--up)"/>
<line x1="239.2" y1="453.5" x2="239.2" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="453.5" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="242.9" y1="392.3" x2="242.9" y2="477.8" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="411.8" width="2.34" height="36.0" fill="var(--up)"/>
<line x1="246.7" y1="368.0" x2="246.7" y2="430.1" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="372.8" width="2.34" height="37.2" fill="var(--up)"/>
<line x1="250.5" y1="365.0" x2="250.5" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="377.3" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="254.3" y1="338.9" x2="254.3" y2="393.5" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="350.3" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="258.0" y1="348.5" x2="258.0" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="353.9" width="2.34" height="56.1" fill="var(--down)"/>
<line x1="261.8" y1="404.3" x2="261.8" y2="446.3" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="427.7" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="265.6" y1="445.4" x2="265.6" y2="510.2" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="458.0" width="2.34" height="31.2" fill="var(--down)"/>
<line x1="269.3" y1="433.4" x2="269.3" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="444.2" width="2.34" height="45.0" fill="var(--up)"/>
<line x1="273.1" y1="431.6" x2="273.1" y2="517.4" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="436.1" width="2.34" height="56.4" fill="var(--down)"/>
<line x1="276.9" y1="483.8" x2="276.9" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="501.2" width="2.34" height="53.4" fill="var(--down)"/>
<line x1="280.7" y1="543.8" x2="280.7" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="560.9" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="284.4" y1="512.6" x2="284.4" y2="574.7" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="554.9" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="288.2" y1="547.4" x2="288.2" y2="606.5" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="556.4" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="292.0" y1="519.2" x2="292.0" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="543.8" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="295.7" y1="477.8" x2="295.7" y2="553.7" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="482.0" width="2.34" height="59.7" fill="var(--up)"/>
<line x1="299.5" y1="489.8" x2="299.5" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="493.4" width="2.34" height="38.1" fill="var(--down)"/>
<line x1="303.3" y1="477.8" x2="303.3" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="485.0" width="2.34" height="42.0" fill="var(--up)"/>
<line x1="307.1" y1="477.5" x2="307.1" y2="506.6" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="491.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="310.8" y1="459.5" x2="310.8" y2="497.9" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="468.2" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="314.6" y1="447.8" x2="314.6" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="451.7" width="2.34" height="22.8" fill="var(--up)"/>
<line x1="318.4" y1="458.9" x2="318.4" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="460.1" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="322.1" y1="417.5" x2="322.1" y2="486.2" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="461.9" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="325.9" y1="474.5" x2="325.9" y2="507.8" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="486.8" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="329.7" y1="487.4" x2="329.7" y2="540.8" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="488.9" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="333.5" y1="445.1" x2="333.5" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="452.6" width="2.34" height="42.6" fill="var(--up)"/>
<line x1="337.2" y1="415.4" x2="337.2" y2="452.6" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="419.3" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="341.0" y1="406.1" x2="341.0" y2="446.6" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="422.9" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="344.8" y1="424.4" x2="344.8" y2="442.1" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="433.7" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="348.5" y1="398.3" x2="348.5" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="426.8" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="352.3" y1="427.7" x2="352.3" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="436.7" width="2.34" height="38.4" fill="var(--down)"/>
<line x1="356.1" y1="461.9" x2="356.1" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="473.6" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="359.9" y1="476.6" x2="359.9" y2="525.2" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="493.4" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="363.6" y1="474.2" x2="363.6" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="476.9" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="367.4" y1="468.8" x2="367.4" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="471.8" width="2.34" height="43.5" fill="var(--down)"/>
<line x1="371.2" y1="499.1" x2="371.2" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="517.4" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="375.0" y1="474.8" x2="375.0" y2="526.4" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="510.5" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="378.7" y1="449.0" x2="378.7" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="452.0" width="2.34" height="54.0" fill="var(--up)"/>
<line x1="382.5" y1="459.5" x2="382.5" y2="489.8" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="464.3" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="386.3" y1="449.9" x2="386.3" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="460.1" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="390.0" y1="457.7" x2="390.0" y2="482.0" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="466.4" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="393.8" y1="454.1" x2="393.8" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="457.7" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="397.6" y1="467.3" x2="397.6" y2="495.8" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="470.6" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="401.4" y1="470.9" x2="401.4" y2="490.4" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="477.5" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="405.1" y1="483.8" x2="405.1" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="485.6" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="408.9" y1="478.4" x2="408.9" y2="514.4" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="491.9" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="412.7" y1="475.4" x2="412.7" y2="505.1" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="481.1" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="416.4" y1="472.7" x2="416.4" y2="494.3" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="476.9" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="420.2" y1="464.0" x2="420.2" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="470.6" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="424.0" y1="470.6" x2="424.0" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="474.2" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="427.8" y1="461.3" x2="427.8" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="466.4" width="2.34" height="26.1" fill="var(--up)"/>
<line x1="431.5" y1="477.8" x2="431.5" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="478.1" width="2.34" height="24.9" fill="var(--down)"/>
<line x1="435.3" y1="446.6" x2="435.3" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="465.5" width="2.34" height="35.4" fill="var(--up)"/>
<line x1="439.1" y1="449.0" x2="439.1" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="457.4" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="442.8" y1="447.8" x2="442.8" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="455.6" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="446.6" y1="450.5" x2="446.6" y2="495.8" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="455.9" width="2.34" height="23.1" fill="var(--down)"/>
<line x1="450.4" y1="458.0" x2="450.4" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="473.6" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="454.2" y1="470.6" x2="454.2" y2="502.7" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="477.5" width="2.34" height="18.3" fill="var(--down)"/>
<line x1="457.9" y1="473.9" x2="457.9" y2="503.3" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="480.2" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="461.7" y1="454.1" x2="461.7" y2="477.8" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="466.4" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="465.5" y1="469.7" x2="465.5" y2="491.0" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="469.7" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="469.2" y1="468.5" x2="469.2" y2="481.7" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="476.9" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="473.0" y1="475.4" x2="473.0" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="482.0" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="476.8" y1="492.2" x2="476.8" y2="519.2" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="504.2" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="480.6" y1="521.3" x2="480.6" y2="555.5" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="525.5" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="484.3" y1="515.3" x2="484.3" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="536.0" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="488.1" y1="531.2" x2="488.1" y2="565.1" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="536.9" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="491.9" y1="539.9" x2="491.9" y2="568.1" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="547.7" width="2.34" height="17.7" fill="var(--up)"/>
<line x1="495.7" y1="484.7" x2="495.7" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="486.2" width="2.34" height="61.8" fill="var(--up)"/>
<line x1="499.4" y1="486.8" x2="499.4" y2="508.1" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="491.3" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="503.2" y1="470.6" x2="503.2" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="475.4" width="2.34" height="29.4" fill="var(--up)"/>
<line x1="507.0" y1="463.7" x2="507.0" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="468.5" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="510.7" y1="437.3" x2="510.7" y2="470.6" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="438.8" width="2.34" height="29.7" fill="var(--up)"/>
<line x1="514.5" y1="434.3" x2="514.5" y2="452.0" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="442.7" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="518.3" y1="397.1" x2="518.3" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="410.6" width="2.34" height="33.9" fill="var(--up)"/>
<line x1="522.1" y1="386.0" x2="522.1" y2="416.6" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="394.4" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="525.8" y1="376.1" x2="525.8" y2="396.8" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="393.5" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="529.6" y1="401.3" x2="529.6" y2="422.0" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="404.6" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="533.4" y1="380.9" x2="533.4" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="387.5" width="2.34" height="30.0" fill="var(--up)"/>
<line x1="537.1" y1="392.0" x2="537.1" y2="416.6" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="392.0" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="540.9" y1="385.4" x2="540.9" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="389.6" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="544.7" y1="381.5" x2="544.7" y2="407.3" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="388.7" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="548.5" y1="396.2" x2="548.5" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="397.7" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="552.2" y1="394.7" x2="552.2" y2="425.3" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="398.6" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="556.0" y1="394.7" x2="556.0" y2="413.9" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="398.0" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="559.8" y1="394.4" x2="559.8" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="398.9" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="563.5" y1="386.6" x2="563.5" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="396.5" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="567.3" y1="388.1" x2="567.3" y2="409.7" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="398.3" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="571.1" y1="379.7" x2="571.1" y2="403.1" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="387.5" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="574.9" y1="380.9" x2="574.9" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="386.6" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="578.6" y1="398.0" x2="578.6" y2="417.2" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="398.0" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="582.4" y1="401.6" x2="582.4" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="413.6" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="586.2" y1="425.0" x2="586.2" y2="450.8" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="425.0" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="589.9" y1="415.7" x2="589.9" y2="441.2" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="419.9" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="593.7" y1="396.8" x2="593.7" y2="440.6" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="406.1" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="597.5" y1="400.1" x2="597.5" y2="414.2" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="403.4" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="601.3" y1="394.7" x2="601.3" y2="413.0" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="400.1" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="605.0" y1="396.5" x2="605.0" y2="414.8" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="401.6" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="608.8" y1="402.8" x2="608.8" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="403.4" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="612.6" y1="401.9" x2="612.6" y2="416.0" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="411.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="616.3" y1="389.3" x2="616.3" y2="415.7" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="406.7" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="620.1" y1="396.2" x2="620.1" y2="413.3" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="396.8" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="623.9" y1="392.9" x2="623.9" y2="404.3" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="397.7" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="627.7" y1="395.0" x2="627.7" y2="417.8" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="395.6" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="631.4" y1="377.9" x2="631.4" y2="401.6" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="379.1" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="635.2" y1="368.6" x2="635.2" y2="382.1" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="377.3" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="639.0" y1="365.9" x2="639.0" y2="378.2" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="369.8" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="642.8" y1="360.5" x2="642.8" y2="390.2" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="366.5" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="646.5" y1="375.8" x2="646.5" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="379.4" width="2.34" height="39.9" fill="var(--up)"/>
<line x1="650.3" y1="352.1" x2="650.3" y2="382.4" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="353.3" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="654.1" y1="336.5" x2="654.1" y2="356.0" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="336.5" width="2.34" height="17.7" fill="var(--up)"/>
<line x1="657.8" y1="335.6" x2="657.8" y2="345.2" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="336.8" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="661.6" y1="337.1" x2="661.6" y2="359.0" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="338.6" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="665.4" y1="328.1" x2="665.4" y2="349.4" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="329.6" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="669.2" y1="308.6" x2="669.2" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="310.7" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="672.9" y1="307.4" x2="672.9" y2="318.5" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="307.7" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="676.7" y1="307.4" x2="676.7" y2="332.3" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="308.6" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="680.5" y1="330.8" x2="680.5" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="331.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="684.2" y1="324.2" x2="684.2" y2="336.5" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="324.5" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="688.0" y1="327.2" x2="688.0" y2="346.4" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="328.7" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="691.8" y1="329.0" x2="691.8" y2="356.6" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="335.9" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="695.6" y1="323.6" x2="695.6" y2="351.8" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="324.5" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="699.3" y1="323.9" x2="699.3" y2="347.0" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="324.8" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="703.1" y1="329.3" x2="703.1" y2="342.8" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="333.8" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="706.9" y1="316.4" x2="706.9" y2="331.1" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="317.3" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="710.6" y1="318.5" x2="710.6" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="320.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="714.4" y1="318.8" x2="714.4" y2="337.1" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="321.5" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="718.2" y1="329.9" x2="718.2" y2="378.5" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="332.0" width="2.34" height="29.1" fill="var(--down)"/>
<line x1="722.0" y1="353.9" x2="722.0" y2="368.0" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="359.0" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="725.7" y1="347.6" x2="725.7" y2="363.5" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="349.7" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="729.5" y1="341.9" x2="729.5" y2="363.5" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="344.0" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="733.3" y1="332.9" x2="733.3" y2="367.4" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="334.7" width="2.34" height="29.1" fill="var(--up)"/>
<line x1="737.0" y1="323.6" x2="737.0" y2="335.3" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="326.0" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="740.8" y1="319.4" x2="740.8" y2="330.2" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="326.9" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="744.6" y1="324.8" x2="744.6" y2="347.3" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="338.0" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="748.4" y1="321.8" x2="748.4" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="325.7" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="752.1" y1="322.7" x2="752.1" y2="331.7" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="326.0" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="755.9" y1="314.6" x2="755.9" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="314.6" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="759.7" y1="326.0" x2="759.7" y2="340.1" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="327.8" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="763.5" y1="337.1" x2="763.5" y2="363.8" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="339.5" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="767.2" y1="332.3" x2="767.2" y2="352.4" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="341.9" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="771.0" y1="331.1" x2="771.0" y2="358.7" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="335.9" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="774.8" y1="350.9" x2="774.8" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="362.9" width="2.34" height="52.8" fill="var(--down)"/>
<line x1="778.5" y1="383.3" x2="778.5" y2="466.1" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="416.3" width="2.34" height="26.1" fill="var(--up)"/>
<line x1="782.3" y1="384.8" x2="782.3" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="385.4" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="786.1" y1="350.3" x2="786.1" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="355.4" width="2.34" height="38.4" fill="var(--up)"/>
<line x1="789.9" y1="347.0" x2="789.9" y2="371.9" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="355.1" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="793.6" y1="355.4" x2="793.6" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="362.0" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="797.4" y1="331.1" x2="797.4" y2="347.6" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="335.9" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="801.2" y1="336.8" x2="801.2" y2="356.3" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="346.7" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="804.9" y1="331.1" x2="804.9" y2="343.4" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="331.4" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="808.7" y1="333.2" x2="808.7" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="339.5" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="812.5" y1="329.3" x2="812.5" y2="340.1" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="337.7" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="816.3" y1="324.2" x2="816.3" y2="337.4" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="324.5" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="820.0" y1="304.4" x2="820.0" y2="327.2" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="308.3" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="823.8" y1="298.4" x2="823.8" y2="316.1" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="302.6" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="827.6" y1="308.3" x2="827.6" y2="320.6" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="308.6" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="831.3" y1="308.9" x2="831.3" y2="326.0" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="311.0" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="835.1" y1="301.1" x2="835.1" y2="308.9" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="303.8" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="838.9" y1="302.0" x2="838.9" y2="324.5" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="302.9" width="2.34" height="16.2" fill="var(--down)"/>
<line x1="842.7" y1="307.7" x2="842.7" y2="316.7" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="311.9" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="846.4" y1="300.2" x2="846.4" y2="313.4" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="304.7" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="850.2" y1="292.7" x2="850.2" y2="312.8" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="293.0" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="854.0" y1="288.2" x2="854.0" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="292.7" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="857.7" y1="285.5" x2="857.7" y2="312.5" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="292.4" width="2.34" height="18.0" fill="var(--up)"/>
<line x1="861.5" y1="285.5" x2="861.5" y2="298.4" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="289.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="865.3" y1="279.8" x2="865.3" y2="291.2" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="280.7" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="869.1" y1="277.7" x2="869.1" y2="291.8" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="282.8" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="872.8" y1="281.3" x2="872.8" y2="295.1" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="283.7" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="876.6" y1="291.2" x2="876.6" y2="320.0" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="291.8" width="2.34" height="28.2" fill="var(--down)"/>
<line x1="880.4" y1="293.6" x2="880.4" y2="315.2" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="296.9" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="884.2" y1="285.8" x2="884.2" y2="300.5" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="286.1" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="887.9" y1="278.6" x2="887.9" y2="296.0" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="283.4" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="891.7" y1="306.5" x2="891.7" y2="319.7" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="306.8" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="895.5" y1="296.6" x2="895.5" y2="316.1" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="305.0" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="899.2" y1="303.8" x2="899.2" y2="318.8" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="307.4" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="903.0" y1="286.4" x2="903.0" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="288.8" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="906.8" y1="294.2" x2="906.8" y2="307.1" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="296.0" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="910.6" y1="294.8" x2="910.6" y2="305.9" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="296.9" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="914.3" y1="294.5" x2="914.3" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="298.4" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="918.1" y1="297.5" x2="918.1" y2="309.8" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="300.5" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="921.9" y1="296.0" x2="921.9" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="298.4" width="2.34" height="3.3" fill="var(--up)"/>
<line x1="925.6" y1="287.6" x2="925.6" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="288.5" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="929.4" y1="285.2" x2="929.4" y2="291.5" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="285.8" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="933.2" y1="281.3" x2="933.2" y2="298.4" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="284.3" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="937.0" y1="281.9" x2="937.0" y2="291.5" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="282.8" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="940.7" y1="294.2" x2="940.7" y2="305.0" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="294.2" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="944.5" y1="288.2" x2="944.5" y2="296.9" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="293.0" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="948.3" y1="288.5" x2="948.3" y2="296.3" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="288.5" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="952.0" y1="288.2" x2="952.0" y2="299.0" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="289.7" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="955.8" y1="305.0" x2="955.8" y2="329.0" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="316.7" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="959.6" y1="307.1" x2="959.6" y2="344.9" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="330.8" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="963.4" y1="323.9" x2="963.4" y2="353.0" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="333.2" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="967.1" y1="327.5" x2="967.1" y2="361.4" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="339.5" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="970.9" y1="329.6" x2="970.9" y2="355.7" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="331.7" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="974.7" y1="302.9" x2="974.7" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="319.7" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="978.4" y1="295.7" x2="978.4" y2="322.1" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="299.0" width="2.34" height="23.1" fill="var(--up)"/>
<line x1="982.2" y1="298.4" x2="982.2" y2="313.7" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="299.6" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="986.0" y1="302.3" x2="986.0" y2="319.1" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="305.3" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="989.8" y1="311.3" x2="989.8" y2="327.8" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="314.3" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="993.5" y1="314.0" x2="993.5" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="316.1" width="2.34" height="18.6" fill="var(--down)"/>
<line x1="997.3" y1="317.9" x2="997.3" y2="341.6" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="321.2" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="1001.1" y1="307.7" x2="1001.1" y2="317.3" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="309.2" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="1004.9" y1="321.5" x2="1004.9" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="324.8" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="1008.6" y1="318.5" x2="1008.6" y2="335.9" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="320.3" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="1012.4" y1="313.4" x2="1012.4" y2="327.2" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="314.3" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="1016.2" y1="318.8" x2="1016.2" y2="324.2" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="320.3" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="1019.9" y1="317.0" x2="1019.9" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="320.0" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="1023.7" y1="321.2" x2="1023.7" y2="332.3" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="326.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1027.5" y1="323.3" x2="1027.5" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="328.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1031.3" y1="325.4" x2="1031.3" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="326.3" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="1035.0" y1="332.3" x2="1035.0" y2="344.3" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="334.1" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="1038.8" y1="327.8" x2="1038.8" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="330.2" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="1042.6" y1="322.7" x2="1042.6" y2="336.2" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="327.2" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="1046.3" y1="326.3" x2="1046.3" y2="334.4" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="327.2" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="1050.1" y1="326.3" x2="1050.1" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="327.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="60" y1="302.7" x2="1052" y2="302.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="306.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$81 R1</text>
<text x="1058" y="318.2" font-size="9.5" fill="var(--muted)">터치 11회</text>
<line x1="60" y1="87.6" x2="1052" y2="87.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="91.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$88 R2</text>
<text x="1058" y="103.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="338.9" x2="1052" y2="338.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="332.9" font-size="11.5" fill="var(--support)" font-weight="600">$79 S1</text>
<text x="1058" y="344.9" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="426.6" x2="1052" y2="426.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="420.6" font-size="11.5" fill="var(--support)" font-weight="600">$76 S2</text>
<text x="1058" y="432.6" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="539.5" x2="1052" y2="539.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="533.5" font-size="11.5" fill="var(--support)" font-weight="600">$73 S3</text>
<text x="1058" y="545.5" font-size="9.5" fill="var(--muted)">터치 8회</text>
<circle cx="1052.0" cy="327.2" r="3" fill="var(--ink)"/>
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

- **상승**: 신용스프레드 축소 — 저신용 기업의 자금조달 여건 개선, 위험선호 확대 신호로 흔히 해석된다.
- **하락**: 신용스프레드 확대 — 저신용 기업의 자금조달 리스크 부각, 위험회피 심리 신호로 흔히 해석된다.
- 정확한 신용스프레드가 아니라 ETF **가격**의 프록시다 — 정밀한 스프레드 수치가 필요하면 FRED의 ICE BofA 하이일드 스프레드(`BAMLH0A0HYM2`) 같은 원출처를 확인한다.

---

## 관련 문서

- [거시경제 개념 정리](../../concepts/macroeconomics.md) — "주요 지표 읽는 법 요약" 표의 신용스프레드 행
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — iShares iBoxx High Yield Corporate Bond ETF (HYG)](https://finance.yahoo.com/quote/HYG/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
