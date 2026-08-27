# 기술적 분석 (주봉 캔들차트 · 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 단기 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **⚠️ 차트의 마지막 봉(2026-08-24 주)은 아직 끝나지 않은 주다.** 차트를 생성한 시점이 미 동부시간 2026-08-24 오전(그 주의 첫 거래일 정규장 개장 중)이라, 마지막 주봉은 하루치 장중 값($30.67)만 담고 있다. **다른 문서가 인용하는 기준 종가는 2026-08-21 종가 $30.98이다**(직전 주의 마지막 거래일).
    - **대조 결과**: 2026-08-17 주봉 종가 $30.98이 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)의 기준 종가와 일치한다(그 주의 마지막 거래일이 2026-08-21이기 때문).
    - **회계연도 말 종가는 주봉과 직접 대조되지 않는다** — [핵심 지표](./04_metrics.md) A.2의 FY2023 $17.64(2023-12-29)는 그 주(2023-12-25 시작)의 마지막 거래일이라 주봉 종가와 일치하지만, FY2024 $27.40(2024-12-31)·FY2025 $27.49(2025-12-31)는 주 중간이라 해당 주봉 종가($28.27·$27.71)와 다르다. **연말 종가는 주봉 차트가 아니라 핵심 지표의 값을 쓸 것.**

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-24)

