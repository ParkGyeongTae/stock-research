# 하이일드 회사채 ETF (HYG)

!!! note ""
    최근 5년간 iShares 하이일드 회사채 ETF(`HYG`)의 주간 가격을 지지선·저항선과 함께 정리한 참고 자료다. 이 ETF는 신용등급이 낮은(투기등급) 회사채를 담고 있다. 가격이 내려가면(=수익률은 올라가면) **신용스프레드가 벌어지고 있다**는, 즉 시장이 신용등급 낮은 기업들의 자금조달 위험을 더 크게 보고 있다는 신호로 흔히 읽힌다.

    ⚠️ **정확한 신용스프레드 수치는 아니다** — 이 문서가 보여주는 것은 ETF의 **가격**일 뿐, FRED의 ICE BofA 하이일드 스프레드(`BAMLH0A0HYM2`) 같은 실제 신용스프레드 지표가 아니다. 가격 방향이 대체로 스프레드와 반대로 움직이는 참고용 지표(프록시)일 뿐이니, 정밀한 스프레드 수치가 필요하면 원출처를 따로 확인한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="hyg-chart">
<style>
.hyg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .hyg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 $79.61 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="618.5" x2="1052" y2="618.5" class="grid"/>
<text x="52" y="622.5" font-size="11" text-anchor="end" fill="var(--muted)">70.00</text>
<line x1="60" y1="543.5" x2="1052" y2="543.5" class="grid"/>
<text x="52" y="547.5" font-size="11" text-anchor="end" fill="var(--muted)">72.50</text>
<line x1="60" y1="468.5" x2="1052" y2="468.5" class="grid"/>
<text x="52" y="472.5" font-size="11" text-anchor="end" fill="var(--muted)">75.00</text>
<line x1="60" y1="393.5" x2="1052" y2="393.5" class="grid"/>
<text x="52" y="397.5" font-size="11" text-anchor="end" fill="var(--muted)">77.50</text>
<line x1="60" y1="318.5" x2="1052" y2="318.5" class="grid"/>
<text x="52" y="322.5" font-size="11" text-anchor="end" fill="var(--muted)">80.00</text>
<line x1="60" y1="243.5" x2="1052" y2="243.5" class="grid"/>
<text x="52" y="247.5" font-size="11" text-anchor="end" fill="var(--muted)">82.50</text>
<line x1="60" y1="168.5" x2="1052" y2="168.5" class="grid"/>
<text x="52" y="172.5" font-size="11" text-anchor="end" fill="var(--muted)">85.00</text>
<line x1="60" y1="93.5" x2="1052" y2="93.5" class="grid"/>
<text x="52" y="97.5" font-size="11" text-anchor="end" fill="var(--muted)">87.50</text>
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
<line x1="61.9" y1="78.8" x2="61.9" y2="96.2" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="79.7" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="65.7" y1="75.5" x2="65.7" y2="83.9" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="78.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="69.5" y1="75.8" x2="69.5" y2="87.2" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="78.8" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="73.3" y1="74.3" x2="73.3" y2="81.8" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="78.5" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="77.0" y1="73.7" x2="77.0" y2="92.0" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="81.2" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="80.8" y1="81.8" x2="80.8" y2="104.3" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="85.7" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="84.6" y1="97.1" x2="84.6" y2="115.7" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="98.0" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="88.4" y1="96.8" x2="88.4" y2="123.8" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="101.9" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="92.2" y1="99.8" x2="92.2" y2="114.5" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="107.9" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="96.0" y1="102.5" x2="96.0" y2="115.4" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="110.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="99.8" y1="91.7" x2="99.8" y2="122.0" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="93.5" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="103.5" y1="90.2" x2="103.5" y2="113.9" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="90.8" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="107.3" y1="110.9" x2="107.3" y2="121.7" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="111.2" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="111.1" y1="118.4" x2="111.1" y2="158.3" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="119.3" width="2.35" height="35.1" fill="var(--down)"/>
<line x1="114.9" y1="134.6" x2="114.9" y2="158.9" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="138.5" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="118.7" y1="106.4" x2="118.7" y2="138.5" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="119.6" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="122.5" y1="113.3" x2="122.5" y2="132.2" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="119.6" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="126.3" y1="102.2" x2="126.3" y2="135.8" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="103.7" width="2.35" height="30.9" fill="var(--up)"/>
<line x1="130.0" y1="98.9" x2="130.0" y2="109.1" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="103.4" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="133.8" y1="108.5" x2="133.8" y2="142.7" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="110.9" width="2.35" height="31.5" fill="var(--down)"/>
<line x1="137.6" y1="122.9" x2="137.6" y2="157.4" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="135.8" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="141.4" y1="139.4" x2="141.4" y2="158.6" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="143.3" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="145.2" y1="142.4" x2="145.2" y2="200.0" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="162.8" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="149.0" y1="169.7" x2="149.0" y2="222.5" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="183.5" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="152.8" y1="194.9" x2="152.8" y2="245.0" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="212.3" width="2.35" height="26.4" fill="var(--down)"/>
<line x1="156.5" y1="223.1" x2="156.5" y2="251.9" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="231.8" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="160.3" y1="209.6" x2="160.3" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="210.2" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="164.1" y1="202.1" x2="164.1" y2="252.2" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="221.9" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="167.9" y1="246.2" x2="167.9" y2="292.7" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="246.8" width="2.35" height="43.8" fill="var(--down)"/>
<line x1="171.7" y1="242.3" x2="171.7" y2="322.1" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="242.6" width="2.35" height="50.4" fill="var(--up)"/>
<line x1="175.5" y1="245.0" x2="175.5" y2="280.7" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="246.8" width="2.35" height="32.1" fill="var(--down)"/>
<line x1="179.3" y1="232.7" x2="179.3" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="260.0" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="183.1" y1="241.1" x2="183.1" y2="311.6" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="257.9" width="2.35" height="53.4" fill="var(--down)"/>
<line x1="186.8" y1="291.8" x2="186.8" y2="331.1" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="311.3" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="190.6" y1="302.3" x2="190.6" y2="343.4" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="313.7" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="194.4" y1="318.5" x2="194.4" y2="364.1" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="336.5" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="198.2" y1="329.0" x2="198.2" y2="396.2" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="373.7" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="202.0" y1="392.6" x2="202.0" y2="426.5" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="404.6" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="205.8" y1="409.7" x2="205.8" y2="442.4" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="413.3" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="209.6" y1="312.8" x2="209.6" y2="422.0" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="312.8" width="2.35" height="106.5" fill="var(--up)"/>
<line x1="213.3" y1="322.7" x2="213.3" y2="362.9" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="326.3" width="2.35" height="33.0" fill="var(--down)"/>
<line x1="217.1" y1="354.5" x2="217.1" y2="460.1" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="355.1" width="2.35" height="94.5" fill="var(--down)"/>
<line x1="220.9" y1="456.8" x2="220.9" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="491.0" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="224.7" y1="457.7" x2="224.7" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="467.3" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="228.5" y1="465.5" x2="228.5" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="465.5" width="2.35" height="33.6" fill="var(--down)"/>
<line x1="232.3" y1="469.7" x2="232.3" y2="527.6" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="471.8" width="2.35" height="41.4" fill="var(--up)"/>
<line x1="236.1" y1="453.5" x2="236.1" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="453.5" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="239.8" y1="392.3" x2="239.8" y2="477.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="411.8" width="2.35" height="36.0" fill="var(--up)"/>
<line x1="243.6" y1="368.0" x2="243.6" y2="430.1" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="372.8" width="2.35" height="37.2" fill="var(--up)"/>
<line x1="247.4" y1="365.0" x2="247.4" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="377.3" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="251.2" y1="338.9" x2="251.2" y2="393.5" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="350.3" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="255.0" y1="348.5" x2="255.0" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="353.9" width="2.35" height="56.1" fill="var(--down)"/>
<line x1="258.8" y1="404.3" x2="258.8" y2="446.3" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="427.7" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="262.6" y1="445.4" x2="262.6" y2="510.2" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="458.0" width="2.35" height="31.2" fill="var(--down)"/>
<line x1="266.4" y1="433.4" x2="266.4" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="444.2" width="2.35" height="45.0" fill="var(--up)"/>
<line x1="270.1" y1="431.6" x2="270.1" y2="517.4" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="436.1" width="2.35" height="56.4" fill="var(--down)"/>
<line x1="273.9" y1="483.8" x2="273.9" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="501.2" width="2.35" height="53.4" fill="var(--down)"/>
<line x1="277.7" y1="543.8" x2="277.7" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="560.9" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="281.5" y1="512.6" x2="281.5" y2="574.7" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="554.9" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="285.3" y1="547.4" x2="285.3" y2="606.5" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="556.4" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="289.1" y1="519.2" x2="289.1" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="543.8" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="292.9" y1="477.8" x2="292.9" y2="553.7" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="482.0" width="2.35" height="59.7" fill="var(--up)"/>
<line x1="296.6" y1="489.8" x2="296.6" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="493.4" width="2.35" height="38.1" fill="var(--down)"/>
<line x1="300.4" y1="477.8" x2="300.4" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="485.0" width="2.35" height="42.0" fill="var(--up)"/>
<line x1="304.2" y1="477.5" x2="304.2" y2="506.6" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="491.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="308.0" y1="459.5" x2="308.0" y2="497.9" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="468.2" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="311.8" y1="447.8" x2="311.8" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="451.7" width="2.35" height="22.8" fill="var(--up)"/>
<line x1="315.6" y1="458.9" x2="315.6" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="460.1" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="319.4" y1="417.5" x2="319.4" y2="486.2" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="461.9" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="323.1" y1="474.5" x2="323.1" y2="507.8" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="486.8" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="326.9" y1="487.4" x2="326.9" y2="540.8" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="488.9" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="330.7" y1="445.1" x2="330.7" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="452.6" width="2.35" height="42.6" fill="var(--up)"/>
<line x1="334.5" y1="415.4" x2="334.5" y2="452.6" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="419.3" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="338.3" y1="406.1" x2="338.3" y2="446.6" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="422.9" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="342.1" y1="424.4" x2="342.1" y2="442.1" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="433.7" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="345.9" y1="398.3" x2="345.9" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="426.8" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="349.6" y1="427.7" x2="349.6" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="436.7" width="2.35" height="38.4" fill="var(--down)"/>
<line x1="353.4" y1="461.9" x2="353.4" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="473.6" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="357.2" y1="476.6" x2="357.2" y2="525.2" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="493.4" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="361.0" y1="474.2" x2="361.0" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="476.9" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="364.8" y1="468.8" x2="364.8" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="471.8" width="2.35" height="43.5" fill="var(--down)"/>
<line x1="368.6" y1="499.1" x2="368.6" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="517.4" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="372.4" y1="474.8" x2="372.4" y2="526.4" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="510.5" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="376.2" y1="449.0" x2="376.2" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="452.0" width="2.35" height="54.0" fill="var(--up)"/>
<line x1="379.9" y1="459.5" x2="379.9" y2="489.8" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="464.3" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="383.7" y1="449.9" x2="383.7" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="460.1" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="387.5" y1="457.7" x2="387.5" y2="482.0" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="466.4" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="391.3" y1="454.1" x2="391.3" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="457.7" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="395.1" y1="467.3" x2="395.1" y2="495.8" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="470.6" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="398.9" y1="470.9" x2="398.9" y2="490.4" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="477.5" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="402.7" y1="483.8" x2="402.7" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="485.6" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="406.4" y1="478.4" x2="406.4" y2="514.4" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="491.9" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="410.2" y1="475.4" x2="410.2" y2="505.1" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="481.1" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="414.0" y1="472.7" x2="414.0" y2="494.3" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="476.9" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="417.8" y1="464.0" x2="417.8" y2="486.2" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="470.6" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="421.6" y1="470.6" x2="421.6" y2="498.5" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="474.2" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="425.4" y1="461.3" x2="425.4" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="466.4" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="429.2" y1="477.8" x2="429.2" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="478.1" width="2.35" height="24.9" fill="var(--down)"/>
<line x1="432.9" y1="446.6" x2="432.9" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="465.5" width="2.35" height="35.4" fill="var(--up)"/>
<line x1="436.7" y1="449.0" x2="436.7" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="457.4" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="440.5" y1="447.8" x2="440.5" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="455.6" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="444.3" y1="450.5" x2="444.3" y2="495.8" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="455.9" width="2.35" height="23.1" fill="var(--down)"/>
<line x1="448.1" y1="458.0" x2="448.1" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="473.6" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="451.9" y1="470.6" x2="451.9" y2="502.7" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="477.5" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="455.7" y1="473.9" x2="455.7" y2="503.3" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="480.2" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="459.5" y1="454.1" x2="459.5" y2="477.8" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="466.4" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="463.2" y1="469.7" x2="463.2" y2="491.0" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="469.7" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="467.0" y1="468.5" x2="467.0" y2="481.7" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="476.9" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="470.8" y1="475.4" x2="470.8" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="482.0" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="474.6" y1="492.2" x2="474.6" y2="519.2" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="504.2" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="478.4" y1="521.3" x2="478.4" y2="555.5" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="525.5" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="482.2" y1="515.3" x2="482.2" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="536.0" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="486.0" y1="531.2" x2="486.0" y2="565.1" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="536.9" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="489.7" y1="539.9" x2="489.7" y2="568.1" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="547.7" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="493.5" y1="484.7" x2="493.5" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="486.2" width="2.35" height="61.8" fill="var(--up)"/>
<line x1="497.3" y1="486.8" x2="497.3" y2="508.1" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="491.3" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="501.1" y1="470.6" x2="501.1" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="475.4" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="504.9" y1="463.7" x2="504.9" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="468.5" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="508.7" y1="437.3" x2="508.7" y2="470.6" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="438.8" width="2.35" height="29.7" fill="var(--up)"/>
<line x1="512.5" y1="434.3" x2="512.5" y2="452.0" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="442.7" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="516.2" y1="397.1" x2="516.2" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="410.6" width="2.35" height="33.9" fill="var(--up)"/>
<line x1="520.0" y1="386.0" x2="520.0" y2="416.6" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="394.4" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="523.8" y1="376.1" x2="523.8" y2="396.8" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="393.5" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="527.6" y1="401.3" x2="527.6" y2="422.0" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="404.6" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="531.4" y1="380.9" x2="531.4" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="387.5" width="2.35" height="30.0" fill="var(--up)"/>
<line x1="535.2" y1="392.0" x2="535.2" y2="416.6" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="392.0" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="539.0" y1="385.4" x2="539.0" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="389.6" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="542.7" y1="381.5" x2="542.7" y2="407.3" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="388.7" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="546.5" y1="396.2" x2="546.5" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="397.7" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="550.3" y1="394.7" x2="550.3" y2="425.3" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="398.6" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="554.1" y1="394.7" x2="554.1" y2="413.9" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="398.0" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="557.9" y1="394.4" x2="557.9" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="398.9" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="561.7" y1="386.6" x2="561.7" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="396.5" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="565.5" y1="388.1" x2="565.5" y2="409.7" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="398.3" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="569.3" y1="379.7" x2="569.3" y2="403.1" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="387.5" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="573.0" y1="380.9" x2="573.0" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="386.6" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="576.8" y1="398.0" x2="576.8" y2="417.2" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="398.0" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="580.6" y1="401.6" x2="580.6" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="413.6" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="584.4" y1="425.0" x2="584.4" y2="450.8" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="425.0" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="588.2" y1="415.7" x2="588.2" y2="441.2" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="419.9" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="592.0" y1="396.8" x2="592.0" y2="440.6" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="406.1" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="595.8" y1="400.1" x2="595.8" y2="414.2" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="403.4" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="599.5" y1="394.7" x2="599.5" y2="413.0" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="400.1" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="603.3" y1="396.5" x2="603.3" y2="414.8" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="401.6" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="607.1" y1="402.8" x2="607.1" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="403.4" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="610.9" y1="401.9" x2="610.9" y2="416.0" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="411.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="614.7" y1="389.3" x2="614.7" y2="415.7" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="406.7" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="618.5" y1="396.2" x2="618.5" y2="413.3" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="396.8" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="622.3" y1="392.9" x2="622.3" y2="404.3" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="397.7" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="626.0" y1="395.0" x2="626.0" y2="417.8" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="395.6" width="2.35" height="16.8" fill="var(--up)"/>
<line x1="629.8" y1="377.9" x2="629.8" y2="401.6" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="379.1" width="2.35" height="17.1" fill="var(--up)"/>
<line x1="633.6" y1="368.6" x2="633.6" y2="382.1" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="377.3" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="637.4" y1="365.9" x2="637.4" y2="378.2" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="369.8" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="641.2" y1="360.5" x2="641.2" y2="390.2" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="366.5" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="645.0" y1="375.8" x2="645.0" y2="421.1" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="379.4" width="2.35" height="39.9" fill="var(--up)"/>
<line x1="648.8" y1="352.1" x2="648.8" y2="382.4" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="353.3" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="652.5" y1="336.5" x2="652.5" y2="356.0" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="336.5" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="656.3" y1="335.6" x2="656.3" y2="345.2" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="336.8" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="660.1" y1="337.1" x2="660.1" y2="359.0" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="338.6" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="663.9" y1="328.1" x2="663.9" y2="349.4" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="329.6" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="667.7" y1="308.6" x2="667.7" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="310.7" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="671.5" y1="307.4" x2="671.5" y2="318.5" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="307.7" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="675.3" y1="307.4" x2="675.3" y2="332.3" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="308.6" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="679.1" y1="330.8" x2="679.1" y2="341.0" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="331.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="682.8" y1="324.2" x2="682.8" y2="336.5" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="324.5" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="686.6" y1="327.2" x2="686.6" y2="346.4" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="328.7" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="690.4" y1="329.0" x2="690.4" y2="356.6" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="335.9" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="694.2" y1="323.6" x2="694.2" y2="351.8" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="324.5" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="698.0" y1="323.9" x2="698.0" y2="347.0" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="324.8" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="701.8" y1="329.3" x2="701.8" y2="342.8" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="333.8" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="705.6" y1="316.4" x2="705.6" y2="331.1" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="317.3" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="709.3" y1="318.5" x2="709.3" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="320.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="713.1" y1="318.8" x2="713.1" y2="337.1" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="321.5" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="716.9" y1="329.9" x2="716.9" y2="378.5" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="332.0" width="2.35" height="29.1" fill="var(--down)"/>
<line x1="720.7" y1="353.9" x2="720.7" y2="368.0" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="359.0" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="724.5" y1="347.6" x2="724.5" y2="363.5" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="349.7" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="728.3" y1="341.9" x2="728.3" y2="363.5" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="344.0" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="732.1" y1="332.9" x2="732.1" y2="367.4" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="334.7" width="2.35" height="29.1" fill="var(--up)"/>
<line x1="735.8" y1="323.6" x2="735.8" y2="335.3" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="326.0" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="739.6" y1="319.4" x2="739.6" y2="330.2" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="326.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="743.4" y1="324.8" x2="743.4" y2="347.3" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="338.0" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="747.2" y1="321.8" x2="747.2" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="325.7" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="751.0" y1="322.7" x2="751.0" y2="331.7" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="326.0" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="754.8" y1="314.6" x2="754.8" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="314.6" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="758.6" y1="326.0" x2="758.6" y2="340.1" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="327.8" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="762.4" y1="337.1" x2="762.4" y2="363.8" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="339.5" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="766.1" y1="332.3" x2="766.1" y2="352.4" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="341.9" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="769.9" y1="331.1" x2="769.9" y2="358.7" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="335.9" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="773.7" y1="350.9" x2="773.7" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="362.9" width="2.35" height="52.8" fill="var(--down)"/>
<line x1="777.5" y1="383.3" x2="777.5" y2="466.1" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="416.3" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="781.3" y1="384.8" x2="781.3" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="385.4" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="785.1" y1="350.3" x2="785.1" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="355.4" width="2.35" height="38.4" fill="var(--up)"/>
<line x1="788.9" y1="347.0" x2="788.9" y2="371.9" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="355.1" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="792.6" y1="355.4" x2="792.6" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="362.0" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="796.4" y1="331.1" x2="796.4" y2="347.6" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="335.9" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="800.2" y1="336.8" x2="800.2" y2="356.3" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="346.7" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="804.0" y1="331.1" x2="804.0" y2="343.4" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="331.4" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="807.8" y1="333.2" x2="807.8" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="339.5" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="811.6" y1="329.3" x2="811.6" y2="340.1" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="337.7" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="815.4" y1="324.2" x2="815.4" y2="337.4" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="324.5" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="819.1" y1="304.4" x2="819.1" y2="327.2" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="308.3" width="2.35" height="17.1" fill="var(--up)"/>
<line x1="822.9" y1="298.4" x2="822.9" y2="316.1" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="302.6" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="826.7" y1="308.3" x2="826.7" y2="320.6" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="308.6" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="830.5" y1="308.9" x2="830.5" y2="326.0" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="311.0" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="834.3" y1="301.1" x2="834.3" y2="308.9" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="303.8" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="838.1" y1="302.0" x2="838.1" y2="324.5" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="302.9" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="841.9" y1="307.7" x2="841.9" y2="316.7" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="311.9" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="845.6" y1="300.2" x2="845.6" y2="313.4" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="304.7" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="849.4" y1="292.7" x2="849.4" y2="312.8" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="293.0" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="853.2" y1="288.2" x2="853.2" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="292.7" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="857.0" y1="285.5" x2="857.0" y2="312.5" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="292.4" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="860.8" y1="285.5" x2="860.8" y2="298.4" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="289.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="864.6" y1="279.8" x2="864.6" y2="291.2" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="280.7" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="868.4" y1="277.7" x2="868.4" y2="291.8" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="282.8" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="872.2" y1="281.3" x2="872.2" y2="295.1" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="283.7" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="875.9" y1="291.2" x2="875.9" y2="320.0" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="291.8" width="2.35" height="28.2" fill="var(--down)"/>
<line x1="879.7" y1="293.6" x2="879.7" y2="315.2" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="296.9" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="883.5" y1="285.8" x2="883.5" y2="300.5" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="286.1" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="887.3" y1="278.6" x2="887.3" y2="296.0" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="283.4" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="891.1" y1="306.5" x2="891.1" y2="319.7" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="306.8" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="894.9" y1="296.6" x2="894.9" y2="316.1" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="305.0" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="898.7" y1="303.8" x2="898.7" y2="318.8" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="307.4" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="902.4" y1="286.4" x2="902.4" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="288.8" width="2.35" height="17.1" fill="var(--up)"/>
<line x1="906.2" y1="294.2" x2="906.2" y2="307.1" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="296.0" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="910.0" y1="294.8" x2="910.0" y2="305.9" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="296.9" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="913.8" y1="294.5" x2="913.8" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="298.4" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="917.6" y1="297.5" x2="917.6" y2="309.8" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="300.5" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="921.4" y1="296.0" x2="921.4" y2="302.0" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="298.4" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="925.2" y1="287.6" x2="925.2" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="288.5" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="928.9" y1="285.2" x2="928.9" y2="291.5" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="285.8" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="932.7" y1="281.3" x2="932.7" y2="298.4" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="284.3" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="936.5" y1="281.9" x2="936.5" y2="291.5" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="282.8" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="940.3" y1="294.2" x2="940.3" y2="305.0" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="294.2" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="944.1" y1="288.2" x2="944.1" y2="296.9" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="293.0" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="947.9" y1="288.5" x2="947.9" y2="296.3" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="288.5" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="951.7" y1="288.2" x2="951.7" y2="299.0" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="289.7" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="955.5" y1="305.0" x2="955.5" y2="329.0" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="316.7" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="959.2" y1="307.1" x2="959.2" y2="344.9" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="330.8" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="963.0" y1="323.9" x2="963.0" y2="353.0" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="333.2" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="966.8" y1="327.5" x2="966.8" y2="361.4" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="339.5" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="970.6" y1="329.6" x2="970.6" y2="355.7" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="331.7" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="974.4" y1="302.9" x2="974.4" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="319.7" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="978.2" y1="295.7" x2="978.2" y2="322.1" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="299.0" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="982.0" y1="298.4" x2="982.0" y2="313.7" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="299.6" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="985.7" y1="302.3" x2="985.7" y2="319.1" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="305.3" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="989.5" y1="311.3" x2="989.5" y2="327.8" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="314.3" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="993.3" y1="314.0" x2="993.3" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="316.1" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="997.1" y1="317.9" x2="997.1" y2="341.6" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="321.2" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="1000.9" y1="307.7" x2="1000.9" y2="317.3" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="309.2" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="1004.7" y1="321.5" x2="1004.7" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="324.8" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="1008.5" y1="318.5" x2="1008.5" y2="335.9" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="320.3" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="1012.2" y1="313.4" x2="1012.2" y2="327.2" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="314.3" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="1016.0" y1="318.8" x2="1016.0" y2="324.2" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="320.3" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="1019.8" y1="317.0" x2="1019.8" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="320.0" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="1023.6" y1="321.2" x2="1023.6" y2="332.3" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="326.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1027.4" y1="323.3" x2="1027.4" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="328.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1031.2" y1="325.4" x2="1031.2" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="326.3" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="1035.0" y1="332.3" x2="1035.0" y2="344.3" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="334.1" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="1038.7" y1="327.8" x2="1038.7" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="330.2" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="1042.5" y1="322.7" x2="1042.5" y2="336.2" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="327.2" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="1046.3" y1="326.3" x2="1046.3" y2="334.4" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="328.4" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="1050.1" y1="329.0" x2="1050.1" y2="332.0" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="328.7" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="60" y1="302.7" x2="1052" y2="302.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="306.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$80.53 R1</text>
<text x="1058" y="318.2" font-size="9.5" fill="var(--muted)">터치 11회</text>
<line x1="60" y1="87.6" x2="1052" y2="87.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="91.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$87.70 R2</text>
<text x="1058" y="103.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="338.9" x2="1052" y2="338.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="332.9" font-size="11.5" fill="var(--support)" font-weight="600">$79.32 S1</text>
<text x="1058" y="344.9" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="426.6" x2="1052" y2="426.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="420.6" font-size="11.5" fill="var(--support)" font-weight="600">$76.40 S2</text>
<text x="1058" y="432.6" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="539.5" x2="1052" y2="539.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="533.5" font-size="11.5" fill="var(--support)" font-weight="600">$72.63 S3</text>
<text x="1058" y="545.5" font-size="9.5" fill="var(--muted)">터치 8회</text>
<circle cx="1052.0" cy="330.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="322.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $79.61 (2026-08-21)</text>
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

