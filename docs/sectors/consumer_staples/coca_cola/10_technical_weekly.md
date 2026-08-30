# 기술적 분석 (주봉 캔들차트 · 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 최근 1년의 세부 구조는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: 주봉 마지막 봉의 종가는 **2026-08-28 $89.66**으로, [핵심 지표 A.2](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 **2026-08-27 $89.06과 $0.60(0.7%) 다르다.** 어느 쪽이 수정주가라서 갈린 것이 아니라 **기준 거래일이 하루 다르기 때문**이며(일봉 원자료에 2026-08-28이 아직 없다), 밸류에이션 인용은 모두 일봉 기준 $89.06으로 통일했다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-08-28)

<div class="ko-chart">
<style>
.ko-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ko-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ko-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ko-chart svg { width:100%; height:auto; display:block; }
.ko-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ko-chart .title { fill: var(--ink); font-weight:600; }
.ko-chart .grid { stroke: var(--grid); stroke-width:1; }
.ko-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="코카콜라(KO) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">코카콜라 (KO) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 $89.66 (2026-08-28) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="496.5" x2="1052" y2="496.5" class="grid"/>
<text x="52" y="500.5" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="366.9" x2="1052" y2="366.9" class="grid"/>
<text x="52" y="370.9" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="237.4" x2="1052" y2="237.4" class="grid"/>
<text x="52" y="241.4" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="107.8" x2="1052" y2="107.8" class="grid"/>
<text x="52" y="111.8" font-size="11" text-anchor="end" fill="var(--muted)">90</text>
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
<line x1="61.9" y1="534.9" x2="61.9" y2="552.9" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="538.8" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="65.7" y1="539.3" x2="65.7" y2="554.6" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="540.5" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="69.5" y1="543.1" x2="69.5" y2="569.4" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="551.6" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="73.3" y1="563.6" x2="73.3" y2="577.7" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="572.8" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="77.0" y1="570.9" x2="77.0" y2="594.5" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="576.1" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="80.8" y1="569.1" x2="80.8" y2="594.9" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="572.6" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="84.6" y1="562.8" x2="84.6" y2="576.9" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="568.0" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="88.4" y1="564.3" x2="88.4" y2="577.2" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="568.4" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="92.2" y1="542.2" x2="92.2" y2="573.9" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="543.5" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="96.0" y1="533.2" x2="96.0" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="537.4" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="99.8" y1="535.4" x2="99.8" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="538.6" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="103.5" y1="536.1" x2="103.5" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="541.4" width="2.35" height="18.1" fill="var(--down)"/>
<line x1="107.3" y1="546.8" x2="107.3" y2="579.6" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="559.9" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="111.1" y1="564.7" x2="111.1" y2="596.5" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="573.5" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="114.9" y1="544.1" x2="114.9" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="544.6" width="2.35" height="25.5" fill="var(--up)"/>
<line x1="118.7" y1="510.4" x2="118.7" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="525.9" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="122.5" y1="514.5" x2="122.5" y2="535.3" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="519.5" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="126.3" y1="504.9" x2="126.3" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="506.7" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="130.0" y1="480.9" x2="130.0" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="492.2" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="133.8" y1="477.7" x2="133.8" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="478.4" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="137.6" y1="477.8" x2="137.6" y2="491.3" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="482.7" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="141.4" y1="484.4" x2="141.4" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="485.6" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="145.2" y1="473.4" x2="145.2" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="484.0" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="149.0" y1="466.3" x2="149.0" y2="494.5" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="478.6" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="152.8" y1="459.9" x2="152.8" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="463.5" width="2.35" height="30.8" fill="var(--up)"/>
<line x1="156.5" y1="458.9" x2="156.5" y2="506.6" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="459.5" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="160.3" y1="457.3" x2="160.3" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="463.2" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="164.1" y1="469.6" x2="164.1" y2="528.8" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="470.4" width="2.35" height="53.0" fill="var(--down)"/>
<line x1="167.9" y1="492.6" x2="167.9" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="495.2" width="2.35" height="27.6" fill="var(--up)"/>
<line x1="171.7" y1="475.6" x2="171.7" y2="496.5" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="476.6" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="175.5" y1="458.2" x2="175.5" y2="480.8" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="459.3" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="179.3" y1="444.1" x2="179.3" y2="474.2" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="446.8" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="183.1" y1="424.3" x2="183.1" y2="449.3" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="431.4" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="186.8" y1="405.8" x2="186.8" y2="442.3" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="428.4" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="190.6" y1="403.2" x2="190.6" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="405.8" width="2.35" height="31.0" fill="var(--down)"/>
<line x1="194.4" y1="427.7" x2="194.4" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="428.1" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="198.2" y1="421.3" x2="198.2" y2="454.9" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="422.4" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="202.0" y1="413.8" x2="202.0" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="426.0" width="2.35" height="57.8" fill="var(--down)"/>
<line x1="205.8" y1="430.4" x2="205.8" y2="475.9" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="435.8" width="2.35" height="39.3" fill="var(--up)"/>
<line x1="209.6" y1="440.5" x2="209.6" y2="469.1" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="443.6" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="213.3" y1="447.6" x2="213.3" y2="490.5" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="453.3" width="2.35" height="24.9" fill="var(--down)"/>
<line x1="217.1" y1="466.8" x2="217.1" y2="519.1" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="486.7" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="220.9" y1="456.8" x2="220.9" y2="509.3" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="457.1" width="2.35" height="46.0" fill="var(--up)"/>
<line x1="224.7" y1="438.8" x2="224.7" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="439.7" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="228.5" y1="442.3" x2="228.5" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="442.3" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="232.3" y1="451.6" x2="232.3" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="457.7" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="236.1" y1="462.1" x2="236.1" y2="486.2" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="463.8" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="239.8" y1="440.9" x2="239.8" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="442.4" width="2.35" height="33.9" fill="var(--up)"/>
<line x1="243.6" y1="431.2" x2="243.6" y2="461.9" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="443.5" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="247.4" y1="444.8" x2="247.4" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="448.5" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="251.2" y1="425.6" x2="251.2" y2="450.2" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="429.5" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="255.0" y1="432.7" x2="255.0" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="433.8" width="2.35" height="22.4" fill="var(--down)"/>
<line x1="258.8" y1="457.2" x2="258.8" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="461.6" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="262.6" y1="459.1" x2="262.6" y2="483.6" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="466.4" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="266.4" y1="460.1" x2="266.4" y2="508.0" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="465.0" width="2.35" height="37.4" fill="var(--down)"/>
<line x1="270.1" y1="487.4" x2="270.1" y2="522.4" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="504.4" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="273.9" y1="515.0" x2="273.9" y2="549.4" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="516.0" width="2.35" height="32.0" fill="var(--down)"/>
<line x1="277.7" y1="524.8" x2="277.7" y2="570.9" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="543.6" width="2.35" height="24.0" fill="var(--down)"/>
<line x1="281.5" y1="542.2" x2="281.5" y2="573.9" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="561.5" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="285.3" y1="538.2" x2="285.3" y2="561.7" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="548.8" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="289.1" y1="484.7" x2="289.1" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="486.6" width="2.35" height="53.4" fill="var(--up)"/>
<line x1="292.9" y1="489.1" x2="292.9" y2="521.1" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="489.8" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="296.6" y1="477.7" x2="296.6" y2="512.6" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="479.4" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="300.4" y1="474.2" x2="300.4" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="479.4" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="304.2" y1="460.1" x2="304.2" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="461.6" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="308.0" y1="437.9" x2="308.0" y2="473.8" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="440.1" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="311.8" y1="446.2" x2="311.8" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="452.3" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="315.6" y1="435.6" x2="315.6" y2="466.3" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="453.7" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="319.4" y1="444.0" x2="319.4" y2="464.5" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="447.0" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="323.1" y1="436.2" x2="323.1" y2="455.4" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="445.5" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="326.9" y1="448.9" x2="326.9" y2="469.5" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="450.3" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="330.7" y1="448.3" x2="330.7" y2="488.8" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="453.7" width="2.35" height="24.2" fill="var(--down)"/>
<line x1="334.5" y1="465.6" x2="334.5" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="474.0" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="338.3" y1="472.5" x2="338.3" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="490.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="342.1" y1="476.0" x2="342.1" y2="506.4" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="489.5" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="345.9" y1="492.0" x2="345.9" y2="511.0" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="499.2" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="349.6" y1="484.8" x2="349.6" y2="510.1" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="494.9" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="353.4" y1="491.0" x2="353.4" y2="504.4" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="496.6" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="357.2" y1="492.6" x2="357.2" y2="517.6" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="494.1" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="361.0" y1="489.1" x2="361.0" y2="509.5" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="506.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="364.8" y1="485.2" x2="364.8" y2="506.3" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="496.2" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="368.6" y1="483.2" x2="368.6" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="484.8" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="372.4" y1="467.3" x2="372.4" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="470.2" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="376.2" y1="457.1" x2="376.2" y2="472.4" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="459.7" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="379.9" y1="455.5" x2="379.9" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="456.9" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="383.7" y1="441.1" x2="383.7" y2="455.8" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="444.0" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="387.5" y1="431.8" x2="387.5" y2="456.2" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="434.9" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="391.3" y1="435.7" x2="391.3" y2="454.1" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="442.7" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="395.1" y1="442.2" x2="395.1" y2="457.7" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="443.2" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="398.9" y1="441.4" x2="398.9" y2="463.2" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="441.8" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="402.7" y1="459.3" x2="402.7" y2="495.0" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="460.3" width="2.35" height="32.8" fill="var(--down)"/>
<line x1="406.4" y1="479.4" x2="406.4" y2="504.6" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="481.4" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="410.2" y1="477.8" x2="410.2" y2="498.8" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="483.5" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="414.0" y1="468.3" x2="414.0" y2="496.2" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="474.8" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="417.8" y1="469.3" x2="417.8" y2="483.8" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="475.9" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="421.6" y1="478.8" x2="421.6" y2="499.4" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="480.8" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="425.4" y1="482.2" x2="425.4" y2="500.0" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="493.9" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="429.2" y1="483.0" x2="429.2" y2="511.5" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="484.8" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="432.9" y1="461.7" x2="432.9" y2="491.1" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="464.8" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="436.7" y1="454.1" x2="436.7" y2="478.4" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="464.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="440.5" y1="462.9" x2="440.5" y2="488.4" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="464.7" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="444.3" y1="474.0" x2="444.3" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="481.3" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="448.1" y1="477.3" x2="448.1" y2="491.7" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="479.4" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="451.9" y1="484.4" x2="451.9" y2="496.7" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="485.3" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="455.7" y1="486.9" x2="455.7" y2="507.9" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="489.3" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="459.5" y1="505.3" x2="459.5" y2="522.2" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="506.2" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="463.2" y1="509.4" x2="463.2" y2="525.6" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="517.2" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="467.0" y1="511.6" x2="467.0" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="522.6" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="470.8" y1="529.0" x2="470.8" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="530.1" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="474.6" y1="548.1" x2="474.6" y2="605.9" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="549.4" width="2.35" height="35.9" fill="var(--down)"/>
<line x1="478.4" y1="569.9" x2="478.4" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="587.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="482.2" y1="561.0" x2="482.2" y2="589.2" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="566.8" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="486.0" y1="540.1" x2="486.0" y2="573.5" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="558.1" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="489.7" y1="527.7" x2="489.7" y2="555.8" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="538.7" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="493.5" y1="529.2" x2="493.5" y2="547.5" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="538.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="497.3" y1="528.5" x2="497.3" y2="540.5" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="532.0" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="501.1" y1="512.6" x2="501.1" y2="535.8" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="515.0" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="504.9" y1="511.6" x2="504.9" y2="527.5" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="514.1" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="508.7" y1="509.9" x2="508.7" y2="519.6" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="514.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="512.5" y1="495.9" x2="512.5" y2="525.0" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="511.6" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="516.2" y1="503.1" x2="516.2" y2="529.2" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="512.0" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="520.0" y1="509.7" x2="520.0" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="510.3" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="523.8" y1="493.1" x2="523.8" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="500.7" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="527.6" y1="490.5" x2="527.6" y2="504.0" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="491.4" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="531.4" y1="490.9" x2="531.4" y2="502.5" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="491.4" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="535.2" y1="495.5" x2="535.2" y2="513.8" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="499.6" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="539.0" y1="483.4" x2="539.0" y2="507.2" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="489.5" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="542.7" y1="491.5" x2="542.7" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="491.5" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="546.5" y1="487.9" x2="546.5" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="500.9" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="550.3" y1="475.5" x2="550.3" y2="502.8" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="480.9" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="554.1" y1="480.0" x2="554.1" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="480.4" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="557.9" y1="495.0" x2="557.9" y2="509.8" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="502.7" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="561.7" y1="480.8" x2="561.7" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="498.0" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="565.5" y1="483.6" x2="565.5" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="490.1" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="569.3" y1="477.9" x2="569.3" y2="494.9" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="481.2" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="573.0" y1="479.6" x2="573.0" y2="510.6" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="481.2" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="576.8" y1="499.8" x2="576.8" y2="520.7" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="504.2" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="580.6" y1="491.8" x2="580.6" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="494.3" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="584.4" y1="462.9" x2="584.4" y2="500.1" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="473.9" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="588.2" y1="459.8" x2="588.2" y2="480.8" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="468.3" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="592.0" y1="452.9" x2="592.0" y2="471.8" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="454.2" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="595.8" y1="447.7" x2="595.8" y2="460.2" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="454.5" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="599.5" y1="457.3" x2="599.5" y2="470.9" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="458.5" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="603.3" y1="457.2" x2="603.3" y2="482.6" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="458.5" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="607.1" y1="440.0" x2="607.1" y2="464.7" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="445.8" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="610.9" y1="444.8" x2="610.9" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="445.4" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="614.7" y1="456.3" x2="614.7" y2="471.2" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="460.6" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="618.5" y1="441.1" x2="618.5" y2="458.8" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="449.2" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="622.3" y1="440.7" x2="622.3" y2="459.4" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="444.2" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="626.0" y1="443.2" x2="626.0" y2="466.8" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="448.5" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="629.8" y1="421.2" x2="629.8" y2="453.1" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="427.9" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="633.6" y1="404.3" x2="633.6" y2="440.5" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="405.1" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="637.4" y1="371.2" x2="637.4" y2="414.1" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="375.6" width="2.35" height="31.7" fill="var(--up)"/>
<line x1="641.2" y1="372.7" x2="641.2" y2="396.3" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="380.0" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="645.0" y1="376.0" x2="645.0" y2="395.0" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="377.5" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="648.8" y1="365.2" x2="648.8" y2="382.8" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="369.6" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="652.5" y1="333.6" x2="652.5" y2="370.4" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="334.9" width="2.35" height="34.2" fill="var(--up)"/>
<line x1="656.3" y1="321.2" x2="656.3" y2="355.4" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="335.3" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="660.1" y1="335.6" x2="660.1" y2="360.7" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="348.6" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="663.9" y1="336.1" x2="663.9" y2="362.0" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="344.0" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="667.7" y1="338.4" x2="667.7" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="343.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="671.5" y1="331.3" x2="671.5" y2="370.5" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="341.0" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="675.3" y1="365.6" x2="675.3" y2="381.7" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="366.3" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="679.1" y1="351.2" x2="679.1" y2="373.8" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="361.2" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="682.8" y1="362.6" x2="682.8" y2="411.2" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="366.9" width="2.35" height="39.9" fill="var(--down)"/>
<line x1="686.6" y1="400.6" x2="686.6" y2="433.1" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="406.3" width="2.35" height="25.3" fill="var(--down)"/>
<line x1="690.4" y1="425.6" x2="690.4" y2="455.3" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="430.6" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="694.2" y1="443.1" x2="694.2" y2="478.4" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="444.8" width="2.35" height="29.1" fill="var(--down)"/>
<line x1="698.0" y1="438.4" x2="698.0" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="445.7" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="701.8" y1="430.4" x2="701.8" y2="447.6" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="440.5" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="705.6" y1="442.2" x2="705.6" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="444.0" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="709.3" y1="445.7" x2="709.3" y2="473.3" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="456.0" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="713.1" y1="446.4" x2="713.1" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="454.6" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="716.9" y1="458.2" x2="716.9" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="464.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="720.7" y1="460.8" x2="720.7" y2="475.5" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="466.1" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="724.5" y1="473.5" x2="724.5" y2="488.4" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="477.0" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="728.3" y1="460.6" x2="728.3" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="461.3" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="732.1" y1="454.6" x2="732.1" y2="478.7" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="458.9" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="735.8" y1="440.9" x2="735.8" y2="466.9" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="451.4" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="739.6" y1="445.7" x2="739.6" y2="466.0" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="446.7" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="743.4" y1="366.5" x2="743.4" y2="449.0" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="381.5" width="2.35" height="61.8" fill="var(--up)"/>
<line x1="747.2" y1="346.2" x2="747.2" y2="387.4" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="349.4" width="2.35" height="36.3" fill="var(--up)"/>
<line x1="751.0" y1="344.0" x2="751.0" y2="362.6" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="351.2" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="754.8" y1="332.6" x2="754.8" y2="374.0" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="348.4" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="758.6" y1="325.2" x2="758.6" y2="387.9" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="341.5" width="2.35" height="36.3" fill="var(--down)"/>
<line x1="762.4" y1="364.4" x2="762.4" y2="390.5" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="376.8" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="766.1" y1="349.8" x2="766.1" y2="388.5" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="362.1" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="769.9" y1="315.7" x2="769.9" y2="369.6" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="357.5" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="773.7" y1="342.9" x2="773.7" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="348.4" width="2.35" height="67.4" fill="var(--up)"/>
<line x1="777.5" y1="322.5" x2="777.5" y2="354.9" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="328.0" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="781.3" y1="310.2" x2="781.3" y2="352.3" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="323.1" width="2.35" height="19.0" fill="var(--down)"/>
<line x1="785.1" y1="321.8" x2="785.1" y2="363.3" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="340.0" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="788.9" y1="332.1" x2="788.9" y2="361.0" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="345.3" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="792.6" y1="337.6" x2="792.6" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="341.0" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="796.4" y1="338.8" x2="796.4" y2="358.0" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="340.6" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="800.2" y1="334.9" x2="800.2" y2="361.0" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="339.7" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="804.0" y1="340.5" x2="804.0" y2="360.8" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="340.6" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="807.8" y1="332.1" x2="807.8" y2="357.5" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="349.4" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="811.6" y1="345.9" x2="811.6" y2="382.7" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="351.4" width="2.35" height="30.6" fill="var(--down)"/>
<line x1="815.4" y1="359.7" x2="815.4" y2="380.3" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="362.6" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="819.1" y1="335.2" x2="819.1" y2="365.7" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="349.4" width="2.35" height="15.8" fill="var(--up)"/>
<line x1="822.9" y1="349.2" x2="822.9" y2="380.3" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="349.2" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="826.7" y1="357.8" x2="826.7" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="368.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="830.5" y1="358.9" x2="830.5" y2="385.0" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="364.4" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="834.3" y1="374.4" x2="834.3" y2="396.2" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="381.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="838.1" y1="355.6" x2="838.1" y2="388.8" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="362.5" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="841.9" y1="353.2" x2="841.9" y2="374.8" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="363.0" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="845.6" y1="344.8" x2="845.6" y2="379.2" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="365.2" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="849.4" y1="363.9" x2="849.4" y2="389.2" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="365.5" width="2.35" height="14.5" fill="var(--down)"/>
<line x1="853.2" y1="373.9" x2="853.2" y2="401.0" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="380.4" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="857.0" y1="390.6" x2="857.0" y2="406.5" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="394.6" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="860.8" y1="404.1" x2="860.8" y2="418.1" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="409.9" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="864.6" y1="406.8" x2="864.6" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="416.7" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="868.4" y1="405.9" x2="868.4" y2="427.1" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="410.3" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="872.2" y1="400.6" x2="872.2" y2="420.8" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="405.3" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="875.9" y1="386.3" x2="875.9" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="387.1" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="879.7" y1="345.9" x2="879.7" y2="393.9" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="370.7" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="883.5" y1="355.2" x2="883.5" y2="394.1" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="369.8" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="887.3" y1="355.6" x2="887.3" y2="397.2" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="359.8" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="891.1" y1="342.4" x2="891.1" y2="374.2" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="351.9" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="894.9" y1="325.6" x2="894.9" y2="359.5" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="328.7" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="898.7" y1="325.1" x2="898.7" y2="346.6" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="326.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="902.4" y1="329.2" x2="902.4" y2="368.6" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="333.2" width="2.35" height="33.7" fill="var(--down)"/>
<line x1="906.2" y1="358.0" x2="906.2" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="360.2" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="910.0" y1="349.8" x2="910.0" y2="366.5" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="361.3" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="913.8" y1="363.5" x2="913.8" y2="371.3" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="367.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="917.6" y1="361.5" x2="917.6" y2="380.1" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="366.9" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="921.4" y1="358.4" x2="921.4" y2="402.3" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="360.3" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="925.2" y1="344.8" x2="925.2" y2="366.4" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="355.2" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="928.9" y1="327.3" x2="928.9" y2="369.6" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="329.6" width="2.35" height="37.3" fill="var(--up)"/>
<line x1="932.7" y1="303.4" x2="932.7" y2="337.5" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="304.6" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="936.5" y1="247.7" x2="936.5" y2="309.9" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="249.9" width="2.35" height="52.1" fill="var(--up)"/>
<line x1="940.3" y1="232.1" x2="940.3" y2="289.1" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="254.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="944.1" y1="239.4" x2="944.1" y2="255.6" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="239.4" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="947.9" y1="211.5" x2="947.9" y2="243.8" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="217.2" width="2.35" height="26.4" fill="var(--up)"/>
<line x1="951.7" y1="219.2" x2="951.7" y2="284.6" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="221.2" width="2.35" height="54.5" fill="var(--down)"/>
<line x1="955.5" y1="258.0" x2="955.5" y2="282.3" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="271.8" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="959.2" y1="257.7" x2="959.2" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="263.3" width="2.35" height="42.1" fill="var(--down)"/>
<line x1="963.0" y1="288.5" x2="963.0" y2="314.2" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="292.9" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="966.8" y1="276.0" x2="966.8" y2="298.8" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="279.9" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="970.6" y1="259.5" x2="970.6" y2="298.0" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="270.1" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="974.4" y1="270.4" x2="974.4" y2="305.8" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="272.1" width="2.35" height="20.5" fill="var(--down)"/>
<line x1="978.2" y1="276.1" x2="978.2" y2="308.0" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="281.0" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="982.0" y1="233.2" x2="982.0" y2="297.0" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="255.8" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="985.7" y1="246.0" x2="985.7" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="257.8" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="989.5" y1="219.7" x2="989.5" y2="265.3" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="226.7" width="2.35" height="34.5" fill="var(--up)"/>
<line x1="993.3" y1="202.9" x2="993.3" y2="232.3" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="218.2" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="997.1" y1="204.8" x2="997.1" y2="251.5" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="226.5" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="1000.9" y1="227.8" x2="1000.9" y2="278.7" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="244.1" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="1004.7" y1="185.0" x2="1004.7" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="203.4" width="2.35" height="42.9" fill="var(--up)"/>
<line x1="1008.5" y1="219.4" x2="1008.5" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="223.4" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="1012.2" y1="201.0" x2="1012.2" y2="249.5" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="203.3" width="2.35" height="43.8" fill="var(--up)"/>
<line x1="1016.0" y1="183.7" x2="1016.0" y2="224.9" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="183.7" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="1019.8" y1="163.8" x2="1019.8" y2="215.2" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="184.3" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="1023.6" y1="165.3" x2="1023.6" y2="226.6" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="186.8" width="2.35" height="30.3" fill="var(--down)"/>
<line x1="1027.4" y1="199.5" x2="1027.4" y2="226.0" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="208.2" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="1031.2" y1="95.9" x2="1031.2" y2="205.0" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="139.0" width="2.35" height="58.4" fill="var(--up)"/>
<line x1="1035.0" y1="127.5" x2="1035.0" y2="170.5" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="127.5" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="1038.7" y1="134.1" x2="1038.7" y2="164.0" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="137.5" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="1042.5" y1="83.6" x2="1042.5" y2="148.6" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="93.6" width="2.35" height="49.2" fill="var(--up)"/>
<line x1="1046.3" y1="75.6" x2="1046.3" y2="121.3" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="80.4" width="2.35" height="39.6" fill="var(--down)"/>
<line x1="1050.1" y1="107.4" x2="1050.1" y2="119.9" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="112.2" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="60" y1="384.0" x2="1052" y2="384.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="378.0" font-size="11.5" fill="var(--support)" font-weight="600">$69 S1</text>
<text x="1058" y="390.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="410.9" x2="1052" y2="410.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="404.9" font-size="11.5" fill="var(--support)" font-weight="600">$67 S2</text>
<text x="1058" y="416.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="483.2" x2="1052" y2="483.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="477.2" font-size="11.5" fill="var(--support)" font-weight="600">$61 S3</text>
<text x="1058" y="489.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="112.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="104.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $90 (2026-08-28)</text>
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
|------|------|-----------|------|
| **현재가** | **$89.66** (2026-08-28 주봉 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $69 | 2 | 2025-05-12·2025-06-16 주의 스윙 저점대. FY2025 상반기 조정 구간의 바닥이며, 공교롭게 FY2025 연말 종가($69.91)와 겹친다 |
| S2 | $67 | 4 | 2025-04-07·2025-07-28·2025-09-29·2026-01-05 주. **5년 중 터치가 가장 많은 레벨**로, 2025년 내내 반복해서 되돌아온 가격대다 |
| S3 | $61 | 3 | 2024-05-27·2024-11-11·2025-01-06 주. 2024년 박스권의 하단 |
| 참고선 | $92.49 | — | 5년 최고(2026-08-24 주). 저항으로 검증된 가격대가 아니다 |
| 참고선 | $51.55 | — | 5년 최저. 현재가에서 −43% 떨어져 있어 근시일 지지로 볼 수 없다 |

일봉과 마찬가지로 **저항선(R)이 하나도 없다** — 5년 고점이 곧 현재가 부근이기 때문이다. 눈여겨볼 것은 **현재가와 가장 가까운 지지(S1 $69)가 −23% 아래에 있다**는 점으로, 2026년 상승 구간에서 새로 만들어진 스윙 저점대가 아직 주봉 클러스터로 잡히지 않았다는 뜻이다. 근시일 하방 참고는 주봉이 아니라 [일봉 문서의 S1($85)](./09_technical_daily.md)을 봐야 한다.

---

## 3. 관측된 특이 구간

5년 구간 안에 가격대를 구조적으로 재설정한 단일 이벤트는 없다. 주봉 기준으로는 **2025년 내내 $67~72 박스권에 머물다 2026년 들어 한 방향으로 올라온 흐름**이 전부이며, 그 상승의 계기가 된 일간 갭(2026-07-28 +5.0%)은 [일봉 문서 3. 관측된 특이 구간](./09_technical_daily.md)에서 다룬다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-30~2026-08-28. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py KO --name "코카콜라" --interval 1wk --close-on 2026-08-27 --emit all` (기본 옵션 그대로, `--force-level`·`--levels` 변경 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 5년 창에서 잡힌 지지 셋이 모두 2024~2025년 가격대라, **2026년 상승분(+27%)을 지지 구조로 설명하지 못한다.** 근시일 하방은 일봉 문서를 봐야 한다.
    - 기간 내 배당이 20회 있었고 이 차트는 원주가(배당 미반영)라, 실제 총수익 기준 성과는 표시된 가격 상승률보다 높다. 주식분할·유상증자 등 가격 연속성을 깨는 이벤트는 없었다(마지막 2:1 분할은 2012-08).

---

*작성일: 2026-08-30*
