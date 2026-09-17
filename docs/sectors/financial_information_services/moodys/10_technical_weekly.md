# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-11 종가 **$474.95**는 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 및 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치**한다.
- **주의**: 5년 구간 내 주식분할·분사가 없어 소급조정 없이 원주가 그대로다.
:::

---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-11)

<style>
.mco-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .mco-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.mco-chart svg { width:100%; height:auto; display:block; }
.mco-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.mco-chart .title { fill: var(--ink); font-weight:600; }
.mco-chart .grid { stroke: var(--grid); stroke-width:1; }
.mco-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="mco-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Moody's(MCO) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Moody's (MCO) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-11 · 마지막 종가 $474.95 (2026-09-11) · 단위 USD</text>
<line x1="60" y1="575.7" x2="1052" y2="575.7" class="grid"/>
<text x="52" y="579.7" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="491.9" x2="1052" y2="491.9" class="grid"/>
<text x="52" y="495.9" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="408.1" x2="1052" y2="408.1" class="grid"/>
<text x="52" y="412.1" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="324.2" x2="1052" y2="324.2" class="grid"/>
<text x="52" y="328.2" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="240.4" x2="1052" y2="240.4" class="grid"/>
<text x="52" y="244.4" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="156.6" x2="1052" y2="156.6" class="grid"/>
<text x="52" y="160.6" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="72.8" x2="1052" y2="72.8" class="grid"/>
<text x="52" y="76.8" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="122.5" y1="56.0" x2="122.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="122.5" y1="626.0" x2="122.5" y2="631.0" class="axis"/>
<text x="122.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="319.4" y1="56.0" x2="319.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="319.4" y1="626.0" x2="319.4" y2="631.0" class="axis"/>
<text x="319.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="516.2" y1="56.0" x2="516.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="516.2" y1="626.0" x2="516.2" y2="631.0" class="axis"/>
<text x="516.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.9" y1="56.0" x2="716.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.9" y1="626.0" x2="716.9" y2="631.0" class="axis"/>
<text x="716.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.8" y1="56.0" x2="913.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.8" y1="626.0" x2="913.8" y2="631.0" class="axis"/>
<text x="913.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="346.0" x2="61.9" y2="376.6" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="348.9" width="2.35" height="25.6" fill="var(--down)"/>
<line x1="65.7" y1="360.1" x2="65.7" y2="382.3" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="364.0" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="69.5" y1="366.9" x2="69.5" y2="403.0" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="366.9" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="73.3" y1="379.4" x2="73.3" y2="413.3" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="387.5" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="77.0" y1="369.3" x2="77.0" y2="394.0" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="372.6" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="80.8" y1="353.6" x2="80.8" y2="378.7" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="355.0" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="84.6" y1="311.3" x2="84.6" y2="358.5" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="317.3" width="2.35" height="37.7" fill="var(--up)"/>
<line x1="88.4" y1="310.9" x2="88.4" y2="353.7" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="312.8" width="2.35" height="33.0" fill="var(--down)"/>
<line x1="92.2" y1="334.3" x2="92.2" y2="354.0" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="344.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="96.0" y1="318.3" x2="96.0" y2="346.9" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="344.1" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="99.8" y1="335.6" x2="99.8" y2="360.4" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="346.4" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="103.5" y1="324.7" x2="103.5" y2="358.5" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="341.2" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="107.3" y1="323.2" x2="107.3" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="328.0" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="111.1" y1="323.0" x2="111.1" y2="344.7" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="327.5" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="114.9" y1="324.5" x2="114.9" y2="353.4" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="328.8" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="118.7" y1="318.0" x2="118.7" y2="343.4" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="326.0" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="122.5" y1="336.8" x2="122.5" y2="377.4" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="338.1" width="2.35" height="32.4" fill="var(--down)"/>
<line x1="126.3" y1="363.7" x2="126.3" y2="410.9" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="377.2" width="2.35" height="24.9" fill="var(--down)"/>
<line x1="130.0" y1="400.2" x2="130.0" y2="423.2" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="411.8" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="133.8" y1="417.2" x2="133.8" y2="454.9" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="430.7" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="137.6" y1="406.4" x2="137.6" y2="435.6" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="413.3" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="141.4" y1="400.0" x2="141.4" y2="441.9" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="414.3" width="2.35" height="23.5" fill="var(--down)"/>
<line x1="145.2" y1="437.2" x2="145.2" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="440.1" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="149.0" y1="442.7" x2="149.0" y2="474.7" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="452.1" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="152.8" y1="442.6" x2="152.8" y2="460.7" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="448.6" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="156.5" y1="444.6" x2="156.5" y2="488.5" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="448.6" width="2.35" height="35.8" fill="var(--down)"/>
<line x1="160.3" y1="438.5" x2="160.3" y2="492.4" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="439.5" width="2.35" height="42.1" fill="var(--up)"/>
<line x1="164.1" y1="437.6" x2="164.1" y2="453.5" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="440.7" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="167.9" y1="416.1" x2="167.9" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="424.3" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="171.7" y1="414.4" x2="171.7" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="420.3" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="175.5" y1="424.3" x2="175.5" y2="447.7" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="425.4" width="2.35" height="18.8" fill="var(--down)"/>
<line x1="179.3" y1="426.0" x2="179.3" y2="454.9" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="445.8" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="183.1" y1="444.5" x2="183.1" y2="465.8" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="458.4" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="186.8" y1="460.7" x2="186.8" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="491.1" width="2.35" height="20.8" fill="var(--up)"/>
<line x1="190.6" y1="495.6" x2="190.6" y2="530.8" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="498.7" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="194.4" y1="501.9" x2="194.4" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="509.9" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="198.2" y1="479.2" x2="198.2" y2="511.3" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="479.3" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="202.0" y1="481.5" x2="202.0" y2="543.1" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="483.3" width="2.35" height="33.3" fill="var(--down)"/>
<line x1="205.8" y1="508.5" x2="205.8" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="514.2" width="2.35" height="22.6" fill="var(--down)"/>
<line x1="209.6" y1="542.5" x2="209.6" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="545.9" width="2.35" height="20.0" fill="var(--down)"/>
<line x1="213.3" y1="529.1" x2="213.3" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="529.6" width="2.35" height="28.7" fill="var(--up)"/>
<line x1="217.1" y1="526.0" x2="217.1" y2="545.4" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="528.5" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="220.9" y1="514.2" x2="220.9" y2="540.5" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="518.5" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="224.7" y1="515.6" x2="224.7" y2="542.8" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="518.7" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="228.5" y1="494.4" x2="228.5" y2="525.7" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="499.5" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="232.3" y1="472.6" x2="232.3" y2="520.2" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="474.7" width="2.35" height="26.1" fill="var(--up)"/>
<line x1="236.1" y1="467.5" x2="236.1" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="473.3" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="239.8" y1="450.6" x2="239.8" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="453.4" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="243.6" y1="449.5" x2="243.6" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="242.46" y="454.6" width="2.35" height="19.0" fill="var(--down)"/>
<line x1="247.4" y1="478.3" x2="247.4" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="480.2" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="251.2" y1="502.3" x2="251.2" y2="526.3" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="506.5" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="255.0" y1="491.0" x2="255.0" y2="519.2" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="492.7" width="2.35" height="23.7" fill="var(--up)"/>
<line x1="258.8" y1="485.6" x2="258.8" y2="530.7" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="488.4" width="2.35" height="36.6" fill="var(--down)"/>
<line x1="262.6" y1="525.9" x2="262.6" y2="575.4" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="528.6" width="2.35" height="39.2" fill="var(--down)"/>
<line x1="266.4" y1="567.6" x2="266.4" y2="587.9" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="568.0" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="270.1" y1="552.0" x2="270.1" y2="588.1" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="583.3" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="273.9" y1="579.9" x2="273.9" y2="609.0" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="580.2" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="277.7" y1="573.8" x2="277.7" y2="603.8" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="589.1" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="281.5" y1="542.2" x2="281.5" y2="592.9" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="543.7" width="2.35" height="42.4" fill="var(--up)"/>
<line x1="285.3" y1="540.9" x2="285.3" y2="572.4" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="547.6" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="289.1" y1="470.3" x2="289.1" y2="558.7" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="474.5" width="2.35" height="79.8" fill="var(--up)"/>
<line x1="292.9" y1="479.1" x2="292.9" y2="516.2" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="481.3" width="2.35" height="23.5" fill="var(--down)"/>
<line x1="296.6" y1="488.0" x2="296.6" y2="511.0" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="490.2" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="300.4" y1="477.0" x2="300.4" y2="518.0" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="489.0" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="304.2" y1="494.5" x2="304.2" y2="512.9" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="496.3" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="308.0" y1="474.0" x2="308.0" y2="526.8" stroke="var(--down)" class="wick"/>
<rect x="306.83" y="510.8" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="311.8" y1="521.2" x2="311.8" y2="534.1" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="525.8" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="315.6" y1="520.2" x2="315.6" y2="537.6" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="527.7" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="319.4" y1="509.0" x2="319.4" y2="534.1" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="509.1" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="323.1" y1="466.7" x2="323.1" y2="508.9" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="467.5" width="2.35" height="37.3" fill="var(--up)"/>
<line x1="326.9" y1="454.3" x2="326.9" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="457.6" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="330.7" y1="450.7" x2="330.7" y2="479.1" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="459.1" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="334.5" y1="431.7" x2="334.5" y2="469.4" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="451.0" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="338.3" y1="458.1" x2="338.3" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="459.2" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="342.1" y1="467.5" x2="342.1" y2="495.7" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="478.7" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="345.9" y1="495.0" x2="345.9" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="496.9" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="349.6" y1="492.9" x2="349.6" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="494.2" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="353.4" y1="484.8" x2="353.4" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="494.0" width="2.35" height="22.9" fill="var(--down)"/>
<line x1="357.2" y1="491.3" x2="357.2" y2="528.4" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="501.5" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="361.0" y1="490.9" x2="361.0" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="499.7" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="364.8" y1="481.5" x2="364.8" y2="506.0" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="481.8" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="368.6" y1="474.6" x2="368.6" y2="498.3" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="484.9" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="372.4" y1="481.7" x2="372.4" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="488.0" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="376.2" y1="482.4" x2="376.2" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="485.9" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="379.9" y1="464.1" x2="379.9" y2="490.8" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="469.9" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="383.7" y1="466.8" x2="383.7" y2="497.8" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="471.4" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="387.5" y1="472.8" x2="387.5" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="475.6" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="391.3" y1="461.8" x2="391.3" y2="480.6" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="466.7" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="395.1" y1="454.6" x2="395.1" y2="478.0" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="466.9" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="398.9" y1="442.1" x2="398.9" y2="473.7" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="446.6" width="2.35" height="19.7" fill="var(--up)"/>
<line x1="402.7" y1="427.7" x2="402.7" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="432.4" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="406.4" y1="406.3" x2="406.4" y2="436.6" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="421.7" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="410.2" y1="422.5" x2="410.2" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="427.6" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="414.0" y1="406.4" x2="414.0" y2="434.6" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="411.9" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="417.8" y1="412.6" x2="417.8" y2="427.2" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="415.1" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="421.6" y1="401.8" x2="421.6" y2="428.1" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="402.8" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="425.4" y1="389.0" x2="425.4" y2="404.8" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="395.0" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="429.2" y1="385.9" x2="429.2" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="396.0" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="432.9" y1="399.8" x2="432.9" y2="431.1" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="400.1" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="436.7" y1="420.7" x2="436.7" y2="435.4" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="421.3" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="440.5" y1="425.7" x2="440.5" y2="453.3" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="430.2" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="444.3" y1="427.1" x2="444.3" y2="453.1" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="434.2" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="448.1" y1="419.7" x2="448.1" y2="434.9" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="426.0" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="451.9" y1="419.6" x2="451.9" y2="432.0" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="425.2" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="455.7" y1="407.3" x2="455.7" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="422.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="459.5" y1="416.5" x2="459.5" y2="451.9" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="424.0" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="463.2" y1="450.6" x2="463.2" y2="470.2" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="453.0" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="467.0" y1="459.2" x2="467.0" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="463.2" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="470.8" y1="446.0" x2="470.8" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="462.7" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="474.6" y1="449.8" x2="474.6" y2="478.8" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="457.8" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="478.4" y1="450.0" x2="478.4" y2="490.2" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="479.8" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="482.2" y1="431.3" x2="482.2" y2="493.8" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="439.2" width="2.35" height="44.7" fill="var(--up)"/>
<line x1="486.0" y1="416.4" x2="486.0" y2="442.1" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="417.2" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="489.7" y1="395.2" x2="489.7" y2="421.2" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="396.9" width="2.35" height="23.4" fill="var(--up)"/>
<line x1="493.5" y1="376.8" x2="493.5" y2="398.4" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="387.3" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="497.3" y1="372.5" x2="497.3" y2="393.8" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="372.8" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="501.1" y1="360.6" x2="501.1" y2="377.0" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="366.8" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="504.9" y1="329.4" x2="504.9" y2="371.2" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="342.6" width="2.35" height="24.4" fill="var(--up)"/>
<line x1="508.7" y1="334.8" x2="508.7" y2="356.2" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="341.4" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="512.5" y1="335.2" x2="512.5" y2="348.3" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="340.1" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="516.2" y1="343.4" x2="516.2" y2="373.9" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="347.7" width="2.35" height="24.0" fill="var(--down)"/>
<line x1="520.0" y1="357.8" x2="520.0" y2="372.8" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="358.1" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="523.8" y1="344.1" x2="523.8" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="522.64" y="346.3" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="527.6" y1="336.3" x2="527.6" y2="348.9" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="342.2" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="531.4" y1="318.9" x2="531.4" y2="348.3" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="324.9" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="535.2" y1="313.7" x2="535.2" y2="335.7" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="315.6" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="539.0" y1="311.5" x2="539.0" y2="385.4" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="311.5" width="2.35" height="61.8" fill="var(--down)"/>
<line x1="542.7" y1="346.8" x2="542.7" y2="377.5" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="348.5" width="2.35" height="26.9" fill="var(--up)"/>
<line x1="546.5" y1="346.0" x2="546.5" y2="364.9" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="347.9" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="550.3" y1="333.5" x2="550.3" y2="361.8" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="346.0" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="554.1" y1="337.7" x2="554.1" y2="359.9" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="347.8" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="557.9" y1="327.6" x2="557.9" y2="351.7" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="345.0" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="561.7" y1="330.9" x2="561.7" y2="349.4" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="335.9" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="565.5" y1="320.2" x2="565.5" y2="344.7" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="334.3" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="569.3" y1="322.5" x2="569.3" y2="364.7" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="335.2" width="2.35" height="27.3" fill="var(--down)"/>
<line x1="573.0" y1="350.0" x2="573.0" y2="375.5" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="354.5" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="576.8" y1="351.6" x2="576.8" y2="371.2" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="363.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="580.6" y1="352.8" x2="580.6" y2="391.2" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="356.8" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="584.4" y1="317.5" x2="584.4" y2="354.6" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="323.6" width="2.35" height="29.9" fill="var(--up)"/>
<line x1="588.2" y1="299.9" x2="588.2" y2="333.2" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="300.9" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="592.0" y1="294.5" x2="592.0" y2="313.6" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="303.9" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="595.8" y1="307.7" x2="595.8" y2="334.8" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="307.9" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="599.5" y1="305.0" x2="599.5" y2="331.8" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="318.0" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="603.3" y1="296.7" x2="603.3" y2="326.1" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="310.6" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="607.1" y1="284.0" x2="607.1" y2="312.8" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="287.5" width="2.35" height="24.2" fill="var(--up)"/>
<line x1="610.9" y1="276.0" x2="610.9" y2="296.9" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="285.6" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="614.7" y1="269.3" x2="614.7" y2="293.9" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="270.2" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="618.5" y1="238.4" x2="618.5" y2="272.8" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="247.2" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="622.3" y1="226.6" x2="622.3" y2="254.6" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="243.2" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="626.0" y1="227.6" x2="626.0" y2="272.2" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="242.5" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="629.8" y1="219.2" x2="629.8" y2="246.7" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="222.7" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="633.6" y1="214.8" x2="633.6" y2="258.5" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="215.4" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="637.4" y1="207.3" x2="637.4" y2="224.4" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="212.4" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="641.2" y1="184.1" x2="641.2" y2="211.2" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="191.2" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="645.0" y1="175.6" x2="645.0" y2="195.4" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="177.1" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="648.8" y1="173.1" x2="648.8" y2="200.3" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="175.5" width="2.35" height="22.3" fill="var(--down)"/>
<line x1="652.5" y1="178.3" x2="652.5" y2="210.9" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="191.6" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="656.3" y1="164.8" x2="656.3" y2="192.5" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="165.5" width="2.35" height="26.4" fill="var(--up)"/>
<line x1="660.1" y1="166.6" x2="660.1" y2="204.8" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="174.6" width="2.35" height="26.4" fill="var(--down)"/>
<line x1="663.9" y1="195.3" x2="663.9" y2="225.5" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="201.4" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="667.7" y1="198.0" x2="667.7" y2="229.3" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="198.3" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="671.5" y1="166.3" x2="671.5" y2="198.9" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="175.9" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="675.3" y1="174.8" x2="675.3" y2="221.6" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="179.0" width="2.35" height="40.0" fill="var(--down)"/>
<line x1="679.1" y1="210.2" x2="679.1" y2="233.8" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="211.8" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="682.8" y1="191.2" x2="682.8" y2="239.7" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="194.8" width="2.35" height="35.6" fill="var(--up)"/>
<line x1="686.6" y1="177.6" x2="686.6" y2="202.9" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="192.1" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="690.4" y1="184.7" x2="690.4" y2="217.7" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="189.0" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="694.2" y1="150.0" x2="694.2" y2="184.5" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="156.6" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="698.0" y1="156.2" x2="698.0" y2="174.3" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="157.4" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="701.8" y1="155.1" x2="701.8" y2="180.4" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="171.2" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="705.6" y1="168.8" x2="705.6" y2="227.8" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="173.0" width="2.35" height="40.1" fill="var(--down)"/>
<line x1="709.3" y1="186.7" x2="709.3" y2="216.2" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="195.5" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="713.1" y1="189.8" x2="713.1" y2="208.1" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="191.5" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="716.9" y1="190.4" x2="716.9" y2="241.3" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="192.3" width="2.35" height="43.4" fill="var(--down)"/>
<line x1="720.7" y1="186.7" x2="720.7" y2="239.6" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="197.1" width="2.35" height="42.4" fill="var(--up)"/>
<line x1="724.5" y1="171.1" x2="724.5" y2="194.1" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="173.9" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="728.3" y1="146.9" x2="728.3" y2="190.5" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="157.5" width="2.35" height="20.3" fill="var(--up)"/>
<line x1="732.1" y1="146.1" x2="732.1" y2="178.3" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="151.1" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="735.8" y1="103.1" x2="735.8" y2="160.3" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="118.3" width="2.35" height="29.2" fill="var(--up)"/>
<line x1="739.6" y1="119.3" x2="739.6" y2="158.2" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="119.4" width="2.35" height="36.7" fill="var(--down)"/>
<line x1="743.4" y1="144.2" x2="743.4" y2="169.5" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="149.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="747.2" y1="144.3" x2="747.2" y2="234.8" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="148.2" width="2.35" height="72.9" fill="var(--down)"/>
<line x1="751.0" y1="226.1" x2="751.0" y2="264.8" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="233.3" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="754.8" y1="219.8" x2="754.8" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="224.5" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="758.6" y1="188.7" x2="758.6" y2="223.3" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="213.2" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="762.4" y1="203.7" x2="762.4" y2="323.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="226.0" width="2.35" height="94.1" fill="var(--down)"/>
<line x1="766.1" y1="256.9" x2="766.1" y2="359.9" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="276.6" width="2.35" height="61.6" fill="var(--up)"/>
<line x1="769.9" y1="255.0" x2="769.9" y2="290.2" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="262.2" width="2.35" height="20.3" fill="var(--down)"/>
<line x1="773.7" y1="242.1" x2="773.7" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="259.5" width="2.35" height="32.9" fill="var(--up)"/>
<line x1="777.5" y1="212.4" x2="777.5" y2="266.1" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="215.7" width="2.35" height="41.6" fill="var(--up)"/>
<line x1="781.3" y1="191.8" x2="781.3" y2="225.3" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="205.8" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="785.1" y1="171.8" x2="785.1" y2="193.8" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="175.2" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="788.9" y1="167.8" x2="788.9" y2="212.2" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="183.4" width="2.35" height="24.0" fill="var(--down)"/>
<line x1="792.6" y1="185.0" x2="792.6" y2="200.5" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="191.3" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="796.4" y1="167.4" x2="796.4" y2="207.6" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="175.1" width="2.35" height="22.3" fill="var(--up)"/>
<line x1="800.2" y1="173.6" x2="800.2" y2="206.0" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="175.6" width="2.35" height="28.1" fill="var(--down)"/>
<line x1="804.0" y1="188.9" x2="804.0" y2="210.7" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="195.7" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="807.8" y1="169.1" x2="807.8" y2="210.4" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="176.7" width="2.35" height="29.3" fill="var(--up)"/>
<line x1="811.6" y1="148.1" x2="811.6" y2="179.2" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="148.1" width="2.35" height="27.1" fill="var(--up)"/>
<line x1="815.4" y1="142.2" x2="815.4" y2="160.3" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="149.5" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="819.1" y1="148.8" x2="819.1" y2="171.0" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="156.8" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="822.9" y1="125.6" x2="822.9" y2="189.1" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="134.9" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="826.7" y1="121.4" x2="826.7" y2="163.0" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="137.6" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="830.5" y1="117.7" x2="830.5" y2="153.2" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="131.0" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="834.3" y1="117.9" x2="834.3" y2="138.3" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="129.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="838.1" y1="125.3" x2="838.1" y2="142.1" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="129.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="841.9" y1="127.5" x2="841.9" y2="146.8" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="129.6" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="845.6" y1="150.3" x2="845.6" y2="168.4" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="151.0" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="849.4" y1="123.8" x2="849.4" y2="160.2" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="136.0" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="853.2" y1="127.9" x2="853.2" y2="197.3" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="135.4" width="2.35" height="53.5" fill="var(--down)"/>
<line x1="857.0" y1="172.6" x2="857.0" y2="208.6" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="185.1" width="2.35" height="10.5" fill="var(--down)"/>
<line x1="860.8" y1="176.5" x2="860.8" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="181.7" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="864.6" y1="161.7" x2="864.6" y2="184.5" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="180.3" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="868.4" y1="176.9" x2="868.4" y2="213.3" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="179.7" width="2.35" height="25.4" fill="var(--down)"/>
<line x1="872.2" y1="170.4" x2="872.2" y2="208.8" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="172.0" width="2.35" height="30.5" fill="var(--up)"/>
<line x1="875.9" y1="161.1" x2="875.9" y2="208.4" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="165.0" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="879.7" y1="174.5" x2="879.7" y2="200.1" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="176.7" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="883.5" y1="158.3" x2="883.5" y2="192.5" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="178.3" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="887.3" y1="184.4" x2="887.3" y2="212.9" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="190.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="891.1" y1="167.1" x2="891.1" y2="195.7" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="172.0" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="894.9" y1="159.9" x2="894.9" y2="180.6" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="162.5" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="898.7" y1="165.6" x2="898.7" y2="201.1" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="166.5" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="902.4" y1="147.3" x2="902.4" y2="179.8" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="151.4" width="2.35" height="21.9" fill="var(--up)"/>
<line x1="906.2" y1="121.6" x2="906.2" y2="156.6" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="123.0" width="2.35" height="31.0" fill="var(--up)"/>
<line x1="910.0" y1="119.1" x2="910.0" y2="162.3" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="122.0" width="2.35" height="36.3" fill="var(--down)"/>
<line x1="913.8" y1="89.5" x2="913.8" y2="156.6" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="103.6" width="2.35" height="48.8" fill="var(--up)"/>
<line x1="917.6" y1="78.0" x2="917.6" y2="112.2" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="91.3" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="921.4" y1="98.6" x2="921.4" y2="132.6" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="108.2" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="925.2" y1="108.4" x2="925.2" y2="140.6" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="115.4" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="928.9" y1="120.9" x2="928.9" y2="252.6" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="129.5" width="2.35" height="106.7" fill="var(--down)"/>
<line x1="932.7" y1="229.8" x2="932.7" y2="320.4" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="237.0" width="2.35" height="42.9" fill="var(--down)"/>
<line x1="936.5" y1="235.0" x2="936.5" y2="289.4" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="244.1" width="2.35" height="29.5" fill="var(--up)"/>
<line x1="940.3" y1="183.5" x2="940.3" y2="263.4" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="194.2" width="2.35" height="54.5" fill="var(--up)"/>
<line x1="944.1" y1="194.6" x2="944.1" y2="233.0" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="203.6" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="947.9" y1="211.7" x2="947.9" y2="287.1" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="216.2" width="2.35" height="57.7" fill="var(--down)"/>
<line x1="951.7" y1="246.8" x2="951.7" y2="271.3" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="265.4" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="955.5" y1="246.4" x2="955.5" y2="287.0" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="251.7" width="2.35" height="30.8" fill="var(--down)"/>
<line x1="959.2" y1="247.6" x2="959.2" y2="280.7" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="255.9" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="963.0" y1="232.2" x2="963.0" y2="283.3" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="258.6" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="966.8" y1="224.9" x2="966.8" y2="281.9" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="231.4" width="2.35" height="50.4" fill="var(--up)"/>
<line x1="970.6" y1="185.9" x2="970.6" y2="243.7" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="230.3" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="974.4" y1="205.8" x2="974.4" y2="235.8" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="230.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="978.2" y1="222.3" x2="978.2" y2="253.5" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="233.8" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="982.0" y1="225.9" x2="982.0" y2="280.3" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="243.5" width="2.35" height="32.3" fill="var(--down)"/>
<line x1="985.7" y1="235.6" x2="985.7" y2="279.0" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="241.9" width="2.35" height="37.1" fill="var(--up)"/>
<line x1="989.5" y1="224.9" x2="989.5" y2="246.4" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="235.0" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="993.3" y1="214.1" x2="993.3" y2="254.2" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="234.3" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="997.1" y1="233.5" x2="997.1" y2="260.2" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="238.5" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="1000.9" y1="202.8" x2="1000.9" y2="242.3" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="239.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1004.7" y1="224.0" x2="1004.7" y2="261.4" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="240.4" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="1008.5" y1="172.1" x2="1008.5" y2="245.2" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="172.5" width="2.35" height="63.8" fill="var(--up)"/>
<line x1="1012.2" y1="148.4" x2="1012.2" y2="193.0" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="169.4" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="1016.0" y1="117.5" x2="1016.0" y2="190.1" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="138.4" width="2.35" height="32.1" fill="var(--up)"/>
<line x1="1019.8" y1="139.8" x2="1019.8" y2="209.6" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="142.8" width="2.35" height="61.6" fill="var(--down)"/>
<line x1="1023.6" y1="171.3" x2="1023.6" y2="206.1" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="191.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1027.4" y1="171.5" x2="1027.4" y2="206.0" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="183.2" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="1031.2" y1="173.9" x2="1031.2" y2="201.4" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="181.8" width="2.35" height="16.8" fill="var(--up)"/>
<line x1="1035.0" y1="145.6" x2="1035.0" y2="194.9" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="151.0" width="2.35" height="37.1" fill="var(--up)"/>
<line x1="1038.7" y1="121.9" x2="1038.7" y2="154.9" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="131.5" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="1042.5" y1="136.6" x2="1042.5" y2="182.7" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="137.6" width="2.35" height="29.8" fill="var(--down)"/>
<line x1="1046.3" y1="173.8" x2="1046.3" y2="212.9" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="173.9" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="1050.1" y1="197.7" x2="1050.1" y2="211.3" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="198.6" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="60" y1="157.7" x2="1052" y2="157.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="161.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$499 R1</text>
<text x="1058" y="173.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="112.8" x2="1052" y2="112.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="116.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$526 R2</text>
<text x="1058" y="128.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="213.1" x2="1052" y2="213.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="207.1" font-size="11.5" fill="var(--support)" font-weight="600">$466 S1</text>
<text x="1058" y="219.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="240.5" x2="1052" y2="240.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="234.5" font-size="11.5" fill="var(--support)" font-weight="600">$450 S2</text>
<text x="1058" y="246.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="360.2" x2="1052" y2="360.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="354.2" font-size="11.5" fill="var(--support)" font-weight="600">$379 S3</text>
<text x="1058" y="366.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="198.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="190.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $475 (2026-09-11)</text>
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
| R2 | $526 | 3 | 2025-02-10·2025-08-04·2026-07-13 — 2025년 내내 반복 시험된 상단대가 2026년 7월 반등에서도 저항으로 작동했다 |
| R1 | $499 | 3 | 2024-09-16·2024-11-25·2025-11-10 — 2024년 하반기 고점대. **현재가 바로 위** |
| **현재가** | **$474.95** (2026-09-11 종가) | — | R1과 S1 사이 |
| S1 | $466 | 2 | 2025-10-13·2025-11-17 — 2025년 가을 조정의 하단. 현재가 바로 아래 |
| S2 | $450 | 2 | 2024-11-04·2025-01-06 — 2024년 말~2025년 초 밴드의 바닥 |
| S3 | $379 | 2 | 2021-11-22·2025-04-07 — 2021년 말 하락 초입과 2025년 4월 관세 충격 저점이 3년 반을 사이에 두고 같은 가격대에서 만났다 |

