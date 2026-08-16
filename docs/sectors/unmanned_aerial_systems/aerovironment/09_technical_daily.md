# AeroVironment, Inc. (에어로바이런먼트) — 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [`10_technical_weekly.md`](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `04_metrics.md`의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API(Yahoo Finance)에서 직접 수집한 것이다(1년 일봉은 `04_metrics.md`가 다루는 범위 밖이라 단일 출처 규칙의 예외). 대신 겹치는 시점의 종가를 대조한 결과: `2026-04-30`(FY2026 회계연도 말) 종가 $195.02는 [`04_metrics.md`](./04_metrics.md) A.2·[`06_valuation.md`](./06_valuation.md) §2에 인용된 값과 **일치**한다. 이 문서의 최신 종가($192.81, 2026-08-14)는 `01_overview.md`·`06_valuation.md`가 인용하는 기준일(2026-08-13, $189.43)보다 하루 늦은 시점의 값으로, 하루 사이 +1.78% 상승한 결과다 — 오차가 아니라 수집 시점 차이임을 밝혀둔다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="avav-chart">
<style>
.avav-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .avav-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .avav-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.avav-chart svg { width:100%; height:auto; display:block; }
.avav-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.avav-chart .title { fill: var(--ink); font-weight:600; }
.avav-chart .grid { stroke: var(--grid); stroke-width:1; }
.avav-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="AeroVironment(AVAV) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">AeroVironment (AVAV) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $192.81 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="579.3" x2="1052" y2="579.3" class="grid"/>
<text x="52" y="583.3" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="485.8" x2="1052" y2="485.8" class="grid"/>
<text x="52" y="489.8" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="392.4" x2="1052" y2="392.4" class="grid"/>
<text x="52" y="396.4" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="299.0" x2="1052" y2="299.0" class="grid"/>
<text x="52" y="303.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="205.5" x2="1052" y2="205.5" class="grid"/>
<text x="52" y="209.5" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="112.1" x2="1052" y2="112.1" class="grid"/>
<text x="52" y="116.1" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
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
<line x1="623.2" y1="56.0" x2="623.2" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="629.2" y="68.0" font-size="10.5" fill="var(--down)">2026-03-11 FY2026 3분기 실적·Space 손상 최초 발표 충격</text>
<line x1="899.8" y1="56.0" x2="899.8" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="905.8" y="68.0" font-size="10.5" fill="var(--down)">2026-06-22 10-Q/A 재작성·내부통제 취약점 공시</text>
<line x1="923.6" y1="56.0" x2="923.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="929.6" y="68.0" font-size="10.5" fill="var(--down)">2026-06-30 FY2026 4분기 실적 서프라이즈(매출 +133%)</text>
<line x1="62.0" y1="394.1" x2="62.0" y2="410.1" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="394.1" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="65.9" y1="391.6" x2="65.9" y2="402.4" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="397.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="69.9" y1="384.9" x2="69.9" y2="423.5" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="386.8" width="2.45" height="33.3" fill="var(--down)"/>
<line x1="73.8" y1="417.1" x2="73.8" y2="434.3" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="424.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="77.8" y1="419.7" x2="77.8" y2="428.0" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="420.3" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="81.7" y1="402.3" x2="81.7" y2="422.4" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="411.4" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="85.7" y1="396.5" x2="85.7" y2="411.1" stroke="var(--up)" class="wick"/>
<rect x="84.46" y="408.9" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="89.6" y1="392.6" x2="89.6" y2="408.9" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="400.1" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="93.6" y1="390.9" x2="93.6" y2="405.1" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="397.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="97.5" y1="390.7" x2="97.5" y2="398.0" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="394.4" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="101.5" y1="385.5" x2="101.5" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="386.5" width="2.45" height="22.0" fill="var(--down)"/>
<line x1="105.5" y1="409.1" x2="105.5" y2="426.0" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="411.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="109.4" y1="401.7" x2="109.4" y2="415.8" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="406.2" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="113.4" y1="414.6" x2="113.4" y2="446.5" stroke="var(--down)" class="wick"/>
<rect x="112.13" y="415.8" width="2.45" height="20.0" fill="var(--down)"/>
<line x1="117.3" y1="425.5" x2="117.3" y2="446.8" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="427.9" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="121.3" y1="412.3" x2="121.3" y2="430.6" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="416.9" width="2.45" height="13.0" fill="var(--up)"/>
<line x1="125.2" y1="417.5" x2="125.2" y2="429.4" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="420.0" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="129.2" y1="397.5" x2="129.2" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="127.94" y="397.9" width="2.45" height="28.1" fill="var(--up)"/>
<line x1="133.1" y1="379.2" x2="133.1" y2="409.0" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="407.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="137.1" y1="390.8" x2="137.1" y2="407.3" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="401.5" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="141.0" y1="389.1" x2="141.0" y2="404.7" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="390.4" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="145.0" y1="361.7" x2="145.0" y2="386.5" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="362.7" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="148.9" y1="346.6" x2="148.9" y2="369.2" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="351.1" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="152.9" y1="321.4" x2="152.9" y2="344.2" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="329.9" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="156.8" y1="318.8" x2="156.8" y2="340.2" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="329.6" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="160.8" y1="318.6" x2="160.8" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="321.2" width="2.45" height="18.3" fill="var(--up)"/>
<line x1="164.7" y1="296.9" x2="164.7" y2="314.3" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="301.5" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="168.7" y1="285.7" x2="168.7" y2="303.7" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="295.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="172.6" y1="294.3" x2="172.6" y2="339.9" stroke="var(--up)" class="wick"/>
<rect x="171.41" y="295.6" width="2.45" height="16.3" fill="var(--up)"/>
<line x1="176.6" y1="289.6" x2="176.6" y2="310.2" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="292.7" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="180.5" y1="267.0" x2="180.5" y2="289.0" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="279.5" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="184.5" y1="267.9" x2="184.5" y2="292.0" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="271.1" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="188.4" y1="212.5" x2="188.4" y2="265.3" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="212.8" width="2.45" height="52.2" fill="var(--up)"/>
<line x1="192.4" y1="179.8" x2="192.4" y2="206.1" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="186.3" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="196.4" y1="142.3" x2="196.4" y2="174.1" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="159.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="200.3" y1="125.5" x2="200.3" y2="162.5" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="127.2" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="204.3" y1="112.0" x2="204.3" y2="138.2" stroke="var(--up)" class="wick"/>
<rect x="203.03" y="121.2" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="208.2" y1="92.0" x2="208.2" y2="130.8" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="98.0" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="212.2" y1="78.7" x2="212.2" y2="119.5" stroke="var(--down)" class="wick"/>
<rect x="210.93" y="96.8" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="216.1" y1="95.3" x2="216.1" y2="130.5" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="116.1" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="220.1" y1="91.5" x2="220.1" y2="147.6" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="93.7" width="2.45" height="32.8" fill="var(--up)"/>
<line x1="224.0" y1="91.2" x2="224.0" y2="127.8" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="109.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="228.0" y1="94.0" x2="228.0" y2="155.0" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="100.9" width="2.45" height="39.8" fill="var(--down)"/>
<line x1="231.9" y1="135.9" x2="231.9" y2="170.8" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="140.1" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="235.9" y1="170.5" x2="235.9" y2="207.2" stroke="var(--down)" class="wick"/>
<rect x="234.65" y="178.4" width="2.45" height="26.0" fill="var(--down)"/>
<line x1="239.8" y1="175.3" x2="239.8" y2="196.2" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="179.3" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="243.8" y1="150.1" x2="243.8" y2="184.7" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="154.7" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="247.7" y1="152.6" x2="247.7" y2="214.3" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="161.5" width="2.45" height="34.4" fill="var(--down)"/>
<line x1="251.7" y1="166.3" x2="251.7" y2="186.9" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="174.7" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="255.6" y1="149.1" x2="255.6" y2="178.7" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="152.2" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="259.6" y1="128.6" x2="259.6" y2="158.8" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="133.1" width="2.45" height="16.1" fill="var(--down)"/>
<line x1="263.5" y1="136.7" x2="263.5" y2="151.2" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="140.3" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="267.5" y1="123.2" x2="267.5" y2="158.8" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="141.3" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="271.4" y1="151.3" x2="271.4" y2="181.2" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="157.2" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="275.4" y1="157.3" x2="275.4" y2="188.5" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="164.0" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="279.3" y1="149.4" x2="279.3" y2="181.0" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="157.9" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="283.3" y1="172.0" x2="283.3" y2="209.4" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="177.3" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="287.3" y1="183.9" x2="287.3" y2="213.4" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="192.4" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="291.2" y1="204.0" x2="291.2" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="204.0" width="2.45" height="42.2" fill="var(--down)"/>
<line x1="295.2" y1="238.8" x2="295.2" y2="285.3" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="243.5" width="2.45" height="18.2" fill="var(--up)"/>
<line x1="299.1" y1="222.0" x2="299.1" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="227.3" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="303.1" y1="237.1" x2="303.1" y2="254.0" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="244.4" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="307.0" y1="234.4" x2="307.0" y2="261.5" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="246.4" width="2.45" height="8.9" fill="var(--down)"/>
<line x1="311.0" y1="265.3" x2="311.0" y2="311.2" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="267.3" width="2.45" height="40.1" fill="var(--down)"/>
<line x1="314.9" y1="299.5" x2="314.9" y2="336.3" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="315.4" width="2.45" height="20.9" fill="var(--up)"/>
<line x1="318.9" y1="313.2" x2="318.9" y2="338.8" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="315.7" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="322.8" y1="321.2" x2="322.8" y2="344.5" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="328.9" width="2.45" height="5.7" fill="var(--down)"/>
<line x1="326.8" y1="324.7" x2="326.8" y2="342.3" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="335.5" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="330.7" y1="307.2" x2="330.7" y2="353.2" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="309.4" width="2.45" height="38.2" fill="var(--down)"/>
<line x1="334.7" y1="348.4" x2="334.7" y2="373.2" stroke="var(--up)" class="wick"/>
<rect x="333.45" y="350.3" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="338.6" y1="332.5" x2="338.6" y2="350.9" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="342.0" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="342.6" y1="336.3" x2="342.6" y2="355.6" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="339.2" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="346.5" y1="328.9" x2="346.5" y2="348.4" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="329.7" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="350.5" y1="328.9" x2="350.5" y2="340.7" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="329.0" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="354.4" y1="345.3" x2="354.4" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="345.7" width="2.45" height="32.1" fill="var(--down)"/>
<line x1="358.4" y1="361.8" x2="358.4" y2="377.8" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="364.5" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="362.3" y1="350.5" x2="362.3" y2="371.4" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="351.7" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="366.3" y1="312.5" x2="366.3" y2="356.0" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="322.4" width="2.45" height="28.9" fill="var(--up)"/>
<line x1="370.2" y1="322.4" x2="370.2" y2="348.7" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="323.6" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="374.2" y1="326.0" x2="374.2" y2="344.1" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="331.7" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="378.2" y1="314.8" x2="378.2" y2="339.1" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="324.9" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="382.1" y1="355.5" x2="382.1" y2="405.8" stroke="var(--down)" class="wick"/>
<rect x="380.88" y="365.8" width="2.45" height="35.5" fill="var(--down)"/>
<line x1="386.1" y1="387.2" x2="386.1" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="392.9" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="390.0" y1="393.8" x2="390.0" y2="420.2" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="397.5" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="394.0" y1="405.1" x2="394.0" y2="427.7" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="410.1" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="397.9" y1="415.4" x2="397.9" y2="426.1" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="421.1" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="401.9" y1="410.5" x2="401.9" y2="434.5" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="420.4" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="405.8" y1="414.4" x2="405.8" y2="428.6" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="423.7" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="409.8" y1="401.5" x2="409.8" y2="425.8" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="405.5" width="2.45" height="20.3" fill="var(--up)"/>
<line x1="413.7" y1="377.5" x2="413.7" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="382.3" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="417.7" y1="367.4" x2="417.7" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="371.6" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="421.6" y1="368.1" x2="421.6" y2="381.2" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="371.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="425.6" y1="370.3" x2="425.6" y2="387.7" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="370.3" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="429.5" y1="383.0" x2="429.5" y2="396.8" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="388.9" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="433.5" y1="389.0" x2="433.5" y2="406.2" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="390.7" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="437.4" y1="402.5" x2="437.4" y2="411.5" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="402.5" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="441.4" y1="377.6" x2="441.4" y2="408.0" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="380.8" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="445.3" y1="294.3" x2="445.3" y2="358.8" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="303.8" width="2.45" height="53.9" fill="var(--up)"/>
<line x1="449.3" y1="264.9" x2="449.3" y2="303.8" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="267.1" width="2.45" height="36.0" fill="var(--up)"/>
<line x1="453.2" y1="237.3" x2="453.2" y2="272.1" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="263.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="457.2" y1="165.5" x2="457.2" y2="233.5" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="205.5" width="2.45" height="9.4" fill="var(--down)"/>
<line x1="461.1" y1="167.2" x2="461.1" y2="213.0" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="177.5" width="2.45" height="26.0" fill="var(--up)"/>
<line x1="465.1" y1="159.7" x2="465.1" y2="183.6" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="166.9" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="469.1" y1="158.8" x2="469.1" y2="201.7" stroke="var(--down)" class="wick"/>
<rect x="467.83" y="159.7" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="473.0" y1="144.4" x2="473.0" y2="212.1" stroke="var(--up)" class="wick"/>
<rect x="471.78" y="146.1" width="2.45" height="44.6" fill="var(--up)"/>
<line x1="477.0" y1="142.8" x2="477.0" y2="175.9" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="152.1" width="2.45" height="1.8" fill="var(--up)"/>
<line x1="480.9" y1="96.6" x2="480.9" y2="147.6" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="125.4" width="2.45" height="19.8" fill="var(--up)"/>
<line x1="484.9" y1="130.7" x2="484.9" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="168.1" width="2.45" height="73.1" fill="var(--down)"/>
<line x1="488.8" y1="212.8" x2="488.8" y2="295.2" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="212.8" width="2.45" height="49.5" fill="var(--down)"/>
<line x1="492.8" y1="249.5" x2="492.8" y2="283.0" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="254.5" width="2.45" height="21.8" fill="var(--down)"/>
<line x1="496.7" y1="271.4" x2="496.7" y2="299.0" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="273.7" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="500.7" y1="280.4" x2="500.7" y2="301.7" stroke="var(--down)" class="wick"/>
<rect x="499.44" y="285.7" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="504.6" y1="277.1" x2="504.6" y2="300.8" stroke="var(--up)" class="wick"/>
<rect x="503.40" y="281.1" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="508.6" y1="259.6" x2="508.6" y2="298.5" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="268.5" width="2.45" height="17.5" fill="var(--down)"/>
<line x1="512.5" y1="287.7" x2="512.5" y2="320.8" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="289.2" width="2.45" height="22.4" fill="var(--down)"/>
<line x1="516.5" y1="312.6" x2="516.5" y2="342.4" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="321.7" width="2.45" height="17.7" fill="var(--down)"/>
<line x1="520.4" y1="341.9" x2="520.4" y2="363.4" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="351.3" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="524.4" y1="325.9" x2="524.4" y2="354.9" stroke="var(--up)" class="wick"/>
<rect x="523.16" y="326.2" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="528.3" y1="322.4" x2="528.3" y2="399.8" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="325.1" width="2.45" height="53.6" fill="var(--down)"/>
<line x1="532.3" y1="377.5" x2="532.3" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="397.8" width="2.45" height="19.2" fill="var(--down)"/>
<line x1="536.2" y1="376.0" x2="536.2" y2="407.3" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="378.9" width="2.45" height="19.5" fill="var(--up)"/>
<line x1="540.2" y1="345.7" x2="540.2" y2="386.8" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="346.9" width="2.45" height="33.1" fill="var(--up)"/>
<line x1="544.1" y1="340.2" x2="544.1" y2="370.9" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="345.9" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="548.1" y1="359.0" x2="548.1" y2="417.9" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="359.3" width="2.45" height="45.4" fill="var(--down)"/>
<line x1="552.0" y1="388.6" x2="552.0" y2="422.7" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="388.6" width="2.45" height="31.6" fill="var(--down)"/>
<line x1="556.0" y1="395.0" x2="556.0" y2="422.3" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="403.8" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="560.0" y1="362.1" x2="560.0" y2="388.1" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="368.1" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="563.9" y1="356.3" x2="563.9" y2="375.8" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="363.5" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="567.9" y1="325.5" x2="567.9" y2="364.7" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="333.2" width="2.45" height="22.4" fill="var(--up)"/>
<line x1="571.8" y1="327.0" x2="571.8" y2="366.3" stroke="var(--down)" class="wick"/>
<rect x="570.58" y="334.8" width="2.45" height="30.3" fill="var(--down)"/>
<line x1="575.8" y1="359.7" x2="575.8" y2="383.0" stroke="var(--up)" class="wick"/>
<rect x="574.54" y="371.2" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="579.7" y1="362.7" x2="579.7" y2="399.6" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="369.5" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="583.7" y1="364.4" x2="583.7" y2="383.9" stroke="var(--down)" class="wick"/>
<rect x="582.44" y="364.6" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="587.6" y1="371.4" x2="587.6" y2="391.1" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="374.4" width="2.45" height="4.9" fill="var(--up)"/>
<line x1="591.6" y1="384.8" x2="591.6" y2="405.5" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="388.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="595.5" y1="293.3" x2="595.5" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="594.30" y="328.4" width="2.45" height="141.9" fill="var(--down)"/>
<line x1="599.5" y1="416.7" x2="599.5" y2="465.2" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="432.9" width="2.45" height="25.5" fill="var(--up)"/>
<line x1="603.4" y1="427.3" x2="603.4" y2="445.7" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="436.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="607.4" y1="419.9" x2="607.4" y2="461.5" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="426.1" width="2.45" height="21.3" fill="var(--down)"/>
<line x1="611.3" y1="418.6" x2="611.3" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="430.1" width="2.45" height="28.4" fill="var(--up)"/>
<line x1="615.3" y1="430.7" x2="615.3" y2="454.9" stroke="var(--down)" class="wick"/>
<rect x="614.06" y="430.7" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="619.2" y1="432.8" x2="619.2" y2="446.8" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="439.7" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="623.2" y1="460.5" x2="623.2" y2="487.0" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="471.4" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="627.1" y1="449.4" x2="627.1" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="462.1" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="631.1" y1="447.1" x2="631.1" y2="473.4" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="461.4" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="635.0" y1="455.9" x2="635.0" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="633.82" y="462.4" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="639.0" y1="443.5" x2="639.0" y2="466.0" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="443.8" width="2.45" height="18.0" fill="var(--up)"/>
<line x1="642.9" y1="444.7" x2="642.9" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="448.5" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="646.9" y1="459.7" x2="646.9" y2="476.5" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="464.6" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="650.9" y1="467.7" x2="650.9" y2="497.9" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="472.0" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="654.8" y1="464.3" x2="654.8" y2="491.9" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="474.1" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="658.8" y1="476.2" x2="658.8" y2="495.6" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="478.4" width="2.45" height="14.6" fill="var(--down)"/>
<line x1="662.7" y1="477.2" x2="662.7" y2="488.9" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="484.8" width="2.45" height="2.9" fill="var(--down)"/>
<line x1="666.7" y1="485.3" x2="666.7" y2="497.6" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="493.5" width="2.45" height="1.6" fill="var(--up)"/>
<line x1="670.6" y1="497.2" x2="670.6" y2="516.0" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="500.5" width="2.45" height="14.4" fill="var(--down)"/>
<line x1="674.6" y1="511.2" x2="674.6" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="511.2" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="678.5" y1="513.9" x2="678.5" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="517.5" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="682.5" y1="501.2" x2="682.5" y2="518.6" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="507.1" width="2.45" height="9.6" fill="var(--down)"/>
<line x1="686.4" y1="511.6" x2="686.4" y2="530.1" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="515.1" width="2.45" height="14.5" fill="var(--up)"/>
<line x1="690.4" y1="501.3" x2="690.4" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="505.9" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="694.3" y1="508.7" x2="694.3" y2="520.7" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="510.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="698.3" y1="491.4" x2="698.3" y2="516.0" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="495.9" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="702.2" y1="509.2" x2="702.2" y2="530.9" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="509.2" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="706.2" y1="519.4" x2="706.2" y2="533.1" stroke="var(--up)" class="wick"/>
<rect x="704.96" y="523.7" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="710.1" y1="495.5" x2="710.1" y2="528.8" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="496.3" width="2.45" height="32.5" fill="var(--up)"/>
<line x1="714.1" y1="482.1" x2="714.1" y2="499.8" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="487.7" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="718.0" y1="485.4" x2="718.0" y2="496.7" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="488.8" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="722.0" y1="472.3" x2="722.0" y2="490.1" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="479.7" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="725.9" y1="469.7" x2="725.9" y2="511.7" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="477.1" width="2.45" height="24.8" fill="var(--down)"/>
<line x1="729.9" y1="488.5" x2="729.9" y2="505.5" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="491.0" width="2.45" height="12.0" fill="var(--up)"/>
<line x1="733.8" y1="444.0" x2="733.8" y2="483.6" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="467.0" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="737.8" y1="450.0" x2="737.8" y2="474.1" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="454.5" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="741.8" y1="468.3" x2="741.8" y2="491.9" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="471.1" width="2.45" height="11.2" fill="var(--down)"/>
<line x1="745.7" y1="478.7" x2="745.7" y2="494.6" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="478.8" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="749.7" y1="484.2" x2="749.7" y2="497.7" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="493.8" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="753.6" y1="498.9" x2="753.6" y2="512.9" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="498.9" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="757.6" y1="501.3" x2="757.6" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="501.4" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="761.5" y1="494.2" x2="761.5" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="495.1" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="765.5" y1="493.6" x2="765.5" y2="515.7" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="495.1" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="769.4" y1="512.5" x2="769.4" y2="527.6" stroke="var(--down)" class="wick"/>
<rect x="768.19" y="512.5" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="773.4" y1="518.5" x2="773.4" y2="548.4" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="519.4" width="2.45" height="28.7" fill="var(--down)"/>
<line x1="777.3" y1="527.0" x2="777.3" y2="549.3" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="533.7" width="2.45" height="14.0" fill="var(--up)"/>
<line x1="781.3" y1="533.9" x2="781.3" y2="550.3" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="533.9" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="785.2" y1="542.1" x2="785.2" y2="552.0" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="545.1" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="789.2" y1="545.0" x2="789.2" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="548.5" width="2.45" height="3.2" fill="var(--up)"/>
<line x1="793.1" y1="535.4" x2="793.1" y2="552.2" stroke="var(--up)" class="wick"/>
<rect x="791.91" y="544.0" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="797.1" y1="548.6" x2="797.1" y2="568.1" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="548.6" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="801.0" y1="547.5" x2="801.0" y2="560.6" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="550.7" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="805.0" y1="554.8" x2="805.0" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="556.3" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="808.9" y1="552.5" x2="808.9" y2="564.2" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="557.7" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="812.9" y1="556.8" x2="812.9" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="558.7" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="816.8" y1="552.4" x2="816.8" y2="565.7" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="553.4" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="820.8" y1="550.7" x2="820.8" y2="562.7" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="554.8" width="2.45" height="3.9" fill="var(--up)"/>
<line x1="824.7" y1="533.5" x2="824.7" y2="552.9" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="534.0" width="2.45" height="18.8" fill="var(--up)"/>
<line x1="828.7" y1="509.2" x2="828.7" y2="531.6" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="518.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="832.7" y1="517.6" x2="832.7" y2="531.5" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="518.5" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="836.6" y1="452.6" x2="836.6" y2="494.2" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="458.9" width="2.45" height="27.0" fill="var(--up)"/>
<line x1="840.6" y1="455.4" x2="840.6" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="455.8" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="844.5" y1="469.1" x2="844.5" y2="489.3" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="478.2" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="848.5" y1="477.4" x2="848.5" y2="492.2" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="477.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="852.4" y1="483.0" x2="852.4" y2="506.2" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="483.0" width="2.45" height="18.8" fill="var(--down)"/>
<line x1="856.4" y1="475.5" x2="856.4" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="477.6" width="2.45" height="25.1" fill="var(--up)"/>
<line x1="860.3" y1="484.2" x2="860.3" y2="521.0" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="487.2" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="864.3" y1="504.1" x2="864.3" y2="515.9" stroke="var(--down)" class="wick"/>
<rect x="863.05" y="510.1" width="2.45" height="4.4" fill="var(--down)"/>
<line x1="868.2" y1="510.4" x2="868.2" y2="543.8" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="515.7" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="872.2" y1="527.9" x2="872.2" y2="538.2" stroke="var(--down)" class="wick"/>
<rect x="870.95" y="534.6" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="876.1" y1="514.7" x2="876.1" y2="541.7" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="516.3" width="2.45" height="21.5" fill="var(--up)"/>
<line x1="880.1" y1="516.4" x2="880.1" y2="541.6" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="516.4" width="2.45" height="24.4" fill="var(--down)"/>
<line x1="884.0" y1="530.7" x2="884.0" y2="543.0" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="533.7" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="888.0" y1="538.9" x2="888.0" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="541.3" width="2.45" height="6.8" fill="var(--down)"/>
<line x1="891.9" y1="537.9" x2="891.9" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="547.3" width="2.45" height="2.1" fill="var(--up)"/>
<line x1="895.9" y1="536.3" x2="895.9" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="540.4" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="899.8" y1="553.4" x2="899.8" y2="578.6" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="559.2" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="903.8" y1="575.9" x2="903.8" y2="583.5" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="581.0" width="2.45" height="2.0" fill="var(--up)"/>
<line x1="907.7" y1="581.8" x2="907.7" y2="594.7" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="583.4" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="911.7" y1="595.9" x2="911.7" y2="606.9" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="595.9" width="2.45" height="8.3" fill="var(--down)"/>
<line x1="915.6" y1="591.7" x2="915.6" y2="606.0" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="601.8" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="919.6" y1="585.0" x2="919.6" y2="599.8" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="591.2" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="923.6" y1="526.0" x2="923.6" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="529.8" width="2.45" height="21.4" fill="var(--down)"/>
<line x1="927.5" y1="520.8" x2="927.5" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="537.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="931.5" y1="485.1" x2="931.5" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="502.9" width="2.45" height="19.9" fill="var(--up)"/>
<line x1="935.4" y1="500.8" x2="935.4" y2="530.0" stroke="var(--down)" class="wick"/>
<rect x="934.19" y="504.1" width="2.45" height="25.0" fill="var(--down)"/>
<line x1="939.4" y1="528.6" x2="939.4" y2="556.1" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="532.6" width="2.45" height="23.3" fill="var(--down)"/>
<line x1="943.3" y1="544.0" x2="943.3" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="942.09" y="550.0" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="947.3" y1="572.7" x2="947.3" y2="586.5" stroke="var(--down)" class="wick"/>
<rect x="946.04" y="573.7" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="951.2" y1="582.3" x2="951.2" y2="592.3" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="584.8" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="955.2" y1="586.8" x2="955.2" y2="595.8" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="590.3" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="959.1" y1="584.0" x2="959.1" y2="593.8" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="591.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="963.1" y1="581.2" x2="963.1" y2="599.6" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="592.4" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="967.0" y1="575.8" x2="967.0" y2="591.5" stroke="var(--up)" class="wick"/>
<rect x="965.80" y="580.6" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="971.0" y1="582.4" x2="971.0" y2="594.2" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="589.1" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="974.9" y1="587.2" x2="974.9" y2="597.9" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="593.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="978.9" y1="577.9" x2="978.9" y2="596.2" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="581.4" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="982.8" y1="565.5" x2="982.8" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="578.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="986.8" y1="556.3" x2="986.8" y2="575.5" stroke="var(--up)" class="wick"/>
<rect x="985.56" y="563.0" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="990.7" y1="560.8" x2="990.7" y2="580.5" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="561.2" width="2.45" height="19.0" fill="var(--down)"/>
<line x1="994.7" y1="567.1" x2="994.7" y2="582.5" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="571.4" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="998.6" y1="567.2" x2="998.6" y2="584.5" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="567.4" width="2.45" height="8.5" fill="var(--up)"/>
<line x1="1002.6" y1="569.4" x2="1002.6" y2="594.8" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="570.9" width="2.45" height="23.1" fill="var(--down)"/>
<line x1="1006.5" y1="584.3" x2="1006.5" y2="597.2" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="585.7" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="1010.5" y1="577.9" x2="1010.5" y2="592.7" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="580.5" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="1014.5" y1="561.8" x2="1014.5" y2="578.8" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="562.1" width="2.45" height="14.9" fill="var(--up)"/>
<line x1="1018.4" y1="541.3" x2="1018.4" y2="560.4" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="543.7" width="2.45" height="16.2" fill="var(--up)"/>
<line x1="1022.4" y1="530.3" x2="1022.4" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="534.4" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="1026.3" y1="532.9" x2="1026.3" y2="551.2" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="539.8" width="2.45" height="9.4" fill="var(--up)"/>
<line x1="1030.3" y1="509.2" x2="1030.3" y2="544.3" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="510.6" width="2.45" height="26.2" fill="var(--up)"/>
<line x1="1034.2" y1="502.7" x2="1034.2" y2="522.3" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="506.1" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="1038.2" y1="492.7" x2="1038.2" y2="513.9" stroke="var(--up)" class="wick"/>
<rect x="1036.94" y="493.3" width="2.45" height="13.9" fill="var(--up)"/>
<line x1="1042.1" y1="491.8" x2="1042.1" y2="502.3" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="491.8" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="1046.1" y1="496.5" x2="1046.1" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="504.5" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="1050.0" y1="471.2" x2="1050.0" y2="508.0" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="483.0" width="2.45" height="16.3" fill="var(--down)"/>
<line x1="60" y1="448.3" x2="1052" y2="448.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="451.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$220 R1</text>
<text x="1058" y="463.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="319.0" x2="1052" y2="319.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="322.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$289 R2</text>
<text x="1058" y="334.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="87.7" x2="1052" y2="87.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="91.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$413 R3</text>
<text x="1058" y="103.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="532.4" x2="1052" y2="532.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="526.4" font-size="11.5" fill="var(--support)" font-weight="600">$175 S1</text>
<text x="1058" y="538.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="598.4" x2="1052" y2="598.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="592.4" font-size="11.5" fill="var(--support)" font-weight="600">$140 S2</text>
<text x="1058" y="604.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="499.3" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $413 | 2 | 2025년 10월(10/9, 52주 최고 $417.86)·2026년 1월(1/16, $408.25) 스윙 고점 — BlueHalo 인수 이후 첫 완전 회계연도 기대감이 정점이던 구간 |
| R2 | $289 | 2 | 2025년 12월(12/4)·2026년 2월(2/19) 스윙 고점 |
| R1 | $220 | 2 | 2026년 4월(4/21)·5월(5/28) 스윙 고점 — Q3 실적 충격(§3-A) 이후 반등 상단 |
| **현재가** | **$192.81** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $175 | 2 | 2026년 3월 말(3/30)·4월 초(4/10) 스윙 저점 — Q3 실적·Space 손상 충격 직후 저점대 |
| S2 | $140 | 2 | 2026년 7월(7/15, 7/30) 스윙 저점 — 재작성 공시(§3-B) 이후 형성된 최근 저점대 |