<div class="kmi-chart">
<style>
.kmi-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .kmi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .kmi-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.kmi-chart svg { width:100%; height:auto; display:block; }
.kmi-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.kmi-chart .title { fill: var(--ink); font-weight:600; }
.kmi-chart .grid { stroke: var(--grid); stroke-width:1; }
.kmi-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kinder Morgan(KMI) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Kinder Morgan (KMI) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-24 · 마지막 종가 $30.67 (2026-08-24) · 단위 USD</text>
<line x1="60" y1="599.5" x2="1052" y2="599.5" class="grid"/>
<text x="52" y="603.5" font-size="11" text-anchor="end" fill="var(--muted)">15.00</text>
<line x1="60" y1="466.9" x2="1052" y2="466.9" class="grid"/>
<text x="52" y="470.9" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="334.4" x2="1052" y2="334.4" class="grid"/>
<text x="52" y="338.4" font-size="11" text-anchor="end" fill="var(--muted)">25</text>
<line x1="60" y1="201.8" x2="1052" y2="201.8" class="grid"/>
<text x="52" y="205.8" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="69.3" x2="1052" y2="69.3" class="grid"/>
<text x="52" y="73.3" font-size="11" text-anchor="end" fill="var(--muted)">35</text>
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
<line x1="61.9" y1="553.9" x2="61.9" y2="569.3" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="557.3" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="65.7" y1="556.8" x2="65.7" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="556.8" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="69.5" y1="561.6" x2="69.5" y2="575.9" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="565.6" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="73.3" y1="560.3" x2="73.3" y2="575.4" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="570.6" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="77.0" y1="556.0" x2="77.0" y2="587.0" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="558.9" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="80.8" y1="540.9" x2="80.8" y2="554.9" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="548.9" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="84.6" y1="532.4" x2="84.6" y2="559.2" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="534.0" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="88.4" y1="503.8" x2="88.4" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="507.8" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="92.2" y1="499.8" x2="92.2" y2="538.2" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="505.1" width="2.35" height="23.6" fill="var(--down)"/>
<line x1="96.0" y1="520.5" x2="96.0" y2="553.6" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="525.0" width="2.35" height="28.1" fill="var(--down)"/>
<line x1="99.8" y1="543.8" x2="99.8" y2="558.1" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="547.8" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="103.5" y1="544.6" x2="103.5" y2="556.8" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="545.1" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="107.3" y1="546.5" x2="107.3" y2="572.4" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="553.6" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="111.1" y1="557.3" x2="111.1" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="566.1" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="114.9" y1="560.5" x2="114.9" y2="592.6" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="561.8" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="118.7" y1="562.6" x2="118.7" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="568.7" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="122.5" y1="567.7" x2="122.5" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="569.3" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="126.3" y1="578.5" x2="126.3" y2="599.2" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="582.5" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="130.0" y1="573.5" x2="130.0" y2="586.5" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="576.7" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="133.8" y1="538.0" x2="133.8" y2="575.9" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="539.3" width="2.35" height="35.0" fill="var(--up)"/>
<line x1="137.6" y1="522.6" x2="137.6" y2="544.1" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="522.9" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="141.4" y1="520.5" x2="141.4" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="523.7" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="145.2" y1="514.7" x2="145.2" y2="555.2" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="541.2" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="149.0" y1="532.1" x2="149.0" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="537.2" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="152.8" y1="529.8" x2="152.8" y2="543.5" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="532.1" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="156.5" y1="532.1" x2="156.5" y2="560.8" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="532.9" width="2.35" height="24.1" fill="var(--down)"/>
<line x1="160.3" y1="542.5" x2="160.3" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="544.6" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="164.1" y1="496.9" x2="164.1" y2="549.9" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="497.7" width="2.35" height="50.9" fill="var(--up)"/>
<line x1="167.9" y1="489.5" x2="167.9" y2="517.3" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="496.1" width="2.35" height="21.2" fill="var(--down)"/>
<line x1="171.7" y1="520.2" x2="171.7" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="522.6" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="175.5" y1="491.6" x2="175.5" y2="530.6" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="491.6" width="2.35" height="38.4" fill="var(--up)"/>
<line x1="179.3" y1="486.5" x2="179.3" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="487.6" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="183.1" y1="477.8" x2="183.1" y2="498.7" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="480.7" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="186.8" y1="479.7" x2="186.8" y2="492.6" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="483.6" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="190.6" y1="461.9" x2="190.6" y2="489.7" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="481.8" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="194.4" y1="495.8" x2="194.4" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="497.9" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="198.2" y1="484.2" x2="198.2" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="485.5" width="2.35" height="31.8" fill="var(--up)"/>
<line x1="202.0" y1="491.1" x2="202.0" y2="515.7" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="493.4" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="205.8" y1="469.8" x2="205.8" y2="502.2" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="492.6" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="209.6" y1="466.4" x2="209.6" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="468.5" width="2.35" height="19.9" fill="var(--up)"/>
<line x1="213.3" y1="462.7" x2="213.3" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="467.2" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="217.1" y1="461.6" x2="217.1" y2="499.3" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="465.9" width="2.35" height="26.8" fill="var(--down)"/>
<line x1="220.9" y1="502.7" x2="220.9" y2="578.8" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="504.3" width="2.35" height="67.3" fill="var(--down)"/>
<line x1="224.7" y1="552.0" x2="224.7" y2="573.5" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="560.3" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="228.5" y1="533.5" x2="228.5" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="547.0" width="2.35" height="9.3" fill="var(--up)"/>
<line x1="232.3" y1="543.8" x2="232.3" y2="575.1" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="547.3" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="236.1" y1="547.5" x2="236.1" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="551.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="239.8" y1="523.7" x2="239.8" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="529.2" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="243.6" y1="513.9" x2="243.6" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="520.2" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="247.4" y1="518.6" x2="247.4" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="526.6" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="251.2" y1="500.1" x2="251.2" y2="533.7" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="501.7" width="2.35" height="32.1" fill="var(--up)"/>
<line x1="255.0" y1="494.8" x2="255.0" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="500.9" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="258.8" y1="484.7" x2="258.8" y2="508.6" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="493.7" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="262.6" y1="489.7" x2="262.6" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="494.8" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="266.4" y1="507.0" x2="266.4" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="508.8" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="270.1" y1="499.5" x2="270.1" y2="527.9" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="506.7" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="273.9" y1="515.2" x2="273.9" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="533.2" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="277.7" y1="547.8" x2="277.7" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="556.0" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="281.5" y1="525.3" x2="281.5" y2="547.5" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="540.1" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="285.3" y1="526.6" x2="285.3" y2="550.7" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="538.5" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="289.1" y1="517.6" x2="289.1" y2="547.5" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="532.7" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="292.9" y1="515.7" x2="292.9" y2="543.0" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="526.1" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="296.6" y1="507.2" x2="296.6" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="515.4" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="300.4" y1="499.0" x2="300.4" y2="531.4" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="501.7" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="304.2" y1="494.5" x2="304.2" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="502.5" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="308.0" y1="496.9" x2="308.0" y2="524.2" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="503.3" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="311.8" y1="483.9" x2="311.8" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="493.4" width="2.35" height="19.9" fill="var(--up)"/>
<line x1="315.6" y1="490.0" x2="315.6" y2="535.6" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="490.5" width="2.35" height="44.0" fill="var(--down)"/>
<line x1="319.4" y1="510.7" x2="319.4" y2="536.1" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="528.2" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="323.1" y1="516.2" x2="323.1" y2="536.1" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="516.2" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="326.9" y1="510.9" x2="326.9" y2="523.7" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="514.4" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="330.7" y1="501.7" x2="330.7" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="504.6" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="334.5" y1="491.9" x2="334.5" y2="506.4" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="497.4" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="338.3" y1="490.8" x2="338.3" y2="512.3" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="495.3" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="342.1" y1="496.1" x2="342.1" y2="511.5" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="500.3" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="345.9" y1="503.0" x2="345.9" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="512.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="349.6" y1="509.1" x2="349.6" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="510.4" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="353.4" y1="506.4" x2="353.4" y2="528.4" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="511.7" width="2.35" height="15.4" fill="var(--down)"/>
<line x1="357.2" y1="527.9" x2="357.2" y2="539.6" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="529.8" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="361.0" y1="527.9" x2="361.0" y2="544.9" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="529.2" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="364.8" y1="526.3" x2="364.8" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="530.0" width="2.35" height="22.5" fill="var(--down)"/>
<line x1="368.6" y1="538.5" x2="368.6" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="559.7" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="372.4" y1="545.9" x2="372.4" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="552.0" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="376.2" y1="532.1" x2="376.2" y2="553.6" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="532.9" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="379.9" y1="524.2" x2="379.9" y2="537.5" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="526.1" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="383.7" y1="520.5" x2="383.7" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="525.0" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="387.5" y1="523.7" x2="387.5" y2="544.1" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="525.0" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="391.3" y1="528.4" x2="391.3" y2="546.2" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="536.9" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="395.1" y1="540.4" x2="395.1" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="545.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="398.9" y1="541.7" x2="398.9" y2="557.1" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="543.5" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="402.7" y1="549.1" x2="402.7" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="549.9" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="406.4" y1="554.9" x2="406.4" y2="570.1" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="560.3" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="410.2" y1="551.2" x2="410.2" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="553.1" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="414.0" y1="536.7" x2="414.0" y2="556.0" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="545.7" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="417.8" y1="539.6" x2="417.8" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="545.4" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="421.6" y1="545.9" x2="421.6" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="546.2" width="2.35" height="18.3" fill="var(--down)"/>
<line x1="425.4" y1="537.5" x2="425.4" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="540.6" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="429.2" y1="536.1" x2="429.2" y2="552.8" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="540.6" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="432.9" y1="529.0" x2="432.9" y2="552.0" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="540.9" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="436.7" y1="522.3" x2="436.7" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="525.3" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="440.5" y1="512.0" x2="440.5" y2="535.3" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="523.7" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="444.3" y1="525.8" x2="444.3" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="529.8" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="448.1" y1="522.3" x2="448.1" y2="543.8" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="525.8" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="451.9" y1="523.7" x2="451.9" y2="541.4" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="525.0" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="455.7" y1="533.5" x2="455.7" y2="547.3" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="533.5" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="459.5" y1="532.7" x2="459.5" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="535.6" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="463.2" y1="540.6" x2="463.2" y2="557.9" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="543.3" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="467.0" y1="535.9" x2="467.0" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="544.6" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="470.8" y1="542.8" x2="470.8" y2="558.9" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="544.3" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="474.6" y1="551.5" x2="474.6" y2="562.1" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="557.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="478.4" y1="556.5" x2="478.4" y2="575.9" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="557.1" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="482.2" y1="541.7" x2="482.2" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="543.5" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="486.0" y1="534.8" x2="486.0" y2="550.7" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="541.2" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="489.7" y1="544.6" x2="489.7" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="549.4" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="493.5" y1="546.5" x2="493.5" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="549.9" width="2.35" height="19.4" fill="var(--up)"/>
<line x1="497.3" y1="548.1" x2="497.3" y2="568.5" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="548.1" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="501.1" y1="544.6" x2="501.1" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="547.5" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="504.9" y1="534.3" x2="504.9" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="537.2" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="508.7" y1="525.3" x2="508.7" y2="541.2" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="526.6" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="512.5" y1="522.6" x2="512.5" y2="535.6" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="527.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="516.2" y1="523.1" x2="516.2" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="528.7" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="520.0" y1="524.2" x2="520.0" y2="546.5" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="526.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="523.8" y1="522.9" x2="523.8" y2="531.4" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="525.3" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="527.6" y1="513.6" x2="527.6" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="519.4" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="531.4" y1="516.0" x2="531.4" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="520.7" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="535.2" y1="520.5" x2="535.2" y2="543.8" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="522.1" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="539.0" y1="534.0" x2="539.0" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="534.8" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="542.7" y1="533.5" x2="542.7" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="534.8" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="546.5" y1="550.4" x2="546.5" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="550.4" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="550.3" y1="541.7" x2="550.3" y2="560.5" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="543.5" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="554.1" y1="534.8" x2="554.1" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="539.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="557.9" y1="533.2" x2="557.9" y2="545.9" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="534.3" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="561.7" y1="521.3" x2="561.7" y2="535.3" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="524.5" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="565.5" y1="517.0" x2="565.5" y2="534.5" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="524.5" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="569.3" y1="511.7" x2="569.3" y2="532.7" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="518.4" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="573.0" y1="508.6" x2="573.0" y2="522.9" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="510.9" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="576.8" y1="500.9" x2="576.8" y2="515.4" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="507.8" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="580.6" y1="503.5" x2="580.6" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="507.2" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="584.4" y1="496.1" x2="584.4" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="497.7" width="2.35" height="15.9" fill="var(--up)"/>
<line x1="588.2" y1="495.6" x2="588.2" y2="506.2" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="499.0" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="592.0" y1="503.8" x2="592.0" y2="516.5" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="504.8" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="595.8" y1="488.7" x2="595.8" y2="507.0" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="491.3" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="599.5" y1="472.5" x2="599.5" y2="492.1" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="474.9" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="603.3" y1="468.8" x2="603.3" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="474.6" width="2.35" height="17.0" fill="var(--down)"/>
<line x1="607.1" y1="479.9" x2="607.1" y2="497.9" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="480.5" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="610.9" y1="471.2" x2="610.9" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="477.0" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="614.7" y1="465.1" x2="614.7" y2="478.9" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="476.5" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="618.5" y1="468.5" x2="618.5" y2="478.6" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="474.6" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="622.3" y1="461.9" x2="622.3" y2="477.0" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="470.4" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="626.0" y1="464.8" x2="626.0" y2="481.0" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="467.5" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="629.8" y1="458.4" x2="629.8" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="461.9" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="633.6" y1="419.5" x2="633.6" y2="466.1" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="427.4" width="2.35" height="32.1" fill="var(--up)"/>
<line x1="637.4" y1="417.6" x2="637.4" y2="440.2" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="426.4" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="641.2" y1="419.2" x2="641.2" y2="453.4" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="429.5" width="2.35" height="19.4" fill="var(--down)"/>
<line x1="645.0" y1="432.7" x2="645.0" y2="475.4" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="439.9" width="2.35" height="28.6" fill="var(--up)"/>
<line x1="648.8" y1="435.1" x2="648.8" y2="449.4" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="438.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="652.5" y1="429.8" x2="652.5" y2="444.7" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="433.0" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="656.3" y1="424.8" x2="656.3" y2="434.9" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="425.3" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="660.1" y1="423.2" x2="660.1" y2="439.4" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="428.5" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="663.9" y1="432.7" x2="663.9" y2="452.1" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="435.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="667.7" y1="417.1" x2="667.7" y2="432.5" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="419.5" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="671.5" y1="404.9" x2="671.5" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="418.1" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="675.3" y1="370.2" x2="675.3" y2="423.2" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="371.0" width="2.35" height="47.7" fill="var(--up)"/>
<line x1="679.1" y1="342.3" x2="679.1" y2="385.8" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="342.3" width="2.35" height="28.1" fill="var(--up)"/>
<line x1="682.8" y1="323.0" x2="682.8" y2="347.6" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="335.7" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="686.6" y1="329.1" x2="686.6" y2="345.8" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="334.4" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="690.4" y1="331.7" x2="690.4" y2="357.2" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="342.6" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="694.2" y1="281.3" x2="694.2" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="284.5" width="2.35" height="69.2" fill="var(--up)"/>
<line x1="698.0" y1="265.7" x2="698.0" y2="290.9" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="274.2" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="701.8" y1="233.4" x2="701.8" y2="272.1" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="241.8" width="2.35" height="30.2" fill="var(--up)"/>
<line x1="705.6" y1="235.7" x2="705.6" y2="264.1" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="239.2" width="2.35" height="8.5" fill="var(--down)"/>
<line x1="709.3" y1="247.7" x2="709.3" y2="278.2" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="249.0" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="713.1" y1="258.0" x2="713.1" y2="289.3" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="258.8" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="716.9" y1="281.6" x2="716.9" y2="313.7" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="285.3" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="720.7" y1="271.0" x2="720.7" y2="293.3" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="276.6" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="724.5" y1="240.8" x2="724.5" y2="283.2" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="247.7" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="728.3" y1="233.1" x2="728.3" y2="263.3" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="246.9" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="732.1" y1="188.3" x2="732.1" y2="250.1" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="193.6" width="2.35" height="54.6" fill="var(--up)"/>
<line x1="735.8" y1="162.6" x2="735.8" y2="199.4" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="186.4" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="739.6" y1="222.8" x2="739.6" y2="282.7" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="227.3" width="2.35" height="41.4" fill="var(--down)"/>
<line x1="743.4" y1="258.0" x2="743.4" y2="293.5" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="280.3" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="747.2" y1="273.7" x2="747.2" y2="304.4" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="276.0" width="2.35" height="17.2" fill="var(--down)"/>
<line x1="751.0" y1="276.0" x2="751.0" y2="302.8" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="292.0" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="754.8" y1="278.2" x2="754.8" y2="323.0" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="278.7" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="758.6" y1="257.8" x2="758.6" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="268.1" width="2.35" height="36.1" fill="var(--down)"/>
<line x1="762.4" y1="276.0" x2="762.4" y2="313.7" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="278.7" width="2.35" height="28.4" fill="var(--up)"/>
<line x1="766.1" y1="250.3" x2="766.1" y2="282.1" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="256.7" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="769.9" y1="224.9" x2="769.9" y2="255.4" stroke="var(--up)" class="wick"/>
<rect x="768.75" y="245.0" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="773.7" y1="229.9" x2="773.7" y2="331.5" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="251.9" width="2.35" height="74.8" fill="var(--down)"/>
<line x1="777.5" y1="290.9" x2="777.5" y2="362.5" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="295.4" width="2.35" height="55.4" fill="var(--up)"/>
<line x1="781.3" y1="263.3" x2="781.3" y2="291.7" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="278.7" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="785.1" y1="277.9" x2="785.1" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="285.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="788.9" y1="272.6" x2="788.9" y2="309.2" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="285.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="792.6" y1="258.3" x2="792.6" y2="300.7" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="273.1" width="2.35" height="19.9" fill="var(--up)"/>
<line x1="796.4" y1="248.7" x2="796.4" y2="284.0" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="252.5" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="800.2" y1="250.1" x2="800.2" y2="279.5" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="258.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="804.0" y1="245.6" x2="804.0" y2="264.9" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="252.7" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="807.8" y1="236.3" x2="807.8" y2="259.6" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="248.2" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="811.6" y1="251.4" x2="811.6" y2="276.0" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="252.2" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="815.4" y1="250.6" x2="815.4" y2="273.9" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="254.6" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="819.1" y1="224.1" x2="819.1" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="228.9" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="822.9" y1="212.9" x2="822.9" y2="258.0" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="226.2" width="2.35" height="17.8" fill="var(--down)"/>
<line x1="826.7" y1="240.5" x2="826.7" y2="272.9" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="244.2" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="830.5" y1="245.3" x2="830.5" y2="284.3" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="258.0" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="834.3" y1="259.6" x2="834.3" y2="295.1" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="261.2" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="838.1" y1="248.7" x2="838.1" y2="277.9" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="252.2" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="841.9" y1="242.6" x2="841.9" y2="290.1" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="251.9" width="2.35" height="32.3" fill="var(--down)"/>
<line x1="845.6" y1="278.7" x2="845.6" y2="300.7" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="284.0" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="849.4" y1="281.6" x2="849.4" y2="307.3" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="289.3" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="853.2" y1="279.0" x2="853.2" y2="304.1" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="281.9" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="857.0" y1="277.4" x2="857.0" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="288.5" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="860.8" y1="259.9" x2="860.8" y2="300.2" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="266.0" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="864.6" y1="258.0" x2="864.6" y2="279.5" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="263.6" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="868.4" y1="241.3" x2="868.4" y2="277.6" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="249.3" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="872.2" y1="230.7" x2="872.2" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="242.6" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="875.9" y1="238.4" x2="875.9" y2="279.0" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="239.2" width="2.35" height="39.5" fill="var(--down)"/>
<line x1="879.7" y1="259.3" x2="879.7" y2="281.3" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="271.3" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="883.5" y1="251.4" x2="883.5" y2="314.2" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="264.1" width="2.35" height="47.5" fill="var(--down)"/>
<line x1="887.3" y1="297.3" x2="887.3" y2="315.0" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="302.8" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="891.1" y1="291.7" x2="891.1" y2="318.5" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="293.3" width="2.35" height="15.1" fill="var(--up)"/>
<line x1="894.9" y1="268.4" x2="894.9" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="270.2" width="2.35" height="23.1" fill="var(--up)"/>
<line x1="898.7" y1="266.8" x2="898.7" y2="298.6" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="269.9" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="902.4" y1="271.8" x2="902.4" y2="299.4" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="272.9" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="906.2" y1="254.8" x2="906.2" y2="287.2" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="260.9" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="910.0" y1="259.6" x2="910.0" y2="295.9" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="262.3" width="2.35" height="26.2" fill="var(--down)"/>
<line x1="913.8" y1="285.1" x2="913.8" y2="301.5" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="287.4" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="917.6" y1="271.8" x2="917.6" y2="293.3" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="276.3" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="921.4" y1="257.5" x2="921.4" y2="276.3" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="262.5" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="925.2" y1="254.8" x2="925.2" y2="292.2" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="255.9" width="2.35" height="22.3" fill="var(--down)"/>
<line x1="928.9" y1="255.4" x2="928.9" y2="289.3" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="255.9" width="2.35" height="21.7" fill="var(--up)"/>
<line x1="932.7" y1="197.0" x2="932.7" y2="261.7" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="213.2" width="2.35" height="37.9" fill="var(--up)"/>
<line x1="936.5" y1="186.7" x2="936.5" y2="228.6" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="188.8" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="940.3" y1="186.2" x2="940.3" y2="216.4" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="188.6" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="944.1" y1="139.8" x2="944.1" y2="189.6" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="140.3" width="2.35" height="48.8" fill="var(--up)"/>
<line x1="947.9" y1="128.4" x2="947.9" y2="153.8" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="129.4" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="951.7" y1="113.0" x2="951.7" y2="145.1" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="115.1" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="955.5" y1="89.4" x2="955.5" y2="120.4" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="102.4" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="959.2" y1="98.2" x2="959.2" y2="131.0" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="104.8" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="963.0" y1="98.9" x2="963.0" y2="135.5" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="111.7" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="966.8" y1="76.4" x2="966.8" y2="137.1" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="95.0" width="2.35" height="32.3" fill="var(--up)"/>
<line x1="970.6" y1="86.2" x2="970.6" y2="135.0" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="88.3" width="2.35" height="34.7" fill="var(--down)"/>
<line x1="974.4" y1="101.1" x2="974.4" y2="148.0" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="125.5" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="978.2" y1="126.3" x2="978.2" y2="177.4" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="127.8" width="2.35" height="20.4" fill="var(--down)"/>
<line x1="982.0" y1="137.7" x2="982.0" y2="173.4" stroke="var(--down)" class="wick"/>
<rect x="980.78" y="155.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="985.7" y1="124.4" x2="985.7" y2="182.5" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="134.7" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="989.5" y1="133.7" x2="989.5" y2="178.5" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="139.2" width="2.35" height="25.2" fill="var(--down)"/>
<line x1="993.3" y1="100.5" x2="993.3" y2="161.8" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="105.6" width="2.35" height="52.2" fill="var(--up)"/>
<line x1="997.1" y1="74.3" x2="997.1" y2="113.3" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="101.3" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="1000.9" y1="104.0" x2="1000.9" y2="173.7" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="105.6" width="2.35" height="67.6" fill="var(--down)"/>
<line x1="1004.7" y1="150.6" x2="1004.7" y2="180.1" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="157.3" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="1008.5" y1="142.4" x2="1008.5" y2="174.5" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="150.4" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="1012.2" y1="156.2" x2="1012.2" y2="178.2" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="159.7" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="1016.0" y1="113.3" x2="1016.0" y2="160.2" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="117.2" width="2.35" height="42.7" fill="var(--up)"/>
<line x1="1019.8" y1="114.3" x2="1019.8" y2="161.8" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="118.8" width="2.35" height="28.4" fill="var(--down)"/>
<line x1="1023.6" y1="127.8" x2="1023.6" y2="158.1" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="145.6" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="1027.4" y1="123.1" x2="1027.4" y2="152.5" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="135.5" width="2.35" height="5.3" fill="var(--down)"/>
<line x1="1031.2" y1="115.4" x2="1031.2" y2="148.3" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="126.0" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="1035.0" y1="139.0" x2="1035.0" y2="168.7" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="141.6" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="1038.7" y1="155.9" x2="1038.7" y2="183.8" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="158.3" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="1042.5" y1="126.5" x2="1042.5" y2="176.9" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="127.1" width="2.35" height="46.1" fill="var(--up)"/>
<line x1="1046.3" y1="120.7" x2="1046.3" y2="179.5" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="126.8" width="2.35" height="49.0" fill="var(--down)"/>
<line x1="1050.1" y1="175.8" x2="1050.1" y2="185.6" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="179.0" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="60" y1="75.4" x2="1052" y2="75.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="78.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$35 R1</text>
<text x="1058" y="90.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="312.8" x2="1052" y2="312.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="306.8" font-size="11.5" fill="var(--support)" font-weight="600">$26 S1</text>
<text x="1058" y="318.8" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="536.1" x2="1052" y2="536.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="530.1" font-size="11.5" fill="var(--support)" font-weight="600">$17.39 S2</text>
<text x="1058" y="542.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="575.5" x2="1052" y2="575.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="569.5" font-size="11.5" fill="var(--support)" font-weight="600">$15.91 S3</text>
<text x="1058" y="581.5" font-size="9.5" fill="var(--muted)">터치 7회</text>
<circle cx="1052.0" cy="183.9" r="3" fill="var(--ink)"/>
<text x="1046.0" y="175.9" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $31 (2026-08-24)</text>
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
| R1 | $35 | 2 | 2026-03-23 · 2026-05-18 주 스윙 고점대. 5년 전체 최고가($34.81)를 포함하는 **미개척 상단** — 이 위로는 5년 안에 거래 이력이 없다 |
| **기준 종가** | **$30.98** (2026-08-21) | — | R1과 S1 사이. 다른 문서가 인용하는 값 |
| (차트 마지막 봉) | $30.67 (2026-08-24 주, 미완결) | — | 위 ??? 블록 참고 |
| S1 | $26 | 5 | 2024-12-16 · 2025-02-24 · 2025-08-18 · 2025-11-03 · 2025-12-15 주 스윙 저점대. **2024년 재평가 이후 1년 반 넘게 지켜진 현 레짐의 바닥** |
| 참고선 S2 | $17.39 | 2 | 2022-12-12 · 12-19 주. 2022년 레짐의 저점대로, 현재가 대비 −44% — 근시일 지지로 보지 않는다(아래 사유) |
| 참고선 S3 | $15.91 | 7 | 2021-09-20 · 2022-02-21 · 06-13 · 09-26 · 2023-03-20 · 05-29 · 2023-10-02 주. 5년 중 가장 터치가 많은 클러스터지만 **2021~2023년 저평가 국면 전체의 바닥**이라 현 레짐과 단절돼 있다 |