비고 열의 시기는 `--emit dates` 출력을 그대로 옮긴 것이다. 유효 클러스터가 5개로 잡혀 R3에 해당하는 레벨은 없다 — 5년 최고($546.88, 2026-01) 위쪽으로는 스윙 포인트 자체가 존재하지 않기 때문이다.

**5년 구조에서 읽히는 것**: 이 차트의 핵심은 **2022년 한 해에 걸친 −43.6% 낙폭**(2021-11-01 주간 고가 $407.94 → 2022-10-10 주간 저가 $230.16)이다. 아래 3. 관측된 특이 구간에서 보듯 이것이 채권 발행 사이클 반전이 이 종목에 어떻게 작용하는지를 보여주는 실제 사례이며, [투자 판단](./07_investment.md) 3. 리스크 (약점 / Bear Case) 리스크1이 참조하는 선례다. 그 뒤 3년간 저점에서 2.4배 올라 2026-01 사상 최고($546.88)를 찍었고, 지금은 거기서 −13% 내려온 자리다. 현재가($474.95)는 R1 $499와 S1 $466 사이에 있으며, 그 아래 S3($379)까지는 20% 넘게 비어 있다 — **2025년 4월 이후 형성된 가격대가 아직 충분히 다져지지 않았다는 뜻**이다.

