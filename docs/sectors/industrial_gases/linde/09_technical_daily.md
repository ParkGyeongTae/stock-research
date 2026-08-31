# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 이 차트의 마지막 거래일은 **2026-08-27(종가 $485.35)**로, 핵심 지표·밸류에이션 / 적정주가가 기준으로 쓰는 **2026-08-28 종가 $489.51**보다 하루 이르다. 수집 시점(2026-08-31)에 Yahoo 일봉 피드에 08-28 봉이 아직 반영되지 않았기 때문이며, 두 값의 차이는 0.86%다. 같은 08-28 종가를 담은 주봉 차트([기술적 분석 — 주봉·5년](./10_technical_weekly.md))와는 값이 일치한다. **아래 레벨 표의 "현재가" 행만 하루 이른 값이라는 점을 감안해 읽을 것.**
    - 52주 최고 $548.20(2026-07-07 장중) 역시 핵심 지표·밸류에이션 문서에서 인용한 값과 일치한다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

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
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Linde(LIN) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Linde (LIN) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $485.35 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="568.2" x2="1052" y2="568.2" class="grid"/>
<text x="52" y="572.2" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="485.6" x2="1052" y2="485.6" class="grid"/>
<text x="52" y="489.6" font-size="11" text-anchor="end" fill="var(--muted)">425</text>
<line x1="60" y1="403.0" x2="1052" y2="403.0" class="grid"/>
<text x="52" y="407.0" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="320.3" x2="1052" y2="320.3" class="grid"/>
<text x="52" y="324.3" font-size="11" text-anchor="end" fill="var(--muted)">475</text>
<line x1="60" y1="237.7" x2="1052" y2="237.7" class="grid"/>
<text x="52" y="241.7" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="155.1" x2="1052" y2="155.1" class="grid"/>
<text x="52" y="159.1" font-size="11" text-anchor="end" fill="var(--muted)">525</text>
<line x1="60" y1="72.5" x2="1052" y2="72.5" class="grid"/>
<text x="52" y="76.5" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
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
<line x1="60" y1="78.5" x2="1052" y2="78.5" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="81.5" font-size="10.5" fill="var(--muted)">$548 52주 최고</text>
<line x1="974.6" y1="56.0" x2="974.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="980.6" y="68.0" font-size="10.5" fill="var(--down)">2026-07-31 Q2 실적발표 갭다운</text>
<line x1="62.0" y1="292.9" x2="62.0" y2="313.7" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="296.6" width="2.46" height="12.9" fill="var(--down)"/>
<line x1="66.0" y1="313.2" x2="66.0" y2="328.6" stroke="var(--down)" class="wick"/>
<rect x="64.72" y="313.2" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="69.9" y1="322.9" x2="69.9" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="68.69" y="330.9" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="73.9" y1="327.2" x2="73.9" y2="341.5" stroke="var(--up)" class="wick"/>
<rect x="72.66" y="329.0" width="2.46" height="5.4" fill="var(--up)"/>
<line x1="77.9" y1="320.2" x2="77.9" y2="348.1" stroke="var(--down)" class="wick"/>
<rect x="76.63" y="333.1" width="2.46" height="5.4" fill="var(--down)"/>
<line x1="81.8" y1="320.1" x2="81.8" y2="348.1" stroke="var(--up)" class="wick"/>
<rect x="80.59" y="321.6" width="2.46" height="16.4" fill="var(--up)"/>
<line x1="85.8" y1="321.9" x2="85.8" y2="335.6" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="325.5" width="2.46" height="1.1" fill="var(--up)"/>
<line x1="89.8" y1="320.6" x2="89.8" y2="338.6" stroke="var(--down)" class="wick"/>
<rect x="88.53" y="327.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="93.7" y1="289.2" x2="93.7" y2="328.7" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="292.0" width="2.46" height="35.3" fill="var(--up)"/>
<line x1="97.7" y1="290.9" x2="97.7" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="96.47" y="297.1" width="2.46" height="9.5" fill="var(--up)"/>
<line x1="101.7" y1="292.9" x2="101.7" y2="318.6" stroke="var(--down)" class="wick"/>
<rect x="100.43" y="299.3" width="2.46" height="15.4" fill="var(--down)"/>
<line x1="105.6" y1="309.0" x2="105.6" y2="333.9" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="315.6" width="2.46" height="16.4" fill="var(--down)"/>
<line x1="109.6" y1="299.3" x2="109.6" y2="330.2" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="304.3" width="2.46" height="19.7" fill="var(--up)"/>
<line x1="113.6" y1="304.0" x2="113.6" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="112.34" y="307.5" width="2.46" height="9.5" fill="var(--down)"/>
<line x1="117.5" y1="300.9" x2="117.5" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="116.31" y="307.1" width="2.46" height="5.0" fill="var(--up)"/>
<line x1="121.5" y1="308.2" x2="121.5" y2="322.7" stroke="var(--up)" class="wick"/>
<rect x="120.27" y="311.2" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="125.5" y1="294.0" x2="125.5" y2="321.5" stroke="var(--up)" class="wick"/>
<rect x="124.24" y="304.0" width="2.46" height="5.0" fill="var(--up)"/>
<line x1="129.4" y1="298.1" x2="129.4" y2="325.9" stroke="var(--down)" class="wick"/>
<rect x="128.21" y="305.1" width="2.46" height="18.1" fill="var(--down)"/>
<line x1="133.4" y1="315.9" x2="133.4" y2="337.2" stroke="var(--down)" class="wick"/>
<rect x="132.18" y="323.2" width="2.46" height="1.2" fill="var(--down)"/>
<line x1="137.4" y1="319.8" x2="137.4" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="322.3" width="2.46" height="5.6" fill="var(--up)"/>
<line x1="141.3" y1="314.7" x2="141.3" y2="332.2" stroke="var(--up)" class="wick"/>
<rect x="140.11" y="315.4" width="2.46" height="5.8" fill="var(--up)"/>
<line x1="145.3" y1="307.9" x2="145.3" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="320.3" width="2.46" height="4.3" fill="var(--up)"/>
<line x1="149.3" y1="320.1" x2="149.3" y2="367.3" stroke="var(--down)" class="wick"/>
<rect x="148.05" y="327.7" width="2.46" height="19.7" fill="var(--down)"/>
<line x1="153.2" y1="335.9" x2="153.2" y2="360.2" stroke="var(--up)" class="wick"/>
<rect x="152.02" y="338.6" width="2.46" height="20.0" fill="var(--up)"/>
<line x1="157.2" y1="338.8" x2="157.2" y2="360.0" stroke="var(--down)" class="wick"/>
<rect x="155.99" y="346.7" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="161.2" y1="335.0" x2="161.2" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="159.95" y="341.7" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="165.2" y1="335.0" x2="165.2" y2="350.5" stroke="var(--up)" class="wick"/>
<rect x="163.92" y="335.6" width="2.46" height="7.5" fill="var(--up)"/>
<line x1="169.1" y1="331.3" x2="169.1" y2="345.0" stroke="var(--down)" class="wick"/>
<rect x="167.89" y="335.8" width="2.46" height="8.2" fill="var(--down)"/>
<line x1="173.1" y1="336.9" x2="173.1" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="171.86" y="344.0" width="2.46" height="32.0" fill="var(--down)"/>
<line x1="177.1" y1="359.9" x2="177.1" y2="393.3" stroke="var(--down)" class="wick"/>
<rect x="175.83" y="376.3" width="2.46" height="14.0" fill="var(--down)"/>
<line x1="181.0" y1="370.6" x2="181.0" y2="386.4" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="381.0" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="185.0" y1="363.1" x2="185.0" y2="392.8" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="372.4" width="2.46" height="19.8" fill="var(--up)"/>
<line x1="189.0" y1="364.9" x2="189.0" y2="400.3" stroke="var(--down)" class="wick"/>
<rect x="187.73" y="373.1" width="2.46" height="25.1" fill="var(--down)"/>
<line x1="192.9" y1="394.8" x2="192.9" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="191.70" y="396.2" width="2.46" height="25.8" fill="var(--down)"/>
<line x1="196.9" y1="398.6" x2="196.9" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="195.67" y="400.0" width="2.46" height="22.1" fill="var(--up)"/>
<line x1="200.9" y1="385.6" x2="200.9" y2="403.9" stroke="var(--down)" class="wick"/>
<rect x="199.63" y="395.2" width="2.46" height="2.6" fill="var(--down)"/>
<line x1="204.8" y1="394.9" x2="204.8" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="203.60" y="401.1" width="2.46" height="1.6" fill="var(--down)"/>
<line x1="208.8" y1="386.2" x2="208.8" y2="410.4" stroke="var(--down)" class="wick"/>
<rect x="207.57" y="401.9" width="2.46" height="1.4" fill="var(--down)"/>
<line x1="212.8" y1="394.1" x2="212.8" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="211.54" y="394.4" width="2.46" height="8.3" fill="var(--down)"/>
<line x1="216.7" y1="401.6" x2="216.7" y2="417.5" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="404.5" width="2.46" height="11.7" fill="var(--down)"/>
<line x1="220.7" y1="402.5" x2="220.7" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="219.47" y="410.7" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="224.7" y1="412.1" x2="224.7" y2="429.4" stroke="var(--down)" class="wick"/>
<rect x="223.44" y="417.9" width="2.46" height="9.1" fill="var(--down)"/>
<line x1="228.6" y1="437.9" x2="228.6" y2="465.0" stroke="var(--down)" class="wick"/>
<rect x="227.41" y="440.0" width="2.46" height="22.4" fill="var(--down)"/>
<line x1="232.6" y1="451.9" x2="232.6" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="231.38" y="460.9" width="2.46" height="8.4" fill="var(--down)"/>
<line x1="236.6" y1="480.9" x2="236.6" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="235.35" y="485.6" width="2.46" height="22.1" fill="var(--down)"/>
<line x1="240.5" y1="494.7" x2="240.5" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="239.31" y="494.7" width="2.46" height="33.3" fill="var(--down)"/>
<line x1="244.5" y1="497.7" x2="244.5" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="243.28" y="508.9" width="2.46" height="5.8" fill="var(--up)"/>
<line x1="248.5" y1="502.8" x2="248.5" y2="518.6" stroke="var(--up)" class="wick"/>
<rect x="247.25" y="507.9" width="2.46" height="6.4" fill="var(--up)"/>
<line x1="252.4" y1="503.8" x2="252.4" y2="523.3" stroke="var(--down)" class="wick"/>
<rect x="251.22" y="514.1" width="2.46" height="3.4" fill="var(--down)"/>
<line x1="256.4" y1="492.8" x2="256.4" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="500.4" width="2.46" height="11.6" fill="var(--up)"/>
<line x1="260.4" y1="494.9" x2="260.4" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="259.15" y="499.9" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="264.4" y1="474.3" x2="264.4" y2="495.7" stroke="var(--up)" class="wick"/>
<rect x="263.12" y="480.1" width="2.46" height="3.0" fill="var(--up)"/>
<line x1="268.3" y1="463.9" x2="268.3" y2="485.9" stroke="var(--up)" class="wick"/>
<rect x="267.09" y="472.5" width="2.46" height="3.2" fill="var(--up)"/>
<line x1="272.3" y1="472.3" x2="272.3" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="271.06" y="473.5" width="2.46" height="4.8" fill="var(--up)"/>
<line x1="276.3" y1="468.7" x2="276.3" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="275.03" y="473.5" width="2.46" height="17.3" fill="var(--down)"/>
<line x1="280.2" y1="490.9" x2="280.2" y2="510.1" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="496.8" width="2.46" height="12.4" fill="var(--down)"/>
<line x1="284.2" y1="504.1" x2="284.2" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="282.96" y="506.3" width="2.46" height="13.3" fill="var(--down)"/>
<line x1="288.2" y1="515.1" x2="288.2" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="286.93" y="519.5" width="2.46" height="5.1" fill="var(--down)"/>
<line x1="292.1" y1="515.5" x2="292.1" y2="541.0" stroke="var(--down)" class="wick"/>
<rect x="290.90" y="519.9" width="2.46" height="20.1" fill="var(--down)"/>
<line x1="296.1" y1="513.9" x2="296.1" y2="547.0" stroke="var(--up)" class="wick"/>
<rect x="294.87" y="526.1" width="2.46" height="17.7" fill="var(--up)"/>
<line x1="300.1" y1="527.0" x2="300.1" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="298.83" y="534.3" width="2.46" height="8.5" fill="var(--down)"/>
<line x1="304.0" y1="525.6" x2="304.0" y2="548.1" stroke="var(--down)" class="wick"/>
<rect x="302.80" y="529.6" width="2.46" height="12.6" fill="var(--down)"/>
<line x1="308.0" y1="533.5" x2="308.0" y2="544.9" stroke="var(--up)" class="wick"/>
<rect x="306.77" y="542.1" width="2.46" height="1.3" fill="var(--up)"/>
<line x1="312.0" y1="529.9" x2="312.0" y2="546.8" stroke="var(--up)" class="wick"/>
<rect x="310.74" y="534.1" width="2.46" height="8.3" fill="var(--up)"/>
<line x1="315.9" y1="529.9" x2="315.9" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="314.71" y="535.1" width="2.46" height="9.5" fill="var(--down)"/>
<line x1="319.9" y1="530.8" x2="319.9" y2="554.1" stroke="var(--up)" class="wick"/>
<rect x="318.67" y="539.1" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="323.9" y1="531.8" x2="323.9" y2="548.3" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="537.9" width="2.46" height="2.7" fill="var(--up)"/>
<line x1="327.8" y1="539.3" x2="327.8" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="326.61" y="543.0" width="2.46" height="12.8" fill="var(--down)"/>
<line x1="331.8" y1="552.9" x2="331.8" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="555.1" width="2.46" height="14.5" fill="var(--down)"/>
<line x1="335.8" y1="570.1" x2="335.8" y2="608.6" stroke="var(--down)" class="wick"/>
<rect x="334.55" y="572.3" width="2.46" height="31.0" fill="var(--down)"/>
<line x1="339.7" y1="578.6" x2="339.7" y2="600.9" stroke="var(--down)" class="wick"/>
<rect x="338.51" y="597.2" width="2.46" height="2.7" fill="var(--down)"/>
<line x1="343.7" y1="586.8" x2="343.7" y2="604.5" stroke="var(--up)" class="wick"/>
<rect x="342.48" y="592.4" width="2.46" height="10.1" fill="var(--up)"/>
<line x1="347.7" y1="554.0" x2="347.7" y2="585.1" stroke="var(--up)" class="wick"/>
<rect x="346.45" y="557.3" width="2.46" height="26.6" fill="var(--up)"/>
<line x1="351.6" y1="508.6" x2="351.6" y2="545.9" stroke="var(--up)" class="wick"/>
<rect x="350.42" y="514.5" width="2.46" height="31.4" fill="var(--up)"/>
<line x1="355.6" y1="497.1" x2="355.6" y2="535.1" stroke="var(--down)" class="wick"/>
<rect x="354.39" y="510.6" width="2.46" height="1.5" fill="var(--down)"/>
<line x1="359.6" y1="487.4" x2="359.6" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="358.35" y="490.5" width="2.46" height="16.5" fill="var(--up)"/>
<line x1="363.6" y1="487.5" x2="363.6" y2="499.5" stroke="var(--down)" class="wick"/>
<rect x="362.32" y="492.2" width="2.46" height="2.2" fill="var(--down)"/>
<line x1="367.5" y1="487.3" x2="367.5" y2="507.1" stroke="var(--down)" class="wick"/>
<rect x="366.29" y="497.0" width="2.46" height="8.4" fill="var(--down)"/>
<line x1="371.5" y1="490.9" x2="371.5" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="370.26" y="497.4" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="375.5" y1="484.6" x2="375.5" y2="500.3" stroke="var(--up)" class="wick"/>
<rect x="374.23" y="490.5" width="2.46" height="6.4" fill="var(--up)"/>
<line x1="379.4" y1="484.5" x2="379.4" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="378.19" y="485.2" width="2.46" height="5.0" fill="var(--up)"/>
<line x1="383.4" y1="480.2" x2="383.4" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="382.16" y="485.9" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="387.4" y1="482.3" x2="387.4" y2="490.8" stroke="var(--down)" class="wick"/>
<rect x="386.13" y="484.2" width="2.46" height="2.1" fill="var(--down)"/>
<line x1="391.3" y1="478.0" x2="391.3" y2="489.7" stroke="var(--up)" class="wick"/>
<rect x="390.10" y="480.5" width="2.46" height="8.9" fill="var(--up)"/>
<line x1="395.3" y1="470.8" x2="395.3" y2="490.9" stroke="var(--up)" class="wick"/>
<rect x="394.07" y="474.5" width="2.46" height="14.4" fill="var(--up)"/>
<line x1="399.3" y1="472.3" x2="399.3" y2="481.3" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="478.6" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="403.2" y1="466.4" x2="403.2" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="402.00" y="472.0" width="2.46" height="9.4" fill="var(--up)"/>
<line x1="407.2" y1="455.9" x2="407.2" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="405.97" y="458.8" width="2.46" height="24.7" fill="var(--up)"/>
<line x1="411.2" y1="439.3" x2="411.2" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="409.94" y="445.4" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="415.1" y1="439.2" x2="415.1" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="413.91" y="446.2" width="2.46" height="9.2" fill="var(--down)"/>
<line x1="419.1" y1="428.0" x2="419.1" y2="461.1" stroke="var(--up)" class="wick"/>
<rect x="417.87" y="437.0" width="2.46" height="20.7" fill="var(--up)"/>
<line x1="423.1" y1="419.3" x2="423.1" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="422.5" width="2.46" height="20.7" fill="var(--up)"/>
<line x1="427.0" y1="416.2" x2="427.0" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="425.81" y="424.0" width="2.46" height="4.1" fill="var(--up)"/>
<line x1="431.0" y1="420.6" x2="431.0" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="429.78" y="422.9" width="2.46" height="3.5" fill="var(--down)"/>
<line x1="435.0" y1="421.6" x2="435.0" y2="442.9" stroke="var(--down)" class="wick"/>
<rect x="433.75" y="430.0" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="438.9" y1="422.8" x2="438.9" y2="443.5" stroke="var(--down)" class="wick"/>
<rect x="437.71" y="430.1" width="2.46" height="5.7" fill="var(--down)"/>
<line x1="442.9" y1="434.2" x2="442.9" y2="450.3" stroke="var(--down)" class="wick"/>
<rect x="441.68" y="437.8" width="2.46" height="1.7" fill="var(--down)"/>
<line x1="446.9" y1="452.8" x2="446.9" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="445.65" y="454.8" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="450.8" y1="432.9" x2="450.8" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="449.62" y="438.1" width="2.46" height="19.4" fill="var(--up)"/>
<line x1="454.8" y1="411.9" x2="454.8" y2="436.5" stroke="var(--up)" class="wick"/>
<rect x="453.59" y="417.4" width="2.46" height="19.1" fill="var(--up)"/>
<line x1="458.8" y1="396.4" x2="458.8" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="457.55" y="397.8" width="2.46" height="27.5" fill="var(--up)"/>
<line x1="462.8" y1="384.5" x2="462.8" y2="395.9" stroke="var(--up)" class="wick"/>
<rect x="461.52" y="386.3" width="2.46" height="7.9" fill="var(--up)"/>
<line x1="466.7" y1="379.8" x2="466.7" y2="394.9" stroke="var(--down)" class="wick"/>
<rect x="465.49" y="386.3" width="2.46" height="6.6" fill="var(--down)"/>
<line x1="470.7" y1="391.4" x2="470.7" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="469.46" y="394.1" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="474.7" y1="383.0" x2="474.7" y2="409.0" stroke="var(--up)" class="wick"/>
<rect x="473.43" y="386.4" width="2.46" height="6.9" fill="var(--up)"/>
<line x1="478.6" y1="378.6" x2="478.6" y2="397.7" stroke="var(--up)" class="wick"/>
<rect x="477.39" y="379.9" width="2.46" height="14.3" fill="var(--up)"/>
<line x1="482.6" y1="362.1" x2="482.6" y2="376.5" stroke="var(--up)" class="wick"/>
<rect x="481.36" y="369.4" width="2.46" height="2.7" fill="var(--up)"/>
<line x1="486.6" y1="347.4" x2="486.6" y2="375.6" stroke="var(--up)" class="wick"/>
<rect x="485.33" y="358.1" width="2.46" height="17.1" fill="var(--up)"/>
<line x1="490.5" y1="312.6" x2="490.5" y2="351.3" stroke="var(--up)" class="wick"/>
<rect x="489.30" y="325.9" width="2.46" height="23.5" fill="var(--up)"/>
<line x1="494.5" y1="322.4" x2="494.5" y2="372.4" stroke="var(--down)" class="wick"/>
<rect x="493.27" y="333.3" width="2.46" height="37.6" fill="var(--down)"/>
<line x1="498.5" y1="376.6" x2="498.5" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="497.23" y="383.5" width="2.46" height="25.3" fill="var(--down)"/>
<line x1="502.4" y1="378.2" x2="502.4" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="501.20" y="382.0" width="2.46" height="27.0" fill="var(--up)"/>
<line x1="506.4" y1="356.2" x2="506.4" y2="389.1" stroke="var(--up)" class="wick"/>
<rect x="505.17" y="368.2" width="2.46" height="20.5" fill="var(--up)"/>
<line x1="510.4" y1="344.6" x2="510.4" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="509.14" y="345.1" width="2.46" height="30.0" fill="var(--up)"/>
<line x1="514.3" y1="311.9" x2="514.3" y2="338.6" stroke="var(--up)" class="wick"/>
<rect x="513.11" y="327.4" width="2.46" height="9.7" fill="var(--up)"/>
<line x1="518.3" y1="275.6" x2="518.3" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="517.07" y="300.5" width="2.46" height="22.6" fill="var(--up)"/>
<line x1="522.3" y1="291.4" x2="522.3" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="521.04" y="296.5" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="526.2" y1="276.5" x2="526.2" y2="295.2" stroke="var(--up)" class="wick"/>
<rect x="525.01" y="286.4" width="2.46" height="8.1" fill="var(--up)"/>
<line x1="530.2" y1="269.0" x2="530.2" y2="296.6" stroke="var(--up)" class="wick"/>
<rect x="528.98" y="270.4" width="2.46" height="17.2" fill="var(--up)"/>
<line x1="534.2" y1="243.2" x2="534.2" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="532.95" y="249.3" width="2.46" height="27.3" fill="var(--up)"/>
<line x1="538.1" y1="235.9" x2="538.1" y2="261.6" stroke="var(--up)" class="wick"/>
<rect x="536.91" y="243.7" width="2.46" height="15.3" fill="var(--up)"/>
<line x1="542.1" y1="222.9" x2="542.1" y2="255.7" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="224.5" width="2.46" height="20.3" fill="var(--up)"/>
<line x1="546.1" y1="206.0" x2="546.1" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="544.85" y="210.4" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="550.0" y1="202.5" x2="550.0" y2="246.2" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="215.0" width="2.46" height="27.7" fill="var(--down)"/>
<line x1="554.0" y1="206.2" x2="554.0" y2="243.5" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="211.0" width="2.46" height="32.4" fill="var(--up)"/>
<line x1="558.0" y1="204.5" x2="558.0" y2="239.3" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="206.9" width="2.46" height="4.4" fill="var(--up)"/>
<line x1="562.0" y1="225.7" x2="562.0" y2="265.5" stroke="var(--up)" class="wick"/>
<rect x="560.72" y="232.2" width="2.46" height="5.6" fill="var(--up)"/>
<line x1="565.9" y1="224.6" x2="565.9" y2="246.5" stroke="var(--down)" class="wick"/>
<rect x="564.69" y="230.4" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="569.9" y1="246.8" x2="569.9" y2="275.6" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="252.3" width="2.46" height="18.3" fill="var(--down)"/>
<line x1="573.9" y1="276.4" x2="573.9" y2="304.9" stroke="var(--down)" class="wick"/>
<rect x="572.63" y="277.4" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="577.8" y1="282.2" x2="577.8" y2="307.7" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="291.9" width="2.46" height="3.2" fill="var(--up)"/>
<line x1="581.8" y1="293.8" x2="581.8" y2="321.6" stroke="var(--down)" class="wick"/>
<rect x="580.56" y="301.2" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="585.8" y1="297.1" x2="585.8" y2="333.1" stroke="var(--up)" class="wick"/>
<rect x="584.53" y="298.7" width="2.46" height="14.5" fill="var(--up)"/>
<line x1="589.7" y1="261.5" x2="589.7" y2="312.0" stroke="var(--up)" class="wick"/>
<rect x="588.50" y="269.4" width="2.46" height="33.1" fill="var(--up)"/>
<line x1="593.7" y1="237.7" x2="593.7" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="592.47" y="244.3" width="2.46" height="13.5" fill="var(--down)"/>
<line x1="597.7" y1="242.8" x2="597.7" y2="267.8" stroke="var(--up)" class="wick"/>
<rect x="596.43" y="246.3" width="2.46" height="10.3" fill="var(--up)"/>
<line x1="601.6" y1="236.6" x2="601.6" y2="260.1" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="246.3" width="2.46" height="11.1" fill="var(--down)"/>
<line x1="605.6" y1="256.0" x2="605.6" y2="276.1" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="266.0" width="2.46" height="9.5" fill="var(--down)"/>
<line x1="609.6" y1="264.9" x2="609.6" y2="292.4" stroke="var(--up)" class="wick"/>
<rect x="608.34" y="271.4" width="2.46" height="3.7" fill="var(--up)"/>
<line x1="613.5" y1="251.6" x2="613.5" y2="289.5" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="261.2" width="2.46" height="15.7" fill="var(--down)"/>
<line x1="617.5" y1="269.9" x2="617.5" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="274.5" width="2.46" height="35.7" fill="var(--down)"/>
<line x1="621.5" y1="281.2" x2="621.5" y2="325.5" stroke="var(--up)" class="wick"/>
<rect x="620.24" y="304.4" width="2.46" height="19.5" fill="var(--up)"/>
<line x1="625.4" y1="262.8" x2="625.4" y2="297.4" stroke="var(--up)" class="wick"/>
<rect x="624.21" y="263.1" width="2.46" height="30.4" fill="var(--up)"/>
<line x1="629.4" y1="236.7" x2="629.4" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="628.18" y="252.6" width="2.46" height="14.0" fill="var(--up)"/>
<line x1="633.4" y1="243.5" x2="633.4" y2="282.6" stroke="var(--down)" class="wick"/>
<rect x="632.15" y="245.6" width="2.46" height="21.4" fill="var(--down)"/>
<line x1="637.3" y1="225.7" x2="637.3" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="636.11" y="240.2" width="2.46" height="11.3" fill="var(--up)"/>
<line x1="641.3" y1="236.8" x2="641.3" y2="264.5" stroke="var(--down)" class="wick"/>
<rect x="640.08" y="250.5" width="2.46" height="1.3" fill="var(--down)"/>
<line x1="645.3" y1="256.1" x2="645.3" y2="275.8" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="258.1" width="2.46" height="3.3" fill="var(--up)"/>
<line x1="649.2" y1="228.8" x2="649.2" y2="256.3" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="229.1" width="2.46" height="8.6" fill="var(--up)"/>
<line x1="653.2" y1="225.6" x2="653.2" y2="246.8" stroke="var(--down)" class="wick"/>
<rect x="651.99" y="225.6" width="2.46" height="13.8" fill="var(--down)"/>
<line x1="657.2" y1="236.1" x2="657.2" y2="270.2" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="238.4" width="2.46" height="17.2" fill="var(--down)"/>
<line x1="661.2" y1="234.9" x2="661.2" y2="294.7" stroke="var(--up)" class="wick"/>
<rect x="659.92" y="236.2" width="2.46" height="41.2" fill="var(--up)"/>
<line x1="665.1" y1="214.0" x2="665.1" y2="245.9" stroke="var(--up)" class="wick"/>
<rect x="663.89" y="226.8" width="2.46" height="12.7" fill="var(--up)"/>
<line x1="669.1" y1="216.8" x2="669.1" y2="238.6" stroke="var(--down)" class="wick"/>
<rect x="667.86" y="218.1" width="2.46" height="9.3" fill="var(--down)"/>
<line x1="673.1" y1="207.2" x2="673.1" y2="228.5" stroke="var(--up)" class="wick"/>
<rect x="671.83" y="208.4" width="2.46" height="17.4" fill="var(--up)"/>
<line x1="677.0" y1="226.6" x2="677.0" y2="255.4" stroke="var(--down)" class="wick"/>
<rect x="675.79" y="229.5" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="681.0" y1="238.9" x2="681.0" y2="267.8" stroke="var(--up)" class="wick"/>
<rect x="679.76" y="244.5" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="685.0" y1="235.4" x2="685.0" y2="254.1" stroke="var(--up)" class="wick"/>
<rect x="683.73" y="240.3" width="2.46" height="8.0" fill="var(--up)"/>
<line x1="688.9" y1="244.5" x2="688.9" y2="277.4" stroke="var(--down)" class="wick"/>
<rect x="687.70" y="249.1" width="2.46" height="14.3" fill="var(--down)"/>
<line x1="692.9" y1="233.2" x2="692.9" y2="262.5" stroke="var(--up)" class="wick"/>
<rect x="691.67" y="243.9" width="2.46" height="11.6" fill="var(--up)"/>
<line x1="696.9" y1="244.3" x2="696.9" y2="263.1" stroke="var(--down)" class="wick"/>
<rect x="695.63" y="252.4" width="2.46" height="2.4" fill="var(--down)"/>
<line x1="700.8" y1="233.7" x2="700.8" y2="257.8" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="249.4" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="704.8" y1="210.4" x2="704.8" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="703.57" y="211.1" width="2.46" height="29.8" fill="var(--up)"/>
<line x1="708.8" y1="202.5" x2="708.8" y2="231.9" stroke="var(--up)" class="wick"/>
<rect x="707.54" y="203.7" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="712.7" y1="194.9" x2="712.7" y2="216.2" stroke="var(--up)" class="wick"/>
<rect x="711.51" y="202.2" width="2.46" height="1.6" fill="var(--up)"/>
<line x1="716.7" y1="186.1" x2="716.7" y2="208.0" stroke="var(--down)" class="wick"/>
<rect x="715.47" y="194.8" width="2.46" height="9.0" fill="var(--down)"/>
<line x1="720.7" y1="208.0" x2="720.7" y2="226.3" stroke="var(--down)" class="wick"/>
<rect x="719.44" y="210.6" width="2.46" height="11.5" fill="var(--down)"/>
<line x1="724.6" y1="212.5" x2="724.6" y2="238.9" stroke="var(--down)" class="wick"/>
<rect x="723.41" y="231.2" width="2.46" height="2.8" fill="var(--down)"/>
<line x1="728.6" y1="167.4" x2="728.6" y2="231.1" stroke="var(--up)" class="wick"/>
<rect x="727.38" y="211.6" width="2.46" height="15.1" fill="var(--up)"/>
<line x1="732.6" y1="216.9" x2="732.6" y2="262.5" stroke="var(--down)" class="wick"/>
<rect x="731.35" y="225.9" width="2.46" height="33.1" fill="var(--down)"/>
<line x1="736.5" y1="227.1" x2="736.5" y2="269.5" stroke="var(--up)" class="wick"/>
<rect x="735.31" y="236.8" width="2.46" height="18.8" fill="var(--up)"/>
<line x1="740.5" y1="220.7" x2="740.5" y2="247.4" stroke="var(--up)" class="wick"/>
<rect x="739.28" y="231.6" width="2.46" height="14.3" fill="var(--up)"/>
<line x1="744.5" y1="225.4" x2="744.5" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="743.25" y="234.7" width="2.46" height="23.4" fill="var(--down)"/>
<line x1="748.4" y1="245.7" x2="748.4" y2="263.3" stroke="var(--down)" class="wick"/>
<rect x="747.22" y="257.6" width="2.46" height="2.8" fill="var(--down)"/>
<line x1="752.4" y1="217.2" x2="752.4" y2="258.1" stroke="var(--up)" class="wick"/>
<rect x="751.19" y="223.2" width="2.46" height="34.7" fill="var(--up)"/>
<line x1="756.4" y1="218.6" x2="756.4" y2="248.5" stroke="var(--down)" class="wick"/>
<rect x="755.15" y="223.9" width="2.46" height="1.1" fill="var(--down)"/>
<line x1="760.4" y1="185.7" x2="760.4" y2="225.6" stroke="var(--up)" class="wick"/>
<rect x="759.12" y="193.9" width="2.46" height="29.9" fill="var(--up)"/>
<line x1="764.3" y1="188.9" x2="764.3" y2="210.3" stroke="var(--down)" class="wick"/>
<rect x="763.09" y="191.3" width="2.46" height="7.9" fill="var(--down)"/>
<line x1="768.3" y1="181.5" x2="768.3" y2="224.1" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="182.3" width="2.46" height="35.2" fill="var(--down)"/>
<line x1="772.3" y1="191.0" x2="772.3" y2="222.4" stroke="var(--up)" class="wick"/>
<rect x="771.03" y="201.9" width="2.46" height="14.7" fill="var(--up)"/>
<line x1="776.2" y1="203.5" x2="776.2" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="774.99" y="209.0" width="2.46" height="8.7" fill="var(--down)"/>
<line x1="780.2" y1="196.8" x2="780.2" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="778.96" y="215.8" width="2.46" height="20.9" fill="var(--up)"/>
<line x1="784.2" y1="183.1" x2="784.2" y2="218.7" stroke="var(--up)" class="wick"/>
<rect x="782.93" y="189.8" width="2.46" height="16.7" fill="var(--up)"/>
<line x1="788.1" y1="167.6" x2="788.1" y2="188.2" stroke="var(--up)" class="wick"/>
<rect x="786.90" y="179.6" width="2.46" height="1.9" fill="var(--up)"/>
<line x1="792.1" y1="174.7" x2="792.1" y2="195.8" stroke="var(--down)" class="wick"/>
<rect x="790.87" y="178.8" width="2.46" height="9.5" fill="var(--down)"/>
<line x1="796.1" y1="185.4" x2="796.1" y2="212.3" stroke="var(--down)" class="wick"/>
<rect x="794.83" y="194.8" width="2.46" height="16.9" fill="var(--down)"/>
<line x1="800.0" y1="210.5" x2="800.0" y2="242.4" stroke="var(--down)" class="wick"/>
<rect x="798.80" y="211.8" width="2.46" height="19.4" fill="var(--down)"/>
<line x1="804.0" y1="229.4" x2="804.0" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="237.7" width="2.46" height="7.6" fill="var(--down)"/>
<line x1="808.0" y1="243.2" x2="808.0" y2="274.5" stroke="var(--up)" class="wick"/>
<rect x="806.74" y="246.3" width="2.46" height="4.2" fill="var(--up)"/>
<line x1="811.9" y1="238.4" x2="811.9" y2="269.3" stroke="var(--up)" class="wick"/>
<rect x="810.71" y="251.3" width="2.46" height="8.1" fill="var(--up)"/>
<line x1="815.9" y1="197.4" x2="815.9" y2="250.5" stroke="var(--up)" class="wick"/>
<rect x="814.67" y="212.7" width="2.46" height="31.1" fill="var(--up)"/>
<line x1="819.9" y1="197.6" x2="819.9" y2="222.8" stroke="var(--down)" class="wick"/>
<rect x="818.64" y="209.3" width="2.46" height="3.8" fill="var(--down)"/>
<line x1="823.8" y1="179.5" x2="823.8" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="822.61" y="197.1" width="2.46" height="14.5" fill="var(--down)"/>
<line x1="827.8" y1="203.8" x2="827.8" y2="237.9" stroke="var(--down)" class="wick"/>
<rect x="826.58" y="214.2" width="2.46" height="17.2" fill="var(--down)"/>
<line x1="831.8" y1="181.3" x2="831.8" y2="216.7" stroke="var(--up)" class="wick"/>
<rect x="830.55" y="186.2" width="2.46" height="25.2" fill="var(--up)"/>
<line x1="835.7" y1="162.1" x2="835.7" y2="221.3" stroke="var(--down)" class="wick"/>
<rect x="834.51" y="164.2" width="2.46" height="43.3" fill="var(--down)"/>
<line x1="839.7" y1="176.3" x2="839.7" y2="198.1" stroke="var(--up)" class="wick"/>
<rect x="838.48" y="186.7" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="843.7" y1="152.4" x2="843.7" y2="180.9" stroke="var(--up)" class="wick"/>
<rect x="842.45" y="159.9" width="2.46" height="17.1" fill="var(--up)"/>
<line x1="847.6" y1="152.3" x2="847.6" y2="179.0" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="166.8" width="2.46" height="8.0" fill="var(--up)"/>
<line x1="851.6" y1="159.6" x2="851.6" y2="192.9" stroke="var(--down)" class="wick"/>
<rect x="850.39" y="169.8" width="2.46" height="7.9" fill="var(--down)"/>
<line x1="855.6" y1="173.0" x2="855.6" y2="200.0" stroke="var(--up)" class="wick"/>
<rect x="854.35" y="185.4" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="859.6" y1="175.5" x2="859.6" y2="200.9" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="184.7" width="2.46" height="12.9" fill="var(--down)"/>
<line x1="863.5" y1="178.3" x2="863.5" y2="214.2" stroke="var(--up)" class="wick"/>
<rect x="862.29" y="182.5" width="2.46" height="28.9" fill="var(--up)"/>
<line x1="867.5" y1="158.8" x2="867.5" y2="208.9" stroke="var(--down)" class="wick"/>
<rect x="866.26" y="158.8" width="2.46" height="38.4" fill="var(--down)"/>
<line x1="871.5" y1="162.8" x2="871.5" y2="190.2" stroke="var(--up)" class="wick"/>
<rect x="870.23" y="185.8" width="2.46" height="3.2" fill="var(--up)"/>
<line x1="875.4" y1="145.4" x2="875.4" y2="192.1" stroke="var(--up)" class="wick"/>
<rect x="874.19" y="164.1" width="2.46" height="23.1" fill="var(--up)"/>
<line x1="879.4" y1="155.1" x2="879.4" y2="177.1" stroke="var(--down)" class="wick"/>
<rect x="878.16" y="168.3" width="2.46" height="4.6" fill="var(--down)"/>
<line x1="883.4" y1="172.7" x2="883.4" y2="215.3" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="174.6" width="2.46" height="26.6" fill="var(--down)"/>
<line x1="887.3" y1="163.1" x2="887.3" y2="199.5" stroke="var(--up)" class="wick"/>
<rect x="886.10" y="175.2" width="2.46" height="21.7" fill="var(--up)"/>
<line x1="891.3" y1="109.0" x2="891.3" y2="181.6" stroke="var(--up)" class="wick"/>
<rect x="890.07" y="126.9" width="2.46" height="27.2" fill="var(--up)"/>
<line x1="895.3" y1="81.7" x2="895.3" y2="128.8" stroke="var(--up)" class="wick"/>
<rect x="894.03" y="83.6" width="2.46" height="37.0" fill="var(--up)"/>
<line x1="899.2" y1="92.0" x2="899.2" y2="134.6" stroke="var(--down)" class="wick"/>
<rect x="898.00" y="93.3" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="903.2" y1="78.5" x2="903.2" y2="120.9" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="82.5" width="2.46" height="28.9" fill="var(--down)"/>
<line x1="907.2" y1="115.3" x2="907.2" y2="151.2" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="118.4" width="2.46" height="27.9" fill="var(--down)"/>
<line x1="911.1" y1="145.7" x2="911.1" y2="174.9" stroke="var(--down)" class="wick"/>
<rect x="909.91" y="151.8" width="2.46" height="1.5" fill="var(--down)"/>
<line x1="915.1" y1="129.7" x2="915.1" y2="160.2" stroke="var(--up)" class="wick"/>
<rect x="913.87" y="139.3" width="2.46" height="15.6" fill="var(--up)"/>
<line x1="919.1" y1="130.5" x2="919.1" y2="166.8" stroke="var(--down)" class="wick"/>
<rect x="917.84" y="135.6" width="2.46" height="22.7" fill="var(--down)"/>
<line x1="923.0" y1="133.3" x2="923.0" y2="168.3" stroke="var(--down)" class="wick"/>
<rect x="921.81" y="157.1" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="927.0" y1="168.0" x2="927.0" y2="193.5" stroke="var(--down)" class="wick"/>
<rect x="925.78" y="176.1" width="2.46" height="14.8" fill="var(--down)"/>
<line x1="931.0" y1="164.5" x2="931.0" y2="202.5" stroke="var(--up)" class="wick"/>
<rect x="929.75" y="169.2" width="2.46" height="24.8" fill="var(--up)"/>
<line x1="934.9" y1="147.0" x2="934.9" y2="199.1" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="164.4" width="2.46" height="29.6" fill="var(--down)"/>
<line x1="938.9" y1="183.2" x2="938.9" y2="201.6" stroke="var(--down)" class="wick"/>
<rect x="937.68" y="192.9" width="2.46" height="5.1" fill="var(--down)"/>
<line x1="942.9" y1="195.3" x2="942.9" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="941.65" y="198.4" width="2.46" height="22.7" fill="var(--down)"/>
<line x1="946.8" y1="201.5" x2="946.8" y2="220.9" stroke="var(--up)" class="wick"/>
<rect x="945.62" y="209.1" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="950.8" y1="201.7" x2="950.8" y2="230.8" stroke="var(--up)" class="wick"/>
<rect x="949.59" y="216.9" width="2.46" height="8.1" fill="var(--up)"/>
<line x1="954.8" y1="195.0" x2="954.8" y2="221.6" stroke="var(--up)" class="wick"/>
<rect x="953.55" y="197.2" width="2.46" height="22.6" fill="var(--up)"/>
<line x1="958.8" y1="188.2" x2="958.8" y2="216.4" stroke="var(--down)" class="wick"/>
<rect x="957.52" y="193.7" width="2.46" height="20.9" fill="var(--down)"/>
<line x1="962.7" y1="165.0" x2="962.7" y2="204.7" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="197.9" width="2.46" height="2.9" fill="var(--down)"/>
<line x1="966.7" y1="192.6" x2="966.7" y2="220.8" stroke="var(--down)" class="wick"/>
<rect x="965.46" y="198.8" width="2.46" height="2.0" fill="var(--down)"/>
<line x1="970.7" y1="188.9" x2="970.7" y2="229.1" stroke="var(--down)" class="wick"/>
<rect x="969.43" y="203.3" width="2.46" height="5.9" fill="var(--down)"/>
<line x1="974.6" y1="290.8" x2="974.6" y2="347.2" stroke="var(--up)" class="wick"/>
<rect x="973.39" y="309.2" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="978.6" y1="287.3" x2="978.6" y2="315.7" stroke="var(--down)" class="wick"/>
<rect x="977.36" y="293.7" width="2.46" height="8.6" fill="var(--down)"/>
<line x1="982.6" y1="285.3" x2="982.6" y2="308.8" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="288.5" width="2.46" height="8.8" fill="var(--up)"/>
<line x1="986.5" y1="255.2" x2="986.5" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="985.30" y="267.3" width="2.46" height="2.0" fill="var(--up)"/>
<line x1="990.5" y1="240.4" x2="990.5" y2="272.9" stroke="var(--down)" class="wick"/>
<rect x="989.27" y="244.6" width="2.46" height="25.8" fill="var(--down)"/>
<line x1="994.5" y1="260.7" x2="994.5" y2="283.3" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="270.8" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="998.4" y1="262.3" x2="998.4" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="997.20" y="262.7" width="2.46" height="10.5" fill="var(--up)"/>
<line x1="1002.4" y1="251.1" x2="1002.4" y2="270.8" stroke="var(--down)" class="wick"/>
<rect x="1001.17" y="267.3" width="2.46" height="1.7" fill="var(--down)"/>
<line x1="1006.4" y1="269.7" x2="1006.4" y2="308.0" stroke="var(--down)" class="wick"/>
<rect x="1005.14" y="277.9" width="2.46" height="27.8" fill="var(--down)"/>
<line x1="1010.3" y1="293.0" x2="1010.3" y2="317.9" stroke="var(--down)" class="wick"/>
<rect x="1009.11" y="304.3" width="2.46" height="5.5" fill="var(--down)"/>
<line x1="1014.3" y1="292.3" x2="1014.3" y2="313.3" stroke="var(--up)" class="wick"/>
<rect x="1013.07" y="294.8" width="2.46" height="12.1" fill="var(--up)"/>
<line x1="1018.3" y1="296.0" x2="1018.3" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="297.2" width="2.46" height="25.3" fill="var(--down)"/>
<line x1="1022.2" y1="292.3" x2="1022.2" y2="311.4" stroke="var(--down)" class="wick"/>
<rect x="1021.01" y="298.3" width="2.46" height="9.8" fill="var(--down)"/>
<line x1="1026.2" y1="290.7" x2="1026.2" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="1024.98" y="300.1" width="2.46" height="8.7" fill="var(--up)"/>
<line x1="1030.2" y1="271.4" x2="1030.2" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="1028.95" y="299.6" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="1034.1" y1="264.9" x2="1034.1" y2="295.7" stroke="var(--up)" class="wick"/>
<rect x="1032.91" y="278.8" width="2.46" height="4.0" fill="var(--up)"/>
<line x1="1038.1" y1="265.9" x2="1038.1" y2="287.3" stroke="var(--up)" class="wick"/>
<rect x="1036.88" y="270.7" width="2.46" height="5.3" fill="var(--up)"/>
<line x1="1042.1" y1="268.7" x2="1042.1" y2="286.9" stroke="var(--down)" class="wick"/>
<rect x="1040.85" y="273.4" width="2.46" height="6.6" fill="var(--down)"/>
<line x1="1046.0" y1="255.9" x2="1046.0" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="1044.82" y="269.7" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="1050.0" y1="281.7" x2="1050.0" y2="300.5" stroke="var(--up)" class="wick"/>
<rect x="1048.79" y="286.1" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="60" y1="215.5" x2="1052" y2="215.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="219.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$507 R1</text>
<text x="1058" y="231.0" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="163.1" x2="1052" y2="163.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="166.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$523 R2</text>
<text x="1058" y="178.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="340.0" x2="1052" y2="340.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="334.0" font-size="11.5" fill="var(--support)" font-weight="600">$469 S1</text>
<text x="1058" y="346.0" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="427.8" x2="1052" y2="427.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="421.8" font-size="11.5" fill="var(--support)" font-weight="600">$442 S2</text>
<text x="1058" y="433.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="483.5" x2="1052" y2="483.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="477.5" font-size="11.5" fill="var(--support)" font-weight="600">$426 S3</text>
<text x="1058" y="489.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="286.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="278.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $485 (2026-08-27)</text>
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
| R2 | $523 | 4 | 2026-05-01·05-22·06-15·07-28의 스윙 고점대 — 사상 최고($548) 직전 5~7월 상승 구간의 중간 저항 |
| R1 | $507 | 3 | 2026-02-26·03-17·04-13의 스윙 고점대. 아래 3. 관측된 특이 구간의 갭다운 직전 종가($508.64)도 이 대역이라, 현재는 갭 상단으로도 기능한다 |
| **현재가** | **$485.35** (2026-08-27 종가) | — | R1과 S1 사이 |
| S1 | $469 | 5 | 2025-10-01·2026-03-11·03-24·07-31·08-17 — 1년 내내 반복 확인된 최다 터치 대역. 실적 갭다운 당일(2026-07-31) 장중 저가($466.88)도 여기서 멈췄다 |
| S2 | $442 | 2 | 2025-10-16·2026-02-09의 스윙 저점대 |
| S3 | $426 | 2 | 2026-01-02·01-20의 스윙 저점대 — 2025년 말 종가($426.39)와 겹치는 연초 시작 가격대 |
| 참고선 | $548 | — | 52주 최고(2026-07-07 장중). 스윙 클러스터가 아니라 단일 고점이라 근시일 저항으로 보지 않는다 — 현재가보다 11.4% 위다 |