> S2·S3를 참고선으로 격하한 이유: 두 레벨은 모두 **주가가 $15~18 박스에 갇혀 있던 2021~2023년**의 흔적이다. 그 국면은 FY2023 말 Adjusted PER 16.5x로 대표되는 미드스트림 섹터 전반의 저평가기였고([밸류에이션 / 적정주가](./06_valuation.md) 2. 최근 3개년 — 적정주가 vs 실제주가), FY2024 이후 주가가 76% 오르며 레짐 자체가 바뀌었다. 터치 횟수(S3는 7회로 최다)만 보고 "강한 지지"로 읽으면 안 된다 — **현재가에서 그 레벨까지 가려면 이익이 아니라 배수가 3년 전으로 되돌아가야 한다.**

---

## 3. 관측된 특이 구간 — 2024년의 레짐 전환

- 2021년 8월부터 2023년 말까지 KMI 주가는 **$15~19 박스**에 3년 가까이 갇혀 있었다(위 참고선 S2·S3가 그 흔적이다). 이 기간 회사 실적은 나쁘지 않았고(Adjusted EBITDA FY2023 $7,561M), 배당도 매년 인상됐다 — 즉 **주가 정체는 실적이 아니라 시장이 미드스트림에 부여하는 배수의 문제였다.**
- 2024년 중 주가가 이 박스를 상향 돌파해 연말 $27.40으로 마감했다(연간 +55%). 같은 해 Adjusted EPS는 $1.07 → $1.15로 7.5% 늘었을 뿐이므로, **상승의 대부분은 배수 재평가**다 — [핵심 지표](./04_metrics.md) A.2에서 Adjusted PER이 16.5x → 23.8x(+44%)로 뛴 것이 이에 해당하며, 이익 증가(+7.5%)와 곱하면 실제 주가 상승률(+55%)이 그대로 설명된다. 배경은 데이터센터·LNG 수출發 천연가스 수요 기대의 부상이다.
- 그 뒤로는 새 레짐이 유지되고 있다 — S1($26)이 2024-12부터 2025-12까지 다섯 차례 지켜졌고, 상단은 2026년 상반기 $35 부근에서 두 번 막혔다. **즉 최근 1년 반은 $26~35 사이의 새 박스**이고, 현재가($30.98)는 그 한가운데 있다.
- 이 전환 때문에 5년 차트의 앞 3년과 뒤 2년은 사실상 다른 가격대의 이야기다. 4. 방법론 · 한계의 클러스터 계산은 5년 전체를 대상으로 하므로, **S2·S3처럼 앞 구간에서만 나온 레벨은 위 표에서 참고선으로 분리했다.**

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-23~2026-08-24. 수집 시점: 2026-08-24. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py KMI --name "Kinder Morgan" --interval 1wk --close-on 2026-08-21 --emit all` (레벨 날짜는 `--emit dates`로 별도 조회). 파라미터는 일봉 문서와 스윙 탐지 창(전후 4주 vs 5거래일)만 다르고 나머지는 같아, 두 문서 간 비교가 가능하다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **마지막 주봉이 미완결이다** — 위 ??? 블록 참고. 다음 갱신 시 이 봉의 값이 달라진다.
    - **기간 내 배당이 20회 지급됐으나 원주가 기준이라 반영되지 않았다.** 연 3.8~6.4%의 배당수익률([핵심 지표](./04_metrics.md) A.4)이 5년 내내 지급됐으므로, 총수익률로 보면 이 차트가 보여주는 상승폭보다 누적 20%p 이상 높다. **배당 비중이 큰 종목이라 이 차트만으로 투자 성과를 판단하면 크게 어긋난다.**
    - 5년 기간 내 주식분할·병합은 없어 가격 연속성을 깨는 이벤트는 없다.
    - **터치 횟수와 유효성이 비례하지 않는다** — 위 3. 관측된 특이 구간에서 설명한 레짐 전환 때문에, 터치가 가장 많은 S3($15.91, 7회)가 오히려 가장 참고 가치가 낮다.

---

*작성일: 2026-08-24*
