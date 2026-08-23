# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, Yahoo Finance 일봉 API에서 직접 수집했다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). **겹치는 시점의 종가 대조**: 2026-08-14 종가 $482.74는 핵심 지표 A.2·밸류에이션 / 적정주가에서 인용한 stockanalysis.com 기준값($482.74)과 정확히 일치한다. 52주 최고 $548.20 역시 두 문서에서 동일하게 인용한 값과 일치.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $482.74 (2026-08-14) · 단위 USD</text>
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
<line x1="105.5" y1="626.0" x2="105.5" y2="631.0" class="axis"/>
<text x="105.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="188.4" y1="626.0" x2="188.4" y2="631.0" class="axis"/>
<text x="188.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="279.3" y1="626.0" x2="279.3" y2="631.0" class="axis"/>
<text x="279.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="354.4" y1="626.0" x2="354.4" y2="631.0" class="axis"/>
<text x="354.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="441.4" y1="626.0" x2="441.4" y2="631.0" class="axis"/>
<text x="441.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="520.4" y1="626.0" x2="520.4" y2="631.0" class="axis"/>
<text x="520.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="595.5" y1="626.0" x2="595.5" y2="631.0" class="axis"/>
<text x="595.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="682.5" y1="626.0" x2="682.5" y2="631.0" class="axis"/>
<text x="682.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="765.5" y1="626.0" x2="765.5" y2="631.0" class="axis"/>
<text x="765.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="844.5" y1="626.0" x2="844.5" y2="631.0" class="axis"/>
<text x="844.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="927.5" y1="626.0" x2="927.5" y2="631.0" class="axis"/>
<text x="927.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="1014.5" y1="626.0" x2="1014.5" y2="631.0" class="axis"/>
<text x="1014.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="78.5" x2="1052" y2="78.5" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="81.5" font-size="10.5" fill="var(--muted)">$548 52주 최고</text>
<line x1="1010.5" y1="56.0" x2="1010.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="1016.5" y="68.0" font-size="10.5" fill="var(--down)">2026-07-31 Q2 실적발표(가이던스·CapEx 우려로 급락)</text>
<line x1="62.0" y1="295.0" x2="62.0" y2="308.5" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="300.9" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="65.9" y1="300.4" x2="65.9" y2="313.2" stroke="var(--down)" class="wick"/>
<rect x="64.70" y="302.4" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="69.9" y1="294.5" x2="69.9" y2="315.2" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="304.1" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="73.8" y1="282.7" x2="73.8" y2="302.2" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="294.6" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="77.8" y1="294.2" x2="77.8" y2="303.7" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="299.2" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="81.7" y1="284.9" x2="81.7" y2="304.9" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="290.4" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="85.7" y1="290.6" x2="85.7" y2="314.8" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="297.5" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="89.6" y1="296.9" x2="89.6" y2="320.3" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="297.5" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="93.6" y1="291.2" x2="93.6" y2="305.9" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="294.9" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="97.5" y1="293.9" x2="97.5" y2="306.7" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="295.4" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="101.5" y1="292.9" x2="101.5" y2="313.7" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="296.6" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="105.5" y1="313.2" x2="105.5" y2="328.6" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="313.2" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="109.4" y1="322.9" x2="109.4" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="330.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="113.4" y1="327.2" x2="113.4" y2="341.5" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="329.0" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="117.3" y1="320.2" x2="117.3" y2="348.1" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="333.1" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="121.3" y1="320.1" x2="121.3" y2="348.1" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="321.6" width="2.45" height="16.4" fill="var(--up)"/>
<line x1="125.2" y1="321.9" x2="125.2" y2="335.6" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="325.5" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="129.2" y1="320.6" x2="129.2" y2="338.6" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="327.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="133.1" y1="289.2" x2="133.1" y2="328.7" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="292.0" width="2.45" height="35.3" fill="var(--up)"/>
<line x1="137.1" y1="290.9" x2="137.1" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="297.1" width="2.45" height="9.5" fill="var(--up)"/>
<line x1="141.0" y1="292.9" x2="141.0" y2="318.6" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="299.3" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="145.0" y1="309.0" x2="145.0" y2="333.9" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="315.6" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="148.9" y1="299.3" x2="148.9" y2="330.2" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="304.3" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="152.9" y1="304.0" x2="152.9" y2="332.6" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="307.5" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="156.8" y1="300.9" x2="156.8" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="307.1" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="160.8" y1="308.2" x2="160.8" y2="322.7" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="311.2" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="164.7" y1="294.0" x2="164.7" y2="321.5" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="304.0" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="168.7" y1="298.1" x2="168.7" y2="325.9" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="305.1" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="172.6" y1="315.9" x2="172.6" y2="337.2" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="323.2" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="176.6" y1="319.8" x2="176.6" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="322.3" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="180.5" y1="314.7" x2="180.5" y2="332.2" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="315.4" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="184.5" y1="307.9" x2="184.5" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="320.3" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="188.4" y1="320.1" x2="188.4" y2="367.3" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="327.7" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="192.4" y1="335.9" x2="192.4" y2="360.2" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="338.6" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="196.4" y1="338.8" x2="196.4" y2="360.0" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="346.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="200.3" y1="335.0" x2="200.3" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="341.7" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="204.3" y1="335.0" x2="204.3" y2="350.5" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="335.6" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="208.2" y1="331.3" x2="208.2" y2="345.0" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="335.8" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="212.2" y1="336.9" x2="212.2" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="344.0" width="2.45" height="32.0" fill="var(--down)"/>
<line x1="216.1" y1="359.9" x2="216.1" y2="393.3" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="376.3" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="220.1" y1="370.6" x2="220.1" y2="386.4" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="381.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="224.0" y1="363.1" x2="224.0" y2="392.8" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="372.4" width="2.45" height="19.8" fill="var(--up)"/>
<line x1="228.0" y1="364.9" x2="228.0" y2="400.3" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="373.1" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="231.9" y1="394.8" x2="231.9" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="396.2" width="2.45" height="25.8" fill="var(--down)"/>
<line x1="235.9" y1="398.6" x2="235.9" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="400.0" width="2.45" height="22.1" fill="var(--up)"/>
<line x1="239.8" y1="385.6" x2="239.8" y2="403.9" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="395.2" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="243.8" y1="394.9" x2="243.8" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="401.1" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="247.7" y1="386.2" x2="247.7" y2="410.4" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="401.9" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="251.7" y1="394.1" x2="251.7" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="394.4" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="255.6" y1="401.6" x2="255.6" y2="417.5" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="404.5" width="2.45" height="11.7" fill="var(--down)"/>
<line x1="259.6" y1="402.5" x2="259.6" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="410.7" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="263.5" y1="412.1" x2="263.5" y2="429.4" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="417.9" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="267.5" y1="437.9" x2="267.5" y2="465.0" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="440.0" width="2.45" height="22.4" fill="var(--down)"/>
<line x1="271.4" y1="451.9" x2="271.4" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="460.9" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="275.4" y1="480.9" x2="275.4" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="485.6" width="2.45" height="22.1" fill="var(--down)"/>
<line x1="279.3" y1="494.7" x2="279.3" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="494.7" width="2.45" height="33.3" fill="var(--down)"/>
<line x1="283.3" y1="497.7" x2="283.3" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="508.9" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="287.3" y1="502.8" x2="287.3" y2="518.6" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="507.9" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="291.2" y1="503.8" x2="291.2" y2="523.3" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="514.1" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="295.2" y1="492.8" x2="295.2" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="500.4" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="299.1" y1="494.9" x2="299.1" y2="515.6" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="499.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="303.1" y1="474.3" x2="303.1" y2="495.7" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="480.1" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="307.0" y1="463.9" x2="307.0" y2="485.9" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="472.5" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="311.0" y1="472.3" x2="311.0" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="473.5" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="314.9" y1="468.7" x2="314.9" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="313.69" y="473.5" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="318.9" y1="490.9" x2="318.9" y2="510.1" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="496.8" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="322.8" y1="504.1" x2="322.8" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="506.3" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="326.8" y1="515.1" x2="326.8" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="519.5" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="330.7" y1="515.5" x2="330.7" y2="541.0" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="519.9" width="2.45" height="20.1" fill="var(--down)"/>
<line x1="334.7" y1="513.9" x2="334.7" y2="547.0" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="526.1" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="338.6" y1="527.0" x2="338.6" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="534.3" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="342.6" y1="525.6" x2="342.6" y2="548.1" stroke="var(--down)" class="wick"/>
<rect x="341.36" y="529.6" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="346.5" y1="533.5" x2="346.5" y2="544.9" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="542.1" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="350.5" y1="529.9" x2="350.5" y2="546.8" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="534.1" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="354.4" y1="529.9" x2="354.4" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="535.1" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="358.4" y1="530.8" x2="358.4" y2="554.1" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="539.1" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="362.3" y1="531.8" x2="362.3" y2="548.3" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="537.9" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="366.3" y1="539.3" x2="366.3" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="543.0" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="370.2" y1="552.9" x2="370.2" y2="571.7" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="555.1" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="374.2" y1="570.1" x2="374.2" y2="608.6" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="572.3" width="2.45" height="31.0" fill="var(--down)"/>
<line x1="378.2" y1="578.6" x2="378.2" y2="600.9" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="597.2" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="382.1" y1="586.8" x2="382.1" y2="604.5" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="592.4" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="386.1" y1="554.0" x2="386.1" y2="585.1" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="557.3" width="2.45" height="26.6" fill="var(--up)"/>
<line x1="390.0" y1="508.6" x2="390.0" y2="545.9" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="514.5" width="2.45" height="31.4" fill="var(--up)"/>
<line x1="394.0" y1="497.1" x2="394.0" y2="535.1" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="510.6" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="397.9" y1="487.4" x2="397.9" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="490.5" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="401.9" y1="487.5" x2="401.9" y2="499.5" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="492.2" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="405.8" y1="487.3" x2="405.8" y2="507.1" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="497.0" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="409.8" y1="490.9" x2="409.8" y2="511.4" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="497.4" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="413.7" y1="484.6" x2="413.7" y2="500.3" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="490.5" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="417.7" y1="484.5" x2="417.7" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="485.2" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="421.6" y1="480.2" x2="421.6" y2="488.4" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="485.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="425.6" y1="482.3" x2="425.6" y2="490.8" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="484.2" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="429.5" y1="478.0" x2="429.5" y2="489.7" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="480.5" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="433.5" y1="470.8" x2="433.5" y2="490.9" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="474.5" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="437.4" y1="472.3" x2="437.4" y2="481.3" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="478.6" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="441.4" y1="466.4" x2="441.4" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="472.0" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="445.3" y1="455.9" x2="445.3" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="458.8" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="449.3" y1="439.3" x2="449.3" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="445.4" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="453.2" y1="439.2" x2="453.2" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="446.2" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="457.2" y1="428.0" x2="457.2" y2="461.1" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="437.0" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="461.1" y1="419.3" x2="461.1" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="422.5" width="2.45" height="20.7" fill="var(--up)"/>
<line x1="465.1" y1="416.2" x2="465.1" y2="438.0" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="424.0" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="469.1" y1="420.6" x2="469.1" y2="435.7" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="422.9" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="473.0" y1="421.6" x2="473.0" y2="442.9" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="430.0" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="477.0" y1="422.8" x2="477.0" y2="443.5" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="430.1" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="480.9" y1="434.2" x2="480.9" y2="450.3" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="437.8" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="484.9" y1="452.8" x2="484.9" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="454.8" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="488.8" y1="432.9" x2="488.8" y2="459.0" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="438.1" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="492.8" y1="411.9" x2="492.8" y2="436.5" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="417.4" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="496.7" y1="396.4" x2="496.7" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="397.8" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="500.7" y1="384.5" x2="500.7" y2="395.9" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="386.3" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="504.6" y1="379.8" x2="504.6" y2="394.9" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="386.3" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="508.6" y1="391.4" x2="508.6" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="394.1" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="512.5" y1="383.0" x2="512.5" y2="409.0" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="386.4" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="516.5" y1="378.6" x2="516.5" y2="397.7" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="379.9" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="520.4" y1="362.1" x2="520.4" y2="376.5" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="369.4" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="524.4" y1="347.4" x2="524.4" y2="375.6" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="358.1" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="528.3" y1="312.6" x2="528.3" y2="351.3" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="325.9" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="532.3" y1="322.4" x2="532.3" y2="372.4" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="333.3" width="2.45" height="37.6" fill="var(--down)"/>
<line x1="536.2" y1="376.6" x2="536.2" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="383.5" width="2.45" height="25.3" fill="var(--down)"/>
<line x1="540.2" y1="378.2" x2="540.2" y2="422.7" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="382.0" width="2.45" height="27.0" fill="var(--up)"/>
<line x1="544.1" y1="356.2" x2="544.1" y2="389.1" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="368.2" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="548.1" y1="344.6" x2="548.1" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="345.1" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="552.0" y1="311.9" x2="552.0" y2="338.6" stroke="var(--up)" class="wick"/>
<rect x="550.82" y="327.4" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="556.0" y1="275.6" x2="556.0" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="300.5" width="2.45" height="22.6" fill="var(--up)"/>
<line x1="560.0" y1="291.4" x2="560.0" y2="310.4" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="296.5" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="563.9" y1="276.5" x2="563.9" y2="295.2" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="286.4" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="567.9" y1="269.0" x2="567.9" y2="296.6" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="270.4" width="2.45" height="17.2" fill="var(--up)"/>
<line x1="571.8" y1="243.2" x2="571.8" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="249.3" width="2.45" height="27.3" fill="var(--up)"/>
<line x1="575.8" y1="235.9" x2="575.8" y2="261.6" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="243.7" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="579.7" y1="222.9" x2="579.7" y2="255.7" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="224.5" width="2.45" height="20.3" fill="var(--up)"/>
<line x1="583.7" y1="206.0" x2="583.7" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="210.4" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="587.6" y1="202.5" x2="587.6" y2="246.2" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="215.0" width="2.45" height="27.7" fill="var(--down)"/>
<line x1="591.6" y1="206.2" x2="591.6" y2="243.5" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="211.0" width="2.45" height="32.4" fill="var(--up)"/>
<line x1="595.5" y1="204.5" x2="595.5" y2="239.3" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="206.9" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="599.5" y1="225.7" x2="599.5" y2="265.5" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="232.2" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="603.4" y1="224.6" x2="603.4" y2="246.5" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="230.4" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="607.4" y1="246.8" x2="607.4" y2="275.6" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="252.3" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="611.3" y1="276.4" x2="611.3" y2="304.9" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="277.4" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="615.3" y1="282.2" x2="615.3" y2="307.7" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="291.9" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="619.2" y1="293.8" x2="619.2" y2="321.6" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="301.2" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="623.2" y1="297.1" x2="623.2" y2="333.1" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="298.7" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="627.1" y1="261.5" x2="627.1" y2="312.0" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="269.4" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="631.1" y1="237.7" x2="631.1" y2="262.1" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="244.3" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="635.0" y1="242.8" x2="635.0" y2="267.8" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="246.3" width="2.45" height="10.3" fill="var(--up)"/>
<line x1="639.0" y1="236.6" x2="639.0" y2="260.1" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="246.3" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="642.9" y1="256.0" x2="642.9" y2="276.1" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="266.0" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="646.9" y1="264.9" x2="646.9" y2="292.4" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="271.4" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="650.9" y1="251.6" x2="650.9" y2="289.5" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="261.2" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="654.8" y1="269.9" x2="654.8" y2="312.6" stroke="var(--down)" class="wick"/>
<rect x="653.58" y="274.5" width="2.45" height="35.7" fill="var(--down)"/>
<line x1="658.8" y1="281.2" x2="658.8" y2="325.5" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="304.4" width="2.45" height="19.5" fill="var(--up)"/>
<line x1="662.7" y1="262.8" x2="662.7" y2="297.4" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="263.1" width="2.45" height="30.4" fill="var(--up)"/>
<line x1="666.7" y1="236.7" x2="666.7" y2="267.0" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="252.6" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="670.6" y1="243.5" x2="670.6" y2="282.6" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="245.6" width="2.45" height="21.4" fill="var(--down)"/>
<line x1="674.6" y1="225.7" x2="674.6" y2="254.8" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="240.2" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="678.5" y1="236.8" x2="678.5" y2="264.5" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="250.5" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="682.5" y1="256.1" x2="682.5" y2="275.8" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="258.1" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="686.4" y1="228.8" x2="686.4" y2="256.3" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="229.1" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="690.4" y1="225.6" x2="690.4" y2="246.8" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="225.6" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="694.3" y1="236.1" x2="694.3" y2="270.2" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="238.4" width="2.45" height="17.2" fill="var(--down)"/>
<line x1="698.3" y1="234.9" x2="698.3" y2="294.7" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="236.2" width="2.45" height="41.2" fill="var(--up)"/>
<line x1="702.2" y1="214.0" x2="702.2" y2="245.9" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="226.8" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="706.2" y1="216.8" x2="706.2" y2="238.6" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="218.1" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="710.1" y1="207.2" x2="710.1" y2="228.5" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="208.4" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="714.1" y1="226.6" x2="714.1" y2="255.4" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="229.5" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="718.0" y1="238.9" x2="718.0" y2="267.8" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="244.5" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="722.0" y1="235.4" x2="722.0" y2="254.1" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="240.3" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="725.9" y1="244.5" x2="725.9" y2="277.4" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="249.1" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="729.9" y1="233.2" x2="729.9" y2="262.5" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="243.9" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="733.8" y1="244.3" x2="733.8" y2="263.1" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="252.4" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="737.8" y1="233.7" x2="737.8" y2="257.8" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="249.4" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="741.8" y1="210.4" x2="741.8" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="211.1" width="2.45" height="29.8" fill="var(--up)"/>
<line x1="745.7" y1="202.5" x2="745.7" y2="231.9" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="203.7" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="749.7" y1="194.9" x2="749.7" y2="216.2" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="202.2" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="753.6" y1="186.1" x2="753.6" y2="208.0" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="194.8" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="757.6" y1="208.0" x2="757.6" y2="226.3" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="210.6" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="761.5" y1="212.5" x2="761.5" y2="238.9" stroke="var(--down)" class="wick"/>
<rect x="760.29" y="231.2" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="765.5" y1="167.4" x2="765.5" y2="231.1" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="211.6" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="769.4" y1="216.9" x2="769.4" y2="262.5" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="225.9" width="2.45" height="33.1" fill="var(--down)"/>
<line x1="773.4" y1="227.1" x2="773.4" y2="269.5" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="236.8" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="777.3" y1="220.7" x2="777.3" y2="247.4" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="231.6" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="781.3" y1="225.4" x2="781.3" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="234.7" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="785.2" y1="245.7" x2="785.2" y2="263.3" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="257.6" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="789.2" y1="217.2" x2="789.2" y2="258.1" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="223.2" width="2.45" height="34.7" fill="var(--up)"/>
<line x1="793.1" y1="218.6" x2="793.1" y2="248.5" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="223.9" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="797.1" y1="185.7" x2="797.1" y2="225.6" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="193.9" width="2.45" height="29.9" fill="var(--up)"/>
<line x1="801.0" y1="188.9" x2="801.0" y2="210.3" stroke="var(--down)" class="wick"/>
<rect x="799.81" y="191.3" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="805.0" y1="181.5" x2="805.0" y2="224.1" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="182.3" width="2.45" height="35.2" fill="var(--down)"/>
<line x1="808.9" y1="191.0" x2="808.9" y2="222.4" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="201.9" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="812.9" y1="203.5" x2="812.9" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="209.0" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="816.8" y1="196.8" x2="816.8" y2="237.8" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="215.8" width="2.45" height="20.9" fill="var(--up)"/>
<line x1="820.8" y1="183.1" x2="820.8" y2="218.7" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="189.8" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="824.7" y1="167.6" x2="824.7" y2="188.2" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="179.6" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="828.7" y1="174.7" x2="828.7" y2="195.8" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="178.8" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="832.7" y1="185.4" x2="832.7" y2="212.3" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="194.8" width="2.45" height="16.9" fill="var(--down)"/>
<line x1="836.6" y1="210.5" x2="836.6" y2="242.4" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="211.8" width="2.45" height="19.4" fill="var(--down)"/>
<line x1="840.6" y1="229.4" x2="840.6" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="237.7" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="844.5" y1="243.2" x2="844.5" y2="274.5" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="246.3" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="848.5" y1="238.4" x2="848.5" y2="269.3" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="251.3" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="852.4" y1="197.4" x2="852.4" y2="250.5" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="212.7" width="2.45" height="31.1" fill="var(--up)"/>
<line x1="856.4" y1="197.6" x2="856.4" y2="222.8" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="209.3" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="860.3" y1="179.5" x2="860.3" y2="214.5" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="197.1" width="2.45" height="14.5" fill="var(--down)"/>
<line x1="864.3" y1="203.8" x2="864.3" y2="237.9" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="214.2" width="2.45" height="17.2" fill="var(--down)"/>
<line x1="868.2" y1="181.3" x2="868.2" y2="216.7" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="186.2" width="2.45" height="25.2" fill="var(--up)"/>
<line x1="872.2" y1="162.1" x2="872.2" y2="221.3" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="164.2" width="2.45" height="43.3" fill="var(--down)"/>
<line x1="876.1" y1="176.3" x2="876.1" y2="198.1" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="186.7" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="880.1" y1="152.4" x2="880.1" y2="180.9" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="159.9" width="2.45" height="17.1" fill="var(--up)"/>
<line x1="884.0" y1="152.3" x2="884.0" y2="179.0" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="166.8" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="888.0" y1="159.6" x2="888.0" y2="192.9" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="169.8" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="891.9" y1="173.0" x2="891.9" y2="200.0" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="185.4" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="895.9" y1="175.5" x2="895.9" y2="200.9" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="184.7" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="899.8" y1="178.3" x2="899.8" y2="214.2" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="182.5" width="2.45" height="28.9" fill="var(--up)"/>
<line x1="903.8" y1="158.8" x2="903.8" y2="208.9" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="158.8" width="2.45" height="38.4" fill="var(--down)"/>
<line x1="907.7" y1="162.8" x2="907.7" y2="190.2" stroke="var(--up)" class="wick"/>
<rect x="906.52" y="185.8" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="911.7" y1="145.4" x2="911.7" y2="192.1" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="164.1" width="2.45" height="23.1" fill="var(--up)"/>
<line x1="915.6" y1="155.1" x2="915.6" y2="177.1" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="168.3" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="919.6" y1="172.7" x2="919.6" y2="215.3" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="174.6" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="923.6" y1="163.1" x2="923.6" y2="199.5" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="175.2" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="927.5" y1="109.0" x2="927.5" y2="181.6" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="126.9" width="2.45" height="27.2" fill="var(--up)"/>
<line x1="931.5" y1="81.7" x2="931.5" y2="128.8" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="83.6" width="2.45" height="37.0" fill="var(--up)"/>
<line x1="935.4" y1="92.0" x2="935.4" y2="134.6" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="93.3" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="939.4" y1="78.5" x2="939.4" y2="120.9" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="82.5" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="943.3" y1="115.3" x2="943.3" y2="151.2" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="118.4" width="2.45" height="27.9" fill="var(--down)"/>
<line x1="947.3" y1="145.7" x2="947.3" y2="174.9" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="151.8" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="951.2" y1="129.7" x2="951.2" y2="160.2" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="139.3" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="955.2" y1="130.5" x2="955.2" y2="166.8" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="135.6" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="959.1" y1="133.3" x2="959.1" y2="168.3" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="157.1" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="963.1" y1="168.0" x2="963.1" y2="193.5" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="176.1" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="967.0" y1="164.5" x2="967.0" y2="202.5" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="169.2" width="2.45" height="24.8" fill="var(--up)"/>
<line x1="971.0" y1="147.0" x2="971.0" y2="199.1" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="164.4" width="2.45" height="29.6" fill="var(--down)"/>
<line x1="974.9" y1="183.2" x2="974.9" y2="201.6" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="192.9" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="978.9" y1="195.3" x2="978.9" y2="228.3" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="198.4" width="2.45" height="22.7" fill="var(--down)"/>
<line x1="982.8" y1="201.5" x2="982.8" y2="220.9" stroke="var(--up)" class="wick"/>
<rect x="981.61" y="209.1" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="986.8" y1="201.7" x2="986.8" y2="230.8" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="216.9" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="990.7" y1="195.0" x2="990.7" y2="221.6" stroke="var(--up)" class="wick"/>
<rect x="989.52" y="197.2" width="2.45" height="22.6" fill="var(--up)"/>
<line x1="994.7" y1="188.2" x2="994.7" y2="216.4" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="193.7" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="998.6" y1="165.0" x2="998.6" y2="204.7" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="197.9" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="1002.6" y1="192.6" x2="1002.6" y2="220.8" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="198.8" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="1006.5" y1="188.9" x2="1006.5" y2="229.1" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="203.3" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="1010.5" y1="290.8" x2="1010.5" y2="347.2" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="309.2" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="1014.5" y1="287.3" x2="1014.5" y2="315.7" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="293.7" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="1018.4" y1="285.3" x2="1018.4" y2="308.8" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="288.5" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="1022.4" y1="255.2" x2="1022.4" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="1021.13" y="267.3" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="1026.3" y1="240.4" x2="1026.3" y2="272.9" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="244.6" width="2.45" height="25.8" fill="var(--down)"/>
<line x1="1030.3" y1="260.7" x2="1030.3" y2="283.3" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="270.8" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="1034.2" y1="262.3" x2="1034.2" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="262.7" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="1038.2" y1="251.1" x2="1038.2" y2="270.8" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="267.3" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="1042.1" y1="269.7" x2="1042.1" y2="308.0" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="277.9" width="2.45" height="27.8" fill="var(--down)"/>
<line x1="1046.1" y1="293.0" x2="1046.1" y2="317.9" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="304.3" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="1050.0" y1="292.3" x2="1050.0" y2="313.3" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="294.8" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="60" y1="215.5" x2="1052" y2="215.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="219.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$507 R1</text>
<text x="1058" y="231.0" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="163.1" x2="1052" y2="163.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="166.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$523 R2</text>
<text x="1058" y="178.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="344.2" x2="1052" y2="344.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="338.2" font-size="11.5" fill="var(--support)" font-weight="600">$468 S1</text>
<text x="1058" y="350.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="427.8" x2="1052" y2="427.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="421.8" font-size="11.5" fill="var(--support)" font-weight="600">$442 S2</text>
<text x="1058" y="433.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="483.5" x2="1052" y2="483.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="477.5" font-size="11.5" fill="var(--support)" font-weight="600">$426 S3</text>
<text x="1058" y="489.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="294.8" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $523 | 4 | 2026년 5월 한 차례 + 사상 최고가($548.20, 2026-07) 형성 직후 되돌림 국면에서 세 차례 형성된 저항대 |
| R1 | $507 | 3 | 2026년 3월과 2026-07-30(실적발표 직전 마지막 거래일) 부근에서 형성 — 아래 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운의 "발생 직전 저항"과 사실상 같은 레벨 |
| **현재가** | **$482.74** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $468 | 5 | 2025년 11월~2026년 1월 조정 국면과 2026-07-31 갭다운 이후 되돌림 국면에서 반복적으로 형성된 지지대(레벨 중 터치 횟수 최다) |
| S2 | $442 | 2 | 2025년 하반기 조정 국면의 지지대 |
| S3 | $426 | 2 | 2025년 하반기 저점권에 가까운 지지대 |
| 참고선 | $548 | — | 52주 최고(2026-07) — 실적 발표 이후 조정으로 현재가와 12% 이상 괴리돼 있어 최근 거래 레짐과 단절된 참고 수준으로만 다룸 |

