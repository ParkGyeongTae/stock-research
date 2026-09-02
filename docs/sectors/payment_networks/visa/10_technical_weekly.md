# 기술적 분석 (주봉 캔들차트 · 5년 구조)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 단기 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: 2026-09-01 종가 **$372.67**은 [기술적 분석 — 일봉](./09_technical_daily.md)·[핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)의 값과 **일치**한다. 네 문서 모두 배당·분할 미반영 원주가 기준이다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-09-01)

<div class="v-chart">
<style>
.v-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .v-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-09-01 · 마지막 종가 $372.67 (2026-09-01) · 단위 USD</text>
<line x1="60" y1="539.3" x2="1052" y2="539.3" class="grid"/>
<text x="52" y="543.3" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="415.3" x2="1052" y2="415.3" class="grid"/>
<text x="52" y="419.3" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="291.4" x2="1052" y2="291.4" class="grid"/>
<text x="52" y="295.4" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="167.5" x2="1052" y2="167.5" class="grid"/>
<text x="52" y="171.5" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="129.8" y1="56.0" x2="129.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="129.8" y1="626.0" x2="129.8" y2="631.0" class="axis"/>
<text x="129.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="325.9" y1="56.0" x2="325.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="325.9" y1="626.0" x2="325.9" y2="631.0" class="axis"/>
<text x="325.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="522.1" y1="56.0" x2="522.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="522.1" y1="626.0" x2="522.1" y2="631.0" class="axis"/>
<text x="522.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="722.0" y1="56.0" x2="722.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="722.0" y1="626.0" x2="722.0" y2="631.0" class="axis"/>
<text x="722.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="918.1" y1="56.0" x2="918.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="918.1" y1="626.0" x2="918.1" y2="631.0" class="axis"/>
<text x="918.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="463.0" x2="61.9" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="467.1" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="65.7" y1="464.4" x2="65.7" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="473.0" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="69.4" y1="471.9" x2="69.4" y2="491.4" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="476.0" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="73.2" y1="460.1" x2="73.2" y2="498.8" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="461.0" width="2.34" height="36.3" fill="var(--up)"/>
<line x1="77.0" y1="456.7" x2="77.0" y2="483.2" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="460.7" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="80.7" y1="458.1" x2="80.7" y2="487.7" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="464.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="84.5" y1="462.2" x2="84.5" y2="493.1" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="462.5" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="88.3" y1="455.5" x2="88.3" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="461.9" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="92.1" y1="447.7" x2="92.1" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="456.4" width="2.34" height="53.7" fill="var(--down)"/>
<line x1="95.8" y1="495.6" x2="95.8" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="497.9" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="99.6" y1="485.7" x2="99.6" y2="514.1" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="493.7" width="2.34" height="15.6" fill="var(--down)"/>
<line x1="103.4" y1="498.6" x2="103.4" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="505.5" width="2.34" height="31.6" fill="var(--down)"/>
<line x1="107.1" y1="529.5" x2="107.1" y2="557.7" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="539.3" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="110.9" y1="536.2" x2="110.9" y2="563.8" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="536.8" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="114.7" y1="503.9" x2="114.7" y2="544.9" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="506.1" width="2.34" height="36.3" fill="var(--up)"/>
<line x1="118.5" y1="498.9" x2="118.5" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="508.4" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="122.2" y1="492.3" x2="122.2" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="498.1" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="126.0" y1="490.4" x2="126.0" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="495.4" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="129.8" y1="472.9" x2="129.8" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="495.8" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="133.6" y1="488.5" x2="133.6" y2="523.2" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="502.9" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="137.3" y1="490.7" x2="137.3" y2="524.8" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="499.9" width="2.34" height="24.7" fill="var(--down)"/>
<line x1="141.1" y1="469.6" x2="141.1" y2="550.0" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="469.9" width="2.34" height="64.0" fill="var(--up)"/>
<line x1="144.9" y1="450.4" x2="144.9" y2="484.6" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="468.9" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="148.6" y1="457.1" x2="148.6" y2="480.9" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="469.9" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="152.4" y1="465.2" x2="152.4" y2="485.1" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="481.5" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="156.2" y1="478.9" x2="156.2" y2="535.7" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="487.2" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="160.0" y1="493.0" x2="160.0" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="499.6" width="2.34" height="38.9" fill="var(--down)"/>
<line x1="163.7" y1="537.2" x2="163.7" y2="572.3" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="539.7" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="167.5" y1="491.5" x2="167.5" y2="543.8" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="491.9" width="2.34" height="51.3" fill="var(--up)"/>
<line x1="171.3" y1="490.8" x2="171.3" y2="504.6" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="493.6" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="175.0" y1="467.9" x2="175.0" y2="495.9" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="473.9" width="2.34" height="19.5" fill="var(--up)"/>
<line x1="178.8" y1="466.8" x2="178.8" y2="506.8" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="475.4" width="2.34" height="21.8" fill="var(--down)"/>
<line x1="182.6" y1="496.4" x2="182.6" y2="521.5" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="501.5" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="186.4" y1="480.0" x2="186.4" y2="519.6" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="510.3" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="190.1" y1="477.5" x2="190.1" y2="536.5" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="506.7" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="193.9" y1="502.6" x2="193.9" y2="538.7" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="510.1" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="197.7" y1="537.4" x2="197.7" y2="564.2" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="539.1" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="201.4" y1="525.7" x2="201.4" y2="555.8" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="541.7" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="205.2" y1="506.5" x2="205.2" y2="541.7" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="507.3" width="2.34" height="29.7" fill="var(--up)"/>
<line x1="209.0" y1="501.5" x2="209.0" y2="517.4" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="507.9" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="212.8" y1="495.7" x2="212.8" y2="541.3" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="501.0" width="2.34" height="39.5" fill="var(--down)"/>
<line x1="216.5" y1="542.2" x2="216.5" y2="574.2" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="556.6" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="220.3" y1="525.3" x2="220.3" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="525.6" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="224.1" y1="521.7" x2="224.1" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="525.0" width="2.34" height="16.3" fill="var(--down)"/>
<line x1="227.8" y1="529.1" x2="227.8" y2="553.8" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="530.4" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="231.6" y1="510.2" x2="231.6" y2="544.3" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="514.4" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="235.4" y1="494.5" x2="235.4" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="505.3" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="239.2" y1="497.5" x2="239.2" y2="536.3" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="503.1" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="242.9" y1="499.7" x2="242.9" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="499.9" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="246.7" y1="498.0" x2="246.7" y2="515.1" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="501.5" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="250.5" y1="495.6" x2="250.5" y2="513.6" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="507.5" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="254.3" y1="511.4" x2="254.3" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="514.6" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="258.0" y1="528.3" x2="258.0" y2="547.5" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="536.2" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="261.8" y1="523.4" x2="261.8" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="526.4" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="265.6" y1="521.4" x2="265.6" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="523.2" width="2.34" height="32.7" fill="var(--down)"/>
<line x1="269.3" y1="554.2" x2="269.3" y2="583.3" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="560.1" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="273.1" y1="576.8" x2="273.1" y2="601.6" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="581.3" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="276.9" y1="567.0" x2="276.9" y2="593.4" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="579.3" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="280.7" y1="571.2" x2="280.7" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="578.6" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="284.4" y1="561.6" x2="284.4" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="563.1" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="288.2" y1="510.7" x2="288.2" y2="566.3" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="516.1" width="2.34" height="44.4" fill="var(--up)"/>
<line x1="292.0" y1="514.6" x2="292.0" y2="553.7" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="517.2" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="295.7" y1="523.3" x2="295.7" y2="555.8" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="526.9" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="299.5" y1="504.1" x2="299.5" y2="531.3" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="512.5" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="303.3" y1="504.6" x2="303.3" y2="526.0" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="505.1" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="307.1" y1="493.0" x2="307.1" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="495.5" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="310.8" y1="497.4" x2="310.8" y2="526.5" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="500.5" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="314.6" y1="489.7" x2="314.6" y2="526.1" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="514.5" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="318.4" y1="519.5" x2="318.4" y2="534.0" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="522.8" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="322.1" y1="518.1" x2="322.1" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="520.0" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="325.9" y1="494.3" x2="325.9" y2="524.0" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="495.3" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="329.7" y1="480.3" x2="329.7" y2="494.2" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="482.1" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="333.5" y1="477.3" x2="333.5" y2="495.9" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="479.0" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="337.2" y1="457.9" x2="337.2" y2="498.0" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="461.3" width="2.34" height="17.0" fill="var(--up)"/>
<line x1="341.0" y1="454.3" x2="341.0" y2="470.8" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="464.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="344.8" y1="458.8" x2="344.8" y2="474.4" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="468.1" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="348.5" y1="461.4" x2="348.5" y2="485.4" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="472.6" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="352.3" y1="483.6" x2="352.3" y2="496.0" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="489.3" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="356.1" y1="479.7" x2="356.1" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="480.4" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="359.9" y1="471.3" x2="359.9" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="480.0" width="2.34" height="19.3" fill="var(--down)"/>
<line x1="363.6" y1="490.0" x2="363.6" y2="517.6" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="496.2" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="367.4" y1="476.7" x2="367.4" y2="497.5" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="487.1" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="371.2" y1="475.2" x2="371.2" y2="493.0" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="476.2" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="375.0" y1="464.8" x2="375.0" y2="479.5" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="474.9" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="378.7" y1="452.5" x2="378.7" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="455.0" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="382.5" y1="451.1" x2="382.5" y2="462.6" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="454.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="386.3" y1="452.2" x2="386.3" y2="473.3" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="454.4" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="390.0" y1="453.5" x2="390.0" y2="481.1" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="457.8" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="393.8" y1="453.0" x2="393.8" y2="469.2" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="461.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="397.6" y1="454.2" x2="397.6" y2="465.8" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="456.7" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="401.4" y1="455.3" x2="401.4" y2="489.6" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="456.7" width="2.34" height="20.6" fill="var(--down)"/>
<line x1="405.1" y1="464.2" x2="405.1" y2="499.3" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="467.9" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="408.9" y1="466.8" x2="408.9" y2="487.2" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="470.1" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="412.7" y1="465.4" x2="412.7" y2="486.3" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="467.6" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="416.4" y1="465.0" x2="416.4" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="466.0" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="420.2" y1="444.4" x2="420.2" y2="474.8" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="446.4" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="424.0" y1="440.1" x2="424.0" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="447.6" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="427.8" y1="428.4" x2="427.8" y2="448.8" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="432.3" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="431.5" y1="426.8" x2="431.5" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="432.4" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="435.3" y1="437.0" x2="435.3" y2="470.7" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="440.9" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="439.1" y1="435.4" x2="439.1" y2="451.9" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="442.6" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="442.8" y1="430.3" x2="442.8" y2="446.6" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="440.0" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="446.6" y1="431.9" x2="446.6" y2="451.8" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="438.3" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="450.4" y1="431.3" x2="450.4" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="433.8" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="454.2" y1="418.1" x2="454.2" y2="433.7" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="420.0" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="457.9" y1="418.6" x2="457.9" y2="429.7" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="419.4" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="461.7" y1="415.2" x2="461.7" y2="443.2" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="422.0" width="2.34" height="15.5" fill="var(--down)"/>
<line x1="465.5" y1="427.2" x2="465.5" y2="452.8" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="437.8" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="469.2" y1="451.4" x2="469.2" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="451.6" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="473.0" y1="448.6" x2="473.0" y2="470.4" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="452.4" width="2.34" height="14.4" fill="var(--up)"/>
<line x1="476.8" y1="443.5" x2="476.8" y2="460.7" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="445.9" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="480.6" y1="436.5" x2="480.6" y2="458.4" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="442.6" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="484.3" y1="443.9" x2="484.3" y2="469.8" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="461.5" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="488.1" y1="426.9" x2="488.1" y2="464.8" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="431.2" width="2.34" height="28.3" fill="var(--up)"/>
<line x1="491.9" y1="427.1" x2="491.9" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="427.1" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="495.7" y1="414.8" x2="495.7" y2="429.9" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="416.4" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="499.4" y1="403.7" x2="499.4" y2="426.3" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="404.7" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="503.2" y1="398.2" x2="503.2" y2="411.4" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="399.4" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="507.0" y1="397.0" x2="507.0" y2="410.0" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="400.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="510.7" y1="382.5" x2="510.7" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="395.4" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="514.5" y1="387.6" x2="514.5" y2="397.9" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="393.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="518.3" y1="386.9" x2="518.3" y2="394.8" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="389.7" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="522.1" y1="386.9" x2="522.1" y2="398.3" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="391.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="525.8" y1="375.2" x2="525.8" y2="390.7" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="380.2" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="529.6" y1="362.9" x2="529.6" y2="384.7" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="363.6" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="533.4" y1="358.7" x2="533.4" y2="376.7" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="360.2" width="2.34" height="10.7" fill="var(--down)"/>
<line x1="537.1" y1="341.0" x2="537.1" y2="373.9" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="348.0" width="2.34" height="25.3" fill="var(--up)"/>
<line x1="540.9" y1="341.8" x2="540.9" y2="355.8" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="347.4" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="544.7" y1="338.2" x2="544.7" y2="358.9" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="344.6" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="548.5" y1="326.3" x2="548.5" y2="357.5" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="332.1" width="2.34" height="22.4" fill="var(--up)"/>
<line x1="552.2" y1="325.8" x2="552.2" y2="337.2" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="333.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="556.0" y1="333.6" x2="556.0" y2="350.5" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="334.0" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="559.8" y1="318.6" x2="559.8" y2="346.0" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="333.5" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="563.5" y1="313.8" x2="563.5" y2="333.8" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="331.4" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="567.3" y1="330.8" x2="567.3" y2="348.5" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="333.5" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="571.1" y1="338.8" x2="571.1" y2="357.0" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="340.1" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="574.9" y1="346.0" x2="574.9" y2="360.4" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="350.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="578.6" y1="346.2" x2="578.6" y2="370.0" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="346.2" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="582.4" y1="333.6" x2="582.4" y2="367.4" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="354.6" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="586.2" y1="354.7" x2="586.2" y2="374.5" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="360.0" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="589.9" y1="338.4" x2="589.9" y2="366.8" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="339.2" width="2.34" height="27.5" fill="var(--up)"/>
<line x1="593.7" y1="335.1" x2="593.7" y2="355.2" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="337.4" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="597.5" y1="340.3" x2="597.5" y2="358.3" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="342.9" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="601.3" y1="354.7" x2="601.3" y2="370.1" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="355.3" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="605.0" y1="340.2" x2="605.0" y2="370.6" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="344.3" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="608.8" y1="344.6" x2="608.8" y2="367.6" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="345.6" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="612.6" y1="345.9" x2="612.6" y2="368.3" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="352.8" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="616.3" y1="340.0" x2="616.3" y2="387.5" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="352.6" width="2.34" height="31.8" fill="var(--down)"/>
<line x1="620.1" y1="364.4" x2="620.1" y2="387.3" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="364.9" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="623.9" y1="362.2" x2="623.9" y2="394.3" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="365.2" width="2.34" height="11.2" fill="var(--down)"/>
<line x1="627.7" y1="356.8" x2="627.7" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="376.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="631.4" y1="369.7" x2="631.4" y2="408.7" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="372.6" width="2.34" height="19.3" fill="var(--down)"/>
<line x1="635.2" y1="370.8" x2="635.2" y2="394.1" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="374.3" width="2.34" height="15.5" fill="var(--up)"/>
<line x1="639.0" y1="383.3" x2="639.0" y2="404.2" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="387.0" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="642.8" y1="369.6" x2="642.8" y2="393.7" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="372.3" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="646.5" y1="367.0" x2="646.5" y2="377.6" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="372.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="650.3" y1="348.5" x2="650.3" y2="371.6" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="350.0" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="654.1" y1="335.8" x2="654.1" y2="350.0" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="342.6" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="657.8" y1="319.3" x2="657.8" y2="345.2" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="322.8" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="661.6" y1="308.6" x2="661.6" y2="333.9" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="321.1" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="665.4" y1="319.0" x2="665.4" y2="370.2" stroke="var(--down)" class="wick"/>
<rect x="664.21" y="328.9" width="2.34" height="24.1" fill="var(--down)"/>
<line x1="669.2" y1="343.3" x2="669.2" y2="357.9" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="346.1" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="672.9" y1="344.0" x2="672.9" y2="357.8" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="346.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="676.7" y1="313.6" x2="676.7" y2="346.0" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="314.7" width="2.34" height="28.6" fill="var(--up)"/>
<line x1="680.5" y1="315.1" x2="680.5" y2="339.1" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="317.2" width="2.34" height="19.5" fill="var(--down)"/>
<line x1="684.2" y1="300.5" x2="684.2" y2="337.7" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="314.4" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="688.0" y1="263.8" x2="688.0" y2="314.3" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="271.9" width="2.34" height="40.4" fill="var(--up)"/>
<line x1="691.8" y1="260.6" x2="691.8" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="266.4" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="695.6" y1="260.7" x2="695.6" y2="276.0" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="266.9" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="699.3" y1="250.9" x2="699.3" y2="267.9" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="254.1" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="703.1" y1="248.3" x2="703.1" y2="269.6" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="249.6" width="2.34" height="14.6" fill="var(--down)"/>
<line x1="706.9" y1="249.4" x2="706.9" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="254.9" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="710.6" y1="237.9" x2="710.6" y2="267.7" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="247.5" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="714.4" y1="238.1" x2="714.4" y2="258.3" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="245.2" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="718.2" y1="242.7" x2="718.2" y2="261.7" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="254.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="722.0" y1="253.3" x2="722.0" y2="276.6" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="254.2" width="2.34" height="18.1" fill="var(--down)"/>
<line x1="725.7" y1="240.4" x2="725.7" y2="281.9" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="242.8" width="2.34" height="36.2" fill="var(--up)"/>
<line x1="729.5" y1="214.4" x2="729.5" y2="241.9" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="216.6" width="2.34" height="24.5" fill="var(--up)"/>
<line x1="733.3" y1="164.4" x2="733.3" y2="221.9" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="187.8" width="2.34" height="29.2" fill="var(--up)"/>
<line x1="737.0" y1="165.7" x2="737.0" y2="194.2" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="172.4" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="740.8" y1="152.5" x2="740.8" y2="176.8" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="158.1" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="744.6" y1="149.8" x2="744.6" y2="173.8" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="158.4" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="748.4" y1="132.8" x2="748.4" y2="177.4" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="136.0" width="2.34" height="34.6" fill="var(--up)"/>
<line x1="752.1" y1="126.5" x2="752.1" y2="194.4" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="135.3" width="2.34" height="43.8" fill="var(--down)"/>
<line x1="755.9" y1="179.9" x2="755.9" y2="226.1" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="192.5" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="759.7" y1="186.8" x2="759.7" y2="217.7" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="203.1" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="763.5" y1="163.5" x2="763.5" y2="198.1" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="185.2" width="2.34" height="10.4" fill="var(--up)"/>
<line x1="767.2" y1="162.9" x2="767.2" y2="261.4" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="193.9" width="2.34" height="65.0" fill="var(--down)"/>
<line x1="771.0" y1="199.8" x2="771.0" y2="293.9" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="208.7" width="2.34" height="77.6" fill="var(--up)"/>
<line x1="774.8" y1="193.3" x2="774.8" y2="221.0" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="201.2" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="778.5" y1="189.2" x2="778.5" y2="250.2" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="204.3" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="782.3" y1="167.3" x2="782.3" y2="209.1" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="173.5" width="2.34" height="26.8" fill="var(--up)"/>
<line x1="786.1" y1="154.3" x2="786.1" y2="178.0" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="161.2" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="789.9" y1="127.4" x2="789.9" y2="164.7" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="130.1" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="793.6" y1="120.1" x2="793.6" y2="162.0" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="135.3" width="2.34" height="23.5" fill="var(--down)"/>
<line x1="797.4" y1="125.3" x2="797.4" y2="156.4" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="129.9" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="801.2" y1="115.5" x2="801.2" y2="142.8" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="117.4" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="804.9" y1="104.3" x2="804.9" y2="179.9" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="118.5" width="2.34" height="42.0" fill="var(--down)"/>
<line x1="808.7" y1="142.2" x2="808.7" y2="204.9" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="151.4" width="2.34" height="44.4" fill="var(--down)"/>
<line x1="812.5" y1="156.2" x2="812.5" y2="203.1" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="171.0" width="2.34" height="27.5" fill="var(--up)"/>
<line x1="816.3" y1="145.2" x2="816.3" y2="169.9" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="145.6" width="2.34" height="23.6" fill="var(--up)"/>
<line x1="820.0" y1="143.6" x2="820.0" y2="181.4" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="145.4" width="2.34" height="27.2" fill="var(--down)"/>
<line x1="823.8" y1="162.6" x2="823.8" y2="179.9" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="169.9" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="827.6" y1="148.6" x2="827.6" y2="171.5" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="150.1" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="831.3" y1="146.9" x2="831.3" y2="197.0" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="151.7" width="2.34" height="42.2" fill="var(--down)"/>
<line x1="835.1" y1="181.4" x2="835.1" y2="220.3" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="188.1" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="838.9" y1="171.6" x2="838.9" y2="205.9" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="181.2" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="842.7" y1="164.5" x2="842.7" y2="193.0" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="167.4" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="846.4" y1="159.0" x2="846.4" y2="173.8" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="163.1" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="850.2" y1="161.0" x2="850.2" y2="191.8" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="169.2" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="854.0" y1="176.6" x2="854.0" y2="201.1" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="186.5" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="857.7" y1="176.9" x2="857.7" y2="208.5" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="188.3" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="861.5" y1="179.3" x2="861.5" y2="205.9" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="194.8" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="865.3" y1="159.7" x2="865.3" y2="203.3" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="167.9" width="2.34" height="30.9" fill="var(--up)"/>
<line x1="869.1" y1="155.1" x2="869.1" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="167.5" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="872.8" y1="167.3" x2="872.8" y2="206.8" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="183.1" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="876.6" y1="168.4" x2="876.6" y2="194.9" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="174.0" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="880.4" y1="165.1" x2="880.4" y2="196.8" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="170.0" width="2.34" height="20.5" fill="var(--down)"/>
<line x1="884.2" y1="187.1" x2="884.2" y2="207.9" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="189.8" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="887.9" y1="181.7" x2="887.9" y2="219.5" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="200.6" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="891.7" y1="208.8" x2="891.7" y2="246.8" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="214.2" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="895.5" y1="202.1" x2="895.5" y2="227.0" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="206.1" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="899.2" y1="206.9" x2="899.2" y2="231.3" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="209.8" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="903.0" y1="167.9" x2="903.0" y2="230.2" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="172.9" width="2.34" height="44.5" fill="var(--up)"/>
<line x1="906.8" y1="167.7" x2="906.8" y2="183.2" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="169.4" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="910.6" y1="150.8" x2="910.6" y2="168.5" stroke="var(--up)" class="wick"/>
<rect x="909.39" y="155.1" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="914.3" y1="151.3" x2="914.3" y2="183.7" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="153.9" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="918.1" y1="146.2" x2="918.1" y2="182.3" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="168.1" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="921.9" y1="176.2" x2="921.9" y2="232.4" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="185.4" width="2.34" height="35.9" fill="var(--down)"/>
<line x1="925.6" y1="220.4" x2="925.6" y2="238.0" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="226.6" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="929.4" y1="208.8" x2="929.4" y2="237.9" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="222.0" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="933.2" y1="198.3" x2="933.2" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="213.2" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="937.0" y1="210.1" x2="937.0" y2="259.7" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="215.2" width="2.34" height="41.3" fill="var(--down)"/>
<line x1="940.7" y1="236.0" x2="940.7" y2="255.7" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="239.5" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="944.5" y1="240.6" x2="944.5" y2="283.8" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="241.5" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="948.3" y1="227.6" x2="948.3" y2="261.0" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="248.4" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="952.0" y1="249.0" x2="952.0" y2="276.5" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="258.1" width="2.34" height="15.7" fill="var(--down)"/>
<line x1="955.8" y1="260.0" x2="955.8" y2="298.8" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="272.0" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="959.6" y1="270.4" x2="959.6" y2="305.5" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="278.5" width="2.34" height="24.0" fill="var(--down)"/>
<line x1="963.4" y1="278.9" x2="963.4" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="289.5" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="967.1" y1="264.0" x2="967.1" y2="292.8" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="280.6" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="970.9" y1="243.3" x2="970.9" y2="285.6" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="249.3" width="2.34" height="32.4" fill="var(--up)"/>
<line x1="974.7" y1="247.9" x2="974.7" y2="280.3" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="250.8" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="978.4" y1="187.4" x2="978.4" y2="276.4" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="222.0" width="2.34" height="50.9" fill="var(--up)"/>
<line x1="982.2" y1="217.6" x2="982.2" y2="251.4" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="222.0" width="2.34" height="22.8" fill="var(--down)"/>
<line x1="986.0" y1="219.5" x2="986.0" y2="246.8" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="227.6" width="2.34" height="16.5" fill="var(--up)"/>
<line x1="989.8" y1="204.3" x2="989.8" y2="232.5" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="219.9" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="993.5" y1="212.9" x2="993.5" y2="239.6" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="225.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="997.3" y1="222.4" x2="997.3" y2="269.1" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="223.9" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="1001.1" y1="224.8" x2="1001.1" y2="249.3" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="235.9" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="1004.9" y1="200.2" x2="1004.9" y2="235.1" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="223.9" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="1008.6" y1="192.5" x2="1008.6" y2="227.3" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="201.6" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="1012.4" y1="137.5" x2="1012.4" y2="196.6" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="137.5" width="2.34" height="59.1" fill="var(--up)"/>
<line x1="1016.2" y1="130.3" x2="1016.2" y2="181.4" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="135.3" width="2.34" height="34.8" fill="var(--down)"/>
<line x1="1019.9" y1="130.0" x2="1019.9" y2="169.7" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="146.3" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="1023.7" y1="135.3" x2="1023.7" y2="171.2" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="149.9" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="1027.5" y1="108.1" x2="1027.5" y2="153.9" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="127.5" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="1031.3" y1="112.0" x2="1031.3" y2="142.5" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="121.7" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="1035.0" y1="125.9" x2="1035.0" y2="146.9" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="132.5" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="1038.8" y1="113.5" x2="1038.8" y2="147.6" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="115.4" width="2.34" height="20.3" fill="var(--up)"/>
<line x1="1042.6" y1="79.4" x2="1042.6" y2="112.5" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="94.0" width="2.34" height="15.9" fill="var(--up)"/>
<line x1="1046.3" y1="87.0" x2="1046.3" y2="112.5" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="89.8" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="1050.1" y1="91.3" x2="1050.1" y2="112.5" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="94.0" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="60" y1="211.2" x2="1052" y2="211.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="205.2" font-size="11.5" fill="var(--support)" font-weight="600">$332 S1</text>
<text x="1058" y="217.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="294.1" x2="1052" y2="294.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="288.1" font-size="11.5" fill="var(--support)" font-weight="600">$299 S2</text>
<text x="1058" y="300.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="568.6" x2="1052" y2="568.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="562.6" font-size="11.5" fill="var(--support)" font-weight="600">$188 S3</text>
<text x="1058" y="574.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="111.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="103.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $373 (2026-09-01)</text>
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
| **현재가** | **$372.67** (2026-09-01 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $332 | 3 | 2025-06-16·2025-08-04·2025-09-15 주의 스윙 저점대. 일봉 S2($334)와 사실상 같은 가격대로, 두 인터벌이 서로를 확인해준다 |
| S2 | $299 | 3 | 2025-01-13·2025-04-07·2026-03-30 주의 스윙 저점대. 2026-03-27 종가 $295.52(최근 1년 최저)가 이 대에서 잡혔고, 2026-04-29 실적 갭 상승의 출발점이기도 하다 |
| S3 | $188 | 4 | 2021-11-29·2022-03-07·2022-05-09·2022-06-13 주의 스윙 저점대 — **2022년 하락장 바닥권**이다. 현재가에서 −50% 아래에 있어 근시일 지지로 볼 성격이 아니고, 5년 구조에서 어디까지 밀렸었는지를 보는 참조점으로만 읽을 것 |

---

## 3. 관측된 특이 구간 — 2022년 하락장과 그 이후의 레짐 전환

- 2021-11 ~ 2022-06 사이 주가는 $250권에서 $174.60(기간 내 최저)까지 밀렸다. 금리 급등기의 성장주 디레이팅과 크로스보더 회복 지연이 겹친 구간으로, S3($188) 클러스터가 이때 형성됐다.
- 그 이후로는 방향이 한 번도 뒤집히지 않았다 — 2022년 저점 이후 2026-09-01까지 4년간 주가는 두 배 이상 올랐고, 5년 차트에서 확인되는 조정은 모두 상승 추세 안의 눌림목(S1·S2)이다.
- 이 레짐 차이 때문에 S3는 S1·S2와 성격이 다르다. S1·S2는 현재 추세 안에서 실제로 시험된 지지대이지만, S3는 **다른 밸류에이션 국면에서 만들어진 가격**이다(당시 Non-GAAP PER은 20배대 중반, 현재는 29.2배 — [핵심 지표](./04_metrics.md) A.2).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-30~2026-09-01. 수집 시점: 2026-09-02. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py V --name "Visa" --interval 1wk --close-on 2026-09-01 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간대로 S3($188)는 2022년 하락장에서 형성된 레벨이라 현재 국면의 지지로 해석하지 않는다 — 스크립트는 터치 횟수만 세므로 이 구분을 하지 못한다.
    - 표시 기간(2021-08-30~2026-09-01)에 주식분할·유상증자 등 가격 연속성을 깨는 이벤트는 없었다(마지막 분할은 2015-03). 배당은 기간 내 20회 지급됐으나 원주가라 반영되지 않았다.
    - 2026-05 Class B-1/B-2 교환공개매수는 Class A 주가에 직접적인 연속성 단절을 일으키지 않았다(Class A 주식수·주가에 소급 조정 없음).

---

*작성일: 2026-09-02*