---

## 3. 관측된 특이 구간 — 2026-07-31 Q2 실적 발표 갭다운

- 계기는 [Q2 2026 실적 발표](./08_news.md)다. 매출·Adjusted EPS는 컨센서스를 상회했지만 Adjusted 영업이익률 60bp 하락, 미국 홈케어(Lincare) 전략적 검토, CapEx 가이던스 상향이 겹쳤다.
- 종가 기준 전일 대비 **−5.95%**($508.64 → $478.38), 장중 저가는 $466.88까지 밀렸다. 거래량은 평소(일 240만 주 내외) 대비 약 **2.2배**인 **522만 주**로 1년 중 최대였다.
- 이 하루로 가격대가 재설정됐다. 갭다운 이전 6주간 $505~$540에서 거래되던 흐름이 끊기고, 이후 한 달간은 $478~$492의 좁은 범위에서만 움직였다. 그래서 갭 위쪽의 R2($523)는 최근 한 달의 거래와 접점이 없는 대역이며, 갭 아래 S1($469)이 갭다운 당일 저가와 8월 중순 저점을 모두 잡아낸 실질적 지지로 기능하고 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-31. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py LIN --name "Linde" --close-on 2026-08-28 --event 2026-07-31:"Q2 실적발표 갭다운" --ref-line 548.20:"52주 최고" --emit all` (재현용 — `--close-on`을 2026-08-28로 줬으나 피드의 마지막 봉이 2026-08-27이라 차트도 그 날짜로 끝난다)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간의 갭다운으로 $492~$505 구간에 거래가 거의 없는 공백이 생겼다. R1($507)과 현재가 사이의 이 공백 때문에 가격이 위로 움직일 때는 저항 없이 빠르게 통과하고, 되돌릴 때는 지지 없이 밀릴 수 있다 — 레벨 간 간격을 균질하게 읽지 말 것.
    - 이 기간 중 주식분할·대규모 유상증자는 없었다. 다만 원주가라 기간 내 배당 4회(주당 총 $6.20)는 반영되지 않았으므로, 총수익 관점의 가격 흐름과는 그만큼 차이가 난다.

---

*작성일: 2026-08-31*