> 현재가 위쪽·아래쪽 모두 스크립트 기본값(3개)보다 적은 3개·2개로 나왔다 — 억지로 레벨을 채우지 않고 실제 클러스터(터치 2회 이상)만 표시했다. 최근 1년간 두 차례의 대형 이벤트(3월 실적 충격, 6월 재작성)로 가격이 넓은 밴드($135~$418)를 오가며 스윙 포인트가 여러 층에 분산된 결과, S3 후보(52주 최저 $135.20, 2026-06-25)는 인접 클러스터($140)와 거의 겹쳐 별도 레벨로 강제 추가하지 않았다.

---

## 3. 관측된 특이 구간

> 최근 1년간 가격대가 구조적으로 재설정된 사건이 세 차례 있었다 — 템플릿 기본 단일 사건 서술 대신 시간순으로 3개 하위 절로 나눠 기록한다.

### 3-A. 2026-03-10~11 — FY2026 3분기 실적·Space 손상 최초 발표 충격

- 2026-03-10 장중 FY2026 3분기 실적 발표 — Space 보고단위 영업권 손상 $151.3M 최초 인식, 미 우주군 SCAR 프로그램 계약 해지·재입찰 필요 공시([`02_history.md`](./02_history.md), [`08_news.md`](./08_news.md) 참고. 이 손상액은 이후 2026-06-22 10-Q/A로 $240.7M까지 확대 정정됨).
- 종가 기준 2026-03-09 $227.29 → 2026-03-10 $221.57(−2.5%) → 2026-03-11 $207.73(−6.3%), 이틀 누적 **−8.6%**. 2026-03-11 거래량은 523만 주로 직전 20거래일 평균(약 141만 주) 대비 약 3.7배.
- 이 충격 이후 주가는 4월 저점(S1 $175 구간)까지 추가 하락했다가, BlueHalo 통합 진행과 함께 5월 이후 R1($220) 구간까지 완만히 반등했다.

