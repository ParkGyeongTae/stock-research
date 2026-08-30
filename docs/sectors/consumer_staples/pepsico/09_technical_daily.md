# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 이 차트의 마지막 거래일은 **2026-08-27(종가 $139.72)**로, 핵심 지표·밸류에이션 / 적정주가가 기준으로 쓰는 **2026-08-28 종가 $141.07보다 하루 이르다.** 수집 시점(2026-08-30)에 Yahoo 일봉 시계열이 2026-08-28을 아직 포함하지 않았기 때문이며, 같은 소스의 주봉(2026-08-28 종가 $141.07)과 집계 사이트 stockanalysis.com은 $141.07로 일치한다. **두 값의 차이 $1.35(1.0%)는 하루치 차이일 뿐 수정주가 기준 차이가 아니다.**

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

<div class="pep-chart">
<style>
.pep-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .pep-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .pep-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.pep-chart svg { width:100%; height:auto; display:block; }
.pep-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.pep-chart .title { fill: var(--ink); font-weight:600; }
.pep-chart .grid { stroke: var(--grid); stroke-width:1; }
.pep-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="PepsiCo(PEP) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">PepsiCo (PEP) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $139.72 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="520.4" x2="1052" y2="520.4" class="grid"/>
<text x="52" y="524.4" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="379.7" x2="1052" y2="379.7" class="grid"/>
<text x="52" y="383.7" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="239.0" x2="1052" y2="239.0" class="grid"/>
<text x="52" y="243.0" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="98.2" x2="1052" y2="98.2" class="grid"/>
<text x="52" y="102.2" font-size="11" text-anchor="end" fill="var(--muted)">170</text>
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
<line x1="335.8" y1="56.0" x2="335.8" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="341.8" y="68.0" font-size="10.5" fill="var(--down)">2025-12-08 Elliott 합의 발표</text>
<line x1="911.1" y1="56.0" x2="911.1" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="917.1" y="68.0" font-size="10.5" fill="var(--down)">2026-07-09 2026 Q2 실적발표</text>
<line x1="62.0" y1="390.7" x2="62.0" y2="423.8" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="398.7" width="2.46" height="21.8" fill="var(--up)"/>
<line x1="66.0" y1="269.9" x2="66.0" y2="376.7" stroke="var(--down)" class="wick"/>
<rect x="64.72" y="275.0" width="2.46" height="100.8" fill="var(--down)"/>
<line x1="69.9" y1="373.2" x2="69.9" y2="420.4" stroke="var(--down)" class="wick"/>
<rect x="68.69" y="380.4" width="2.46" height="18.4" fill="var(--down)"/>
<line x1="73.9" y1="387.2" x2="73.9" y2="429.7" stroke="var(--down)" class="wick"/>
<rect x="72.66" y="393.5" width="2.46" height="30.0" fill="var(--down)"/>
<line x1="77.9" y1="409.5" x2="77.9" y2="446.1" stroke="var(--up)" class="wick"/>
<rect x="76.63" y="430.5" width="2.46" height="5.5" fill="var(--up)"/>
<line x1="81.8" y1="439.9" x2="81.8" y2="515.5" stroke="var(--down)" class="wick"/>
<rect x="80.59" y="439.9" width="2.46" height="56.4" fill="var(--down)"/>
<line x1="85.8" y1="469.4" x2="85.8" y2="505.0" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="476.8" width="2.46" height="27.0" fill="var(--up)"/>
<line x1="89.8" y1="476.7" x2="89.8" y2="500.5" stroke="var(--up)" class="wick"/>
<rect x="88.53" y="483.0" width="2.46" height="6.1" fill="var(--up)"/>
<line x1="93.7" y1="453.6" x2="93.7" y2="485.3" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="460.9" width="2.46" height="18.9" fill="var(--up)"/>
<line x1="97.7" y1="460.6" x2="97.7" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="96.47" y="463.2" width="2.46" height="7.6" fill="var(--down)"/>
<line x1="101.7" y1="470.8" x2="101.7" y2="513.0" stroke="var(--down)" class="wick"/>
<rect x="100.43" y="472.6" width="2.46" height="38.8" fill="var(--down)"/>
<line x1="105.6" y1="502.0" x2="105.6" y2="521.7" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="510.7" width="2.46" height="9.3" fill="var(--down)"/>
<line x1="109.6" y1="491.7" x2="109.6" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="503.1" width="2.46" height="14.9" fill="var(--up)"/>
<line x1="113.6" y1="497.5" x2="113.6" y2="515.0" stroke="var(--up)" class="wick"/>
<rect x="112.34" y="510.2" width="2.46" height="1.3" fill="var(--up)"/>
<line x1="117.5" y1="491.2" x2="117.5" y2="514.0" stroke="var(--up)" class="wick"/>
<rect x="116.31" y="495.7" width="2.46" height="4.2" fill="var(--up)"/>
<line x1="121.5" y1="499.1" x2="121.5" y2="521.3" stroke="var(--down)" class="wick"/>
<rect x="120.27" y="505.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="125.5" y1="489.1" x2="125.5" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="124.24" y="493.7" width="2.46" height="12.1" fill="var(--up)"/>
<line x1="129.4" y1="487.5" x2="129.4" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="128.21" y="489.9" width="2.46" height="5.1" fill="var(--up)"/>
<line x1="133.4" y1="472.3" x2="133.4" y2="522.4" stroke="var(--down)" class="wick"/>
<rect x="132.18" y="478.2" width="2.46" height="43.3" fill="var(--down)"/>
<line x1="137.4" y1="506.5" x2="137.4" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="514.3" width="2.46" height="7.0" fill="var(--up)"/>
<line x1="141.3" y1="511.0" x2="141.3" y2="532.8" stroke="var(--down)" class="wick"/>
<rect x="140.11" y="514.3" width="2.46" height="3.8" fill="var(--down)"/>
<line x1="145.3" y1="505.9" x2="145.3" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="514.3" width="2.46" height="3.8" fill="var(--up)"/>
<line x1="149.3" y1="473.0" x2="149.3" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="148.05" y="476.3" width="2.46" height="32.8" fill="var(--up)"/>
<line x1="153.2" y1="474.7" x2="153.2" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="152.02" y="487.9" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="157.2" y1="473.2" x2="157.2" y2="494.3" stroke="var(--down)" class="wick"/>
<rect x="155.99" y="488.6" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="161.2" y1="494.4" x2="161.2" y2="536.2" stroke="var(--down)" class="wick"/>
<rect x="159.95" y="495.5" width="2.46" height="29.1" fill="var(--down)"/>
<line x1="165.2" y1="494.5" x2="165.2" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="163.92" y="509.3" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="169.1" y1="506.7" x2="169.1" y2="538.9" stroke="var(--down)" class="wick"/>
<rect x="167.89" y="509.3" width="2.46" height="27.4" fill="var(--down)"/>
<line x1="173.1" y1="453.7" x2="173.1" y2="540.3" stroke="var(--up)" class="wick"/>
<rect x="171.86" y="454.2" width="2.46" height="59.8" fill="var(--up)"/>
<line x1="177.1" y1="368.2" x2="177.1" y2="450.1" stroke="var(--up)" class="wick"/>
<rect x="175.83" y="378.6" width="2.46" height="62.6" fill="var(--up)"/>
<line x1="181.0" y1="380.0" x2="181.0" y2="417.1" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="395.3" width="2.46" height="3.4" fill="var(--up)"/>
<line x1="185.0" y1="356.9" x2="185.0" y2="400.8" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="358.0" width="2.46" height="40.1" fill="var(--up)"/>
<line x1="189.0" y1="346.1" x2="189.0" y2="391.4" stroke="var(--down)" class="wick"/>
<rect x="187.73" y="361.0" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="192.9" y1="318.1" x2="192.9" y2="347.5" stroke="var(--up)" class="wick"/>
<rect x="191.70" y="342.1" width="2.46" height="4.1" fill="var(--up)"/>
<line x1="196.9" y1="324.7" x2="196.9" y2="355.2" stroke="var(--down)" class="wick"/>
<rect x="195.67" y="326.6" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="200.9" y1="317.5" x2="200.9" y2="341.4" stroke="var(--down)" class="wick"/>
<rect x="199.63" y="317.5" width="2.46" height="11.0" fill="var(--down)"/>
<line x1="204.8" y1="306.7" x2="204.8" y2="339.7" stroke="var(--down)" class="wick"/>
<rect x="203.60" y="313.6" width="2.46" height="21.4" fill="var(--down)"/>
<line x1="208.8" y1="306.8" x2="208.8" y2="341.6" stroke="var(--down)" class="wick"/>
<rect x="207.57" y="335.4" width="2.46" height="1.7" fill="var(--down)"/>
<line x1="212.8" y1="331.9" x2="212.8" y2="365.2" stroke="var(--down)" class="wick"/>
<rect x="211.54" y="335.1" width="2.46" height="23.4" fill="var(--down)"/>
<line x1="216.7" y1="345.6" x2="216.7" y2="361.8" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="351.0" width="2.46" height="6.9" fill="var(--down)"/>
<line x1="220.7" y1="339.3" x2="220.7" y2="366.2" stroke="var(--up)" class="wick"/>
<rect x="219.47" y="342.7" width="2.46" height="22.8" fill="var(--up)"/>
<line x1="224.7" y1="334.5" x2="224.7" y2="380.8" stroke="var(--down)" class="wick"/>
<rect x="223.44" y="359.9" width="2.46" height="18.2" fill="var(--down)"/>
<line x1="228.6" y1="398.6" x2="228.6" y2="468.8" stroke="var(--down)" class="wick"/>
<rect x="227.41" y="407.1" width="2.46" height="26.6" fill="var(--down)"/>
<line x1="232.6" y1="406.6" x2="232.6" y2="432.5" stroke="var(--up)" class="wick"/>
<rect x="231.38" y="414.2" width="2.46" height="17.0" fill="var(--up)"/>
<line x1="236.6" y1="421.9" x2="236.6" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="235.35" y="433.2" width="2.46" height="1.5" fill="var(--down)"/>
<line x1="240.5" y1="437.3" x2="240.5" y2="474.7" stroke="var(--down)" class="wick"/>
<rect x="239.31" y="438.0" width="2.46" height="31.8" fill="var(--down)"/>
<line x1="244.5" y1="451.1" x2="244.5" y2="491.5" stroke="var(--down)" class="wick"/>
<rect x="243.28" y="454.3" width="2.46" height="25.3" fill="var(--down)"/>
<line x1="248.5" y1="474.3" x2="248.5" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="247.25" y="479.6" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="252.4" y1="475.3" x2="252.4" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="251.22" y="486.5" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="256.4" y1="463.4" x2="256.4" y2="497.2" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="478.9" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="260.4" y1="477.9" x2="260.4" y2="502.7" stroke="var(--up)" class="wick"/>
<rect x="259.15" y="483.6" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="264.4" y1="439.4" x2="264.4" y2="482.7" stroke="var(--up)" class="wick"/>
<rect x="263.12" y="448.9" width="2.46" height="25.3" fill="var(--up)"/>
<line x1="268.3" y1="443.0" x2="268.3" y2="463.3" stroke="var(--down)" class="wick"/>
<rect x="267.09" y="456.3" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="272.3" y1="430.5" x2="272.3" y2="469.1" stroke="var(--up)" class="wick"/>
<rect x="271.06" y="449.8" width="2.46" height="12.9" fill="var(--up)"/>
<line x1="276.3" y1="424.2" x2="276.3" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="275.03" y="437.5" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="280.2" y1="406.3" x2="280.2" y2="447.0" stroke="var(--up)" class="wick"/>
<rect x="278.99" y="410.2" width="2.46" height="24.1" fill="var(--up)"/>
<line x1="284.2" y1="382.1" x2="284.2" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="282.96" y="397.0" width="2.46" height="6.6" fill="var(--up)"/>
<line x1="288.2" y1="396.6" x2="288.2" y2="426.3" stroke="var(--down)" class="wick"/>
<rect x="286.93" y="403.6" width="2.46" height="16.7" fill="var(--down)"/>
<line x1="292.1" y1="420.8" x2="292.1" y2="451.5" stroke="var(--down)" class="wick"/>
<rect x="290.90" y="427.6" width="2.46" height="7.0" fill="var(--down)"/>
<line x1="296.1" y1="394.6" x2="296.1" y2="436.3" stroke="var(--up)" class="wick"/>
<rect x="294.87" y="431.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="300.1" y1="431.2" x2="300.1" y2="453.5" stroke="var(--down)" class="wick"/>
<rect x="298.83" y="438.4" width="2.46" height="4.6" fill="var(--down)"/>
<line x1="304.0" y1="420.2" x2="304.0" y2="442.1" stroke="var(--up)" class="wick"/>
<rect x="302.80" y="434.5" width="2.46" height="2.5" fill="var(--up)"/>
<line x1="308.0" y1="401.2" x2="308.0" y2="432.8" stroke="var(--up)" class="wick"/>
<rect x="306.77" y="408.1" width="2.46" height="23.4" fill="var(--up)"/>
<line x1="312.0" y1="396.3" x2="312.0" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="310.74" y="397.4" width="2.46" height="21.3" fill="var(--up)"/>
<line x1="315.9" y1="382.2" x2="315.9" y2="400.7" stroke="var(--up)" class="wick"/>
<rect x="314.71" y="386.6" width="2.46" height="12.4" fill="var(--up)"/>
<line x1="319.9" y1="386.6" x2="319.9" y2="428.5" stroke="var(--down)" class="wick"/>
<rect x="318.67" y="387.3" width="2.46" height="12.0" fill="var(--down)"/>
<line x1="323.9" y1="369.9" x2="323.9" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="322.64" y="398.1" width="2.46" height="8.9" fill="var(--down)"/>
<line x1="327.8" y1="404.3" x2="327.8" y2="434.2" stroke="var(--down)" class="wick"/>
<rect x="326.61" y="411.4" width="2.46" height="11.8" fill="var(--down)"/>
<line x1="331.8" y1="438.8" x2="331.8" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="441.3" width="2.46" height="8.4" fill="var(--down)"/>
<line x1="335.8" y1="428.1" x2="335.8" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="334.55" y="441.2" width="2.46" height="8.7" fill="var(--up)"/>
<line x1="339.7" y1="414.0" x2="339.7" y2="465.4" stroke="var(--down)" class="wick"/>
<rect x="338.51" y="431.1" width="2.46" height="24.1" fill="var(--down)"/>
<line x1="343.7" y1="382.8" x2="343.7" y2="421.9" stroke="var(--up)" class="wick"/>
<rect x="342.48" y="383.9" width="2.46" height="27.2" fill="var(--up)"/>
<line x1="347.7" y1="367.2" x2="347.7" y2="406.0" stroke="var(--down)" class="wick"/>
<rect x="346.45" y="377.6" width="2.46" height="15.6" fill="var(--down)"/>
<line x1="351.6" y1="370.3" x2="351.6" y2="397.4" stroke="var(--up)" class="wick"/>
<rect x="350.42" y="370.6" width="2.46" height="12.7" fill="var(--up)"/>
<line x1="355.6" y1="355.8" x2="355.6" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="354.39" y="362.5" width="2.46" height="3.9" fill="var(--up)"/>
<line x1="359.6" y1="346.6" x2="359.6" y2="379.8" stroke="var(--down)" class="wick"/>
<rect x="358.35" y="351.7" width="2.46" height="22.8" fill="var(--down)"/>
<line x1="363.6" y1="362.3" x2="363.6" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="362.32" y="374.4" width="2.46" height="4.2" fill="var(--down)"/>
<line x1="367.5" y1="374.5" x2="367.5" y2="390.3" stroke="var(--down)" class="wick"/>
<rect x="366.29" y="382.5" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="371.5" y1="381.3" x2="371.5" y2="409.3" stroke="var(--down)" class="wick"/>
<rect x="370.26" y="391.7" width="2.46" height="13.9" fill="var(--down)"/>
<line x1="375.5" y1="394.1" x2="375.5" y2="430.2" stroke="var(--down)" class="wick"/>
<rect x="374.23" y="414.5" width="2.46" height="6.8" fill="var(--down)"/>
<line x1="379.4" y1="419.3" x2="379.4" y2="470.3" stroke="var(--down)" class="wick"/>
<rect x="378.19" y="419.3" width="2.46" height="49.4" fill="var(--down)"/>
<line x1="383.4" y1="464.3" x2="383.4" y2="478.9" stroke="var(--down)" class="wick"/>
<rect x="382.16" y="467.1" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="387.4" y1="465.0" x2="387.4" y2="477.0" stroke="var(--up)" class="wick"/>
<rect x="386.13" y="467.2" width="2.46" height="3.1" fill="var(--up)"/>
<line x1="391.3" y1="449.4" x2="391.3" y2="469.8" stroke="var(--up)" class="wick"/>
<rect x="390.10" y="460.8" width="2.46" height="7.0" fill="var(--up)"/>
<line x1="395.3" y1="446.3" x2="395.3" y2="465.3" stroke="var(--up)" class="wick"/>
<rect x="394.07" y="461.9" width="2.46" height="2.7" fill="var(--up)"/>
<line x1="399.3" y1="463.7" x2="399.3" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="466.5" width="2.46" height="4.4" fill="var(--down)"/>
<line x1="403.2" y1="472.5" x2="403.2" y2="490.9" stroke="var(--down)" class="wick"/>
<rect x="402.00" y="475.1" width="2.46" height="13.9" fill="var(--down)"/>
<line x1="407.2" y1="495.0" x2="407.2" y2="528.9" stroke="var(--down)" class="wick"/>
<rect x="405.97" y="497.1" width="2.46" height="24.5" fill="var(--down)"/>
<line x1="411.2" y1="519.6" x2="411.2" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="409.94" y="524.9" width="2.46" height="10.1" fill="var(--down)"/>
<line x1="415.1" y1="522.8" x2="415.1" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="413.91" y="531.4" width="2.46" height="31.1" fill="var(--down)"/>
<line x1="419.1" y1="527.8" x2="419.1" y2="576.6" stroke="var(--up)" class="wick"/>
<rect x="417.87" y="529.3" width="2.46" height="39.4" fill="var(--up)"/>
<line x1="423.1" y1="509.3" x2="423.1" y2="538.7" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="521.7" width="2.46" height="6.6" fill="var(--up)"/>
<line x1="427.0" y1="499.2" x2="427.0" y2="540.7" stroke="var(--up)" class="wick"/>
<rect x="425.81" y="501.3" width="2.46" height="20.4" fill="var(--up)"/>
<line x1="431.0" y1="469.1" x2="431.0" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="471.5" width="2.46" height="33.5" fill="var(--up)"/>
<line x1="435.0" y1="431.8" x2="435.0" y2="476.3" stroke="var(--up)" class="wick"/>
<rect x="433.75" y="437.1" width="2.46" height="39.1" fill="var(--up)"/>
<line x1="438.9" y1="421.6" x2="438.9" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="437.71" y="428.0" width="2.46" height="7.2" fill="var(--up)"/>
<line x1="442.9" y1="414.2" x2="442.9" y2="442.9" stroke="var(--down)" class="wick"/>
<rect x="441.68" y="419.7" width="2.46" height="11.8" fill="var(--down)"/>
<line x1="446.9" y1="412.6" x2="446.9" y2="459.6" stroke="var(--up)" class="wick"/>
<rect x="445.65" y="412.6" width="2.46" height="20.3" fill="var(--up)"/>
<line x1="450.8" y1="407.7" x2="450.8" y2="450.9" stroke="var(--down)" class="wick"/>
<rect x="449.62" y="421.2" width="2.46" height="4.4" fill="var(--down)"/>
<line x1="454.8" y1="420.1" x2="454.8" y2="461.8" stroke="var(--down)" class="wick"/>
<rect x="453.59" y="426.4" width="2.46" height="32.1" fill="var(--down)"/>
<line x1="458.8" y1="452.3" x2="458.8" y2="477.4" stroke="var(--up)" class="wick"/>
<rect x="457.55" y="456.0" width="2.46" height="10.1" fill="var(--up)"/>
<line x1="462.8" y1="437.1" x2="462.8" y2="462.2" stroke="var(--up)" class="wick"/>
<rect x="461.52" y="437.8" width="2.46" height="15.1" fill="var(--up)"/>
<line x1="466.7" y1="396.3" x2="466.7" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="465.49" y="396.9" width="2.46" height="42.6" fill="var(--up)"/>
<line x1="470.7" y1="379.1" x2="470.7" y2="411.2" stroke="var(--up)" class="wick"/>
<rect x="469.46" y="400.8" width="2.46" height="1.3" fill="var(--up)"/>
<line x1="474.7" y1="367.6" x2="474.7" y2="401.7" stroke="var(--down)" class="wick"/>
<rect x="473.43" y="396.0" width="2.46" height="2.1" fill="var(--down)"/>
<line x1="478.6" y1="325.0" x2="478.6" y2="399.5" stroke="var(--up)" class="wick"/>
<rect x="477.39" y="328.6" width="2.46" height="65.0" fill="var(--up)"/>
<line x1="482.6" y1="286.5" x2="482.6" y2="334.8" stroke="var(--up)" class="wick"/>
<rect x="481.36" y="306.5" width="2.46" height="16.0" fill="var(--up)"/>
<line x1="486.6" y1="190.5" x2="486.6" y2="302.3" stroke="var(--up)" class="wick"/>
<rect x="485.33" y="198.9" width="2.46" height="88.0" fill="var(--up)"/>
<line x1="490.5" y1="127.2" x2="490.5" y2="180.3" stroke="var(--up)" class="wick"/>
<rect x="489.30" y="152.0" width="2.46" height="18.2" fill="var(--up)"/>
<line x1="494.5" y1="126.2" x2="494.5" y2="165.1" stroke="var(--up)" class="wick"/>
<rect x="493.27" y="133.0" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="498.5" y1="87.7" x2="498.5" y2="136.8" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="91.3" width="2.46" height="42.8" fill="var(--up)"/>
<line x1="502.4" y1="99.2" x2="502.4" y2="169.4" stroke="var(--down)" class="wick"/>
<rect x="501.20" y="105.3" width="2.46" height="42.6" fill="var(--down)"/>
<line x1="506.4" y1="134.7" x2="506.4" y2="186.3" stroke="var(--up)" class="wick"/>
<rect x="505.17" y="140.9" width="2.46" height="17.2" fill="var(--up)"/>
<line x1="510.4" y1="94.4" x2="510.4" y2="154.2" stroke="var(--up)" class="wick"/>
<rect x="509.14" y="110.2" width="2.46" height="21.1" fill="var(--up)"/>
<line x1="514.3" y1="77.4" x2="514.3" y2="139.2" stroke="var(--down)" class="wick"/>
<rect x="513.11" y="101.6" width="2.46" height="36.0" fill="var(--down)"/>
<line x1="518.3" y1="128.1" x2="518.3" y2="168.6" stroke="var(--down)" class="wick"/>
<rect x="517.07" y="137.6" width="2.46" height="17.7" fill="var(--down)"/>
<line x1="522.3" y1="132.8" x2="522.3" y2="227.6" stroke="var(--down)" class="wick"/>
<rect x="521.04" y="152.8" width="2.46" height="59.1" fill="var(--down)"/>
<line x1="526.2" y1="175.2" x2="526.2" y2="230.1" stroke="var(--up)" class="wick"/>
<rect x="525.01" y="177.2" width="2.46" height="36.6" fill="var(--up)"/>
<line x1="530.2" y1="167.9" x2="530.2" y2="194.9" stroke="var(--up)" class="wick"/>
<rect x="528.98" y="174.4" width="2.46" height="2.8" fill="var(--up)"/>
<line x1="534.2" y1="169.0" x2="534.2" y2="196.5" stroke="var(--up)" class="wick"/>
<rect x="532.95" y="169.4" width="2.46" height="4.1" fill="var(--up)"/>
<line x1="538.1" y1="115.0" x2="538.1" y2="179.3" stroke="var(--up)" class="wick"/>
<rect x="536.91" y="121.9" width="2.46" height="53.9" fill="var(--up)"/>
<line x1="542.1" y1="101.2" x2="542.1" y2="129.6" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="104.7" width="2.46" height="18.4" fill="var(--up)"/>
<line x1="546.1" y1="105.3" x2="546.1" y2="154.5" stroke="var(--up)" class="wick"/>
<rect x="544.85" y="109.9" width="2.46" height="7.9" fill="var(--up)"/>
<line x1="550.0" y1="97.4" x2="550.0" y2="138.2" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="103.4" width="2.46" height="28.9" fill="var(--down)"/>
<line x1="554.0" y1="94.3" x2="554.0" y2="128.9" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="101.9" width="2.46" height="19.1" fill="var(--up)"/>
<line x1="558.0" y1="104.7" x2="558.0" y2="138.5" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="111.6" width="2.46" height="24.9" fill="var(--down)"/>
<line x1="562.0" y1="137.3" x2="562.0" y2="187.3" stroke="var(--down)" class="wick"/>
<rect x="560.72" y="146.9" width="2.46" height="22.9" fill="var(--down)"/>
<line x1="565.9" y1="155.5" x2="565.9" y2="191.5" stroke="var(--down)" class="wick"/>
<rect x="564.69" y="168.0" width="2.46" height="15.8" fill="var(--down)"/>
<line x1="569.9" y1="191.1" x2="569.9" y2="236.7" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="208.6" width="2.46" height="20.5" fill="var(--down)"/>
<line x1="573.9" y1="245.6" x2="573.9" y2="294.0" stroke="var(--up)" class="wick"/>
<rect x="572.63" y="247.0" width="2.46" height="16.6" fill="var(--up)"/>
<line x1="577.8" y1="204.8" x2="577.8" y2="265.7" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="217.4" width="2.46" height="33.2" fill="var(--up)"/>
<line x1="581.8" y1="198.7" x2="581.8" y2="244.7" stroke="var(--up)" class="wick"/>
<rect x="580.56" y="228.0" width="2.46" height="1.1" fill="var(--up)"/>
<line x1="585.8" y1="226.2" x2="585.8" y2="268.7" stroke="var(--down)" class="wick"/>
<rect x="584.53" y="234.6" width="2.46" height="2.3" fill="var(--down)"/>
<line x1="589.7" y1="217.3" x2="589.7" y2="257.4" stroke="var(--down)" class="wick"/>
<rect x="588.50" y="254.9" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="593.7" y1="217.7" x2="593.7" y2="249.7" stroke="var(--up)" class="wick"/>
<rect x="592.47" y="240.7" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="597.7" y1="216.7" x2="597.7" y2="273.6" stroke="var(--down)" class="wick"/>
<rect x="596.43" y="219.8" width="2.46" height="51.2" fill="var(--down)"/>
<line x1="601.6" y1="251.5" x2="601.6" y2="291.2" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="255.4" width="2.46" height="32.8" fill="var(--down)"/>
<line x1="605.6" y1="293.6" x2="605.6" y2="333.4" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="305.8" width="2.46" height="24.1" fill="var(--down)"/>
<line x1="609.6" y1="313.8" x2="609.6" y2="342.3" stroke="var(--down)" class="wick"/>
<rect x="608.34" y="326.9" width="2.46" height="14.2" fill="var(--down)"/>
<line x1="613.5" y1="331.7" x2="613.5" y2="389.0" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="345.2" width="2.46" height="33.9" fill="var(--down)"/>
<line x1="617.5" y1="347.3" x2="617.5" y2="380.5" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="347.3" width="2.46" height="20.0" fill="var(--down)"/>
<line x1="621.5" y1="343.4" x2="621.5" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="620.24" y="371.4" width="2.46" height="2.0" fill="var(--up)"/>
<line x1="625.4" y1="353.8" x2="625.4" y2="393.4" stroke="var(--up)" class="wick"/>
<rect x="624.21" y="355.4" width="2.46" height="6.1" fill="var(--up)"/>
<line x1="629.4" y1="335.4" x2="629.4" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="628.18" y="352.5" width="2.46" height="15.5" fill="var(--down)"/>
<line x1="633.4" y1="315.8" x2="633.4" y2="373.1" stroke="var(--up)" class="wick"/>
<rect x="632.15" y="336.9" width="2.46" height="26.7" fill="var(--up)"/>
<line x1="637.3" y1="261.6" x2="637.3" y2="332.3" stroke="var(--up)" class="wick"/>
<rect x="636.11" y="283.7" width="2.46" height="42.2" fill="var(--up)"/>
<line x1="641.3" y1="271.8" x2="641.3" y2="321.0" stroke="var(--down)" class="wick"/>
<rect x="640.08" y="271.8" width="2.46" height="33.5" fill="var(--down)"/>
<line x1="645.3" y1="307.2" x2="645.3" y2="333.8" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="314.3" width="2.46" height="15.5" fill="var(--up)"/>
<line x1="649.2" y1="280.3" x2="649.2" y2="320.3" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="281.0" width="2.46" height="33.1" fill="var(--up)"/>
<line x1="653.2" y1="283.2" x2="653.2" y2="303.7" stroke="var(--up)" class="wick"/>
<rect x="651.99" y="285.0" width="2.46" height="4.5" fill="var(--up)"/>
<line x1="657.2" y1="287.7" x2="657.2" y2="343.5" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="292.7" width="2.46" height="41.8" fill="var(--down)"/>
<line x1="661.2" y1="311.9" x2="661.2" y2="355.1" stroke="var(--up)" class="wick"/>
<rect x="659.92" y="312.1" width="2.46" height="41.1" fill="var(--up)"/>
<line x1="665.1" y1="267.0" x2="665.1" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="663.89" y="274.3" width="2.46" height="53.3" fill="var(--up)"/>
<line x1="669.1" y1="270.1" x2="669.1" y2="290.6" stroke="var(--down)" class="wick"/>
<rect x="667.86" y="278.9" width="2.46" height="1.4" fill="var(--down)"/>
<line x1="673.1" y1="280.8" x2="673.1" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="671.83" y="281.3" width="2.46" height="15.6" fill="var(--down)"/>
<line x1="677.0" y1="286.4" x2="677.0" y2="319.3" stroke="var(--up)" class="wick"/>
<rect x="675.79" y="299.2" width="2.46" height="17.0" fill="var(--up)"/>
<line x1="681.0" y1="298.6" x2="681.0" y2="332.7" stroke="var(--down)" class="wick"/>
<rect x="679.76" y="309.1" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="685.0" y1="241.9" x2="685.0" y2="319.7" stroke="var(--up)" class="wick"/>
<rect x="683.73" y="261.8" width="2.46" height="40.0" fill="var(--up)"/>
<line x1="688.9" y1="238.5" x2="688.9" y2="288.6" stroke="var(--down)" class="wick"/>
<rect x="687.70" y="263.5" width="2.46" height="8.3" fill="var(--down)"/>
<line x1="692.9" y1="255.3" x2="692.9" y2="297.5" stroke="var(--down)" class="wick"/>
<rect x="691.67" y="256.7" width="2.46" height="24.6" fill="var(--down)"/>
<line x1="696.9" y1="280.6" x2="696.9" y2="327.2" stroke="var(--down)" class="wick"/>
<rect x="695.63" y="284.8" width="2.46" height="25.6" fill="var(--down)"/>
<line x1="700.8" y1="278.1" x2="700.8" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="308.2" width="2.46" height="18.2" fill="var(--down)"/>
<line x1="704.8" y1="286.7" x2="704.8" y2="315.4" stroke="var(--up)" class="wick"/>
<rect x="703.57" y="299.5" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="708.8" y1="291.3" x2="708.8" y2="314.1" stroke="var(--down)" class="wick"/>
<rect x="707.54" y="296.2" width="2.46" height="6.9" fill="var(--down)"/>
<line x1="712.7" y1="286.1" x2="712.7" y2="323.4" stroke="var(--down)" class="wick"/>
<rect x="711.51" y="301.9" width="2.46" height="20.1" fill="var(--down)"/>
<line x1="716.7" y1="265.6" x2="716.7" y2="304.8" stroke="var(--down)" class="wick"/>
<rect x="715.47" y="284.0" width="2.46" height="7.2" fill="var(--down)"/>
<line x1="720.7" y1="288.4" x2="720.7" y2="330.7" stroke="var(--down)" class="wick"/>
<rect x="719.44" y="301.0" width="2.46" height="4.2" fill="var(--down)"/>
<line x1="724.6" y1="253.0" x2="724.6" y2="305.4" stroke="var(--up)" class="wick"/>
<rect x="723.41" y="260.2" width="2.46" height="35.3" fill="var(--up)"/>
<line x1="728.6" y1="239.0" x2="728.6" y2="289.2" stroke="var(--down)" class="wick"/>
<rect x="727.38" y="245.3" width="2.46" height="30.1" fill="var(--down)"/>
<line x1="732.6" y1="285.0" x2="732.6" y2="328.1" stroke="var(--down)" class="wick"/>
<rect x="731.35" y="296.7" width="2.46" height="18.4" fill="var(--down)"/>
<line x1="736.5" y1="290.9" x2="736.5" y2="344.0" stroke="var(--up)" class="wick"/>
<rect x="735.31" y="308.8" width="2.46" height="13.9" fill="var(--up)"/>
<line x1="740.5" y1="282.2" x2="740.5" y2="311.2" stroke="var(--up)" class="wick"/>
<rect x="739.28" y="295.8" width="2.46" height="2.3" fill="var(--up)"/>
<line x1="744.5" y1="276.3" x2="744.5" y2="311.0" stroke="var(--up)" class="wick"/>
<rect x="743.25" y="291.2" width="2.46" height="18.0" fill="var(--up)"/>
<line x1="748.4" y1="277.0" x2="748.4" y2="318.1" stroke="var(--down)" class="wick"/>
<rect x="747.22" y="284.7" width="2.46" height="30.0" fill="var(--down)"/>
<line x1="752.4" y1="313.6" x2="752.4" y2="392.9" stroke="var(--down)" class="wick"/>
<rect x="751.19" y="317.9" width="2.46" height="70.1" fill="var(--down)"/>
<line x1="756.4" y1="341.4" x2="756.4" y2="402.8" stroke="var(--up)" class="wick"/>
<rect x="755.15" y="353.7" width="2.46" height="18.4" fill="var(--up)"/>
<line x1="760.4" y1="334.1" x2="760.4" y2="394.3" stroke="var(--down)" class="wick"/>
<rect x="759.12" y="370.0" width="2.46" height="20.0" fill="var(--down)"/>
<line x1="764.3" y1="379.8" x2="764.3" y2="405.7" stroke="var(--down)" class="wick"/>
<rect x="763.09" y="386.7" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="768.3" y1="378.2" x2="768.3" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="385.9" width="2.46" height="6.2" fill="var(--down)"/>
<line x1="772.3" y1="378.0" x2="772.3" y2="415.2" stroke="var(--down)" class="wick"/>
<rect x="771.03" y="379.8" width="2.46" height="13.1" fill="var(--down)"/>
<line x1="776.2" y1="343.5" x2="776.2" y2="394.2" stroke="var(--up)" class="wick"/>
<rect x="774.99" y="374.5" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="780.2" y1="370.6" x2="780.2" y2="402.4" stroke="var(--down)" class="wick"/>
<rect x="778.96" y="385.8" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="784.2" y1="384.3" x2="784.2" y2="430.7" stroke="var(--down)" class="wick"/>
<rect x="782.93" y="389.7" width="2.46" height="6.2" fill="var(--down)"/>
<line x1="788.1" y1="367.9" x2="788.1" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="786.90" y="371.7" width="2.46" height="16.3" fill="var(--up)"/>
<line x1="792.1" y1="376.2" x2="792.1" y2="443.0" stroke="var(--down)" class="wick"/>
<rect x="790.87" y="383.8" width="2.46" height="56.7" fill="var(--down)"/>
<line x1="796.1" y1="395.0" x2="796.1" y2="440.2" stroke="var(--up)" class="wick"/>
<rect x="794.83" y="411.5" width="2.46" height="20.7" fill="var(--up)"/>
<line x1="800.0" y1="399.3" x2="800.0" y2="441.3" stroke="var(--down)" class="wick"/>
<rect x="798.80" y="411.1" width="2.46" height="20.8" fill="var(--down)"/>
<line x1="804.0" y1="425.2" x2="804.0" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="448.1" width="2.46" height="13.4" fill="var(--down)"/>
<line x1="808.0" y1="462.6" x2="808.0" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="806.74" y="484.0" width="2.46" height="15.1" fill="var(--down)"/>
<line x1="811.9" y1="479.8" x2="811.9" y2="509.0" stroke="var(--up)" class="wick"/>
<rect x="810.71" y="492.3" width="2.46" height="6.5" fill="var(--up)"/>
<line x1="815.9" y1="468.7" x2="815.9" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="814.67" y="484.7" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="819.9" y1="440.2" x2="819.9" y2="503.4" stroke="var(--down)" class="wick"/>
<rect x="818.64" y="452.0" width="2.46" height="38.1" fill="var(--down)"/>
<line x1="823.8" y1="459.4" x2="823.8" y2="503.4" stroke="var(--up)" class="wick"/>
<rect x="822.61" y="493.4" width="2.46" height="5.1" fill="var(--up)"/>
<line x1="827.8" y1="494.3" x2="827.8" y2="530.9" stroke="var(--down)" class="wick"/>
<rect x="826.58" y="507.5" width="2.46" height="3.4" fill="var(--down)"/>
<line x1="831.8" y1="459.9" x2="831.8" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="830.55" y="481.3" width="2.46" height="17.6" fill="var(--up)"/>
<line x1="835.7" y1="443.7" x2="835.7" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="834.51" y="459.6" width="2.46" height="5.2" fill="var(--up)"/>
<line x1="839.7" y1="444.4" x2="839.7" y2="470.2" stroke="var(--down)" class="wick"/>
<rect x="838.48" y="452.0" width="2.46" height="15.9" fill="var(--down)"/>
<line x1="843.7" y1="459.1" x2="843.7" y2="486.5" stroke="var(--up)" class="wick"/>
<rect x="842.45" y="460.3" width="2.46" height="6.6" fill="var(--up)"/>
<line x1="847.6" y1="425.2" x2="847.6" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="432.5" width="2.46" height="45.5" fill="var(--up)"/>
<line x1="851.6" y1="412.9" x2="851.6" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="850.39" y="423.8" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="855.6" y1="437.8" x2="855.6" y2="508.5" stroke="var(--down)" class="wick"/>
<rect x="854.35" y="442.9" width="2.46" height="55.2" fill="var(--down)"/>
<line x1="859.6" y1="482.0" x2="859.6" y2="505.8" stroke="var(--up)" class="wick"/>
<rect x="858.32" y="492.0" width="2.46" height="13.7" fill="var(--up)"/>
<line x1="863.5" y1="485.4" x2="863.5" y2="513.7" stroke="var(--down)" class="wick"/>
<rect x="862.29" y="502.4" width="2.46" height="8.0" fill="var(--down)"/>
<line x1="867.5" y1="468.7" x2="867.5" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="866.26" y="468.7" width="2.46" height="22.9" fill="var(--down)"/>
<line x1="871.5" y1="467.8" x2="871.5" y2="496.9" stroke="var(--up)" class="wick"/>
<rect x="870.23" y="488.5" width="2.46" height="3.5" fill="var(--up)"/>
<line x1="875.4" y1="476.8" x2="875.4" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="874.19" y="492.4" width="2.46" height="34.8" fill="var(--down)"/>
<line x1="879.4" y1="490.3" x2="879.4" y2="517.6" stroke="var(--up)" class="wick"/>
<rect x="878.16" y="500.9" width="2.46" height="12.2" fill="var(--up)"/>
<line x1="883.4" y1="487.1" x2="883.4" y2="555.2" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="492.7" width="2.46" height="46.3" fill="var(--down)"/>
<line x1="887.3" y1="532.5" x2="887.3" y2="591.7" stroke="var(--down)" class="wick"/>
<rect x="886.10" y="537.2" width="2.46" height="48.0" fill="var(--down)"/>
<line x1="891.3" y1="501.6" x2="891.3" y2="568.2" stroke="var(--up)" class="wick"/>
<rect x="890.07" y="504.1" width="2.46" height="55.6" fill="var(--up)"/>
<line x1="895.3" y1="453.7" x2="895.3" y2="490.0" stroke="var(--up)" class="wick"/>
<rect x="894.03" y="461.1" width="2.46" height="13.8" fill="var(--up)"/>
<line x1="899.2" y1="454.3" x2="899.2" y2="501.0" stroke="var(--down)" class="wick"/>
<rect x="898.00" y="460.8" width="2.46" height="13.4" fill="var(--down)"/>
<line x1="903.2" y1="393.2" x2="903.2" y2="456.5" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="422.1" width="2.46" height="28.3" fill="var(--down)"/>
<line x1="907.2" y1="436.0" x2="907.2" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="436.0" width="2.46" height="49.1" fill="var(--down)"/>
<line x1="911.1" y1="538.2" x2="911.1" y2="595.2" stroke="var(--up)" class="wick"/>
<rect x="909.91" y="550.6" width="2.46" height="10.8" fill="var(--up)"/>
<line x1="915.1" y1="549.2" x2="915.1" y2="586.5" stroke="var(--up)" class="wick"/>
<rect x="913.87" y="557.3" width="2.46" height="21.4" fill="var(--up)"/>
<line x1="919.1" y1="516.9" x2="919.1" y2="552.1" stroke="var(--up)" class="wick"/>
<rect x="917.84" y="541.7" width="2.46" height="6.6" fill="var(--up)"/>
<line x1="923.0" y1="537.5" x2="923.0" y2="585.0" stroke="var(--down)" class="wick"/>
<rect x="921.81" y="545.1" width="2.46" height="39.4" fill="var(--down)"/>
<line x1="927.0" y1="562.8" x2="927.0" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="925.78" y="585.2" width="2.46" height="4.4" fill="var(--up)"/>
<line x1="931.0" y1="525.8" x2="931.0" y2="569.7" stroke="var(--up)" class="wick"/>
<rect x="929.75" y="528.5" width="2.46" height="33.6" fill="var(--up)"/>
<line x1="934.9" y1="492.9" x2="934.9" y2="574.2" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="507.9" width="2.46" height="53.1" fill="var(--down)"/>
<line x1="938.9" y1="554.4" x2="938.9" y2="605.6" stroke="var(--down)" class="wick"/>
<rect x="937.68" y="554.6" width="2.46" height="29.7" fill="var(--down)"/>
<line x1="942.9" y1="585.5" x2="942.9" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="941.65" y="590.8" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="946.8" y1="571.7" x2="946.8" y2="594.8" stroke="var(--down)" class="wick"/>
<rect x="945.62" y="571.7" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="950.8" y1="586.0" x2="950.8" y2="608.7" stroke="var(--up)" class="wick"/>
<rect x="949.59" y="591.5" width="2.46" height="3.5" fill="var(--up)"/>
<line x1="954.8" y1="560.8" x2="954.8" y2="596.9" stroke="var(--up)" class="wick"/>
<rect x="953.55" y="567.7" width="2.46" height="15.6" fill="var(--up)"/>
<line x1="958.8" y1="516.1" x2="958.8" y2="562.5" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="523.4" width="2.46" height="38.3" fill="var(--up)"/>
<line x1="962.7" y1="444.0" x2="962.7" y2="495.3" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="475.3" width="2.46" height="4.9" fill="var(--down)"/>
<line x1="966.7" y1="446.8" x2="966.7" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="965.46" y="471.2" width="2.46" height="3.1" fill="var(--up)"/>
<line x1="970.7" y1="485.0" x2="970.7" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="969.43" y="505.0" width="2.46" height="12.7" fill="var(--down)"/>
<line x1="974.6" y1="518.2" x2="974.6" y2="543.2" stroke="var(--up)" class="wick"/>
<rect x="973.39" y="526.6" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="978.6" y1="498.6" x2="978.6" y2="538.6" stroke="var(--down)" class="wick"/>
<rect x="977.36" y="505.2" width="2.46" height="20.4" fill="var(--down)"/>
<line x1="982.6" y1="531.6" x2="982.6" y2="560.8" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="533.1" width="2.46" height="18.7" fill="var(--up)"/>
<line x1="986.5" y1="516.6" x2="986.5" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="517.2" width="2.46" height="20.4" fill="var(--down)"/>
<line x1="990.5" y1="513.1" x2="990.5" y2="560.7" stroke="var(--down)" class="wick"/>
<rect x="989.27" y="519.2" width="2.46" height="23.2" fill="var(--down)"/>
<line x1="994.5" y1="527.6" x2="994.5" y2="560.6" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="534.2" width="2.46" height="20.8" fill="var(--up)"/>
<line x1="998.4" y1="541.3" x2="998.4" y2="560.1" stroke="var(--down)" class="wick"/>
<rect x="997.20" y="541.3" width="2.46" height="11.1" fill="var(--down)"/>
<line x1="1002.4" y1="541.4" x2="1002.4" y2="564.1" stroke="var(--up)" class="wick"/>
<rect x="1001.17" y="542.8" width="2.46" height="19.7" fill="var(--up)"/>
<line x1="1006.4" y1="538.0" x2="1006.4" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="1005.14" y="538.7" width="2.46" height="16.6" fill="var(--up)"/>
<line x1="1010.3" y1="508.8" x2="1010.3" y2="529.9" stroke="var(--up)" class="wick"/>
<rect x="1009.11" y="511.7" width="2.46" height="17.0" fill="var(--up)"/>
<line x1="1014.3" y1="502.6" x2="1014.3" y2="518.8" stroke="var(--up)" class="wick"/>
<rect x="1013.07" y="509.3" width="2.46" height="2.4" fill="var(--up)"/>
<line x1="1018.3" y1="522.0" x2="1018.3" y2="553.4" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="524.5" width="2.46" height="20.7" fill="var(--down)"/>
<line x1="1022.2" y1="509.2" x2="1022.2" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="1021.01" y="515.4" width="2.46" height="3.2" fill="var(--down)"/>
<line x1="1026.2" y1="469.4" x2="1026.2" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="1024.98" y="484.1" width="2.46" height="24.1" fill="var(--up)"/>
<line x1="1030.2" y1="473.0" x2="1030.2" y2="504.8" stroke="var(--up)" class="wick"/>
<rect x="1028.95" y="491.2" width="2.46" height="4.8" fill="var(--up)"/>
<line x1="1034.1" y1="470.3" x2="1034.1" y2="497.4" stroke="var(--up)" class="wick"/>
<rect x="1032.91" y="471.5" width="2.46" height="11.4" fill="var(--up)"/>
<line x1="1038.1" y1="437.4" x2="1038.1" y2="458.8" stroke="var(--down)" class="wick"/>
<rect x="1036.88" y="451.3" width="2.46" height="3.4" fill="var(--down)"/>
<line x1="1042.1" y1="466.0" x2="1042.1" y2="491.2" stroke="var(--down)" class="wick"/>
<rect x="1040.85" y="467.9" width="2.46" height="20.5" fill="var(--down)"/>
<line x1="1046.0" y1="482.6" x2="1046.0" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="482.6" width="2.46" height="7.0" fill="var(--down)"/>
<line x1="1050.0" y1="505.1" x2="1050.0" y2="524.9" stroke="var(--down)" class="wick"/>
<rect x="1048.79" y="512.6" width="2.46" height="11.8" fill="var(--down)"/>
<line x1="60" y1="469.7" x2="1052" y2="469.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="473.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$144 R1</text>
<text x="1058" y="485.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="380.9" x2="1052" y2="380.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="384.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$150 R2</text>
<text x="1058" y="396.4" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="261.4" x2="1052" y2="261.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="264.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$158 R3</text>
<text x="1058" y="276.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="556.5" x2="1052" y2="556.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="550.5" font-size="11.5" fill="var(--support)" font-weight="600">$137 S1</text>
<text x="1058" y="562.5" font-size="9.5" fill="var(--muted)">터치 8회</text>
<circle cx="1052.0" cy="524.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="516.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $140 (2026-08-27)</text>
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
| R3 | $158 | 4 | 2025-10·2026-03~05 스윙 고점대. 2026년 3~5월 세 차례 되밀린 구간으로 1년 내 가장 여러 번 확인된 저항 |
| R2 | $150 | 5 | 2025-11~12 반등 고점과 2026-06~07 고점이 겹치는 구간. Elliott 합의 직후 상승이 멈춘 자리 |
| R1 | $144 | 3 | 2025-09 고점과 2026-07 중순 고점대. 7/28을 마지막으로 되밀렸다 |
| **현재가** | **$139.72** (2026-08-27 종가) | — | R1과 S1 사이 |
| S1 | $137 | 8 | 2025-09~10, 2026-01, 2026-06~08에 반복 확인된 1년 최다 터치 지지대. 현재가 바로 아래 |
| 참고선 | $133.73 | — | 52주 최저(2026년 중). 터치가 클러스터 기준에 못 미쳐 레벨로 잡히지 않았다 — 근시일 지지로 보지 않는다 |
| 참고선 | $171.48 | — | 52주 최고. 현재가 대비 22% 위라 근시일 저항으로 의미가 없다 |

