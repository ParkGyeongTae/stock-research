# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). 두 문서에서 겹치는 시점의 종가를 대조한 결과: `2025-12-31` 종가 $44.87, `2026-08-14` 종가 $46.26 — 둘 다 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md) 상단에 인용된 값과 일치(주식분할 이력 없어 수정주가 이슈 없음).

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="ionq-chart">
<style>
.ionq-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ionq-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ionq-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ionq-chart svg { width:100%; height:auto; display:block; }
.ionq-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ionq-chart .title { fill: var(--ink); font-weight:600; }
.ionq-chart .grid { stroke: var(--grid); stroke-width:1; }
.ionq-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="IonQ(IONQ) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">IonQ (IONQ) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $46.26 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="571.7" x2="1052" y2="571.7" class="grid"/>
<text x="52" y="575.7" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="481.2" x2="1052" y2="481.2" class="grid"/>
<text x="52" y="485.2" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="390.8" x2="1052" y2="390.8" class="grid"/>
<text x="52" y="394.8" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="300.3" x2="1052" y2="300.3" class="grid"/>
<text x="52" y="304.3" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="209.8" x2="1052" y2="209.8" class="grid"/>
<text x="52" y="213.8" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="119.3" x2="1052" y2="119.3" class="grid"/>
<text x="52" y="123.3" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
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
<line x1="60" y1="77.4" x2="1052" y2="77.4" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="80.4" font-size="10.5" fill="var(--muted)">$85 52주 최고</text>
<line x1="62.0" y1="473.7" x2="62.0" y2="486.5" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="474.2" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="65.9" y1="476.7" x2="65.9" y2="490.2" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="479.2" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="69.9" y1="478.6" x2="69.9" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="479.2" width="2.45" height="30.9" fill="var(--down)"/>
<line x1="73.8" y1="504.7" x2="73.8" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="504.9" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="77.8" y1="505.0" x2="77.8" y2="513.4" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="506.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="81.7" y1="482.0" x2="81.7" y2="511.5" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="483.2" width="2.45" height="24.2" fill="var(--up)"/>
<line x1="85.7" y1="482.9" x2="85.7" y2="494.5" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="484.0" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="89.6" y1="472.9" x2="89.6" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="474.5" width="2.45" height="17.2" fill="var(--up)"/>
<line x1="93.6" y1="457.1" x2="93.6" y2="474.3" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="468.4" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="97.5" y1="447.5" x2="97.5" y2="468.1" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="451.4" width="2.45" height="15.8" fill="var(--up)"/>
<line x1="101.5" y1="451.7" x2="101.5" y2="464.9" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="456.4" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="105.5" y1="453.6" x2="105.5" y2="479.2" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="454.2" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="109.4" y1="452.2" x2="109.4" y2="476.0" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="457.3" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="113.4" y1="453.8" x2="113.4" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="462.1" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="117.3" y1="456.5" x2="117.3" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="459.0" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="121.3" y1="457.8" x2="121.3" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="462.3" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="125.2" y1="442.7" x2="125.2" y2="471.8" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="445.0" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="129.2" y1="434.4" x2="129.2" y2="449.0" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="442.2" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="133.1" y1="415.8" x2="133.1" y2="450.7" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="417.5" width="2.45" height="25.8" fill="var(--up)"/>
<line x1="137.1" y1="335.8" x2="137.1" y2="416.5" stroke="var(--up)" class="wick"/>
<rect x="135.84" y="340.0" width="2.45" height="75.2" fill="var(--up)"/>
<line x1="141.0" y1="301.3" x2="141.0" y2="336.9" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="308.3" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="145.0" y1="274.5" x2="145.0" y2="326.2" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="279.8" width="2.45" height="29.7" fill="var(--up)"/>
<line x1="148.9" y1="242.5" x2="148.9" y2="290.5" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="251.1" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="152.9" y1="205.9" x2="152.9" y2="251.2" stroke="var(--down)" class="wick"/>
<rect x="151.65" y="222.7" width="2.45" height="15.9" fill="var(--down)"/>
<line x1="156.8" y1="198.0" x2="156.8" y2="249.3" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="206.1" width="2.45" height="40.1" fill="var(--up)"/>
<line x1="160.8" y1="181.1" x2="160.8" y2="244.6" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="192.3" width="2.45" height="34.7" fill="var(--up)"/>
<line x1="164.7" y1="154.4" x2="164.7" y2="196.7" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="163.3" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="168.7" y1="156.0" x2="168.7" y2="200.7" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="162.3" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="172.6" y1="189.1" x2="172.6" y2="237.8" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="199.3" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="176.6" y1="206.0" x2="176.6" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="224.2" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="180.5" y1="219.9" x2="180.5" y2="271.2" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="224.5" width="2.45" height="37.3" fill="var(--down)"/>
<line x1="184.5" y1="255.0" x2="184.5" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="267.8" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="188.4" y1="256.4" x2="188.4" y2="299.0" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="272.3" width="2.45" height="15.4" fill="var(--up)"/>
<line x1="192.4" y1="213.4" x2="192.4" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="213.4" width="2.45" height="43.3" fill="var(--up)"/>
<line x1="196.4" y1="175.8" x2="196.4" y2="224.7" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="180.1" width="2.45" height="24.3" fill="var(--up)"/>
<line x1="200.3" y1="126.3" x2="200.3" y2="192.8" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="128.5" width="2.45" height="63.2" fill="var(--up)"/>
<line x1="204.3" y1="92.5" x2="204.3" y2="160.2" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="110.6" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="208.2" y1="97.5" x2="208.2" y2="186.3" stroke="var(--down)" class="wick"/>
<rect x="206.98" y="128.8" width="2.45" height="42.1" fill="var(--down)"/>
<line x1="212.2" y1="137.4" x2="212.2" y2="176.8" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="142.0" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="216.1" y1="143.0" x2="216.1" y2="204.0" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="146.5" width="2.45" height="57.5" fill="var(--down)"/>
<line x1="220.1" y1="77.4" x2="220.1" y2="184.5" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="100.4" width="2.45" height="72.2" fill="var(--up)"/>
<line x1="224.0" y1="109.6" x2="224.0" y2="156.2" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="120.7" width="2.45" height="20.8" fill="var(--down)"/>
<line x1="228.0" y1="117.3" x2="228.0" y2="202.6" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="119.9" width="2.45" height="68.1" fill="var(--down)"/>
<line x1="231.9" y1="174.8" x2="231.9" y2="250.5" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="174.8" width="2.45" height="74.9" fill="var(--down)"/>
<line x1="235.9" y1="248.5" x2="235.9" y2="289.4" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="251.4" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="239.8" y1="250.5" x2="239.8" y2="312.1" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="252.2" width="2.45" height="48.6" fill="var(--down)"/>
<line x1="243.8" y1="292.1" x2="243.8" y2="325.5" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="296.3" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="247.7" y1="306.2" x2="247.7" y2="370.2" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="316.6" width="2.45" height="24.9" fill="var(--down)"/>
<line x1="251.7" y1="273.8" x2="251.7" y2="327.4" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="290.3" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="255.6" y1="263.1" x2="255.6" y2="301.0" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="282.1" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="259.6" y1="250.5" x2="259.6" y2="279.7" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="273.1" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="263.5" y1="258.9" x2="263.5" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="275.0" width="2.45" height="51.1" fill="var(--down)"/>
<line x1="267.5" y1="281.3" x2="267.5" y2="319.1" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="290.2" width="2.45" height="20.4" fill="var(--up)"/>
<line x1="271.4" y1="283.6" x2="271.4" y2="316.6" stroke="var(--up)" class="wick"/>
<rect x="270.22" y="298.7" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="275.4" y1="273.4" x2="275.4" y2="300.6" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="278.8" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="279.3" y1="275.9" x2="279.3" y2="331.4" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="279.0" width="2.45" height="35.7" fill="var(--down)"/>
<line x1="283.3" y1="326.0" x2="283.3" y2="362.9" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="338.6" width="2.45" height="21.6" fill="var(--down)"/>
<line x1="287.3" y1="332.8" x2="287.3" y2="362.7" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="341.8" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="291.2" y1="309.4" x2="291.2" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="289.98" y="323.5" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="295.2" y1="306.6" x2="295.2" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="306.9" width="2.45" height="42.1" fill="var(--up)"/>
<line x1="299.1" y1="309.2" x2="299.1" y2="347.2" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="313.9" width="2.45" height="28.3" fill="var(--down)"/>
<line x1="303.1" y1="336.2" x2="303.1" y2="357.1" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="349.4" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="307.0" y1="340.1" x2="307.0" y2="391.8" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="347.7" width="2.45" height="36.6" fill="var(--down)"/>
<line x1="311.0" y1="391.7" x2="311.0" y2="442.3" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="395.8" width="2.45" height="36.6" fill="var(--down)"/>
<line x1="314.9" y1="401.8" x2="314.9" y2="455.7" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="416.3" width="2.45" height="38.0" fill="var(--up)"/>
<line x1="318.9" y1="397.5" x2="318.9" y2="427.5" stroke="var(--up)" class="wick"/>
<rect x="317.64" y="410.8" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="322.8" y1="388.2" x2="322.8" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="398.7" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="326.8" y1="384.6" x2="326.8" y2="414.9" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="398.5" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="330.7" y1="394.7" x2="330.7" y2="475.0" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="403.7" width="2.45" height="68.5" fill="var(--down)"/>
<line x1="334.7" y1="456.3" x2="334.7" y2="499.3" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="458.1" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="338.6" y1="414.9" x2="338.6" y2="458.7" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="420.1" width="2.45" height="36.3" fill="var(--up)"/>
<line x1="342.6" y1="409.7" x2="342.6" y2="443.1" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="417.4" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="346.5" y1="406.6" x2="346.5" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="414.3" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="350.5" y1="392.1" x2="350.5" y2="412.7" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="397.1" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="354.4" y1="401.0" x2="354.4" y2="421.4" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="403.1" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="358.4" y1="393.7" x2="358.4" y2="419.5" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="412.7" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="362.3" y1="400.7" x2="362.3" y2="433.2" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="403.0" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="366.3" y1="342.6" x2="366.3" y2="406.1" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="347.7" width="2.45" height="55.1" fill="var(--up)"/>
<line x1="370.2" y1="352.2" x2="370.2" y2="380.5" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="354.6" width="2.45" height="11.9" fill="var(--down)"/>
<line x1="374.2" y1="347.2" x2="374.2" y2="377.6" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="351.3" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="378.2" y1="339.6" x2="378.2" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="350.6" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="382.1" y1="358.1" x2="382.1" y2="379.5" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="361.8" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="386.1" y1="364.7" x2="386.1" y2="399.2" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="367.7" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="390.0" y1="363.6" x2="390.0" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="371.9" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="394.0" y1="381.7" x2="394.0" y2="434.4" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="383.7" width="2.45" height="42.6" fill="var(--down)"/>
<line x1="397.9" y1="391.7" x2="397.9" y2="418.8" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="393.7" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="401.9" y1="371.3" x2="401.9" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="388.8" width="2.45" height="39.5" fill="var(--down)"/>
<line x1="405.8" y1="402.4" x2="405.8" y2="426.6" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="407.7" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="409.8" y1="395.8" x2="409.8" y2="419.0" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="404.5" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="413.7" y1="340.1" x2="413.7" y2="393.7" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="355.8" width="2.45" height="36.0" fill="var(--up)"/>
<line x1="417.7" y1="349.7" x2="417.7" y2="380.4" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="366.1" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="421.6" y1="373.8" x2="421.6" y2="402.3" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="375.4" width="2.45" height="17.0" fill="var(--down)"/>
<line x1="425.6" y1="393.7" x2="425.6" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="394.5" width="2.45" height="32.5" fill="var(--down)"/>
<line x1="429.5" y1="420.1" x2="429.5" y2="439.1" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="431.8" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="433.5" y1="419.4" x2="433.5" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="423.2" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="437.4" y1="423.0" x2="437.4" y2="438.9" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="429.9" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="441.4" y1="417.1" x2="441.4" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="420.0" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="445.3" y1="387.9" x2="445.3" y2="422.2" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="402.4" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="449.3" y1="383.8" x2="449.3" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="383.9" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="453.2" y1="373.9" x2="453.2" y2="396.9" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="390.8" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="457.2" y1="368.1" x2="457.2" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="386.7" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="461.1" y1="367.1" x2="461.1" y2="397.3" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="377.6" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="465.1" y1="381.5" x2="465.1" y2="410.8" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="382.2" width="2.45" height="21.4" fill="var(--up)"/>
<line x1="469.1" y1="373.4" x2="469.1" y2="409.0" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="380.3" width="2.45" height="20.1" fill="var(--down)"/>
<line x1="473.0" y1="382.4" x2="473.0" y2="414.9" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="382.8" width="2.45" height="21.2" fill="var(--up)"/>
<line x1="477.0" y1="376.5" x2="477.0" y2="413.0" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="379.2" width="2.45" height="33.7" fill="var(--down)"/>
<line x1="480.9" y1="373.7" x2="480.9" y2="413.2" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="383.5" width="2.45" height="24.5" fill="var(--up)"/>
<line x1="484.9" y1="352.4" x2="484.9" y2="403.8" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="384.8" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="488.8" y1="366.7" x2="488.8" y2="429.8" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="375.3" width="2.45" height="30.6" fill="var(--down)"/>
<line x1="492.8" y1="389.1" x2="492.8" y2="409.4" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="396.8" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="496.7" y1="395.2" x2="496.7" y2="421.5" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="397.6" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="500.7" y1="385.4" x2="500.7" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="406.0" width="2.45" height="44.8" fill="var(--down)"/>
<line x1="504.6" y1="423.0" x2="504.6" y2="453.8" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="431.6" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="508.6" y1="418.8" x2="508.6" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="424.9" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="512.5" y1="428.2" x2="512.5" y2="461.7" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="428.2" width="2.45" height="23.7" fill="var(--down)"/>
<line x1="516.5" y1="449.7" x2="516.5" y2="491.1" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="450.5" width="2.45" height="30.9" fill="var(--down)"/>
<line x1="520.4" y1="474.7" x2="520.4" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="475.5" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="524.4" y1="482.9" x2="524.4" y2="511.7" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="484.8" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="528.3" y1="494.4" x2="528.3" y2="538.9" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="494.8" width="2.45" height="28.6" fill="var(--down)"/>
<line x1="532.3" y1="532.1" x2="532.3" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="536.2" width="2.45" height="31.6" fill="var(--down)"/>
<line x1="536.2" y1="516.5" x2="536.2" y2="559.5" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="526.6" width="2.45" height="28.0" fill="var(--up)"/>
<line x1="540.2" y1="520.7" x2="540.2" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="522.1" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="544.1" y1="512.3" x2="544.1" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="524.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="548.1" y1="516.9" x2="548.1" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="517.0" width="2.45" height="22.1" fill="var(--down)"/>
<line x1="552.0" y1="538.2" x2="552.0" y2="563.7" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="538.2" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="556.0" y1="529.6" x2="556.0" y2="564.0" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="534.5" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="560.0" y1="532.6" x2="560.0" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="540.2" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="563.9" y1="527.5" x2="563.9" y2="550.1" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="541.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="567.9" y1="539.3" x2="567.9" y2="553.8" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="540.7" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="571.8" y1="536.6" x2="571.8" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="547.6" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="575.8" y1="556.6" x2="575.8" y2="570.2" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="562.5" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="579.7" y1="554.0" x2="579.7" y2="570.0" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="557.1" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="583.7" y1="531.9" x2="583.7" y2="555.1" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="539.2" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="587.6" y1="464.0" x2="587.6" y2="492.5" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="473.3" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="591.6" y1="485.2" x2="591.6" y2="513.3" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="486.5" width="2.45" height="9.5" fill="var(--down)"/>
<line x1="595.5" y1="495.4" x2="595.5" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="496.3" width="2.45" height="17.3" fill="var(--up)"/>
<line x1="599.5" y1="498.2" x2="599.5" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="507.9" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="603.4" y1="497.2" x2="603.4" y2="512.5" stroke="var(--down)" class="wick"/>
<rect x="602.20" y="502.2" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="607.4" y1="511.3" x2="607.4" y2="532.7" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="512.0" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="611.3" y1="504.0" x2="611.3" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="519.9" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="615.3" y1="516.7" x2="615.3" y2="537.2" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="518.6" width="2.45" height="10.0" fill="var(--up)"/>
<line x1="619.2" y1="509.1" x2="619.2" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="517.9" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="623.2" y1="518.4" x2="623.2" y2="540.0" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="523.9" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="627.1" y1="529.1" x2="627.1" y2="544.3" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="535.7" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="631.1" y1="530.3" x2="631.1" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="539.3" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="635.0" y1="531.8" x2="635.0" y2="550.1" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="539.9" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="639.0" y1="534.2" x2="639.0" y2="544.0" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="541.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="642.9" y1="535.5" x2="642.9" y2="550.4" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="544.1" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="646.9" y1="548.6" x2="646.9" y2="565.1" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="554.5" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="650.9" y1="551.4" x2="650.9" y2="567.2" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="555.4" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="654.8" y1="538.9" x2="654.8" y2="560.0" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="543.6" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="658.8" y1="540.4" x2="658.8" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="657.53" y="547.3" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="662.7" y1="533.9" x2="662.7" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="541.1" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="666.7" y1="557.1" x2="666.7" y2="574.3" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="559.1" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="670.6" y1="575.3" x2="670.6" y2="595.5" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="575.8" width="2.45" height="18.5" fill="var(--down)"/>
<line x1="674.6" y1="588.4" x2="674.6" y2="608.9" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="591.7" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="678.5" y1="579.1" x2="678.5" y2="598.4" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="582.3" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="682.5" y1="572.5" x2="682.5" y2="593.7" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="575.0" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="686.4" y1="576.3" x2="686.4" y2="601.2" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="578.0" width="2.45" height="22.6" fill="var(--up)"/>
<line x1="690.4" y1="569.0" x2="690.4" y2="583.4" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="577.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="694.3" y1="581.8" x2="694.3" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="693.10" y="583.3" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="698.3" y1="561.8" x2="698.3" y2="585.2" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="565.7" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="702.2" y1="578.5" x2="702.2" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="583.0" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="706.2" y1="577.4" x2="706.2" y2="588.6" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="582.7" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="710.1" y1="573.2" x2="710.1" y2="591.0" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="573.9" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="714.1" y1="518.6" x2="714.1" y2="562.1" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="519.6" width="2.45" height="36.0" fill="var(--up)"/>
<line x1="718.0" y1="451.0" x2="718.0" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="451.8" width="2.45" height="44.2" fill="var(--up)"/>
<line x1="722.0" y1="432.1" x2="722.0" y2="473.6" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="438.9" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="725.9" y1="420.7" x2="725.9" y2="447.9" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="426.1" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="729.9" y1="403.7" x2="729.9" y2="434.9" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="406.0" width="2.45" height="27.0" fill="var(--up)"/>
<line x1="733.8" y1="402.3" x2="733.8" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="403.4" width="2.45" height="21.0" fill="var(--down)"/>
<line x1="737.8" y1="398.6" x2="737.8" y2="422.1" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="414.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="741.8" y1="410.3" x2="741.8" y2="463.9" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="421.4" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="745.7" y1="441.5" x2="745.7" y2="469.8" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="441.6" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="749.7" y1="444.4" x2="749.7" y2="471.2" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="446.5" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="753.6" y1="442.6" x2="753.6" y2="460.9" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="453.4" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="757.6" y1="457.4" x2="757.6" y2="483.4" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="457.4" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="761.5" y1="431.7" x2="761.5" y2="467.8" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="434.9" width="2.45" height="28.8" fill="var(--up)"/>
<line x1="765.5" y1="424.2" x2="765.5" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="425.1" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="769.4" y1="398.5" x2="769.4" y2="433.2" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="422.2" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="773.4" y1="405.8" x2="773.4" y2="437.9" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="408.9" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="777.3" y1="359.2" x2="777.3" y2="403.7" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="367.5" width="2.45" height="31.4" fill="var(--up)"/>
<line x1="781.3" y1="373.6" x2="781.3" y2="424.5" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="390.4" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="785.2" y1="395.8" x2="785.2" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="397.6" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="789.2" y1="313.5" x2="789.2" y2="409.9" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="328.4" width="2.45" height="79.2" fill="var(--up)"/>
<line x1="793.1" y1="308.0" x2="793.1" y2="371.1" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="325.2" width="2.45" height="12.5" fill="var(--down)"/>
<line x1="797.1" y1="334.8" x2="797.1" y2="364.2" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="337.0" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="801.0" y1="316.8" x2="801.0" y2="355.4" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="323.2" width="2.45" height="27.8" fill="var(--up)"/>
<line x1="805.0" y1="348.2" x2="805.0" y2="379.1" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="350.0" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="808.9" y1="370.9" x2="808.9" y2="413.6" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="374.4" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="812.9" y1="395.8" x2="812.9" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="404.9" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="816.8" y1="366.0" x2="816.8" y2="405.7" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="368.4" width="2.45" height="29.1" fill="var(--up)"/>
<line x1="820.8" y1="290.2" x2="820.8" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="310.3" width="2.45" height="38.7" fill="var(--up)"/>
<line x1="824.7" y1="247.8" x2="824.7" y2="318.4" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="267.4" width="2.45" height="51.0" fill="var(--up)"/>
<line x1="828.7" y1="255.0" x2="828.7" y2="299.5" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="261.4" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="832.7" y1="238.7" x2="832.7" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="251.4" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="836.6" y1="196.5" x2="836.6" y2="257.6" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="208.5" width="2.45" height="47.7" fill="var(--up)"/>
<line x1="840.6" y1="190.2" x2="840.6" y2="238.8" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="191.1" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="844.5" y1="187.9" x2="844.5" y2="237.2" stroke="var(--down)" class="wick"/>
<rect x="843.28" y="213.0" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="848.5" y1="186.0" x2="848.5" y2="218.0" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="197.1" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="852.4" y1="176.8" x2="852.4" y2="232.3" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="206.9" width="2.45" height="19.0" fill="var(--down)"/>
<line x1="856.4" y1="214.7" x2="856.4" y2="262.5" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="236.5" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="860.3" y1="266.0" x2="860.3" y2="337.9" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="268.5" width="2.45" height="60.9" fill="var(--down)"/>
<line x1="864.3" y1="256.0" x2="864.3" y2="318.7" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="275.0" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="868.2" y1="264.6" x2="868.2" y2="361.2" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="278.6" width="2.45" height="51.7" fill="var(--down)"/>
<line x1="872.2" y1="293.5" x2="872.2" y2="332.0" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="320.7" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="876.1" y1="305.1" x2="876.1" y2="347.8" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="318.5" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="880.1" y1="298.2" x2="880.1" y2="335.0" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="319.7" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="884.0" y1="268.1" x2="884.0" y2="294.9" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="287.6" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="888.0" y1="292.2" x2="888.0" y2="337.3" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="300.7" width="2.45" height="35.2" fill="var(--down)"/>
<line x1="891.9" y1="320.8" x2="891.9" y2="350.5" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="328.3" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="895.9" y1="330.5" x2="895.9" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="331.5" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="899.8" y1="282.3" x2="899.8" y2="340.7" stroke="var(--up)" class="wick"/>
<rect x="898.62" y="315.5" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="903.8" y1="287.0" x2="903.8" y2="336.5" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="319.7" width="2.45" height="11.2" fill="var(--up)"/>
<line x1="907.7" y1="324.3" x2="907.7" y2="369.4" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="324.3" width="2.45" height="33.9" fill="var(--down)"/>
<line x1="911.7" y1="344.8" x2="911.7" y2="389.3" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="348.9" width="2.45" height="36.8" fill="var(--down)"/>
<line x1="915.6" y1="368.3" x2="915.6" y2="404.4" stroke="var(--down)" class="wick"/>
<rect x="914.42" y="393.9" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="919.6" y1="352.8" x2="919.6" y2="393.9" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="355.7" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="923.6" y1="347.0" x2="923.6" y2="369.0" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="361.3" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="927.5" y1="347.7" x2="927.5" y2="378.1" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="371.1" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="931.5" y1="351.0" x2="931.5" y2="407.2" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="380.7" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="935.4" y1="378.7" x2="935.4" y2="401.7" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="399.4" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="939.4" y1="409.3" x2="939.4" y2="444.8" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="413.0" width="2.45" height="19.7" fill="var(--down)"/>
<line x1="943.3" y1="424.9" x2="943.3" y2="447.6" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="435.3" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="947.3" y1="427.0" x2="947.3" y2="441.7" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="431.5" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="951.2" y1="431.9" x2="951.2" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="433.1" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="955.2" y1="461.5" x2="955.2" y2="493.7" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="462.5" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="959.1" y1="477.2" x2="959.1" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="957.90" y="480.9" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="963.1" y1="480.6" x2="963.1" y2="509.6" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="481.2" width="2.45" height="22.5" fill="var(--down)"/>
<line x1="967.0" y1="506.2" x2="967.0" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="508.4" width="2.45" height="17.2" fill="var(--down)"/>
<line x1="971.0" y1="518.2" x2="971.0" y2="541.9" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="526.6" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="974.9" y1="514.7" x2="974.9" y2="533.6" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="526.0" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="978.9" y1="516.8" x2="978.9" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="521.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="982.8" y1="517.5" x2="982.8" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="527.5" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="986.8" y1="521.8" x2="986.8" y2="539.5" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="534.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="990.7" y1="532.8" x2="990.7" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="534.6" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="994.7" y1="506.8" x2="994.7" y2="532.8" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="518.2" width="2.45" height="13.1" fill="var(--up)"/>
<line x1="998.6" y1="529.6" x2="998.6" y2="552.5" stroke="var(--down)" class="wick"/>
<rect x="997.42" y="533.9" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="1002.6" y1="532.6" x2="1002.6" y2="555.3" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="538.1" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="1006.5" y1="515.8" x2="1006.5" y2="544.6" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="519.5" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="1010.5" y1="502.5" x2="1010.5" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="513.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1014.5" y1="479.8" x2="1014.5" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="491.6" width="2.45" height="27.3" fill="var(--up)"/>
<line x1="1018.4" y1="462.7" x2="1018.4" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="465.7" width="2.45" height="18.9" fill="var(--up)"/>
<line x1="1022.4" y1="464.0" x2="1022.4" y2="484.0" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="472.6" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="1026.3" y1="464.2" x2="1026.3" y2="484.4" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="468.8" width="2.45" height="14.9" fill="var(--down)"/>
<line x1="1030.3" y1="439.5" x2="1030.3" y2="481.2" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="441.2" width="2.45" height="36.6" fill="var(--up)"/>
<line x1="1034.2" y1="443.2" x2="1034.2" y2="461.3" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="451.9" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="1038.2" y1="444.9" x2="1038.2" y2="461.5" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="450.1" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="1042.1" y1="431.1" x2="1042.1" y2="455.5" stroke="var(--up)" class="wick"/>
<rect x="1040.89" y="434.2" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="1046.1" y1="409.4" x2="1046.1" y2="438.4" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="436.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1050.0" y1="415.5" x2="1050.0" y2="441.8" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="424.6" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="60" y1="344.0" x2="1052" y2="344.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="347.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$55 R1</text>
<text x="1058" y="359.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="432.9" x2="1052" y2="432.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="426.9" font-size="11.5" fill="var(--support)" font-weight="600">$45 S1</text>
<text x="1058" y="438.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="571.0" x2="1052" y2="571.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="565.0" font-size="11.5" fill="var(--support)" font-weight="600">$30 S2</text>
<text x="1058" y="577.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="424.6" r="3" fill="var(--ink)"/>
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
| R1 | $55 | 3 | 2025년 10월 고점($82.09) 이후 하락 국면(11월)과 2026년 7월 재조정 국면에서 반복적으로 걸린 구간 |
| **현재가** | **$46.26** (2026-08-14 종가) | — | R1과 S1 사이, S1에 더 근접 |
| S1 | $45 | 2 | 2025년 12월~2026년 1월 저점대, 2026년 5월 저점대와 겹치는 구간 — 현재가에 가장 근접한 지지 |
| S2 | $30 | 2 | 2026년 4월 급락 구간(저점 $27.79 부근) 및 52주 최저($25.89) 인근 |
| 참고선 | $85 | — | 52주 최고($84.64, 2025-10-13 부근) — 현재가와 84% 이상 괴리돼 있어 근시일 저항으로 보지 않고 참고선으로만 표시 |