---

## 3. 관측된 특이 구간 — 2021~2022년 채권 발행 한파

- 계기: 금리 급등으로 회사채 발행이 급감하면서 MIS 거래성 매출이 직격탄을 맞았다. 실적 기록이 그 규모를 보여준다 — FY2021 → FY2022 매출 $6,218M → $5,468M(**−12.1%**), 영업이익 $2,844M → $1,883M(**−33.8%**, 마진 45.7% → 34.4%), GAAP 희석 EPS $11.78 → $7.44(**−36.8%**).
- 주가는 2021-11-01 주간 고가 $407.94에서 2022-10-10 주간 저가 $230.16까지 **약 11개월에 걸쳐 −43.6%** 하락했다. 5년 구간 최대 낙폭이다.
- **매출이 12% 줄었을 뿐인데 이익이 3분의 1 이상 증발했다** — 이 사업의 영업레버리지가 양방향으로 작동한다는 증거이며, 현재(2026 Q2) MIS 거래성 매출 비중이 그때보다 오히려 높은 70.7%라는 점에서 이 구간은 단순한 과거가 아니다.

### 참고 — 2026년 2월 급락

2026-01-12 주간 고가 $546.88에서 2026-02-09 주간 저가 $402.28까지 **4주 만에 −26.4%**. 폭은 2022년보다 작지만 속도는 훨씬 빨랐고, 원인도 다르다(실적이 아니라 정보 서비스 섹터 전체의 AI 대체 우려 — 일별 경위는 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 3. 관측된 특이 구간).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-09-13~2026-09-11. 수집 시점: 2026-09-13. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py MCO --name "Moody's" --interval 1wk --close-on 2026-09-11 --emit all` (재현용)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간의 2022년 −43.6% 하락 때문에 **$379(S3)와 $450(S2) 사이가 거의 비어 있다** — 그 구간을 빠르게 통과했기 때문이며, 지금 가격에서 하방으로 밀릴 경우 참고할 중간 레벨이 부족하다는 뜻이다.
    - 유효 클러스터가 5개(R2~S3)로 잡혀 템플릿의 3+3 구성과 다르다. 5년 최고 위쪽에는 스윙 포인트가 없어 R3을 만들지 않았고, `--force-level`은 사용하지 않았다.
    - 5년 구간 내 주식분할·분사 없음. 배당은 반영되지 않았다(원주가 기준).

---

*작성일: 2026-09-13*
