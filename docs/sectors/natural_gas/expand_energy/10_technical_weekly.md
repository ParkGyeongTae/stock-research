# 기술적 분석 (주봉 캔들차트 · 5년)

> 최근 5년 주봉으로 본 다년 가격 구조. 최근 1년의 세부 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 마지막 주봉(2026-09-14 주)의 종가 **$87.49**는 [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 기준 종가 **2026-09-18 $87.49**와 일치한다. **같은 회사의 [일봉 차트](./09_technical_daily.md)는 마지막 봉이 2026-09-17($88.33)로 하루 짧다** — 그 사정은 일봉 문서의 같은 블록에 적어 두었다.
- **이 차트의 절반 이상이 다른 회사의 주가다** — 2024-10-02 이전 구간은 Chesapeake Energy(CHK) 시절이며, 아래 3절과 한계에서 그 함의를 다룬다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-20 ~ 2026-09-18)

<style>
.exe-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .exe-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.exe-chart svg { width:100%; height:auto; display:block; }
.exe-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.exe-chart .title { fill: var(--ink); font-weight:600; }
.exe-chart .grid { stroke: var(--grid); stroke-width:1; }
.exe-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="exe-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Expand Energy(EXE) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Expand Energy (EXE) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-20 ~ 2026-09-18 · 마지막 종가 $87.49 (2026-09-18) · 단위 USD</text>
<line x1="60" y1="580.4" x2="1052" y2="580.4" class="grid"/>
<text x="52" y="584.4" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="504.4" x2="1052" y2="504.4" class="grid"/>
<text x="52" y="508.4" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="428.4" x2="1052" y2="428.4" class="grid"/>
<text x="52" y="432.4" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="352.4" x2="1052" y2="352.4" class="grid"/>
<text x="52" y="356.4" font-size="11" text-anchor="end" fill="var(--muted)">90</text>
<line x1="60" y1="276.4" x2="1052" y2="276.4" class="grid"/>
<text x="52" y="280.4" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="200.4" x2="1052" y2="200.4" class="grid"/>
<text x="52" y="204.4" font-size="11" text-anchor="end" fill="var(--muted)">110</text>
<line x1="60" y1="124.4" x2="1052" y2="124.4" class="grid"/>
<text x="52" y="128.4" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="118.7" y1="56.0" x2="118.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="118.7" y1="626.0" x2="118.7" y2="631.0" class="axis"/>
<text x="118.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="315.6" y1="56.0" x2="315.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="315.6" y1="626.0" x2="315.6" y2="631.0" class="axis"/>
<text x="315.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="512.5" y1="56.0" x2="512.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="512.5" y1="626.0" x2="512.5" y2="631.0" class="axis"/>
<text x="512.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="713.1" y1="56.0" x2="713.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="713.1" y1="626.0" x2="713.1" y2="631.0" class="axis"/>
<text x="713.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="910.0" y1="56.0" x2="910.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="910.0" y1="626.0" x2="910.0" y2="631.0" class="axis"/>
<text x="910.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="569.0" x2="61.9" y2="595.4" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="582.9" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="65.7" y1="550.0" x2="65.7" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="564.6" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="69.5" y1="527.2" x2="69.5" y2="558.1" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="536.5" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="73.3" y1="524.1" x2="73.3" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="526.1" width="2.35" height="33.4" fill="var(--down)"/>
<line x1="77.0" y1="550.9" x2="77.0" y2="576.6" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="559.1" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="80.8" y1="509.0" x2="80.8" y2="559.7" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="546.9" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="84.6" y1="509.1" x2="84.6" y2="548.1" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="536.2" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="88.4" y1="520.1" x2="88.4" y2="559.4" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="532.1" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="92.2" y1="546.4" x2="92.2" y2="572.6" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="552.6" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="96.0" y1="544.1" x2="96.0" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="550.6" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="99.8" y1="544.1" x2="99.8" y2="605.1" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="547.3" width="2.35" height="30.6" fill="var(--down)"/>
<line x1="103.5" y1="544.0" x2="103.5" y2="594.2" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="551.5" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="107.3" y1="551.5" x2="107.3" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="558.7" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="111.1" y1="550.5" x2="111.1" y2="589.3" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="556.2" width="2.35" height="26.9" fill="var(--up)"/>
<line x1="114.9" y1="532.8" x2="114.9" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="546.0" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="118.7" y1="506.8" x2="118.7" y2="544.5" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="509.7" width="2.35" height="33.4" fill="var(--up)"/>
<line x1="122.5" y1="476.6" x2="122.5" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="492.8" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="126.3" y1="480.2" x2="126.3" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="481.6" width="2.35" height="75.7" fill="var(--down)"/>
<line x1="130.0" y1="499.1" x2="130.0" y2="569.4" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="516.6" width="2.35" height="52.1" fill="var(--up)"/>
<line x1="133.8" y1="494.7" x2="133.8" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="517.9" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="137.6" y1="507.4" x2="137.6" y2="546.1" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="510.9" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="141.4" y1="504.6" x2="141.4" y2="536.9" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="511.0" width="2.35" height="25.5" fill="var(--down)"/>
<line x1="145.2" y1="459.9" x2="145.2" y2="543.8" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="465.8" width="2.35" height="58.0" fill="var(--up)"/>
<line x1="149.0" y1="388.8" x2="149.0" y2="469.7" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="390.4" width="2.35" height="75.6" fill="var(--up)"/>
<line x1="152.8" y1="361.9" x2="152.8" y2="442.6" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="384.2" width="2.35" height="40.0" fill="var(--down)"/>
<line x1="156.5" y1="431.5" x2="156.5" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="435.8" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="160.3" y1="348.0" x2="160.3" y2="441.3" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="357.6" width="2.35" height="67.8" fill="var(--up)"/>
<line x1="164.1" y1="346.6" x2="164.1" y2="404.2" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="352.4" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="167.9" y1="330.4" x2="167.9" y2="372.5" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="335.9" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="171.7" y1="312.3" x2="171.7" y2="348.0" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="319.3" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="175.5" y1="294.6" x2="175.5" y2="387.8" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="311.6" width="2.35" height="67.2" fill="var(--down)"/>
<line x1="179.3" y1="383.4" x2="179.3" y2="419.1" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="396.9" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="183.1" y1="295.5" x2="183.1" y2="425.1" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="328.5" width="2.35" height="92.3" fill="var(--up)"/>
<line x1="186.8" y1="340.8" x2="186.8" y2="412.7" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="347.8" width="2.35" height="35.8" fill="var(--down)"/>
<line x1="190.6" y1="339.0" x2="190.6" y2="390.9" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="343.8" width="2.35" height="30.2" fill="var(--up)"/>
<line x1="194.4" y1="246.6" x2="194.4" y2="350.2" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="252.5" width="2.35" height="84.5" fill="var(--up)"/>
<line x1="198.2" y1="238.4" x2="198.2" y2="312.2" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="241.7" width="2.35" height="43.9" fill="var(--down)"/>
<line x1="202.0" y1="246.4" x2="202.0" y2="314.2" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="281.3" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="205.8" y1="303.4" x2="205.8" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="314.3" width="2.35" height="111.9" fill="var(--down)"/>
<line x1="209.6" y1="386.6" x2="209.6" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="399.5" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="213.3" y1="347.3" x2="213.3" y2="428.6" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="395.9" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="217.1" y1="424.0" x2="217.1" y2="485.4" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="427.9" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="220.9" y1="395.4" x2="220.9" y2="464.7" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="404.2" width="2.35" height="34.7" fill="var(--up)"/>
<line x1="224.7" y1="333.2" x2="224.7" y2="386.4" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="354.3" width="2.35" height="29.3" fill="var(--up)"/>
<line x1="228.5" y1="316.0" x2="228.5" y2="352.9" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="320.7" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="232.3" y1="311.6" x2="232.3" y2="379.0" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="335.8" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="236.1" y1="288.5" x2="236.1" y2="340.8" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="290.0" width="2.35" height="48.3" fill="var(--up)"/>
<line x1="239.8" y1="259.0" x2="239.8" y2="333.4" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="304.3" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="243.6" y1="234.2" x2="243.6" y2="314.6" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="248.6" width="2.35" height="43.4" fill="var(--up)"/>
<line x1="247.4" y1="234.6" x2="247.4" y2="315.5" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="258.2" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="251.2" y1="243.9" x2="251.2" y2="330.5" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="255.3" width="2.35" height="27.4" fill="var(--up)"/>
<line x1="255.0" y1="231.3" x2="255.0" y2="282.6" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="241.5" width="2.35" height="30.5" fill="var(--down)"/>
<line x1="258.8" y1="235.7" x2="258.8" y2="348.0" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="291.4" width="2.35" height="38.7" fill="var(--down)"/>
<line x1="262.6" y1="308.0" x2="262.6" y2="345.6" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="320.4" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="266.4" y1="247.0" x2="266.4" y2="307.0" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="272.9" width="2.35" height="34.0" fill="var(--up)"/>
<line x1="270.1" y1="235.0" x2="270.1" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="255.9" width="2.35" height="56.1" fill="var(--down)"/>
<line x1="273.9" y1="263.9" x2="273.9" y2="314.7" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="299.0" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="277.7" y1="265.4" x2="277.7" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="292.7" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="281.5" y1="220.8" x2="281.5" y2="292.4" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="269.8" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="285.3" y1="228.9" x2="285.3" y2="286.9" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="254.7" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="289.1" y1="255.8" x2="289.1" y2="302.2" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="274.3" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="292.9" y1="238.9" x2="292.9" y2="321.7" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="254.1" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="296.6" y1="237.3" x2="296.6" y2="291.5" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="263.1" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="300.4" y1="243.6" x2="300.4" y2="330.3" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="260.1" width="2.35" height="56.5" fill="var(--down)"/>
<line x1="304.2" y1="258.5" x2="304.2" y2="308.9" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="294.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="308.0" y1="287.3" x2="308.0" y2="330.5" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="296.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="311.8" y1="280.3" x2="311.8" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="290.7" width="2.35" height="28.5" fill="var(--down)"/>
<line x1="315.6" y1="325.6" x2="315.6" y2="393.7" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="329.1" width="2.35" height="40.1" fill="var(--down)"/>
<line x1="319.4" y1="335.1" x2="319.4" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="343.2" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="323.1" y1="328.7" x2="323.1" y2="376.2" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="332.3" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="326.9" y1="329.8" x2="326.9" y2="385.5" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="338.6" width="2.35" height="31.8" fill="var(--down)"/>
<line x1="330.7" y1="372.4" x2="330.7" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="374.4" width="2.35" height="19.0" fill="var(--down)"/>
<line x1="334.5" y1="384.5" x2="334.5" y2="419.4" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="393.4" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="338.3" y1="387.4" x2="338.3" y2="431.4" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="408.2" width="2.35" height="19.5" fill="var(--down)"/>
<line x1="342.1" y1="385.8" x2="342.1" y2="449.9" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="387.4" width="2.35" height="45.4" fill="var(--up)"/>
<line x1="345.9" y1="378.3" x2="345.9" y2="435.9" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="382.7" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="349.6" y1="416.8" x2="349.6" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="420.6" width="2.35" height="44.4" fill="var(--down)"/>
<line x1="353.4" y1="454.8" x2="353.4" y2="506.8" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="480.0" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="357.2" y1="460.5" x2="357.2" y2="489.7" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="471.7" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="361.0" y1="450.9" x2="361.0" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="458.5" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="364.8" y1="436.0" x2="364.8" y2="466.7" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="444.0" width="2.35" height="20.3" fill="var(--down)"/>
<line x1="368.6" y1="418.7" x2="368.6" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="421.0" width="2.35" height="36.9" fill="var(--up)"/>
<line x1="372.4" y1="411.7" x2="372.4" y2="430.8" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="413.2" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="376.2" y1="403.5" x2="376.2" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="408.0" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="379.9" y1="405.9" x2="379.9" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="415.4" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="383.7" y1="422.7" x2="383.7" y2="452.7" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="426.6" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="387.5" y1="405.2" x2="387.5" y2="447.2" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="419.1" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="391.3" y1="406.3" x2="391.3" y2="452.9" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="427.9" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="395.1" y1="426.8" x2="395.1" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="431.2" width="2.35" height="24.6" fill="var(--up)"/>
<line x1="398.9" y1="412.8" x2="398.9" y2="453.7" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="420.8" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="402.7" y1="402.8" x2="402.7" y2="441.6" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="410.5" width="2.35" height="25.5" fill="var(--up)"/>
<line x1="406.4" y1="407.1" x2="406.4" y2="428.5" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="412.7" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="410.2" y1="392.9" x2="410.2" y2="426.9" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="400.4" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="414.0" y1="392.3" x2="414.0" y2="425.7" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="400.3" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="417.8" y1="390.6" x2="417.8" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="407.4" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="421.6" y1="398.1" x2="421.6" y2="430.4" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="404.9" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="425.4" y1="390.7" x2="425.4" y2="414.6" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="394.4" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="429.2" y1="377.2" x2="429.2" y2="420.0" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="387.6" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="432.9" y1="359.5" x2="432.9" y2="393.7" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="382.3" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="436.7" y1="366.4" x2="436.7" y2="418.0" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="383.3" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="440.5" y1="370.9" x2="440.5" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="383.3" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="444.3" y1="348.9" x2="444.3" y2="391.2" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="350.4" width="2.35" height="32.4" fill="var(--up)"/>
<line x1="448.1" y1="347.8" x2="448.1" y2="372.8" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="353.3" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="451.9" y1="357.6" x2="451.9" y2="391.6" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="358.2" width="2.35" height="28.8" fill="var(--down)"/>
<line x1="455.7" y1="377.7" x2="455.7" y2="414.4" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="385.1" width="2.35" height="27.6" fill="var(--down)"/>
<line x1="459.5" y1="373.8" x2="459.5" y2="414.3" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="381.1" width="2.35" height="32.8" fill="var(--up)"/>
<line x1="463.2" y1="367.1" x2="463.2" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="373.1" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="467.0" y1="353.0" x2="467.0" y2="376.6" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="360.6" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="470.8" y1="344.8" x2="470.8" y2="374.7" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="359.1" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="474.6" y1="369.5" x2="474.6" y2="396.1" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="373.8" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="478.4" y1="352.8" x2="478.4" y2="395.8" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="357.3" width="2.35" height="30.9" fill="var(--up)"/>
<line x1="482.2" y1="359.3" x2="482.2" y2="441.5" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="362.6" width="2.35" height="72.7" fill="var(--down)"/>
<line x1="486.0" y1="400.2" x2="486.0" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="416.4" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="489.7" y1="406.4" x2="489.7" y2="428.9" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="412.1" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="493.5" y1="414.4" x2="493.5" y2="433.3" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="417.4" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="497.3" y1="427.5" x2="497.3" y2="475.0" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="431.1" width="2.35" height="34.9" fill="var(--down)"/>
<line x1="501.1" y1="453.6" x2="501.1" y2="482.8" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="460.5" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="504.9" y1="445.1" x2="504.9" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="449.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="508.7" y1="437.0" x2="508.7" y2="452.4" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="450.0" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="512.5" y1="428.0" x2="512.5" y2="460.9" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="434.5" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="516.2" y1="405.6" x2="516.2" y2="453.3" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="406.6" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="520.0" y1="410.3" x2="520.0" y2="467.6" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="413.2" width="2.35" height="46.1" fill="var(--down)"/>
<line x1="523.8" y1="443.9" x2="523.8" y2="472.6" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="447.3" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="527.6" y1="433.7" x2="527.6" y2="457.4" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="444.4" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="531.4" y1="448.8" x2="531.4" y2="468.2" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="452.5" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="535.2" y1="435.1" x2="535.2" y2="468.7" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="438.1" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="539.0" y1="395.5" x2="539.0" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="413.7" width="2.35" height="27.0" fill="var(--up)"/>
<line x1="542.7" y1="400.5" x2="542.7" y2="419.1" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="407.0" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="546.5" y1="396.0" x2="546.5" y2="419.1" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="398.7" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="550.3" y1="386.9" x2="550.3" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="402.0" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="554.1" y1="375.9" x2="554.1" y2="407.0" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="380.4" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="557.9" y1="359.1" x2="557.9" y2="388.7" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="361.3" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="561.7" y1="344.6" x2="561.7" y2="367.7" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="356.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="565.5" y1="346.8" x2="565.5" y2="373.7" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="355.4" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="569.3" y1="358.2" x2="569.3" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="361.9" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="573.0" y1="335.3" x2="573.0" y2="378.1" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="336.7" width="2.35" height="37.5" fill="var(--up)"/>
<line x1="576.8" y1="325.2" x2="576.8" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="337.8" width="2.35" height="39.9" fill="var(--down)"/>
<line x1="580.6" y1="352.3" x2="580.6" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="372.0" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="584.4" y1="335.1" x2="584.4" y2="374.8" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="339.6" width="2.35" height="32.1" fill="var(--up)"/>
<line x1="588.2" y1="329.8" x2="588.2" y2="363.3" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="341.1" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="592.0" y1="339.9" x2="592.0" y2="361.3" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="345.3" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="595.8" y1="336.6" x2="595.8" y2="371.5" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="341.2" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="599.5" y1="354.7" x2="599.5" y2="390.5" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="365.4" width="2.35" height="23.9" fill="var(--down)"/>
<line x1="603.3" y1="381.7" x2="603.3" y2="411.1" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="387.1" width="2.35" height="22.9" fill="var(--down)"/>
<line x1="607.1" y1="387.9" x2="607.1" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="405.2" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="610.9" y1="397.3" x2="610.9" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="410.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="614.7" y1="395.1" x2="614.7" y2="415.1" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="402.0" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="618.5" y1="396.1" x2="618.5" y2="429.6" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="401.2" width="2.35" height="19.5" fill="var(--down)"/>
<line x1="622.3" y1="416.0" x2="622.3" y2="455.1" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="420.6" width="2.35" height="24.5" fill="var(--down)"/>
<line x1="626.0" y1="444.9" x2="626.0" y2="493.2" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="444.9" width="2.35" height="41.0" fill="var(--down)"/>
<line x1="629.8" y1="477.9" x2="629.8" y2="508.8" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="485.2" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="633.6" y1="474.3" x2="633.6" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="482.1" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="637.4" y1="469.8" x2="637.4" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="478.3" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="641.2" y1="466.3" x2="641.2" y2="497.1" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="470.3" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="645.0" y1="479.1" x2="645.0" y2="504.1" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="479.8" width="2.35" height="18.2" fill="var(--down)"/>
<line x1="648.8" y1="477.9" x2="648.8" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="479.9" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="652.5" y1="436.0" x2="652.5" y2="483.9" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="440.1" width="2.35" height="36.9" fill="var(--up)"/>
<line x1="656.3" y1="399.1" x2="656.3" y2="448.1" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="408.6" width="2.35" height="31.0" fill="var(--up)"/>
<line x1="660.1" y1="382.8" x2="660.1" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="385.6" width="2.35" height="25.5" fill="var(--up)"/>
<line x1="663.9" y1="366.3" x2="663.9" y2="403.6" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="372.2" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="667.7" y1="368.0" x2="667.7" y2="394.2" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="376.0" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="671.5" y1="371.4" x2="671.5" y2="407.9" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="379.1" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="675.3" y1="349.3" x2="675.3" y2="408.0" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="400.6" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="679.1" y1="326.1" x2="679.1" y2="402.4" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="333.5" width="2.35" height="68.9" fill="var(--up)"/>
<line x1="682.8" y1="302.1" x2="682.8" y2="324.8" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="314.5" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="686.6" y1="266.7" x2="686.6" y2="314.3" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="280.7" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="690.4" y1="272.6" x2="690.4" y2="293.3" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="275.0" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="694.2" y1="282.3" x2="694.2" y2="309.1" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="284.0" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="698.0" y1="272.5" x2="698.0" y2="301.2" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="283.1" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="701.8" y1="288.2" x2="701.8" y2="322.0" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="289.2" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="705.6" y1="293.2" x2="705.6" y2="321.3" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="302.2" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="709.3" y1="261.7" x2="709.3" y2="295.5" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="276.3" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="713.1" y1="238.4" x2="713.1" y2="270.5" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="260.1" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="716.9" y1="204.4" x2="716.9" y2="268.6" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="228.1" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="720.7" y1="213.2" x2="720.7" y2="237.3" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="230.8" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="724.5" y1="244.5" x2="724.5" y2="283.5" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="247.1" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="728.3" y1="231.9" x2="728.3" y2="266.0" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="253.6" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="732.1" y1="225.8" x2="732.1" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="235.9" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="735.8" y1="207.5" x2="735.8" y2="250.6" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="235.9" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="739.6" y1="242.8" x2="739.6" y2="299.8" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="243.7" width="2.35" height="41.2" fill="var(--down)"/>
<line x1="743.4" y1="261.0" x2="743.4" y2="328.9" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="277.2" width="2.35" height="29.3" fill="var(--down)"/>
<line x1="747.2" y1="252.0" x2="747.2" y2="303.8" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="256.6" width="2.35" height="38.3" fill="var(--up)"/>
<line x1="751.0" y1="203.2" x2="751.0" y2="261.6" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="220.5" width="2.35" height="36.9" fill="var(--up)"/>
<line x1="754.8" y1="191.5" x2="754.8" y2="220.5" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="193.3" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="758.6" y1="169.8" x2="758.6" y2="289.6" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="193.3" width="2.35" height="83.1" fill="var(--down)"/>
<line x1="762.4" y1="234.0" x2="762.4" y2="311.7" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="250.4" width="2.35" height="40.6" fill="var(--up)"/>
<line x1="766.1" y1="220.9" x2="766.1" y2="257.2" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="227.2" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="769.9" y1="227.8" x2="769.9" y2="267.1" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="227.8" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="773.7" y1="215.6" x2="773.7" y2="267.1" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="231.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="777.5" y1="177.2" x2="777.5" y2="236.1" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="182.3" width="2.35" height="53.1" fill="var(--up)"/>
<line x1="781.3" y1="163.2" x2="781.3" y2="207.2" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="169.8" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="785.1" y1="151.3" x2="785.1" y2="182.5" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="155.1" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="788.9" y1="142.2" x2="788.9" y2="164.3" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="146.6" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="792.6" y1="124.1" x2="792.6" y2="163.9" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="136.9" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="796.4" y1="148.6" x2="796.4" y2="190.5" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="151.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="800.2" y1="99.0" x2="800.2" y2="149.5" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="108.8" width="2.35" height="37.8" fill="var(--up)"/>
<line x1="804.0" y1="99.4" x2="804.0" y2="142.2" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="109.9" width="2.35" height="22.4" fill="var(--down)"/>
<line x1="807.8" y1="134.7" x2="807.8" y2="216.1" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="142.3" width="2.35" height="67.7" fill="var(--down)"/>
<line x1="811.6" y1="199.9" x2="811.6" y2="252.4" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="213.7" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="815.4" y1="197.5" x2="815.4" y2="234.1" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="210.7" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="819.1" y1="219.2" x2="819.1" y2="309.7" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="219.2" width="2.35" height="71.1" fill="var(--down)"/>
<line x1="822.9" y1="231.6" x2="822.9" y2="300.6" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="261.4" width="2.35" height="27.8" fill="var(--up)"/>
<line x1="826.7" y1="255.7" x2="826.7" y2="291.4" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="258.3" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="830.5" y1="276.4" x2="830.5" y2="333.1" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="283.6" width="2.35" height="29.8" fill="var(--down)"/>
<line x1="834.3" y1="308.8" x2="834.3" y2="344.7" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="317.0" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="838.1" y1="295.2" x2="838.1" y2="325.6" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="300.9" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="841.9" y1="285.5" x2="841.9" y2="318.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="307.1" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="845.6" y1="294.9" x2="845.6" y2="321.8" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="301.1" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="849.4" y1="268.8" x2="849.4" y2="316.8" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="287.8" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="853.2" y1="229.1" x2="853.2" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="232.5" width="2.35" height="59.7" fill="var(--up)"/>
<line x1="857.0" y1="197.7" x2="857.0" y2="237.9" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="219.9" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="860.8" y1="200.4" x2="860.8" y2="263.5" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="209.7" width="2.35" height="53.4" fill="var(--down)"/>
<line x1="864.6" y1="245.5" x2="864.6" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="256.9" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="868.4" y1="211.6" x2="868.4" y2="257.9" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="247.7" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="872.2" y1="239.2" x2="872.2" y2="286.6" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="240.5" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="875.9" y1="178.2" x2="875.9" y2="253.4" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="181.8" width="2.35" height="66.3" fill="var(--up)"/>
<line x1="879.7" y1="122.1" x2="879.7" y2="186.2" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="145.1" width="2.35" height="30.6" fill="var(--up)"/>
<line x1="883.5" y1="115.4" x2="883.5" y2="181.8" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="146.1" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="887.3" y1="103.9" x2="887.3" y2="186.3" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="109.7" width="2.35" height="52.7" fill="var(--up)"/>
<line x1="891.1" y1="74.1" x2="891.1" y2="142.3" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="102.7" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="894.9" y1="106.2" x2="894.9" y2="189.8" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="108.9" width="2.35" height="70.3" fill="var(--down)"/>
<line x1="898.7" y1="179.3" x2="898.7" y2="230.8" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="179.3" width="2.35" height="30.6" fill="var(--down)"/>
<line x1="902.4" y1="188.9" x2="902.4" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="204.3" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="906.2" y1="174.4" x2="906.2" y2="213.9" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="199.5" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="910.0" y1="213.4" x2="910.0" y2="268.5" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="213.5" width="2.35" height="50.5" fill="var(--down)"/>
<line x1="913.8" y1="237.2" x2="913.8" y2="287.0" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="258.2" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="917.6" y1="187.3" x2="917.6" y2="252.5" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="204.3" width="2.35" height="27.7" fill="var(--up)"/>
<line x1="921.4" y1="168.3" x2="921.4" y2="221.6" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="182.1" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="925.2" y1="183.1" x2="925.2" y2="233.0" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="197.6" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="928.9" y1="227.0" x2="928.9" y2="272.1" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="242.1" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="932.7" y1="206.6" x2="932.7" y2="288.9" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="215.1" width="2.35" height="34.5" fill="var(--up)"/>
<line x1="936.5" y1="202.1" x2="936.5" y2="269.9" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="215.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="940.3" y1="190.0" x2="940.3" y2="239.0" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="194.4" width="2.35" height="30.0" fill="var(--down)"/>
<line x1="944.1" y1="201.8" x2="944.1" y2="246.7" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="216.4" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="947.9" y1="186.9" x2="947.9" y2="248.8" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="220.8" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="951.7" y1="163.8" x2="951.7" y2="243.9" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="173.8" width="2.35" height="68.8" fill="var(--up)"/>
<line x1="955.5" y1="166.3" x2="955.5" y2="249.4" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="168.6" width="2.35" height="78.2" fill="var(--down)"/>
<line x1="959.2" y1="240.6" x2="959.2" y2="297.0" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="255.7" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="963.0" y1="275.8" x2="963.0" y2="314.9" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="279.9" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="966.8" y1="291.7" x2="966.8" y2="323.9" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="303.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="970.6" y1="253.9" x2="970.6" y2="306.3" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="275.5" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="974.4" y1="262.5" x2="974.4" y2="314.1" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="275.0" width="2.35" height="32.2" fill="var(--down)"/>
<line x1="978.2" y1="293.0" x2="978.2" y2="318.4" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="298.3" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="982.0" y1="269.2" x2="982.0" y2="304.5" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="292.1" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="985.7" y1="297.8" x2="985.7" y2="336.8" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="301.5" width="2.35" height="28.3" fill="var(--down)"/>
<line x1="989.5" y1="319.5" x2="989.5" y2="346.4" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="329.7" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="993.3" y1="335.1" x2="993.3" y2="376.7" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="336.7" width="2.35" height="25.0" fill="var(--down)"/>
<line x1="997.1" y1="354.6" x2="997.1" y2="380.0" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="373.8" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="1000.9" y1="345.0" x2="1000.9" y2="375.9" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="364.0" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="1004.7" y1="329.5" x2="1004.7" y2="373.0" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="346.9" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="1008.5" y1="347.8" x2="1008.5" y2="390.5" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="353.7" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="1012.2" y1="352.4" x2="1012.2" y2="384.1" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="366.6" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="1016.0" y1="319.7" x2="1016.0" y2="379.7" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="340.8" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="1019.8" y1="320.7" x2="1019.8" y2="366.9" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="321.8" width="2.35" height="16.3" fill="var(--up)"/>
<line x1="1023.6" y1="310.5" x2="1023.6" y2="348.4" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="321.2" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="1027.4" y1="284.9" x2="1027.4" y2="327.1" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="316.1" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="1031.2" y1="296.3" x2="1031.2" y2="332.4" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="306.1" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="1035.0" y1="280.7" x2="1035.0" y2="318.6" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="290.4" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="1038.7" y1="275.3" x2="1038.7" y2="297.0" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="285.7" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="1042.5" y1="279.4" x2="1042.5" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="287.8" width="2.35" height="27.9" fill="var(--down)"/>
<line x1="1046.3" y1="302.8" x2="1046.3" y2="368.7" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="304.3" width="2.35" height="60.8" fill="var(--down)"/>
<line x1="1050.1" y1="362.4" x2="1050.1" y2="372.4" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="365.2" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="60" y1="346.3" x2="1052" y2="346.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="349.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$91 R1</text>
<text x="1058" y="361.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="230.2" x2="1052" y2="230.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="233.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$106 R2</text>
<text x="1058" y="245.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="201.0" x2="1052" y2="201.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="204.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$110 R3</text>
<text x="1058" y="216.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="390.2" x2="1052" y2="390.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="384.2" font-size="11.5" fill="var(--support)" font-weight="600">$85 S1</text>
<text x="1058" y="396.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="426.0" x2="1052" y2="426.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="420.0" font-size="11.5" fill="var(--support)" font-weight="600">$80 S2</text>
<text x="1058" y="432.0" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="478.4" x2="1052" y2="478.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="472.4" font-size="11.5" fill="var(--support)" font-weight="600">$73 S3</text>
<text x="1058" y="484.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="371.5" r="3" fill="var(--ink)"/>
<text x="1046.0" y="363.5" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $87 (2026-09-18)</text>
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
| ------ | ------ | ----------- | ------ |
| R3 | $110 | 2 | 2025-01-13·2025-09-29 고점대 — 5년 최고($126.62)에 인접한 구간 |
| R2 | $106 | 3 | 2022-05-30, 2022-09-12·10-31 고점대 — **Chesapeake 시절 가격대**라 현재 자본구조와 비교 불가(§3 참고) |
| R1 | $91 | 2 | 2023-09-04·2023-10-16 고점대 — 역시 합병 이전 구간 |
| **현재가** | **$87.49** (2026-09-18 종가) | — | R1($91)과 S1($85) 사이. 5년 최고 대비 −30.9%, 5년 최저 대비 +54.2% |
| S1 | $85 | 2 | 2024-04-29, 2026-07-06 저점대 — 터치 2회. **합병 전후에 하나씩 걸쳐 있어 표본 성격이 섞여 있다** |
| S2 | $80 | 3 | 2022-05-02, 2023-07-17·10-02 저점대 — 전부 Chesapeake 시절 |
| S3 | $73 | 4 | 2022-07-04, 2023-05-29·12-11, 2024-01-22 저점대 — 4회 터치로 가장 두껍지만 **모두 합병 이전 구간**이다 |
| 참고선 | $126.62 / $56.75 | — | 최근 5년 최고·최저. 최저가는 2022년 Chesapeake 시절이라 주식수가 지금의 56% 수준이던 때다 — 근시일 지지로 보지 않는다 |