- **상승**: 신용스프레드 축소 — 신용등급이 낮은 기업들의 자금조달 여건이 좋아졌거나, 위험을 더 감수하려는 심리가 커졌다는 신호로 흔히 해석한다.
- **하락**: 신용스프레드 확대 — 신용등급이 낮은 기업들의 자금조달 위험이 부각됐거나, 위험을 피하려는 심리가 커졌다는 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 채권 가격은 앞으로 받을 이자와 원금을 지금 가치로 환산한 값이고, 그 환산에 쓰는 할인율은 "무위험금리 + 신용스프레드(신용등급이 낮은 만큼 추가로 요구하는 보상)"로 나뉜다. 무위험금리가 크게 안 움직인 구간에서 HYG 가격이 변했다면, 신용스프레드 쪽이 움직였다는 신호로 볼 수 있다. 다만 실제로는 무위험금리도 함께 움직이는 경우가 많아서, 이 가격 변화를 순수하게 신용스프레드 변화라고 단정하지는 않는다.
- 정확한 신용스프레드가 아니라 ETF **가격**을 통해 짐작하는 참고 지표다 — 정밀한 스프레드 수치가 필요하면 FRED의 ICE BofA 하이일드 스프레드(`BAMLH0A0HYM2`) 같은 원출처를 확인한다.

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