> S1~S3의 정확한 스윙 시점은 원자료(OHLCV)를 캔들 단위로 재대조한 것이 아니라 차트 좌표를 근거로 한 근사 판단이다 — 정밀한 날짜가 필요하면 스크립트 원자료를 다시 조회할 것.

---

## 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운

- 2026-07-31 Q2 2026 실적을 발표했다. 매출·Adjusted EPS 모두 컨센서스를 상회했으나, FY2026 Adjusted EPS 가이던스 중점($17.80)이 당시 컨센서스($17.93)에 못 미쳤고 CapEx 가이던스를 9.5% 상향한 데다 유럽·중국向 물량 가이던스를 하향한 것이 겹쳐 실망 매물이 나왔다(최근 뉴스 / 이슈 참고).
- 발표 전날(2026-07-30 부근) 종가는 위 2. 지지선 / 저항선 요약의 R1 레벨($507)과 거의 일치하는 수준이었고, 실적 발표 당일 종가는 $478.38로 **전일 대비 약 -5.7%~-6.0%** 하락했다(회사·언론 보도 기준, 이번 조사에서 정확한 거래량 배수는 확인하지 못했다 — 확인 필요).
- 이 갭다운 이후 주가는 R1($507)을 다시 넘어서지 못한 채 $460~$490대에서 등락하며 새 레짐을 형성 중이다 — 2. 지지선 / 저항선 요약에서 $548 참고선을 근시일 저항으로 다루지 않은 이유이기도 하다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-15. 원주가(과거 분할은 소급 반영, 배당은 미반영) — 최근 3년 내 주식분할 없음(핵심 지표 상단 각주와 일치).
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py LIN --name Linde --event 2026-07-31:"Q2 실적발표(가이던스·CapEx 우려로 급락)" --ref-line 548.20:"52주 최고" --close-on 2026-08-14` (기본 파라미터 그대로 사용, `--force-level`·`--levels` 등 조정 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값은 이 저장소의 다른 회사 문서와 비교 가능하도록 고정된 기본값이며, 최적화된 값이 아니다.
    - 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운의 갭다운 구간은 배당 미반영 원주가 기준이라, 배당락 효과가 섞여 있을 가능성은 낮지만(분기배당 규모가 주가 대비 미미) 완전히 배제하지는 않는다.
    - S1~S3 비고의 구체적 시기는 2. 지지선 / 저항선 요약 각주대로 좌표 기반 근사치이며 캔들 단위 재검증은 하지 않았다.

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
- [기술적 분석 — 주봉·5년](./10_technical_weekly.md)

---

## 참고 자료

- [Yahoo Finance — LIN 일봉 OHLCV](https://finance.yahoo.com/quote/LIN/history)
- [Investing.com — 2Q26 실적콜 트랜스크립트](https://www.investing.com/news/transcripts/earnings-call-transcript-linde-beats-q2-2026-estimates-but-shares-fall-52-93CH-4828679)

---

*작성일: 2026-08-15 (최종 수정일: 2026-08-23)*
