# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, Yahoo Finance 일봉 API에서 직접 수집했다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). **겹치는 시점의 종가 대조(이 문서 수집 시점 2026-08-16 기준)**: 2026-08-13 종가 $99.37은 당시 핵심 지표 A.2·밸류에이션 / 적정주가가 인용한 stockanalysis.com 기준값과 정확히 일치했다. FY2025 회계연도 말(2025-12-31) 종가 $113.10 역시 핵심 지표 A.2 "FY2025" 열 값과 정확히 일치한다. ⚠️ **이후 갱신 참고**: 핵심 지표·밸류에이션 / 적정주가는 2026-08-19~21 급등을 반영해 2026-08-21 종가($108.13) 기준으로 갱신됐으나(2026-08-22), 이 일봉 차트 자체는 아직 2026-08-14까지의 데이터만 반영한다 — 차트를 최신 가격까지 재생성하기 전까지는 이 문서의 "현재가"($95.56)가 다른 문서보다 며칠 뒤처져 있다는 점에 유의할 것.
>
> ⚠️ 이 차트는 최근 1년(2025-08-15~2026-08-14) 구간만 다룬다 — 2021년 IPO(공모가 $38)·같은 해 GameStop 사태·2025년 6월 Bitstamp 인수 등 그 이전 연혁은 이 기간 밖이며 [역사 / 주요 이벤트](./02_history.md)를 참고할 것.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="hood-chart">
<style>
.hood-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .hood-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .hood-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.hood-chart svg { width:100%; height:auto; display:block; }
.hood-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.hood-chart .title { fill: var(--ink); font-weight:600; }
.hood-chart .grid { stroke: var(--grid); stroke-width:1; }
.hood-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Robinhood Markets(HOOD) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Robinhood Markets (HOOD) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $95.56 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="509.7" x2="1052" y2="509.7" class="grid"/>
<text x="52" y="513.7" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="393.3" x2="1052" y2="393.3" class="grid"/>
<text x="52" y="397.3" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="277.0" x2="1052" y2="277.0" class="grid"/>
<text x="52" y="281.0" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="160.7" x2="1052" y2="160.7" class="grid"/>
<text x="52" y="164.7" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
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
<line x1="121.3" y1="56.0" x2="121.3" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="127.3" y="68.0" font-size="10.5" fill="var(--down)">2025-09-08 S&P 500 편입 발표(+15.8%)</text>
<line x1="548.1" y1="56.0" x2="548.1" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="554.1" y="68.0" font-size="10.5" fill="var(--down)">2026-02-11 FY2025 Q4 실적 발표 반응(-8.9%)</text>
<line x1="757.6" y1="56.0" x2="757.6" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="763.6" y="68.0" font-size="10.5" fill="var(--down)">2026-04-29 2026 Q1 실적 발표 반응(-13.2%)</text>
<line x1="62.0" y1="309.8" x2="62.0" y2="343.3" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="310.9" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="65.9" y1="305.6" x2="65.9" y2="336.5" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="306.0" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="69.9" y1="291.8" x2="69.9" y2="355.5" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="299.6" width="2.45" height="50.1" fill="var(--down)"/>
<line x1="73.8" y1="346.9" x2="73.8" y2="399.2" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="354.6" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="77.8" y1="345.6" x2="77.8" y2="368.0" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="356.7" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="81.7" y1="324.2" x2="81.7" y2="371.2" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="339.1" width="2.45" height="22.0" fill="var(--up)"/>
<line x1="85.7" y1="336.1" x2="85.7" y2="358.7" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="344.0" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="89.6" y1="338.9" x2="89.6" y2="363.6" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="342.2" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="93.6" y1="339.4" x2="93.6" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="92.37" y="342.8" width="2.45" height="33.6" fill="var(--down)"/>
<line x1="97.5" y1="361.9" x2="97.5" y2="377.3" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="370.1" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="101.5" y1="367.8" x2="101.5" y2="382.1" stroke="var(--up)" class="wick"/>
<rect x="100.27" y="369.9" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="105.5" y1="382.3" x2="105.5" y2="405.6" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="388.5" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="109.4" y1="377.7" x2="109.4" y2="396.8" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="384.1" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="113.4" y1="365.7" x2="113.4" y2="389.9" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="376.4" width="2.45" height="12.6" fill="var(--up)"/>
<line x1="117.3" y1="358.3" x2="117.3" y2="418.6" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="364.4" width="2.45" height="21.7" fill="var(--down)"/>
<line x1="121.3" y1="292.7" x2="121.3" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="292.8" width="2.45" height="38.7" fill="var(--up)"/>
<line x1="125.2" y1="284.6" x2="125.2" y2="313.3" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="285.7" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="129.2" y1="257.0" x2="129.2" y2="296.3" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="272.2" width="2.45" height="19.6" fill="var(--down)"/>
<line x1="133.1" y1="267.2" x2="133.1" y2="292.3" stroke="var(--down)" class="wick"/>
<rect x="131.89" y="289.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="137.1" y1="285.3" x2="137.1" y2="311.6" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="289.1" width="2.45" height="16.9" fill="var(--down)"/>
<line x1="141.0" y1="297.2" x2="141.0" y2="321.1" stroke="var(--down)" class="wick"/>
<rect x="139.79" y="304.1" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="145.0" y1="287.9" x2="145.0" y2="313.1" stroke="var(--up)" class="wick"/>
<rect x="143.75" y="292.3" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="148.9" y1="282.1" x2="148.9" y2="306.7" stroke="var(--up)" class="wick"/>
<rect x="147.70" y="284.9" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="152.9" y1="251.7" x2="152.9" y2="277.8" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="271.7" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="156.8" y1="246.9" x2="156.8" y2="271.2" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="249.2" width="2.45" height="17.9" fill="var(--up)"/>
<line x1="160.8" y1="238.4" x2="160.8" y2="264.2" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="248.6" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="164.7" y1="231.8" x2="164.7" y2="253.3" stroke="var(--up)" class="wick"/>
<rect x="163.51" y="241.0" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="168.7" y1="218.4" x2="168.7" y2="247.9" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="233.3" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="172.6" y1="243.3" x2="172.6" y2="273.4" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="257.7" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="176.6" y1="247.6" x2="176.6" y2="274.3" stroke="var(--down)" class="wick"/>
<rect x="175.36" y="252.7" width="2.45" height="14.0" fill="var(--down)"/>
<line x1="180.5" y1="179.1" x2="180.5" y2="255.0" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="179.8" width="2.45" height="75.3" fill="var(--up)"/>
<line x1="184.5" y1="139.6" x2="184.5" y2="186.5" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="142.2" width="2.45" height="43.7" fill="var(--up)"/>
<line x1="188.4" y1="142.3" x2="188.4" y2="173.6" stroke="var(--down)" class="wick"/>
<rect x="187.22" y="153.4" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="192.4" y1="121.7" x2="192.4" y2="159.8" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="127.5" width="2.45" height="17.0" fill="var(--up)"/>
<line x1="196.4" y1="101.3" x2="196.4" y2="130.3" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="110.3" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="200.3" y1="80.1" x2="200.3" y2="136.7" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="85.1" width="2.45" height="50.8" fill="var(--down)"/>
<line x1="204.3" y1="119.3" x2="204.3" y2="153.4" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="123.9" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="208.2" y1="94.7" x2="208.2" y2="134.2" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="97.5" width="2.45" height="27.7" fill="var(--up)"/>
<line x1="212.2" y1="84.6" x2="212.2" y2="118.2" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="88.2" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="216.1" y1="81.8" x2="216.1" y2="166.9" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="93.8" width="2.45" height="73.0" fill="var(--down)"/>
<line x1="220.1" y1="122.5" x2="220.1" y2="180.9" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="133.8" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="224.0" y1="153.7" x2="224.0" y2="201.1" stroke="var(--down)" class="wick"/>
<rect x="222.79" y="179.8" width="2.45" height="10.3" fill="var(--down)"/>
<line x1="228.0" y1="162.7" x2="228.0" y2="198.3" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="171.8" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="231.9" y1="175.4" x2="231.9" y2="215.5" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="187.6" width="2.45" height="22.9" fill="var(--down)"/>
<line x1="235.9" y1="211.8" x2="235.9" y2="244.4" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="219.4" width="2.45" height="10.2" fill="var(--up)"/>
<line x1="239.8" y1="159.5" x2="239.8" y2="202.0" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="185.1" width="2.45" height="13.8" fill="var(--up)"/>
<line x1="243.8" y1="188.0" x2="243.8" y2="211.0" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="188.1" width="2.45" height="20.1" fill="var(--down)"/>
<line x1="247.7" y1="205.1" x2="247.7" y2="271.9" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="209.4" width="2.45" height="25.7" fill="var(--down)"/>
<line x1="251.7" y1="186.5" x2="251.7" y2="234.7" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="193.7" width="2.45" height="35.2" fill="var(--up)"/>
<line x1="255.6" y1="147.9" x2="255.6" y2="177.6" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="161.9" width="2.45" height="10.5" fill="var(--up)"/>
<line x1="259.6" y1="107.2" x2="259.6" y2="142.2" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="126.6" width="2.45" height="5.1" fill="var(--up)"/>
<line x1="263.5" y1="113.5" x2="263.5" y2="127.9" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="124.3" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="267.5" y1="115.8" x2="267.5" y2="144.8" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="125.8" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="271.4" y1="136.6" x2="271.4" y2="176.7" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="146.8" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="275.4" y1="99.8" x2="275.4" y2="141.5" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="121.3" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="279.3" y1="106.0" x2="279.3" y2="146.2" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="109.6" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="283.3" y1="135.1" x2="283.3" y2="180.3" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="161.5" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="287.3" y1="132.9" x2="287.3" y2="186.8" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="146.3" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="291.2" y1="159.8" x2="291.2" y2="241.2" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="160.7" width="2.45" height="75.1" fill="var(--down)"/>
<line x1="295.2" y1="206.1" x2="295.2" y2="272.9" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="216.8" width="2.45" height="38.4" fill="var(--up)"/>
<line x1="299.1" y1="166.6" x2="299.1" y2="209.3" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="184.7" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="303.1" y1="191.7" x2="303.1" y2="213.6" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="195.6" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="307.0" y1="196.5" x2="307.0" y2="228.6" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="199.5" width="2.45" height="2.0" fill="var(--down)"/>
<line x1="311.0" y1="218.0" x2="311.0" y2="280.1" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="219.6" width="2.45" height="48.5" fill="var(--down)"/>
<line x1="314.9" y1="239.2" x2="314.9" y2="311.9" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="262.5" width="2.45" height="42.7" fill="var(--up)"/>
<line x1="318.9" y1="271.3" x2="318.9" y2="321.1" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="274.1" width="2.45" height="26.3" fill="var(--down)"/>
<line x1="322.8" y1="294.6" x2="322.8" y2="321.5" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="310.2" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="326.8" y1="281.7" x2="326.8" y2="314.5" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="287.7" width="2.45" height="19.9" fill="var(--up)"/>
<line x1="330.7" y1="261.7" x2="330.7" y2="362.9" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="267.5" width="2.45" height="89.7" fill="var(--down)"/>
<line x1="334.7" y1="335.2" x2="334.7" y2="381.1" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="347.7" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="338.6" y1="301.9" x2="338.6" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="306.3" width="2.45" height="29.4" fill="var(--up)"/>
<line x1="342.6" y1="295.6" x2="342.6" y2="339.9" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="302.8" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="346.5" y1="225.3" x2="346.5" y2="272.0" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="229.3" width="2.45" height="40.0" fill="var(--up)"/>
<line x1="350.5" y1="219.1" x2="350.5" y2="235.4" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="227.6" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="354.4" y1="246.3" x2="354.4" y2="283.7" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="257.0" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="358.4" y1="223.6" x2="358.4" y2="250.8" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="242.4" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="362.3" y1="193.6" x2="362.3" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="197.7" width="2.45" height="43.9" fill="var(--up)"/>
<line x1="366.3" y1="176.0" x2="366.3" y2="202.7" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="177.7" width="2.45" height="22.5" fill="var(--up)"/>
<line x1="370.2" y1="188.4" x2="370.2" y2="219.1" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="189.4" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="374.2" y1="171.8" x2="374.2" y2="207.2" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="181.5" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="378.2" y1="162.1" x2="378.2" y2="198.1" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="185.6" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="382.1" y1="175.5" x2="382.1" y2="198.9" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="185.9" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="386.1" y1="208.5" x2="386.1" y2="262.3" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="208.5" width="2.45" height="48.8" fill="var(--down)"/>
<line x1="390.0" y1="244.2" x2="390.0" y2="289.6" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="246.0" width="2.45" height="34.0" fill="var(--down)"/>
<line x1="394.0" y1="273.2" x2="394.0" y2="311.3" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="274.7" width="2.45" height="29.9" fill="var(--down)"/>
<line x1="397.9" y1="272.9" x2="397.9" y2="301.7" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="280.5" width="2.45" height="15.7" fill="var(--up)"/>
<line x1="401.9" y1="249.7" x2="401.9" y2="302.7" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="271.4" width="2.45" height="30.1" fill="var(--down)"/>
<line x1="405.8" y1="252.3" x2="405.8" y2="294.2" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="266.1" width="2.45" height="27.4" fill="var(--down)"/>
<line x1="409.8" y1="259.8" x2="409.8" y2="287.5" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="269.2" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="413.7" y1="250.6" x2="413.7" y2="270.8" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="256.6" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="417.7" y1="270.3" x2="417.7" y2="295.9" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="275.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="421.6" y1="273.1" x2="421.6" y2="285.2" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="274.5" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="425.6" y1="271.0" x2="425.6" y2="290.4" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="272.9" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="429.5" y1="283.1" x2="429.5" y2="300.2" stroke="var(--up)" class="wick"/>
<rect x="428.30" y="292.0" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="433.5" y1="285.0" x2="433.5" y2="305.1" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="290.8" width="2.45" height="12.7" fill="var(--down)"/>
<line x1="437.4" y1="302.3" x2="437.4" y2="318.6" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="307.0" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="441.4" y1="300.1" x2="441.4" y2="332.8" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="303.3" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="445.3" y1="257.1" x2="445.3" y2="291.3" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="258.2" width="2.45" height="30.9" fill="var(--up)"/>
<line x1="449.3" y1="251.7" x2="449.3" y2="288.4" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="252.8" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="453.2" y1="276.4" x2="453.2" y2="297.1" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="276.7" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="457.2" y1="292.6" x2="457.2" y2="312.7" stroke="var(--down)" class="wick"/>
<rect x="455.97" y="301.7" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="461.1" y1="287.3" x2="461.1" y2="306.8" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="294.6" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="465.1" y1="279.2" x2="465.1" y2="309.3" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="291.4" width="2.45" height="17.5" fill="var(--up)"/>
<line x1="469.1" y1="274.5" x2="469.1" y2="300.3" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="275.6" width="2.45" height="16.5" fill="var(--up)"/>
<line x1="473.0" y1="271.9" x2="473.0" y2="296.7" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="275.3" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="477.0" y1="277.7" x2="477.0" y2="334.4" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="279.3" width="2.45" height="53.9" fill="var(--down)"/>
<line x1="480.9" y1="327.9" x2="480.9" y2="353.3" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="329.1" width="2.45" height="13.4" fill="var(--down)"/>
<line x1="484.9" y1="344.8" x2="484.9" y2="367.5" stroke="var(--up)" class="wick"/>
<rect x="483.64" y="359.7" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="488.8" y1="343.9" x2="488.8" y2="364.6" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="358.9" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="492.8" y1="346.4" x2="492.8" y2="363.7" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="349.8" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="496.7" y1="326.7" x2="496.7" y2="355.5" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="352.7" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="500.7" y1="344.0" x2="500.7" y2="365.3" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="352.6" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="504.6" y1="340.7" x2="504.6" y2="366.2" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="348.6" width="2.45" height="14.3" fill="var(--down)"/>
<line x1="508.6" y1="351.2" x2="508.6" y2="375.9" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="362.6" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="512.5" y1="371.1" x2="512.5" y2="398.0" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="371.1" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="516.5" y1="368.3" x2="516.5" y2="402.8" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="377.4" width="2.45" height="18.9" fill="var(--down)"/>
<line x1="520.4" y1="417.3" x2="520.4" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="417.3" width="2.45" height="34.7" fill="var(--down)"/>
<line x1="524.4" y1="449.5" x2="524.4" y2="481.0" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="450.9" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="528.3" y1="478.8" x2="528.3" y2="523.5" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="481.9" width="2.45" height="24.1" fill="var(--down)"/>
<line x1="532.3" y1="513.1" x2="532.3" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="523.2" width="2.45" height="29.0" fill="var(--down)"/>
<line x1="536.2" y1="484.7" x2="536.2" y2="526.4" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="493.3" width="2.45" height="28.8" fill="var(--up)"/>
<line x1="540.2" y1="459.7" x2="540.2" y2="493.2" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="471.5" width="2.45" height="9.8" fill="var(--up)"/>
<line x1="544.1" y1="461.9" x2="544.1" y2="479.4" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="477.1" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="548.1" y1="510.3" x2="548.1" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="546.87" y="521.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="552.0" y1="515.5" x2="552.0" y2="565.3" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="516.2" width="2.45" height="45.1" fill="var(--down)"/>
<line x1="556.0" y1="526.7" x2="556.0" y2="559.0" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="533.1" width="2.45" height="20.4" fill="var(--up)"/>
<line x1="560.0" y1="528.8" x2="560.0" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="536.2" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="563.9" y1="519.8" x2="563.9" y2="544.2" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="537.5" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="567.9" y1="532.1" x2="567.9" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="535.0" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="571.8" y1="520.8" x2="571.8" y2="538.0" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="532.3" width="2.45" height="5.3" fill="var(--up)"/>
<line x1="575.8" y1="539.0" x2="575.8" y2="559.6" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="541.1" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="579.7" y1="545.3" x2="579.7" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="548.1" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="583.7" y1="520.6" x2="583.7" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="524.0" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="587.6" y1="512.2" x2="587.6" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="586.39" y="512.9" width="2.45" height="14.7" fill="var(--up)"/>
<line x1="591.6" y1="522.5" x2="591.6" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="590.34" y="528.3" width="2.45" height="5.5" fill="var(--down)"/>
<line x1="595.5" y1="512.3" x2="595.5" y2="550.4" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="516.8" width="2.45" height="30.8" fill="var(--up)"/>
<line x1="599.5" y1="524.8" x2="599.5" y2="554.8" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="532.5" width="2.45" height="11.8" fill="var(--up)"/>
<line x1="603.4" y1="487.3" x2="603.4" y2="512.1" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="496.8" width="2.45" height="15.2" fill="var(--up)"/>
<line x1="607.4" y1="482.0" x2="607.4" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="497.3" width="2.45" height="9.1" fill="var(--down)"/>
<line x1="611.3" y1="515.5" x2="611.3" y2="530.7" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="521.8" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="615.3" y1="511.7" x2="615.3" y2="535.6" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="513.5" width="2.45" height="20.0" fill="var(--up)"/>
<line x1="619.2" y1="505.3" x2="619.2" y2="523.3" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="508.5" width="2.45" height="9.7" fill="var(--down)"/>
<line x1="623.2" y1="511.0" x2="623.2" y2="528.7" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="517.3" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="627.1" y1="522.4" x2="627.1" y2="538.3" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="525.2" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="631.1" y1="523.5" x2="631.1" y2="551.6" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="528.6" width="2.45" height="19.5" fill="var(--down)"/>
<line x1="635.0" y1="534.1" x2="635.0" y2="543.9" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="537.0" width="2.45" height="1.2" fill="var(--up)"/>
<line x1="639.0" y1="523.1" x2="639.0" y2="536.5" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="525.1" width="2.45" height="11.3" fill="var(--up)"/>
<line x1="642.9" y1="525.7" x2="642.9" y2="539.7" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="532.2" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="646.9" y1="537.8" x2="646.9" y2="557.9" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="543.6" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="650.9" y1="548.0" x2="650.9" y2="568.4" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="549.8" width="2.45" height="12.9" fill="var(--down)"/>
<line x1="654.8" y1="546.9" x2="654.8" y2="562.5" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="553.4" width="2.45" height="3.7" fill="var(--up)"/>
<line x1="658.8" y1="557.1" x2="658.8" y2="576.1" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="559.1" width="2.45" height="14.1" fill="var(--down)"/>
<line x1="662.7" y1="541.1" x2="662.7" y2="557.7" stroke="var(--up)" class="wick"/>
<rect x="661.48" y="553.1" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="666.7" y1="549.0" x2="666.7" y2="569.6" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="561.1" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="670.6" y1="574.3" x2="670.6" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="576.3" width="2.45" height="14.7" fill="var(--down)"/>
<line x1="674.6" y1="580.1" x2="674.6" y2="605.6" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="586.1" width="2.45" height="9.9" fill="var(--down)"/>
<line x1="678.5" y1="571.3" x2="678.5" y2="595.9" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="571.9" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="682.5" y1="558.8" x2="682.5" y2="572.8" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="561.3" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="686.4" y1="567.0" x2="686.4" y2="593.6" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="574.2" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="690.4" y1="563.1" x2="690.4" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="569.1" width="2.45" height="2.7" fill="var(--up)"/>
<line x1="694.3" y1="569.8" x2="694.3" y2="587.5" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="569.9" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="698.3" y1="522.1" x2="698.3" y2="560.2" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="528.3" width="2.45" height="28.9" fill="var(--down)"/>
<line x1="702.2" y1="553.5" x2="702.2" y2="574.9" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="558.6" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="706.2" y1="562.8" x2="706.2" y2="577.8" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="567.2" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="710.1" y1="557.9" x2="710.1" y2="580.6" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="558.1" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="714.1" y1="513.9" x2="714.1" y2="538.5" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="515.0" width="2.45" height="23.0" fill="var(--up)"/>
<line x1="718.0" y1="465.8" x2="718.0" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="467.1" width="2.45" height="21.9" fill="var(--up)"/>
<line x1="722.0" y1="455.1" x2="722.0" y2="487.2" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="456.2" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="725.9" y1="432.2" x2="725.9" y2="454.0" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="447.1" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="729.9" y1="437.7" x2="729.9" y2="461.9" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="444.1" width="2.45" height="9.2" fill="var(--up)"/>
<line x1="733.8" y1="443.1" x2="733.8" y2="473.7" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="445.2" width="2.45" height="27.0" fill="var(--down)"/>
<line x1="737.8" y1="450.7" x2="737.8" y2="466.2" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="455.3" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="741.8" y1="465.4" x2="741.8" y2="499.5" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="470.7" width="2.45" height="18.4" fill="var(--down)"/>
<line x1="745.7" y1="480.2" x2="745.7" y2="493.3" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="481.2" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="749.7" y1="476.5" x2="749.7" y2="491.6" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="484.8" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="753.6" y1="491.4" x2="753.6" y2="504.9" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="497.6" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="757.6" y1="547.0" x2="757.6" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="554.5" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="761.5" y1="545.3" x2="761.5" y2="563.4" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="551.0" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="765.5" y1="537.1" x2="765.5" y2="550.0" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="545.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="769.4" y1="519.6" x2="769.4" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="529.7" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="773.4" y1="516.9" x2="773.4" y2="530.1" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="523.5" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="777.3" y1="512.6" x2="777.3" y2="531.8" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="515.2" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="781.3" y1="514.2" x2="781.3" y2="536.1" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="515.8" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="785.2" y1="526.7" x2="785.2" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="526.9" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="789.2" y1="503.0" x2="789.2" y2="539.9" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="505.1" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="793.1" y1="508.6" x2="793.1" y2="530.1" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="515.0" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="797.1" y1="523.5" x2="797.1" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="526.7" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="801.0" y1="498.4" x2="801.0" y2="538.1" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="505.6" width="2.45" height="27.0" fill="var(--up)"/>
<line x1="805.0" y1="517.9" x2="805.0" y2="530.6" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="518.2" width="2.45" height="8.1" fill="var(--down)"/>
<line x1="808.9" y1="510.1" x2="808.9" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="807.72" y="526.2" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="812.9" y1="530.8" x2="812.9" y2="549.3" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="532.1" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="816.8" y1="530.9" x2="816.8" y2="546.0" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="534.3" width="2.45" height="5.9" fill="var(--up)"/>
<line x1="820.8" y1="528.5" x2="820.8" y2="540.8" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="533.4" width="2.45" height="5.7" fill="var(--up)"/>
<line x1="824.7" y1="526.5" x2="824.7" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="531.1" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="828.7" y1="532.7" x2="828.7" y2="547.7" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="541.7" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="832.7" y1="529.2" x2="832.7" y2="547.8" stroke="var(--up)" class="wick"/>
<rect x="831.43" y="531.6" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="836.6" y1="481.1" x2="836.6" y2="547.3" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="481.5" width="2.45" height="58.1" fill="var(--up)"/>
<line x1="840.6" y1="425.9" x2="840.6" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="426.5" width="2.45" height="50.3" fill="var(--up)"/>
<line x1="844.5" y1="437.6" x2="844.5" y2="477.3" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="447.3" width="2.45" height="4.6" fill="var(--up)"/>
<line x1="848.5" y1="454.8" x2="848.5" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="459.2" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="852.4" y1="470.0" x2="852.4" y2="495.7" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="472.2" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="856.4" y1="459.5" x2="856.4" y2="493.4" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="461.2" width="2.45" height="29.5" fill="var(--up)"/>
<line x1="860.3" y1="467.0" x2="860.3" y2="512.6" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="471.5" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="864.3" y1="476.9" x2="864.3" y2="493.3" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="480.4" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="868.2" y1="462.7" x2="868.2" y2="515.9" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="475.5" width="2.45" height="12.2" fill="var(--down)"/>
<line x1="872.2" y1="443.0" x2="872.2" y2="485.9" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="472.7" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="876.1" y1="430.3" x2="876.1" y2="476.4" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="438.5" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="880.1" y1="416.0" x2="880.1" y2="450.2" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="433.0" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="884.0" y1="388.3" x2="884.0" y2="408.2" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="400.8" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="888.0" y1="382.4" x2="888.0" y2="424.9" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="392.4" width="2.45" height="20.1" fill="var(--down)"/>
<line x1="891.9" y1="330.9" x2="891.9" y2="418.0" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="363.1" width="2.45" height="53.9" fill="var(--up)"/>
<line x1="895.9" y1="340.5" x2="895.9" y2="373.2" stroke="var(--up)" class="wick"/>
<rect x="894.66" y="345.9" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="899.8" y1="320.6" x2="899.8" y2="362.7" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="346.8" width="2.45" height="13.3" fill="var(--down)"/>
<line x1="903.8" y1="358.5" x2="903.8" y2="387.4" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="374.4" width="2.45" height="9.3" fill="var(--up)"/>
<line x1="907.7" y1="368.5" x2="907.7" y2="414.9" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="379.7" width="2.45" height="30.0" fill="var(--down)"/>
<line x1="911.7" y1="398.1" x2="911.7" y2="435.2" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="400.4" width="2.45" height="30.9" fill="var(--down)"/>
<line x1="915.6" y1="396.6" x2="915.6" y2="433.6" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="401.0" width="2.45" height="31.8" fill="var(--up)"/>
<line x1="919.6" y1="376.8" x2="919.6" y2="404.7" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="382.7" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="923.6" y1="375.5" x2="923.6" y2="395.3" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="382.5" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="927.5" y1="337.9" x2="927.5" y2="391.1" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="343.0" width="2.45" height="46.4" fill="var(--up)"/>
<line x1="931.5" y1="276.7" x2="931.5" y2="329.8" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="319.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="935.4" y1="284.9" x2="935.4" y2="327.0" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="291.3" width="2.45" height="35.7" fill="var(--up)"/>
<line x1="939.4" y1="289.5" x2="939.4" y2="320.5" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="301.6" width="2.45" height="16.7" fill="var(--down)"/>
<line x1="943.3" y1="311.2" x2="943.3" y2="341.6" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="314.7" width="2.45" height="15.5" fill="var(--up)"/>
<line x1="947.3" y1="290.7" x2="947.3" y2="325.7" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="305.5" width="2.45" height="16.8" fill="var(--up)"/>
<line x1="951.2" y1="280.3" x2="951.2" y2="342.1" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="281.9" width="2.45" height="41.8" fill="var(--down)"/>
<line x1="955.2" y1="313.7" x2="955.2" y2="341.9" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="327.8" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="959.1" y1="313.7" x2="959.1" y2="340.4" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="315.1" width="2.45" height="14.1" fill="var(--up)"/>
<line x1="963.1" y1="296.8" x2="963.1" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="303.0" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="967.0" y1="308.9" x2="967.0" y2="361.5" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="311.2" width="2.45" height="47.2" fill="var(--down)"/>
<line x1="971.0" y1="369.4" x2="971.0" y2="413.2" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="391.2" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="974.9" y1="378.2" x2="974.9" y2="401.4" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="378.9" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="978.9" y1="345.6" x2="978.9" y2="377.0" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="356.4" width="2.45" height="20.6" fill="var(--up)"/>
<line x1="982.8" y1="353.3" x2="982.8" y2="368.2" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="365.9" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="986.8" y1="369.4" x2="986.8" y2="397.3" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="382.4" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="990.7" y1="392.9" x2="990.7" y2="433.9" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="392.9" width="2.45" height="30.0" fill="var(--down)"/>
<line x1="994.7" y1="396.5" x2="994.7" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="993.47" y="410.9" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="998.6" y1="429.0" x2="998.6" y2="461.9" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="435.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1002.6" y1="432.2" x2="1002.6" y2="459.7" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="438.7" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="1006.5" y1="436.6" x2="1006.5" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="446.2" width="2.45" height="25.1" fill="var(--down)"/>
<line x1="1010.5" y1="454.4" x2="1010.5" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="471.5" width="2.45" height="2.5" fill="var(--up)"/>
<line x1="1014.5" y1="437.8" x2="1014.5" y2="478.8" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="449.5" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="1018.4" y1="418.9" x2="1018.4" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="431.1" width="2.45" height="5.2" fill="var(--up)"/>
<line x1="1022.4" y1="419.2" x2="1022.4" y2="438.0" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="428.5" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="1026.3" y1="436.4" x2="1026.3" y2="450.3" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="447.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="1030.3" y1="418.1" x2="1030.3" y2="436.9" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="432.4" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="1034.2" y1="416.9" x2="1034.2" y2="437.6" stroke="var(--up)" class="wick"/>
<rect x="1032.99" y="425.2" width="2.45" height="7.4" fill="var(--up)"/>
<line x1="1038.2" y1="421.7" x2="1038.2" y2="435.5" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="422.6" width="2.45" height="3.4" fill="var(--down)"/>
<line x1="1042.1" y1="409.8" x2="1042.1" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="410.9" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="1046.1" y1="391.3" x2="1046.1" y2="414.2" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="397.0" width="2.45" height="16.6" fill="var(--up)"/>
<line x1="1050.0" y1="402.5" x2="1050.0" y2="419.9" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="405.0" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="60" y1="264.3" x2="1052" y2="264.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="267.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$122 R1</text>
<text x="1058" y="279.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="89.9" x2="1052" y2="89.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="93.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$152 R2</text>
<text x="1058" y="105.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="568.7" x2="1052" y2="568.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="562.7" font-size="11.5" fill="var(--support)" font-weight="600">$70 S1</text>
<text x="1058" y="574.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="419.2" r="3" fill="var(--ink)"/>
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
| R2 | $152 | 2 | 2025-10-03~10-10 스윙 고점대 (52주 최고 $153.86, 2025-10-06) |
| R1 | $122 | 4 | 2025-09-18, 2025-12-17~12-22, 2026-01-05~01-06 등 약 4개월에 걸쳐 반복 형성된 스윙 고점대 |
| **현재가** | **$95.56** (2026-08-14 종가) | — | R1과 S1 사이 |
| S1 | $70 | 3 | 2026-02-24~2026-04-13 구간의 스윙 저점대 (52주 최저 $63.51, 2026-03-30 근접) |

