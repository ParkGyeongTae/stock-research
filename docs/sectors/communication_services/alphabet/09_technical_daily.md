# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **한 거래일 차이가 있다.** 이 차트의 마지막 봉은 2026-08-27 종가 $340.65인 반면, [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 기준 종가는 **2026-08-28의 $346.59**다. 수집 시점(2026-08-30)에 일봉 피드가 2026-08-28 봉을 아직 반영하지 않았기 때문이며, 같은 스크립트의 주봉 산출물과 시장 시세는 2026-08-28 $346.59로 일치한다. 배당·분할 조정 차이가 아니라 **데이터 반영 시차**이므로, 아래 레벨 표의 "현재가"는 차트와 같은 2026-08-27 종가를 그대로 두고 다른 문서는 2026-08-28 종가를 쓴다(차이 1.7%).

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

<div class="googl-chart">
<style>
.googl-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .googl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .googl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.googl-chart svg { width:100%; height:auto; display:block; }
.googl-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.googl-chart .title { fill: var(--ink); font-weight:600; }
.googl-chart .grid { stroke: var(--grid); stroke-width:1; }
.googl-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Alphabet(GOOGL) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Alphabet (GOOGL) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $340.65 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="493.4" x2="1052" y2="493.4" class="grid"/>
<text x="52" y="497.4" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="360.9" x2="1052" y2="360.9" class="grid"/>
<text x="52" y="364.9" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="228.3" x2="1052" y2="228.3" class="grid"/>
<text x="52" y="232.3" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="95.8" x2="1052" y2="95.8" class="grid"/>
<text x="52" y="99.8" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="66.0" y1="626.0" x2="66.0" y2="631.0" class="axis"/>
<text x="66.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="149.3" y1="626.0" x2="149.3" y2="631.0" class="axis"/>
<text x="149.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="240.5" y1="626.0" x2="240.5" y2="631.0" class="axis"/>
<text x="240.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="315.9" y1="626.0" x2="315.9" y2="631.0" class="axis"/>
<text x="315.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="403.2" y1="626.0" x2="403.2" y2="631.0" class="axis"/>
<text x="403.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="482.6" y1="626.0" x2="482.6" y2="631.0" class="axis"/>
<text x="482.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="558.0" y1="626.0" x2="558.0" y2="631.0" class="axis"/>
<text x="558.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="645.3" y1="626.0" x2="645.3" y2="631.0" class="axis"/>
<text x="645.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="728.6" y1="626.0" x2="728.6" y2="631.0" class="axis"/>
<text x="728.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="808.0" y1="626.0" x2="808.0" y2="631.0" class="axis"/>
<text x="808.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="891.3" y1="626.0" x2="891.3" y2="631.0" class="axis"/>
<text x="891.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="978.6" y1="626.0" x2="978.6" y2="631.0" class="axis"/>
<text x="978.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="587.2" x2="62.0" y2="599.0" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="591.8" width="2.46" height="6.4" fill="var(--up)"/>
<line x1="66.0" y1="595.0" x2="66.0" y2="609.6" stroke="var(--up)" class="wick"/>
<rect x="64.72" y="595.9" width="2.46" height="7.7" fill="var(--up)"/>
<line x1="69.9" y1="543.0" x2="69.9" y2="560.3" stroke="var(--up)" class="wick"/>
<rect x="68.69" y="544.7" width="2.46" height="11.8" fill="var(--up)"/>
<line x1="73.9" y1="540.2" x2="73.9" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="72.66" y="540.4" width="2.46" height="7.0" fill="var(--up)"/>
<line x1="77.9" y1="531.2" x2="77.9" y2="541.4" stroke="var(--up)" class="wick"/>
<rect x="76.63" y="533.2" width="2.46" height="7.4" fill="var(--up)"/>
<line x1="81.8" y1="524.9" x2="81.8" y2="536.7" stroke="var(--down)" class="wick"/>
<rect x="80.59" y="532.0" width="2.46" height="3.8" fill="var(--down)"/>
<line x1="85.8" y1="518.7" x2="85.8" y2="537.9" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="520.9" width="2.46" height="14.5" fill="var(--up)"/>
<line x1="89.8" y1="515.6" x2="89.8" y2="525.7" stroke="var(--up)" class="wick"/>
<rect x="88.53" y="522.2" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="93.7" y1="514.0" x2="93.7" y2="529.9" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="519.0" width="2.46" height="1.3" fill="var(--up)"/>
<line x1="97.7" y1="514.4" x2="97.7" y2="525.3" stroke="var(--up)" class="wick"/>
<rect x="96.47" y="517.8" width="2.46" height="1.1" fill="var(--up)"/>
<line x1="101.7" y1="487.1" x2="101.7" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="100.43" y="489.2" width="2.46" height="18.4" fill="var(--up)"/>
<line x1="105.6" y1="485.4" x2="105.6" y2="494.8" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="487.9" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="109.6" y1="489.2" x2="109.6" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="108.37" y="490.2" width="2.46" height="4.5" fill="var(--down)"/>
<line x1="113.6" y1="482.9" x2="113.6" y2="494.0" stroke="var(--up)" class="wick"/>
<rect x="112.34" y="488.1" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="117.5" y1="477.5" x2="117.5" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="116.31" y="480.9" width="2.46" height="3.9" fill="var(--up)"/>
<line x1="121.5" y1="478.1" x2="121.5" y2="492.6" stroke="var(--down)" class="wick"/>
<rect x="120.27" y="481.7" width="2.46" height="5.0" fill="var(--down)"/>
<line x1="125.5" y1="481.9" x2="125.5" y2="492.2" stroke="var(--down)" class="wick"/>
<rect x="124.24" y="485.4" width="2.46" height="3.7" fill="var(--down)"/>
<line x1="129.4" y1="487.2" x2="129.4" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="128.21" y="489.0" width="2.46" height="12.0" fill="var(--down)"/>
<line x1="133.4" y1="502.7" x2="133.4" y2="518.0" stroke="var(--up)" class="wick"/>
<rect x="132.18" y="504.6" width="2.46" height="3.7" fill="var(--up)"/>
<line x1="137.4" y1="495.0" x2="137.4" y2="504.1" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="501.2" width="2.46" height="1.4" fill="var(--down)"/>
<line x1="141.3" y1="490.4" x2="141.3" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="140.11" y="499.1" width="2.46" height="10.1" fill="var(--down)"/>
<line x1="145.3" y1="511.2" x2="145.3" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="511.7" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="149.3" y1="503.3" x2="149.3" y2="523.6" stroke="var(--up)" class="wick"/>
<rect x="148.05" y="507.0" width="2.46" height="11.0" fill="var(--up)"/>
<line x1="153.2" y1="501.9" x2="153.2" y2="513.9" stroke="var(--up)" class="wick"/>
<rect x="152.02" y="504.9" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="157.2" y1="503.3" x2="157.2" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="155.99" y="505.8" width="2.46" height="2.3" fill="var(--up)"/>
<line x1="161.2" y1="489.9" x2="161.2" y2="507.8" stroke="var(--up)" class="wick"/>
<rect x="159.95" y="492.3" width="2.46" height="15.0" fill="var(--up)"/>
<line x1="165.2" y1="492.3" x2="165.2" y2="505.3" stroke="var(--down)" class="wick"/>
<rect x="163.92" y="498.0" width="2.46" height="6.7" fill="var(--down)"/>
<line x1="169.1" y1="504.0" x2="169.1" y2="509.8" stroke="var(--down)" class="wick"/>
<rect x="167.89" y="506.8" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="173.1" y1="507.3" x2="173.1" y2="522.2" stroke="var(--down)" class="wick"/>
<rect x="171.86" y="508.1" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="177.1" y1="509.1" x2="177.1" y2="531.0" stroke="var(--down)" class="wick"/>
<rect x="175.83" y="516.2" width="2.46" height="12.9" fill="var(--down)"/>
<line x1="181.0" y1="508.0" x2="181.0" y2="520.7" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="509.0" width="2.46" height="10.4" fill="var(--up)"/>
<line x1="185.0" y1="501.1" x2="185.0" y2="518.6" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="505.5" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="189.0" y1="487.8" x2="189.0" y2="504.1" stroke="var(--up)" class="wick"/>
<rect x="187.73" y="490.7" width="2.46" height="10.0" fill="var(--up)"/>
<line x1="192.9" y1="475.0" x2="192.9" y2="493.2" stroke="var(--down)" class="wick"/>
<rect x="191.70" y="488.7" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="196.9" y1="482.3" x2="196.9" y2="499.2" stroke="var(--up)" class="wick"/>
<rect x="195.67" y="484.7" width="2.46" height="6.7" fill="var(--up)"/>
<line x1="200.9" y1="474.0" x2="200.9" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="199.63" y="476.1" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="204.8" y1="480.5" x2="204.8" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="203.60" y="480.9" width="2.46" height="11.3" fill="var(--down)"/>
<line x1="208.8" y1="476.6" x2="208.8" y2="495.3" stroke="var(--down)" class="wick"/>
<rect x="207.57" y="481.9" width="2.46" height="7.1" fill="var(--down)"/>
<line x1="212.8" y1="480.1" x2="212.8" y2="488.5" stroke="var(--up)" class="wick"/>
<rect x="211.54" y="485.3" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="216.7" y1="462.5" x2="216.7" y2="479.3" stroke="var(--up)" class="wick"/>
<rect x="215.51" y="467.1" width="2.46" height="8.9" fill="var(--up)"/>
<line x1="220.7" y1="440.0" x2="220.7" y2="455.6" stroke="var(--up)" class="wick"/>
<rect x="219.47" y="442.4" width="2.46" height="11.8" fill="var(--up)"/>
<line x1="224.7" y1="438.5" x2="224.7" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="223.44" y="441.2" width="2.46" height="5.9" fill="var(--down)"/>
<line x1="228.6" y1="426.3" x2="228.6" y2="446.6" stroke="var(--up)" class="wick"/>
<rect x="227.41" y="428.3" width="2.46" height="18.1" fill="var(--up)"/>
<line x1="232.6" y1="383.2" x2="232.6" y2="413.7" stroke="var(--down)" class="wick"/>
<rect x="231.38" y="383.2" width="2.46" height="26.8" fill="var(--down)"/>
<line x1="236.6" y1="398.0" x2="236.6" y2="421.8" stroke="var(--down)" class="wick"/>
<rect x="235.35" y="405.4" width="2.46" height="5.4" fill="var(--down)"/>
<line x1="240.5" y1="399.2" x2="240.5" y2="414.4" stroke="var(--up)" class="wick"/>
<rect x="239.31" y="404.0" width="2.46" height="4.1" fill="var(--up)"/>
<line x1="244.5" y1="410.5" x2="244.5" y2="423.8" stroke="var(--up)" class="wick"/>
<rect x="243.28" y="420.4" width="2.46" height="2.1" fill="var(--up)"/>
<line x1="248.5" y1="396.9" x2="248.5" y2="421.0" stroke="var(--up)" class="wick"/>
<rect x="247.25" y="402.5" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="252.4" y1="391.8" x2="252.4" y2="410.9" stroke="var(--down)" class="wick"/>
<rect x="251.22" y="399.8" width="2.46" height="1.5" fill="var(--down)"/>
<line x1="256.4" y1="403.9" x2="256.4" y2="426.7" stroke="var(--down)" class="wick"/>
<rect x="255.19" y="405.4" width="2.46" height="11.6" fill="var(--down)"/>
<line x1="260.4" y1="385.3" x2="260.4" y2="406.3" stroke="var(--up)" class="wick"/>
<rect x="259.15" y="387.1" width="2.46" height="15.1" fill="var(--up)"/>
<line x1="264.4" y1="382.3" x2="264.4" y2="394.5" stroke="var(--up)" class="wick"/>
<rect x="263.12" y="383.9" width="2.46" height="9.4" fill="var(--up)"/>
<line x1="268.3" y1="382.1" x2="268.3" y2="404.1" stroke="var(--down)" class="wick"/>
<rect x="267.09" y="382.9" width="2.46" height="13.2" fill="var(--down)"/>
<line x1="272.3" y1="406.4" x2="272.3" y2="421.2" stroke="var(--down)" class="wick"/>
<rect x="271.06" y="407.7" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="276.3" y1="417.7" x2="276.3" y2="438.6" stroke="var(--up)" class="wick"/>
<rect x="275.03" y="423.4" width="2.46" height="13.3" fill="var(--up)"/>
<line x1="280.2" y1="376.9" x2="280.2" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="398.6" width="2.46" height="2.0" fill="var(--down)"/>
<line x1="284.2" y1="390.6" x2="284.2" y2="418.7" stroke="var(--down)" class="wick"/>
<rect x="282.96" y="392.9" width="2.46" height="9.7" fill="var(--down)"/>
<line x1="288.2" y1="350.8" x2="288.2" y2="396.3" stroke="var(--up)" class="wick"/>
<rect x="286.93" y="379.9" width="2.46" height="15.0" fill="var(--up)"/>
<line x1="292.1" y1="343.9" x2="292.1" y2="390.9" stroke="var(--down)" class="wick"/>
<rect x="290.90" y="348.8" width="2.46" height="40.0" fill="var(--down)"/>
<line x1="296.1" y1="350.5" x2="296.1" y2="377.2" stroke="var(--up)" class="wick"/>
<rect x="294.87" y="361.8" width="2.46" height="8.6" fill="var(--up)"/>
<line x1="300.1" y1="309.2" x2="300.1" y2="335.4" stroke="var(--up)" class="wick"/>
<rect x="298.83" y="311.6" width="2.46" height="19.8" fill="var(--up)"/>
<line x1="304.0" y1="284.5" x2="304.0" y2="314.1" stroke="var(--down)" class="wick"/>
<rect x="302.80" y="291.4" width="2.46" height="7.3" fill="var(--down)"/>
<line x1="308.0" y1="295.9" x2="308.0" y2="316.4" stroke="var(--down)" class="wick"/>
<rect x="306.77" y="306.1" width="2.46" height="1.9" fill="var(--down)"/>
<line x1="312.0" y1="289.7" x2="312.0" y2="316.4" stroke="var(--down)" class="wick"/>
<rect x="310.74" y="298.9" width="2.46" height="8.5" fill="var(--down)"/>
<line x1="315.9" y1="308.3" x2="315.9" y2="324.1" stroke="var(--down)" class="wick"/>
<rect x="314.71" y="314.0" width="2.46" height="7.4" fill="var(--down)"/>
<line x1="319.9" y1="312.2" x2="319.9" y2="324.0" stroke="var(--down)" class="wick"/>
<rect x="318.67" y="316.5" width="2.46" height="2.5" fill="var(--down)"/>
<line x1="323.9" y1="303.7" x2="323.9" y2="323.5" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="308.8" width="2.46" height="9.9" fill="var(--up)"/>
<line x1="327.8" y1="301.6" x2="327.8" y2="321.9" stroke="var(--down)" class="wick"/>
<rect x="326.61" y="301.9" width="2.46" height="12.2" fill="var(--down)"/>
<line x1="331.8" y1="299.5" x2="331.8" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="330.58" y="304.5" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="335.8" y1="306.7" x2="335.8" y2="331.1" stroke="var(--down)" class="wick"/>
<rect x="334.55" y="307.7" width="2.46" height="16.8" fill="var(--down)"/>
<line x1="339.7" y1="313.2" x2="339.7" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="338.51" y="315.6" width="2.46" height="12.5" fill="var(--up)"/>
<line x1="343.7" y1="304.4" x2="343.7" y2="322.0" stroke="var(--up)" class="wick"/>
<rect x="342.48" y="307.3" width="2.46" height="11.6" fill="var(--up)"/>
<line x1="347.7" y1="304.9" x2="347.7" y2="338.1" stroke="var(--down)" class="wick"/>
<rect x="346.45" y="307.6" width="2.46" height="20.3" fill="var(--down)"/>
<line x1="351.6" y1="321.5" x2="351.6" y2="346.1" stroke="var(--down)" class="wick"/>
<rect x="350.42" y="324.6" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="355.6" y1="330.6" x2="355.6" y2="347.9" stroke="var(--down)" class="wick"/>
<rect x="354.39" y="330.9" width="2.46" height="8.2" fill="var(--down)"/>
<line x1="359.6" y1="332.3" x2="359.6" y2="354.0" stroke="var(--up)" class="wick"/>
<rect x="358.35" y="343.5" width="2.46" height="4.3" fill="var(--up)"/>
<line x1="363.6" y1="339.4" x2="363.6" y2="371.2" stroke="var(--down)" class="wick"/>
<rect x="362.32" y="339.6" width="2.46" height="29.9" fill="var(--down)"/>
<line x1="367.5" y1="350.4" x2="367.5" y2="362.9" stroke="var(--up)" class="wick"/>
<rect x="366.29" y="354.4" width="2.46" height="2.0" fill="var(--up)"/>
<line x1="371.5" y1="341.7" x2="371.5" y2="358.3" stroke="var(--up)" class="wick"/>
<rect x="370.26" y="341.9" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="375.5" y1="334.0" x2="375.5" y2="346.8" stroke="var(--down)" class="wick"/>
<rect x="374.23" y="334.7" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="379.4" y1="321.3" x2="379.4" y2="336.2" stroke="var(--up)" class="wick"/>
<rect x="378.19" y="322.8" width="2.46" height="12.5" fill="var(--up)"/>
<line x1="383.4" y1="320.9" x2="383.4" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="382.16" y="321.7" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="387.4" y1="320.9" x2="387.4" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="386.13" y="322.5" width="2.46" height="2.6" fill="var(--down)"/>
<line x1="391.3" y1="323.7" x2="391.3" y2="332.7" stroke="var(--up)" class="wick"/>
<rect x="390.10" y="324.9" width="2.46" height="5.8" fill="var(--up)"/>
<line x1="395.3" y1="315.9" x2="395.3" y2="327.9" stroke="var(--up)" class="wick"/>
<rect x="394.07" y="324.2" width="2.46" height="3.6" fill="var(--up)"/>
<line x1="399.3" y1="322.2" x2="399.3" y2="330.6" stroke="var(--up)" class="wick"/>
<rect x="398.03" y="326.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="403.2" y1="301.2" x2="403.2" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="402.00" y="316.1" width="2.46" height="4.6" fill="var(--down)"/>
<line x1="407.2" y1="310.5" x2="407.2" y2="322.1" stroke="var(--down)" class="wick"/>
<rect x="405.97" y="314.1" width="2.46" height="3.0" fill="var(--down)"/>
<line x1="411.2" y1="305.4" x2="411.2" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="409.94" y="317.4" width="2.46" height="5.5" fill="var(--down)"/>
<line x1="415.1" y1="291.6" x2="415.1" y2="323.3" stroke="var(--up)" class="wick"/>
<rect x="413.91" y="302.6" width="2.46" height="20.2" fill="var(--up)"/>
<line x1="419.1" y1="280.5" x2="419.1" y2="303.9" stroke="var(--down)" class="wick"/>
<rect x="417.87" y="284.1" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="423.1" y1="279.1" x2="423.1" y2="292.5" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="285.1" width="2.46" height="3.9" fill="var(--up)"/>
<line x1="427.0" y1="270.6" x2="427.0" y2="294.6" stroke="var(--up)" class="wick"/>
<rect x="425.81" y="276.4" width="2.46" height="16.1" fill="var(--up)"/>
<line x1="431.0" y1="253.5" x2="431.0" y2="271.8" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="265.5" width="2.46" height="2.7" fill="var(--up)"/>
<line x1="435.0" y1="264.1" x2="435.0" y2="280.1" stroke="var(--up)" class="wick"/>
<rect x="433.75" y="265.9" width="2.46" height="2.1" fill="var(--up)"/>
<line x1="438.9" y1="261.0" x2="438.9" y2="279.4" stroke="var(--down)" class="wick"/>
<rect x="437.71" y="261.1" width="2.46" height="12.9" fill="var(--down)"/>
<line x1="442.9" y1="269.0" x2="442.9" y2="287.4" stroke="var(--down)" class="wick"/>
<rect x="441.68" y="269.7" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="446.9" y1="287.4" x2="446.9" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="445.65" y="302.6" width="2.46" height="3.0" fill="var(--up)"/>
<line x1="450.8" y1="274.8" x2="450.8" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="449.62" y="285.6" width="2.46" height="19.8" fill="var(--up)"/>
<line x1="454.8" y1="267.7" x2="454.8" y2="284.7" stroke="var(--down)" class="wick"/>
<rect x="453.59" y="269.6" width="2.46" height="10.4" fill="var(--down)"/>
<line x1="458.8" y1="271.6" x2="458.8" y2="288.1" stroke="var(--down)" class="wick"/>
<rect x="457.55" y="274.7" width="2.46" height="12.1" fill="var(--down)"/>
<line x1="462.8" y1="265.9" x2="462.8" y2="289.3" stroke="var(--up)" class="wick"/>
<rect x="461.52" y="272.7" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="466.7" y1="260.4" x2="466.7" y2="272.1" stroke="var(--down)" class="wick"/>
<rect x="465.49" y="267.1" width="2.46" height="2.2" fill="var(--down)"/>
<line x1="470.7" y1="261.4" x2="470.7" y2="276.2" stroke="var(--down)" class="wick"/>
<rect x="469.46" y="265.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="474.7" y1="248.8" x2="474.7" y2="290.5" stroke="var(--down)" class="wick"/>
<rect x="473.43" y="254.0" width="2.46" height="5.4" fill="var(--down)"/>
<line x1="478.6" y1="254.8" x2="478.6" y2="275.3" stroke="var(--down)" class="wick"/>
<rect x="477.39" y="254.8" width="2.46" height="5.3" fill="var(--down)"/>
<line x1="482.6" y1="242.0" x2="482.6" y2="266.4" stroke="var(--up)" class="wick"/>
<rect x="481.36" y="245.1" width="2.46" height="19.8" fill="var(--up)"/>
<line x1="486.6" y1="231.0" x2="486.6" y2="261.5" stroke="var(--down)" class="wick"/>
<rect x="485.33" y="235.4" width="2.46" height="20.2" fill="var(--down)"/>
<line x1="490.5" y1="246.1" x2="490.5" y2="285.3" stroke="var(--down)" class="wick"/>
<rect x="489.30" y="247.0" width="2.46" height="26.3" fill="var(--down)"/>
<line x1="494.5" y1="274.2" x2="494.5" y2="343.8" stroke="var(--up)" class="wick"/>
<rect x="493.27" y="278.0" width="2.46" height="50.5" fill="var(--up)"/>
<line x1="498.5" y1="280.3" x2="498.5" y2="308.1" stroke="var(--down)" class="wick"/>
<rect x="497.23" y="288.8" width="2.46" height="11.5" fill="var(--down)"/>
<line x1="502.4" y1="287.4" x2="502.4" y2="315.1" stroke="var(--up)" class="wick"/>
<rect x="501.20" y="296.4" width="2.46" height="9.0" fill="var(--up)"/>
<line x1="506.4" y1="303.4" x2="506.4" y2="322.2" stroke="var(--down)" class="wick"/>
<rect x="505.17" y="305.3" width="2.46" height="6.3" fill="var(--down)"/>
<line x1="510.4" y1="305.1" x2="510.4" y2="335.3" stroke="var(--down)" class="wick"/>
<rect x="509.14" y="310.6" width="2.46" height="21.2" fill="var(--down)"/>
<line x1="514.3" y1="317.8" x2="514.3" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="513.11" y="328.8" width="2.46" height="8.2" fill="var(--down)"/>
<line x1="518.3" y1="338.0" x2="518.3" y2="351.0" stroke="var(--down)" class="wick"/>
<rect x="517.07" y="340.4" width="2.46" height="5.3" fill="var(--down)"/>
<line x1="522.3" y1="349.1" x2="522.3" y2="370.8" stroke="var(--up)" class="wick"/>
<rect x="521.04" y="355.5" width="2.46" height="5.2" fill="var(--up)"/>
<line x1="526.2" y1="346.6" x2="526.2" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="525.01" y="352.1" width="2.46" height="3.3" fill="var(--up)"/>
<line x1="530.2" y1="346.4" x2="530.2" y2="360.8" stroke="var(--up)" class="wick"/>
<rect x="528.98" y="353.3" width="2.46" height="2.7" fill="var(--up)"/>
<line x1="534.2" y1="317.1" x2="534.2" y2="350.5" stroke="var(--up)" class="wick"/>
<rect x="532.95" y="321.2" width="2.46" height="28.3" fill="var(--up)"/>
<line x1="538.1" y1="309.1" x2="538.1" y2="334.7" stroke="var(--down)" class="wick"/>
<rect x="536.91" y="310.4" width="2.46" height="20.0" fill="var(--down)"/>
<line x1="542.1" y1="328.4" x2="542.1" y2="345.2" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="332.0" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="546.1" y1="324.7" x2="546.1" y2="335.9" stroke="var(--up)" class="wick"/>
<rect x="544.85" y="326.7" width="2.46" height="2.2" fill="var(--up)"/>
<line x1="550.0" y1="326.0" x2="550.0" y2="354.7" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="327.4" width="2.46" height="13.9" fill="var(--down)"/>
<line x1="554.0" y1="328.1" x2="554.0" y2="350.8" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="329.7" width="2.46" height="20.2" fill="var(--up)"/>
<line x1="558.0" y1="338.4" x2="558.0" y2="357.4" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="343.6" width="2.46" height="8.7" fill="var(--up)"/>
<line x1="562.0" y1="350.4" x2="562.0" y2="369.6" stroke="var(--up)" class="wick"/>
<rect x="560.72" y="351.4" width="2.46" height="13.2" fill="var(--up)"/>
<line x1="565.9" y1="346.4" x2="565.9" y2="358.9" stroke="var(--up)" class="wick"/>
<rect x="564.69" y="352.6" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="569.9" y1="352.1" x2="569.9" y2="366.2" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="352.8" width="2.46" height="5.7" fill="var(--down)"/>
<line x1="573.9" y1="359.5" x2="573.9" y2="373.7" stroke="var(--up)" class="wick"/>
<rect x="572.63" y="364.8" width="2.46" height="6.4" fill="var(--up)"/>
<line x1="577.8" y1="342.9" x2="577.8" y2="376.6" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="344.0" width="2.46" height="31.8" fill="var(--up)"/>
<line x1="581.8" y1="335.7" x2="581.8" y2="346.1" stroke="var(--up)" class="wick"/>
<rect x="580.56" y="342.2" width="2.46" height="2.3" fill="var(--up)"/>
<line x1="585.8" y1="330.6" x2="585.8" y2="345.2" stroke="var(--up)" class="wick"/>
<rect x="584.53" y="337.8" width="2.46" height="5.2" fill="var(--up)"/>
<line x1="589.7" y1="337.2" x2="589.7" y2="358.2" stroke="var(--down)" class="wick"/>
<rect x="588.50" y="342.8" width="2.46" height="8.7" fill="var(--down)"/>
<line x1="593.7" y1="340.5" x2="593.7" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="592.47" y="342.3" width="2.46" height="12.5" fill="var(--down)"/>
<line x1="597.7" y1="343.7" x2="597.7" y2="352.9" stroke="var(--up)" class="wick"/>
<rect x="596.43" y="346.1" width="2.46" height="3.2" fill="var(--up)"/>
<line x1="601.6" y1="330.6" x2="601.6" y2="346.3" stroke="var(--up)" class="wick"/>
<rect x="600.40" y="331.9" width="2.46" height="13.4" fill="var(--up)"/>
<line x1="605.6" y1="327.8" x2="605.6" y2="342.5" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="336.3" width="2.46" height="4.2" fill="var(--down)"/>
<line x1="609.6" y1="339.5" x2="609.6" y2="354.7" stroke="var(--up)" class="wick"/>
<rect x="608.34" y="342.0" width="2.46" height="8.3" fill="var(--up)"/>
<line x1="613.5" y1="345.0" x2="613.5" y2="365.5" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="346.4" width="2.46" height="11.8" fill="var(--down)"/>
<line x1="617.5" y1="345.0" x2="617.5" y2="358.4" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="355.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="621.5" y1="361.1" x2="621.5" y2="386.5" stroke="var(--down)" class="wick"/>
<rect x="620.24" y="363.0" width="2.46" height="23.2" fill="var(--down)"/>
<line x1="625.4" y1="371.5" x2="625.4" y2="389.4" stroke="var(--down)" class="wick"/>
<rect x="624.21" y="378.3" width="2.46" height="6.7" fill="var(--down)"/>
<line x1="629.4" y1="392.8" x2="629.4" y2="417.9" stroke="var(--down)" class="wick"/>
<rect x="628.18" y="392.9" width="2.46" height="18.5" fill="var(--down)"/>
<line x1="633.4" y1="415.6" x2="633.4" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="632.15" y="421.1" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="637.3" y1="421.6" x2="637.3" y2="434.8" stroke="var(--down)" class="wick"/>
<rect x="636.11" y="423.4" width="2.46" height="7.7" fill="var(--down)"/>
<line x1="641.3" y1="392.5" x2="641.3" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="640.08" y="393.9" width="2.46" height="25.2" fill="var(--up)"/>
<line x1="645.3" y1="359.5" x2="645.3" y2="386.3" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="367.8" width="2.46" height="17.4" fill="var(--up)"/>
<line x1="649.2" y1="366.0" x2="649.2" y2="388.9" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="372.1" width="2.46" height="13.5" fill="var(--up)"/>
<line x1="653.2" y1="359.2" x2="653.2" y2="373.7" stroke="var(--up)" class="wick"/>
<rect x="651.99" y="360.9" width="2.46" height="10.9" fill="var(--up)"/>
<line x1="657.2" y1="346.0" x2="657.2" y2="366.9" stroke="var(--up)" class="wick"/>
<rect x="655.95" y="346.4" width="2.46" height="7.2" fill="var(--up)"/>
<line x1="661.2" y1="302.3" x2="661.2" y2="321.1" stroke="var(--down)" class="wick"/>
<rect x="659.92" y="306.7" width="2.46" height="8.3" fill="var(--down)"/>
<line x1="665.1" y1="309.1" x2="665.1" y2="331.6" stroke="var(--up)" class="wick"/>
<rect x="663.89" y="311.9" width="2.46" height="6.8" fill="var(--up)"/>
<line x1="669.1" y1="303.0" x2="669.1" y2="317.6" stroke="var(--down)" class="wick"/>
<rect x="667.86" y="307.8" width="2.46" height="7.4" fill="var(--down)"/>
<line x1="673.1" y1="303.5" x2="673.1" y2="319.9" stroke="var(--up)" class="wick"/>
<rect x="671.83" y="304.4" width="2.46" height="11.1" fill="var(--up)"/>
<line x1="677.0" y1="272.6" x2="677.0" y2="297.9" stroke="var(--up)" class="wick"/>
<rect x="675.79" y="273.6" width="2.46" height="21.5" fill="var(--up)"/>
<line x1="681.0" y1="261.5" x2="681.0" y2="279.0" stroke="var(--up)" class="wick"/>
<rect x="679.76" y="262.5" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="685.0" y1="255.2" x2="685.0" y2="269.4" stroke="var(--down)" class="wick"/>
<rect x="683.73" y="258.2" width="2.46" height="7.2" fill="var(--down)"/>
<line x1="688.9" y1="248.7" x2="688.9" y2="264.8" stroke="var(--up)" class="wick"/>
<rect x="687.70" y="250.4" width="2.46" height="10.7" fill="var(--up)"/>
<line x1="692.9" y1="251.1" x2="692.9" y2="263.8" stroke="var(--down)" class="wick"/>
<rect x="691.67" y="252.8" width="2.46" height="8.9" fill="var(--down)"/>
<line x1="696.9" y1="256.6" x2="696.9" y2="277.8" stroke="var(--down)" class="wick"/>
<rect x="695.63" y="261.0" width="2.46" height="14.3" fill="var(--down)"/>
<line x1="700.8" y1="255.3" x2="700.8" y2="267.6" stroke="var(--up)" class="wick"/>
<rect x="699.60" y="256.6" width="2.46" height="6.1" fill="var(--up)"/>
<line x1="704.8" y1="249.6" x2="704.8" y2="265.0" stroke="var(--down)" class="wick"/>
<rect x="703.57" y="251.7" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="708.8" y1="240.9" x2="708.8" y2="267.1" stroke="var(--up)" class="wick"/>
<rect x="707.54" y="243.2" width="2.46" height="15.0" fill="var(--up)"/>
<line x1="712.7" y1="219.9" x2="712.7" y2="247.6" stroke="var(--up)" class="wick"/>
<rect x="711.51" y="227.4" width="2.46" height="11.6" fill="var(--up)"/>
<line x1="716.7" y1="221.9" x2="716.7" y2="238.6" stroke="var(--up)" class="wick"/>
<rect x="715.47" y="228.9" width="2.46" height="3.3" fill="var(--up)"/>
<line x1="720.7" y1="213.0" x2="720.7" y2="243.7" stroke="var(--up)" class="wick"/>
<rect x="719.44" y="228.5" width="2.46" height="6.3" fill="var(--up)"/>
<line x1="724.6" y1="133.3" x2="724.6" y2="186.4" stroke="var(--up)" class="wick"/>
<rect x="723.41" y="136.1" width="2.46" height="28.4" fill="var(--up)"/>
<line x1="728.6" y1="130.9" x2="728.6" y2="151.3" stroke="var(--up)" class="wick"/>
<rect x="727.38" y="133.7" width="2.46" height="10.8" fill="var(--up)"/>
<line x1="732.6" y1="129.2" x2="732.6" y2="149.3" stroke="var(--down)" class="wick"/>
<rect x="731.35" y="133.9" width="2.46" height="6.3" fill="var(--down)"/>
<line x1="736.5" y1="114.8" x2="736.5" y2="138.1" stroke="var(--up)" class="wick"/>
<rect x="735.31" y="126.4" width="2.46" height="5.8" fill="var(--up)"/>
<line x1="740.5" y1="96.2" x2="740.5" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="739.28" y="101.0" width="2.46" height="10.0" fill="var(--up)"/>
<line x1="744.5" y1="95.5" x2="744.5" y2="115.2" stroke="var(--down)" class="wick"/>
<rect x="743.25" y="96.0" width="2.46" height="5.1" fill="var(--down)"/>
<line x1="748.4" y1="90.5" x2="748.4" y2="105.4" stroke="var(--up)" class="wick"/>
<rect x="747.22" y="93.6" width="2.46" height="10.1" fill="var(--up)"/>
<line x1="752.4" y1="102.6" x2="752.4" y2="126.3" stroke="var(--down)" class="wick"/>
<rect x="751.19" y="112.6" width="2.46" height="13.3" fill="var(--down)"/>
<line x1="756.4" y1="126.2" x2="756.4" y2="141.4" stroke="var(--up)" class="wick"/>
<rect x="755.15" y="129.3" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="760.4" y1="86.0" x2="760.4" y2="135.5" stroke="var(--up)" class="wick"/>
<rect x="759.12" y="88.8" width="2.46" height="45.1" fill="var(--up)"/>
<line x1="764.3" y1="88.0" x2="764.3" y2="106.8" stroke="var(--up)" class="wick"/>
<rect x="763.09" y="92.9" width="2.46" height="10.0" fill="var(--up)"/>
<line x1="768.3" y1="97.0" x2="768.3" y2="113.8" stroke="var(--up)" class="wick"/>
<rect x="767.06" y="104.3" width="2.46" height="1.2" fill="var(--up)"/>
<line x1="772.3" y1="72.9" x2="772.3" y2="110.3" stroke="var(--up)" class="wick"/>
<rect x="771.03" y="103.9" width="2.46" height="3.3" fill="var(--up)"/>
<line x1="776.2" y1="103.3" x2="776.2" y2="132.6" stroke="var(--down)" class="wick"/>
<rect x="774.99" y="103.8" width="2.46" height="24.7" fill="var(--down)"/>
<line x1="780.2" y1="112.0" x2="780.2" y2="141.1" stroke="var(--up)" class="wick"/>
<rect x="778.96" y="125.2" width="2.46" height="3.2" fill="var(--up)"/>
<line x1="784.2" y1="115.7" x2="784.2" y2="140.8" stroke="var(--up)" class="wick"/>
<rect x="782.93" y="128.5" width="2.46" height="5.2" fill="var(--up)"/>
<line x1="788.1" y1="125.6" x2="788.1" y2="144.1" stroke="var(--down)" class="wick"/>
<rect x="786.90" y="129.3" width="2.46" height="11.6" fill="var(--down)"/>
<line x1="792.1" y1="124.2" x2="792.1" y2="141.9" stroke="var(--up)" class="wick"/>
<rect x="790.87" y="125.2" width="2.46" height="11.6" fill="var(--up)"/>
<line x1="796.1" y1="112.0" x2="796.1" y2="133.1" stroke="var(--up)" class="wick"/>
<rect x="794.83" y="125.4" width="2.46" height="5.7" fill="var(--up)"/>
<line x1="800.0" y1="117.3" x2="800.0" y2="135.1" stroke="var(--up)" class="wick"/>
<rect x="798.80" y="121.9" width="2.46" height="5.6" fill="var(--up)"/>
<line x1="804.0" y1="134.9" x2="804.0" y2="152.9" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="134.9" width="2.46" height="13.0" fill="var(--down)"/>
<line x1="808.0" y1="152.6" x2="808.0" y2="166.0" stroke="var(--down)" class="wick"/>
<rect x="806.74" y="158.0" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="811.9" y1="165.9" x2="811.9" y2="205.9" stroke="var(--down)" class="wick"/>
<rect x="810.71" y="184.3" width="2.46" height="12.6" fill="var(--down)"/>
<line x1="815.9" y1="184.7" x2="815.9" y2="206.9" stroke="var(--down)" class="wick"/>
<rect x="814.67" y="196.4" width="2.46" height="8.1" fill="var(--down)"/>
<line x1="819.9" y1="166.7" x2="819.9" y2="206.6" stroke="var(--up)" class="wick"/>
<rect x="818.64" y="169.5" width="2.46" height="35.2" fill="var(--up)"/>
<line x1="823.8" y1="169.8" x2="823.8" y2="190.9" stroke="var(--up)" class="wick"/>
<rect x="822.61" y="179.2" width="2.46" height="5.8" fill="var(--up)"/>
<line x1="827.8" y1="185.4" x2="827.8" y2="200.4" stroke="var(--down)" class="wick"/>
<rect x="826.58" y="188.1" width="2.46" height="5.0" fill="var(--down)"/>
<line x1="831.8" y1="169.8" x2="831.8" y2="209.0" stroke="var(--down)" class="wick"/>
<rect x="830.55" y="183.0" width="2.46" height="7.5" fill="var(--down)"/>
<line x1="835.7" y1="179.1" x2="835.7" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="834.51" y="193.4" width="2.46" height="18.1" fill="var(--down)"/>
<line x1="839.7" y1="205.0" x2="839.7" y2="238.0" stroke="var(--up)" class="wick"/>
<rect x="838.48" y="207.7" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="843.7" y1="184.4" x2="843.7" y2="215.2" stroke="var(--down)" class="wick"/>
<rect x="842.45" y="194.9" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="847.6" y1="167.4" x2="847.6" y2="184.4" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="177.0" width="2.46" height="3.8" fill="var(--up)"/>
<line x1="851.6" y1="159.4" x2="851.6" y2="183.1" stroke="var(--up)" class="wick"/>
<rect x="850.39" y="166.7" width="2.46" height="9.7" fill="var(--up)"/>
<line x1="855.6" y1="169.1" x2="855.6" y2="196.5" stroke="var(--down)" class="wick"/>
<rect x="854.35" y="177.6" width="2.46" height="14.2" fill="var(--down)"/>
<line x1="859.6" y1="176.7" x2="859.6" y2="205.3" stroke="var(--up)" class="wick"/>
<rect x="858.32" y="180.5" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="863.5" y1="204.7" x2="863.5" y2="250.3" stroke="var(--down)" class="wick"/>
<rect x="862.29" y="207.2" width="2.46" height="21.9" fill="var(--down)"/>
<line x1="867.5" y1="230.2" x2="867.5" y2="254.3" stroke="var(--up)" class="wick"/>
<rect x="866.26" y="238.6" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="871.5" y1="219.1" x2="871.5" y2="249.7" stroke="var(--down)" class="wick"/>
<rect x="870.23" y="230.9" width="2.46" height="9.9" fill="var(--down)"/>
<line x1="875.4" y1="240.1" x2="875.4" y2="265.9" stroke="var(--up)" class="wick"/>
<rect x="874.19" y="245.0" width="2.46" height="18.5" fill="var(--up)"/>
<line x1="879.4" y1="238.0" x2="879.4" y2="280.8" stroke="var(--down)" class="wick"/>
<rect x="878.16" y="248.1" width="2.46" height="13.7" fill="var(--down)"/>
<line x1="883.4" y1="216.8" x2="883.4" y2="253.1" stroke="var(--up)" class="wick"/>
<rect x="882.13" y="218.6" width="2.46" height="31.3" fill="var(--up)"/>
<line x1="887.3" y1="205.5" x2="887.3" y2="227.3" stroke="var(--up)" class="wick"/>
<rect x="886.10" y="208.8" width="2.46" height="9.3" fill="var(--up)"/>
<line x1="891.3" y1="193.9" x2="891.3" y2="211.3" stroke="var(--up)" class="wick"/>
<rect x="890.07" y="198.6" width="2.46" height="7.5" fill="var(--up)"/>
<line x1="895.3" y1="190.7" x2="895.3" y2="219.3" stroke="var(--up)" class="wick"/>
<rect x="894.03" y="202.1" width="2.46" height="1.1" fill="var(--up)"/>
<line x1="899.2" y1="180.8" x2="899.2" y2="208.8" stroke="var(--up)" class="wick"/>
<rect x="898.00" y="184.7" width="2.46" height="13.0" fill="var(--up)"/>
<line x1="903.2" y1="166.9" x2="903.2" y2="187.2" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="177.8" width="2.46" height="5.4" fill="var(--down)"/>
<line x1="907.2" y1="181.0" x2="907.2" y2="207.1" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="189.2" width="2.46" height="7.5" fill="var(--down)"/>
<line x1="911.1" y1="202.7" x2="911.1" y2="225.5" stroke="var(--up)" class="wick"/>
<rect x="909.91" y="204.8" width="2.46" height="12.1" fill="var(--up)"/>
<line x1="915.1" y1="207.6" x2="915.1" y2="221.0" stroke="var(--down)" class="wick"/>
<rect x="913.87" y="208.4" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="919.1" y1="206.8" x2="919.1" y2="223.7" stroke="var(--down)" class="wick"/>
<rect x="917.84" y="211.9" width="2.46" height="9.8" fill="var(--down)"/>
<line x1="923.0" y1="201.4" x2="923.0" y2="225.4" stroke="var(--up)" class="wick"/>
<rect x="921.81" y="203.1" width="2.46" height="22.0" fill="var(--up)"/>
<line x1="927.0" y1="165.6" x2="927.0" y2="207.8" stroke="var(--up)" class="wick"/>
<rect x="925.78" y="172.9" width="2.46" height="34.3" fill="var(--up)"/>
<line x1="931.0" y1="161.3" x2="931.0" y2="222.2" stroke="var(--down)" class="wick"/>
<rect x="929.75" y="167.2" width="2.46" height="49.3" fill="var(--down)"/>
<line x1="934.9" y1="232.2" x2="934.9" y2="251.2" stroke="var(--up)" class="wick"/>
<rect x="933.71" y="236.9" width="2.46" height="2.0" fill="var(--up)"/>
<line x1="938.9" y1="202.7" x2="938.9" y2="226.9" stroke="var(--up)" class="wick"/>
<rect x="937.68" y="223.0" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="942.9" y1="224.8" x2="942.9" y2="236.3" stroke="var(--down)" class="wick"/>
<rect x="941.65" y="224.8" width="2.46" height="11.1" fill="var(--down)"/>
<line x1="946.8" y1="228.5" x2="946.8" y2="250.3" stroke="var(--down)" class="wick"/>
<rect x="945.62" y="233.2" width="2.46" height="16.1" fill="var(--down)"/>
<line x1="950.8" y1="296.0" x2="950.8" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="949.59" y="304.9" width="2.46" height="9.1" fill="var(--down)"/>
<line x1="954.8" y1="296.8" x2="954.8" y2="315.0" stroke="var(--up)" class="wick"/>
<rect x="953.55" y="308.5" width="2.46" height="3.5" fill="var(--up)"/>
<line x1="958.8" y1="280.2" x2="958.8" y2="296.1" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="290.5" width="2.46" height="4.0" fill="var(--up)"/>
<line x1="962.7" y1="265.8" x2="962.7" y2="296.1" stroke="var(--up)" class="wick"/>
<rect x="961.49" y="271.5" width="2.46" height="15.4" fill="var(--up)"/>
<line x1="966.7" y1="248.2" x2="966.7" y2="277.1" stroke="var(--up)" class="wick"/>
<rect x="965.46" y="263.6" width="2.46" height="5.4" fill="var(--up)"/>
<line x1="970.7" y1="264.1" x2="970.7" y2="280.4" stroke="var(--down)" class="wick"/>
<rect x="969.43" y="270.2" width="2.46" height="1.4" fill="var(--down)"/>
<line x1="974.6" y1="205.6" x2="974.6" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="973.39" y="212.1" width="2.46" height="40.6" fill="var(--up)"/>
<line x1="978.6" y1="157.6" x2="978.6" y2="192.9" stroke="var(--up)" class="wick"/>
<rect x="977.36" y="166.0" width="2.46" height="21.4" fill="var(--up)"/>
<line x1="982.6" y1="147.4" x2="982.6" y2="181.9" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="155.0" width="2.46" height="25.0" fill="var(--up)"/>
<line x1="986.5" y1="136.9" x2="986.5" y2="210.4" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="139.9" width="2.46" height="55.4" fill="var(--down)"/>
<line x1="990.5" y1="190.9" x2="990.5" y2="210.1" stroke="var(--down)" class="wick"/>
<rect x="989.27" y="199.8" width="2.46" height="8.0" fill="var(--down)"/>
<line x1="994.5" y1="204.7" x2="994.5" y2="218.3" stroke="var(--down)" class="wick"/>
<rect x="993.23" y="210.5" width="2.46" height="6.4" fill="var(--down)"/>
<line x1="998.4" y1="208.2" x2="998.4" y2="221.1" stroke="var(--up)" class="wick"/>
<rect x="997.20" y="208.4" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="1002.4" y1="210.3" x2="1002.4" y2="245.8" stroke="var(--down)" class="wick"/>
<rect x="1001.17" y="212.7" width="2.46" height="32.1" fill="var(--down)"/>
<line x1="1006.4" y1="237.7" x2="1006.4" y2="252.5" stroke="var(--down)" class="wick"/>
<rect x="1005.14" y="238.1" width="2.46" height="7.3" fill="var(--down)"/>
<line x1="1010.3" y1="233.8" x2="1010.3" y2="244.9" stroke="var(--up)" class="wick"/>
<rect x="1009.11" y="238.0" width="2.46" height="1.6" fill="var(--up)"/>
<line x1="1014.3" y1="227.1" x2="1014.3" y2="242.9" stroke="var(--down)" class="wick"/>
<rect x="1013.07" y="236.8" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="1018.3" y1="235.6" x2="1018.3" y2="249.7" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="238.2" width="2.46" height="6.0" fill="var(--down)"/>
<line x1="1022.2" y1="241.9" x2="1022.2" y2="254.3" stroke="var(--up)" class="wick"/>
<rect x="1021.01" y="243.7" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="1026.2" y1="237.0" x2="1026.2" y2="253.1" stroke="var(--up)" class="wick"/>
<rect x="1024.98" y="242.3" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="1030.2" y1="244.5" x2="1030.2" y2="258.6" stroke="var(--down)" class="wick"/>
<rect x="1028.95" y="246.7" width="2.46" height="6.3" fill="var(--down)"/>
<line x1="1034.1" y1="238.4" x2="1034.1" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="1032.91" y="242.1" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="1038.1" y1="224.1" x2="1038.1" y2="248.2" stroke="var(--up)" class="wick"/>
<rect x="1036.88" y="233.5" width="2.46" height="11.8" fill="var(--up)"/>
<line x1="1042.1" y1="227.9" x2="1042.1" y2="240.0" stroke="var(--down)" class="wick"/>
<rect x="1040.85" y="229.3" width="2.46" height="7.1" fill="var(--down)"/>
<line x1="1046.0" y1="236.6" x2="1046.0" y2="254.4" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="237.3" width="2.46" height="12.2" fill="var(--down)"/>
<line x1="1050.0" y1="250.4" x2="1050.0" y2="258.8" stroke="var(--up)" class="wick"/>
<rect x="1048.79" y="253.1" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="60" y1="242.3" x2="1052" y2="242.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="245.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$345 R1</text>
<text x="1058" y="257.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="162.6" x2="1052" y2="162.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="166.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$375 R2</text>
<text x="1058" y="178.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="332.9" x2="1052" y2="332.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="326.9" font-size="11.5" fill="var(--support)" font-weight="600">$311 S1</text>
<text x="1058" y="338.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="372.9" x2="1052" y2="372.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="366.9" font-size="11.5" fill="var(--support)" font-weight="600">$295 S2</text>
<text x="1058" y="378.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="436.7" x2="1052" y2="436.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="430.7" font-size="11.5" fill="var(--support)" font-weight="600">$271 S3</text>
<text x="1058" y="442.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="253.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="245.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $341 (2026-08-27)</text>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $375 | 3 | 2026년 6~7월 고점대 — 2분기 실적 발표 직전 신고가 구간(2026-06-16·07-07·07-16) |
| R1 | $345 | 2 | 2026년 1~2월 고점대(2026-01-13·02-03) — 7월 급락 이후 회복 과정에서 다시 마주친 구간 |
| **현재가** | **$340.65** (2026-08-27 종가) | — | R1과 S1 사이 |
| S1 | $311 | 3 | 2026년 1~2월 저점대와 7월 실적 직후 저점이 겹치는 구간(2026-01-02·02-05·07-23) |
| S2 | $295 | 3 | 2025년 12월~2026년 3월 조정기 저점대(2025-12-17·2026-02-17·03-09) |
| S3 | $271 | 2 | 2025년 11월·2026년 3월 저점(2025-11-14·2026-03-30) — 현재가와 20% 이상 떨어져 있어 근시일 지지로 보기 어렵다 |
| 참고선 | $408.61 | — | 최근 1년 최고가. 2026년 7~8월 한 차례만 닿은 값이라 클러스터를 이루지 못했다 — 근시일 저항으로 보지 않고 상단 기준선으로만 둔다 |
| 참고선 | $206.20 | — | 최근 1년 최저가(2025년 8월 말). 이후 반독점 구제안 발표로 가격대가 통째로 재설정돼 현재 지지로 기능하지 않는다 |

