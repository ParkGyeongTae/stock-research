# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 주봉 API에서 직접 수집한 것이다. 2026-08-20은 주봉 마감일(금요일)이 아니라 직접 대조는 어려우나, 가장 가까운 주봉 종가(2026-08-21 기준 최근 주) $53.87은 [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)의 2026-08-20 종가 $53.89와 오차 범위 내에서 일치.
>
> ⚠️ **5년 조사 기간(2021-08~2026-08) 중 사업 구조 자체가 바뀌었다** — 2024.07 Equitrans Midstream 재인수로 EQT는 순수 E&P에서 수직계열화 기업으로 전환됐고, 이 대가로 발행주식수가 42% 급증했다(역사 / 주요 이벤트·핵심 지표 참고). 2024.07 이전(순수 E&P 시기)의 스윙 레벨은 지금과 다른 사업·자본구조에서 형성된 것이므로, 아래 2. 지지선 / 저항선 요약의 하위 레벨(S2·S3)은 참고선에 가깝게 해석할 것.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-21)

<div class="eqt-chart">
<style>
.eqt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.eqt-chart svg { width:100%; height:auto; display:block; }
.eqt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.eqt-chart .title { fill: var(--ink); font-weight:600; }
.eqt-chart .grid { stroke: var(--grid); stroke-width:1; }
.eqt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="EQT Corporation(EQT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">EQT Corporation (EQT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 $53.87 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="564.9" x2="1052" y2="564.9" class="grid"/>
<text x="52" y="568.9" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="463.1" x2="1052" y2="463.1" class="grid"/>
<text x="52" y="467.1" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="361.4" x2="1052" y2="361.4" class="grid"/>
<text x="52" y="365.4" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="259.6" x2="1052" y2="259.6" class="grid"/>
<text x="52" y="263.6" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="157.8" x2="1052" y2="157.8" class="grid"/>
<text x="52" y="161.8" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
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
<line x1="61.9" y1="575.8" x2="61.9" y2="602.7" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="579.0" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="65.7" y1="557.3" x2="65.7" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="559.5" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="69.5" y1="551.6" x2="69.5" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="558.6" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="73.3" y1="556.4" x2="73.3" y2="577.4" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="566.5" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="77.0" y1="560.6" x2="77.0" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="565.0" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="80.8" y1="535.4" x2="80.8" y2="562.8" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="556.3" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="84.6" y1="540.2" x2="84.6" y2="561.0" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="555.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="88.4" y1="552.1" x2="88.4" y2="571.4" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="553.4" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="92.2" y1="550.1" x2="92.2" y2="569.3" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="550.7" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="96.0" y1="535.5" x2="96.0" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="545.7" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="99.8" y1="553.3" x2="99.8" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="559.0" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="103.5" y1="547.6" x2="103.5" y2="573.4" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="551.1" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="107.3" y1="541.3" x2="107.3" y2="561.0" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="549.4" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="111.1" y1="547.9" x2="111.1" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="554.9" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="114.9" y1="552.3" x2="114.9" y2="585.8" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="555.0" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="118.7" y1="552.8" x2="118.7" y2="579.3" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="556.2" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="122.5" y1="542.7" x2="122.5" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="552.1" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="126.3" y1="539.9" x2="126.3" y2="559.8" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="543.2" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="130.0" y1="530.6" x2="130.0" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="539.2" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="133.8" y1="531.3" x2="133.8" y2="550.0" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="536.3" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="137.6" y1="515.7" x2="137.6" y2="540.3" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="526.4" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="141.4" y1="525.0" x2="141.4" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="525.2" width="2.35" height="34.0" fill="var(--down)"/>
<line x1="145.2" y1="550.2" x2="145.2" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="553.3" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="149.0" y1="540.7" x2="149.0" y2="561.2" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="549.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="152.8" y1="534.2" x2="152.8" y2="558.5" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="535.1" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="156.5" y1="524.1" x2="156.5" y2="542.0" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="534.2" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="160.3" y1="534.4" x2="160.3" y2="551.5" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="535.4" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="164.1" y1="494.8" x2="164.1" y2="540.6" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="500.2" width="2.35" height="40.2" fill="var(--up)"/>
<line x1="167.9" y1="488.0" x2="167.9" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="493.7" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="171.7" y1="491.2" x2="171.7" y2="521.2" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="492.5" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="175.5" y1="417.6" x2="175.5" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="419.1" width="2.35" height="68.8" fill="var(--up)"/>
<line x1="179.3" y1="401.3" x2="179.3" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="401.8" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="183.1" y1="374.3" x2="183.1" y2="407.7" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="378.6" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="186.8" y1="335.1" x2="186.8" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="337.3" width="2.35" height="41.9" fill="var(--up)"/>
<line x1="190.6" y1="305.4" x2="190.6" y2="365.5" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="326.1" width="2.35" height="37.9" fill="var(--down)"/>
<line x1="194.4" y1="342.1" x2="194.4" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="363.9" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="198.2" y1="327.2" x2="198.2" y2="379.7" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="350.7" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="202.0" y1="361.5" x2="202.0" y2="416.1" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="361.9" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="205.8" y1="328.3" x2="205.8" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="352.7" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="209.6" y1="268.1" x2="209.6" y2="351.2" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="275.6" width="2.35" height="73.5" fill="var(--up)"/>
<line x1="213.3" y1="255.4" x2="213.3" y2="293.3" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="267.6" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="217.1" y1="256.5" x2="217.1" y2="292.1" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="269.4" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="220.9" y1="292.8" x2="220.9" y2="411.0" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="295.3" width="2.35" height="107.4" fill="var(--down)"/>
<line x1="224.7" y1="388.5" x2="224.7" y2="436.7" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="395.1" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="228.5" y1="369.2" x2="228.5" y2="426.0" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="405.9" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="232.3" y1="411.6" x2="232.3" y2="452.7" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="420.4" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="236.1" y1="385.5" x2="236.1" y2="431.2" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="395.8" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="239.8" y1="321.3" x2="239.8" y2="388.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="338.7" width="2.35" height="50.2" fill="var(--up)"/>
<line x1="243.6" y1="293.1" x2="243.6" y2="340.4" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="320.3" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="247.4" y1="327.0" x2="247.4" y2="359.4" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="330.4" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="251.2" y1="297.2" x2="251.2" y2="348.3" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="298.4" width="2.35" height="43.9" fill="var(--up)"/>
<line x1="255.0" y1="269.2" x2="255.0" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="283.0" width="2.35" height="37.7" fill="var(--up)"/>
<line x1="258.8" y1="242.0" x2="258.8" y2="288.7" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="262.9" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="262.6" y1="245.3" x2="262.6" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="270.3" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="266.4" y1="269.2" x2="266.4" y2="317.2" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="276.4" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="270.1" y1="239.5" x2="270.1" y2="314.1" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="272.7" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="273.9" y1="279.2" x2="273.9" y2="364.2" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="310.8" width="2.35" height="37.8" fill="var(--down)"/>
<line x1="277.7" y1="347.3" x2="277.7" y2="380.2" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="353.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="281.5" y1="301.2" x2="281.5" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="329.1" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="285.3" y1="312.1" x2="285.3" y2="350.6" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="322.2" width="2.35" height="27.7" fill="var(--down)"/>
<line x1="289.1" y1="323.4" x2="289.1" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="350.3" width="2.35" height="32.7" fill="var(--down)"/>
<line x1="292.9" y1="350.2" x2="292.9" y2="394.1" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="374.8" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="296.6" y1="335.7" x2="296.6" y2="368.5" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="350.4" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="300.4" y1="313.0" x2="300.4" y2="353.3" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="334.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="304.2" y1="315.2" x2="304.2" y2="362.6" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="326.6" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="308.0" y1="310.7" x2="308.0" y2="368.2" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="330.5" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="311.8" y1="326.9" x2="311.8" y2="366.2" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="346.6" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="315.6" y1="363.1" x2="315.6" y2="408.7" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="367.3" width="2.35" height="38.2" fill="var(--down)"/>
<line x1="319.4" y1="369.8" x2="319.4" y2="399.2" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="389.4" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="323.1" y1="390.8" x2="323.1" y2="417.8" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="396.2" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="326.9" y1="391.7" x2="326.9" y2="432.3" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="397.0" width="2.35" height="27.2" fill="var(--down)"/>
<line x1="330.7" y1="421.8" x2="330.7" y2="447.9" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="429.1" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="334.5" y1="408.9" x2="334.5" y2="431.3" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="414.2" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="338.3" y1="402.3" x2="338.3" y2="429.8" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="408.6" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="342.1" y1="407.7" x2="342.1" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="417.5" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="345.9" y1="434.1" x2="345.9" y2="454.2" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="440.7" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="349.6" y1="445.2" x2="349.6" y2="473.2" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="446.1" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="353.4" y1="430.9" x2="353.4" y2="463.6" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="449.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="357.2" y1="414.6" x2="357.2" y2="463.0" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="415.0" width="2.35" height="35.0" fill="var(--up)"/>
<line x1="361.0" y1="414.3" x2="361.0" y2="438.1" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="414.8" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="364.8" y1="427.2" x2="364.8" y2="461.6" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="430.4" width="2.35" height="28.6" fill="var(--down)"/>
<line x1="368.6" y1="449.0" x2="368.6" y2="482.4" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="466.0" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="372.4" y1="451.2" x2="372.4" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="457.4" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="376.2" y1="438.4" x2="376.2" y2="467.1" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="443.7" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="379.9" y1="433.6" x2="379.9" y2="449.8" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="434.2" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="383.7" y1="423.5" x2="383.7" y2="440.1" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="431.2" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="387.5" y1="420.2" x2="387.5" y2="441.2" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="423.5" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="391.3" y1="410.2" x2="391.3" y2="452.7" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="413.9" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="395.1" y1="413.7" x2="395.1" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="418.4" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="398.9" y1="426.6" x2="398.9" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="428.0" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="402.7" y1="386.8" x2="402.7" y2="425.5" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="399.7" width="2.35" height="23.8" fill="var(--up)"/>
<line x1="406.4" y1="394.0" x2="406.4" y2="408.5" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="401.2" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="410.2" y1="392.4" x2="410.2" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="396.5" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="414.0" y1="369.4" x2="414.0" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="376.1" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="417.8" y1="360.2" x2="417.8" y2="384.0" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="365.0" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="421.6" y1="361.4" x2="421.6" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="364.4" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="425.4" y1="347.0" x2="425.4" y2="368.1" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="349.9" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="429.2" y1="347.8" x2="429.2" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="352.2" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="432.9" y1="351.2" x2="432.9" y2="380.7" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="366.1" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="436.7" y1="350.1" x2="436.7" y2="382.3" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="362.4" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="440.5" y1="334.4" x2="440.5" y2="374.8" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="338.2" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="444.3" y1="335.2" x2="444.3" y2="362.1" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="342.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="448.1" y1="317.0" x2="448.1" y2="351.2" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="330.3" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="451.9" y1="324.8" x2="451.9" y2="343.0" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="326.0" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="455.7" y1="311.7" x2="455.7" y2="347.3" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="320.6" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="459.5" y1="318.2" x2="459.5" y2="343.3" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="318.4" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="463.2" y1="320.5" x2="463.2" y2="345.3" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="321.3" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="467.0" y1="320.7" x2="467.0" y2="347.5" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="333.6" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="470.8" y1="342.0" x2="470.8" y2="378.5" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="346.7" width="2.35" height="30.4" fill="var(--down)"/>
<line x1="474.6" y1="353.6" x2="474.6" y2="380.0" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="355.5" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="478.4" y1="329.0" x2="478.4" y2="375.1" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="333.0" width="2.35" height="25.1" fill="var(--up)"/>
<line x1="482.2" y1="315.0" x2="482.2" y2="334.6" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="327.1" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="486.0" y1="313.9" x2="486.0" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="325.7" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="489.7" y1="328.7" x2="489.7" y2="365.6" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="341.5" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="493.5" y1="308.1" x2="493.5" y2="357.4" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="313.3" width="2.35" height="33.0" fill="var(--up)"/>
<line x1="497.3" y1="315.9" x2="497.3" y2="375.4" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="318.7" width="2.35" height="51.5" fill="var(--down)"/>
<line x1="501.1" y1="343.8" x2="501.1" y2="369.4" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="357.6" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="504.9" y1="350.2" x2="504.9" y2="369.7" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="352.7" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="508.7" y1="353.3" x2="508.7" y2="369.0" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="356.2" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="512.5" y1="362.3" x2="512.5" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="364.9" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="516.2" y1="373.0" x2="516.2" y2="403.6" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="377.2" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="520.0" y1="365.8" x2="520.0" y2="385.0" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="369.2" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="523.8" y1="362.6" x2="523.8" y2="375.0" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="371.5" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="527.6" y1="367.5" x2="527.6" y2="386.3" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="370.4" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="531.4" y1="375.7" x2="531.4" y2="391.7" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="381.5" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="535.2" y1="388.1" x2="535.2" y2="415.9" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="392.8" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="539.0" y1="399.6" x2="539.0" y2="414.6" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="403.3" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="542.7" y1="397.0" x2="542.7" y2="416.5" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="404.4" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="546.5" y1="413.5" x2="546.5" y2="424.1" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="414.5" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="550.3" y1="408.6" x2="550.3" y2="442.1" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="415.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="554.1" y1="379.3" x2="554.1" y2="427.0" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="391.8" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="557.9" y1="384.8" x2="557.9" y2="398.1" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="387.5" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="561.7" y1="378.6" x2="561.7" y2="390.9" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="383.2" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="565.5" y1="407.5" x2="565.5" y2="432.7" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="413.3" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="569.3" y1="418.3" x2="569.3" y2="430.9" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="418.8" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="573.0" y1="387.8" x2="573.0" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="391.2" width="2.35" height="26.4" fill="var(--up)"/>
<line x1="576.8" y1="383.3" x2="576.8" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="388.5" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="580.6" y1="377.5" x2="580.6" y2="397.5" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="389.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="584.4" y1="385.4" x2="584.4" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="388.8" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="588.2" y1="350.8" x2="588.2" y2="397.5" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="355.1" width="2.35" height="41.9" fill="var(--up)"/>
<line x1="592.0" y1="346.4" x2="592.0" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="356.1" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="595.8" y1="346.4" x2="595.8" y2="374.2" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="352.9" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="599.5" y1="339.7" x2="599.5" y2="373.8" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="349.4" width="2.35" height="20.4" fill="var(--up)"/>
<line x1="603.3" y1="336.4" x2="603.3" y2="364.1" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="346.8" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="607.1" y1="344.1" x2="607.1" y2="357.9" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="350.3" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="610.9" y1="340.2" x2="610.9" y2="360.9" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="342.0" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="614.7" y1="343.2" x2="614.7" y2="368.5" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="352.8" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="618.5" y1="366.7" x2="618.5" y2="392.8" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="370.0" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="622.3" y1="374.9" x2="622.3" y2="393.9" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="389.3" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="626.0" y1="385.4" x2="626.0" y2="401.8" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="392.9" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="629.8" y1="386.1" x2="629.8" y2="405.4" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="389.8" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="633.6" y1="387.9" x2="633.6" y2="412.8" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="389.3" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="637.4" y1="395.3" x2="637.4" y2="425.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="399.1" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="641.2" y1="408.7" x2="641.2" y2="448.8" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="417.4" width="2.35" height="29.7" fill="var(--down)"/>
<line x1="645.0" y1="446.1" x2="645.0" y2="462.9" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="451.9" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="648.8" y1="438.9" x2="648.8" y2="454.2" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="441.3" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="652.5" y1="423.4" x2="652.5" y2="439.7" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="426.1" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="656.3" y1="420.9" x2="656.3" y2="442.3" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="423.6" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="660.1" y1="425.0" x2="660.1" y2="441.3" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="432.2" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="663.9" y1="423.4" x2="663.9" y2="448.3" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="430.7" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="667.7" y1="410.7" x2="667.7" y2="433.7" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="414.0" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="671.5" y1="390.8" x2="671.5" y2="413.4" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="396.7" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="675.3" y1="380.1" x2="675.3" y2="403.2" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="392.5" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="679.1" y1="386.2" x2="679.1" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="387.7" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="682.8" y1="389.9" x2="682.8" y2="402.2" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="390.6" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="686.6" y1="384.1" x2="686.6" y2="405.1" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="387.0" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="690.4" y1="373.3" x2="690.4" y2="407.7" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="392.9" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="694.2" y1="345.3" x2="694.2" y2="406.1" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="348.9" width="2.35" height="56.2" fill="var(--up)"/>
<line x1="698.0" y1="317.8" x2="698.0" y2="341.7" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="333.8" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="701.8" y1="279.7" x2="701.8" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="301.1" width="2.35" height="29.8" fill="var(--up)"/>
<line x1="705.6" y1="280.7" x2="705.6" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="284.2" width="2.35" height="21.8" fill="var(--down)"/>
<line x1="709.3" y1="305.0" x2="709.3" y2="328.7" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="310.5" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="713.1" y1="297.1" x2="713.1" y2="333.6" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="304.5" width="2.35" height="16.3" fill="var(--up)"/>
<line x1="716.9" y1="302.1" x2="716.9" y2="338.3" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="304.5" width="2.35" height="26.5" fill="var(--down)"/>
<line x1="720.7" y1="310.7" x2="720.7" y2="332.3" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="317.4" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="724.5" y1="276.6" x2="724.5" y2="309.9" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="289.9" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="728.3" y1="259.3" x2="728.3" y2="287.1" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="269.8" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="732.1" y1="219.1" x2="732.1" y2="271.9" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="229.4" width="2.35" height="39.3" fill="var(--up)"/>
<line x1="735.8" y1="210.2" x2="735.8" y2="236.9" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="222.1" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="739.6" y1="238.5" x2="739.6" y2="284.1" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="246.7" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="743.4" y1="223.3" x2="743.4" y2="252.0" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="241.1" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="747.2" y1="213.5" x2="747.2" y2="244.2" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="224.7" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="751.0" y1="191.8" x2="751.0" y2="261.7" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="222.7" width="2.35" height="34.4" fill="var(--down)"/>
<line x1="754.8" y1="253.0" x2="754.8" y2="298.2" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="258.9" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="758.6" y1="247.3" x2="758.6" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="271.3" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="762.4" y1="250.6" x2="762.4" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="252.2" width="2.35" height="33.5" fill="var(--up)"/>
<line x1="766.1" y1="213.8" x2="766.1" y2="254.6" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="230.3" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="769.9" y1="205.2" x2="769.9" y2="245.1" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="224.7" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="773.7" y1="206.1" x2="773.7" y2="325.0" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="232.2" width="2.35" height="67.0" fill="var(--down)"/>
<line x1="777.5" y1="250.8" x2="777.5" y2="315.0" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="263.1" width="2.35" height="51.1" fill="var(--up)"/>
<line x1="781.3" y1="239.8" x2="781.3" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="249.6" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="785.1" y1="255.4" x2="785.1" y2="288.7" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="257.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="788.9" y1="240.1" x2="788.9" y2="270.5" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="240.7" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="792.6" y1="202.1" x2="792.6" y2="240.6" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="202.4" width="2.35" height="37.4" fill="var(--up)"/>
<line x1="796.4" y1="187.9" x2="796.4" y2="218.8" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="198.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="800.2" y1="184.6" x2="800.2" y2="209.5" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="202.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="804.0" y1="188.0" x2="804.0" y2="214.0" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="197.7" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="807.8" y1="186.4" x2="807.8" y2="209.3" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="193.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="811.6" y1="188.7" x2="811.6" y2="225.0" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="189.9" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="815.4" y1="149.6" x2="815.4" y2="189.4" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="153.3" width="2.35" height="35.7" fill="var(--up)"/>
<line x1="819.1" y1="147.4" x2="819.1" y2="182.5" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="149.6" width="2.35" height="25.3" fill="var(--down)"/>
<line x1="822.9" y1="169.2" x2="822.9" y2="211.6" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="178.3" width="2.35" height="27.2" fill="var(--down)"/>
<line x1="826.7" y1="189.3" x2="826.7" y2="224.8" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="205.3" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="830.5" y1="154.6" x2="830.5" y2="204.7" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="166.0" width="2.35" height="38.1" fill="var(--up)"/>
<line x1="834.3" y1="178.2" x2="834.3" y2="246.7" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="180.2" width="2.35" height="57.1" fill="var(--down)"/>
<line x1="838.1" y1="214.0" x2="838.1" y2="248.7" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="233.6" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="841.9" y1="231.1" x2="841.9" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="234.4" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="845.6" y1="225.2" x2="845.6" y2="255.3" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="230.6" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="849.4" y1="230.7" x2="849.4" y2="265.7" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="239.5" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="853.2" y1="227.3" x2="853.2" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="240.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="857.0" y1="229.0" x2="857.0" y2="254.4" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="243.3" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="860.8" y1="233.5" x2="860.8" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="235.2" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="864.6" y1="248.8" x2="864.6" y2="275.1" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="251.3" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="868.4" y1="209.1" x2="868.4" y2="273.8" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="218.2" width="2.35" height="51.3" fill="var(--up)"/>
<line x1="872.2" y1="184.8" x2="872.2" y2="222.8" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="198.2" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="875.9" y1="182.7" x2="875.9" y2="227.9" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="192.5" width="2.35" height="35.3" fill="var(--down)"/>
<line x1="879.7" y1="196.2" x2="879.7" y2="242.7" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="218.0" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="883.5" y1="187.8" x2="883.5" y2="238.4" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="205.1" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="887.3" y1="215.3" x2="887.3" y2="250.3" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="220.5" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="891.1" y1="178.2" x2="891.1" y2="224.7" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="178.4" width="2.35" height="43.1" fill="var(--up)"/>
<line x1="894.9" y1="145.0" x2="894.9" y2="179.2" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="158.8" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="898.7" y1="151.1" x2="898.7" y2="207.4" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="162.0" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="902.4" y1="145.9" x2="902.4" y2="206.0" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="149.0" width="2.35" height="41.7" fill="var(--up)"/>
<line x1="906.2" y1="135.1" x2="906.2" y2="173.2" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="150.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="910.0" y1="152.8" x2="910.0" y2="208.5" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="153.5" width="2.35" height="49.4" fill="var(--down)"/>
<line x1="913.8" y1="202.8" x2="913.8" y2="231.7" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="202.9" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="917.6" y1="211.3" x2="917.6" y2="227.7" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="219.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="921.4" y1="206.6" x2="921.4" y2="233.8" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="218.9" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="925.2" y1="211.8" x2="925.2" y2="255.0" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="230.1" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="928.9" y1="227.6" x2="928.9" y2="267.1" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="244.3" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="932.7" y1="194.1" x2="932.7" y2="250.2" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="203.4" width="2.35" height="27.4" fill="var(--up)"/>
<line x1="936.5" y1="175.3" x2="936.5" y2="221.9" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="180.9" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="940.3" y1="188.4" x2="940.3" y2="218.8" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="190.5" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="944.1" y1="167.9" x2="944.1" y2="207.5" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="171.0" width="2.35" height="32.0" fill="var(--up)"/>
<line x1="947.9" y1="145.2" x2="947.9" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="152.7" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="951.7" y1="139.8" x2="951.7" y2="181.9" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="143.3" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="955.5" y1="126.6" x2="955.5" y2="156.6" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="134.5" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="959.2" y1="103.4" x2="959.2" y2="144.2" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="113.3" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="963.0" y1="85.0" x2="963.0" y2="162.9" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="110.3" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="966.8" y1="73.9" x2="966.8" y2="127.1" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="80.9" width="2.35" height="43.0" fill="var(--up)"/>
<line x1="970.6" y1="79.0" x2="970.6" y2="163.9" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="81.9" width="2.35" height="79.0" fill="var(--down)"/>
<line x1="974.4" y1="142.0" x2="974.4" y2="177.2" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="162.4" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="978.2" y1="168.3" x2="978.2" y2="194.6" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="170.2" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="982.0" y1="162.9" x2="982.0" y2="195.9" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="168.9" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="985.7" y1="149.6" x2="985.7" y2="176.8" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="162.3" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="989.5" y1="159.5" x2="989.5" y2="205.5" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="170.0" width="2.35" height="28.9" fill="var(--down)"/>
<line x1="993.3" y1="186.1" x2="993.3" y2="207.6" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="193.4" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="997.1" y1="159.8" x2="997.1" y2="197.6" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="179.0" width="2.35" height="16.0" fill="var(--up)"/>
<line x1="1000.9" y1="178.9" x2="1000.9" y2="213.5" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="181.5" width="2.35" height="27.9" fill="var(--down)"/>
<line x1="1004.7" y1="201.3" x2="1004.7" y2="222.2" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="209.7" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="1008.5" y1="218.7" x2="1008.5" y2="248.5" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="223.9" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="1012.2" y1="237.5" x2="1012.2" y2="257.0" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="251.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1016.0" y1="222.9" x2="1016.0" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="232.1" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="1019.8" y1="221.5" x2="1019.8" y2="240.9" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="233.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1023.6" y1="231.9" x2="1023.6" y2="280.5" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="233.5" width="2.35" height="37.8" fill="var(--down)"/>
<line x1="1027.4" y1="254.5" x2="1027.4" y2="271.1" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="264.0" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="1031.2" y1="210.6" x2="1031.2" y2="274.2" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="228.7" width="2.35" height="37.0" fill="var(--up)"/>
<line x1="1035.0" y1="225.5" x2="1035.0" y2="247.2" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="226.1" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="1038.7" y1="221.5" x2="1038.7" y2="248.6" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="232.0" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="1042.5" y1="207.2" x2="1042.5" y2="240.8" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="214.6" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="1046.3" y1="212.0" x2="1046.3" y2="235.3" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="215.1" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="1050.1" y1="214.0" x2="1050.1" y2="222.1" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="219.1" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="60" y1="198.5" x2="1052" y2="198.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="202.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$56 R1</text>
<text x="1058" y="214.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="141.2" x2="1052" y2="141.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="144.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$62 R2</text>
<text x="1058" y="156.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="274.3" x2="1052" y2="274.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="268.3" font-size="11.5" fill="var(--support)" font-weight="600">$49 S1</text>
<text x="1058" y="280.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="381.2" x2="1052" y2="381.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="375.2" font-size="11.5" fill="var(--support)" font-weight="600">$38 S2</text>
<text x="1058" y="387.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="409.1" x2="1052" y2="409.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="403.1" font-size="11.5" fill="var(--support)" font-weight="600">$35 S3</text>
<text x="1058" y="415.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="220.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="212.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $54 (2026-08-21)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). 기술적 분석 — 일봉·1년의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $62 | 2 | 2025-06-23·2025-12-01 — Equitrans 합병(2024.07) 이후 형성된 고점대 |
| R1 | $56 | 2 | 2025-02-17·2025-03-24 |
| **현재가** | **$53.87** (2026-08-21 기준 최근 주 종가) | — | R1과 S1 사이 |
| S1 | $49 | 3 | 2025-09-15·2026-01-12·2026-07-06 — 현재가에 가장 근접한 지지, 합병 이후 형성 |
| S2 | $38 | 2 | 2023-07-17·2023-09-25 — **합병 이전(순수 E&P 시기) 레벨, 참고선 성격** |
| S3 | $35 | 3 | 2022-05-09·2023-12-11·2024-10-28 — **합병 전후에 걸쳐 있어 참고선 성격**(2024-10-28은 합병 완료 3개월 후) |
| 참고선 | $16.29 (5년 최저) | — | 2022년 이전 저점으로, 이후 사업·자본구조가 완전히 달라져 근시일 지지로 보지 않음 |

> 레벨 개수는 5개(스크립트 기본값 3개에서 확대) — 위 ⚠️ 블록에서 밝힌 대로 합병 전후 자본구조 단절 때문에 하위 2개 레벨(S2·S3)은 참고선에 가깝다는 점을 표에 남기기 위해 확대했다(4. 방법론 · 한계에 반영).

---

## 3. 관측된 특이 구간 — 2024.07 Equitrans Midstream 합병 완료

- 2024.07.22 Equitrans Midstream 인수 완료([역사 / 주요 이벤트](./02_history.md) 참고) — 전량 주식교환 대가로 발행주식수가 약 42% 급증(419.9→596.9백만 주, 핵심 지표 A.2).
- 이 사건은 특정 주의 급격한 가격 갭보다는, **이후 몇 개월간 거래 레짐 자체를 재편**한 구조적 이벤트에 가깝다 — 합병 이전(S2 $38, S3 $35 부근)과 이후(S1 $49, R1 $56, R2 $62) 스윙 레벨이 뚜렷이 다른 가격대에 형성된 것이 그 근거.
- 이후 신용등급 상향(2026.05~06)까지 이어지는 디레버리징 스토리(재무 / 실적 3. 재무 건전성)가 겹치며, 2024년 말부터 저점(S1)이 우상향하는 추세가 형성됐다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-23~2026-08-21. 수집 시점: 2026-08-21. 원주가(과거 분할은 소급 반영, 배당은 미반영 — 조사 기간 내 배당 19회 지급)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 기술적 분석 — 일봉·1년(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py EQT --name "EQT Corporation" --interval 1wk --close-on 2026-08-20` — 레벨 개수만 기본값(3)에서 5로 확대(위 2. 지지선 / 저항선 요약 각주 근거).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 스크립트에 고정된 파라미터이며, 최적화된 값이 아니다.
    - **5년 구간 안에 사업 구조 자체가 바뀌었다**(2024.07 Equitrans 합병) — 2. 지지선 / 저항선 요약·3. 관측된 특이 구간 — 2024.07 Equitrans Midstream 합병 완료에서 밝힌 대로 합병 이전 레벨(S2·S3)은 지금과 다른 자본구조에서 형성돼 참고선으로만 취급했다.
    - 원자재 가격(헨리허브) 사이클이 겹쳐 있어, 합병 효과와 순수 가격 사이클 효과를 이 차트만으로는 분리하기 어렵다.

---

## 관련 문서

- [개요](./01_overview.md)
- [역사 / 주요 이벤트](./02_history.md)
- [CEO / 경영진](./03_ceo.md)
- [핵심 지표](./04_metrics.md)
- [재무 / 실적](./05_financials.md)
- [밸류에이션 / 적정주가](./06_valuation.md)
- [투자 판단](./07_investment.md)
- [최근 뉴스 / 이슈](./08_news.md)
- [기술적 분석 — 일봉·1년](./09_technical_daily.md)
- [최종 보고서](./11_final_report.md)

---

## 참고 자료

- [Yahoo Finance — EQT Corporation (EQT)](https://finance.yahoo.com/quote/EQT/)
- [StockAnalysis — EQT 종가 이력](https://stockanalysis.com/stocks/eqt/history/)

---

*작성일: 2026-08-21 (최종 수정일: 2026-08-23)*