> 레벨은 유효한 클러스터 3개(R2·R1·S1)만 표시했다 — 현재가 아래로 스크립트 기본값(3개)만큼의 지지 클러스터가 형성되지 않아 S2·S3는 생략했다.

---

## 3. 관측된 특이 구간

### 3-1. 2025-09-08 — S&P 500 편입 발표 (+15.8%)

- Robinhood가 MarketAxess Holdings를 대체해 S&P 500에 편입된다는 발표가 나오면서 인덱스펀드·ETF의 자동 매수가 촉발됐다(편입 발효일은 2025-09-22)[^sp500].
- 종가 기준 전일 대비 **+15.83%** ($101.25 → $117.28), 거래량은 평소(직전 구간 일 3천만 주대) 대비 약 3배가 넘는 **약 1억 240만 주**로 뛰었다. 이 구간의 1년 내 일간 등락률 중 최대치다.
- 이 사건 이후 주가는 9월 말~10월 초 $150대까지 추가 상승하며 2. 지지선 / 저항선 요약의 R2($152) 저항대를 형성했다 — 즉 R2는 이 지수 편입 랠리의 연장선에서 만들어진 레벨이다.

### 3-2. 2026-02-11 — FY2025 4분기 실적 발표 반응 (-8.9%)

- 2026-02-10 장 마감 후 발표된 FY2025 4분기 실적에서 EPS($0.66)는 컨센서스($0.64)를 상회했지만 매출이 컨센서스에 못 미쳤고, 특히 크립토 매출($221M)이 예상($248.2M)을 하회했다[^q4miss]. 최근 뉴스 / 이슈의 2026-02-10 로그 항목 참고.
- 종가 기준 전일 대비 **-8.91%** ($85.60 → $77.97). 장중 낙폭은 이보다 더 커 발표 다음 날 오전 한때 -12.5%까지 밀렸다는 보도가 있다[^q4miss].
- 이 구간을 전후로 주가는 $70대 박스권에 진입했고, 이후 2. 지지선 / 저항선 요약의 S1($70) 지지대가 형성되는 출발점이 됐다.

