# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **일봉 시계열은 2026-08-27($102.63)에서 끝나고, [밸류에이션 / 적정주가](./06_valuation.md)·[핵심 지표](./04_metrics.md)가 쓰는 기준 종가는 한 거래일 뒤인 2026-08-28의 $103.09다.** 어긋난 것이 아니라 일봉 수정주가 반영이 하루 늦은 것으로, 두 값의 차이는 0.45%다. 아래 §2 표의 "현재가" 행은 차트와 같은 2026-08-27 종가를 쓰고, 다른 문서는 2026-08-28 종가를 쓴다. $103.09는 [주봉 차트](./10_technical_weekly.md)와 stockanalysis에서 각각 확인했다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

<div class="wmt-chart">
<style>
.wmt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .wmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .wmt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.wmt-chart svg { width:100%; height:auto; display:block; }
.wmt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.wmt-chart .title { fill: var(--ink); font-weight:600; }
.wmt-chart .grid { stroke: var(--grid); stroke-width:1; }
.wmt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Walmart(WMT) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Walmart (WMT) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $102.63 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="551.4" x2="1052" y2="551.4" class="grid"/>
<text x="52" y="555.4" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="415.6" x2="1052" y2="415.6" class="grid"/>
<text x="52" y="419.6" font-size="11" text-anchor="end" fill="var(--muted)">110</text>
<line x1="60" y1="279.9" x2="1052" y2="279.9" class="grid"/>
<text x="52" y="283.9" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="144.2" x2="1052" y2="144.2" class="grid"/>
<text x="52" y="148.2" font-size="11" text-anchor="end" fill="var(--muted)">130</text>
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
<line x1="62.0" y1="591.7" x2="62.0" y2="608.4" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="592.3" width="2.46" height="11.9" fill="var(--up)"/>
<line x1="66.0" y1="580.5" x2="66.0" y2="598.7" stroke="var(--up)" class="wick"/>
<rect x="64.72" y="580.5" width="2.46" height="8.4" fill="var(--up)"/>
<line x1="69.9" y1="559.0" x2="69.9" y2="585.3" stroke="var(--up)" class="wick"/>
<rect x="68.69" y="559.0" width="2.46" height="21.6" fill="var(--up)"/>
<line x1="73.9" y1="533.0" x2="73.9" y2="556.1" stroke="var(--up)" class="wick"/>
<rect x="72.66" y="538.7" width="2.46" height="13.8" fill="var(--up)"/>
<line x1="77.9" y1="531.3" x2="77.9" y2="557.5" stroke="var(--down)" class="wick"/>
<rect x="76.63" y="536.7" width="2.46" height="7.7" fill="var(--down)"/>
<line x1="81.8" y1="519.3" x2="81.8" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="80.59" y="520.4" width="2.46" height="19.4" fill="var(--up)"/>
<line x1="85.8" y1="517.6" x2="85.8" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="520.3" width="2.46" height="3.9" fill="var(--up)"/>
<line x1="89.8" y1="518.1" x2="89.8" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="88.53" y="524.9" width="2.46" height="20.9" fill="var(--down)"/>
<line x1="93.7" y1="513.6" x2="93.7" y2="547.6" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="515.4" width="2.46" height="22.5" fill="var(--up)"/>
<line x1="97.7" y1="497.3" x2="97.7" y2="519.3" stroke="var(--up)" class="wick"/>
<rect x="96.47" y="504.0" width="2.46" height="12.9" fill="var(--up)"/>
<line x1="101.7" y1="497.3" x2="101.7" y2="505.1" stroke="var(--up)" class="wick"/>
<rect x="100.43" y="501.3" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="105.6" y1="494.2" x2="105.6" y2="508.9" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="499.1" width="2.46" height="5.8" fill="var(--down)"/>
<line x1="109.6" y1="468.4" x2="109.6" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="493.4" width="2.46" height="7.3" fill="var(--up)"/>
<line x1="113.6" y1="488.4" x2="113.6" y2="522.6" stroke="var(--down)" class="wick"/>
<rect x="112.34" y="500.1" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="117.5" y1="497.9" x2="117.5" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="116.31" y="499.7" width="2.46" height="20.1" fill="var(--down)"/>
<line x1="121.5" y1="507.9" x2="121.5" y2="525.3" stroke="var(--up)" class="wick"/>
<rect x="120.27" y="513.1" width="2.46" height="5.0" fill="var(--up)"/>
<line x1="125.5" y1="515.0" x2="125.5" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="124.24" y="517.2" width="2.46" height="1.5" fill="var(--up)"/>
<line x1="129.4" y1="504.3" x2="129.4" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="128.21" y="510.1" width="2.46" height="4.2" fill="var(--down)"/>
<line x1="133.4" y1="503.7" x2="133.4" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="132.18" y="507.7" width="2.46" height="2.3" fill="var(--down)"/>
<line x1="137.4" y1="504.0" x2="137.4" y2="517.8" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="508.5" width="2.46" height="3.8" fill="var(--up)"/>
<line x1="141.3" y1="506.4" x2="141.3" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="140.11" y="509.6" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="145.3" y1="497.9" x2="145.3" y2="514.4" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="509.8" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="149.3" y1="512.5" x2="149.3" y2="543.9" stroke="var(--down)" class="wick"/>
<rect x="148.05" y="516.6" width="2.46" height="8.1" fill="var(--down)"/>
<line x1="153.2" y1="522.3" x2="153.2" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="152.02" y="528.3" width="2.46" height="3.4" fill="var(--up)"/>
<line x1="157.2" y1="513.1" x2="157.2" y2="535.1" stroke="var(--up)" class="wick"/>
<rect x="155.99" y="523.3" width="2.46" height="8.3" fill="var(--up)"/>
<line x1="161.2" y1="509.7" x2="161.2" y2="529.9" stroke="var(--up)" class="wick"/>
<rect x="159.95" y="514.7" width="2.46" height="11.1" fill="var(--up)"/>
<line x1="165.2" y1="507.2" x2="165.2" y2="538.5" stroke="var(--up)" class="wick"/>
<rect x="163.92" y="507.4" width="2.46" height="11.7" fill="var(--up)"/>
<line x1="169.1" y1="507.1" x2="169.1" y2="522.2" stroke="var(--down)" class="wick"/>
<rect x="167.89" y="510.4" width="2.46" height="1.6" fill="var(--down)"/>
<line x1="173.1" y1="504.5" x2="173.1" y2="546.3" stroke="var(--down)" class="wick"/>
<rect x="171.86" y="508.9" width="2.46" height="18.5" fill="var(--down)"/>
<line x1="177.1" y1="502.1" x2="177.1" y2="530.7" stroke="var(--down)" class="wick"/>
<rect x="175.83" y="523.5" width="2.46" height="2.9" fill="var(--down)"/>
<line x1="181.0" y1="518.1" x2="181.0" y2="536.8" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="522.6" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="185.0" y1="443.9" x2="185.0" y2="512.1" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="453.5" width="2.46" height="42.9" fill="var(--up)"/>
<line x1="189.0" y1="421.6" x2="189.0" y2="452.3" stroke="var(--up)" class="wick"/>
<rect x="187.73" y="428.8" width="2.46" height="23.2" fill="var(--up)"/>
<line x1="192.9" y1="421.3" x2="192.9" y2="474.5" stroke="var(--down)" class="wick"/>
<rect x="191.70" y="426.5" width="2.46" height="37.0" fill="var(--down)"/>
<line x1="196.9" y1="440.1" x2="196.9" y2="466.9" stroke="var(--up)" class="wick"/>
<rect x="195.67" y="446.4" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="200.9" y1="439.4" x2="200.9" y2="461.6" stroke="var(--down)" class="wick"/>
<rect x="199.63" y="444.8" width="2.46" height="10.9" fill="var(--down)"/>
<line x1="204.8" y1="449.8" x2="204.8" y2="467.5" stroke="var(--down)" class="wick"/>
<rect x="203.60" y="451.9" width="2.46" height="15.1" fill="var(--down)"/>
<line x1="208.8" y1="445.9" x2="208.8" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="207.57" y="454.5" width="2.46" height="8.0" fill="var(--up)"/>
<line x1="212.8" y1="448.6" x2="212.8" y2="472.9" stroke="var(--down)" class="wick"/>
<rect x="211.54" y="451.6" width="2.46" height="6.6" fill="var(--down)"/>
<line x1="216.7" y1="454.1" x2="216.7" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="455.4" width="2.46" height="12.2" fill="var(--down)"/>
<line x1="220.7" y1="465.0" x2="220.7" y2="495.0" stroke="var(--down)" class="wick"/>
<rect x="219.47" y="465.3" width="2.46" height="25.4" fill="var(--down)"/>
<line x1="224.7" y1="495.2" x2="224.7" y2="510.0" stroke="var(--down)" class="wick"/>
<rect x="223.44" y="496.3" width="2.46" height="12.1" fill="var(--down)"/>
<line x1="228.6" y1="501.6" x2="228.6" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="227.41" y="511.9" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="232.6" y1="505.6" x2="232.6" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="231.38" y="521.1" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="236.6" y1="522.9" x2="236.6" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="235.35" y="528.3" width="2.46" height="7.1" fill="var(--down)"/>
<line x1="240.5" y1="526.9" x2="240.5" y2="545.9" stroke="var(--up)" class="wick"/>
<rect x="239.31" y="529.8" width="2.46" height="10.4" fill="var(--up)"/>
<line x1="244.5" y1="515.8" x2="244.5" y2="531.5" stroke="var(--up)" class="wick"/>
<rect x="243.28" y="520.6" width="2.46" height="1.9" fill="var(--up)"/>
<line x1="248.5" y1="515.0" x2="248.5" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="247.25" y="527.7" width="2.46" height="3.7" fill="var(--down)"/>
<line x1="252.4" y1="525.2" x2="252.4" y2="551.0" stroke="var(--up)" class="wick"/>
<rect x="251.22" y="528.6" width="2.46" height="4.6" fill="var(--up)"/>
<line x1="256.4" y1="511.0" x2="256.4" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="516.2" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="260.4" y1="515.1" x2="260.4" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="259.15" y="518.5" width="2.46" height="3.7" fill="var(--up)"/>
<line x1="264.4" y1="500.6" x2="264.4" y2="519.9" stroke="var(--up)" class="wick"/>
<rect x="263.12" y="504.7" width="2.46" height="12.8" fill="var(--up)"/>
<line x1="268.3" y1="502.5" x2="268.3" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="267.09" y="504.7" width="2.46" height="1.2" fill="var(--up)"/>
<line x1="272.3" y1="498.0" x2="272.3" y2="523.9" stroke="var(--down)" class="wick"/>
<rect x="271.06" y="502.6" width="2.46" height="14.2" fill="var(--down)"/>
<line x1="276.3" y1="517.6" x2="276.3" y2="566.6" stroke="var(--up)" class="wick"/>
<rect x="275.03" y="517.7" width="2.46" height="30.9" fill="var(--up)"/>
<line x1="280.2" y1="506.3" x2="280.2" y2="522.9" stroke="var(--up)" class="wick"/>
<rect x="278.99" y="511.3" width="2.46" height="5.0" fill="var(--up)"/>
<line x1="284.2" y1="506.0" x2="284.2" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="282.96" y="510.9" width="2.46" height="21.6" fill="var(--down)"/>
<line x1="288.2" y1="528.2" x2="288.2" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="286.93" y="529.9" width="2.46" height="13.2" fill="var(--down)"/>
<line x1="292.1" y1="444.0" x2="292.1" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="290.90" y="454.9" width="2.46" height="43.0" fill="var(--up)"/>
<line x1="296.1" y1="440.7" x2="296.1" y2="487.3" stroke="var(--down)" class="wick"/>
<rect x="294.87" y="443.1" width="2.46" height="36.1" fill="var(--down)"/>
<line x1="300.1" y1="466.3" x2="300.1" y2="500.3" stroke="var(--down)" class="wick"/>
<rect x="298.83" y="478.6" width="2.46" height="17.6" fill="var(--down)"/>
<line x1="304.0" y1="450.7" x2="304.0" y2="493.9" stroke="var(--up)" class="wick"/>
<rect x="302.80" y="456.4" width="2.46" height="32.4" fill="var(--up)"/>
<line x1="308.0" y1="421.2" x2="308.0" y2="454.1" stroke="var(--up)" class="wick"/>
<rect x="306.77" y="427.9" width="2.46" height="25.8" fill="var(--up)"/>
<line x1="312.0" y1="406.1" x2="312.0" y2="429.2" stroke="var(--up)" class="wick"/>
<rect x="310.74" y="408.7" width="2.46" height="16.4" fill="var(--up)"/>
<line x1="315.9" y1="391.8" x2="315.9" y2="410.8" stroke="var(--up)" class="wick"/>
<rect x="314.71" y="394.9" width="2.46" height="13.8" fill="var(--up)"/>
<line x1="319.9" y1="379.7" x2="319.9" y2="404.9" stroke="var(--up)" class="wick"/>
<rect x="318.67" y="382.9" width="2.46" height="12.8" fill="var(--up)"/>
<line x1="323.9" y1="349.3" x2="323.9" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="355.8" width="2.46" height="25.9" fill="var(--up)"/>
<line x1="327.8" y1="349.3" x2="327.8" y2="372.8" stroke="var(--up)" class="wick"/>
<rect x="326.61" y="350.0" width="2.46" height="16.6" fill="var(--up)"/>
<line x1="331.8" y1="330.6" x2="331.8" y2="352.1" stroke="var(--up)" class="wick"/>
<rect x="330.58" y="346.3" width="2.46" height="5.2" fill="var(--up)"/>
<line x1="335.8" y1="347.9" x2="335.8" y2="384.4" stroke="var(--down)" class="wick"/>
<rect x="334.55" y="353.6" width="2.46" height="13.7" fill="var(--down)"/>
<line x1="339.7" y1="338.0" x2="339.7" y2="374.7" stroke="var(--up)" class="wick"/>
<rect x="338.51" y="347.0" width="2.46" height="15.1" fill="var(--up)"/>
<line x1="343.7" y1="331.1" x2="343.7" y2="375.1" stroke="var(--down)" class="wick"/>
<rect x="342.48" y="343.0" width="2.46" height="29.4" fill="var(--down)"/>
<line x1="347.7" y1="336.0" x2="347.7" y2="377.0" stroke="var(--up)" class="wick"/>
<rect x="346.45" y="340.7" width="2.46" height="32.3" fill="var(--up)"/>
<line x1="351.6" y1="321.3" x2="351.6" y2="347.5" stroke="var(--up)" class="wick"/>
<rect x="350.42" y="324.7" width="2.46" height="19.5" fill="var(--up)"/>
<line x1="355.6" y1="314.5" x2="355.6" y2="339.1" stroke="var(--down)" class="wick"/>
<rect x="354.39" y="321.6" width="2.46" height="1.9" fill="var(--down)"/>
<line x1="359.6" y1="322.3" x2="359.6" y2="348.5" stroke="var(--down)" class="wick"/>
<rect x="358.35" y="326.3" width="2.46" height="15.7" fill="var(--down)"/>
<line x1="363.6" y1="328.9" x2="363.6" y2="346.8" stroke="var(--up)" class="wick"/>
<rect x="362.32" y="338.8" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="367.5" y1="327.7" x2="367.5" y2="353.1" stroke="var(--down)" class="wick"/>
<rect x="366.29" y="347.6" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="371.5" y1="344.0" x2="371.5" y2="367.7" stroke="var(--down)" class="wick"/>
<rect x="370.26" y="345.9" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="375.5" y1="357.0" x2="375.5" y2="385.5" stroke="var(--down)" class="wick"/>
<rect x="374.23" y="361.2" width="2.46" height="19.1" fill="var(--down)"/>
<line x1="379.4" y1="383.8" x2="379.4" y2="406.1" stroke="var(--down)" class="wick"/>
<rect x="378.19" y="388.6" width="2.46" height="14.8" fill="var(--down)"/>
<line x1="383.4" y1="392.4" x2="383.4" y2="408.2" stroke="var(--up)" class="wick"/>
<rect x="382.16" y="393.8" width="2.46" height="9.6" fill="var(--up)"/>
<line x1="387.4" y1="388.9" x2="387.4" y2="397.2" stroke="var(--up)" class="wick"/>
<rect x="386.13" y="392.0" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="391.3" y1="377.9" x2="391.3" y2="394.3" stroke="var(--up)" class="wick"/>
<rect x="390.10" y="381.3" width="2.46" height="12.8" fill="var(--up)"/>
<line x1="395.3" y1="379.1" x2="395.3" y2="390.7" stroke="var(--up)" class="wick"/>
<rect x="394.07" y="389.6" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="399.3" y1="385.1" x2="399.3" y2="397.7" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="392.2" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="403.2" y1="377.8" x2="403.2" y2="400.4" stroke="var(--up)" class="wick"/>
<rect x="402.00" y="378.2" width="2.46" height="18.1" fill="var(--up)"/>
<line x1="407.2" y1="365.0" x2="407.2" y2="386.5" stroke="var(--down)" class="wick"/>
<rect x="405.97" y="377.4" width="2.46" height="1.5" fill="var(--down)"/>
<line x1="411.2" y1="350.6" x2="411.2" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="409.94" y="356.7" width="2.46" height="26.3" fill="var(--up)"/>
<line x1="415.1" y1="351.4" x2="415.1" y2="387.1" stroke="var(--down)" class="wick"/>
<rect x="413.91" y="358.8" width="2.46" height="20.0" fill="var(--down)"/>
<line x1="419.1" y1="368.5" x2="419.1" y2="418.2" stroke="var(--up)" class="wick"/>
<rect x="417.87" y="374.0" width="2.46" height="24.2" fill="var(--up)"/>
<line x1="423.1" y1="341.5" x2="423.1" y2="385.0" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="354.2" width="2.46" height="30.8" fill="var(--up)"/>
<line x1="427.0" y1="295.7" x2="427.0" y2="328.6" stroke="var(--up)" class="wick"/>
<rect x="425.81" y="307.5" width="2.46" height="6.4" fill="var(--up)"/>
<line x1="431.0" y1="273.0" x2="431.0" y2="310.7" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="275.0" width="2.46" height="33.5" fill="var(--up)"/>
<line x1="435.0" y1="263.1" x2="435.0" y2="293.1" stroke="var(--down)" class="wick"/>
<rect x="433.75" y="277.3" width="2.46" height="2.0" fill="var(--down)"/>
<line x1="438.9" y1="268.1" x2="438.9" y2="297.2" stroke="var(--down)" class="wick"/>
<rect x="437.71" y="280.2" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="442.9" y1="271.8" x2="442.9" y2="322.0" stroke="var(--up)" class="wick"/>
<rect x="441.68" y="284.0" width="2.46" height="14.0" fill="var(--up)"/>
<line x1="446.9" y1="257.9" x2="446.9" y2="312.4" stroke="var(--down)" class="wick"/>
<rect x="445.65" y="267.9" width="2.46" height="29.6" fill="var(--down)"/>
<line x1="450.8" y1="273.3" x2="450.8" y2="313.2" stroke="var(--up)" class="wick"/>
<rect x="449.62" y="288.6" width="2.46" height="17.4" fill="var(--up)"/>
<line x1="454.8" y1="286.4" x2="454.8" y2="311.8" stroke="var(--down)" class="wick"/>
<rect x="453.59" y="289.6" width="2.46" height="19.8" fill="var(--down)"/>
<line x1="458.8" y1="298.8" x2="458.8" y2="318.7" stroke="var(--down)" class="wick"/>
<rect x="457.55" y="304.8" width="2.46" height="6.0" fill="var(--down)"/>
<line x1="462.8" y1="295.5" x2="462.8" y2="315.4" stroke="var(--down)" class="wick"/>
<rect x="461.52" y="309.7" width="2.46" height="2.3" fill="var(--down)"/>
<line x1="466.7" y1="312.1" x2="466.7" y2="341.3" stroke="var(--down)" class="wick"/>
<rect x="465.49" y="313.9" width="2.46" height="7.6" fill="var(--down)"/>
<line x1="470.7" y1="314.4" x2="470.7" y2="336.0" stroke="var(--down)" class="wick"/>
<rect x="469.46" y="325.5" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="474.7" y1="311.7" x2="474.7" y2="333.3" stroke="var(--up)" class="wick"/>
<rect x="473.43" y="315.1" width="2.46" height="13.0" fill="var(--up)"/>
<line x1="478.6" y1="287.9" x2="478.6" y2="326.1" stroke="var(--up)" class="wick"/>
<rect x="477.39" y="291.6" width="2.46" height="30.3" fill="var(--up)"/>
<line x1="482.6" y1="222.9" x2="482.6" y2="292.8" stroke="var(--up)" class="wick"/>
<rect x="481.36" y="224.8" width="2.46" height="61.9" fill="var(--up)"/>
<line x1="486.6" y1="169.1" x2="486.6" y2="230.4" stroke="var(--up)" class="wick"/>
<rect x="485.33" y="175.3" width="2.46" height="55.1" fill="var(--up)"/>
<line x1="490.5" y1="152.2" x2="490.5" y2="183.7" stroke="var(--down)" class="wick"/>
<rect x="489.30" y="169.6" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="494.5" y1="149.6" x2="494.5" y2="190.9" stroke="var(--down)" class="wick"/>
<rect x="493.27" y="163.5" width="2.46" height="22.3" fill="var(--down)"/>
<line x1="498.5" y1="121.1" x2="498.5" y2="184.2" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="128.2" width="2.46" height="52.8" fill="var(--up)"/>
<line x1="502.4" y1="119.9" x2="502.4" y2="170.1" stroke="var(--down)" class="wick"/>
<rect x="501.20" y="124.9" width="2.46" height="32.6" fill="var(--down)"/>
<line x1="506.4" y1="153.2" x2="506.4" y2="193.2" stroke="var(--down)" class="wick"/>
<rect x="505.17" y="158.6" width="2.46" height="30.4" fill="var(--down)"/>
<line x1="510.4" y1="147.7" x2="510.4" y2="190.0" stroke="var(--up)" class="wick"/>
<rect x="509.14" y="160.9" width="2.46" height="28.1" fill="var(--up)"/>
<line x1="514.3" y1="83.3" x2="514.3" y2="153.6" stroke="var(--up)" class="wick"/>
<rect x="513.11" y="94.8" width="2.46" height="57.8" fill="var(--up)"/>
<line x1="518.3" y1="81.1" x2="518.3" y2="120.5" stroke="var(--up)" class="wick"/>
<rect x="517.07" y="91.4" width="2.46" height="16.2" fill="var(--up)"/>
<line x1="522.3" y1="80.6" x2="522.3" y2="169.2" stroke="var(--down)" class="wick"/>
<rect x="521.04" y="102.0" width="2.46" height="57.8" fill="var(--down)"/>
<line x1="526.2" y1="159.6" x2="526.2" y2="201.6" stroke="var(--down)" class="wick"/>
<rect x="525.01" y="169.6" width="2.46" height="20.5" fill="var(--down)"/>
<line x1="530.2" y1="142.9" x2="530.2" y2="220.2" stroke="var(--down)" class="wick"/>
<rect x="528.98" y="164.6" width="2.46" height="49.3" fill="var(--down)"/>
<line x1="534.2" y1="232.7" x2="534.2" y2="265.7" stroke="var(--down)" class="wick"/>
<rect x="532.95" y="239.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="538.1" y1="187.6" x2="538.1" y2="239.8" stroke="var(--up)" class="wick"/>
<rect x="536.91" y="201.1" width="2.46" height="31.1" fill="var(--up)"/>
<line x1="542.1" y1="170.8" x2="542.1" y2="213.3" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="188.3" width="2.46" height="11.5" fill="var(--up)"/>
<line x1="546.1" y1="179.5" x2="546.1" y2="206.4" stroke="var(--down)" class="wick"/>
<rect x="544.85" y="190.2" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="550.0" y1="180.4" x2="550.0" y2="226.5" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="198.8" width="2.46" height="21.2" fill="var(--down)"/>
<line x1="554.0" y1="163.2" x2="554.0" y2="210.0" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="172.0" width="2.46" height="33.0" fill="var(--up)"/>
<line x1="558.0" y1="161.2" x2="558.0" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="178.7" width="2.46" height="4.9" fill="var(--down)"/>
<line x1="562.0" y1="166.3" x2="562.0" y2="203.0" stroke="var(--up)" class="wick"/>
<rect x="560.72" y="172.6" width="2.46" height="18.9" fill="var(--up)"/>
<line x1="565.9" y1="169.1" x2="565.9" y2="195.2" stroke="var(--up)" class="wick"/>
<rect x="564.69" y="173.9" width="2.46" height="9.5" fill="var(--up)"/>
<line x1="569.9" y1="202.8" x2="569.9" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="206.9" width="2.46" height="28.1" fill="var(--down)"/>
<line x1="573.9" y1="223.1" x2="573.9" y2="257.9" stroke="var(--up)" class="wick"/>
<rect x="572.63" y="228.4" width="2.46" height="17.6" fill="var(--up)"/>
<line x1="577.8" y1="218.7" x2="577.8" y2="246.0" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="221.0" width="2.46" height="8.8" fill="var(--up)"/>
<line x1="581.8" y1="197.1" x2="581.8" y2="234.5" stroke="var(--up)" class="wick"/>
<rect x="580.56" y="210.4" width="2.46" height="12.4" fill="var(--up)"/>
<line x1="585.8" y1="205.4" x2="585.8" y2="238.5" stroke="var(--down)" class="wick"/>
<rect x="584.53" y="207.9" width="2.46" height="24.7" fill="var(--down)"/>
<line x1="589.7" y1="206.8" x2="589.7" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="588.50" y="207.6" width="2.46" height="41.1" fill="var(--up)"/>
<line x1="593.7" y1="189.1" x2="593.7" y2="212.5" stroke="var(--up)" class="wick"/>
<rect x="592.47" y="191.4" width="2.46" height="15.3" fill="var(--up)"/>
<line x1="597.7" y1="185.2" x2="597.7" y2="214.4" stroke="var(--down)" class="wick"/>
<rect x="596.43" y="188.2" width="2.46" height="10.5" fill="var(--down)"/>
<line x1="601.6" y1="182.3" x2="601.6" y2="214.0" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="189.7" width="2.46" height="21.3" fill="var(--down)"/>
<line x1="605.6" y1="217.4" x2="605.6" y2="255.1" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="221.2" width="2.46" height="31.9" fill="var(--down)"/>
<line x1="609.6" y1="242.6" x2="609.6" y2="289.8" stroke="var(--down)" class="wick"/>
<rect x="608.34" y="247.4" width="2.46" height="17.8" fill="var(--down)"/>
<line x1="613.5" y1="262.3" x2="613.5" y2="306.8" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="271.4" width="2.46" height="21.9" fill="var(--down)"/>
<line x1="617.5" y1="264.6" x2="617.5" y2="292.8" stroke="var(--up)" class="wick"/>
<rect x="616.27" y="270.2" width="2.46" height="3.3" fill="var(--up)"/>
<line x1="621.5" y1="224.1" x2="621.5" y2="273.3" stroke="var(--up)" class="wick"/>
<rect x="620.24" y="252.1" width="2.46" height="19.3" fill="var(--up)"/>
<line x1="625.4" y1="232.6" x2="625.4" y2="255.8" stroke="var(--up)" class="wick"/>
<rect x="624.21" y="238.4" width="2.46" height="3.4" fill="var(--up)"/>
<line x1="629.4" y1="228.4" x2="629.4" y2="255.6" stroke="var(--down)" class="wick"/>
<rect x="628.18" y="230.9" width="2.46" height="19.4" fill="var(--down)"/>
<line x1="633.4" y1="222.0" x2="633.4" y2="255.2" stroke="var(--up)" class="wick"/>
<rect x="632.15" y="240.7" width="2.46" height="11.7" fill="var(--up)"/>
<line x1="637.3" y1="208.5" x2="637.3" y2="237.3" stroke="var(--down)" class="wick"/>
<rect x="636.11" y="229.6" width="2.46" height="2.8" fill="var(--down)"/>
<line x1="641.3" y1="212.1" x2="641.3" y2="241.4" stroke="var(--up)" class="wick"/>
<rect x="640.08" y="221.8" width="2.46" height="11.5" fill="var(--up)"/>
<line x1="645.3" y1="208.9" x2="645.3" y2="237.5" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="215.6" width="2.46" height="12.8" fill="var(--up)"/>
<line x1="649.2" y1="199.9" x2="649.2" y2="223.6" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="201.3" width="2.46" height="8.7" fill="var(--up)"/>
<line x1="653.2" y1="185.2" x2="653.2" y2="207.0" stroke="var(--up)" class="wick"/>
<rect x="651.99" y="187.8" width="2.46" height="13.3" fill="var(--up)"/>
<line x1="657.2" y1="193.6" x2="657.2" y2="255.6" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="195.9" width="2.46" height="50.2" fill="var(--down)"/>
<line x1="661.2" y1="180.9" x2="661.2" y2="261.9" stroke="var(--up)" class="wick"/>
<rect x="659.92" y="181.4" width="2.46" height="67.6" fill="var(--up)"/>
<line x1="665.1" y1="148.4" x2="665.1" y2="187.4" stroke="var(--up)" class="wick"/>
<rect x="663.89" y="156.0" width="2.46" height="27.7" fill="var(--up)"/>
<line x1="669.1" y1="158.7" x2="669.1" y2="195.5" stroke="var(--down)" class="wick"/>
<rect x="667.86" y="161.6" width="2.46" height="26.5" fill="var(--down)"/>
<line x1="673.1" y1="194.4" x2="673.1" y2="226.3" stroke="var(--down)" class="wick"/>
<rect x="671.83" y="194.6" width="2.46" height="23.3" fill="var(--down)"/>
<line x1="677.0" y1="209.4" x2="677.0" y2="245.3" stroke="var(--up)" class="wick"/>
<rect x="675.79" y="211.4" width="2.46" height="25.8" fill="var(--up)"/>
<line x1="681.0" y1="211.1" x2="681.0" y2="236.8" stroke="var(--up)" class="wick"/>
<rect x="679.76" y="215.3" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="685.0" y1="199.3" x2="685.0" y2="226.0" stroke="var(--up)" class="wick"/>
<rect x="683.73" y="214.5" width="2.46" height="6.6" fill="var(--up)"/>
<line x1="688.9" y1="177.2" x2="688.9" y2="234.2" stroke="var(--up)" class="wick"/>
<rect x="687.70" y="178.1" width="2.46" height="39.8" fill="var(--up)"/>
<line x1="692.9" y1="151.4" x2="692.9" y2="180.6" stroke="var(--up)" class="wick"/>
<rect x="691.67" y="172.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="696.9" y1="147.3" x2="696.9" y2="178.4" stroke="var(--up)" class="wick"/>
<rect x="695.63" y="149.6" width="2.46" height="24.0" fill="var(--up)"/>
<line x1="700.8" y1="138.1" x2="700.8" y2="160.0" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="144.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="704.8" y1="110.8" x2="704.8" y2="137.6" stroke="var(--up)" class="wick"/>
<rect x="703.57" y="116.7" width="2.46" height="19.8" fill="var(--up)"/>
<line x1="708.8" y1="115.4" x2="708.8" y2="154.0" stroke="var(--down)" class="wick"/>
<rect x="707.54" y="117.9" width="2.46" height="27.4" fill="var(--down)"/>
<line x1="712.7" y1="146.8" x2="712.7" y2="179.5" stroke="var(--down)" class="wick"/>
<rect x="711.51" y="149.4" width="2.46" height="27.5" fill="var(--down)"/>
<line x1="716.7" y1="147.3" x2="716.7" y2="187.9" stroke="var(--down)" class="wick"/>
<rect x="715.47" y="153.2" width="2.46" height="23.8" fill="var(--down)"/>
<line x1="720.7" y1="170.3" x2="720.7" y2="199.7" stroke="var(--up)" class="wick"/>
<rect x="719.44" y="171.2" width="2.46" height="18.0" fill="var(--up)"/>
<line x1="724.6" y1="111.2" x2="724.6" y2="172.0" stroke="var(--up)" class="wick"/>
<rect x="723.41" y="118.0" width="2.46" height="53.1" fill="var(--up)"/>
<line x1="728.6" y1="98.5" x2="728.6" y2="130.9" stroke="var(--down)" class="wick"/>
<rect x="727.38" y="118.2" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="732.6" y1="120.5" x2="732.6" y2="148.6" stroke="var(--down)" class="wick"/>
<rect x="731.35" y="138.6" width="2.46" height="1.1" fill="var(--down)"/>
<line x1="736.5" y1="120.7" x2="736.5" y2="140.1" stroke="var(--up)" class="wick"/>
<rect x="735.31" y="133.5" width="2.46" height="3.8" fill="var(--up)"/>
<line x1="740.5" y1="128.6" x2="740.5" y2="150.6" stroke="var(--down)" class="wick"/>
<rect x="739.28" y="132.5" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="744.5" y1="136.1" x2="744.5" y2="162.3" stroke="var(--up)" class="wick"/>
<rect x="743.25" y="141.5" width="2.46" height="4.1" fill="var(--up)"/>
<line x1="748.4" y1="125.1" x2="748.4" y2="140.8" stroke="var(--up)" class="wick"/>
<rect x="747.22" y="138.4" width="2.46" height="1.5" fill="var(--up)"/>
<line x1="752.4" y1="136.1" x2="752.4" y2="193.3" stroke="var(--down)" class="wick"/>
<rect x="751.19" y="141.8" width="2.46" height="35.1" fill="var(--down)"/>
<line x1="756.4" y1="129.0" x2="756.4" y2="175.2" stroke="var(--up)" class="wick"/>
<rect x="755.15" y="139.5" width="2.46" height="30.8" fill="var(--up)"/>
<line x1="760.4" y1="109.9" x2="760.4" y2="160.9" stroke="var(--up)" class="wick"/>
<rect x="759.12" y="124.3" width="2.46" height="30.9" fill="var(--up)"/>
<line x1="764.3" y1="106.5" x2="764.3" y2="132.5" stroke="var(--up)" class="wick"/>
<rect x="763.09" y="110.8" width="2.46" height="14.9" fill="var(--up)"/>
<line x1="768.3" y1="90.6" x2="768.3" y2="133.5" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="94.1" width="2.46" height="30.4" fill="var(--down)"/>
<line x1="772.3" y1="97.1" x2="772.3" y2="128.9" stroke="var(--up)" class="wick"/>
<rect x="771.03" y="98.9" width="2.46" height="24.7" fill="var(--up)"/>
<line x1="776.2" y1="74.2" x2="776.2" y2="116.3" stroke="var(--up)" class="wick"/>
<rect x="774.99" y="87.2" width="2.46" height="17.1" fill="var(--up)"/>
<line x1="780.2" y1="94.7" x2="780.2" y2="139.7" stroke="var(--down)" class="wick"/>
<rect x="778.96" y="104.7" width="2.46" height="28.0" fill="var(--down)"/>
<line x1="784.2" y1="201.2" x2="784.2" y2="274.6" stroke="var(--down)" class="wick"/>
<rect x="782.93" y="220.1" width="2.46" height="41.7" fill="var(--down)"/>
<line x1="788.1" y1="253.5" x2="788.1" y2="294.7" stroke="var(--down)" class="wick"/>
<rect x="786.90" y="261.7" width="2.46" height="14.5" fill="var(--down)"/>
<line x1="792.1" y1="265.7" x2="792.1" y2="308.2" stroke="var(--down)" class="wick"/>
<rect x="790.87" y="270.6" width="2.46" height="28.8" fill="var(--down)"/>
<line x1="796.1" y1="287.7" x2="796.1" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="794.83" y="299.7" width="2.46" height="2.8" fill="var(--up)"/>
<line x1="800.0" y1="291.2" x2="800.0" y2="316.2" stroke="var(--down)" class="wick"/>
<rect x="798.80" y="294.0" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="804.0" y1="292.4" x2="804.0" y2="351.7" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="305.6" width="2.46" height="32.0" fill="var(--down)"/>
<line x1="808.0" y1="334.5" x2="808.0" y2="367.3" stroke="var(--down)" class="wick"/>
<rect x="806.74" y="351.4" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="811.9" y1="353.6" x2="811.9" y2="378.6" stroke="var(--down)" class="wick"/>
<rect x="810.71" y="363.1" width="2.46" height="11.0" fill="var(--down)"/>
<line x1="815.9" y1="316.7" x2="815.9" y2="375.5" stroke="var(--up)" class="wick"/>
<rect x="814.67" y="322.1" width="2.46" height="51.4" fill="var(--up)"/>
<line x1="819.9" y1="280.7" x2="819.9" y2="316.7" stroke="var(--down)" class="wick"/>
<rect x="818.64" y="281.3" width="2.46" height="29.3" fill="var(--down)"/>
<line x1="823.8" y1="267.9" x2="823.8" y2="305.7" stroke="var(--up)" class="wick"/>
<rect x="822.61" y="295.1" width="2.46" height="7.2" fill="var(--up)"/>
<line x1="827.8" y1="277.5" x2="827.8" y2="305.0" stroke="var(--up)" class="wick"/>
<rect x="826.58" y="282.2" width="2.46" height="21.4" fill="var(--up)"/>
<line x1="831.8" y1="273.1" x2="831.8" y2="307.1" stroke="var(--down)" class="wick"/>
<rect x="830.55" y="274.8" width="2.46" height="20.4" fill="var(--down)"/>
<line x1="835.7" y1="268.8" x2="835.7" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="834.51" y="271.9" width="2.46" height="11.9" fill="var(--up)"/>
<line x1="839.7" y1="254.7" x2="839.7" y2="287.3" stroke="var(--down)" class="wick"/>
<rect x="838.48" y="272.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="843.7" y1="258.1" x2="843.7" y2="286.3" stroke="var(--up)" class="wick"/>
<rect x="842.45" y="265.8" width="2.46" height="6.1" fill="var(--up)"/>
<line x1="847.6" y1="259.7" x2="847.6" y2="299.2" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="268.8" width="2.46" height="14.7" fill="var(--up)"/>
<line x1="851.6" y1="240.0" x2="851.6" y2="281.6" stroke="var(--down)" class="wick"/>
<rect x="850.39" y="264.5" width="2.46" height="1.5" fill="var(--down)"/>
<line x1="855.6" y1="266.2" x2="855.6" y2="314.5" stroke="var(--down)" class="wick"/>
<rect x="854.35" y="285.6" width="2.46" height="19.7" fill="var(--down)"/>
<line x1="859.6" y1="300.6" x2="859.6" y2="323.4" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="304.4" width="2.46" height="13.8" fill="var(--down)"/>
<line x1="863.5" y1="301.6" x2="863.5" y2="321.3" stroke="var(--up)" class="wick"/>
<rect x="862.29" y="318.2" width="2.46" height="3.0" fill="var(--up)"/>
<line x1="867.5" y1="276.5" x2="867.5" y2="329.6" stroke="var(--down)" class="wick"/>
<rect x="866.26" y="283.9" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="871.5" y1="274.5" x2="871.5" y2="294.4" stroke="var(--down)" class="wick"/>
<rect x="870.23" y="285.9" width="2.46" height="7.6" fill="var(--down)"/>
<line x1="875.4" y1="299.2" x2="875.4" y2="342.6" stroke="var(--down)" class="wick"/>
<rect x="874.19" y="314.3" width="2.46" height="22.9" fill="var(--down)"/>
<line x1="879.4" y1="308.7" x2="879.4" y2="346.6" stroke="var(--down)" class="wick"/>
<rect x="878.16" y="316.7" width="2.46" height="21.7" fill="var(--down)"/>
<line x1="883.4" y1="323.4" x2="883.4" y2="358.6" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="327.8" width="2.46" height="25.4" fill="var(--down)"/>
<line x1="887.3" y1="353.1" x2="887.3" y2="375.9" stroke="var(--down)" class="wick"/>
<rect x="886.10" y="361.8" width="2.46" height="9.6" fill="var(--down)"/>
<line x1="891.3" y1="406.0" x2="891.3" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="890.07" y="413.9" width="2.46" height="17.8" fill="var(--down)"/>
<line x1="895.3" y1="382.4" x2="895.3" y2="427.0" stroke="var(--up)" class="wick"/>
<rect x="894.03" y="390.7" width="2.46" height="34.1" fill="var(--up)"/>
<line x1="899.2" y1="383.5" x2="899.2" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="898.00" y="396.6" width="2.46" height="10.2" fill="var(--down)"/>
<line x1="903.2" y1="368.1" x2="903.2" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="375.3" width="2.46" height="19.4" fill="var(--down)"/>
<line x1="907.2" y1="363.3" x2="907.2" y2="391.1" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="372.9" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="911.1" y1="378.2" x2="911.1" y2="401.5" stroke="var(--up)" class="wick"/>
<rect x="909.91" y="385.7" width="2.46" height="13.2" fill="var(--up)"/>
<line x1="915.1" y1="359.2" x2="915.1" y2="389.4" stroke="var(--up)" class="wick"/>
<rect x="913.87" y="362.7" width="2.46" height="26.5" fill="var(--up)"/>
<line x1="919.1" y1="340.5" x2="919.1" y2="361.2" stroke="var(--up)" class="wick"/>
<rect x="917.84" y="350.8" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="923.0" y1="335.8" x2="923.0" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="921.81" y="346.7" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="927.0" y1="351.4" x2="927.0" y2="387.6" stroke="var(--down)" class="wick"/>
<rect x="925.78" y="371.5" width="2.46" height="9.8" fill="var(--down)"/>
<line x1="931.0" y1="339.8" x2="931.0" y2="367.3" stroke="var(--up)" class="wick"/>
<rect x="929.75" y="348.5" width="2.46" height="16.1" fill="var(--up)"/>
<line x1="934.9" y1="305.9" x2="934.9" y2="366.8" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="321.2" width="2.46" height="36.9" fill="var(--down)"/>
<line x1="938.9" y1="355.9" x2="938.9" y2="386.6" stroke="var(--down)" class="wick"/>
<rect x="937.68" y="361.9" width="2.46" height="23.9" fill="var(--down)"/>
<line x1="942.9" y1="391.2" x2="942.9" y2="417.1" stroke="var(--down)" class="wick"/>
<rect x="941.65" y="395.1" width="2.46" height="15.2" fill="var(--down)"/>
<line x1="946.8" y1="415.6" x2="946.8" y2="433.0" stroke="var(--down)" class="wick"/>
<rect x="945.62" y="422.0" width="2.46" height="2.7" fill="var(--down)"/>
<line x1="950.8" y1="435.2" x2="950.8" y2="459.2" stroke="var(--up)" class="wick"/>
<rect x="949.59" y="437.4" width="2.46" height="12.1" fill="var(--up)"/>
<line x1="954.8" y1="421.1" x2="954.8" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="953.55" y="422.8" width="2.46" height="18.3" fill="var(--up)"/>
<line x1="958.8" y1="381.6" x2="958.8" y2="417.1" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="392.0" width="2.46" height="24.7" fill="var(--up)"/>
<line x1="962.7" y1="333.8" x2="962.7" y2="377.1" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="361.9" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="966.7" y1="352.0" x2="966.7" y2="382.4" stroke="var(--up)" class="wick"/>
<rect x="965.46" y="358.4" width="2.46" height="13.4" fill="var(--up)"/>
<line x1="970.7" y1="374.5" x2="970.7" y2="409.7" stroke="var(--down)" class="wick"/>
<rect x="969.43" y="393.8" width="2.46" height="6.9" fill="var(--down)"/>
<line x1="974.6" y1="389.7" x2="974.6" y2="417.1" stroke="var(--up)" class="wick"/>
<rect x="973.39" y="399.4" width="2.46" height="9.2" fill="var(--up)"/>
<line x1="978.6" y1="371.0" x2="978.6" y2="413.5" stroke="var(--down)" class="wick"/>
<rect x="977.36" y="373.6" width="2.46" height="32.4" fill="var(--down)"/>
<line x1="982.6" y1="392.8" x2="982.6" y2="435.2" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="394.6" width="2.46" height="34.5" fill="var(--up)"/>
<line x1="986.5" y1="372.8" x2="986.5" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="382.4" width="2.46" height="1.5" fill="var(--down)"/>
<line x1="990.5" y1="353.8" x2="990.5" y2="401.5" stroke="var(--down)" class="wick"/>
<rect x="989.27" y="360.4" width="2.46" height="27.1" fill="var(--down)"/>
<line x1="994.5" y1="384.6" x2="994.5" y2="408.9" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="390.5" width="2.46" height="16.8" fill="var(--up)"/>
<line x1="998.4" y1="379.0" x2="998.4" y2="405.3" stroke="var(--up)" class="wick"/>
<rect x="997.20" y="379.5" width="2.46" height="21.4" fill="var(--up)"/>
<line x1="1002.4" y1="370.3" x2="1002.4" y2="385.9" stroke="var(--up)" class="wick"/>
<rect x="1001.17" y="371.4" width="2.46" height="11.1" fill="var(--up)"/>
<line x1="1006.4" y1="333.5" x2="1006.4" y2="384.7" stroke="var(--up)" class="wick"/>
<rect x="1005.14" y="334.1" width="2.46" height="49.4" fill="var(--up)"/>
<line x1="1010.3" y1="329.9" x2="1010.3" y2="350.4" stroke="var(--down)" class="wick"/>
<rect x="1009.11" y="331.9" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="1014.3" y1="328.1" x2="1014.3" y2="352.7" stroke="var(--down)" class="wick"/>
<rect x="1013.07" y="338.8" width="2.46" height="5.3" fill="var(--down)"/>
<line x1="1018.3" y1="345.3" x2="1018.3" y2="362.4" stroke="var(--up)" class="wick"/>
<rect x="1017.04" y="356.9" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="1022.2" y1="330.0" x2="1022.2" y2="354.8" stroke="var(--down)" class="wick"/>
<rect x="1021.01" y="330.1" width="2.46" height="14.9" fill="var(--down)"/>
<line x1="1026.2" y1="322.4" x2="1026.2" y2="361.5" stroke="var(--down)" class="wick"/>
<rect x="1024.98" y="345.2" width="2.46" height="12.1" fill="var(--down)"/>
<line x1="1030.2" y1="456.4" x2="1030.2" y2="512.7" stroke="var(--down)" class="wick"/>
<rect x="1028.95" y="464.8" width="2.46" height="34.5" fill="var(--down)"/>
<line x1="1034.1" y1="493.3" x2="1034.1" y2="522.2" stroke="var(--up)" class="wick"/>
<rect x="1032.91" y="501.1" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="1038.1" y1="461.8" x2="1038.1" y2="497.1" stroke="var(--up)" class="wick"/>
<rect x="1036.88" y="463.3" width="2.46" height="31.9" fill="var(--up)"/>
<line x1="1042.1" y1="469.0" x2="1042.1" y2="491.6" stroke="var(--down)" class="wick"/>
<rect x="1040.85" y="475.6" width="2.46" height="2.7" fill="var(--down)"/>
<line x1="1046.0" y1="468.7" x2="1046.0" y2="496.0" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="476.6" width="2.46" height="15.9" fill="var(--down)"/>
<line x1="1050.0" y1="500.5" x2="1050.0" y2="520.6" stroke="var(--down)" class="wick"/>
<rect x="1048.79" y="502.4" width="2.46" height="13.3" fill="var(--down)"/>
<line x1="60" y1="483.2" x2="1052" y2="483.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="486.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$105 R1</text>
<text x="1058" y="498.7" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="319.2" x2="1052" y2="319.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="322.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$117 R2</text>
<text x="1058" y="334.7" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="249.0" x2="1052" y2="249.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="252.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$122 R3</text>
<text x="1058" y="264.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="551.0" x2="1052" y2="551.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="545.0" font-size="11.5" fill="var(--support)" font-weight="600">$100 S1</text>
<text x="1058" y="557.0" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="515.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="507.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $103 (2026-08-27)</text>
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
| R3 | $122 | 2 | 2026-01-20·2026-06-16 — FY2026 실적 발표 전후의 고점대와 5월 최고가 이후 반등 실패 지점 |
| R2 | $117 | 4 | 2025-12-15·2026-07-17·2026-07-28·2026-08-19 — 가장 두꺼운 저항. **2026-08-19는 Q2 FY27 실적 발표 전날**로, 다음 날 갭다운이 이 레벨에서 시작됐다 |
| R1 | $105 | 2 | 2025-09-17·2025-09-30 — 1년 전 상승 초입의 고점대. 8월 급락 이후 되돌림이 이 부근($106.49, 2026-08-24)에서 멈췄다 |
| **현재가** | **$102.63** (2026-08-27 종가) | — | R1과 S1 사이 |
| S1 | $100 | 4 | 2025-09-23·2025-10-02·2025-11-06·2025-11-14 — 1년 중 유일하게 유효한 지지 클러스터. 심리적 라운드 넘버와 겹친다 |
| 참고선 | $135.16 | — | 최근 1년 최고(2026-05-18). 현재가 대비 +31.7%로 근시일 저항으로 보기 어렵다 |
| 참고선 | $95.80 | — | 최근 1년 최저. S1($100) 아래로는 터치 2회 이상 클러스터가 형성되지 않아 레벨이 아닌 참고선으로 둔다 |