> 유효한 클러스터가 저항 3개·지지 1개로 나와 **지지선은 S1 하나만** 표시했다(S2·S3에 해당하는 클러스터가 터치 2회 기준을 넘지 못했다). 현재가 $139.72는 S1($137)과 R1($144) 사이, S1 쪽에 가깝다.

---

## 3. 관측된 특이 구간 — 2026-07-09 FY2026 Q2 실적발표 갭다운

- FY2026 Q2 실적발표일. 순매출과 코어 EPS는 컨센서스를 소폭 웃돌았지만 유기적 성장률·마진이 기대에 못 미쳤고, 북미 식품(PFNA) 순매출이 −2%로 나온 것이 하락의 계기가 됐다([최근 뉴스 / 이슈](./08_news.md) 2026-07-09 항목).
- 종가 기준 전일 대비 **−3.3%** ($142.51 → $137.86), 거래량은 평소(일 773만 주 내외) 대비 약 **2.4배**인 **1,876만 주**.
- 이 갭다운 이후 주가는 $135~$145 박스로 내려앉았고, 그 이전의 $150선(R2)은 한 번도 회복하지 못했다. **7월 이전과 이후는 사실상 다른 가격대**이며, R2·R3는 갭 이전 구간에서 만들어진 레벨이라 근시일 저항으로는 R1($144)이 더 유효하다.

