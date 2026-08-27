# 기술적 분석 (주봉 캔들차트 · 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료 — 여러 금리·경기 사이클을 관통하는 다년 구조를 보기 위한 것이다. 최근 1년 세부 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 주봉 API에서 직접 수집한 것이다. **대조 결과**: 2026-08-14 종가 $418.80은 [밸류에이션 / 적정주가](./06_valuation.md)·[기술적 분석 — 일봉·1년](./09_technical_daily.md)에 인용된 값과 일치.
>
> ⚠️ 2026-07-01 Mobility Global(MBGL) 분사 관련 데이터 제공처(Yahoo Finance)의 "분할(split) 비율 1057:1000" 메타데이터는 실제 주식분할이 아니다 — 자세한 확인 내용은 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 상단 ⚠️ 참고. 5년 구간 안에는 이 외의 실제 주식분할 이력이 없다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-14)

<div class="spgi-chart">
<style>
.spgi-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .spgi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .spgi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.spgi-chart svg { width:100%; height:auto; display:block; }
.spgi-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.spgi-chart .title { fill: var(--ink); font-weight:600; }
.spgi-chart .grid { stroke: var(--grid); stroke-width:1; }
.spgi-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="S&P Global(SPGI) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">S&P Global (SPGI) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-14 · 마지막 종가 $418.80 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="541.9" x2="1052" y2="541.9" class="grid"/>
<text x="52" y="545.9" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="448.5" x2="1052" y2="448.5" class="grid"/>
<text x="52" y="452.5" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="355.0" x2="1052" y2="355.0" class="grid"/>
<text x="52" y="359.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="261.6" x2="1052" y2="261.6" class="grid"/>
<text x="52" y="265.6" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="168.1" x2="1052" y2="168.1" class="grid"/>
<text x="52" y="172.1" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="74.7" x2="1052" y2="74.7" class="grid"/>
<text x="52" y="78.7" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.6" y1="626.0" x2="137.6" y2="631.0" class="axis"/>
<text x="137.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="334.5" y1="626.0" x2="334.5" y2="631.0" class="axis"/>
<text x="334.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="531.4" y1="626.0" x2="531.4" y2="631.0" class="axis"/>
<text x="531.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="732.1" y1="626.0" x2="732.1" y2="631.0" class="axis"/>
<text x="732.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="928.9" y1="626.0" x2="928.9" y2="631.0" class="axis"/>
<text x="928.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="313.5" x2="61.9" y2="355.0" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="323.1" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="65.7" y1="320.4" x2="65.7" y2="336.3" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="324.7" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="69.5" y1="299.6" x2="69.5" y2="328.1" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="303.2" width="2.35" height="20.6" fill="var(--up)"/>
<line x1="73.3" y1="295.2" x2="73.3" y2="319.2" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="303.8" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="77.0" y1="295.3" x2="77.0" y2="317.8" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="300.2" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="80.8" y1="297.4" x2="80.8" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="301.5" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="84.6" y1="304.1" x2="84.6" y2="359.9" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="304.4" width="2.35" height="40.8" fill="var(--down)"/>
<line x1="88.4" y1="330.4" x2="88.4" y2="368.9" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="342.8" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="92.2" y1="313.1" x2="92.2" y2="351.9" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="317.7" width="2.35" height="28.5" fill="var(--up)"/>
<line x1="96.0" y1="301.4" x2="96.0" y2="331.9" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="306.1" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="99.8" y1="261.6" x2="99.8" y2="318.0" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="264.2" width="2.35" height="42.5" fill="var(--up)"/>
<line x1="103.5" y1="260.7" x2="103.5" y2="302.5" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="264.3" width="2.35" height="24.5" fill="var(--down)"/>
<line x1="107.3" y1="279.1" x2="107.3" y2="309.0" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="281.9" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="111.1" y1="267.7" x2="111.1" y2="307.1" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="286.9" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="114.9" y1="278.5" x2="114.9" y2="304.3" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="281.7" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="118.7" y1="276.7" x2="118.7" y2="315.2" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="289.8" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="122.5" y1="264.7" x2="122.5" y2="304.1" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="265.1" width="2.35" height="23.8" fill="var(--up)"/>
<line x1="126.3" y1="246.4" x2="126.3" y2="280.7" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="262.5" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="130.0" y1="258.4" x2="130.0" y2="299.9" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="265.0" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="133.8" y1="251.3" x2="133.8" y2="273.3" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="257.0" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="137.6" y1="266.6" x2="137.6" y2="313.8" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="266.6" width="2.35" height="46.1" fill="var(--down)"/>
<line x1="141.4" y1="305.9" x2="141.4" y2="347.1" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="326.2" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="145.2" y1="333.8" x2="145.2" y2="370.0" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="349.0" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="149.0" y1="362.0" x2="149.0" y2="411.3" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="378.6" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="152.8" y1="353.9" x2="152.8" y2="385.7" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="369.9" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="156.5" y1="364.1" x2="156.5" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="370.4" width="2.35" height="46.7" fill="var(--down)"/>
<line x1="160.3" y1="413.0" x2="160.3" y2="438.7" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="419.2" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="164.1" y1="422.3" x2="164.1" y2="459.8" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="429.1" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="167.9" y1="379.8" x2="167.9" y2="444.6" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="382.0" width="2.35" height="50.5" fill="var(--up)"/>
<line x1="171.7" y1="381.2" x2="171.7" y2="441.6" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="383.3" width="2.35" height="48.0" fill="var(--down)"/>
<line x1="175.5" y1="374.1" x2="175.5" y2="442.7" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="377.8" width="2.35" height="46.7" fill="var(--up)"/>
<line x1="179.3" y1="366.1" x2="179.3" y2="392.0" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="371.5" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="183.1" y1="353.7" x2="183.1" y2="385.4" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="370.0" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="186.8" y1="364.6" x2="186.8" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="372.2" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="190.6" y1="373.4" x2="190.6" y2="418.3" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="375.5" width="2.35" height="41.8" fill="var(--down)"/>
<line x1="194.4" y1="389.2" x2="194.4" y2="431.9" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="419.2" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="198.2" y1="414.4" x2="198.2" y2="441.9" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="435.6" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="202.0" y1="444.8" x2="202.0" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="459.0" width="2.35" height="32.2" fill="var(--down)"/>
<line x1="205.8" y1="497.0" x2="205.8" y2="532.9" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="506.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="209.6" y1="496.3" x2="209.6" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="497.1" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="213.3" y1="463.9" x2="213.3" y2="497.4" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="464.9" width="2.35" height="30.2" fill="var(--up)"/>
<line x1="217.1" y1="469.3" x2="217.1" y2="551.1" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="472.3" width="2.35" height="36.3" fill="var(--down)"/>
<line x1="220.9" y1="491.5" x2="220.9" y2="521.7" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="507.0" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="224.7" y1="520.7" x2="224.7" y2="550.5" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="525.9" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="228.5" y1="497.6" x2="228.5" y2="542.8" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="498.5" width="2.35" height="33.3" fill="var(--up)"/>
<line x1="232.3" y1="494.3" x2="232.3" y2="516.4" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="495.5" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="236.1" y1="473.4" x2="236.1" y2="507.2" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="479.3" width="2.35" height="25.1" fill="var(--up)"/>
<line x1="239.8" y1="472.5" x2="239.8" y2="507.5" stroke="var(--down)" class="wick"/>
<rect x="238.67" y="476.5" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="243.6" y1="458.4" x2="243.6" y2="493.2" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="462.6" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="247.4" y1="433.4" x2="247.4" y2="484.0" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="436.1" width="2.35" height="29.0" fill="var(--up)"/>
<line x1="251.2" y1="432.9" x2="251.2" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="436.6" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="255.0" y1="403.7" x2="255.0" y2="441.1" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="409.6" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="258.8" y1="402.8" x2="258.8" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="411.6" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="262.6" y1="430.4" x2="262.6" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="439.2" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="266.4" y1="457.0" x2="266.4" y2="491.6" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="465.1" width="2.35" height="22.8" fill="var(--down)"/>
<line x1="270.1" y1="446.2" x2="270.1" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="449.4" width="2.35" height="34.3" fill="var(--up)"/>
<line x1="273.9" y1="440.9" x2="273.9" y2="500.2" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="447.5" width="2.35" height="43.2" fill="var(--down)"/>
<line x1="277.7" y1="492.5" x2="277.7" y2="545.1" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="496.7" width="2.35" height="43.8" fill="var(--down)"/>
<line x1="281.5" y1="536.3" x2="281.5" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="541.7" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="285.3" y1="529.1" x2="285.3" y2="567.5" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="559.6" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="289.1" y1="559.4" x2="289.1" y2="608.7" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="559.5" width="2.35" height="36.2" fill="var(--down)"/>
<line x1="292.9" y1="561.3" x2="292.9" y2="594.6" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="579.3" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="296.6" y1="523.3" x2="296.6" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="524.5" width="2.35" height="50.8" fill="var(--up)"/>
<line x1="300.4" y1="525.2" x2="300.4" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="528.8" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="304.2" y1="470.1" x2="304.2" y2="549.8" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="472.8" width="2.35" height="61.6" fill="var(--up)"/>
<line x1="308.0" y1="469.9" x2="308.0" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="486.0" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="311.8" y1="462.4" x2="311.8" y2="503.2" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="469.7" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="315.6" y1="455.8" x2="315.6" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="466.4" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="319.4" y1="471.0" x2="319.4" y2="490.1" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="475.4" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="323.1" y1="454.7" x2="323.1" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="489.7" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="326.9" y1="502.5" x2="326.9" y2="521.9" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="503.5" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="330.7" y1="501.0" x2="330.7" y2="520.1" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="510.4" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="334.5" y1="485.0" x2="334.5" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="487.6" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="338.3" y1="450.8" x2="338.3" y2="487.3" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="454.8" width="2.35" height="26.9" fill="var(--up)"/>
<line x1="342.1" y1="440.7" x2="342.1" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="451.8" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="345.9" y1="439.1" x2="345.9" y2="465.4" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="442.4" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="349.6" y1="415.8" x2="349.6" y2="456.2" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="443.2" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="353.4" y1="439.9" x2="353.4" y2="467.3" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="453.1" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="357.2" y1="445.8" x2="357.2" y2="477.1" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="457.7" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="361.0" y1="471.2" x2="361.0" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="472.5" width="2.35" height="22.9" fill="var(--down)"/>
<line x1="364.8" y1="488.0" x2="364.8" y2="517.6" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="488.4" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="368.6" y1="478.3" x2="368.6" y2="527.5" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="488.9" width="2.35" height="36.3" fill="var(--down)"/>
<line x1="372.4" y1="498.7" x2="372.4" y2="534.7" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="511.2" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="376.2" y1="493.0" x2="376.2" y2="524.3" stroke="var(--down)" class="wick"/>
<rect x="374.98" y="510.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="379.9" y1="489.8" x2="379.9" y2="516.8" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="493.0" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="383.7" y1="479.8" x2="383.7" y2="511.1" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="497.0" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="387.5" y1="483.5" x2="387.5" y2="520.0" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="487.5" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="391.3" y1="474.3" x2="391.3" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="480.7" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="395.1" y1="460.8" x2="395.1" y2="503.3" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="461.5" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="398.9" y1="456.3" x2="398.9" y2="489.7" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="463.0" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="402.7" y1="459.6" x2="402.7" y2="478.0" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="467.2" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="406.4" y1="447.0" x2="406.4" y2="470.9" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="456.5" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="410.2" y1="441.2" x2="410.2" y2="476.3" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="456.5" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="414.0" y1="433.0" x2="414.0" y2="466.5" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="437.7" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="417.8" y1="421.8" x2="417.8" y2="443.4" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="423.6" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="421.6" y1="390.2" x2="421.6" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="403.8" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="425.4" y1="408.3" x2="425.4" y2="423.9" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="412.4" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="429.2" y1="385.3" x2="429.2" y2="418.9" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="393.8" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="432.9" y1="393.0" x2="432.9" y2="409.5" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="398.2" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="436.7" y1="364.6" x2="436.7" y2="406.0" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="367.0" width="2.35" height="39.0" fill="var(--up)"/>
<line x1="440.5" y1="350.5" x2="440.5" y2="369.3" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="354.2" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="444.3" y1="344.7" x2="444.3" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="352.2" width="2.35" height="57.0" fill="var(--down)"/>
<line x1="448.1" y1="397.3" x2="448.1" y2="429.6" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="409.8" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="451.9" y1="404.6" x2="451.9" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="417.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="455.7" y1="411.9" x2="455.7" y2="430.4" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="416.4" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="459.5" y1="402.0" x2="459.5" y2="436.4" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="416.1" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="463.2" y1="401.3" x2="463.2" y2="416.8" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="405.5" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="467.0" y1="390.1" x2="467.0" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="405.1" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="470.8" y1="401.7" x2="470.8" y2="421.4" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="411.8" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="474.6" y1="409.3" x2="474.6" y2="446.5" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="418.4" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="478.4" y1="440.1" x2="478.4" y2="464.4" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="447.6" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="482.2" y1="444.8" x2="482.2" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="453.2" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="486.0" y1="441.2" x2="486.0" y2="465.1" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="459.5" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="489.7" y1="445.5" x2="489.7" y2="483.9" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="454.8" width="2.35" height="28.9" fill="var(--down)"/>
<line x1="493.5" y1="475.5" x2="493.5" y2="500.3" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="487.4" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="497.3" y1="420.9" x2="497.3" y2="500.5" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="425.6" width="2.35" height="67.4" fill="var(--up)"/>
<line x1="501.1" y1="405.8" x2="501.1" y2="428.3" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="406.0" width="2.35" height="20.8" fill="var(--up)"/>
<line x1="504.9" y1="380.4" x2="504.9" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="381.0" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="508.7" y1="363.9" x2="508.7" y2="382.0" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="368.6" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="512.5" y1="351.2" x2="512.5" y2="377.6" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="356.4" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="516.2" y1="349.1" x2="516.2" y2="372.0" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="360.8" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="520.0" y1="321.7" x2="520.0" y2="367.1" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="332.1" width="2.35" height="34.8" fill="var(--up)"/>
<line x1="523.8" y1="324.9" x2="523.8" y2="346.6" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="331.7" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="527.6" y1="318.0" x2="527.6" y2="335.2" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="323.7" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="531.4" y1="323.7" x2="531.4" y2="349.8" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="325.9" width="2.35" height="20.0" fill="var(--down)"/>
<line x1="535.2" y1="325.8" x2="535.2" y2="346.6" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="329.9" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="539.0" y1="318.5" x2="539.0" y2="337.2" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="321.2" width="2.35" height="15.0" fill="var(--up)"/>
<line x1="542.7" y1="306.4" x2="542.7" y2="319.6" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="312.9" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="546.5" y1="293.7" x2="546.5" y2="315.8" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="299.8" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="550.3" y1="287.2" x2="550.3" y2="360.2" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="306.9" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="554.1" y1="326.1" x2="554.1" y2="364.4" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="326.1" width="2.35" height="27.5" fill="var(--down)"/>
<line x1="557.9" y1="324.0" x2="557.9" y2="358.7" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="327.7" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="561.7" y1="325.8" x2="561.7" y2="349.1" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="330.5" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="565.5" y1="341.0" x2="565.5" y2="357.5" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="345.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="569.3" y1="341.0" x2="569.3" y2="362.4" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="347.6" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="573.0" y1="339.8" x2="573.0" y2="361.7" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="352.8" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="576.8" y1="347.3" x2="576.8" y2="372.7" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="350.3" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="580.6" y1="329.2" x2="580.6" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="339.5" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="584.4" y1="327.6" x2="584.4" y2="366.2" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="338.7" width="2.35" height="25.1" fill="var(--down)"/>
<line x1="588.2" y1="355.3" x2="588.2" y2="381.6" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="356.7" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="592.0" y1="342.3" x2="592.0" y2="381.7" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="367.4" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="595.8" y1="350.5" x2="595.8" y2="379.7" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="350.8" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="599.5" y1="333.0" x2="599.5" y2="358.4" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="339.5" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="603.3" y1="320.9" x2="603.3" y2="359.3" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="321.3" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="607.1" y1="320.0" x2="607.1" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="325.4" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="610.9" y1="328.7" x2="610.9" y2="360.9" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="330.9" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="614.7" y1="326.5" x2="614.7" y2="351.4" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="344.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="618.5" y1="321.4" x2="618.5" y2="350.3" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="334.5" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="622.3" y1="324.0" x2="622.3" y2="342.5" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="326.0" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="626.0" y1="305.2" x2="626.0" y2="327.5" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="314.0" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="629.8" y1="299.8" x2="629.8" y2="317.4" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="301.1" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="633.6" y1="251.8" x2="633.6" y2="300.7" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="256.9" width="2.35" height="42.6" fill="var(--up)"/>
<line x1="637.4" y1="233.6" x2="637.4" y2="258.8" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="254.2" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="641.2" y1="221.8" x2="641.2" y2="259.2" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="236.5" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="645.0" y1="213.3" x2="645.0" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="233.6" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="648.8" y1="235.4" x2="648.8" y2="275.6" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="238.8" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="652.5" y1="223.0" x2="652.5" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="234.7" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="656.3" y1="213.7" x2="656.3" y2="232.9" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="217.5" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="660.1" y1="193.8" x2="660.1" y2="219.2" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="195.1" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="663.9" y1="180.5" x2="663.9" y2="206.2" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="192.0" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="667.7" y1="175.8" x2="667.7" y2="210.6" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="184.1" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="671.5" y1="169.0" x2="671.5" y2="190.2" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="176.7" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="675.3" y1="169.3" x2="675.3" y2="202.1" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="183.1" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="679.1" y1="185.2" x2="679.1" y2="203.8" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="197.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="682.8" y1="175.5" x2="682.8" y2="209.4" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="179.6" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="686.6" y1="159.7" x2="686.6" y2="191.6" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="174.7" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="690.4" y1="174.8" x2="690.4" y2="238.6" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="181.1" width="2.35" height="54.0" fill="var(--down)"/>
<line x1="694.2" y1="227.5" x2="694.2" y2="253.8" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="229.4" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="698.0" y1="205.3" x2="698.0" y2="258.7" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="213.5" width="2.35" height="33.4" fill="var(--up)"/>
<line x1="701.8" y1="190.6" x2="701.8" y2="218.5" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="212.7" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="705.6" y1="187.7" x2="705.6" y2="225.4" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="193.0" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="709.3" y1="171.1" x2="709.3" y2="192.3" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="178.7" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="713.1" y1="169.2" x2="713.1" y2="197.7" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="178.9" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="716.9" y1="183.4" x2="716.9" y2="211.0" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="193.7" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="720.7" y1="200.8" x2="720.7" y2="247.0" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="207.0" width="2.35" height="26.0" fill="var(--down)"/>
<line x1="724.5" y1="206.9" x2="724.5" y2="238.8" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="215.3" width="2.35" height="20.8" fill="var(--up)"/>
<line x1="728.3" y1="212.7" x2="728.3" y2="230.5" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="219.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="732.1" y1="216.4" x2="732.1" y2="251.7" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="216.4" width="2.35" height="32.7" fill="var(--down)"/>
<line x1="735.8" y1="205.9" x2="735.8" y2="256.4" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="215.2" width="2.35" height="38.7" fill="var(--up)"/>
<line x1="739.6" y1="187.1" x2="739.6" y2="211.0" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="194.2" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="743.4" y1="169.0" x2="743.4" y2="205.1" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="180.7" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="747.2" y1="180.3" x2="747.2" y2="200.1" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="184.7" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="751.0" y1="138.3" x2="751.0" y2="194.7" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="148.3" width="2.35" height="38.3" fill="var(--up)"/>
<line x1="754.8" y1="140.1" x2="754.8" y2="162.7" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="141.8" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="758.6" y1="154.1" x2="758.6" y2="178.2" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="158.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="762.4" y1="152.1" x2="762.4" y2="240.5" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="158.9" width="2.35" height="65.0" fill="var(--down)"/>
<line x1="766.1" y1="226.9" x2="766.1" y2="264.4" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="237.1" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="769.9" y1="219.8" x2="769.9" y2="245.4" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="222.3" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="773.7" y1="192.6" x2="773.7" y2="216.6" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="213.0" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="777.5" y1="192.2" x2="777.5" y2="305.7" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="215.7" width="2.35" height="88.6" fill="var(--down)"/>
<line x1="781.3" y1="261.1" x2="781.3" y2="347.3" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="280.2" width="2.35" height="39.4" fill="var(--up)"/>
<line x1="785.1" y1="261.3" x2="785.1" y2="289.2" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="267.7" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="788.9" y1="246.3" x2="788.9" y2="317.4" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="253.9" width="2.35" height="35.4" fill="var(--up)"/>
<line x1="792.6" y1="201.2" x2="792.6" y2="265.0" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="206.8" width="2.35" height="47.1" fill="var(--up)"/>
<line x1="796.4" y1="192.4" x2="796.4" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="204.9" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="800.2" y1="178.1" x2="800.2" y2="200.8" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="178.8" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="804.0" y1="171.6" x2="804.0" y2="206.8" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="188.1" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="807.8" y1="186.2" x2="807.8" y2="203.6" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="191.8" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="811.6" y1="179.7" x2="811.6" y2="215.1" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="184.3" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="815.4" y1="184.5" x2="815.4" y2="223.5" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="186.2" width="2.35" height="29.7" fill="var(--down)"/>
<line x1="819.1" y1="199.7" x2="819.1" y2="219.3" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="209.7" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="822.9" y1="175.3" x2="822.9" y2="209.7" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="187.2" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="826.7" y1="165.3" x2="826.7" y2="189.1" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="166.2" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="830.5" y1="159.5" x2="830.5" y2="180.1" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="164.5" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="834.3" y1="162.5" x2="834.3" y2="188.0" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="173.3" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="838.1" y1="153.1" x2="838.1" y2="192.7" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="156.7" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="841.9" y1="114.5" x2="841.9" y2="169.7" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="137.8" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="845.6" y1="101.1" x2="845.6" y2="133.9" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="118.0" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="849.4" y1="78.8" x2="849.4" y2="122.7" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="116.6" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="853.2" y1="113.1" x2="853.2" y2="131.3" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="118.3" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="857.0" y1="117.6" x2="857.0" y2="136.7" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="118.9" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="860.8" y1="139.9" x2="860.8" y2="161.0" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="141.4" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="864.6" y1="126.3" x2="864.6" y2="157.0" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="140.3" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="868.4" y1="133.8" x2="868.4" y2="214.0" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="137.8" width="2.35" height="68.1" fill="var(--down)"/>
<line x1="872.2" y1="193.5" x2="872.2" y2="249.7" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="203.8" width="2.35" height="37.4" fill="var(--down)"/>
<line x1="875.9" y1="229.2" x2="875.9" y2="263.1" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="232.7" width="2.35" height="21.5" fill="var(--down)"/>
<line x1="879.7" y1="228.4" x2="879.7" y2="264.0" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="243.1" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="883.5" y1="233.9" x2="883.5" y2="271.6" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="243.4" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="887.3" y1="232.3" x2="887.3" y2="266.5" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="237.2" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="891.1" y1="218.1" x2="891.1" y2="269.8" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="232.6" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="894.9" y1="217.9" x2="894.9" y2="247.2" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="224.9" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="898.7" y1="207.4" x2="898.7" y2="240.5" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="229.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="902.4" y1="221.5" x2="902.4" y2="242.8" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="229.8" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="906.2" y1="218.2" x2="906.2" y2="238.3" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="220.6" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="910.0" y1="214.8" x2="910.0" y2="234.8" stroke="var(--up)" class="wick"/>
<rect x="908.84" y="221.1" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="913.8" y1="211.6" x2="913.8" y2="244.6" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="216.7" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="917.6" y1="190.5" x2="917.6" y2="227.4" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="196.2" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="921.4" y1="166.1" x2="921.4" y2="201.0" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="166.5" width="2.35" height="34.0" fill="var(--up)"/>
<line x1="925.2" y1="161.1" x2="925.2" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="165.3" width="2.35" height="30.8" fill="var(--down)"/>
<line x1="928.9" y1="134.8" x2="928.9" y2="198.2" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="144.4" width="2.35" height="53.0" fill="var(--up)"/>
<line x1="932.7" y1="126.1" x2="932.7" y2="154.3" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="136.6" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="936.5" y1="138.9" x2="936.5" y2="186.1" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="150.7" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="940.3" y1="149.9" x2="940.3" y2="181.1" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="160.2" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="944.1" y1="162.9" x2="944.1" y2="330.7" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="169.4" width="2.35" height="156.5" fill="var(--down)"/>
<line x1="947.9" y1="314.6" x2="947.9" y2="427.8" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="328.2" width="2.35" height="50.3" fill="var(--down)"/>
<line x1="951.7" y1="355.4" x2="951.7" y2="379.4" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="364.4" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="955.5" y1="318.4" x2="955.5" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="321.3" width="2.35" height="50.2" fill="var(--up)"/>
<line x1="959.2" y1="302.2" x2="959.2" y2="337.0" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="302.8" width="2.35" height="34.2" fill="var(--up)"/>
<line x1="963.0" y1="307.6" x2="963.0" y2="367.2" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="309.4" width="2.35" height="46.1" fill="var(--down)"/>
<line x1="966.8" y1="331.7" x2="966.8" y2="361.7" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="351.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="970.6" y1="335.9" x2="970.6" y2="389.4" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="343.2" width="2.35" height="41.1" fill="var(--down)"/>
<line x1="974.4" y1="336.0" x2="974.4" y2="379.5" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="340.2" width="2.35" height="35.8" fill="var(--up)"/>
<line x1="978.2" y1="321.1" x2="978.2" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="342.9" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="982.0" y1="315.3" x2="982.0" y2="367.0" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="320.1" width="2.35" height="45.6" fill="var(--up)"/>
<line x1="985.7" y1="295.1" x2="985.7" y2="337.0" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="320.4" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="989.5" y1="299.9" x2="989.5" y2="352.6" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="330.4" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="993.3" y1="336.8" x2="993.3" y2="366.7" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="352.4" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="997.1" y1="342.1" x2="997.1" y2="393.6" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="363.6" width="2.35" height="26.2" fill="var(--down)"/>
<line x1="1000.9" y1="355.5" x2="1000.9" y2="389.7" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="364.2" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="1004.7" y1="345.0" x2="1004.7" y2="380.0" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="352.9" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="1008.5" y1="340.7" x2="1008.5" y2="382.4" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="349.8" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="1012.2" y1="341.8" x2="1012.2" y2="378.8" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="357.2" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="1016.0" y1="331.0" x2="1016.0" y2="381.2" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="363.0" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="1019.8" y1="367.0" x2="1019.8" y2="407.7" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="380.9" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="1023.6" y1="280.2" x2="1023.6" y2="390.7" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="280.5" width="2.35" height="92.8" fill="var(--up)"/>
<line x1="1027.4" y1="261.0" x2="1027.4" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="281.1" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="1031.2" y1="239.1" x2="1031.2" y2="306.9" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="260.0" width="2.35" height="32.5" fill="var(--up)"/>
<line x1="1035.0" y1="255.8" x2="1035.0" y2="320.1" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="256.1" width="2.35" height="49.6" fill="var(--down)"/>
<line x1="1038.7" y1="274.7" x2="1038.7" y2="346.5" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="293.3" width="2.35" height="39.4" fill="var(--down)"/>
<line x1="1042.5" y1="313.9" x2="1042.5" y2="348.6" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="326.6" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="1046.3" y1="309.5" x2="1046.3" y2="346.7" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="319.9" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="1050.1" y1="311.6" x2="1050.1" y2="328.4" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="313.9" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="60" y1="291.1" x2="1052" y2="291.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="294.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$434 R1</text>
<text x="1058" y="306.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="248.7" x2="1052" y2="248.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="252.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$457 R2</text>
<text x="1058" y="264.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="166.8" x2="1052" y2="166.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="170.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$501 R3</text>
<text x="1058" y="182.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="371.7" x2="1052" y2="371.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="365.7" font-size="11.5" fill="var(--support)" font-weight="600">$391 S1</text>
<text x="1058" y="377.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="400.6" x2="1052" y2="400.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="394.6" font-size="11.5" fill="var(--support)" font-weight="600">$376 S2</text>
<text x="1058" y="406.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="528.3" x2="1052" y2="528.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="522.3" font-size="11.5" fill="var(--support)" font-weight="600">$307 S3</text>
<text x="1058" y="534.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="319.9" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $501 | 3 | 2025년 2월 고점과 2026년 1월 고점(FY2026 최초 가이던스 발표 직전)이 겹쳐 형성된 클러스터 |
| R2 | $457 | 3 | 2024년 하반기~2025년 중반 사이 반복적으로 형성된 상단 레인지 |
| R1 | $434 | 2 | 2024년 초 반등 국면의 고점대 |
| **현재가** | **$418.80** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $391 | 3 | 2023년 말~2024년 초 저점대, 2026년 조정 국면과도 겹침 |
| S2 | $376 | 2 | 2023년 상반기 저점대 |
| S3 | $307 | 2 | 2022년 금리인상기 약세장 저점대(2022년 10월 저가 $271.16 부근의 스윙 클러스터) |