### 3-3. 2026-04-29 — 2026년 1분기 실적 발표 반응 (-13.2%)

- 2026-04-28 장 마감 후 발표된 1분기 실적에서 EPS($0.38)·매출($1.07B)이 모두 컨센서스(EPS $0.42, 매출 $1.14B)를 하회했다. 크립토 거래 매출이 전년 동기 대비 47% 급감한 것이 주된 원인으로 지목됐다[^q1miss]. 재무 / 실적 1. 성장성, 최근 뉴스 / 이슈 2026-04-28 로그 참고.
- 종가 기준 전일 대비 **-13.24%** ($82.07 → $71.20), 거래량은 3개월 평균(약 3,300만 주) 대비 약 2.3배인 **약 7,670만 주**로 급증했다[^q1miss].
- 이 발표 직후 주가는 2. 지지선 / 저항선 요약의 S1($70) 클러스터 하단부에 근접했으며, 이후 2026년 5월 중순까지 이 구간에서 등락했다.

> 위 3건 외에도 2025-11-06(3분기 실적 반응, -10.8%)·2026-07-30(2분기 실적 반응, -3.6%) 등 분기 실적 발표일 전후로 크고 작은 변동이 반복됐다 — Robinhood는 분기별 크립토·이벤트 계약 매출 변동성이 커(재무 / 실적 1. 성장성) 실적 발표일 자체가 구조적으로 큰 갭을 만드는 종목이라는 점을 감안해야 한다. 위 3건은 그중 자료로 확인 가능했던 최대 폭의 사례만 다뤘다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-16. 원주가(과거 분할은 소급 반영, 배당은 미반영) — Robinhood는 이 구간 내 주식분할 이력이 없다(핵심 지표 상단 각주 참고).
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py HOOD --name "Robinhood Markets" --event 2025-09-08:"S&P 500 편입 발표(+15.8%)" --event 2026-02-11:"FY2025 Q4 실적 발표 반응(-8.9%)" --event 2026-04-29:"2026 Q1 실적 발표 반응(-13.2%)" --close-on 2026-08-13 --close-on 2025-12-31`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있어 변경하지 않았다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - Robinhood는 이 1년 구간 내에서만도 ±10% 넘는 단일 거래일 변동이 15회 넘게 발생한 고변동성 종목이다(3. 관측된 특이 구간) — 스윙 클러스터의 "강도"가 안정적 레짐의 지지/저항보다 뉴스 이벤트에 의해 기계적으로 형성된 경우가 많아, 저변동성 종목보다 이 방법론의 신뢰도가 낮다고 봐야 한다.
    - 이 구간에는 주식분할·대규모 유상증자 등 가격 연속성을 깨는 이벤트가 없어 소급 조정은 불필요했다.

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

- [Yahoo Finance — HOOD 일봉 OHLCV (query1.finance.yahoo.com chart API)](https://finance.yahoo.com/quote/HOOD/history/)
- [stockanalysis.com — HOOD 종가 데이터](https://stockanalysis.com/stocks/hood/) (대조용)

[^sp500]: [Robinhood shares soar 15% after getting long-sought addition to S&P 500 — CNBC (2025-09-08)](https://www.cnbc.com/2025/09/08/robinhood-shares-soar-14percent-after-getting-long-sought-addition-to-sp-500.html)
[^q4miss]: [Why Robinhood Stock Crashed After Earnings — Yahoo Finance](https://finance.yahoo.com/news/why-robinhood-stock-crashed-earnings-161735966.html); [Robinhood revenue miss: Why the market reaction is 'warranted' — Yahoo Finance](https://finance.yahoo.com/video/robinhood-revenue-miss-why-market-221409897.html)
[^q1miss]: [Robinhood Stock Is Dropping After Q1 2026 Earnings -- What Happened and What to Do Next — The Motley Fool (2026-04-30)](https://www.fool.com/investing/2026/04/30/robinhood-stock-is-dropping-after-q1-2026-earnings/); [Robinhood Markets Inc Stock (HOOD) Moved Down by 13.72% on Apr 29 — TradingKey](https://www.tradingkey.com/news/market-movers/261838577-market-movers-hood-20260429)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-23)*