**참고 — 2025-12 Elliott 합의 구간**: 2025-12-08 Elliott와의 합의가 보도된 날 주가는 +0.4%($145.63)에 그쳤지만, 이틀 뒤인 **2025-12-10에 +3.5%($144.64 → $149.70), 거래량 1,853만 주(평균의 2.4배)**로 크게 올랐다. 그 이틀 사이 회사가 2026년 우선순위와 예비 전망을 별도로 발표한 것으로 보이나 **정확한 촉발 사건은 확인 필요**다. 이 반등이 만든 고점이 R2($150) 클러스터의 일부다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py` (`PEP --name "PepsiCo" --close-on 2026-08-27 --event 2025-12-08:"Elliott 합의 발표" --event 2026-07-09:"2026 Q2 실적발표"`)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간의 2026-07-09 갭다운 때문에 **R2·R3는 갭 이전 가격대에서 만들어진 레벨**이다 — 갭 이후 거래 레짐에서 같은 강도로 작동한다고 보기 어렵다.
    - 기간 내 주식분할·유상증자는 없었다. 다만 **원주가(배당 미반영)**이며 이 기간에 분기배당이 4회 지급됐으므로, 배당 재투자를 반영한 총수익 기준 차트와는 레벨이 다르다.

---

*작성일: 2026-08-30*
