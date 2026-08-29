# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, Yahoo Finance 일봉 API에서 직접 수집했다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). **겹치는 시점의 종가 대조(이 문서 수집 시점 2026-08-15 기준)**: 2026-08-13 종가 $153.90은 당시 핵심 지표 A.2·밸류에이션 / 적정주가가 인용한 stockanalysis.com 기준값과 정확히 일치했다. FY2025 회계연도 말(2025-12-31) 종가 $226.14 역시 핵심 지표 A.2 "FY2025" 열 값과 정확히 일치한다. ⚠️ **이후 갱신 참고**: 핵심 지표·밸류에이션 / 적정주가는 2026-08-19~21 급등을 반영해 2026-08-21 종가($186.49) 기준으로 갱신됐으나(2026-08-22), 이 일봉 차트 자체는 아직 2026-08-14까지의 데이터만 반영한다 — 차트를 최신 가격까지 재생성하기 전까지는 이 문서의 "현재가"($148.47)가 다른 문서보다 며칠 뒤처져 있다는 점에 유의할 것.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="coin-chart">
<style>
.coin-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .coin-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .coin-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.coin-chart svg { width:100%; height:auto; display:block; }
.coin-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.coin-chart .title { fill: var(--ink); font-weight:600; }
.coin-chart .grid { stroke: var(--grid); stroke-width:1; }
.coin-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Coinbase(COIN) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Coinbase (COIN) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $148.47 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="586.0" x2="1052" y2="586.0" class="grid"/>
<text x="52" y="590.0" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="486.0" x2="1052" y2="486.0" class="grid"/>
<text x="52" y="490.0" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="386.0" x2="1052" y2="386.0" class="grid"/>
<text x="52" y="390.0" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="286.0" x2="1052" y2="286.0" class="grid"/>
<text x="52" y="290.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="186.0" x2="1052" y2="186.0" class="grid"/>
<text x="52" y="190.0" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="86.0" x2="1052" y2="86.0" class="grid"/>
<text x="52" y="90.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
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
<line x1="60" y1="81.7" x2="1052" y2="81.7" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="84.7" font-size="10.5" fill="var(--muted)">$402 52주 최고</text>
<line x1="1010.5" y1="56.0" x2="1010.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="1016.5" y="68.0" font-size="10.5" fill="var(--down)">2026-07-31 Q2 실적발표 갭다운(52주 최저 경신)</text>
<line x1="62.0" y1="239.2" x2="62.0" y2="256.9" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="240.3" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="65.9" y1="237.4" x2="65.9" y2="271.8" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="244.5" width="2.45" height="18.5" fill="var(--up)"/>
<line x1="69.9" y1="240.8" x2="69.9" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="244.6" width="2.45" height="37.2" fill="var(--down)"/>
<line x1="73.8" y1="273.1" x2="73.8" y2="303.1" stroke="var(--up)" class="wick"/>
<rect x="72.61" y="277.2" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="77.8" y1="276.0" x2="77.8" y2="290.4" stroke="var(--down)" class="wick"/>
<rect x="76.56" y="283.2" width="2.45" height="2.3" fill="var(--down)"/>
<line x1="81.7" y1="241.5" x2="81.7" y2="291.6" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="246.3" width="2.45" height="38.5" fill="var(--up)"/>
<line x1="85.7" y1="254.8" x2="85.7" y2="275.8" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="261.6" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="89.6" y1="267.6" x2="89.6" y2="285.3" stroke="var(--up)" class="wick"/>
<rect x="88.42" y="269.0" width="2.45" height="9.0" fill="var(--up)"/>
<line x1="93.6" y1="261.2" x2="93.6" y2="272.6" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="268.1" width="2.45" height="3.5" fill="var(--up)"/>
<line x1="97.5" y1="254.1" x2="97.5" y2="274.0" stroke="var(--down)" class="wick"/>
<rect x="96.32" y="260.9" width="2.45" height="8.2" fill="var(--down)"/>
<line x1="101.5" y1="269.6" x2="101.5" y2="283.0" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="273.6" width="2.45" height="3.3" fill="var(--down)"/>
<line x1="105.5" y1="265.2" x2="105.5" y2="295.2" stroke="var(--up)" class="wick"/>
<rect x="104.23" y="278.9" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="109.4" y1="269.3" x2="109.4" y2="283.7" stroke="var(--down)" class="wick"/>
<rect x="108.18" y="276.0" width="2.45" height="5.4" fill="var(--down)"/>
<line x1="113.4" y1="270.5" x2="113.4" y2="286.0" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="272.4" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="117.3" y1="254.5" x2="117.3" y2="300.9" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="258.3" width="2.45" height="29.6" fill="var(--down)"/>
<line x1="121.3" y1="272.8" x2="121.3" y2="291.7" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="281.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="125.2" y1="247.2" x2="125.2" y2="278.8" stroke="var(--up)" class="wick"/>
<rect x="123.99" y="248.4" width="2.45" height="30.0" fill="var(--up)"/>
<line x1="129.2" y1="228.7" x2="129.2" y2="260.9" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="243.2" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="133.1" y1="234.0" x2="133.1" y2="254.9" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="238.1" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="137.1" y1="227.0" x2="137.1" y2="246.4" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="229.9" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="141.0" y1="229.1" x2="141.0" y2="244.1" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="232.0" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="145.0" y1="218.8" x2="145.0" y2="243.4" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="221.5" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="148.9" y1="229.0" x2="148.9" y2="263.4" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="234.1" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="152.9" y1="182.2" x2="152.9" y2="239.0" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="199.7" width="2.45" height="34.6" fill="var(--up)"/>
<line x1="156.8" y1="186.6" x2="156.8" y2="210.7" stroke="var(--down)" class="wick"/>
<rect x="155.60" y="200.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="160.8" y1="213.6" x2="160.8" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="159.56" y="219.1" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="164.7" y1="214.6" x2="164.7" y2="250.6" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="219.2" width="2.45" height="26.6" fill="var(--down)"/>
<line x1="168.7" y1="231.4" x2="168.7" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="238.5" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="172.6" y1="250.0" x2="172.6" y2="277.3" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="257.3" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="176.6" y1="257.5" x2="176.6" y2="279.2" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="260.8" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="180.5" y1="217.2" x2="180.5" y2="253.3" stroke="var(--up)" class="wick"/>
<rect x="179.32" y="218.0" width="2.45" height="32.0" fill="var(--up)"/>
<line x1="184.5" y1="209.8" x2="184.5" y2="226.7" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="211.0" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="188.4" y1="186.3" x2="188.4" y2="205.0" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="193.7" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="192.4" y1="133.7" x2="192.4" y2="179.2" stroke="var(--up)" class="wick"/>
<rect x="191.17" y="141.9" width="2.45" height="34.6" fill="var(--up)"/>
<line x1="196.4" y1="119.0" x2="196.4" y2="145.9" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="126.0" width="2.45" height="13.3" fill="var(--up)"/>
<line x1="200.3" y1="100.3" x2="200.3" y2="125.0" stroke="var(--down)" class="wick"/>
<rect x="199.08" y="105.3" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="204.3" y1="110.0" x2="204.3" y2="160.0" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="112.3" width="2.45" height="22.1" fill="var(--down)"/>
<line x1="208.2" y1="105.0" x2="208.2" y2="134.7" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="111.5" width="2.45" height="17.3" fill="var(--up)"/>
<line x1="212.2" y1="101.7" x2="212.2" y2="122.4" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="112.0" width="2.45" height="5.5" fill="var(--up)"/>
<line x1="216.1" y1="81.7" x2="216.1" y2="182.7" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="110.7" width="2.45" height="61.3" fill="var(--down)"/>
<line x1="220.1" y1="156.2" x2="220.1" y2="202.3" stroke="var(--down)" class="wick"/>
<rect x="218.84" y="159.6" width="2.45" height="12.4" fill="var(--down)"/>
<line x1="224.0" y1="179.0" x2="224.0" y2="216.5" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="202.9" width="2.45" height="1.4" fill="var(--up)"/>
<line x1="228.0" y1="190.3" x2="228.0" y2="219.8" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="194.4" width="2.45" height="19.0" fill="var(--down)"/>
<line x1="231.9" y1="200.6" x2="231.9" y2="228.6" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="209.0" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="235.9" y1="213.4" x2="235.9" y2="250.5" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="214.0" width="2.45" height="33.2" fill="var(--up)"/>
<line x1="239.8" y1="177.9" x2="239.8" y2="208.5" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="198.4" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="243.8" y1="196.4" x2="243.8" y2="215.0" stroke="var(--down)" class="wick"/>
<rect x="242.55" y="201.4" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="247.7" y1="216.6" x2="247.7" y2="265.0" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="218.2" width="2.45" height="27.1" fill="var(--down)"/>
<line x1="251.7" y1="229.2" x2="251.7" y2="249.0" stroke="var(--down)" class="wick"/>
<rect x="250.46" y="240.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="255.6" y1="172.2" x2="255.6" y2="220.0" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="177.1" width="2.45" height="38.9" fill="var(--up)"/>
<line x1="259.6" y1="139.5" x2="259.6" y2="171.4" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="160.4" width="2.45" height="2.8" fill="var(--down)"/>
<line x1="263.5" y1="149.7" x2="263.5" y2="177.9" stroke="var(--down)" class="wick"/>
<rect x="262.31" y="159.5" width="2.45" height="16.0" fill="var(--down)"/>
<line x1="267.5" y1="166.0" x2="267.5" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="266.26" y="171.1" width="2.45" height="17.6" fill="var(--down)"/>
<line x1="271.4" y1="197.6" x2="271.4" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="199.1" width="2.45" height="29.9" fill="var(--down)"/>
<line x1="275.4" y1="163.2" x2="275.4" y2="217.1" stroke="var(--up)" class="wick"/>
<rect x="274.17" y="198.4" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="279.3" y1="200.4" x2="279.3" y2="234.2" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="204.3" width="2.45" height="20.9" fill="var(--down)"/>
<line x1="283.3" y1="235.1" x2="283.3" y2="272.3" stroke="var(--down)" class="wick"/>
<rect x="282.07" y="248.0" width="2.45" height="23.4" fill="var(--down)"/>
<line x1="287.3" y1="237.7" x2="287.3" y2="264.3" stroke="var(--up)" class="wick"/>
<rect x="286.03" y="247.4" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="291.2" y1="252.8" x2="291.2" y2="296.6" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="253.0" width="2.45" height="42.6" fill="var(--down)"/>
<line x1="295.2" y1="264.1" x2="295.2" y2="318.7" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="267.7" width="2.45" height="37.9" fill="var(--up)"/>
<line x1="299.1" y1="236.4" x2="299.1" y2="262.7" stroke="var(--down)" class="wick"/>
<rect x="297.88" y="240.0" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="303.1" y1="251.8" x2="303.1" y2="278.8" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="261.6" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="307.0" y1="263.0" x2="307.0" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="267.5" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="311.0" y1="278.1" x2="311.0" y2="326.3" stroke="var(--down)" class="wick"/>
<rect x="309.74" y="282.7" width="2.45" height="37.0" fill="var(--down)"/>
<line x1="314.9" y1="300.5" x2="314.9" y2="349.7" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="318.0" width="2.45" height="29.0" fill="var(--up)"/>
<line x1="318.9" y1="330.3" x2="318.9" y2="369.6" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="336.2" width="2.45" height="21.9" fill="var(--down)"/>
<line x1="322.8" y1="344.0" x2="322.8" y2="364.0" stroke="var(--up)" class="wick"/>
<rect x="321.60" y="362.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="326.8" y1="360.4" x2="326.8" y2="392.0" stroke="var(--down)" class="wick"/>
<rect x="325.55" y="362.3" width="2.45" height="9.2" fill="var(--down)"/>
<line x1="330.7" y1="358.7" x2="330.7" y2="414.0" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="366.0" width="2.45" height="43.6" fill="var(--down)"/>
<line x1="334.7" y1="393.7" x2="334.7" y2="423.7" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="398.2" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="338.6" y1="370.1" x2="338.6" y2="400.0" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="374.1" width="2.45" height="22.6" fill="var(--up)"/>
<line x1="342.6" y1="377.3" x2="342.6" y2="404.5" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="377.8" width="2.45" height="12.7" fill="var(--up)"/>
<line x1="346.5" y1="352.8" x2="346.5" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="345.31" y="356.1" width="2.45" height="17.5" fill="var(--up)"/>
<line x1="350.5" y1="326.3" x2="350.5" y2="347.4" stroke="var(--down)" class="wick"/>
<rect x="349.26" y="338.0" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="354.4" y1="354.2" x2="354.4" y2="381.6" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="364.9" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="358.4" y1="340.9" x2="358.4" y2="359.6" stroke="var(--down)" class="wick"/>
<rect x="357.17" y="350.6" width="2.45" height="8.8" fill="var(--down)"/>
<line x1="362.3" y1="330.8" x2="362.3" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="332.2" width="2.45" height="17.8" fill="var(--up)"/>
<line x1="366.3" y1="317.5" x2="366.3" y2="343.5" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="337.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="370.2" y1="337.9" x2="370.2" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="345.1" width="2.45" height="1.4" fill="var(--down)"/>
<line x1="374.2" y1="332.7" x2="374.2" y2="347.0" stroke="var(--up)" class="wick"/>
<rect x="372.97" y="337.6" width="2.45" height="2.8" fill="var(--up)"/>
<line x1="378.2" y1="316.5" x2="378.2" y2="352.3" stroke="var(--up)" class="wick"/>
<rect x="376.93" y="331.3" width="2.45" height="13.5" fill="var(--up)"/>
<line x1="382.1" y1="327.1" x2="382.1" y2="344.5" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="335.8" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="386.1" y1="343.7" x2="386.1" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="384.83" y="348.0" width="2.45" height="4.2" fill="var(--up)"/>
<line x1="390.0" y1="329.6" x2="390.0" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="342.7" width="2.45" height="8.4" fill="var(--down)"/>
<line x1="394.0" y1="348.8" x2="394.0" y2="392.4" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="350.0" width="2.45" height="35.1" fill="var(--down)"/>
<line x1="397.9" y1="372.0" x2="397.9" y2="385.4" stroke="var(--down)" class="wick"/>
<rect x="396.69" y="378.9" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="401.9" y1="366.9" x2="401.9" y2="398.6" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="376.4" width="2.45" height="21.2" fill="var(--down)"/>
<line x1="405.8" y1="375.2" x2="405.8" y2="407.8" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="379.8" width="2.45" height="27.8" fill="var(--down)"/>
<line x1="409.8" y1="392.0" x2="409.8" y2="404.3" stroke="var(--up)" class="wick"/>
<rect x="408.54" y="395.8" width="2.45" height="1.1" fill="var(--up)"/>
<line x1="413.7" y1="376.3" x2="413.7" y2="391.1" stroke="var(--down)" class="wick"/>
<rect x="412.50" y="382.6" width="2.45" height="7.6" fill="var(--down)"/>
<line x1="417.7" y1="395.6" x2="417.7" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="416.45" y="399.5" width="2.45" height="1.9" fill="var(--down)"/>
<line x1="421.6" y1="404.0" x2="421.6" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="420.40" y="405.4" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="425.6" y1="405.0" x2="425.6" y2="420.4" stroke="var(--down)" class="wick"/>
<rect x="424.35" y="405.2" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="429.5" y1="406.2" x2="429.5" y2="420.4" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="417.3" width="2.45" height="1.2" fill="var(--down)"/>
<line x1="433.5" y1="413.9" x2="433.5" y2="423.0" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="418.7" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="437.4" y1="421.2" x2="437.4" y2="435.1" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="423.6" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="441.4" y1="409.0" x2="441.4" y2="434.2" stroke="var(--up)" class="wick"/>
<rect x="440.16" y="412.9" width="2.45" height="11.9" fill="var(--up)"/>
<line x1="445.3" y1="368.2" x2="445.3" y2="392.9" stroke="var(--up)" class="wick"/>
<rect x="444.11" y="376.2" width="2.45" height="15.6" fill="var(--up)"/>
<line x1="449.3" y1="369.3" x2="449.3" y2="394.6" stroke="var(--down)" class="wick"/>
<rect x="448.07" y="375.6" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="453.2" y1="388.1" x2="453.2" y2="405.5" stroke="var(--down)" class="wick"/>
<rect x="452.02" y="389.4" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="457.2" y1="385.2" x2="457.2" y2="401.5" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="394.8" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="461.1" y1="392.2" x2="461.1" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="459.92" y="393.9" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="465.1" y1="390.0" x2="465.1" y2="409.9" stroke="var(--up)" class="wick"/>
<rect x="463.87" y="400.0" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="469.1" y1="375.0" x2="469.1" y2="396.7" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="380.6" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="473.0" y1="359.9" x2="473.0" y2="380.0" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="372.2" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="477.0" y1="383.6" x2="477.0" y2="411.1" stroke="var(--down)" class="wick"/>
<rect x="475.73" y="384.8" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="480.9" y1="399.6" x2="480.9" y2="413.7" stroke="var(--up)" class="wick"/>
<rect x="479.68" y="403.7" width="2.45" height="3.3" fill="var(--up)"/>
<line x1="484.9" y1="416.2" x2="484.9" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="420.7" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="488.8" y1="423.1" x2="488.8" y2="441.2" stroke="var(--down)" class="wick"/>
<rect x="487.59" y="428.5" width="2.45" height="3.7" fill="var(--down)"/>
<line x1="492.8" y1="424.5" x2="492.8" y2="440.0" stroke="var(--down)" class="wick"/>
<rect x="491.54" y="428.9" width="2.45" height="10.8" fill="var(--down)"/>
<line x1="496.7" y1="440.5" x2="496.7" y2="454.6" stroke="var(--down)" class="wick"/>
<rect x="495.49" y="440.5" width="2.45" height="11.6" fill="var(--down)"/>
<line x1="500.7" y1="454.7" x2="500.7" y2="464.2" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="459.0" width="2.45" height="2.6" fill="var(--up)"/>
<line x1="504.6" y1="458.9" x2="504.6" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="459.0" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="508.6" y1="457.2" x2="508.6" y2="472.4" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="459.4" width="2.45" height="7.7" fill="var(--down)"/>
<line x1="512.5" y1="472.0" x2="512.5" y2="497.6" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="472.4" width="2.45" height="15.3" fill="var(--down)"/>
<line x1="516.5" y1="488.1" x2="516.5" y2="504.1" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="488.6" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="520.4" y1="504.1" x2="520.4" y2="515.8" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="506.4" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="524.4" y1="508.6" x2="524.4" y2="537.9" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="508.6" width="2.45" height="18.0" fill="var(--down)"/>
<line x1="528.3" y1="532.5" x2="528.3" y2="557.2" stroke="var(--down)" class="wick"/>
<rect x="527.11" y="533.8" width="2.45" height="15.0" fill="var(--down)"/>
<line x1="532.3" y1="556.0" x2="532.3" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="565.1" width="2.45" height="28.6" fill="var(--down)"/>
<line x1="536.2" y1="555.0" x2="536.2" y2="582.9" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="555.8" width="2.45" height="21.1" fill="var(--up)"/>
<line x1="540.2" y1="550.9" x2="540.2" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="551.5" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="544.1" y1="550.2" x2="544.1" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="542.92" y="560.9" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="548.1" y1="569.8" x2="548.1" y2="588.3" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="570.6" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="552.0" y1="579.6" x2="552.0" y2="607.3" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="579.8" width="2.45" height="24.0" fill="var(--down)"/>
<line x1="556.0" y1="550.7" x2="556.0" y2="593.7" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="557.4" width="2.45" height="21.2" fill="var(--up)"/>
<line x1="560.0" y1="544.9" x2="560.0" y2="569.2" stroke="var(--up)" class="wick"/>
<rect x="558.73" y="554.0" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="563.9" y1="538.2" x2="563.9" y2="559.7" stroke="var(--down)" class="wick"/>
<rect x="562.68" y="555.2" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="567.9" y1="550.8" x2="567.9" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="566.63" y="554.1" width="2.45" height="7.0" fill="var(--up)"/>
<line x1="571.8" y1="534.9" x2="571.8" y2="557.8" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="543.3" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="575.8" y1="549.8" x2="575.8" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="553.7" width="2.45" height="11.8" fill="var(--down)"/>
<line x1="579.7" y1="561.4" x2="579.7" y2="580.6" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="561.9" width="2.45" height="12.4" fill="var(--up)"/>
<line x1="583.7" y1="514.4" x2="583.7" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="518.1" width="2.45" height="24.3" fill="var(--up)"/>
<line x1="587.6" y1="513.2" x2="587.6" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="523.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="591.6" y1="527.9" x2="591.6" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="534.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="595.5" y1="513.3" x2="595.5" y2="541.6" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="515.5" width="2.45" height="25.5" fill="var(--up)"/>
<line x1="599.5" y1="513.4" x2="599.5" y2="541.9" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="521.3" width="2.45" height="10.4" fill="var(--up)"/>
<line x1="603.4" y1="461.9" x2="603.4" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="468.1" width="2.45" height="26.0" fill="var(--up)"/>
<line x1="607.4" y1="459.0" x2="607.4" y2="483.0" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="474.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="611.3" y1="480.5" x2="611.3" y2="496.7" stroke="var(--down)" class="wick"/>
<rect x="610.11" y="490.5" width="2.45" height="1.1" fill="var(--down)"/>
<line x1="615.3" y1="479.0" x2="615.3" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="486.4" width="2.45" height="3.6" fill="var(--up)"/>
<line x1="619.2" y1="474.0" x2="619.2" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="477.1" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="623.2" y1="479.8" x2="623.2" y2="501.0" stroke="var(--up)" class="wick"/>
<rect x="621.96" y="488.7" width="2.45" height="2.2" fill="var(--up)"/>
<line x1="627.1" y1="490.0" x2="627.1" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="493.7" width="2.45" height="5.8" fill="var(--down)"/>
<line x1="631.1" y1="471.7" x2="631.1" y2="498.3" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="478.5" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="635.0" y1="473.1" x2="635.0" y2="488.8" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="479.4" width="2.45" height="3.0" fill="var(--up)"/>
<line x1="639.0" y1="459.1" x2="639.0" y2="481.7" stroke="var(--up)" class="wick"/>
<rect x="637.77" y="465.5" width="2.45" height="15.9" fill="var(--up)"/>
<line x1="642.9" y1="468.0" x2="642.9" y2="483.7" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="472.5" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="646.9" y1="475.0" x2="646.9" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="645.68" y="480.2" width="2.45" height="15.1" fill="var(--up)"/>
<line x1="650.9" y1="479.4" x2="650.9" y2="496.4" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="481.0" width="2.45" height="10.0" fill="var(--down)"/>
<line x1="654.8" y1="478.1" x2="654.8" y2="493.8" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="484.8" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="658.8" y1="482.5" x2="658.8" y2="530.8" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="487.8" width="2.45" height="36.1" fill="var(--down)"/>
<line x1="662.7" y1="504.6" x2="662.7" y2="525.9" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="516.8" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="666.7" y1="526.5" x2="666.7" y2="542.1" stroke="var(--down)" class="wick"/>
<rect x="665.44" y="532.0" width="2.45" height="7.2" fill="var(--down)"/>
<line x1="670.6" y1="548.5" x2="670.6" y2="566.3" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="549.9" width="2.45" height="13.8" fill="var(--down)"/>
<line x1="674.6" y1="553.0" x2="674.6" y2="569.1" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="556.9" width="2.45" height="7.5" fill="var(--down)"/>
<line x1="678.5" y1="534.3" x2="678.5" y2="561.6" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="536.8" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="682.5" y1="527.4" x2="682.5" y2="542.6" stroke="var(--down)" class="wick"/>
<rect x="681.24" y="528.0" width="2.45" height="12.0" fill="var(--down)"/>
<line x1="686.4" y1="539.9" x2="686.4" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="543.1" width="2.45" height="7.7" fill="var(--up)"/>
<line x1="690.4" y1="530.2" x2="690.4" y2="539.1" stroke="var(--down)" class="wick"/>
<rect x="689.15" y="535.8" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="694.3" y1="535.5" x2="694.3" y2="553.9" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="535.6" width="2.45" height="6.1" fill="var(--up)"/>
<line x1="698.3" y1="506.9" x2="698.3" y2="540.1" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="510.2" width="2.45" height="25.6" fill="var(--down)"/>
<line x1="702.2" y1="531.7" x2="702.2" y2="553.2" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="534.3" width="2.45" height="13.6" fill="var(--down)"/>
<line x1="706.2" y1="545.0" x2="706.2" y2="559.7" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="547.3" width="2.45" height="3.0" fill="var(--down)"/>
<line x1="710.1" y1="536.0" x2="710.1" y2="557.3" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="536.9" width="2.45" height="19.4" fill="var(--up)"/>
<line x1="714.1" y1="511.7" x2="714.1" y2="526.0" stroke="var(--up)" class="wick"/>
<rect x="712.86" y="517.2" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="718.0" y1="493.1" x2="718.0" y2="519.0" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="494.2" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="722.0" y1="484.8" x2="722.0" y2="509.0" stroke="var(--up)" class="wick"/>
<rect x="720.77" y="486.3" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="725.9" y1="453.9" x2="725.9" y2="480.1" stroke="var(--up)" class="wick"/>
<rect x="724.72" y="473.3" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="729.9" y1="461.4" x2="729.9" y2="486.0" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="462.7" width="2.45" height="21.2" fill="var(--up)"/>
<line x1="733.8" y1="463.5" x2="733.8" y2="496.8" stroke="var(--down)" class="wick"/>
<rect x="732.62" y="463.6" width="2.45" height="30.5" fill="var(--down)"/>
<line x1="737.8" y1="462.1" x2="737.8" y2="481.3" stroke="var(--up)" class="wick"/>
<rect x="736.58" y="473.5" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="741.8" y1="474.4" x2="741.8" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="481.4" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="745.7" y1="480.9" x2="745.7" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="744.48" y="481.8" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="749.7" y1="477.0" x2="749.7" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="748.43" y="487.8" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="753.6" y1="494.1" x2="753.6" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="752.38" y="497.8" width="2.45" height="7.8" fill="var(--up)"/>
<line x1="757.6" y1="511.5" x2="757.6" y2="530.8" stroke="var(--down)" class="wick"/>
<rect x="756.34" y="511.5" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="761.5" y1="506.9" x2="761.5" y2="526.2" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="510.5" width="2.45" height="12.3" fill="var(--up)"/>
<line x1="765.5" y1="497.0" x2="765.5" y2="506.3" stroke="var(--down)" class="wick"/>
<rect x="764.24" y="502.2" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="769.4" y1="472.6" x2="769.4" y2="490.3" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="480.0" width="2.45" height="7.2" fill="var(--up)"/>
<line x1="773.4" y1="468.2" x2="773.4" y2="497.2" stroke="var(--down)" class="wick"/>
<rect x="772.15" y="468.2" width="2.45" height="22.3" fill="var(--down)"/>
<line x1="777.3" y1="489.0" x2="777.3" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="490.1" width="2.45" height="4.4" fill="var(--up)"/>
<line x1="781.3" y1="489.7" x2="781.3" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="493.9" width="2.45" height="6.1" fill="var(--down)"/>
<line x1="785.2" y1="483.3" x2="785.2" y2="520.4" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="483.7" width="2.45" height="30.2" fill="var(--up)"/>
<line x1="789.2" y1="450.3" x2="789.2" y2="500.4" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="452.8" width="2.45" height="32.4" fill="var(--up)"/>
<line x1="793.1" y1="449.1" x2="793.1" y2="485.6" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="462.2" width="2.45" height="8.5" fill="var(--down)"/>
<line x1="797.1" y1="477.6" x2="797.1" y2="491.0" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="477.6" width="2.45" height="4.8" fill="var(--down)"/>
<line x1="801.0" y1="441.3" x2="801.0" y2="495.8" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="462.0" width="2.45" height="21.5" fill="var(--up)"/>
<line x1="805.0" y1="474.0" x2="805.0" y2="501.4" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="474.7" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="808.9" y1="497.6" x2="808.9" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="505.5" width="2.45" height="1.6" fill="var(--down)"/>
<line x1="812.9" y1="494.9" x2="812.9" y2="514.9" stroke="var(--up)" class="wick"/>
<rect x="811.67" y="499.1" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="816.8" y1="492.8" x2="816.8" y2="506.5" stroke="var(--down)" class="wick"/>
<rect x="815.62" y="498.5" width="2.45" height="4.9" fill="var(--down)"/>
<line x1="820.8" y1="494.6" x2="820.8" y2="510.7" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="498.9" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="824.7" y1="494.8" x2="824.7" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="823.52" y="498.0" width="2.45" height="18.1" fill="var(--down)"/>
<line x1="828.7" y1="510.4" x2="828.7" y2="527.8" stroke="var(--down)" class="wick"/>
<rect x="827.48" y="513.9" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="832.7" y1="526.3" x2="832.7" y2="538.6" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="533.2" width="2.45" height="5.2" fill="var(--down)"/>
<line x1="836.6" y1="520.7" x2="836.6" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="835.38" y="521.5" width="2.45" height="23.5" fill="var(--up)"/>
<line x1="840.6" y1="502.3" x2="840.6" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="839.33" y="507.9" width="2.45" height="17.6" fill="var(--up)"/>
<line x1="844.5" y1="512.8" x2="844.5" y2="533.6" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="520.8" width="2.45" height="6.8" fill="var(--up)"/>
<line x1="848.5" y1="528.9" x2="848.5" y2="542.7" stroke="var(--down)" class="wick"/>
<rect x="847.24" y="531.7" width="2.45" height="6.4" fill="var(--down)"/>
<line x1="852.4" y1="542.0" x2="852.4" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="542.9" width="2.45" height="16.6" fill="var(--down)"/>
<line x1="856.4" y1="553.0" x2="856.4" y2="562.2" stroke="var(--down)" class="wick"/>
<rect x="855.14" y="557.6" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="860.3" y1="568.6" x2="860.3" y2="590.2" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="568.6" width="2.45" height="12.6" fill="var(--down)"/>
<line x1="864.3" y1="557.4" x2="864.3" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="561.8" width="2.45" height="11.0" fill="var(--up)"/>
<line x1="868.2" y1="556.0" x2="868.2" y2="586.2" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="571.5" width="2.45" height="3.5" fill="var(--down)"/>
<line x1="872.2" y1="562.6" x2="872.2" y2="581.6" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="578.1" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="876.1" y1="562.5" x2="876.1" y2="581.2" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="565.1" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="880.1" y1="555.0" x2="880.1" y2="575.2" stroke="var(--down)" class="wick"/>
<rect x="878.85" y="565.1" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="884.0" y1="537.1" x2="884.0" y2="548.7" stroke="var(--down)" class="wick"/>
<rect x="882.81" y="546.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="888.0" y1="538.4" x2="888.0" y2="552.2" stroke="var(--down)" class="wick"/>
<rect x="886.76" y="547.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="891.9" y1="537.8" x2="891.9" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="890.71" y="552.9" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="895.9" y1="546.4" x2="895.9" y2="564.9" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="550.5" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="899.8" y1="533.0" x2="899.8" y2="559.9" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="556.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="903.8" y1="557.7" x2="903.8" y2="573.4" stroke="var(--up)" class="wick"/>
<rect x="902.57" y="569.6" width="2.45" height="2.4" fill="var(--up)"/>
<line x1="907.7" y1="569.2" x2="907.7" y2="589.4" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="569.4" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="911.7" y1="581.6" x2="911.7" y2="603.0" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="583.7" width="2.45" height="17.3" fill="var(--down)"/>
<line x1="915.6" y1="586.3" x2="915.6" y2="607.6" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="587.9" width="2.45" height="19.7" fill="var(--up)"/>
<line x1="919.6" y1="581.1" x2="919.6" y2="595.4" stroke="var(--up)" class="wick"/>
<rect x="918.38" y="582.7" width="2.45" height="1.7" fill="var(--up)"/>
<line x1="923.6" y1="588.3" x2="923.6" y2="601.4" stroke="var(--down)" class="wick"/>
<rect x="922.33" y="589.6" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="927.5" y1="556.9" x2="927.5" y2="593.4" stroke="var(--up)" class="wick"/>
<rect x="926.28" y="567.5" width="2.45" height="24.2" fill="var(--up)"/>
<line x1="931.5" y1="539.8" x2="931.5" y2="559.6" stroke="var(--up)" class="wick"/>
<rect x="930.23" y="555.0" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="935.4" y1="542.7" x2="935.4" y2="565.8" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="548.3" width="2.45" height="15.0" fill="var(--up)"/>
<line x1="939.4" y1="545.8" x2="939.4" y2="562.6" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="552.4" width="2.45" height="6.6" fill="var(--down)"/>
<line x1="943.3" y1="562.8" x2="943.3" y2="573.6" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="567.3" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="947.3" y1="563.9" x2="947.3" y2="576.4" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="569.1" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="951.2" y1="550.0" x2="951.2" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="552.7" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="955.2" y1="563.6" x2="955.2" y2="578.0" stroke="var(--up)" class="wick"/>
<rect x="953.95" y="571.3" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="959.1" y1="561.5" x2="959.1" y2="571.5" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="563.0" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="963.1" y1="549.0" x2="963.1" y2="565.3" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="551.6" width="2.45" height="4.1" fill="var(--up)"/>
<line x1="967.0" y1="552.9" x2="967.0" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="555.3" width="2.45" height="9.8" fill="var(--down)"/>
<line x1="971.0" y1="564.4" x2="971.0" y2="580.8" stroke="var(--up)" class="wick"/>
<rect x="969.75" y="571.8" width="2.45" height="7.5" fill="var(--up)"/>
<line x1="974.9" y1="556.6" x2="974.9" y2="575.7" stroke="var(--up)" class="wick"/>
<rect x="973.71" y="565.1" width="2.45" height="4.5" fill="var(--up)"/>
<line x1="978.9" y1="523.0" x2="978.9" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="534.3" width="2.45" height="15.9" fill="var(--up)"/>
<line x1="982.8" y1="536.1" x2="982.8" y2="554.0" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="541.5" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="986.8" y1="554.5" x2="986.8" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="559.8" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="990.7" y1="563.8" x2="990.7" y2="578.4" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="563.8" width="2.45" height="5.6" fill="var(--down)"/>
<line x1="994.7" y1="550.3" x2="994.7" y2="565.2" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="551.0" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="998.6" y1="549.7" x2="998.6" y2="568.8" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="550.2" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="1002.6" y1="546.6" x2="1002.6" y2="568.6" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="553.7" width="2.45" height="12.1" fill="var(--down)"/>
<line x1="1006.5" y1="556.4" x2="1006.5" y2="567.4" stroke="var(--up)" class="wick"/>
<rect x="1005.32" y="558.8" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="1010.5" y1="578.6" x2="1010.5" y2="607.8" stroke="var(--down)" class="wick"/>
<rect x="1009.28" y="579.8" width="2.45" height="13.7" fill="var(--down)"/>
<line x1="1014.5" y1="581.1" x2="1014.5" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="1013.23" y="593.0" width="2.45" height="4.7" fill="var(--up)"/>
<line x1="1018.4" y1="580.2" x2="1018.4" y2="594.8" stroke="var(--up)" class="wick"/>
<rect x="1017.18" y="584.5" width="2.45" height="6.7" fill="var(--up)"/>
<line x1="1022.4" y1="578.0" x2="1022.4" y2="590.8" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="584.4" width="2.45" height="1.8" fill="var(--down)"/>
<line x1="1026.3" y1="584.8" x2="1026.3" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="1025.09" y="592.5" width="2.45" height="2.7" fill="var(--down)"/>
<line x1="1030.3" y1="575.2" x2="1030.3" y2="594.9" stroke="var(--up)" class="wick"/>
<rect x="1029.04" y="578.8" width="2.45" height="10.8" fill="var(--up)"/>
<line x1="1034.2" y1="578.8" x2="1034.2" y2="590.2" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="579.3" width="2.45" height="9.3" fill="var(--down)"/>
<line x1="1038.2" y1="580.1" x2="1038.2" y2="593.4" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="586.3" width="2.45" height="2.5" fill="var(--down)"/>
<line x1="1042.1" y1="583.0" x2="1042.1" y2="591.0" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="585.8" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="1046.1" y1="577.2" x2="1046.1" y2="592.1" stroke="var(--up)" class="wick"/>
<rect x="1044.85" y="578.2" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="1050.0" y1="580.8" x2="1050.0" y2="590.3" stroke="var(--down)" class="wick"/>
<rect x="1048.80" y="583.2" width="2.45" height="5.9" fill="var(--down)"/>
<line x1="60" y1="536.4" x2="1052" y2="536.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="539.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$175 R1</text>
<text x="1058" y="551.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="457.3" x2="1052" y2="457.3" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="460.8" font-size="11.5" fill="var(--resistance)" font-weight="600">$214 R2</text>
<text x="1058" y="472.8" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="364.0" x2="1052" y2="364.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="367.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$261 R3</text>
<text x="1058" y="379.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="607.6" x2="1052" y2="607.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="601.6" font-size="11.5" fill="var(--support)" font-weight="600">$139 S1 (52주 최저)</text>
<text x="1058" y="613.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="589.1" r="3" fill="var(--ink)"/>
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
| R3 | $261 | 2 | 2025년 11월 중순~2026년 1월 중순 스윙 고점대(하락 랠리 중 되돌림 상단) |
| R2 | $214 | 3 | 2026년 1월 말~5월 초 스윙 고점대(1분기 내내 반복된 저항) |
| R1 | $175 | 2 | 2026년 2월~7월 스윙 고점대(가장 최근까지 반복 테스트된 저항) |
| **현재가** | **$148.47** (2026-08-14 종가) | — | R1과 S1 (52주 최저) 사이 |
| S1 (52주 최저) | $139 | 3 | 2026-07-31 Q2 실적발표 갭다운 당일 저가(52주 최저) — 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운 참고. 터치 3회는 2026-02-12·2026-06-25~08-03 구간의 근접 저점을 묶은 것 |
| 참고선 | $402 | — | 52주 최고(2025-08-15 구간 초입 부근) — 이후 1년 내내 하락 추세라 근시일 저항으로 보지 않음 |