### 3-B. 2026-06-22 — 10-Q/A 재작성·내부통제 취약점 공시

- 2026-06-22 Space 보고단위 영업권 손상 계산 오류(인수 이연법인세 자산·부채 배분 누락)로 10-Q/A 제출, 손상액 $89.4M 추가(누적 $240.7M)로 확대 정정, 내부통제 중요한 취약점 공시([`02_history.md`](./02_history.md), [`08_news.md`](./08_news.md) 참고).
- 종가 기준 전 거래일(2026-06-18, $169.61) 대비 **−10.8%**($169.61 → $151.33), 거래량은 237만 주로 평균 대비 약 1.7배.
- 이후 주가는 6월 하순~7월 내내 S2($140) 구간까지 추가 하락하며 52주 최저가($135.20, 2026-06-25)를 이 구간에서 기록했다 — 재작성·내부통제 이슈가 3월 실적 충격보다 오히려 더 깊은 저점을 만든 사건이었다.

### 3-C. 2026-06-30 — FY2026 4분기 실적 서프라이즈(매출 +133%)

- 2026-06-29 장 마감 후 FY2026 4분기·연간 실적 발표 — 4분기 매출 $641.6M(YoY +133%), 흑자 전환(EPS $1.25), 펀디드 백로그 $1.2B로 확대([`08_news.md`](./08_news.md) 참고).
- 종가 기준 2026-06-29 $139.00 → 2026-06-30 $165.07로 **+18.8%** 급등, 거래량은 804만 주로 직전 20거래일 평균 대비 약 5.7배(최근 1년 중 최대 거래량 구간).
- 이 반등 이후 주가는 7~8월 사이 R1($220) 구간을 넘지 못하고 현재가($192.81) 부근에서 등락 중 — 3월·6월의 두 차례 악재로 무너진 밸류에이션이 4분기 실적 서프라이즈로 일부 회복됐으나 아직 이전 고점(R2·R3)에는 미치지 못한 상태다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영, 배당은 미반영 — AeroVironment는 배당을 지급한 적이 없어 배당락 영향 자체가 없음)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py AVAV --name AeroVironment --event 2026-03-11:"FY2026 3분기 실적·Space 손상 최초 발표 충격" --event 2026-06-22:"10-Q/A 재작성·내부통제 취약점 공시" --event 2026-06-30:"FY2026 4분기 실적 서프라이즈(매출 +133%)" --close-on 2026-04-30 --close-on 2026-08-13 --emit all`. 파라미터는 회사 간 비교가 가능하도록 스크립트 기본값 그대로 사용(강제 레벨 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - 최근 1년간 세 차례의 정보 이벤트(§3-A·3-B·3-C)로 가격 레짐이 반복적으로 단절됐다 — 특히 3월·6월 저점 구간은 펀더멘털 악재로 인한 급락이라 "지지선"의 기술적 의미(수요 유입)보다 "패닉 이후 반등 시작점"에 가까울 수 있다는 점을 감안해서 읽을 것.
    - 조사 기간(2025-08~2026-08) 내 주식분할·유상증자는 없었다(2025년 7월 유상증자는 이 조사 기간보다 앞선 FY2026 1분기 초, 즉 2025-07-XX로 이 차트 시작일 2025-08-15 이전 — 영향 없음).

---

## 관련 문서

같은 폴더 내 다른 문서로 이동:

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

- [Yahoo Finance — AeroVironment, Inc. (AVAV) 일봉 시세](https://finance.yahoo.com/quote/AVAV/history/) (수집 2026-08-16)
- [stockanalysis.com — AeroVironment 주가 이력 API 교차 확인](https://stockanalysis.com/stocks/AVAV/history/)

---

*작성일: 2026-08-16*
