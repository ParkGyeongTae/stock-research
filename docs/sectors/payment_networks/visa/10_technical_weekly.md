# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [`09_technical_daily.md`](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `04_metrics.md`의 원자료 표와는 별도로, 이 차트 작성을 위해 주봉 API(Yahoo Finance)에서 직접 수집했다(5년 주봉은 `04_metrics.md`가 다루는 범위 밖이라 단일 출처 규칙의 예외). 겹치는 시점의 종가를 대조한 결과: `2026-08-14` 종가 $364.15는 [`01_overview.md`](./01_overview.md)·[`04_metrics.md`](./04_metrics.md) A.2·[`06_valuation.md`](./06_valuation.md)에 인용된 현재주가와 **일치**한다. 이 주봉 데이터의 주 경계(월요일 기준)는 09_technical_daily.md·04_metrics.md가 쓰는 회계연도 말(9/30) 종가와 정확히 같은 날짜로 떨어지지 않아 별도로 대조하지 않았다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-16 ~ 2026-08-14)

<div class="v-chart">
<style>
.v-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .v-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .v-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.v-chart svg { width:100%; height:auto; display:block; }
.v-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.v-chart .title { fill: var(--ink); font-weight:600; }
.v-chart .grid { stroke: var(--grid); stroke-width:1; }
.v-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Visa(V) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Visa (V) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-14 · 마지막 종가 $364.15 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="535.3" x2="1052" y2="535.3" class="grid"/>
<text x="52" y="539.3" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="405.8" x2="1052" y2="405.8" class="grid"/>
<text x="52" y="409.8" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="276.2" x2="1052" y2="276.2" class="grid"/>
<text x="52" y="280.2" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="146.7" x2="1052" y2="146.7" class="grid"/>
<text x="52" y="150.7" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
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
<line x1="675.3" y1="56.0" x2="675.3" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="681.3" y="68.0" font-size="10.5" fill="var(--down)">2024-09-23 DOJ 반독점 소송(debit 시장 독점) 제기</text>
<line x1="61.9" y1="442.9" x2="61.9" y2="460.4" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="451.9" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="65.7" y1="441.6" x2="65.7" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="450.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="69.5" y1="448.1" x2="69.5" y2="478.4" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="450.6" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="73.3" y1="457.0" x2="73.3" y2="471.0" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="466.0" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="77.0" y1="464.8" x2="77.0" y2="485.3" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="469.2" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="80.8" y1="452.5" x2="80.8" y2="493.1" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="453.5" width="2.35" height="37.9" fill="var(--up)"/>
<line x1="84.6" y1="449.0" x2="84.6" y2="476.7" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="453.1" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="88.4" y1="450.5" x2="88.4" y2="481.4" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="456.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="92.2" y1="454.8" x2="92.2" y2="487.0" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="455.0" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="96.0" y1="447.7" x2="96.0" y2="467.2" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="454.4" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="99.8" y1="439.6" x2="99.8" y2="513.2" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="448.7" width="2.35" height="56.2" fill="var(--down)"/>
<line x1="103.5" y1="489.6" x2="103.5" y2="517.9" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="492.1" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="107.3" y1="479.3" x2="107.3" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="487.7" width="2.35" height="16.3" fill="var(--down)"/>
<line x1="111.1" y1="492.8" x2="111.1" y2="536.7" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="500.0" width="2.35" height="33.1" fill="var(--down)"/>
<line x1="114.9" y1="525.1" x2="114.9" y2="554.6" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="535.3" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="118.7" y1="532.1" x2="118.7" y2="561.0" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="532.7" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="122.5" y1="498.4" x2="122.5" y2="541.2" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="500.6" width="2.35" height="37.9" fill="var(--up)"/>
<line x1="126.3" y1="493.2" x2="126.3" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="503.1" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="130.0" y1="486.2" x2="130.0" y2="517.5" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="492.3" width="2.35" height="19.5" fill="var(--up)"/>
<line x1="133.8" y1="484.2" x2="133.8" y2="496.8" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="489.5" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="137.6" y1="465.9" x2="137.6" y2="494.8" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="489.9" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="141.4" y1="482.3" x2="141.4" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="497.3" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="145.2" y1="484.5" x2="145.2" y2="520.2" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="494.2" width="2.35" height="25.8" fill="var(--down)"/>
<line x1="149.0" y1="462.5" x2="149.0" y2="546.6" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="462.8" width="2.35" height="66.9" fill="var(--up)"/>
<line x1="152.8" y1="442.4" x2="152.8" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="461.8" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="156.5" y1="449.4" x2="156.5" y2="474.3" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="462.8" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="160.3" y1="457.9" x2="160.3" y2="478.7" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="475.0" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="164.1" y1="472.3" x2="164.1" y2="531.6" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="480.9" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="167.9" y1="487.0" x2="167.9" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="493.9" width="2.35" height="40.7" fill="var(--down)"/>
<line x1="171.7" y1="533.1" x2="171.7" y2="569.9" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="535.7" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="175.5" y1="485.4" x2="175.5" y2="540.1" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="485.8" width="2.35" height="53.6" fill="var(--up)"/>
<line x1="179.3" y1="484.6" x2="179.3" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="487.6" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="183.1" y1="460.7" x2="183.1" y2="490.0" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="467.0" width="2.35" height="20.4" fill="var(--up)"/>
<line x1="186.8" y1="459.6" x2="186.8" y2="501.4" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="468.6" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="190.6" y1="490.5" x2="190.6" y2="516.7" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="495.8" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="194.4" y1="473.3" x2="194.4" y2="514.7" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="505.1" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="198.2" y1="470.7" x2="198.2" y2="532.5" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="501.3" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="202.0" y1="497.0" x2="202.0" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="504.8" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="205.8" y1="533.4" x2="205.8" y2="561.4" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="535.2" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="209.6" y1="521.2" x2="209.6" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="537.8" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="213.3" y1="501.0" x2="213.3" y2="537.8" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="501.9" width="2.35" height="31.1" fill="var(--up)"/>
<line x1="217.1" y1="495.8" x2="217.1" y2="512.5" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="502.5" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="220.9" y1="489.8" x2="220.9" y2="537.4" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="495.3" width="2.35" height="41.3" fill="var(--down)"/>
<line x1="224.7" y1="538.3" x2="224.7" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="553.5" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="228.5" y1="520.7" x2="228.5" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="521.0" width="2.35" height="25.4" fill="var(--up)"/>
<line x1="232.3" y1="516.9" x2="232.3" y2="553.8" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="520.4" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="236.1" y1="524.7" x2="236.1" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="526.1" width="2.35" height="19.0" fill="var(--up)"/>
<line x1="239.8" y1="505.0" x2="239.8" y2="540.6" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="509.3" width="2.35" height="20.8" fill="var(--up)"/>
<line x1="243.6" y1="488.5" x2="243.6" y2="518.1" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="499.8" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="247.4" y1="491.7" x2="247.4" y2="532.2" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="497.5" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="251.2" y1="494.0" x2="251.2" y2="525.1" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="494.2" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="255.0" y1="492.2" x2="255.0" y2="510.1" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="495.9" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="258.8" y1="489.7" x2="258.8" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="502.1" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="262.6" y1="506.2" x2="262.6" y2="528.3" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="509.6" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="266.4" y1="523.9" x2="266.4" y2="544.0" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="532.1" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="270.1" y1="518.7" x2="270.1" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="521.8" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="273.9" y1="516.7" x2="273.9" y2="565.8" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="518.5" width="2.35" height="34.2" fill="var(--down)"/>
<line x1="277.7" y1="550.9" x2="277.7" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="557.1" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="281.5" y1="574.6" x2="281.5" y2="600.5" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="579.3" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="285.3" y1="564.3" x2="285.3" y2="591.9" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="577.2" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="289.1" y1="568.7" x2="289.1" y2="601.1" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="576.4" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="292.9" y1="558.7" x2="292.9" y2="579.8" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="560.3" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="296.6" y1="505.5" x2="296.6" y2="563.6" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="511.1" width="2.35" height="46.5" fill="var(--up)"/>
<line x1="300.4" y1="509.5" x2="300.4" y2="550.4" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="512.2" width="2.35" height="30.9" fill="var(--down)"/>
<line x1="304.2" y1="518.7" x2="304.2" y2="552.6" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="522.4" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="308.0" y1="498.6" x2="308.0" y2="527.0" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="507.3" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="311.8" y1="499.0" x2="311.8" y2="521.5" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="499.6" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="315.6" y1="487.0" x2="315.6" y2="516.3" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="489.6" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="319.4" y1="491.5" x2="319.4" y2="522.0" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="494.8" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="323.1" y1="483.6" x2="323.1" y2="521.6" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="509.4" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="326.9" y1="514.7" x2="326.9" y2="529.8" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="518.1" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="330.7" y1="513.2" x2="330.7" y2="523.4" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="515.2" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="334.5" y1="488.3" x2="334.5" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="489.3" width="2.35" height="21.9" fill="var(--up)"/>
<line x1="338.3" y1="473.6" x2="338.3" y2="488.2" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="475.6" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="342.1" y1="470.6" x2="342.1" y2="490.0" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="472.3" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="345.9" y1="450.2" x2="345.9" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="453.9" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="349.6" y1="446.4" x2="349.6" y2="463.7" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="457.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="353.4" y1="451.2" x2="353.4" y2="467.5" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="461.0" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="357.2" y1="453.9" x2="357.2" y2="479.0" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="465.7" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="361.0" y1="477.2" x2="361.0" y2="490.1" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="483.1" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="364.8" y1="473.1" x2="364.8" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="473.7" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="368.6" y1="464.3" x2="368.6" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="473.3" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="372.4" y1="483.8" x2="372.4" y2="512.6" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="490.3" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="376.2" y1="469.9" x2="376.2" y2="491.7" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="480.8" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="379.9" y1="468.4" x2="379.9" y2="487.0" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="469.4" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="383.7" y1="457.5" x2="383.7" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="468.0" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="387.5" y1="444.7" x2="387.5" y2="472.3" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="447.2" width="2.35" height="21.9" fill="var(--up)"/>
<line x1="391.3" y1="443.2" x2="391.3" y2="455.2" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="447.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="395.1" y1="444.2" x2="395.1" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="446.6" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="398.9" y1="445.7" x2="398.9" y2="474.5" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="450.2" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="402.7" y1="445.1" x2="402.7" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="454.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="406.4" y1="446.3" x2="406.4" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="449.0" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="410.2" y1="447.6" x2="410.2" y2="483.4" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="449.0" width="2.35" height="21.5" fill="var(--down)"/>
<line x1="414.0" y1="456.9" x2="414.0" y2="493.5" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="460.7" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="417.8" y1="459.5" x2="417.8" y2="480.9" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="463.0" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="421.6" y1="458.1" x2="421.6" y2="480.0" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="460.4" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="425.4" y1="457.6" x2="425.4" y2="470.6" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="458.8" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="429.2" y1="436.1" x2="429.2" y2="467.9" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="438.2" width="2.35" height="20.8" fill="var(--up)"/>
<line x1="432.9" y1="431.7" x2="432.9" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="439.5" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="436.7" y1="419.4" x2="436.7" y2="440.8" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="423.5" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="440.5" y1="417.8" x2="440.5" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="423.6" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="444.3" y1="428.4" x2="444.3" y2="463.6" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="432.5" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="448.1" y1="426.7" x2="448.1" y2="444.0" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="434.3" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="451.9" y1="421.4" x2="451.9" y2="438.4" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="431.6" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="455.7" y1="423.1" x2="455.7" y2="443.9" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="429.8" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="459.5" y1="422.5" x2="459.5" y2="437.5" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="425.0" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="463.2" y1="408.7" x2="463.2" y2="424.9" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="410.7" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="467.0" y1="409.2" x2="467.0" y2="420.8" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="410.0" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="470.8" y1="405.6" x2="470.8" y2="434.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="412.7" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="474.6" y1="418.1" x2="474.6" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="429.2" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="478.4" y1="443.4" x2="478.4" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="443.7" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="482.2" y1="440.5" x2="482.2" y2="463.3" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="444.5" width="2.35" height="15.0" fill="var(--up)"/>
<line x1="486.0" y1="435.2" x2="486.0" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="437.7" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="489.7" y1="427.8" x2="489.7" y2="450.8" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="434.3" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="493.5" y1="435.6" x2="493.5" y2="462.7" stroke="var(--down)" class="wick"/>
<rect x="492.35" y="454.1" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="497.3" y1="417.9" x2="497.3" y2="457.5" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="422.4" width="2.35" height="29.6" fill="var(--up)"/>
<line x1="501.1" y1="418.0" x2="501.1" y2="429.2" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="418.1" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="504.9" y1="405.2" x2="504.9" y2="421.0" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="406.9" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="508.7" y1="393.6" x2="508.7" y2="417.2" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="394.6" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="512.5" y1="387.9" x2="512.5" y2="401.6" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="389.1" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="516.2" y1="386.6" x2="516.2" y2="400.2" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="390.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="520.0" y1="371.4" x2="520.0" y2="394.2" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="385.0" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="523.8" y1="376.7" x2="523.8" y2="387.5" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="383.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="527.6" y1="376.1" x2="527.6" y2="384.2" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="379.0" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="531.4" y1="376.1" x2="531.4" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="380.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="535.2" y1="363.8" x2="535.2" y2="380.0" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="369.1" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="539.0" y1="351.0" x2="539.0" y2="373.8" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="351.6" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="542.7" y1="346.5" x2="542.7" y2="365.4" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="348.2" width="2.35" height="11.1" fill="var(--down)"/>
<line x1="546.5" y1="328.1" x2="546.5" y2="362.5" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="335.4" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="550.3" y1="328.9" x2="550.3" y2="343.5" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="334.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="554.1" y1="325.1" x2="554.1" y2="346.8" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="331.8" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="557.9" y1="312.6" x2="557.9" y2="345.3" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="318.7" width="2.35" height="23.4" fill="var(--up)"/>
<line x1="561.7" y1="312.2" x2="561.7" y2="324.1" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="319.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="565.5" y1="320.3" x2="565.5" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="320.8" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="569.3" y1="304.6" x2="569.3" y2="333.3" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="320.2" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="573.0" y1="299.6" x2="573.0" y2="320.6" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="318.0" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="576.8" y1="317.3" x2="576.8" y2="335.9" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="320.2" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="580.6" y1="325.7" x2="580.6" y2="344.7" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="327.1" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="584.4" y1="333.2" x2="584.4" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="337.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="588.2" y1="333.5" x2="588.2" y2="358.4" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="333.5" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="592.0" y1="320.3" x2="592.0" y2="355.6" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="342.2" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="595.8" y1="342.4" x2="595.8" y2="363.0" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="347.9" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="599.5" y1="325.4" x2="599.5" y2="355.1" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="326.1" width="2.35" height="28.7" fill="var(--up)"/>
<line x1="603.3" y1="321.9" x2="603.3" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="324.3" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="607.1" y1="327.3" x2="607.1" y2="346.1" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="330.1" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="610.9" y1="342.4" x2="610.9" y2="358.5" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="343.0" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="614.7" y1="327.2" x2="614.7" y2="359.0" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="331.5" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="618.5" y1="331.8" x2="618.5" y2="355.8" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="332.9" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="622.3" y1="333.1" x2="622.3" y2="356.5" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="340.4" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="626.0" y1="327.0" x2="626.0" y2="376.6" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="340.2" width="2.35" height="33.3" fill="var(--down)"/>
<line x1="629.8" y1="352.5" x2="629.8" y2="376.5" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="353.0" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="633.6" y1="350.2" x2="633.6" y2="383.7" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="353.3" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="637.4" y1="344.6" x2="637.4" y2="368.7" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="365.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="641.2" y1="358.1" x2="641.2" y2="398.8" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="361.1" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="645.0" y1="359.2" x2="645.0" y2="383.5" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="362.8" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="648.8" y1="372.3" x2="648.8" y2="394.1" stroke="var(--down)" class="wick"/>
<rect x="647.59" y="376.1" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="652.5" y1="358.0" x2="652.5" y2="383.1" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="360.7" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="656.3" y1="355.2" x2="656.3" y2="366.3" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="360.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="660.1" y1="335.8" x2="660.1" y2="360.0" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="337.5" width="2.35" height="22.4" fill="var(--up)"/>
<line x1="663.9" y1="322.6" x2="663.9" y2="337.5" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="329.7" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="667.7" y1="305.4" x2="667.7" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="309.0" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="671.5" y1="294.2" x2="671.5" y2="320.6" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="307.2" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="675.3" y1="305.0" x2="675.3" y2="358.5" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="315.4" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="679.1" y1="330.5" x2="679.1" y2="345.7" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="333.4" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="682.8" y1="331.2" x2="682.8" y2="345.6" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="333.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="686.6" y1="299.4" x2="686.6" y2="333.3" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="300.5" width="2.35" height="29.9" fill="var(--up)"/>
<line x1="690.4" y1="301.0" x2="690.4" y2="326.0" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="303.2" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="694.2" y1="285.7" x2="694.2" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="300.2" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="698.0" y1="247.3" x2="698.0" y2="300.2" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="255.8" width="2.35" height="42.3" fill="var(--up)"/>
<line x1="701.8" y1="244.0" x2="701.8" y2="259.0" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="250.1" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="705.6" y1="244.1" x2="705.6" y2="260.1" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="250.5" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="709.3" y1="233.8" x2="709.3" y2="251.6" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="237.2" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="713.1" y1="231.1" x2="713.1" y2="253.4" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="232.4" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="716.9" y1="232.3" x2="716.9" y2="259.0" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="238.0" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="720.7" y1="220.2" x2="720.7" y2="251.5" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="230.3" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="724.5" y1="220.4" x2="724.5" y2="241.6" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="227.9" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="728.3" y1="225.2" x2="728.3" y2="245.1" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="237.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="732.1" y1="236.4" x2="732.1" y2="260.7" stroke="var(--down)" class="wick"/>
<rect x="730.89" y="237.3" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="735.8" y1="222.9" x2="735.8" y2="266.3" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="225.4" width="2.35" height="37.9" fill="var(--up)"/>
<line x1="739.6" y1="195.7" x2="739.6" y2="224.4" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="198.0" width="2.35" height="25.6" fill="var(--up)"/>
<line x1="743.4" y1="143.4" x2="743.4" y2="203.6" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="167.9" width="2.35" height="30.6" fill="var(--up)"/>
<line x1="747.2" y1="144.7" x2="747.2" y2="174.6" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="151.8" width="2.35" height="20.8" fill="var(--up)"/>
<line x1="751.0" y1="130.9" x2="751.0" y2="156.4" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="136.8" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="754.8" y1="128.2" x2="754.8" y2="153.2" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="137.1" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="758.6" y1="110.4" x2="758.6" y2="157.0" stroke="var(--up)" class="wick"/>
<rect x="757.39" y="113.8" width="2.35" height="36.1" fill="var(--up)"/>
<line x1="762.4" y1="103.8" x2="762.4" y2="174.8" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="113.0" width="2.35" height="45.8" fill="var(--down)"/>
<line x1="766.1" y1="159.6" x2="766.1" y2="207.9" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="172.7" width="2.35" height="21.1" fill="var(--down)"/>
<line x1="769.9" y1="166.8" x2="769.9" y2="199.1" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="183.8" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="773.7" y1="142.5" x2="773.7" y2="178.7" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="165.2" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="777.5" y1="141.9" x2="777.5" y2="244.8" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="174.3" width="2.35" height="67.9" fill="var(--down)"/>
<line x1="781.3" y1="180.4" x2="781.3" y2="278.8" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="189.7" width="2.35" height="81.2" fill="var(--up)"/>
<line x1="785.1" y1="173.6" x2="785.1" y2="202.5" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="181.9" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="788.9" y1="169.4" x2="788.9" y2="233.1" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="185.1" width="2.35" height="16.0" fill="var(--up)"/>
<line x1="792.6" y1="146.4" x2="792.6" y2="190.1" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="152.9" width="2.35" height="28.0" fill="var(--up)"/>
<line x1="796.4" y1="132.9" x2="796.4" y2="157.7" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="140.1" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="800.2" y1="104.7" x2="800.2" y2="143.8" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="107.5" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="804.0" y1="97.1" x2="804.0" y2="140.9" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="112.9" width="2.35" height="24.6" fill="var(--down)"/>
<line x1="807.8" y1="102.5" x2="807.8" y2="135.1" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="107.3" width="2.35" height="25.3" fill="var(--up)"/>
<line x1="811.6" y1="92.3" x2="811.6" y2="120.9" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="94.3" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="815.4" y1="80.6" x2="815.4" y2="159.6" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="95.4" width="2.35" height="43.9" fill="var(--down)"/>
<line x1="819.1" y1="120.2" x2="819.1" y2="185.8" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="129.9" width="2.35" height="46.4" fill="var(--down)"/>
<line x1="822.9" y1="134.9" x2="822.9" y2="183.9" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="150.3" width="2.35" height="28.8" fill="var(--up)"/>
<line x1="826.7" y1="123.4" x2="826.7" y2="149.1" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="123.7" width="2.35" height="24.6" fill="var(--up)"/>
<line x1="830.5" y1="121.7" x2="830.5" y2="161.2" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="123.6" width="2.35" height="28.5" fill="var(--down)"/>
<line x1="834.3" y1="141.6" x2="834.3" y2="159.6" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="149.1" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="838.1" y1="126.9" x2="838.1" y2="150.8" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="128.4" width="2.35" height="20.7" fill="var(--up)"/>
<line x1="841.9" y1="125.1" x2="841.9" y2="177.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="130.2" width="2.35" height="44.1" fill="var(--down)"/>
<line x1="845.6" y1="161.2" x2="845.6" y2="201.9" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="168.2" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="849.4" y1="150.9" x2="849.4" y2="186.8" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="161.0" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="853.2" y1="143.6" x2="853.2" y2="173.3" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="146.6" width="2.35" height="16.1" fill="var(--up)"/>
<line x1="857.0" y1="137.8" x2="857.0" y2="153.3" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="142.1" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="860.8" y1="139.9" x2="860.8" y2="172.1" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="148.5" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="864.6" y1="156.2" x2="864.6" y2="181.8" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="166.5" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="868.4" y1="156.5" x2="868.4" y2="189.5" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="168.4" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="872.2" y1="159.0" x2="872.2" y2="186.8" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="175.2" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="875.9" y1="138.5" x2="875.9" y2="184.1" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="147.1" width="2.35" height="32.3" fill="var(--up)"/>
<line x1="879.7" y1="133.7" x2="879.7" y2="164.2" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="146.7" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="883.5" y1="146.5" x2="883.5" y2="187.7" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="163.0" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="887.3" y1="147.6" x2="887.3" y2="175.3" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="153.5" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="891.1" y1="144.1" x2="891.1" y2="177.3" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="149.3" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="894.9" y1="167.1" x2="894.9" y2="188.9" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="170.0" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="898.7" y1="161.6" x2="898.7" y2="201.0" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="181.3" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="902.4" y1="189.8" x2="902.4" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="195.5" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="906.2" y1="182.8" x2="906.2" y2="208.9" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="187.0" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="910.0" y1="187.9" x2="910.0" y2="213.3" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="190.9" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="913.8" y1="147.1" x2="913.8" y2="212.2" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="152.3" width="2.35" height="46.5" fill="var(--up)"/>
<line x1="917.6" y1="146.9" x2="917.6" y2="163.1" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="148.6" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="921.4" y1="129.2" x2="921.4" y2="147.7" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="133.7" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="925.2" y1="129.7" x2="925.2" y2="163.6" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="132.5" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="928.9" y1="124.3" x2="928.9" y2="162.1" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="147.3" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="932.7" y1="155.7" x2="932.7" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="931.56" y="165.4" width="2.35" height="37.5" fill="var(--down)"/>
<line x1="936.5" y1="201.9" x2="936.5" y2="220.4" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="208.4" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="940.3" y1="189.8" x2="940.3" y2="220.3" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="203.7" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="944.1" y1="178.8" x2="944.1" y2="213.8" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="194.4" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="947.9" y1="191.2" x2="947.9" y2="243.0" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="196.5" width="2.35" height="43.2" fill="var(--down)"/>
<line x1="951.7" y1="218.3" x2="951.7" y2="238.9" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="221.9" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="955.5" y1="223.1" x2="955.5" y2="268.2" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="224.0" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="959.2" y1="209.5" x2="959.2" y2="244.4" stroke="var(--up)" class="wick"/>
<rect x="958.06" y="231.2" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="963.0" y1="231.8" x2="963.0" y2="260.6" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="241.4" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="966.8" y1="243.3" x2="966.8" y2="283.9" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="255.9" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="970.6" y1="254.2" x2="970.6" y2="290.9" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="262.8" width="2.35" height="25.1" fill="var(--down)"/>
<line x1="974.4" y1="263.1" x2="974.4" y2="292.1" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="274.2" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="978.2" y1="247.5" x2="978.2" y2="277.6" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="264.9" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="982.0" y1="225.9" x2="982.0" y2="270.2" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="232.1" width="2.35" height="33.9" fill="var(--up)"/>
<line x1="985.7" y1="230.8" x2="985.7" y2="264.6" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="233.7" width="2.35" height="18.1" fill="var(--down)"/>
<line x1="989.5" y1="167.5" x2="989.5" y2="260.5" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="203.6" width="2.35" height="53.2" fill="var(--up)"/>
<line x1="993.3" y1="199.0" x2="993.3" y2="234.4" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="203.7" width="2.35" height="23.9" fill="var(--down)"/>
<line x1="997.1" y1="201.1" x2="997.1" y2="229.6" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="209.5" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="1000.9" y1="185.1" x2="1000.9" y2="214.6" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="201.4" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="1004.7" y1="194.2" x2="1004.7" y2="222.1" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="207.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1008.5" y1="204.0" x2="1008.5" y2="252.9" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="205.6" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="1012.2" y1="206.5" x2="1012.2" y2="232.2" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="218.2" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="1016.0" y1="180.8" x2="1016.0" y2="217.3" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="205.7" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="1019.8" y1="172.7" x2="1019.8" y2="209.2" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="182.4" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="1023.6" y1="115.3" x2="1023.6" y2="177.1" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="115.3" width="2.35" height="61.8" fill="var(--up)"/>
<line x1="1027.4" y1="107.8" x2="1027.4" y2="161.1" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="113.0" width="2.35" height="36.4" fill="var(--down)"/>
<line x1="1031.2" y1="107.5" x2="1031.2" y2="149.0" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="124.5" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="1035.0" y1="113.0" x2="1035.0" y2="150.6" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="128.3" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="1038.7" y1="84.6" x2="1038.7" y2="132.5" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="104.9" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="1042.5" y1="88.6" x2="1042.5" y2="120.5" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="98.8" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="1046.3" y1="103.2" x2="1046.3" y2="125.2" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="110.0" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="1050.1" y1="103.2" x2="1050.1" y2="113.6" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="105.5" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="60" y1="92.2" x2="1052" y2="92.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="95.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$371 R1</text>
<text x="1058" y="107.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="192.4" x2="1052" y2="192.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="186.4" font-size="11.5" fill="var(--support)" font-weight="600">$332 S1</text>
<text x="1058" y="198.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="279.1" x2="1052" y2="279.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="273.1" font-size="11.5" fill="var(--support)" font-weight="600">$299 S2</text>
<text x="1058" y="285.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="493.3" x2="1052" y2="493.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="487.3" font-size="11.5" fill="var(--support)" font-weight="600">$216 S3</text>
<text x="1058" y="499.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="110.0" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고). `09_technical_daily.md`의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다 — 둘을 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $371 | 2 | 2025년 3월(3/3, $366.54)·6월(6/9, $375.51 — 5년 최고가) 스윙 고점 — FY2025 Q1·Q2 실적 발표 이후 랠리 구간 |
| **현재가** | **$364.15** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $332 | 3 | 2025년 6월(6/16)·8월(8/4)·9월(9/15) 스윙 저점 — DOJ 소송 이후 형성된 박스권 하단(2025년 여름 조정 국면) |
| S2 | $299 | 3 | 2025년 1월(1/13)·4월(4/7)·2026년 3월(3/30, $293.89 — 52주 최저) 스윙 저점대 |
| S3 | $216 | 2 | 2021년 9월(9/20)·2023년 5월(5/29) 스윙 저점 — 2022년 금리 인상기 약세장 이후 오랫동안 유지된 장기 구조적 지지 |