> **검출된 6개 레벨 중 5개(R1·R2·S1~S3)가 2024-10 합병 이전 구간에서 나왔다.** 주식수가 78% 늘기 전의 가격대이므로 **같은 주가가 같은 기업가치를 뜻하지 않는다** — 3절과 한계 참고. 합병 이후 구간에서 유효한 레벨은 사실상 R3($110)와 S1의 2026-07-06 터치뿐이다.

---

## 3. 관측된 특이 구간 — 2024년 10월 합병에 따른 계보 단절

- 2024-10-01 Southwestern Energy 합병(전액 주식교환)으로 **발행주식수가 130.8 → 232.7백만 주로 78% 늘었고**, 사명이 Chesapeake Energy → Expand Energy로, 티커가 CHK → EXE로 바뀌었다(2024-10-02 거래 개시). 생산량과 증명매장량도 함께 두 배가 됐다([역사 / 주요 이벤트](./02_history.md)).
- **이 차트는 원주가라 그 사건을 소급 조정하지 않는다** — 주식분할이 아니므로 조정 대상이 아니기 때문이다. 그 결과 **차트 왼쪽 절반(2021-09~2024-09)은 시가총액이 지금의 절반 이하이던 회사의 주가**다.
- 실무적으로는 하단 레벨을 읽을 때 이 점이 결정적이다. S2($80)·S3($73)는 시가총액 기준으로 보면 현재의 40~45% 수준에서 형성된 가격대이고, **"과거에 이 가격에서 지지됐으니 지금도 지지될 것"이라는 추론이 성립하지 않는다.**

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-20~2026-09-18. 수집 시점: 2026-09-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py EXE --name "Expand Energy" --interval 1wk --close-on 2026-09-17 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3절의 합병 단절이 이 차트의 가장 큰 제약이다.** 6개 레벨 중 5개가 합병 이전 구간에서 나왔고, 그 시기 발행주식수는 현재의 56%였다. **주식분할이 아니라 주식교환 합병이므로 소급 조정은 하지 않았고**, 따라서 이 레벨들은 "과거에 실제로 거래된 가격대"라는 의미 이상으로 읽지 않는다. 같은 이유로 [EQT 주봉 차트](../eqt/10_technical_weekly.md)와 하단 레벨을 나란히 비교하는 것도 적절하지 않다.
    - 기간 내 배당이 20회 있었으나 **원주가(배당 미반영)**다. 배당수익률이 연 2.5~4.4%로 높았던 구간이 있어 **총수익 관점의 비교에는 이 차트를 쓰지 말 것.**
    - `--close-on 2026-09-17`로 실행했으나 주봉은 주 단위로 묶이므로 마지막 봉은 **2026-09-18까지 포함한 완성된 주**다(토요일 실행이라 그 주가 이미 끝났다).

---

*작성일: 2026-09-19*