**레벨을 3개씩 맞추지 않았다.** 저항은 3개(R1~R3)가 잡혔지만 **지지는 S1 하나뿐**이다 — 최근 1년의 스윙 저점이 2025년 9~11월 $100 부근에 몰려 있고, 그 아래 구간($95.80~$100)에는 터치 2회 이상 클러스터가 만들어지지 않았기 때문이다. 이는 **아래쪽에 참고할 가격 기억이 얇다**는 뜻이며, S1이 깨질 경우 다음 준거점이 없다는 점을 함께 읽어야 한다.

---

## 3. 관측된 특이 구간 — 2026-08-20 Q2 FY2027 실적 발표 갭다운

- Q2 FY2027 실적 발표(2026-08-20 장 전). 조정 EPS $0.81·매출 $187.9B로 컨센서스를 상회하고 연간 가이던스도 상향했으나, Q3 순매출 +3.0~3.75%·조정 영업이익 +2.0~4.0% 가이던스가 시장 기대(약 +6%)에 크게 못 미쳤다. 상세는 [최근 뉴스 / 이슈](./08_news.md) 로그 참고.
- 종가 기준 전일 대비 **−9.15%** ($114.30 → $103.84), 거래량은 평소(일 2,299만 주 내외) 대비 약 **3.6배**인 **8,360만 주**. 2022년 이후 최대 일간 낙폭이다.
- 이 하루로 **$105~$117 구간이 통째로 건너뛰어졌다.** 갭 구간에는 거래가 거의 없어 가격 기억이 얇고, 그래서 R1($105)과 R2($117) 사이에는 유효한 클러스터가 없다. 갭 이전에 형성된 $117·$122 레벨은 지금의 거래 레짐과 다른 구간(PER 40배대)에서 만들어진 것이므로, 되돌림 저항으로 볼 때 강도를 낮춰 읽어야 한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, **배당은 미반영** — 기간 내 분기 배당 4회 지급)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py WMT --name Walmart --close-on 2026-08-28 --emit all` (기본 파라미터. `--force-level`·`--ref-line`은 쓰지 않았고, 위 참고선 2개는 표에만 손으로 덧붙인 것이다)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **3절의 갭다운이 레벨 해석을 크게 왜곡한다.** $105~$117 구간이 하루에 건너뛰어져 그 안에 거래 기억이 없고, R2·R3는 갭 이전 레짐에서 만들어진 레벨이다.
    - **지지 레벨이 1개뿐**이라 하방 준거가 얇다. 기간을 늘리면 달라지지만, 그 경우 2024-02 3:1 분할 이전 구간과 재평가 이전 가격대가 섞인다 — 다년 구조는 [주봉 문서](./10_technical_weekly.md)에서 별도로 본다.
    - **`--close-on 2026-08-28`을 지정했으나 일봉 시계열은 2026-08-27에서 끝난다**(그 날짜의 일봉 수정주가가 아직 제공되지 않음). 다른 문서의 기준 종가와 하루 차이가 나는 이유이며, 위 대조 블록에 남겼다.

---

*작성일: 2026-08-30*