> 현재가 위쪽에는 유효한 클러스터가 R1 하나뿐이다 — 2026년 7월 말 실적 서프라이즈 이후 주가가 5년 최고가($375.51, 2025-06-09) 부근까지 회복했지만 그 위로 반복 터치된 스윙 고점이 아직 쌓이지 않았기 때문이다. 억지로 R2·R3를 채우지 않았다. 아래쪽 S1~S3(3개)는 스크립트 기본값(3개)과 동일해 조정하지 않았다.

---

## 3. 관측된 특이 구간 — 2024-09-23(주간) DOJ 반독점 소송(debit 시장 독점) 제기

- 2024-09-23(월) 장 마감 후 언론 보도로 미 법무부(DOJ)의 소송 준비 소식이 알려졌고, 2024-09-24(화) DOJ가 Visa를 상대로 직불카드(debit) 시장 독점 혐의 반독점 소송을 정식 제기했다. 관련 항목은 [`08_news.md`](./08_news.md)에 아직 로그로 남아 있지 않음(2024년 항목은 4분기 경과로 아카이브 대상) — 소송 자체는 [`07_investment.md`](./07_investment.md) §3 "반독점 소송" 리스크 서술에 포함.
- 일간 기준 전일(2024-09-23 종가 $288.63) 대비 **−5.5%**($288.63 → 2024-09-24 종가 $272.78)로 급락했고, 그 주(2024-09-23 주간 봉, 시가 $284.90 → 종가 $275.17) 전체로도 전주(종가 $284.77) 대비 약 −3.4% 하락했다. 이 사건 이후 2024년 4분기~2025년 초까지 $270~$310 박스권에서 등락하며 이전 추세선이 단절됐다.
- 이후 주가는 2025년 들어 완만히 회복해 2025년 3월·6월 R1 구간($366~$376)까지 올라섰다 — DOJ 소송이라는 구조적 리스크가 상존함에도 실적 성장이 주가 회복을 견인한 패턴으로 해석된다(펀더멘털 판단은 [`06_valuation.md`](./06_valuation.md)·[`07_investment.md`](./07_investment.md) 참고, 이 문서는 가격 패턴 서술에 한정).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-16~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영, 배당은 미반영 — 조사 기간 중 주식분할 없음, 배당은 20회 지급돼 배당락일 부근 미세한 하락은 가치 변동이 아닐 수 있음)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. `09_technical_daily.md`(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py V --name Visa --interval 1wk --event 2024-09-23:"DOJ 반독점 소송(debit 시장 독점) 제기" --close-on 2025-09-30 --close-on 2026-08-14 --emit all` (파라미터는 스크립트 기본값 그대로 사용 — 강제 레벨·기본값 변경 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 5년 구간 안에 사업 구조 자체가 바뀐 대형 M&A·사업부 매각·상장 형태 변경은 없었다 — 다만 2024-09 DOJ 소송(§3)이라는 구조적 법률 리스크 발생은 있었고, 그 이전 스윙 레벨(2024년 3~9월 저항대 $280~$293)은 이 사건 이후 레짐과 단절돼 §2에서 참고 레벨로도 포함하지 않았다(터치 부족으로 자연 제외).
    - 조사 기간(2021-08~2026-08) 내 주식분할·대규모 유상증자는 없었다 — 소급조정 이슈 없음.

---

## 관련 문서

같은 폴더 내 다른 문서로 이동:

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

- [Yahoo Finance — Visa Inc. (V) 주봉 시세](https://finance.yahoo.com/quote/V/history/) (수집 2026-08-16)
- [stockanalysis.com — Visa 주가 이력 API 교차 확인](https://stockanalysis.com/stocks/v/history/)
- [FXStreet — Visa sinks more than 5% on pending DOJ antitrust lawsuit (2024-09-24)](https://www.fxstreet.com/news/visa-sinks-more-than-5-on-pending-doj-antitrust-lawsuit-202409242114)

---

*작성일: 2026-08-16*
