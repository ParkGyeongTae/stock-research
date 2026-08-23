# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 Yahoo Finance 주봉 API에서 직접 수집했다(5년 주봉은 핵심 지표가 다루는 범위 밖). 두 문서에서 겹치는 시점의 종가를 대조한 결과: 2026-08-14 종가 $482.74는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)·핵심 지표·밸류에이션 / 적정주가에서 인용한 stockanalysis.com 기준값과 정확히 일치한다.
>
> ⚠️ **배당 미반영 원주가 기준**: 조사 기간(5년) 중 Linde는 분기배당을 20회 지급했다(핵심 지표 A.4, 최근 33년 연속 증액). 이 문서의 가격은 배당을 반영하지 않은 원주가이므로, 배당락(ex-dividend) 효과가 스윙 포인트에 미세하게 섞여 있을 수 있다 — 다만 Linde의 분기배당(연 1.3%대 수익률)은 주가 대비 작아 지지/저항 레벨 해석에 미치는 영향은 제한적이다(4. 방법론 · 한계 참고).

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-14)

<div class="lin-chart">
<style>
.lin-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .lin-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .lin-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lin-chart svg { width:100%; height:auto; display:block; }
.lin-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lin-chart .title { fill: var(--ink); font-weight:600; }
.lin-chart .grid { stroke: var(--grid); stroke-width:1; }
.lin-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Linde(LIN) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Linde (LIN) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-14 · 마지막 종가 $482.74 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="534.1" x2="1052" y2="534.1" class="grid"/>
<text x="52" y="538.1" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="442.1" x2="1052" y2="442.1" class="grid"/>
<text x="52" y="446.1" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="350.2" x2="1052" y2="350.2" class="grid"/>
<text x="52" y="354.2" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="258.3" x2="1052" y2="258.3" class="grid"/>
<text x="52" y="262.3" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="166.3" x2="1052" y2="166.3" class="grid"/>
<text x="52" y="170.3" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="74.4" x2="1052" y2="74.4" class="grid"/>
<text x="52" y="78.4" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
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
<line x1="60" y1="77.7" x2="1052" y2="77.7" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="80.7" font-size="10.5" fill="var(--muted)">$548 5년 최고(2026-07, 사상 최고가)</text>
<line x1="281.5" y1="56.0" x2="281.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="287.5" y="68.0" font-size="10.5" fill="var(--down)">2022-09-26 2022 금리인상기 저점(고점 대비 -25.5%)</text>
<line x1="61.9" y1="507.6" x2="61.9" y2="519.8" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="508.6" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="65.7" y1="506.5" x2="65.7" y2="515.7" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="507.3" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="69.5" y1="504.1" x2="69.5" y2="511.8" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="505.4" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="73.3" y1="502.8" x2="73.3" y2="515.5" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="504.1" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="77.0" y1="505.0" x2="77.0" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="507.3" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="80.8" y1="512.3" x2="80.8" y2="534.9" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="515.2" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="84.6" y1="511.5" x2="84.6" y2="547.7" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="514.8" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="88.4" y1="529.7" x2="88.4" y2="552.0" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="540.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="92.2" y1="516.5" x2="92.2" y2="544.7" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="518.9" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="96.0" y1="506.5" x2="96.0" y2="523.5" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="508.0" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="99.8" y1="492.3" x2="99.8" y2="508.4" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="498.8" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="103.5" y1="474.1" x2="103.5" y2="496.4" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="475.2" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="107.3" y1="460.2" x2="107.3" y2="469.6" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="466.0" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="111.1" y1="466.5" x2="111.1" y2="480.4" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="466.5" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="114.9" y1="470.9" x2="114.9" y2="498.9" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="473.8" width="2.35" height="22.4" fill="var(--down)"/>
<line x1="118.7" y1="484.4" x2="118.7" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="494.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="122.5" y1="470.0" x2="122.5" y2="490.9" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="471.5" width="2.35" height="16.3" fill="var(--up)"/>
<line x1="126.3" y1="454.4" x2="126.3" y2="476.3" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="471.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="130.0" y1="459.3" x2="130.0" y2="484.4" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="462.0" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="133.8" y1="447.7" x2="133.8" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="448.7" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="137.6" y1="438.1" x2="137.6" y2="472.8" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="448.7" width="2.35" height="18.6" fill="var(--down)"/>
<line x1="141.4" y1="457.0" x2="141.4" y2="487.8" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="472.6" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="145.2" y1="483.3" x2="145.2" y2="505.6" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="492.1" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="149.0" y1="501.4" x2="149.0" y2="526.5" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="506.6" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="152.8" y1="489.0" x2="152.8" y2="538.6" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="515.6" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="156.5" y1="503.1" x2="156.5" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="540.1" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="160.3" y1="524.4" x2="160.3" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="528.8" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="164.1" y1="538.4" x2="164.1" y2="576.8" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="538.7" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="167.9" y1="543.8" x2="167.9" y2="577.5" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="556.2" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="171.7" y1="540.9" x2="171.7" y2="593.8" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="569.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="175.5" y1="511.0" x2="175.5" y2="562.4" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="512.6" width="2.35" height="42.3" fill="var(--up)"/>
<line x1="179.3" y1="495.6" x2="179.3" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="499.6" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="183.1" y1="480.7" x2="183.1" y2="499.1" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="492.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="186.8" y1="488.0" x2="186.8" y2="511.8" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="496.6" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="190.6" y1="496.0" x2="190.6" y2="510.4" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="500.0" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="194.4" y1="474.7" x2="194.4" y2="517.5" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="500.1" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="198.2" y1="499.3" x2="198.2" y2="528.5" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="512.1" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="202.0" y1="492.0" x2="202.0" y2="527.1" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="507.3" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="205.8" y1="513.5" x2="205.8" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="517.9" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="209.6" y1="499.3" x2="209.6" y2="525.0" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="506.2" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="213.3" y1="479.3" x2="213.3" y2="509.6" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="479.6" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="217.1" y1="472.4" x2="217.1" y2="501.3" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="475.4" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="220.9" y1="464.2" x2="220.9" y2="519.6" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="467.2" width="2.35" height="46.9" fill="var(--down)"/>
<line x1="224.7" y1="525.8" x2="224.7" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="529.2" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="228.5" y1="525.6" x2="228.5" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="528.1" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="232.3" y1="532.6" x2="232.3" y2="569.1" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="534.8" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="236.1" y1="577.5" x2="236.1" y2="595.1" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="582.5" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="239.8" y1="574.2" x2="239.8" y2="598.2" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="576.4" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="243.6" y1="554.8" x2="243.6" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="560.7" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="247.4" y1="528.3" x2="247.4" y2="562.8" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="530.4" width="2.35" height="27.7" fill="var(--up)"/>
<line x1="251.2" y1="526.5" x2="251.2" y2="541.8" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="530.4" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="255.0" y1="512.8" x2="255.0" y2="534.5" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="512.8" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="258.8" y1="509.3" x2="258.8" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="516.0" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="262.6" y1="538.6" x2="262.6" y2="559.8" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="540.7" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="266.4" y1="552.4" x2="266.4" y2="583.2" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="559.2" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="270.1" y1="556.0" x2="270.1" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="557.9" width="2.35" height="19.6" fill="var(--up)"/>
<line x1="273.9" y1="542.9" x2="273.9" y2="573.6" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="547.1" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="277.7" y1="561.1" x2="277.7" y2="596.8" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="569.9" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="281.5" y1="581.6" x2="281.5" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="590.0" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="285.3" y1="557.7" x2="285.3" y2="586.9" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="583.3" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="289.1" y1="556.9" x2="289.1" y2="596.2" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="579.4" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="292.9" y1="554.6" x2="292.9" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="555.5" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="296.6" y1="528.5" x2="296.6" y2="577.0" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="530.8" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="300.4" y1="515.6" x2="300.4" y2="552.6" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="517.6" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="304.2" y1="471.1" x2="304.2" y2="516.7" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="478.5" width="2.35" height="35.2" fill="var(--up)"/>
<line x1="308.0" y1="461.9" x2="308.0" y2="482.6" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="469.9" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="311.8" y1="452.1" x2="311.8" y2="474.0" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="452.4" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="315.6" y1="451.5" x2="315.6" y2="481.8" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="451.9" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="319.4" y1="467.3" x2="319.4" y2="479.8" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="469.4" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="323.1" y1="446.5" x2="323.1" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="467.8" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="326.9" y1="477.2" x2="326.9" y2="491.7" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="480.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="330.7" y1="475.1" x2="330.7" y2="491.4" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="477.7" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="334.5" y1="493.6" x2="334.5" y2="530.1" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="501.6" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="338.3" y1="470.2" x2="338.3" y2="498.4" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="471.3" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="342.1" y1="467.3" x2="342.1" y2="494.6" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="468.8" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="345.9" y1="479.8" x2="345.9" y2="490.4" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="486.5" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="349.6" y1="470.6" x2="349.6" y2="491.0" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="489.2" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="353.4" y1="448.3" x2="353.4" y2="499.3" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="475.2" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="357.2" y1="468.0" x2="357.2" y2="498.7" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="473.3" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="361.0" y1="445.4" x2="361.0" y2="493.4" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="446.4" width="2.35" height="45.5" fill="var(--up)"/>
<line x1="364.8" y1="418.7" x2="364.8" y2="452.8" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="419.4" width="2.35" height="29.7" fill="var(--up)"/>
<line x1="368.6" y1="422.5" x2="368.6" y2="460.3" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="423.7" width="2.35" height="33.9" fill="var(--down)"/>
<line x1="372.4" y1="448.8" x2="372.4" y2="489.7" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="462.8" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="376.2" y1="449.3" x2="376.2" y2="475.3" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="451.8" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="379.9" y1="431.8" x2="379.9" y2="452.1" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="432.1" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="383.7" y1="421.1" x2="383.7" y2="438.4" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="430.0" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="387.5" y1="416.1" x2="387.5" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="424.3" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="391.3" y1="409.9" x2="391.3" y2="424.6" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="412.3" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="395.1" y1="404.4" x2="395.1" y2="424.1" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="406.4" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="398.9" y1="398.8" x2="398.9" y2="428.4" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="403.9" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="402.7" y1="404.0" x2="402.7" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="404.7" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="406.4" y1="400.9" x2="406.4" y2="419.7" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="402.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="410.2" y1="399.7" x2="410.2" y2="440.2" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="400.8" width="2.35" height="30.0" fill="var(--down)"/>
<line x1="414.0" y1="420.7" x2="414.0" y2="441.0" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="422.9" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="417.8" y1="410.5" x2="417.8" y2="427.8" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="420.5" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="421.6" y1="389.7" x2="421.6" y2="426.3" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="395.6" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="425.4" y1="396.4" x2="425.4" y2="413.6" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="397.3" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="429.2" y1="380.4" x2="429.2" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="385.0" width="2.35" height="20.4" fill="var(--up)"/>
<line x1="432.9" y1="382.6" x2="432.9" y2="426.7" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="383.3" width="2.35" height="32.2" fill="var(--down)"/>
<line x1="436.7" y1="387.9" x2="436.7" y2="417.7" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="389.6" width="2.35" height="27.0" fill="var(--up)"/>
<line x1="440.5" y1="377.0" x2="440.5" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="378.6" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="444.3" y1="365.6" x2="444.3" y2="387.7" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="371.0" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="448.1" y1="361.8" x2="448.1" y2="391.5" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="371.3" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="451.9" y1="374.9" x2="451.9" y2="388.9" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="383.6" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="455.7" y1="380.8" x2="455.7" y2="398.4" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="384.9" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="459.5" y1="381.0" x2="459.5" y2="399.0" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="384.0" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="463.2" y1="366.7" x2="463.2" y2="388.2" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="370.6" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="467.0" y1="368.6" x2="467.0" y2="387.9" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="368.6" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="470.8" y1="362.3" x2="470.8" y2="378.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="371.2" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="474.6" y1="367.9" x2="474.6" y2="404.1" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="372.9" width="2.35" height="27.1" fill="var(--down)"/>
<line x1="478.4" y1="392.7" x2="478.4" y2="407.2" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="401.0" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="482.2" y1="385.1" x2="482.2" y2="411.8" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="398.8" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="486.0" y1="382.4" x2="486.0" y2="406.8" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="390.8" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="489.7" y1="379.0" x2="489.7" y2="412.8" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="389.8" width="2.35" height="22.3" fill="var(--down)"/>
<line x1="493.5" y1="393.3" x2="493.5" y2="421.9" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="404.4" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="497.3" y1="359.1" x2="497.3" y2="398.6" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="364.0" width="2.35" height="30.2" fill="var(--up)"/>
<line x1="501.1" y1="349.5" x2="501.1" y2="377.6" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="350.5" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="504.9" y1="329.8" x2="504.9" y2="359.4" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="335.7" width="2.35" height="21.2" fill="var(--up)"/>
<line x1="508.7" y1="320.4" x2="508.7" y2="338.8" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="324.0" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="512.5" y1="320.8" x2="512.5" y2="332.2" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="324.8" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="516.2" y1="329.5" x2="516.2" y2="355.0" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="333.6" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="520.0" y1="287.3" x2="520.0" y2="350.4" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="336.6" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="523.8" y1="324.0" x2="523.8" y2="339.3" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="328.3" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="527.6" y1="327.9" x2="527.6" y2="335.6" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="330.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="531.4" y1="328.6" x2="531.4" y2="340.5" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="332.2" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="535.2" y1="331.8" x2="535.2" y2="347.2" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="333.8" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="539.0" y1="330.7" x2="539.0" y2="343.3" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="336.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="542.7" y1="334.8" x2="542.7" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="342.8" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="546.5" y1="330.7" x2="546.5" y2="346.0" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="337.2" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="550.3" y1="306.1" x2="550.3" y2="357.4" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="314.5" width="2.35" height="41.5" fill="var(--up)"/>
<line x1="554.1" y1="286.3" x2="554.1" y2="324.0" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="292.0" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="557.9" y1="260.9" x2="557.9" y2="287.3" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="262.7" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="561.7" y1="252.5" x2="561.7" y2="273.2" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="259.7" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="565.5" y1="225.6" x2="565.5" y2="260.6" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="235.2" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="569.3" y1="207.3" x2="569.3" y2="228.1" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="214.2" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="573.0" y1="210.5" x2="573.0" y2="235.3" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="224.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="576.8" y1="224.5" x2="576.8" y2="238.1" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="226.6" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="580.6" y1="227.1" x2="580.6" y2="247.3" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="228.9" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="584.4" y1="234.2" x2="584.4" y2="269.0" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="234.6" width="2.35" height="28.4" fill="var(--down)"/>
<line x1="588.2" y1="251.1" x2="588.2" y2="271.4" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="258.4" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="592.0" y1="260.1" x2="592.0" y2="288.8" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="270.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="595.8" y1="259.4" x2="595.8" y2="325.2" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="266.0" width="2.35" height="40.8" fill="var(--down)"/>
<line x1="599.5" y1="280.4" x2="599.5" y2="307.1" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="287.0" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="603.3" y1="281.9" x2="603.3" y2="299.0" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="285.7" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="607.1" y1="281.2" x2="607.1" y2="293.1" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="284.8" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="610.9" y1="284.0" x2="610.9" y2="306.3" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="284.9" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="614.7" y1="280.0" x2="614.7" y2="297.6" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="287.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="618.5" y1="275.1" x2="618.5" y2="301.3" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="282.3" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="622.3" y1="267.0" x2="622.3" y2="285.8" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="271.6" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="626.0" y1="264.7" x2="626.0" y2="283.4" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="267.9" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="629.8" y1="275.2" x2="629.8" y2="304.9" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="278.2" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="633.6" y1="268.5" x2="633.6" y2="294.5" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="275.4" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="637.4" y1="255.0" x2="637.4" y2="281.2" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="267.9" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="641.2" y1="253.2" x2="641.2" y2="273.0" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="255.7" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="645.0" y1="240.8" x2="645.0" y2="269.8" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="250.9" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="648.8" y1="247.8" x2="648.8" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="250.9" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="652.5" y1="244.7" x2="652.5" y2="267.3" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="245.7" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="656.3" y1="228.0" x2="656.3" y2="246.9" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="229.3" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="660.1" y1="203.5" x2="660.1" y2="230.5" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="206.3" width="2.35" height="23.2" fill="var(--up)"/>
<line x1="663.9" y1="205.6" x2="663.9" y2="246.9" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="214.2" width="2.35" height="31.4" fill="var(--down)"/>
<line x1="667.7" y1="218.2" x2="667.7" y2="251.8" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="223.7" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="671.5" y1="208.6" x2="671.5" y2="231.2" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="213.3" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="675.3" y1="196.9" x2="675.3" y2="217.6" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="204.0" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="679.1" y1="203.9" x2="679.1" y2="230.9" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="204.4" width="2.35" height="20.5" fill="var(--down)"/>
<line x1="682.8" y1="213.0" x2="682.8" y2="238.5" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="214.1" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="686.6" y1="189.3" x2="686.6" y2="215.2" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="191.2" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="690.4" y1="193.0" x2="690.4" y2="218.5" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="194.0" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="694.2" y1="206.8" x2="694.2" y2="251.8" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="210.8" width="2.35" height="34.0" fill="var(--down)"/>
<line x1="698.0" y1="225.2" x2="698.0" y2="250.6" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="240.8" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="701.8" y1="235.5" x2="701.8" y2="264.0" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="240.8" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="705.6" y1="245.0" x2="705.6" y2="277.1" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="249.5" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="709.3" y1="236.8" x2="709.3" y2="255.9" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="238.1" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="713.1" y1="236.4" x2="713.1" y2="263.9" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="238.1" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="716.9" y1="256.8" x2="716.9" y2="290.0" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="262.1" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="720.7" y1="284.5" x2="720.7" y2="316.6" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="284.5" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="724.5" y1="301.3" x2="724.5" y2="317.7" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="307.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="728.3" y1="308.4" x2="728.3" y2="326.1" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="314.9" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="732.1" y1="312.6" x2="732.1" y2="330.5" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="321.8" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="735.8" y1="276.6" x2="735.8" y2="325.0" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="284.0" width="2.35" height="37.2" fill="var(--up)"/>
<line x1="739.6" y1="260.7" x2="739.6" y2="278.4" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="277.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="743.4" y1="258.9" x2="743.4" y2="286.8" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="265.4" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="747.2" y1="237.1" x2="747.2" y2="275.8" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="249.0" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="751.0" y1="232.3" x2="751.0" y2="252.0" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="245.4" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="754.8" y1="228.8" x2="754.8" y2="258.2" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="243.5" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="758.6" y1="223.3" x2="758.6" y2="247.2" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="226.9" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="762.4" y1="217.4" x2="762.4" y2="240.1" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="223.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="766.1" y1="219.3" x2="766.1" y2="262.9" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="228.9" width="2.35" height="19.3" fill="var(--down)"/>
<line x1="769.9" y1="231.0" x2="769.9" y2="259.4" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="242.9" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="773.7" y1="227.6" x2="773.7" y2="249.1" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="241.5" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="777.5" y1="217.8" x2="777.5" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="241.9" width="2.35" height="38.4" fill="var(--down)"/>
<line x1="781.3" y1="258.9" x2="781.3" y2="334.3" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="273.3" width="2.35" height="23.4" fill="var(--up)"/>
<line x1="785.1" y1="248.8" x2="785.1" y2="273.4" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="254.4" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="788.9" y1="243.9" x2="788.9" y2="276.1" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="257.3" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="792.6" y1="245.1" x2="792.6" y2="289.2" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="249.2" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="796.4" y1="243.5" x2="796.4" y2="267.6" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="252.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="800.2" y1="242.9" x2="800.2" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="244.0" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="804.0" y1="236.7" x2="804.0" y2="251.7" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="241.9" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="807.8" y1="223.1" x2="807.8" y2="238.7" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="225.9" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="811.6" y1="211.4" x2="811.6" y2="237.4" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="216.5" width="2.35" height="13.9" fill="var(--up)"/>
<line x1="815.4" y1="210.5" x2="815.4" y2="230.4" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="217.5" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="819.1" y1="222.3" x2="819.1" y2="248.4" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="227.3" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="822.9" y1="226.3" x2="822.9" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="232.9" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="826.7" y1="205.5" x2="826.7" y2="233.3" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="211.2" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="830.5" y1="209.6" x2="830.5" y2="231.6" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="217.1" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="834.3" y1="221.5" x2="834.3" y2="247.2" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="224.4" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="838.1" y1="209.8" x2="838.1" y2="235.4" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="216.2" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="841.9" y1="217.2" x2="841.9" y2="259.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="223.8" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="845.6" y1="210.8" x2="845.6" y2="240.1" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="217.0" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="849.4" y1="198.2" x2="849.4" y2="228.6" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="202.9" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="853.2" y1="191.4" x2="853.2" y2="209.4" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="200.0" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="857.0" y1="195.7" x2="857.0" y2="212.3" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="199.6" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="860.8" y1="208.3" x2="860.8" y2="227.8" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="208.3" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="864.6" y1="194.9" x2="864.6" y2="227.7" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="199.3" width="2.35" height="22.8" fill="var(--up)"/>
<line x1="868.4" y1="197.0" x2="868.4" y2="219.8" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="200.6" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="872.2" y1="197.6" x2="872.2" y2="221.6" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="208.6" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="875.9" y1="205.3" x2="875.9" y2="238.4" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="212.8" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="879.7" y1="218.4" x2="879.7" y2="252.9" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="227.5" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="883.5" y1="236.1" x2="883.5" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="246.2" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="887.3" y1="248.6" x2="887.3" y2="266.4" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="253.9" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="891.1" y1="258.0" x2="891.1" y2="323.6" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="262.6" width="2.35" height="54.0" fill="var(--down)"/>
<line x1="894.9" y1="308.2" x2="894.9" y2="333.6" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="309.3" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="898.7" y1="292.2" x2="898.7" y2="320.9" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="307.2" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="902.4" y1="307.2" x2="902.4" y2="338.4" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="310.5" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="906.2" y1="326.5" x2="906.2" y2="339.0" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="331.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="910.0" y1="328.9" x2="910.0" y2="352.2" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="331.8" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="913.8" y1="317.1" x2="913.8" y2="372.7" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="320.3" width="2.35" height="32.1" fill="var(--up)"/>
<line x1="917.6" y1="305.2" x2="917.6" y2="331.8" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="310.8" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="921.4" y1="301.2" x2="921.4" y2="312.4" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="304.6" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="925.2" y1="293.5" x2="925.2" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="296.7" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="928.9" y1="267.4" x2="928.9" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="269.1" width="2.35" height="34.0" fill="var(--up)"/>
<line x1="932.7" y1="265.6" x2="932.7" y2="284.6" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="272.3" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="936.5" y1="254.6" x2="936.5" y2="296.6" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="255.4" width="2.35" height="31.7" fill="var(--up)"/>
<line x1="940.3" y1="244.7" x2="940.3" y2="261.6" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="245.4" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="944.1" y1="208.0" x2="944.1" y2="267.5" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="241.1" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="947.9" y1="187.4" x2="947.9" y2="269.3" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="201.3" width="2.35" height="60.4" fill="var(--up)"/>
<line x1="951.7" y1="169.4" x2="951.7" y2="206.8" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="172.7" width="2.35" height="32.0" fill="var(--up)"/>
<line x1="955.5" y1="146.7" x2="955.5" y2="179.6" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="151.5" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="959.2" y1="147.8" x2="959.2" y2="203.7" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="151.6" width="2.35" height="42.8" fill="var(--down)"/>
<line x1="963.0" y1="166.3" x2="963.0" y2="219.4" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="177.5" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="966.8" y1="165.7" x2="966.8" y2="196.7" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="176.8" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="970.6" y1="165.8" x2="970.6" y2="215.2" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="182.7" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="974.4" y1="159.6" x2="974.4" y2="187.5" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="161.5" width="2.35" height="12.4" fill="var(--up)"/>
<line x1="978.2" y1="153.1" x2="978.2" y2="198.0" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="159.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="982.0" y1="149.4" x2="982.0" y2="188.4" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="159.7" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="985.7" y1="146.7" x2="985.7" y2="180.4" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="147.4" width="2.35" height="28.8" fill="var(--up)"/>
<line x1="989.5" y1="127.2" x2="989.5" y2="166.9" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="147.4" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="993.3" y1="154.7" x2="993.3" y2="184.0" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="159.7" width="2.35" height="19.2" fill="var(--down)"/>
<line x1="997.1" y1="135.0" x2="997.1" y2="177.6" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="155.1" width="2.35" height="22.4" fill="var(--up)"/>
<line x1="1000.9" y1="127.3" x2="1000.9" y2="166.4" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="134.0" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="1004.7" y1="131.2" x2="1004.7" y2="174.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="133.5" width="2.35" height="37.1" fill="var(--down)"/>
<line x1="1008.5" y1="133.9" x2="1008.5" y2="186.8" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="151.8" width="2.35" height="21.6" fill="var(--up)"/>
<line x1="1012.2" y1="118.8" x2="1012.2" y2="166.4" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="123.0" width="2.35" height="30.2" fill="var(--up)"/>
<line x1="1016.0" y1="118.8" x2="1016.0" y2="145.8" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="131.3" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="1019.8" y1="114.9" x2="1019.8" y2="153.2" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="130.2" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="1023.6" y1="79.5" x2="1023.6" y2="153.9" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="80.6" width="2.35" height="50.6" fill="var(--up)"/>
<line x1="1027.4" y1="77.7" x2="1027.4" y2="131.4" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="85.9" width="2.35" height="25.6" fill="var(--down)"/>
<line x1="1031.2" y1="106.7" x2="1031.2" y2="146.7" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="109.5" width="2.35" height="32.5" fill="var(--down)"/>
<line x1="1035.0" y1="136.0" x2="1035.0" y2="162.5" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="141.4" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="1038.7" y1="125.9" x2="1038.7" y2="227.2" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="141.8" width="2.35" height="64.3" fill="var(--down)"/>
<line x1="1042.5" y1="167.8" x2="1042.5" y2="209.7" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="184.7" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="1046.3" y1="173.8" x2="1046.3" y2="210.9" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="186.0" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="1050.1" y1="196.7" x2="1050.1" y2="208.4" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="198.1" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="60" y1="137.0" x2="1052" y2="137.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="140.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$516 R1</text>
<text x="1058" y="152.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="256.2" x2="1052" y2="256.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="250.2" font-size="11.5" fill="var(--support)" font-weight="600">$451 S1</text>
<text x="1058" y="262.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="330.0" x2="1052" y2="330.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="324.0" font-size="11.5" fill="var(--support)" font-weight="600">$411 S2</text>
<text x="1058" y="336.0" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="365.0" x2="1052" y2="365.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="359.0" font-size="11.5" fill="var(--support)" font-weight="600">$392 S3</text>
<text x="1058" y="371.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="598.4" x2="1052" y2="598.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="592.4" font-size="11.5" fill="var(--support)" font-weight="600">$265 S4 (2022년 저점)</text>
<text x="1058" y="604.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="198.1" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). 기술적 분석 — 일봉·1년의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다 — 둘을 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $516 | 2 | 2026년 2월·4월(2026-02-23·2026-04-20/27) 스윙 고점대 — 기술적 분석 — 일봉·1년의 R1($507)과 근접한 상위 밴드 |
| **현재가** | **$482.74** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $451 | 2 | 2025년 6~7월(2025-06-23·2025-07-28) 스윙 저점대 |
| S2 | $411 | 3 | 2024년 4월~2025년 4월(2024-04-29·2025-01-06·2025-04-07)에 걸쳐 3회 반복된 저점대 |
| S3 | $392 | 2 | 2024년 2월·2025년 12월(2024-02-05·2025-12-08) 스윙 저점대 |
| S4 (2022년 저점) | $265 | 3 | 2022년 3~9월(2022-03-07·2022-07-11·2022-09-26) 형성된 5년 최저치 구간. 현재가에서 45% 이상 떨어져 있어 기본 표시 범위(현재가 기준 상하 3개) 밖이지만, 2022년 금리인상기 조정의 저점이라는 구조적 의미가 커 `--force-level`로 예외 포함(3. 관측된 특이 구간 — 2022년 금리인상기 조정 참고) |
| 참고선 | $548 | — | 5년 최고(2026-07, 사상 최고가 $548.20). 2026-07-31 Q2 실적 발표 갭다운(기술적 분석 — 일봉·1년 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운) 이후 가격대가 재설정되며 현재가와 12% 이상 괴리돼 있어 근시일 저항으로 보지 않음 |