> 레벨은 4개(위 3개 + 강제 포함 S1)만 나왔다 — 상단(R1~R3)은 2025년 11월~2026년 5월 사이 하락 국면에서 순차적으로 남긴 스윙 고점대이고, 하단은 터치 2회 이상 조건을 만족하는 자연 클러스터가 없어(최근 저점대가 아직 반복 테스트되는 초기 단계) 52주 최저가를 `--force-level`로 강제 포함했다.

---

## 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운

- 2026-07-30(현지시각 장 마감 후) 발표된 2026년 2분기 실적(GAAP 순손실 약 $359.5M, 매출 3개 분기 연속 YoY 역성장 — [최근 뉴스 / 이슈](./08_news.md) 2026-07-30 항목·[재무 / 실적](./05_financials.md) 1. 성장성~2. 수익성 참고) 반영 첫 거래일인 2026-07-31에 급락했다.
- 종가 기준 전일(2026-07-30, $163.58) 대비 **-10.6%** ($163.58 → $146.26), 장중에는 52주 최저가 $139.11까지 하락했다. 거래량은 20,870,300주로 최근 1년 일평균(약 979만 주) 대비 약 **2.1배**.
- 이 하루의 저가($139.11)가 그대로 2. 지지선 / 저항선 요약의 S1(52주 최저) 레벨이 됐다 — 아직 반복적으로 테스트된 지지대는 아니고(터치 2회는 2026-02-12·2026-07-31~08-03 구간에서 나온 근접 저점들을 묶은 결과), 그만큼 이 레벨이 "지지선으로 검증됐다"기보다 "가장 최근에 시장이 매긴 바닥"에 가깝다는 점에 유의해야 한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-15. 원주가(과거 분할은 소급 반영, 배당은 미반영) — Coinbase는 2021년 상장 이후 분할·병합 이력이 없어(역사 / 주요 이벤트) 이 구간에는 소급조정 이슈가 없다.
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 2. 지지선 / 저항선 요약의 S1 — 강제 포함 사유 명시).
- **생성**: `scripts/gen_technical_chart.py COIN --name Coinbase --event 2026-07-31:"Q2 실적발표 갭다운(52주 최저 경신)" --ref-line 402.16:"52주 최고" --force-level '139.11:(52주 최저)' --close-on 2026-08-13 --close-on 2025-12-31`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다(기본값 그대로 사용, `--levels`·`--min-touches` 조정 없음).
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 적용한 것이며, 최적화된 값이 아니다.
    - 최근 1년이 대부분 하락 추세(2025-08-15 $317.55 → 2026-08-14 $148.47, -53.2%)라 상단 레벨(R1~R3)이 전부 "하락 도중 남긴 저항"이고, 상승 전환 이후에 형성될 새로운 저항 구조는 이 표본에 없다 — 추세 반전 시 레벨의 유효성이 낮아질 수 있다.
    - 3. 관측된 특이 구간 — 2026-07-31 Q2 실적발표 갭다운의 급락 이후 구간(2026-08 초)은 아직 거래일 수가 짧아, S1 레벨이 실제로 반복 테스트를 거친 지지선인지는 앞으로 몇 개월 데이터가 더 쌓여야 판단할 수 있다.

---

*작성일: 2026-08-23*
