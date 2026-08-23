# 기술적 분석 (주봉 캔들차트 · 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 최근 1년의 단기 구조는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: 2026-08-21 종가 **$277.51**은 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 및 [밸류에이션 / 적정주가](./06_valuation.md)의 값과 **일치**한다. 원주가(배당 미반영) 기준이다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-21)

<div class="lng-chart">
<style>
.lng-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .lng-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .lng-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.lng-chart svg { width:100%; height:auto; display:block; }
.lng-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.lng-chart .title { fill: var(--ink); font-weight:600; }
.lng-chart .grid { stroke: var(--grid); stroke-width:1; }
.lng-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cheniere Energy(LNG) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Cheniere Energy (LNG) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 $277.51 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="565.4" x2="1052" y2="565.4" class="grid"/>
<text x="52" y="569.4" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="444.1" x2="1052" y2="444.1" class="grid"/>
<text x="52" y="448.1" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="322.8" x2="1052" y2="322.8" class="grid"/>
<text x="52" y="326.8" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="201.5" x2="1052" y2="201.5" class="grid"/>
<text x="52" y="205.5" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="80.3" x2="1052" y2="80.3" class="grid"/>
<text x="52" y="84.3" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
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
<line x1="61.9" y1="590.1" x2="61.9" y2="601.7" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="590.3" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="65.7" y1="586.6" x2="65.7" y2="599.2" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="589.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="69.5" y1="584.5" x2="69.5" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="594.3" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="73.3" y1="584.1" x2="73.3" y2="597.6" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="591.7" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="77.0" y1="577.5" x2="77.0" y2="603.7" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="578.3" width="2.35" height="24.6" fill="var(--up)"/>
<line x1="80.8" y1="565.3" x2="80.8" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="568.2" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="84.6" y1="554.4" x2="84.6" y2="572.6" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="562.9" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="88.4" y1="538.4" x2="88.4" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="539.9" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="92.2" y1="532.9" x2="92.2" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="536.1" width="2.35" height="16.5" fill="var(--down)"/>
<line x1="96.0" y1="543.1" x2="96.0" y2="558.6" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="545.2" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="99.8" y1="545.4" x2="99.8" y2="556.4" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="546.4" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="103.5" y1="540.3" x2="103.5" y2="559.1" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="540.3" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="107.3" y1="547.5" x2="107.3" y2="561.8" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="555.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="111.1" y1="542.9" x2="111.1" y2="559.3" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="548.6" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="114.9" y1="541.2" x2="114.9" y2="565.3" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="543.2" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="118.7" y1="543.5" x2="118.7" y2="562.5" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="555.6" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="122.5" y1="553.9" x2="122.5" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="559.2" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="126.3" y1="549.4" x2="126.3" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="555.8" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="130.0" y1="553.7" x2="130.0" y2="563.5" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="553.9" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="133.8" y1="540.5" x2="133.8" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="544.7" width="2.35" height="16.0" fill="var(--up)"/>
<line x1="137.6" y1="527.2" x2="137.6" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="533.8" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="141.4" y1="527.7" x2="141.4" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="529.6" width="2.35" height="24.7" fill="var(--down)"/>
<line x1="145.2" y1="531.7" x2="145.2" y2="565.0" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="534.2" width="2.35" height="23.9" fill="var(--up)"/>
<line x1="149.0" y1="521.9" x2="149.0" y2="539.5" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="530.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="152.8" y1="513.7" x2="152.8" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="516.3" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="156.5" y1="515.9" x2="156.5" y2="536.0" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="518.1" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="160.3" y1="469.6" x2="160.3" y2="530.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="494.4" width="2.35" height="19.3" fill="var(--up)"/>
<line x1="164.1" y1="468.5" x2="164.1" y2="494.9" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="469.2" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="167.9" y1="460.1" x2="167.9" y2="496.8" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="463.5" width="2.35" height="30.4" fill="var(--down)"/>
<line x1="171.7" y1="486.6" x2="171.7" y2="509.8" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="488.1" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="175.5" y1="445.5" x2="175.5" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="445.8" width="2.35" height="34.2" fill="var(--up)"/>
<line x1="179.3" y1="454.5" x2="179.3" y2="487.4" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="454.8" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="183.1" y1="456.3" x2="183.1" y2="469.0" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="458.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="186.8" y1="461.7" x2="186.8" y2="482.6" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="463.6" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="190.6" y1="462.0" x2="190.6" y2="482.1" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="468.4" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="194.4" y1="460.2" x2="194.4" y2="498.7" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="478.5" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="198.2" y1="444.1" x2="198.2" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="450.7" width="2.35" height="30.0" fill="var(--up)"/>
<line x1="202.0" y1="454.0" x2="202.0" y2="498.0" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="455.1" width="2.35" height="24.1" fill="var(--down)"/>
<line x1="205.8" y1="468.9" x2="205.8" y2="498.7" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="478.1" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="209.6" y1="470.4" x2="209.6" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="472.4" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="213.3" y1="458.4" x2="213.3" y2="482.6" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="463.6" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="217.1" y1="452.9" x2="217.1" y2="483.8" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="462.0" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="220.9" y1="478.9" x2="220.9" y2="516.6" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="489.6" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="224.7" y1="480.9" x2="224.7" y2="507.1" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="500.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="228.5" y1="474.4" x2="228.5" y2="498.9" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="487.9" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="232.3" y1="485.6" x2="232.3" y2="511.8" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="492.8" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="236.1" y1="500.2" x2="236.1" y2="516.1" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="501.1" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="239.8" y1="472.0" x2="239.8" y2="505.1" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="482.7" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="243.6" y1="442.6" x2="243.6" y2="479.8" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="445.1" width="2.35" height="33.1" fill="var(--up)"/>
<line x1="247.4" y1="447.7" x2="247.4" y2="463.5" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="449.3" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="251.2" y1="423.0" x2="251.2" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="423.0" width="2.35" height="28.1" fill="var(--up)"/>
<line x1="255.0" y1="400.6" x2="255.0" y2="437.9" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="405.6" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="258.8" y1="390.1" x2="258.8" y2="407.3" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="401.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="262.6" y1="400.2" x2="262.6" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="406.4" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="266.4" y1="401.0" x2="266.4" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="405.6" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="270.1" y1="374.7" x2="270.1" y2="420.4" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="402.2" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="273.9" y1="394.4" x2="273.9" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="412.2" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="277.7" y1="395.3" x2="277.7" y2="449.7" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="405.5" width="2.35" height="27.7" fill="var(--up)"/>
<line x1="281.5" y1="378.4" x2="281.5" y2="406.2" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="385.9" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="285.3" y1="374.7" x2="285.3" y2="407.6" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="385.7" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="289.1" y1="379.9" x2="289.1" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="381.5" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="292.9" y1="379.2" x2="292.9" y2="401.6" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="382.4" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="296.6" y1="365.6" x2="296.6" y2="406.7" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="385.4" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="300.4" y1="382.1" x2="300.4" y2="423.2" stroke="var(--down)" class="wick"/>
<rect x="299.25" y="389.5" width="2.35" height="26.1" fill="var(--down)"/>
<line x1="304.2" y1="400.4" x2="304.2" y2="417.8" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="401.0" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="308.0" y1="380.2" x2="308.0" y2="414.2" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="388.1" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="311.8" y1="375.9" x2="311.8" y2="398.0" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="384.1" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="315.6" y1="380.5" x2="315.6" y2="425.4" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="384.2" width="2.35" height="39.1" fill="var(--down)"/>
<line x1="319.4" y1="403.1" x2="319.4" y2="431.6" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="421.5" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="323.1" y1="425.7" x2="323.1" y2="449.8" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="425.9" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="326.9" y1="421.9" x2="326.9" y2="451.1" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="427.3" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="330.7" y1="445.5" x2="330.7" y2="480.5" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="447.1" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="334.5" y1="427.8" x2="334.5" y2="463.5" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="428.3" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="338.3" y1="428.6" x2="338.3" y2="451.9" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="430.7" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="342.1" y1="430.0" x2="342.1" y2="450.8" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="440.1" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="345.9" y1="433.5" x2="345.9" y2="450.1" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="446.2" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="349.6" y1="439.3" x2="349.6" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="439.3" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="353.4" y1="440.0" x2="353.4" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="440.5" width="2.35" height="16.0" fill="var(--down)"/>
<line x1="357.2" y1="411.4" x2="357.2" y2="462.9" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="425.2" width="2.35" height="35.3" fill="var(--up)"/>
<line x1="361.0" y1="402.2" x2="361.0" y2="428.4" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="409.2" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="364.8" y1="417.4" x2="364.8" y2="441.7" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="422.1" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="368.6" y1="422.9" x2="368.6" y2="469.6" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="443.5" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="372.4" y1="440.4" x2="372.4" y2="463.8" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="450.6" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="376.2" y1="424.7" x2="376.2" y2="450.8" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="425.7" width="2.35" height="24.9" fill="var(--up)"/>
<line x1="379.9" y1="420.0" x2="379.9" y2="439.4" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="420.0" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="383.7" y1="432.0" x2="383.7" y2="439.2" stroke="var(--down)" class="wick"/>
<rect x="382.55" y="437.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="387.5" y1="438.3" x2="387.5" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="442.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="391.3" y1="433.8" x2="391.3" y2="447.7" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="436.8" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="395.1" y1="432.9" x2="395.1" y2="460.2" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="436.8" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="398.9" y1="442.9" x2="398.9" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="446.3" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="402.7" y1="443.5" x2="402.7" y2="467.3" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="448.0" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="406.4" y1="453.9" x2="406.4" y2="473.7" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="464.1" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="410.2" y1="449.3" x2="410.2" y2="479.7" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="454.3" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="414.0" y1="448.2" x2="414.0" y2="465.8" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="451.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="417.8" y1="444.4" x2="417.8" y2="460.1" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="447.3" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="421.6" y1="438.1" x2="421.6" y2="452.8" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="447.6" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="425.4" y1="436.0" x2="425.4" y2="452.4" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="438.4" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="429.2" y1="430.7" x2="429.2" y2="447.6" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="436.7" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="432.9" y1="420.0" x2="432.9" y2="441.1" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="434.6" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="436.7" y1="421.0" x2="436.7" y2="434.8" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="424.2" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="440.5" y1="413.6" x2="440.5" y2="427.5" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="421.0" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="444.3" y1="403.8" x2="444.3" y2="431.2" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="411.9" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="448.1" y1="394.2" x2="448.1" y2="421.0" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="402.8" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="451.9" y1="402.7" x2="451.9" y2="419.8" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="402.9" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="455.7" y1="399.9" x2="455.7" y2="417.8" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="408.6" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="459.5" y1="401.1" x2="459.5" y2="417.9" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="402.0" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="463.2" y1="400.9" x2="463.2" y2="422.0" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="407.5" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="467.0" y1="402.7" x2="467.0" y2="417.5" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="409.7" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="470.8" y1="407.9" x2="470.8" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="411.0" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="474.6" y1="396.9" x2="474.6" y2="420.6" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="405.4" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="478.4" y1="403.4" x2="478.4" y2="429.3" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="405.2" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="482.2" y1="377.3" x2="482.2" y2="403.0" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="379.3" width="2.35" height="22.9" fill="var(--up)"/>
<line x1="486.0" y1="379.3" x2="486.0" y2="392.0" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="384.6" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="489.7" y1="393.1" x2="489.7" y2="408.8" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="393.1" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="493.5" y1="373.6" x2="493.5" y2="407.3" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="386.9" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="497.3" y1="385.7" x2="497.3" y2="401.6" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="386.3" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="501.1" y1="382.2" x2="501.1" y2="395.3" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="387.1" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="504.9" y1="370.2" x2="504.9" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="373.2" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="508.7" y1="362.9" x2="508.7" y2="380.7" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="367.4" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="512.5" y1="371.9" x2="512.5" y2="399.5" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="374.1" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="516.2" y1="380.1" x2="516.2" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="380.5" width="2.35" height="14.6" fill="var(--down)"/>
<line x1="520.0" y1="379.0" x2="520.0" y2="397.2" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="389.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="523.8" y1="386.4" x2="523.8" y2="394.8" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="388.3" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="527.6" y1="387.7" x2="527.6" y2="405.7" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="393.9" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="531.4" y1="396.9" x2="531.4" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="404.9" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="535.2" y1="406.2" x2="535.2" y2="418.6" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="408.3" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="539.0" y1="399.3" x2="539.0" y2="419.6" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="401.1" width="2.35" height="16.3" fill="var(--up)"/>
<line x1="542.7" y1="402.4" x2="542.7" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="405.5" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="546.5" y1="416.8" x2="546.5" y2="425.1" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="418.6" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="550.3" y1="415.8" x2="550.3" y2="431.8" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="418.9" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="554.1" y1="407.8" x2="554.1" y2="426.3" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="418.7" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="557.9" y1="424.1" x2="557.9" y2="437.6" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="425.3" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="561.7" y1="428.0" x2="561.7" y2="438.5" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="428.5" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="565.5" y1="415.6" x2="565.5" y2="433.1" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="416.7" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="569.3" y1="411.3" x2="569.3" y2="421.3" stroke="var(--down)" class="wick"/>
<rect x="568.08" y="417.5" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="573.0" y1="414.6" x2="573.0" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="416.7" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="576.8" y1="415.7" x2="576.8" y2="433.3" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="416.7" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="580.6" y1="417.0" x2="580.6" y2="430.7" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="427.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="584.4" y1="412.6" x2="584.4" y2="437.1" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="415.1" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="588.2" y1="415.0" x2="588.2" y2="430.1" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="416.4" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="592.0" y1="411.0" x2="592.0" y2="431.2" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="421.1" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="595.8" y1="421.2" x2="595.8" y2="430.8" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="423.1" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="599.5" y1="418.3" x2="599.5" y2="432.9" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="419.4" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="603.3" y1="416.5" x2="603.3" y2="429.8" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="419.4" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="607.1" y1="422.5" x2="607.1" y2="436.7" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="425.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="610.9" y1="413.5" x2="610.9" y2="427.6" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="420.8" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="614.7" y1="419.9" x2="614.7" y2="431.4" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="420.8" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="618.5" y1="405.6" x2="618.5" y2="432.4" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="407.9" width="2.35" height="23.9" fill="var(--up)"/>
<line x1="622.3" y1="382.1" x2="622.3" y2="407.1" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="383.9" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="626.0" y1="382.3" x2="626.0" y2="390.6" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="382.6" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="629.8" y1="375.1" x2="629.8" y2="386.1" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="377.2" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="633.6" y1="360.1" x2="633.6" y2="379.1" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="366.6" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="637.4" y1="366.2" x2="637.4" y2="384.2" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="367.4" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="641.2" y1="361.4" x2="641.2" y2="382.7" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="378.5" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="645.0" y1="360.8" x2="645.0" y2="401.3" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="363.6" width="2.35" height="30.3" fill="var(--up)"/>
<line x1="648.8" y1="357.2" x2="648.8" y2="368.3" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="359.2" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="652.5" y1="353.5" x2="652.5" y2="369.7" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="358.5" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="656.3" y1="353.3" x2="656.3" y2="367.4" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="358.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="660.1" y1="358.3" x2="660.1" y2="372.1" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="360.9" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="663.9" y1="369.0" x2="663.9" y2="383.1" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="370.1" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="667.7" y1="362.8" x2="667.7" y2="373.9" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="369.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="671.5" y1="362.3" x2="671.5" y2="377.2" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="369.7" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="675.3" y1="350.1" x2="675.3" y2="376.7" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="350.8" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="679.1" y1="339.4" x2="679.1" y2="356.2" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="345.1" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="682.8" y1="343.9" x2="682.8" y2="368.8" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="344.6" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="686.6" y1="353.4" x2="686.6" y2="369.8" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="359.4" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="690.4" y1="340.2" x2="690.4" y2="367.5" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="353.0" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="694.2" y1="307.8" x2="694.2" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="309.1" width="2.35" height="40.5" fill="var(--up)"/>
<line x1="698.0" y1="279.3" x2="698.0" y2="304.8" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="293.0" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="701.8" y1="261.1" x2="701.8" y2="294.6" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="268.0" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="705.6" y1="262.0" x2="705.6" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="264.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="709.3" y1="254.7" x2="709.3" y2="273.7" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="264.4" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="713.1" y1="270.3" x2="713.1" y2="292.7" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="272.7" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="716.9" y1="289.5" x2="716.9" y2="314.6" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="292.5" width="2.35" height="8.7" fill="var(--down)"/>
<line x1="720.7" y1="295.0" x2="720.7" y2="307.4" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="297.4" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="724.5" y1="262.8" x2="724.5" y2="297.7" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="268.3" width="2.35" height="23.5" fill="var(--up)"/>
<line x1="728.3" y1="250.9" x2="728.3" y2="272.5" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="261.6" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="732.1" y1="183.0" x2="732.1" y2="264.3" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="194.8" width="2.35" height="65.7" fill="var(--up)"/>
<line x1="735.8" y1="190.5" x2="735.8" y2="247.7" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="195.5" width="2.35" height="50.0" fill="var(--down)"/>
<line x1="739.6" y1="245.6" x2="739.6" y2="269.7" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="248.6" width="2.35" height="16.8" fill="var(--down)"/>
<line x1="743.4" y1="242.1" x2="743.4" y2="290.2" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="267.3" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="747.2" y1="264.6" x2="747.2" y2="306.8" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="277.6" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="751.0" y1="254.2" x2="751.0" y2="291.1" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="271.5" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="754.8" y1="250.6" x2="754.8" y2="294.1" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="253.5" width="2.35" height="18.0" fill="var(--up)"/>
<line x1="758.6" y1="250.0" x2="758.6" y2="291.9" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="252.8" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="762.4" y1="273.3" x2="762.4" y2="299.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="274.3" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="766.1" y1="247.5" x2="766.1" y2="278.8" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="257.7" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="769.9" y1="234.7" x2="769.9" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="250.6" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="773.7" y1="236.4" x2="773.7" y2="336.3" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="265.0" width="2.35" height="64.5" fill="var(--down)"/>
<line x1="777.5" y1="270.2" x2="777.5" y2="350.2" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="273.5" width="2.35" height="72.3" fill="var(--up)"/>
<line x1="781.3" y1="239.2" x2="781.3" y2="278.8" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="246.5" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="785.1" y1="238.6" x2="785.1" y2="269.9" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="242.3" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="788.9" y1="228.7" x2="788.9" y2="260.6" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="236.0" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="792.6" y1="216.0" x2="792.6" y2="245.3" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="240.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="796.4" y1="229.1" x2="796.4" y2="255.6" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="229.4" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="800.2" y1="239.5" x2="800.2" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="242.3" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="804.0" y1="232.5" x2="804.0" y2="252.9" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="233.1" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="807.8" y1="210.2" x2="807.8" y2="237.6" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="218.3" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="811.6" y1="228.2" x2="811.6" y2="255.5" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="229.8" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="815.4" y1="219.9" x2="815.4" y2="244.9" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="228.8" width="2.35" height="9.2" fill="var(--down)"/>
<line x1="819.1" y1="218.0" x2="819.1" y2="251.6" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="225.8" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="822.9" y1="211.2" x2="822.9" y2="236.4" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="226.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="826.7" y1="222.2" x2="826.7" y2="246.2" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="227.1" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="830.5" y1="212.3" x2="830.5" y2="250.0" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="215.4" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="834.3" y1="228.0" x2="834.3" y2="271.9" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="238.8" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="838.1" y1="224.7" x2="838.1" y2="256.8" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="229.9" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="841.9" y1="217.7" x2="841.9" y2="252.5" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="228.9" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="845.6" y1="239.3" x2="845.6" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="246.0" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="849.4" y1="220.0" x2="849.4" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="231.7" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="853.2" y1="213.9" x2="853.2" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="221.4" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="857.0" y1="217.3" x2="857.0" y2="246.0" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="224.2" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="860.8" y1="225.4" x2="860.8" y2="245.5" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="235.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="864.6" y1="229.5" x2="864.6" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="234.5" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="868.4" y1="224.8" x2="868.4" y2="249.8" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="229.6" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="872.2" y1="229.5" x2="872.2" y2="247.4" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="229.5" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="875.9" y1="229.9" x2="875.9" y2="256.7" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="243.2" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="879.7" y1="248.9" x2="879.7" y2="281.1" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="254.9" width="2.35" height="21.9" fill="var(--down)"/>
<line x1="883.5" y1="255.6" x2="883.5" y2="277.9" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="273.3" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="887.3" y1="271.9" x2="887.3" y2="303.6" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="273.0" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="891.1" y1="288.3" x2="891.1" y2="310.5" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="294.8" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="894.9" y1="281.7" x2="894.9" y2="306.1" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="286.0" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="898.7" y1="279.6" x2="898.7" y2="311.8" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="285.9" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="902.4" y1="298.3" x2="902.4" y2="321.6" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="302.3" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="906.2" y1="295.2" x2="906.2" y2="315.3" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="303.5" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="910.0" y1="311.5" x2="910.0" y2="349.3" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="315.0" width="2.35" height="33.6" fill="var(--down)"/>
<line x1="913.8" y1="339.6" x2="913.8" y2="356.3" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="347.6" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="917.6" y1="341.7" x2="917.6" y2="351.6" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="347.1" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="921.4" y1="323.3" x2="921.4" y2="348.7" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="328.1" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="925.2" y1="320.8" x2="925.2" y2="343.1" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="323.5" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="928.9" y1="302.2" x2="928.9" y2="342.2" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="306.6" width="2.35" height="30.4" fill="var(--up)"/>
<line x1="932.7" y1="299.8" x2="932.7" y2="317.4" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="305.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="936.5" y1="288.8" x2="936.5" y2="311.4" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="294.9" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="940.3" y1="289.2" x2="940.3" y2="307.8" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="291.0" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="944.1" y1="267.2" x2="944.1" y2="291.5" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="272.4" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="947.9" y1="254.8" x2="947.9" y2="280.2" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="258.6" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="951.7" y1="234.0" x2="951.7" y2="283.0" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="236.1" width="2.35" height="21.8" fill="var(--up)"/>
<line x1="955.5" y1="179.1" x2="955.5" y2="223.0" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="189.0" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="959.2" y1="179.2" x2="959.2" y2="218.6" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="190.9" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="963.0" y1="81.5" x2="963.0" y2="206.0" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="126.6" width="2.35" height="68.5" fill="var(--up)"/>
<line x1="966.8" y1="83.0" x2="966.8" y2="149.5" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="87.8" width="2.35" height="55.7" fill="var(--up)"/>
<line x1="970.6" y1="78.1" x2="970.6" y2="146.9" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="78.1" width="2.35" height="47.9" fill="var(--down)"/>
<line x1="974.4" y1="102.4" x2="974.4" y2="177.0" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="126.0" width="2.35" height="37.9" fill="var(--down)"/>
<line x1="978.2" y1="148.3" x2="978.2" y2="210.2" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="156.0" width="2.35" height="42.9" fill="var(--down)"/>
<line x1="982.0" y1="176.2" x2="982.0" y2="202.2" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="184.3" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="985.7" y1="139.8" x2="985.7" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="152.9" width="2.35" height="29.3" fill="var(--up)"/>
<line x1="989.5" y1="141.3" x2="989.5" y2="235.5" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="150.8" width="2.35" height="74.7" fill="var(--down)"/>
<line x1="993.3" y1="206.0" x2="993.3" y2="229.4" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="221.3" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="997.1" y1="197.3" x2="997.1" y2="238.7" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="223.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1000.9" y1="230.6" x2="1000.9" y2="265.0" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="235.5" width="2.35" height="27.0" fill="var(--down)"/>
<line x1="1004.7" y1="222.1" x2="1004.7" y2="257.3" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="228.6" width="2.35" height="28.5" fill="var(--up)"/>
<line x1="1008.5" y1="211.3" x2="1008.5" y2="242.0" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="222.7" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="1012.2" y1="234.5" x2="1012.2" y2="265.3" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="250.0" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="1016.0" y1="220.7" x2="1016.0" y2="261.9" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="221.8" width="2.35" height="31.2" fill="var(--up)"/>
<line x1="1019.8" y1="201.4" x2="1019.8" y2="235.1" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="211.3" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="1023.6" y1="165.3" x2="1023.6" y2="217.4" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="180.6" width="2.35" height="30.7" fill="var(--up)"/>
<line x1="1027.4" y1="159.4" x2="1027.4" y2="191.7" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="171.0" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="1031.2" y1="136.3" x2="1031.2" y2="177.9" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="153.7" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="1035.0" y1="164.9" x2="1035.0" y2="202.5" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="167.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1038.7" y1="157.0" x2="1038.7" y2="199.7" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="178.2" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="1042.5" y1="146.9" x2="1042.5" y2="183.3" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="149.0" width="2.35" height="34.2" fill="var(--up)"/>
<line x1="1046.3" y1="124.5" x2="1046.3" y2="165.8" stroke="var(--up)" class="wick"/>
<rect x="1045.15" y="134.8" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="1050.1" y1="124.5" x2="1050.1" y2="137.4" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="128.9" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="60" y1="268.6" x2="1052" y2="268.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="262.6" font-size="11.5" fill="var(--support)" font-weight="600">$222 S1</text>
<text x="1058" y="274.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="310.7" x2="1052" y2="310.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="304.7" font-size="11.5" fill="var(--support)" font-weight="600">$205 S2</text>
<text x="1058" y="316.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="353.2" x2="1052" y2="353.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="347.2" font-size="11.5" fill="var(--support)" font-weight="600">$187 S3</text>
<text x="1058" y="359.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="134.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="126.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $278 (2026-08-21)</text>
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
| **현재가** | **$277.51** (2026-08-21 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $222 | 2 | 2025-07-21·2026-06-15 — 1년 가까이 간격을 두고 두 번 눌린 자리 |
| S2 | $205 | 2 | 2024-12-16·2025-02-10 — 2025년 상반기 박스권의 중심대 |
| S3 | $187 | 2 | 2025-04-07·2025-12-15 — 2025년 두 차례 저점대. 일봉 참고선($186.20)과 같은 구간 |
| 참고선 | $300.89 | — | 5년 최고(2026-03-30 주간). 카타르 공급 충격 직후 형성된 고점이라 아직 저항으로 검증된 적이 없다 |
| 참고선 | $84.19 | — | 5년 최저(2021-09-20 주간). 배당 도입 이전·CCL Stage 3 착공 이전의 회사라 현재 레짐과 단절돼 있다 |

> **저항 클러스터가 하나도 없다.** 현재가가 5년 최고가($300.89)에 근접한 신고가 구간이라 위쪽에 스윙 고점이 쌓일 여지가 없었기 때문이다. 억지로 채우지 않고 지지 3개만 뒀으며, 5년 최고·최저는 참고선으로 분리했다.

---

## 3. 관측된 특이 구간 — 5년에 걸친 두 번의 공급 충격

이 종목의 5년 주봉에는 **국제 LNG 공급이 흔들릴 때마다 계단식으로 레짐이 올라선** 패턴이 두 번 나타난다.

- **2022년 2~3월 — 러시아-우크라이나 전쟁.** 유럽이 러시아 파이프라인 가스를 미국 LNG로 대체하기 시작하면서, 2월 21일 주 +11.4%(거래량 1.8배), 3월 21일 주 **+13.2%**(주간 종가 $131.86 → $149.30, 거래량 1.4배)로 뛰었다. 이 국면에서 $80~90대였던 거래대가 $130~150대로 올라섰다.
- **2026년 3월 — 카타르 라스라판 피격.** 3월 16일 주에 주간 종가 $252.27 → $280.89(**+11.3%**)로 급등했고, 거래량은 2,764만 주로 **주평균(940만 주)의 2.9배** — 5년 전체에서 가장 높은 거래량 배수다. 이 주에 형성된 고점대가 곧 5년 최고($300.89, 3월 30일 주)로 이어졌다. 상세는 [기술적 분석 — 일봉·1년](./09_technical_daily.md) 3. 관측된 특이 구간 참고.

두 사건 모두 **회사가 일으킨 것이 아니라 공급 측 지정학 충격**이며, 두 번 다 주가가 이전 구간으로 완전히 되돌아가지 않았다. 이 패턴은 상방 재료로도 하방 경고로도 읽을 수 있다 — 충격이 남긴 가격대가 유지된 이력이 있다는 뜻인 동시에, **최근 상승분의 상당 부분이 회사 실적이 아니라 외부 사건에서 왔다**는 뜻이기도 하다. 후자의 관점은 [투자 판단](./07_investment.md) 3. 리스크 (약점 / Bear Case)에서 다룬다.

참고로 하락 쪽 최대 변동은 2025년 3월 31일 주(**−12.8%**)와 2026년 5월 4일 주(**−11.1%**)였다. 두 경우 모두 거래량 배수가 1.4~1.5배로 상승 국면보다 낮아, 대량 물량이 이탈한 구간은 아니었다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-23~2026-08-21. 수집 시점: 2026-08-24. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(2회 미만인데도 넣은 참고선은 2. 지지선 / 저항선 요약 비고에 사유를 적었다).
- **생성**: `scripts/gen_technical_chart.py` (`LNG --name "Cheniere Energy" --interval 1wk --close-on 2026-08-21`). 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **5년 구간 안에서 회사의 성격이 바뀌었다.** 2021년 9월 자본배분 계획 발표 이전은 무배당·순차입 확대 국면이었고 이후는 배당·자사주매입으로 발행주식수가 줄어드는 국면이다([역사 / 주요 이벤트](./02_history.md) 참고). 5년 최저($84.19, 2021-09-20)를 현재와 같은 회사의 가격으로 비교하면 안 되는 이유다.
    - 기간 내 주식분할·병합은 없었다. **분기배당 20회가 지급됐고 이 차트는 원주가라 배당을 반영하지 않는다** — 5년간 지급된 배당 합계는 주당 $8.86이라, 수정주가 기준 차트는 과거 구간이 그만큼 낮게 그려진다.

---

## 관련 문서

- **먼저 읽기** — [최종 보고서](./11_final_report.md): 아래 문서 전체를 종합한 요약이라, 처음이라면 여기부터 봐도 된다
- **회사 이해** — [개요](./01_overview.md) · [역사 / 주요 이벤트](./02_history.md) · [CEO / 경영진](./03_ceo.md)
- **숫자** — [핵심 지표](./04_metrics.md) · [재무 / 실적](./05_financials.md) · [밸류에이션 / 적정주가](./06_valuation.md)
- **판단 · 로그** — [투자 판단](./07_investment.md) · [최근 뉴스 / 이슈](./08_news.md)
- **가격 차트** — [기술적 분석 — 일봉·1년](./09_technical_daily.md)

---

## 참고 자료

- [Yahoo Finance — Cheniere Energy (LNG)](https://finance.yahoo.com/quote/LNG/)
- [StockAnalysis — LNG 종가 이력](https://stockanalysis.com/stocks/lng/history/)

---

*작성일: 2026-08-24*