> 유효 클러스터가 저항 2개·지지 3개로 잡혀 R3는 두지 않았다 — 현재가 위쪽에서 터치 2회 이상을 만족하는 스윙대가 $345·$375 둘뿐이기 때문이다. `--force-level`은 쓰지 않았다.

---

## 3. 관측된 특이 구간 — 2026-07-23 2분기 실적 발표 후 갭다운

- 2026-07-22 장 마감 후 발표된 2026년 2분기 실적에서 매출·클라우드 성장은 시장 예상을 웃돌았으나, 2026년 CapEx 가이던스가 $180~190B에서 **$195~205B으로 상향**되고 분기 잉여현금흐름이 −$5.9B을 기록한 것이 하락의 계기였다([최근 뉴스 / 이슈](./08_news.md) 2026-07-22 항목).
- 종가 기준 전일 대비 **−7.1%** ($342.09 → $317.69), 거래량은 평소(일 3,324만 주 내외) 대비 약 **2.1배**인 **6,942만 주**.
- 이 하락으로 7월 초 형성된 $355~375대 매물대가 저항으로 굳었고, 저점 $317대는 이후 S1($311) 클러스터에 흡수됐다. 이후 5주간 주가는 $317~356 범위에서 등락하다 8월 말 $340대로 복귀했다 — 즉 갭은 메워지지 않았고 **거래 범위 자체가 한 단계 낮아진 상태**다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py GOOGL --name Alphabet --emit all` (기본 옵션 — `--close-on`·`--force-level`·`--event`·`--ref-line` 미사용, 수집일 2026-08-30)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간의 −7.1% 갭 때문에 $317~342 구간에는 실제 체결이 거의 없다 — S1($311)과 R1($345) 사이의 "빈 구간"이므로, 이 사이 가격대를 지지·저항으로 읽지 말 것.
    - 이 기간(2025-08-29~2026-08-27)에는 주식분할이 없다. 2022년 7월 20:1 분할은 이 창 밖이며, 원자료는 과거 분할을 소급 반영한 값이다. 배당은 4회 있었으나 원주가라 반영되지 않았다 — 배당수익률이 0.25% 수준이라 레벨 해석에 실질적 영향은 없다.

---

*작성일: 2026-08-30*
