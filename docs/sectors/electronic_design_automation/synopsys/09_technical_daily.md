# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉 데이터는 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-08-24 종가 **$394.51**은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 stockanalysis.com 값과 일치한다. 이 폴더의 11개 문서 전체가 같은 기준일(2026-08-24)을 쓴다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-25 ~ 2026-08-24)

<div class="snps-chart">
<style>
.snps-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.snps-chart svg { width:100%; height:auto; display:block; }
.snps-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.snps-chart .title { fill: var(--ink); font-weight:600; }
.snps-chart .grid { stroke: var(--grid); stroke-width:1; }
.snps-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Synopsys(SNPS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Synopsys (SNPS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-25 ~ 2026-08-24 · 마지막 종가 $394.51 (2026-08-24) · 단위 USD</text>
<line x1="60" y1="531.0" x2="1052" y2="531.0" class="grid"/>
<text x="52" y="535.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="425.4" x2="1052" y2="425.4" class="grid"/>
<text x="52" y="429.4" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="319.9" x2="1052" y2="319.9" class="grid"/>
<text x="52" y="323.9" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="214.3" x2="1052" y2="214.3" class="grid"/>
<text x="52" y="218.3" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="108.8" x2="1052" y2="108.8" class="grid"/>
<text x="52" y="112.8" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="81.7" y1="626.0" x2="81.7" y2="631.0" class="axis"/>
<text x="81.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="164.7" y1="626.0" x2="164.7" y2="631.0" class="axis"/>
<text x="164.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="255.6" y1="626.0" x2="255.6" y2="631.0" class="axis"/>
<text x="255.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="330.7" y1="626.0" x2="330.7" y2="631.0" class="axis"/>
<text x="330.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="417.7" y1="626.0" x2="417.7" y2="631.0" class="axis"/>
<text x="417.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="496.7" y1="626.0" x2="496.7" y2="631.0" class="axis"/>
<text x="496.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="571.8" y1="626.0" x2="571.8" y2="631.0" class="axis"/>
<text x="571.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="658.8" y1="626.0" x2="658.8" y2="631.0" class="axis"/>
<text x="658.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="741.8" y1="626.0" x2="741.8" y2="631.0" class="axis"/>
<text x="741.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="820.8" y1="626.0" x2="820.8" y2="631.0" class="axis"/>
<text x="820.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="903.8" y1="626.0" x2="903.8" y2="631.0" class="axis"/>
<text x="903.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="990.7" y1="626.0" x2="990.7" y2="631.0" class="axis"/>
<text x="990.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="75.4" x2="1052" y2="75.4" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="78.4" font-size="10.5" fill="var(--muted)">$616 52주 최고(2025-09-08)</text>
<line x1="105.5" y1="56.0" x2="105.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="111.5" y="68.0" font-size="10.5" fill="var(--down)">2025-09-10 실적발표 갭다운 (시가 -29%, 종가 -35.8%)</text>
<line x1="62.0" y1="97.5" x2="62.0" y2="117.0" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="98.3" width="2.45" height="16.8" fill="var(--down)"/>
<line x1="65.9" y1="108.5" x2="65.9" y2="123.6" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="117.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="69.9" y1="100.6" x2="69.9" y2="122.9" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="102.1" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="73.8" y1="77.9" x2="73.8" y2="98.2" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="83.1" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="77.8" y1="83.4" x2="77.8" y2="104.7" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="89.8" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="81.7" y1="115.5" x2="81.7" y2="142.5" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="125.6" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="85.7" y1="122.1" x2="85.7" y2="136.7" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="125.4" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="89.6" y1="102.8" x2="89.6" y2="142.6" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="104.6" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="93.6" y1="75.5" x2="93.6" y2="120.2" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="88.2" width="2.45" height="24.6" fill="var(--down)"/>
<line x1="97.5" y1="75.4" x2="97.5" y2="110.4" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="89.6" width="2.45" height="17.2" fill="var(--up)"/>
<line x1="101.5" y1="77.3" x2="101.5" y2="103.5" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="85.7" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="105.5" y1="468.4" x2="105.5" y2="571.4" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="472.3" width="2.45" height="84.5" fill="var(--down)"/>
<line x1="109.4" y1="447.2" x2="109.4" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="450.6" width="2.45" height="46.7" fill="var(--up)"/>
<line x1="113.4" y1="437.7" x2="113.4" y2="484.7" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="438.5" width="2.45" height="38.8" fill="var(--down)"/>
<line x1="117.3" y1="459.2" x2="117.3" y2="495.6" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="464.5" width="2.45" height="26.0" fill="var(--down)"/>
<line x1="121.3" y1="473.2" x2="121.3" y2="495.1" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="476.2" width="2.45" height="11.4" fill="var(--up)"/>
<line x1="125.2" y1="469.2" x2="125.2" y2="494.0" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="477.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="129.2" y1="355.3" x2="129.2" y2="429.7" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="361.9" width="2.45" height="42.5" fill="var(--up)"/>
<line x1="133.1" y1="324.0" x2="133.1" y2="372.1" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="329.4" width="2.45" height="34.8" fill="var(--up)"/>
<line x1="137.1" y1="286.9" x2="137.1" y2="359.0" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="288.7" width="2.45" height="52.3" fill="var(--up)"/>
<line x1="141.0" y1="292.4" x2="141.0" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="295.7" width="2.45" height="44.6" fill="var(--down)"/>
<line x1="145.0" y1="338.2" x2="145.0" y2="395.4" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="338.9" width="2.45" height="48.4" fill="var(--down)"/>
<line x1="148.9" y1="346.1" x2="148.9" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="346.9" width="2.45" height="52.1" fill="var(--up)"/>
<line x1="152.9" y1="334.7" x2="152.9" y2="368.1" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="345.7" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="156.8" y1="336.9" x2="156.8" y2="365.7" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="345.2" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="160.8" y1="330.0" x2="160.8" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="333.8" width="2.45" height="23.9" fill="var(--up)"/>
<line x1="164.7" y1="328.9" x2="164.7" y2="352.6" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="343.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="168.7" y1="342.5" x2="168.7" y2="382.5" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="352.2" width="2.45" height="28.6" fill="var(--down)"/>
<line x1="172.6" y1="371.0" x2="172.6" y2="390.4" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="375.8" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="176.6" y1="359.5" x2="176.6" y2="384.2" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="365.9" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="180.5" y1="353.4" x2="180.5" y2="386.5" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="353.4" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="184.5" y1="336.0" x2="184.5" y2="369.0" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="342.4" width="2.45" height="26.5" fill="var(--up)"/>
<line x1="188.4" y1="345.1" x2="188.4" y2="360.7" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="346.3" width="2.45" height="6.5" fill="var(--down)"/>
<line x1="192.4" y1="346.1" x2="192.4" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="352.8" width="2.45" height="96.0" fill="var(--down)"/>
<line x1="196.4" y1="417.4" x2="196.4" y2="446.6" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="426.5" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="200.3" y1="419.5" x2="200.3" y2="460.6" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="438.6" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="204.3" y1="427.8" x2="204.3" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="433.3" width="2.45" height="21.9" fill="var(--down)"/>
<line x1="208.2" y1="434.9" x2="208.2" y2="455.9" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="446.1" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="212.2" y1="411.0" x2="212.2" y2="456.6" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="430.4" width="2.45" height="25.3" fill="var(--up)"/>
<line x1="216.1" y1="408.9" x2="216.1" y2="427.6" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="418.4" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="220.1" y1="405.0" x2="220.1" y2="436.0" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="406.4" width="2.45" height="22.8" fill="var(--up)"/>
<line x1="224.0" y1="392.2" x2="224.0" y2="437.4" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="411.8" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="228.0" y1="403.5" x2="228.0" y2="424.4" stroke="var(--up)" class="wick"/>
<rect x="226.74" y="412.6" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="231.9" y1="375.9" x2="231.9" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="395.5" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="235.9" y1="371.8" x2="235.9" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="380.5" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="239.8" y1="399.3" x2="239.8" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="400.8" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="243.8" y1="410.4" x2="243.8" y2="437.1" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="414.2" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="247.7" y1="419.6" x2="247.7" y2="449.6" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="425.4" width="2.45" height="14.9" fill="var(--down)"/>
<line x1="251.7" y1="412.3" x2="251.7" y2="440.9" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="417.4" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="255.6" y1="420.1" x2="255.6" y2="451.7" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="421.6" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="259.6" y1="452.7" x2="259.6" y2="498.9" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="457.1" width="2.45" height="39.4" fill="var(--down)"/>
<line x1="263.5" y1="495.3" x2="263.5" y2="525.3" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="496.2" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="267.5" y1="506.6" x2="267.5" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="507.8" width="2.45" height="31.4" fill="var(--down)"/>
<line x1="271.4" y1="530.3" x2="271.4" y2="558.6" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="543.0" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="275.4" y1="528.3" x2="275.4" y2="555.4" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="529.4" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="279.3" y1="531.7" x2="279.3" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="535.0" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="283.3" y1="523.1" x2="283.3" y2="542.7" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="529.7" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="287.3" y1="523.3" x2="287.3" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="538.9" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="291.2" y1="535.5" x2="291.2" y2="560.1" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="552.5" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="295.2" y1="532.9" x2="295.2" y2="556.3" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="551.6" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="299.1" y1="553.0" x2="299.1" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="556.3" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="303.1" y1="529.7" x2="303.1" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="301.83" y="559.9" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="307.0" y1="519.3" x2="307.0" y2="566.4" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="527.2" width="2.45" height="34.2" fill="var(--down)"/>
<line x1="311.0" y1="547.6" x2="311.0" y2="580.2" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="555.6" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="314.9" y1="518.5" x2="314.9" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="521.2" width="2.45" height="20.3" fill="var(--up)"/>
<line x1="318.9" y1="519.1" x2="318.9" y2="542.8" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="527.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="322.8" y1="506.4" x2="322.8" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="510.6" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="326.8" y1="491.1" x2="326.8" y2="511.2" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="493.0" width="2.45" height="14.6" fill="var(--up)"/>
<line x1="330.7" y1="431.8" x2="330.7" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="433.9" width="2.45" height="16.3" fill="var(--down)"/>
<line x1="334.7" y1="418.0" x2="334.7" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="426.8" width="2.45" height="16.4" fill="var(--up)"/>
<line x1="338.6" y1="386.8" x2="338.6" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="390.7" width="2.45" height="44.7" fill="var(--up)"/>
<line x1="342.6" y1="392.3" x2="342.6" y2="403.9" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="396.4" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="346.5" y1="380.9" x2="346.5" y2="395.1" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="390.1" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="350.5" y1="385.7" x2="350.5" y2="404.0" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="387.9" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="354.4" y1="379.8" x2="354.4" y2="403.0" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="386.5" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="358.4" y1="365.0" x2="358.4" y2="400.4" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="370.9" width="2.45" height="25.7" fill="var(--up)"/>
<line x1="362.3" y1="357.4" x2="362.3" y2="413.6" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="367.9" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="366.3" y1="367.4" x2="366.3" y2="420.1" stroke="var(--down)" class="wick"/>
<rect x="365.07" y="370.0" width="2.45" height="49.2" fill="var(--down)"/>
<line x1="370.2" y1="381.7" x2="370.2" y2="418.1" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="408.6" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="374.2" y1="393.8" x2="374.2" y2="420.2" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="397.3" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="378.2" y1="389.6" x2="378.2" y2="419.2" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="391.9" width="2.45" height="27.1" fill="var(--down)"/>
<line x1="382.1" y1="387.8" x2="382.1" y2="415.5" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="403.7" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="386.1" y1="384.1" x2="386.1" y2="405.2" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="396.5" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="390.0" y1="353.9" x2="390.0" y2="387.8" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="359.5" width="2.45" height="27.4" fill="var(--up)"/>
<line x1="394.0" y1="365.9" x2="394.0" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="367.3" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="397.9" y1="369.9" x2="397.9" y2="378.5" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="371.1" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="401.9" y1="365.1" x2="401.9" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="400.64" y="368.1" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="405.8" y1="352.4" x2="405.8" y2="379.0" stroke="var(--up)" class="wick"/>
<rect x="404.59" y="364.3" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="409.8" y1="364.7" x2="409.8" y2="378.9" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="373.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="413.7" y1="373.4" x2="413.7" y2="385.2" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="376.6" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="417.7" y1="349.7" x2="417.7" y2="380.1" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="361.2" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="421.6" y1="306.6" x2="421.6" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="332.2" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="425.6" y1="299.9" x2="425.6" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="301.4" width="2.45" height="27.8" fill="var(--up)"/>
<line x1="429.5" y1="267.2" x2="429.5" y2="311.7" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="278.3" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="433.5" y1="281.8" x2="433.5" y2="300.0" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="289.3" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="437.4" y1="258.8" x2="437.4" y2="296.5" stroke="var(--up)" class="wick"/>
<rect x="436.21" y="266.7" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="441.4" y1="245.6" x2="441.4" y2="269.7" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="249.3" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="445.3" y1="261.8" x2="445.3" y2="295.7" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="275.2" width="2.45" height="19.8" fill="var(--down)"/>
<line x1="449.3" y1="304.3" x2="449.3" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="308.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="453.2" y1="279.6" x2="453.2" y2="315.7" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="298.8" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="457.2" y1="277.2" x2="457.2" y2="303.0" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="285.5" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="461.1" y1="292.8" x2="461.1" y2="335.5" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="296.7" width="2.45" height="25.0" fill="var(--up)"/>
<line x1="465.1" y1="266.1" x2="465.1" y2="312.4" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="273.5" width="2.45" height="25.7" fill="var(--up)"/>
<line x1="469.1" y1="267.0" x2="469.1" y2="319.9" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="271.9" width="2.45" height="28.0" fill="var(--down)"/>
<line x1="473.0" y1="299.4" x2="473.0" y2="326.7" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="304.1" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="477.0" y1="303.0" x2="477.0" y2="334.1" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="313.5" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="480.9" y1="307.6" x2="480.9" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="312.5" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="484.9" y1="286.5" x2="484.9" y2="309.7" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="295.9" width="2.45" height="13.7" fill="var(--up)"/>
<line x1="488.8" y1="297.3" x2="488.8" y2="372.9" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="308.6" width="2.45" height="53.5" fill="var(--down)"/>
<line x1="492.8" y1="372.2" x2="492.8" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="373.6" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="496.7" y1="380.7" x2="496.7" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="402.9" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="500.7" y1="410.7" x2="500.7" y2="503.5" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="413.4" width="2.45" height="77.2" fill="var(--down)"/>
<line x1="504.6" y1="477.2" x2="504.6" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="490.9" width="2.45" height="10.7" fill="var(--up)"/>
<line x1="508.6" y1="476.5" x2="508.6" y2="517.9" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="490.7" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="512.5" y1="465.3" x2="512.5" y2="496.9" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="474.3" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="516.5" y1="440.3" x2="516.5" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="448.9" width="2.45" height="23.3" fill="var(--up)"/>
<line x1="520.4" y1="421.2" x2="520.4" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="446.7" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="524.4" y1="439.7" x2="524.4" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="442.1" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="528.3" y1="449.7" x2="528.3" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="450.1" width="2.45" height="31.6" fill="var(--down)"/>
<line x1="532.3" y1="443.5" x2="532.3" y2="487.7" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="452.7" width="2.45" height="29.0" fill="var(--up)"/>
<line x1="536.2" y1="474.3" x2="536.2" y2="504.9" stroke="var(--down)" class="wick"/>
<rect x="535.01" y="477.0" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="540.2" y1="432.0" x2="540.2" y2="460.9" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="441.7" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="544.1" y1="439.8" x2="544.1" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="441.4" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="548.1" y1="424.6" x2="548.1" y2="452.5" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="446.7" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="552.0" y1="460.5" x2="552.0" y2="494.5" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="469.0" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="556.0" y1="439.4" x2="556.0" y2="499.3" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="445.0" width="2.45" height="45.0" fill="var(--up)"/>
<line x1="560.0" y1="416.7" x2="560.0" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="427.2" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="563.9" y1="439.0" x2="563.9" y2="481.6" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="467.9" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="567.9" y1="494.8" x2="567.9" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="501.4" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="571.8" y1="475.6" x2="571.8" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="478.9" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="575.8" y1="465.0" x2="575.8" y2="508.6" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="479.7" width="2.45" height="25.0" fill="var(--up)"/>
<line x1="579.7" y1="447.6" x2="579.7" y2="488.1" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="465.6" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="583.7" y1="430.3" x2="583.7" y2="476.6" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="441.7" width="2.45" height="34.9" fill="var(--up)"/>
<line x1="587.6" y1="435.3" x2="587.6" y2="463.9" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="452.0" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="591.6" y1="444.6" x2="591.6" y2="468.4" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="452.4" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="595.5" y1="448.6" x2="595.5" y2="471.9" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="452.7" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="599.5" y1="454.2" x2="599.5" y2="477.5" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="461.4" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="603.4" y1="454.2" x2="603.4" y2="492.2" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="463.7" width="2.45" height="27.8" fill="var(--down)"/>
<line x1="607.4" y1="477.2" x2="607.4" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="490.9" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="611.3" y1="471.0" x2="611.3" y2="493.8" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="476.4" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="615.3" y1="456.1" x2="615.3" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="469.2" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="619.2" y1="455.6" x2="619.2" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="470.5" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="623.2" y1="460.8" x2="623.2" y2="483.4" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="471.4" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="627.1" y1="467.9" x2="627.1" y2="490.9" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="476.3" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="631.1" y1="442.8" x2="631.1" y2="468.4" stroke="var(--up)" class="wick"/>
<rect x="629.87" y="462.4" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="635.0" y1="469.2" x2="635.0" y2="510.2" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="474.7" width="2.45" height="23.3" fill="var(--down)"/>
<line x1="639.0" y1="476.3" x2="639.0" y2="524.0" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="483.5" width="2.45" height="26.1" fill="var(--down)"/>
<line x1="642.9" y1="502.4" x2="642.9" y2="530.2" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="519.9" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="646.9" y1="527.7" x2="646.9" y2="574.3" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="531.0" width="2.45" height="41.2" fill="var(--down)"/>
<line x1="650.9" y1="550.5" x2="650.9" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="566.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="654.8" y1="536.3" x2="654.8" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="538.4" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="658.8" y1="523.7" x2="658.8" y2="542.6" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="524.0" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="662.7" y1="528.7" x2="662.7" y2="559.3" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="539.5" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="666.7" y1="533.9" x2="666.7" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="537.2" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="670.6" y1="535.0" x2="670.6" y2="554.5" stroke="var(--up)" class="wick"/>
<rect x="669.39" y="535.4" width="2.45" height="8.9" fill="var(--up)"/>
<line x1="674.6" y1="499.0" x2="674.6" y2="519.4" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="506.2" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="678.5" y1="507.8" x2="678.5" y2="543.1" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="510.0" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="682.5" y1="522.7" x2="682.5" y2="553.9" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="527.6" width="2.45" height="19.8" fill="var(--down)"/>
<line x1="686.4" y1="492.1" x2="686.4" y2="556.2" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="493.5" width="2.45" height="53.3" fill="var(--up)"/>
<line x1="690.4" y1="467.4" x2="690.4" y2="492.6" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="478.6" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="694.3" y1="446.8" x2="694.3" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="449.8" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="698.3" y1="426.2" x2="698.3" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="433.1" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="702.2" y1="406.4" x2="702.2" y2="431.4" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="420.1" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="706.2" y1="397.7" x2="706.2" y2="430.9" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="402.3" width="2.45" height="27.2" fill="var(--up)"/>
<line x1="710.1" y1="361.6" x2="710.1" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="388.3" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="714.1" y1="364.8" x2="714.1" y2="381.3" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="367.9" width="2.45" height="13.4" fill="var(--up)"/>
<line x1="718.0" y1="388.9" x2="718.0" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="716.81" y="391.4" width="2.45" height="19.5" fill="var(--down)"/>
<line x1="722.0" y1="315.1" x2="722.0" y2="384.9" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="318.2" width="2.45" height="66.4" fill="var(--up)"/>
<line x1="725.9" y1="317.8" x2="725.9" y2="345.2" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="323.0" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="729.9" y1="324.1" x2="729.9" y2="364.2" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="326.2" width="2.45" height="27.7" fill="var(--down)"/>
<line x1="733.8" y1="358.7" x2="733.8" y2="379.6" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="359.5" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="737.8" y1="354.3" x2="737.8" y2="379.8" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="356.6" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="741.8" y1="324.2" x2="741.8" y2="350.6" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="338.6" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="745.7" y1="319.4" x2="745.7" y2="344.5" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="325.2" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="749.7" y1="293.4" x2="749.7" y2="319.9" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="314.6" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="753.6" y1="304.4" x2="753.6" y2="325.1" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="310.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="757.6" y1="284.0" x2="757.6" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="306.6" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="761.5" y1="279.5" x2="761.5" y2="318.6" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="285.1" width="2.45" height="25.6" fill="var(--up)"/>
<line x1="765.5" y1="278.3" x2="765.5" y2="294.6" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="285.7" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="769.4" y1="283.6" x2="769.4" y2="302.7" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="292.0" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="773.4" y1="288.8" x2="773.4" y2="315.1" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="289.1" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="777.3" y1="291.1" x2="777.3" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="298.7" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="781.3" y1="300.9" x2="781.3" y2="338.8" stroke="var(--up)" class="wick"/>
<rect x="780.05" y="314.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="785.2" y1="316.0" x2="785.2" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="321.6" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="789.2" y1="317.8" x2="789.2" y2="339.8" stroke="var(--down)" class="wick"/>
<rect x="787.95" y="331.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="793.1" y1="321.5" x2="793.1" y2="375.3" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="322.1" width="2.45" height="41.4" fill="var(--up)"/>
<line x1="797.1" y1="309.9" x2="797.1" y2="343.8" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="311.5" width="2.45" height="26.9" fill="var(--up)"/>
<line x1="801.0" y1="247.9" x2="801.0" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="267.7" width="2.45" height="31.1" fill="var(--up)"/>
<line x1="805.0" y1="236.5" x2="805.0" y2="268.8" stroke="var(--up)" class="wick"/>
<rect x="803.76" y="246.9" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="808.9" y1="246.8" x2="808.9" y2="271.0" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="246.9" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="812.9" y1="264.8" x2="812.9" y2="379.7" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="298.8" width="2.45" height="62.0" fill="var(--down)"/>
<line x1="816.8" y1="352.6" x2="816.8" y2="384.6" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="360.7" width="2.45" height="10.7" fill="var(--down)"/>
<line x1="820.8" y1="332.0" x2="820.8" y2="381.7" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="336.2" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="824.7" y1="301.5" x2="824.7" y2="350.2" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="302.3" width="2.45" height="48.0" fill="var(--up)"/>
<line x1="828.7" y1="311.2" x2="828.7" y2="338.5" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="314.0" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="832.7" y1="319.1" x2="832.7" y2="351.6" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="319.1" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="836.6" y1="343.2" x2="836.6" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="345.3" width="2.45" height="48.8" fill="var(--down)"/>
<line x1="840.6" y1="365.3" x2="840.6" y2="397.2" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="375.9" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="844.5" y1="346.2" x2="844.5" y2="423.3" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="371.0" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="848.5" y1="378.1" x2="848.5" y2="418.5" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="403.2" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="852.4" y1="395.1" x2="852.4" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="409.1" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="856.4" y1="402.0" x2="856.4" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="410.5" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="860.3" y1="396.9" x2="860.3" y2="419.1" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="399.5" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="864.3" y1="413.8" x2="864.3" y2="436.4" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="421.2" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="868.2" y1="365.2" x2="868.2" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="867.00" y="400.7" width="2.45" height="28.3" fill="var(--up)"/>
<line x1="872.2" y1="391.5" x2="872.2" y2="420.5" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="400.1" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="876.1" y1="384.5" x2="876.1" y2="419.5" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="394.7" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="880.1" y1="362.5" x2="880.1" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="393.8" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="884.0" y1="376.5" x2="884.0" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="396.0" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="888.0" y1="392.6" x2="888.0" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="397.7" width="2.45" height="17.1" fill="var(--down)"/>
<line x1="891.9" y1="408.5" x2="891.9" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="416.3" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="895.9" y1="403.7" x2="895.9" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="408.7" width="2.45" height="22.5" fill="var(--down)"/>
<line x1="899.8" y1="426.4" x2="899.8" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="433.7" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="903.8" y1="394.9" x2="903.8" y2="418.2" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="415.9" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="907.7" y1="418.1" x2="907.7" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="423.0" width="2.45" height="29.5" fill="var(--down)"/>
<line x1="911.7" y1="439.4" x2="911.7" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="910.47" y="441.8" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="915.6" y1="422.1" x2="915.6" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="430.0" width="2.45" height="23.7" fill="var(--down)"/>
<line x1="919.6" y1="453.9" x2="919.6" y2="476.5" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="454.7" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="923.6" y1="439.2" x2="923.6" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="439.4" width="2.45" height="28.6" fill="var(--up)"/>
<line x1="927.5" y1="429.9" x2="927.5" y2="449.8" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="434.9" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="931.5" y1="417.2" x2="931.5" y2="461.9" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="427.9" width="2.45" height="31.7" fill="var(--down)"/>
<line x1="935.4" y1="458.1" x2="935.4" y2="479.8" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="475.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="939.4" y1="462.7" x2="939.4" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="468.0" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="943.3" y1="476.9" x2="943.3" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="476.9" width="2.45" height="18.2" fill="var(--down)"/>
<line x1="947.3" y1="525.3" x2="947.3" y2="602.8" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="527.6" width="2.45" height="36.5" fill="var(--down)"/>
<line x1="951.2" y1="562.3" x2="951.2" y2="586.2" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="569.0" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="955.2" y1="549.9" x2="955.2" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="554.1" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="959.1" y1="552.0" x2="959.1" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="555.0" width="2.45" height="23.2" fill="var(--down)"/>
<line x1="963.1" y1="575.5" x2="963.1" y2="591.4" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="579.8" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="967.0" y1="573.6" x2="967.0" y2="596.4" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="577.4" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="971.0" y1="539.8" x2="971.0" y2="566.2" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="554.2" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="974.9" y1="526.2" x2="974.9" y2="573.6" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="546.7" width="2.45" height="18.5" fill="var(--down)"/>
<line x1="978.9" y1="557.1" x2="978.9" y2="587.1" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="561.6" width="2.45" height="24.9" fill="var(--down)"/>
<line x1="982.8" y1="571.0" x2="982.8" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="581.7" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="986.8" y1="552.9" x2="986.8" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="554.7" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="990.7" y1="539.3" x2="990.7" y2="560.6" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="543.2" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="994.7" y1="521.9" x2="994.7" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="522.9" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="998.6" y1="505.7" x2="998.6" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="510.6" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="1002.6" y1="510.1" x2="1002.6" y2="538.9" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="518.4" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="1006.5" y1="496.3" x2="1006.5" y2="519.1" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="497.2" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="1010.5" y1="485.9" x2="1010.5" y2="507.2" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="497.2" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="1014.5" y1="504.9" x2="1014.5" y2="526.4" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="505.7" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="1018.4" y1="492.2" x2="1018.4" y2="509.5" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="502.0" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="1022.4" y1="495.3" x2="1022.4" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="505.0" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="1026.3" y1="480.4" x2="1026.3" y2="511.2" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="485.6" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="1030.3" y1="476.6" x2="1030.3" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="493.8" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="1034.2" y1="503.9" x2="1034.2" y2="525.9" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="508.2" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="1038.2" y1="513.6" x2="1038.2" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="520.0" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="1042.1" y1="528.0" x2="1042.1" y2="542.5" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="531.8" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="1046.1" y1="526.8" x2="1046.1" y2="542.0" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="529.6" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="1050.0" y1="539.5" x2="1050.0" y2="556.1" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="541.1" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="60" y1="426.7" x2="1052" y2="426.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="430.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$449 R1</text>
<text x="1058" y="442.2" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="363.9" x2="1052" y2="363.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="367.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$479 R2</text>
<text x="1058" y="379.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="322.0" x2="1052" y2="322.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="325.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$499 R3</text>
<text x="1058" y="337.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="570.8" x2="1052" y2="570.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="564.8" font-size="11.5" fill="var(--support)" font-weight="600">$381 S1</text>
<text x="1058" y="576.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="602.8" x2="1052" y2="602.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="596.8" font-size="11.5" fill="var(--support)" font-weight="600">$366 S2 (52주 최저)</text>
<text x="1058" y="608.8" font-size="9.5" fill="var(--muted)">터치 1회</text>
<circle cx="1052.0" cy="542.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="534.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $395 (2026-08-24)</text>
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
| R3 | $499 | 2 | 2025-10-01·2026-04-24 스윙 고점대 |
| R2 | $479 | 3 | 2025-10-27·2025-12-11·2026-06-23 반복 저항 |
| R1 | $449 | 4 | 2026-02-25·2026-03-05·2026-03-23·2026-07-13 — 최근 1년 중 가장 자주 되돌림한 구간 |
| **현재가** | **$394.51** (2026-08-24 종가) | — | R1과 S1 사이 |
| S1 | $381 | 4 | 2025-09-10·2025-11-18·2026-03-27·2026-04-13 — 현재가에 가장 근접한 지지. 2025-09-10 갭다운 당일이 이 대역의 시작점이다 |
| S2 (52주 최저) | $366 | 1 | 2026-07-17 형성된 52주 최저. 터치 1회로 기준(2회) 미달이나 반등 기점이라는 의미가 커 `--force-level`로 예외 포함 |
| 참고선 | $616 | — | 52주 최고(2025-09-08) — 아래 3. 관측된 특이 구간의 갭다운 직전 레짐이라 현재 가격대와 단절되어 있어 근시일 저항으로 보지 않음 |

> 표시 기준은 "현재가에서 가까운 순으로 각 방향 3개"(스크립트 기본값)다. 다만 이번 구간에서는 **현재가 아래로 터치 2회 이상 클러스터가 $381 하나뿐**이라 억지로 3개를 채우지 않았고, 대신 52주 최저($366)만 예외로 넣었다. 현재가와 R1($449) 사이에는 터치 1회짜리 $426 클러스터가 있으나 기준(2회) 미달이라 표에서 제외했다 — 현재가 바로 위가 그만큼 비어 있다는 뜻이기도 하다. R3 위로도 $518·$537 클러스터가 각각 터치 2회로 존재하나 현재가에서 30% 이상 떨어져 있어 표시하지 않았다.

---

## 3. 관측된 특이 구간 — 2025-09-10 갭다운

- 2025-09-09 장 마감 후 FY2025 3분기 실적 발표([최근 뉴스 / 이슈](./08_news.md) 로그 참고) 이후 다음 거래일(2025-09-10) 시가부터 갭다운.
- 종가 기준 전일 대비 **-35.8%** ($604.37 → $387.78), 거래량은 평소(일 약 224만 주) 대비 약 9배인 **2,116만 주**로 급증.
- 이 사건 이후 가격대가 구조적으로 재설정되어(약 $600대 → $370~540대), 갭다운 이전 스윙 레벨(예: $616 52주 최고)은 현재 거래 레짐과 직접 연결되지 않는 참고선으로만 표시했다. 갭다운 당일 저점대가 그대로 현재의 S1($381) 대역이 됐다는 점도 함께 볼 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-25~2026-08-24. 수집 시점: 2026-08-25. 원주가(과거 분할은 소급 반영, 배당은 미반영) — 조사 기간 중 Synopsys의 주식분할 이력은 확인되지 않음.
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 2. 지지선 / 저항선 요약 각주).
- **생성**: `scripts/gen_technical_chart.py SNPS --name Synopsys --event 2025-09-10:"실적발표 갭다운 (시가 -29%, 종가 -35.8%)" --ref-line 615.79:"52주 최고(2025-09-08)" --force-level '366:(52주 최저)'`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **1년 창이 앞으로 밀리면 레벨 자체가 재편된다.** 직전 갱신(2026-08-14 기준)에서는 $408이 터치 4회 지지였는데, 창이 열흘 밀린 이번 갱신에서는 그 클러스터가 사라지고 $381이 유일한 지지로 남았다 — 클러스터 경계가 ±2.5%라 표본이 조금만 바뀌어도 인접 스윙이 다른 클러스터로 재배치되기 때문이다. 레벨을 고정된 실체로 읽지 말 것.
    - 2025-09-10 갭다운처럼 뉴스 이벤트로 인한 불연속 구간은 통상적인 지지/저항 해석이 적용되기 어렵다(3. 관측된 특이 구간).

---

## 관련 문서

- **먼저 읽기** — [최종 보고서](./11_final_report.md): 아래 문서 전체를 종합한 요약이라, 처음이라면 여기부터 봐도 된다
- **회사 이해** — [개요](./01_overview.md) · [역사 / 주요 이벤트](./02_history.md) · [CEO / 경영진](./03_ceo.md)
- **숫자** — [핵심 지표](./04_metrics.md) · [재무 / 실적](./05_financials.md) · [밸류에이션 / 적정주가](./06_valuation.md)
- **판단 · 로그** — [투자 판단](./07_investment.md) · [최근 뉴스 / 이슈](./08_news.md)
- **가격 차트** — [기술적 분석 — 주봉·5년](./10_technical_weekly.md)

---

## 참고 자료

- [Yahoo Finance — SNPS Chart API](https://query1.finance.yahoo.com/v8/finance/chart/SNPS) (일봉 OHLCV 원자료, 2026-08-25 수집)
- [stockanalysis.com — SNPS Price History](https://stockanalysis.com/stocks/snps/history/)

---

*작성일: 2026-08-15 (최종 수정일: 2026-08-25)*