> 레벨 개수는 스크립트 기본값(3개)을 그대로 사용했다 — 최근 1년간 변동성이 매우 커(52주 고가 대비 저가가 약 -70%) 추가 클러스터를 강제로 넣지 않아도 3개 레벨이 가격대를 고르게 나눈다.

---

## 3. 관측된 특이 구간

최근 1년간 뚜렷한 단일 거래일 갭(실적 발표 직후 급등락 등)은 종가 기준으로 확인되지 않았다 — 2026-08-05 2026 Q2 실적 발표 당일은 오히려 전일 대비 -4.3%($41.72→$39.93) 하락했고, 이후 약 1주일에 걸쳐 완만하게 반등해 8/14 $46.26까지 회복했다([최근 뉴스 / 이슈](./08_news.md) 참고). 대신 **2025년 10월 중순 고점($82.09) 이후 2026년 4월 저점($27.79 부근)까지 약 6개월간 이어진 완만하지만 깊은(-66%) 조정**이 이 기간 가장 큰 가격 구조 변화다 — 특정 하루의 이벤트보다는 국면 전환에 가까워 이 절에서 개별 이벤트로 다루지 않는다. 이후 2026년 5~7월에도 $69대(6월)에서 $37대(7월)까지 재차 큰 폭의 등락이 반복돼, 이 종목은 최근 1년 내내 뉴스·실적 발표 사이클마다 변동성이 매우 큰 상태가 이어지고 있는 것으로 보인다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-15. 원주가(과거 분할은 소급 반영, 배당은 미반영) — IonQ는 상장(2021-10) 이후 분할·병합 이력이 없어 소급조정 이슈 자체가 없다.
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py IONQ --name IonQ --ref-line 84.64:"52주 최고"`. 파라미터는 기본값 그대로 사용해 회사 간 비교 가능성을 유지했다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 이 종목은 최근 1년 변동성이 극히 커(고점 대비 저점 -70%) 스윙 레벨 자체의 "지지/저항"으로서의 의미가 안정된 대형주보다 약할 수 있다 — 3. 관측된 특이 구간에서 보듯 국면 자체가 몇 달 단위로 크게 바뀌는 종목이라는 점을 감안할 것.
    - 해당 기간 주식분할·대규모 유상증자로 인한 가격 연속성 단절은 없었다(신주는 M&A 대가로 발행됐을 뿐 주가에 직접 영향을 주는 유상증자 방식은 아니었음).

---

*작성일: 2026-08-15 (최종 수정일: 2026-08-23)*
