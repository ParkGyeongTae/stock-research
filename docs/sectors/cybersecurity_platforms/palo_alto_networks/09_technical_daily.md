# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-15 종가 $375.09는 [핵심 지표 A.2 밸류에이션 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치한다.**

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-16 ~ 2026-09-15)

<style>
.panw-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .panw-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.panw-chart svg { width:100%; height:auto; display:block; }
.panw-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.panw-chart .title { fill: var(--ink); font-weight:600; }
.panw-chart .grid { stroke: var(--grid); stroke-width:1; }
.panw-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="panw-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="팔로알토 네트웍스(PANW) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">팔로알토 네트웍스 (PANW) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-16 ~ 2026-09-15 · 마지막 종가 $375.09 (2026-09-15) · 단위 USD</text>
<line x1="60" y1="585.3" x2="1052" y2="585.3" class="grid"/>
<text x="52" y="589.3" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="483.5" x2="1052" y2="483.5" class="grid"/>
<text x="52" y="487.5" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="381.7" x2="1052" y2="381.7" class="grid"/>
<text x="52" y="385.7" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="279.9" x2="1052" y2="279.9" class="grid"/>
<text x="52" y="283.9" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="178.1" x2="1052" y2="178.1" class="grid"/>
<text x="52" y="182.1" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="76.4" x2="1052" y2="76.4" class="grid"/>
<text x="52" y="80.4" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="105.5" y1="626.0" x2="105.5" y2="631.0" class="axis"/>
<text x="105.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="196.4" y1="626.0" x2="196.4" y2="631.0" class="axis"/>
<text x="196.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="271.4" y1="626.0" x2="271.4" y2="631.0" class="axis"/>
<text x="271.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="358.4" y1="626.0" x2="358.4" y2="631.0" class="axis"/>
<text x="358.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="437.4" y1="626.0" x2="437.4" y2="631.0" class="axis"/>
<text x="437.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="512.5" y1="626.0" x2="512.5" y2="631.0" class="axis"/>
<text x="512.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="599.5" y1="626.0" x2="599.5" y2="631.0" class="axis"/>
<text x="599.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="682.5" y1="626.0" x2="682.5" y2="631.0" class="axis"/>
<text x="682.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="761.5" y1="626.0" x2="761.5" y2="631.0" class="axis"/>
<text x="761.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="844.5" y1="626.0" x2="844.5" y2="631.0" class="axis"/>
<text x="844.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="931.5" y1="626.0" x2="931.5" y2="631.0" class="axis"/>
<text x="931.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1014.5" y1="626.0" x2="1014.5" y2="631.0" class="axis"/>
<text x="1014.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="78.6" x2="1052" y2="78.6" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="81.6" font-size="10.5" fill="var(--muted)">$399 52주 최고</text>
<line x1="60" y1="606.5" x2="1052" y2="606.5" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="609.5" font-size="10.5" fill="var(--muted)">$140 52주 최저</text>
<line x1="1014.5" y1="56.0" x2="1014.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="1020.5" y="68.0" font-size="10.5" fill="var(--down)">2026-09-01 FY2026 4분기 실적발표</text>
<line x1="465.1" y1="56.0" x2="465.1" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="471.1" y="68.0" font-size="10.5" fill="var(--down)">2026-02-11 CyberArk 인수 종결</text>
<line x1="62.0" y1="479.2" x2="62.0" y2="486.0" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="480.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="65.9" y1="474.3" x2="65.9" y2="482.8" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="477.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="69.9" y1="469.2" x2="69.9" y2="474.8" stroke="var(--up)" class="wick"/>
<rect x="68.66" y="471.9" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="73.8" y1="465.1" x2="73.8" y2="472.3" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="466.8" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="77.8" y1="464.1" x2="77.8" y2="472.0" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="466.8" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="81.7" y1="466.2" x2="81.7" y2="478.9" stroke="var(--down)" class="wick"/>
<rect x="80.51" y="468.9" width="2.45" height="8.0" fill="var(--down)"/>
<line x1="85.7" y1="473.3" x2="85.7" y2="483.1" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="478.1" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="89.6" y1="475.7" x2="89.6" y2="488.2" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="479.0" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="93.6" y1="476.3" x2="93.6" y2="482.2" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="478.7" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="97.5" y1="473.9" x2="97.5" y2="478.2" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="475.4" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="101.5" y1="471.1" x2="101.5" y2="479.6" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="476.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="105.5" y1="468.9" x2="105.5" y2="481.7" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="469.7" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="109.4" y1="463.3" x2="109.4" y2="472.4" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="464.6" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="113.4" y1="458.9" x2="113.4" y2="469.5" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="462.9" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="117.3" y1="455.3" x2="117.3" y2="464.9" stroke="var(--up)" class="wick"/>
<rect x="116.08" y="457.9" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="121.3" y1="455.0" x2="121.3" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="120.03" y="456.6" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="125.2" y1="447.0" x2="125.2" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="447.3" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="129.2" y1="447.4" x2="129.2" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="448.9" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="133.1" y1="448.3" x2="133.1" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="450.9" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="137.1" y1="453.5" x2="137.1" y2="459.7" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="456.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="141.0" y1="461.5" x2="141.0" y2="469.9" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="463.6" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="145.0" y1="461.9" x2="145.0" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="467.1" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="148.9" y1="462.2" x2="148.9" y2="474.1" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="467.2" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="152.9" y1="465.2" x2="152.9" y2="476.1" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="467.4" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="156.8" y1="457.8" x2="156.8" y2="464.1" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="459.4" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="160.8" y1="452.8" x2="160.8" y2="460.7" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="454.2" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="164.7" y1="452.6" x2="164.7" y2="461.1" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="455.0" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="168.7" y1="449.9" x2="168.7" y2="459.8" stroke="var(--up)" class="wick"/>
<rect x="167.46" y="452.9" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="172.6" y1="446.4" x2="172.6" y2="451.2" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="448.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="176.6" y1="440.6" x2="176.6" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="442.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="180.5" y1="435.4" x2="180.5" y2="443.4" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="440.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="184.5" y1="443.2" x2="184.5" y2="450.9" stroke="var(--down)" class="wick"/>
<rect x="183.27" y="444.2" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="188.4" y1="440.2" x2="188.4" y2="449.7" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="446.3" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="192.4" y1="440.4" x2="192.4" y2="447.4" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="442.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="196.4" y1="441.8" x2="196.4" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="195.13" y="442.8" width="2.45" height="1.5" fill="var(--down)"/>
<line x1="200.3" y1="446.9" x2="200.3" y2="458.4" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="451.5" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="204.3" y1="451.7" x2="204.3" y2="458.2" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="452.6" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="208.2" y1="456.2" x2="208.2" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="460.4" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="212.2" y1="457.8" x2="212.2" y2="467.6" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="458.5" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="216.1" y1="449.3" x2="216.1" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="214.89" y="449.8" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="220.1" y1="445.3" x2="220.1" y2="451.4" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="446.3" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="224.0" y1="442.7" x2="224.0" y2="463.7" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="446.6" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="228.0" y1="459.1" x2="228.0" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="463.5" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="231.9" y1="469.4" x2="231.9" y2="486.8" stroke="var(--up)" class="wick"/>
<rect x="230.70" y="472.8" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="235.9" y1="468.9" x2="235.9" y2="479.1" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="473.3" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="239.8" y1="475.4" x2="239.8" y2="483.9" stroke="var(--down)" class="wick"/>
<rect x="238.60" y="478.4" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="243.8" y1="478.2" x2="243.8" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="483.7" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="247.7" y1="484.1" x2="247.7" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="487.3" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="251.7" y1="510.5" x2="251.7" y2="524.1" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="514.0" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="255.6" y1="510.8" x2="255.6" y2="520.3" stroke="var(--down)" class="wick"/>
<rect x="254.41" y="513.2" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="259.6" y1="510.6" x2="259.6" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="511.5" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="263.5" y1="509.7" x2="263.5" y2="516.4" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="509.7" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="267.5" y1="502.0" x2="267.5" y2="510.1" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="503.6" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="271.4" y1="504.1" x2="271.4" y2="512.8" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="504.8" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="275.4" y1="499.6" x2="275.4" y2="507.6" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="504.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="279.3" y1="495.7" x2="279.3" y2="510.4" stroke="var(--up)" class="wick"/>
<rect x="278.12" y="496.5" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="283.3" y1="491.6" x2="283.3" y2="498.9" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="492.3" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="287.3" y1="484.0" x2="287.3" y2="493.7" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="485.9" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="291.2" y1="483.7" x2="291.2" y2="496.3" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="484.8" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="295.2" y1="490.3" x2="295.2" y2="495.3" stroke="var(--down)" class="wick"/>
<rect x="293.93" y="493.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="299.1" y1="493.7" x2="299.1" y2="499.6" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="494.8" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="303.1" y1="498.1" x2="303.1" y2="506.9" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="501.0" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="307.0" y1="496.4" x2="307.0" y2="506.8" stroke="var(--up)" class="wick"/>
<rect x="305.79" y="500.4" width="2.45" height="1.3" fill="var(--up)"/>
<line x1="311.0" y1="501.1" x2="311.0" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="501.1" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="314.9" y1="507.3" x2="314.9" y2="514.8" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="509.8" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="318.9" y1="507.3" x2="318.9" y2="517.5" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="508.9" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="322.8" y1="510.1" x2="322.8" y2="517.7" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="512.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="326.8" y1="507.4" x2="326.8" y2="511.7" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="508.2" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="330.7" y1="502.8" x2="330.7" y2="510.7" stroke="var(--up)" class="wick"/>
<rect x="329.50" y="504.9" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="334.7" y1="504.4" x2="334.7" y2="509.4" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="505.8" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="338.6" y1="508.3" x2="338.6" y2="514.5" stroke="var(--down)" class="wick"/>
<rect x="337.40" y="509.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="342.6" y1="506.7" x2="342.6" y2="511.0" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="507.0" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="346.5" y1="505.8" x2="346.5" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="507.7" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="350.5" y1="508.4" x2="350.5" y2="512.2" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="510.3" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="354.4" y1="510.2" x2="354.4" y2="515.9" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="510.6" width="2.45" height="5.1" fill="var(--down)"/>
<line x1="358.4" y1="514.4" x2="358.4" y2="529.9" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="514.4" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="362.3" y1="512.3" x2="362.3" y2="522.2" stroke="var(--down)" class="wick"/>
<rect x="361.12" y="518.1" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="366.3" y1="511.9" x2="366.3" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="512.3" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="370.2" y1="491.3" x2="370.2" y2="508.4" stroke="var(--up)" class="wick"/>
<rect x="369.02" y="495.9" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="374.2" y1="495.9" x2="374.2" y2="505.8" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="496.3" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="378.2" y1="498.9" x2="378.2" y2="509.3" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="499.9" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="382.1" y1="504.4" x2="382.1" y2="509.4" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="506.1" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="386.1" y1="497.3" x2="386.1" y2="507.9" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="502.1" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="390.0" y1="498.6" x2="390.0" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="388.78" y="502.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="394.0" y1="495.6" x2="394.0" y2="510.9" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="502.5" width="2.45" height="6.0" fill="var(--down)"/>
<line x1="397.9" y1="504.9" x2="397.9" y2="514.7" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="508.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="401.9" y1="506.9" x2="401.9" y2="519.6" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="515.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="405.8" y1="513.9" x2="405.8" y2="526.7" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="515.1" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="409.8" y1="517.9" x2="409.8" y2="522.6" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="519.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="413.7" y1="514.6" x2="413.7" y2="524.8" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="518.0" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="417.7" y1="512.8" x2="417.7" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="515.6" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="421.6" y1="505.1" x2="421.6" y2="519.1" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="509.2" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="425.6" y1="510.6" x2="425.6" y2="517.4" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="515.0" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="429.5" y1="519.7" x2="429.5" y2="542.0" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="522.0" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="433.5" y1="528.1" x2="433.5" y2="538.5" stroke="var(--up)" class="wick"/>
<rect x="432.26" y="530.4" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="437.4" y1="528.8" x2="437.4" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="529.4" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="441.4" y1="535.3" x2="441.4" y2="558.1" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="536.2" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="445.3" y1="549.5" x2="445.3" y2="566.1" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="551.2" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="449.3" y1="552.3" x2="449.3" y2="577.0" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="557.4" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="453.2" y1="565.8" x2="453.2" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="566.3" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="457.2" y1="551.2" x2="457.2" y2="572.3" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="552.7" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="461.1" y1="548.1" x2="461.1" y2="556.2" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="551.9" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="465.1" y1="548.1" x2="465.1" y2="557.8" stroke="var(--down)" class="wick"/>
<rect x="463.87" y="550.3" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="469.1" y1="548.7" x2="469.1" y2="569.4" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="552.1" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="473.0" y1="543.6" x2="473.0" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="550.8" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="477.0" y1="552.7" x2="477.0" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="553.4" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="480.9" y1="574.5" x2="480.9" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="580.5" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="484.9" y1="579.8" x2="484.9" y2="589.1" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="580.2" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="488.8" y1="568.7" x2="488.8" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="584.6" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="492.8" y1="588.1" x2="492.8" y2="598.9" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="589.9" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="496.7" y1="590.3" x2="496.7" y2="606.5" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="599.7" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="500.7" y1="594.7" x2="500.7" y2="605.0" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="595.8" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="504.6" y1="582.7" x2="504.6" y2="595.9" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="586.5" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="508.6" y1="587.3" x2="508.6" y2="598.2" stroke="var(--up)" class="wick"/>
<rect x="507.35" y="587.5" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="512.5" y1="581.5" x2="512.5" y2="593.4" stroke="var(--up)" class="wick"/>
<rect x="511.30" y="585.0" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="516.5" y1="571.4" x2="516.5" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="515.25" y="572.9" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="520.4" y1="564.3" x2="520.4" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="519.21" y="567.9" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="524.4" y1="555.4" x2="524.4" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="558.5" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="528.3" y1="554.0" x2="528.3" y2="562.3" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="554.6" width="2.45" height="5.6" fill="var(--up)"/>
<line x1="532.3" y1="549.1" x2="532.3" y2="557.8" stroke="var(--up)" class="wick"/>
<rect x="531.06" y="554.5" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="536.2" y1="550.7" x2="536.2" y2="563.2" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="553.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="540.2" y1="546.4" x2="540.2" y2="558.0" stroke="var(--down)" class="wick"/>
<rect x="538.97" y="551.4" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="544.1" y1="547.1" x2="544.1" y2="553.9" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="548.4" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="548.1" y1="542.2" x2="548.1" y2="553.1" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="546.8" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="552.0" y1="548.1" x2="552.0" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="549.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="556.0" y1="540.4" x2="556.0" y2="549.6" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="546.2" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="560.0" y1="540.9" x2="560.0" y2="549.7" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="546.8" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="563.9" y1="541.1" x2="563.9" y2="548.6" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="545.1" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="567.9" y1="546.2" x2="567.9" y2="561.1" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="546.2" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="571.8" y1="552.0" x2="571.8" y2="559.9" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="555.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="575.8" y1="559.2" x2="575.8" y2="572.8" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="560.7" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="579.7" y1="564.3" x2="579.7" y2="579.6" stroke="var(--down)" class="wick"/>
<rect x="578.49" y="565.5" width="2.45" height="13.2" fill="var(--down)"/>
<line x1="583.7" y1="566.2" x2="583.7" y2="580.8" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="572.3" width="2.45" height="8.4" fill="var(--up)"/>
<line x1="587.6" y1="586.6" x2="587.6" y2="598.5" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="590.3" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="591.6" y1="566.6" x2="591.6" y2="582.3" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="576.4" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="595.5" y1="562.6" x2="595.5" y2="575.0" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="564.3" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="599.5" y1="561.3" x2="599.5" y2="570.4" stroke="var(--down)" class="wick"/>
<rect x="598.25" y="562.0" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="603.4" y1="558.2" x2="603.4" y2="570.0" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="558.4" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="607.4" y1="556.6" x2="607.4" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="558.1" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="611.3" y1="542.6" x2="611.3" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="544.8" width="2.45" height="16.9" fill="var(--up)"/>
<line x1="615.3" y1="525.7" x2="615.3" y2="541.3" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="536.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="619.2" y1="534.4" x2="619.2" y2="556.2" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="536.1" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="623.2" y1="549.5" x2="623.2" y2="582.7" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="549.5" width="2.45" height="24.2" fill="var(--down)"/>
<line x1="627.1" y1="559.2" x2="627.1" y2="575.4" stroke="var(--up)" class="wick"/>
<rect x="625.91" y="559.8" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="631.1" y1="553.4" x2="631.1" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="558.1" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="635.0" y1="554.3" x2="635.0" y2="561.5" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="555.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="639.0" y1="544.1" x2="639.0" y2="554.8" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="547.4" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="642.9" y1="543.3" x2="642.9" y2="551.3" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="543.6" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="646.9" y1="543.5" x2="646.9" y2="554.3" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="545.5" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="650.9" y1="529.0" x2="650.9" y2="545.4" stroke="var(--up)" class="wick"/>
<rect x="649.63" y="534.5" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="654.8" y1="521.1" x2="654.8" y2="534.1" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="521.8" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="658.8" y1="533.4" x2="658.8" y2="545.4" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="537.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="662.7" y1="526.0" x2="662.7" y2="538.0" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="527.2" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="666.7" y1="516.0" x2="666.7" y2="531.3" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="518.3" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="670.6" y1="512.0" x2="670.6" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="515.8" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="674.6" y1="519.6" x2="674.6" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="673.34" y="521.1" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="678.5" y1="522.5" x2="678.5" y2="538.2" stroke="var(--down)" class="wick"/>
<rect x="677.29" y="522.5" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="682.5" y1="518.0" x2="682.5" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="520.1" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="686.4" y1="509.4" x2="686.4" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="514.9" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="690.4" y1="511.5" x2="690.4" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="512.0" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="694.3" y1="514.1" x2="694.3" y2="525.9" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="516.7" width="2.45" height="6.6" fill="var(--up)"/>
<line x1="698.3" y1="485.4" x2="698.3" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="697.05" y="490.6" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="702.2" y1="467.0" x2="702.2" y2="496.9" stroke="var(--up)" class="wick"/>
<rect x="701.01" y="467.5" width="2.45" height="26.5" fill="var(--up)"/>
<line x1="706.2" y1="454.4" x2="706.2" y2="472.0" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="455.7" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="710.1" y1="450.6" x2="710.1" y2="461.6" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="451.7" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="714.1" y1="424.8" x2="714.1" y2="461.6" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="426.9" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="718.0" y1="403.8" x2="718.0" y2="431.8" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="405.7" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="722.0" y1="390.3" x2="722.0" y2="421.9" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="396.3" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="725.9" y1="384.1" x2="725.9" y2="410.6" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="386.7" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="729.9" y1="384.6" x2="729.9" y2="402.7" stroke="var(--down)" class="wick"/>
<rect x="728.67" y="387.9" width="2.45" height="13.9" fill="var(--down)"/>
<line x1="733.8" y1="381.7" x2="733.8" y2="411.7" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="388.5" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="737.8" y1="375.4" x2="737.8" y2="400.0" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="375.8" width="2.45" height="23.6" fill="var(--up)"/>
<line x1="741.8" y1="358.5" x2="741.8" y2="382.7" stroke="var(--up)" class="wick"/>
<rect x="740.53" y="360.2" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="745.7" y1="361.7" x2="745.7" y2="380.1" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="365.1" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="749.7" y1="378.4" x2="749.7" y2="395.9" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="384.8" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="753.6" y1="363.4" x2="753.6" y2="385.0" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="365.9" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="757.6" y1="313.1" x2="757.6" y2="369.5" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="317.2" width="2.45" height="51.6" fill="var(--up)"/>
<line x1="761.5" y1="273.9" x2="761.5" y2="312.9" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="279.0" width="2.45" height="30.6" fill="var(--up)"/>
<line x1="765.5" y1="281.3" x2="765.5" y2="305.8" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="285.7" width="2.45" height="19.8" fill="var(--up)"/>
<line x1="769.4" y1="304.4" x2="769.4" y2="329.1" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="310.5" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="773.4" y1="319.2" x2="773.4" y2="343.0" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="322.2" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="777.3" y1="319.3" x2="777.3" y2="342.2" stroke="var(--down)" class="wick"/>
<rect x="776.10" y="322.7" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="781.3" y1="334.8" x2="781.3" y2="352.4" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="341.8" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="785.2" y1="348.2" x2="785.2" y2="379.4" stroke="var(--down)" class="wick"/>
<rect x="784.00" y="350.6" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="789.2" y1="347.7" x2="789.2" y2="372.7" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="354.8" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="793.1" y1="320.7" x2="793.1" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="321.6" width="2.45" height="37.7" fill="var(--up)"/>
<line x1="797.1" y1="316.6" x2="797.1" y2="338.0" stroke="var(--up)" class="wick"/>
<rect x="795.86" y="321.4" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="801.0" y1="310.2" x2="801.0" y2="332.2" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="311.4" width="2.45" height="8.1" fill="var(--up)"/>
<line x1="805.0" y1="313.2" x2="805.0" y2="330.7" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="314.1" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="808.9" y1="311.8" x2="808.9" y2="327.3" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="316.3" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="812.9" y1="302.6" x2="812.9" y2="327.8" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="304.8" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="816.8" y1="288.6" x2="816.8" y2="312.0" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="304.4" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="820.8" y1="295.9" x2="820.8" y2="315.5" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="298.4" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="824.7" y1="298.2" x2="824.7" y2="311.9" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="301.1" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="828.7" y1="289.0" x2="828.7" y2="309.9" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="294.0" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="832.7" y1="267.2" x2="832.7" y2="300.3" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="271.4" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="836.6" y1="213.0" x2="836.6" y2="269.1" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="214.8" width="2.45" height="45.1" fill="var(--up)"/>
<line x1="840.6" y1="193.5" x2="840.6" y2="224.3" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="196.4" width="2.45" height="27.4" fill="var(--up)"/>
<line x1="844.5" y1="161.7" x2="844.5" y2="196.5" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="174.0" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="848.5" y1="163.1" x2="848.5" y2="184.5" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="175.1" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="852.4" y1="141.2" x2="852.4" y2="203.2" stroke="var(--up)" class="wick"/>
<rect x="851.19" y="162.8" width="2.45" height="37.8" fill="var(--up)"/>
<line x1="856.4" y1="151.7" x2="856.4" y2="206.6" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="158.1" width="2.45" height="46.5" fill="var(--down)"/>
<line x1="860.3" y1="205.0" x2="860.3" y2="249.5" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="205.0" width="2.45" height="33.0" fill="var(--down)"/>
<line x1="864.3" y1="201.8" x2="864.3" y2="242.6" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="201.9" width="2.45" height="40.7" fill="var(--up)"/>
<line x1="868.2" y1="198.2" x2="868.2" y2="231.4" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="201.6" width="2.45" height="25.6" fill="var(--down)"/>
<line x1="872.2" y1="216.7" x2="872.2" y2="246.8" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="218.2" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="876.1" y1="170.7" x2="876.1" y2="218.3" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="172.3" width="2.45" height="45.0" fill="var(--up)"/>
<line x1="880.1" y1="152.3" x2="880.1" y2="171.8" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="164.3" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="884.0" y1="156.9" x2="884.0" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="163.8" width="2.45" height="6.2" fill="var(--down)"/>
<line x1="888.0" y1="139.9" x2="888.0" y2="188.2" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="160.5" width="2.45" height="23.8" fill="var(--up)"/>
<line x1="891.9" y1="144.9" x2="891.9" y2="181.5" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="168.5" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="895.9" y1="174.1" x2="895.9" y2="210.7" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="179.3" width="2.45" height="14.8" fill="var(--down)"/>
<line x1="899.8" y1="190.0" x2="899.8" y2="221.6" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="192.4" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="903.8" y1="205.5" x2="903.8" y2="235.4" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="207.5" width="2.45" height="20.3" fill="var(--down)"/>
<line x1="907.7" y1="218.9" x2="907.7" y2="235.8" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="222.7" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="911.7" y1="215.2" x2="911.7" y2="245.9" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="215.8" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="915.6" y1="232.3" x2="915.6" y2="262.5" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="241.2" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="919.6" y1="234.9" x2="919.6" y2="258.6" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="240.5" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="923.6" y1="226.4" x2="923.6" y2="253.4" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="227.7" width="2.45" height="19.6" fill="var(--up)"/>
<line x1="927.5" y1="210.8" x2="927.5" y2="240.3" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="214.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="931.5" y1="182.8" x2="931.5" y2="218.9" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="184.0" width="2.45" height="21.7" fill="var(--up)"/>
<line x1="935.4" y1="142.5" x2="935.4" y2="180.0" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="144.9" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="939.4" y1="123.2" x2="939.4" y2="153.3" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="129.6" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="943.3" y1="154.8" x2="943.3" y2="180.2" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="158.8" width="2.45" height="19.1" fill="var(--up)"/>
<line x1="947.3" y1="136.4" x2="947.3" y2="159.5" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="146.6" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="951.2" y1="106.5" x2="951.2" y2="151.8" stroke="var(--up)" class="wick"/>
<rect x="949.99" y="106.8" width="2.45" height="40.0" fill="var(--up)"/>
<line x1="955.2" y1="102.4" x2="955.2" y2="125.4" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="108.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="959.1" y1="98.2" x2="959.1" y2="124.8" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="102.8" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="963.1" y1="78.6" x2="963.1" y2="102.1" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="84.5" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="967.0" y1="81.8" x2="967.0" y2="115.3" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="83.0" width="2.45" height="25.4" fill="var(--down)"/>
<line x1="971.0" y1="104.9" x2="971.0" y2="132.7" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="110.5" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="974.9" y1="121.1" x2="974.9" y2="141.5" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="129.0" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="978.9" y1="124.3" x2="978.9" y2="175.2" stroke="var(--down)" class="wick"/>
<rect x="977.66" y="126.7" width="2.45" height="31.6" fill="var(--down)"/>
<line x1="982.8" y1="156.4" x2="982.8" y2="182.9" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="169.8" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="986.8" y1="156.8" x2="986.8" y2="192.4" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="162.1" width="2.45" height="11.1" fill="var(--up)"/>
<line x1="990.7" y1="162.1" x2="990.7" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="165.8" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="994.7" y1="170.5" x2="994.7" y2="207.6" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="170.5" width="2.45" height="28.2" fill="var(--down)"/>
<line x1="998.6" y1="193.9" x2="998.6" y2="222.9" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="199.9" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="1002.6" y1="102.1" x2="1002.6" y2="164.6" stroke="var(--up)" class="wick"/>
<rect x="1001.37" y="111.3" width="2.45" height="49.4" fill="var(--up)"/>
<line x1="1006.5" y1="120.1" x2="1006.5" y2="166.9" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="122.6" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="1010.5" y1="109.5" x2="1010.5" y2="137.4" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="112.7" width="2.45" height="24.7" fill="var(--up)"/>
<line x1="1014.5" y1="125.4" x2="1014.5" y2="163.4" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="128.0" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="1018.4" y1="176.8" x2="1018.4" y2="236.4" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="186.3" width="2.45" height="35.7" fill="var(--down)"/>
<line x1="1022.4" y1="212.1" x2="1022.4" y2="236.3" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="212.1" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="1026.3" y1="200.3" x2="1026.3" y2="222.9" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="212.2" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="1030.3" y1="199.7" x2="1030.3" y2="228.4" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="204.6" width="2.45" height="19.2" fill="var(--up)"/>
<line x1="1034.2" y1="198.8" x2="1034.2" y2="213.7" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="202.8" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="1038.2" y1="188.7" x2="1038.2" y2="218.2" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="201.6" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="1042.1" y1="196.2" x2="1042.1" y2="224.9" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="201.6" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="1046.1" y1="119.9" x2="1046.1" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="129.4" width="2.45" height="55.9" fill="var(--up)"/>
<line x1="1050.0" y1="116.2" x2="1050.0" y2="143.9" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="127.1" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="60" y1="256.0" x2="1052" y2="256.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="250.0" font-size="11.5" fill="var(--support)" font-weight="600">$312 S1</text>
<text x="1058" y="262.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="524.6" x2="1052" y2="524.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="518.6" font-size="11.5" fill="var(--support)" font-weight="600">$180 S2</text>
<text x="1058" y="530.6" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="582.2" x2="1052" y2="582.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="576.2" font-size="11.5" fill="var(--support)" font-weight="600">$151 S3</text>
<text x="1058" y="588.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="127.1" r="3" fill="var(--ink)"/>
<text x="1046.0" y="119.1" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $375 (2026-09-15)</text>
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
| **현재가** | **$375.09** (2026-09-15 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $312 | 2 | 2026-07-08·2026-07-28 — 2026년 여름 급등 구간의 눌림목 두 차례 |
| S2 | $180 | 4 | 2025-11-21·2025-12-18·2026-01-02·2026-01-21 — 2025년 말~2026년 초 두 달간의 박스권 하단(터치 4회로 이 표에서 가장 두껍다) |
| S3 | $151 | 2 | 2026-02-06·2026-04-10 — CyberArk 인수 종결(2026-02-11) 전후 조정 구간의 저점대 |
| 참고선 | $399 | — | 52주 최고 — 52주 최고 — 2026년 여름 고점. 현재가($375.09)와 6% 차이라 근시일 저항으로 볼 수도 있으나, **터치가 1회뿐이라 클러스터로 잡히지 않았다** |
| 참고선 | $140 | — | 52주 최저 — 52주 최저 — 2026년 봄 저점. 현재가 대비 63% 아래라 근시일 지지로 기능할 구간이 아니다 |

**저항선이 하나도 잡히지 않았다** — 현재가가 최근 1년 구간의 최고가 부근이라 위쪽에 스윙 고점 클러스터가 형성될 자리가 없기 때문이다. 이 표를 "저항이 없으니 더 오른다"로 읽어서는 안 되며, **참조할 가격 기억이 없는 구간**이라는 뜻으로만 읽는다.

지지 레벨의 간격이 매우 넓다는 점도 함께 봐야 한다. 현재가 $375.09에서 가장 가까운 S1이 $312로 **17% 아래**이고, 그다음 S2는 $180으로 **52% 아래**다. 2026년 봄~여름의 상승이 워낙 가팔라 중간 가격대에 거래가 쌓이지 않은 결과다.

---

## 3. 관측된 특이 구간 — 2026-09-02 FY2026 4분기 실적발표 갭다운

- 2026-09-01 장 마감 후 FY2026 4분기·연간 실적을 발표했다([최근 뉴스 / 이슈](./08_news.md) 로그 참고). 매출 $3.41B(+34%)·NGS ARR $9.10B(+63%)로 시장 기대를 웃돌았으나, 함께 제시한 FY2027 Non-GAAP EPS 가이던스가 +8.9% 성장에 그쳤다.
- 종가 기준 전일 대비 **-9.3%** ($362.09 → $328.48). 실적 자체가 아니라 **이익 성장 가이던스**에 반응한 하락이라는 점이 이 갭의 성격이다.
- 이후 9거래일 만에 $375.09까지 회복해 갭을 모두 되돌렸다. 즉 **가격 기억이 남을 만큼 오래 머문 구간이 아니어서 이 레벨($328~362)은 지지/저항 클러스터로 잡히지 않았다.**

또 하나 짚어둘 구간은 **2026년 2월**이다. CyberArk 인수가 종결된 주(2026-02-09 주간 종가 $166.95 → 2026-02-16 주간 종가 $148.70, **-10.9%**)에 주가가 크게 밀렸고, 그 부근이 S3($151) 클러스터를 형성했다. 그 뒤 약 반년 만에 $375까지 올랐으므로, **시장이 이 인수에 대한 평가를 단기간에 정반대로 바꿨다**는 사실이 이 차트에 남아 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-09-16~2026-09-15. 수집 시점: 2026-09-16. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py PANW --name "팔로알토 네트웍스" --event 2026-09-01:"FY2026 4분기 실적발표" --event 2026-02-11:"CyberArk 인수 종결" --ref-line 398.88:"52주 최고" --ref-line 139.57:"52주 최저" --close-on 2026-09-15 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **이 기간의 지지 레벨은 신뢰도가 낮다.** 최근 1년 저점 $139.57에서 고점 $398.88까지 186% 오른 구간이라 가격대별 거래 축적이 얕고, S1($312)조차 터치가 2회뿐이다.
    - **주식분할**: 최근 1년 구간에는 분할이 없다. 다만 [핵심 지표](./04_metrics.md)가 다루는 재무 기간에는 2024-12-16 2:1 분할이 있으며, 이 차트의 가격은 Yahoo Finance가 소급 조정한 값이므로 분할 후 기준으로 연속적이다.

---

*작성일: 2026-09-16*