> 5년 구간 최고가 $547.82(2025년 8월 부근 주봉 기준)·최저가 $264.26(2022년 하반기)로, 상단·하단 레벨이 일봉(기술적 분석 — 일봉·1년, 1년)보다 훨씬 넓은 범위를 커버한다 — 2022년 금리인상 사이클의 약세장까지 포함하기 때문.

---

## 3. 관측된 특이 구간

다년 관점에서 가장 뚜렷한 두 구간은 (1) 2022년 금리인상기 약세장, (2) 2025년 8월 고점 이후 2026년의 두 차례 가이던스 실망발 조정이다. 후자의 개별 갭다운 상세(일자별 등락률·거래량)는 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 3. 관측된 특이 구간을 참고하고, 여기서는 주봉 관점의 큰 그림만 기록한다.

- **2022년 약세장**: 2021년 말 주봉 종가 약 $448에서 2022년 10월 저점 $271.16(주봉 기준)까지 약 −39% 하락 — 연준 금리인상 사이클에 따른 성장주·고밸류에이션주 전반의 재평가 국면으로, S&P Global 고유 이슈라기보다 거시 환경 변화의 결과에 가깝다.
- **2025년 8월 고점 → 2026년 조정**: 2025년 8월 주봉 고점(약 $527, 장중 최고 $579.05) 이후 2026년 2월 4분기 실적발표(가이던스 실망)로 급락해 3월 저점 $384 부근까지 조정, 이후 7월 초 Mobility 분사를 계기로 반등했으나 7월 말 2차 가이던스 하향으로 다시 밀려 현재 $418.80 수준 — 고점 대비 약 −28%. 두 조정 모두 실적/가이던스 발표가 직접 계기였다는 공통점이 있다(기술적 분석 — 일봉·1년 3. 관측된 특이 구간 참고).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-16~2026-08-14. 수집 시점: 2026-08-17. 원주가(배당 미반영), 2026-07-01 "분할" 메타데이터는 실제 분할이 아니므로 소급조정하지 않았다(위 상단 ⚠️ 참고).
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py SPGI --name "S&P Global" --interval 1wk --close-on 2026-08-14`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다(기본값 그대로 사용, 조정 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 5년 구간 안에 2022년 약세장·2025~2026년 실적발 조정 등 서로 다른 성격의 국면이 섞여 있어, 오래된 레벨(S3 등 2022년 저점대)일수록 지금 시장 구조·밸류에이션 수준과의 관련성이 낮을 수 있다.
    - 2026-07-01 Mobility 분사는 실제 주식분할이 아니므로 소급조정하지 않았다(위 상단 ⚠️ 참고).

---

*작성일: 2026-08-17 (최종 수정일: 2026-08-23)*