> 표시 기준은 "현재가에서 가까운 순으로 각 방향 3개"다(4. 방법론 · 한계 생성 스크립트 기본값). 저항 쪽은 유효 클러스터가 1개(R1)뿐이라 R2·R3 없이 표시했다 — 억지로 채우지 않았다. S4($265)는 이 기본값 밖에서 강제로 추가한 예외 레벨.

---

## 3. 관측된 특이 구간 — 2022년 금리인상기 조정

- 2021년 말부터 미 연준의 공격적 금리인상 사이클이 본격화되며, Linde도 예외 없이 조정을 받았다. 2022-01-03 주간 고점 $352.18에서 2022-09-26 주간 저점 $262.47까지 약 9개월간 **-25.5%** 하락했다(주간 종가 기준이 아닌 고가·저가 기준).
- 이후 완만하게 회복해 2023-02-27 무렵 하락 전 고점($352.18)을 다시 상회했다 — 저점 형성 후 약 5개월 만의 회복.
- 낙폭(-25.5%)과 하락 기간(약 9개월, 완만한 그라인딩 다운)은 같은 시기 조정을 겪은 [Synopsys](../../electronic_design_automation/synopsys/10_technical_weekly.md)(−32.5%, 약 4.5개월 급락)·[Cadence](../../electronic_design_automation/cadence_design_systems/10_technical_weekly.md)(−31.3%, 약 4.5개월 급락)보다 낙폭이 작고 하락 속도도 느렸다 — 산업가스라는 방어적 업종 특성이 반영된 결과로 해석할 수 있으나, 업종 간 비교는 참고 수준일 뿐 통계적으로 검증한 것은 아니다.
- 이 조정은 회사 고유 이슈가 아니라 거시 금리 환경에 따른 밸류에이션 디레이팅 성격이 강하다. 기술적 분석 — 일봉·1년 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운의 2026-07-31 실적발표 갭다운(회사 고유 이벤트)과는 원인이 다르므로 혼동하지 말 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-16~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영, 배당은 미반영) — 조사 기간 중 Linde의 주식분할 이력은 확인되지 않는다(핵심 지표 상단 각주와 일치). 다만 이 기간 중 분기배당을 20회 지급했고 가격에는 반영돼 있지 않다(위 상단 경고 참고).
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 기술적 분석 — 일봉·1년(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py LIN --name Linde --interval 1wk --ref-line 548.20:"5년 최고(2026-07, 사상 최고가)" --force-level '262.47:(2022년 저점)' --event '2022-09-26:2022 금리인상기 저점(고점 대비 -25.5%)' --close-on 2026-08-13 --close-on 2026-08-14`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - 배당 미반영 원주가라 배당락 효과가 스윙 레벨에 미세하게 섞여 있을 수 있다(위 상단 경고 참고) — 다만 Linde의 분기배당 규모(연 수익률 1.3%대)가 작아 영향은 제한적이다.
    - 기술적 분석 — 일봉·1년 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운의 2026-07-31 실적발표 갭다운처럼 뉴스 이벤트로 인한 불연속 구간은 통상적인 지지/저항 해석이 적용되기 어렵다 — 참고선($548)을 근시일 저항으로 취급하지 않은 이유이기도 하다.

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

---

## 참고 자료

- [Yahoo Finance — LIN Chart API](https://query1.finance.yahoo.com/v8/finance/chart/LIN) (주봉 OHLCV 원자료, 2026-08-16 수집)
- [stockanalysis.com — LIN Price History](https://stockanalysis.com/stocks/lin/history/)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-23)*
