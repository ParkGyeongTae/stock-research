# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API(Yahoo Finance)에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). 겹치는 시점의 종가를 대조한 결과(이 문서 수집 시점 2026-08-15 기준): **2026-08-13 종가 $323.77**은 당시 [밸류에이션 / 적정주가](./06_valuation.md) §6에 인용된 stockanalysis.com 값과 정확히 일치했다. 두 문서 모두 수정주가(배당·분할 미반영, Cadence는 표 기간 내 분할 이력 없음) 기준이라 대조에 문제가 없다. ⚠️ **이후 갱신 참고**: 핵심 지표·밸류에이션 / 적정주가·투자 판단는 2026-08-21 종가($319.02) 기준으로 갱신됐으나(2026-08-22), 이 일봉 차트 자체는 아직 2026-08-14까지의 데이터만 반영한다 — 차트를 최신 가격까지 재생성하기 전까지는 이 문서의 "현재가"($324.82)가 다른 문서보다 며칠 뒤처져 있다는 점에 유의할 것.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-15 ~ 2026-08-14)

<div class="cdns-chart">
<style>
.cdns-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .cdns-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .cdns-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.cdns-chart svg { width:100%; height:auto; display:block; }
.cdns-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.cdns-chart .title { fill: var(--ink); font-weight:600; }
.cdns-chart .grid { stroke: var(--grid); stroke-width:1; }
.cdns-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cadence Design Systems(CDNS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Cadence Design Systems (CDNS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-15 ~ 2026-08-14 · 마지막 종가 $324.82 (2026-08-14) · 단위 USD</text>
<line x1="60" y1="565.5" x2="1052" y2="565.5" class="grid"/>
<text x="52" y="569.5" font-size="11" text-anchor="end" fill="var(--muted)">275</text>
<line x1="60" y1="479.2" x2="1052" y2="479.2" class="grid"/>
<text x="52" y="483.2" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="392.8" x2="1052" y2="392.8" class="grid"/>
<text x="52" y="396.8" font-size="11" text-anchor="end" fill="var(--muted)">325</text>
<line x1="60" y1="306.5" x2="1052" y2="306.5" class="grid"/>
<text x="52" y="310.5" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="220.1" x2="1052" y2="220.1" class="grid"/>
<text x="52" y="224.1" font-size="11" text-anchor="end" fill="var(--muted)">375</text>
<line x1="60" y1="133.7" x2="1052" y2="133.7" class="grid"/>
<text x="52" y="137.7" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
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
<line x1="60" y1="76.1" x2="1052" y2="76.1" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="79.1" font-size="10.5" fill="var(--muted)">$417 52주 최고</text>
<line x1="844.5" y1="56.0" x2="844.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="850.5" y="68.0" font-size="10.5" fill="var(--down)">2026-06-01 ChipStack AI 발표·Samsung Foundry 협력 급등</text>
<line x1="971.0" y1="56.0" x2="971.0" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="977.0" y="68.0" font-size="10.5" fill="var(--down)">2026-07-17 Moonshot Kimi K3 발표發 AI 밸류에이션 우려 급락</text>
<line x1="62.0" y1="302.9" x2="62.0" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="306.9" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="65.9" y1="282.6" x2="65.9" y2="313.2" stroke="var(--up)" class="wick"/>
<rect x="64.70" y="284.9" width="2.45" height="24.0" fill="var(--up)"/>
<line x1="69.9" y1="287.5" x2="69.9" y2="320.1" stroke="var(--down)" class="wick"/>
<rect x="68.66" y="292.6" width="2.45" height="24.6" fill="var(--down)"/>
<line x1="73.8" y1="318.8" x2="73.8" y2="342.3" stroke="var(--down)" class="wick"/>
<rect x="72.61" y="319.6" width="2.45" height="2.6" fill="var(--down)"/>
<line x1="77.8" y1="310.5" x2="77.8" y2="329.0" stroke="var(--up)" class="wick"/>
<rect x="76.56" y="314.8" width="2.45" height="14.2" fill="var(--up)"/>
<line x1="81.7" y1="289.3" x2="81.7" y2="317.5" stroke="var(--up)" class="wick"/>
<rect x="80.51" y="307.7" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="85.7" y1="309.7" x2="85.7" y2="324.9" stroke="var(--down)" class="wick"/>
<rect x="84.46" y="316.8" width="2.45" height="6.3" fill="var(--down)"/>
<line x1="89.6" y1="321.8" x2="89.6" y2="330.2" stroke="var(--down)" class="wick"/>
<rect x="88.42" y="326.7" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="93.6" y1="314.5" x2="93.6" y2="330.3" stroke="var(--up)" class="wick"/>
<rect x="92.37" y="317.2" width="2.45" height="6.5" fill="var(--up)"/>
<line x1="97.5" y1="287.5" x2="97.5" y2="314.3" stroke="var(--up)" class="wick"/>
<rect x="96.32" y="291.6" width="2.45" height="22.7" fill="var(--up)"/>
<line x1="101.5" y1="288.4" x2="101.5" y2="319.6" stroke="var(--down)" class="wick"/>
<rect x="100.27" y="294.0" width="2.45" height="11.0" fill="var(--down)"/>
<line x1="105.5" y1="317.3" x2="105.5" y2="338.7" stroke="var(--down)" class="wick"/>
<rect x="104.23" y="327.4" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="109.4" y1="315.3" x2="109.4" y2="339.0" stroke="var(--up)" class="wick"/>
<rect x="108.18" y="315.7" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="113.4" y1="306.0" x2="113.4" y2="325.7" stroke="var(--up)" class="wick"/>
<rect x="112.13" y="308.8" width="2.45" height="8.3" fill="var(--up)"/>
<line x1="117.3" y1="288.1" x2="117.3" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="116.08" y="296.0" width="2.45" height="7.0" fill="var(--down)"/>
<line x1="121.3" y1="267.2" x2="121.3" y2="296.1" stroke="var(--up)" class="wick"/>
<rect x="120.03" y="269.7" width="2.45" height="24.1" fill="var(--up)"/>
<line x1="125.2" y1="262.5" x2="125.2" y2="284.3" stroke="var(--down)" class="wick"/>
<rect x="123.99" y="265.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="129.2" y1="311.5" x2="129.2" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="127.94" y="311.6" width="2.45" height="34.4" fill="var(--down)"/>
<line x1="133.1" y1="279.6" x2="133.1" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="131.89" y="290.2" width="2.45" height="42.6" fill="var(--up)"/>
<line x1="137.1" y1="288.9" x2="137.1" y2="333.8" stroke="var(--down)" class="wick"/>
<rect x="135.84" y="294.5" width="2.45" height="34.5" fill="var(--down)"/>
<line x1="141.0" y1="299.5" x2="141.0" y2="333.2" stroke="var(--up)" class="wick"/>
<rect x="139.79" y="301.2" width="2.45" height="28.8" fill="var(--up)"/>
<line x1="145.0" y1="297.6" x2="145.0" y2="313.5" stroke="var(--down)" class="wick"/>
<rect x="143.75" y="305.9" width="2.45" height="4.0" fill="var(--down)"/>
<line x1="148.9" y1="306.9" x2="148.9" y2="336.9" stroke="var(--down)" class="wick"/>
<rect x="147.70" y="306.9" width="2.45" height="9.0" fill="var(--down)"/>
<line x1="152.9" y1="251.0" x2="152.9" y2="284.2" stroke="var(--up)" class="wick"/>
<rect x="151.65" y="255.1" width="2.45" height="18.6" fill="var(--up)"/>
<line x1="156.8" y1="222.5" x2="156.8" y2="252.8" stroke="var(--up)" class="wick"/>
<rect x="155.60" y="225.8" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="160.8" y1="223.9" x2="160.8" y2="255.7" stroke="var(--up)" class="wick"/>
<rect x="159.56" y="225.7" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="164.7" y1="231.0" x2="164.7" y2="258.2" stroke="var(--down)" class="wick"/>
<rect x="163.51" y="234.0" width="2.45" height="16.2" fill="var(--down)"/>
<line x1="168.7" y1="248.7" x2="168.7" y2="286.4" stroke="var(--down)" class="wick"/>
<rect x="167.46" y="248.7" width="2.45" height="33.7" fill="var(--down)"/>
<line x1="172.6" y1="289.1" x2="172.6" y2="306.4" stroke="var(--down)" class="wick"/>
<rect x="171.41" y="297.7" width="2.45" height="5.0" fill="var(--down)"/>
<line x1="176.6" y1="302.7" x2="176.6" y2="316.9" stroke="var(--up)" class="wick"/>
<rect x="175.36" y="306.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="180.5" y1="296.5" x2="180.5" y2="314.0" stroke="var(--down)" class="wick"/>
<rect x="179.32" y="296.5" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="184.5" y1="299.4" x2="184.5" y2="317.1" stroke="var(--up)" class="wick"/>
<rect x="183.27" y="302.1" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="188.4" y1="288.7" x2="188.4" y2="315.4" stroke="var(--up)" class="wick"/>
<rect x="187.22" y="299.6" width="2.45" height="12.8" fill="var(--up)"/>
<line x1="192.4" y1="288.7" x2="192.4" y2="319.1" stroke="var(--down)" class="wick"/>
<rect x="191.17" y="290.7" width="2.45" height="25.3" fill="var(--down)"/>
<line x1="196.4" y1="295.6" x2="196.4" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="195.13" y="315.9" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="200.3" y1="289.7" x2="200.3" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="199.08" y="294.8" width="2.45" height="11.6" fill="var(--up)"/>
<line x1="204.3" y1="295.0" x2="204.3" y2="333.8" stroke="var(--down)" class="wick"/>
<rect x="203.03" y="297.1" width="2.45" height="24.9" fill="var(--down)"/>
<line x1="208.2" y1="291.7" x2="208.2" y2="320.0" stroke="var(--up)" class="wick"/>
<rect x="206.98" y="306.5" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="212.2" y1="310.7" x2="212.2" y2="328.6" stroke="var(--up)" class="wick"/>
<rect x="210.93" y="311.0" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="216.1" y1="305.6" x2="216.1" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="214.89" y="313.0" width="2.45" height="72.9" fill="var(--down)"/>
<line x1="220.1" y1="361.0" x2="220.1" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="218.84" y="367.8" width="2.45" height="8.6" fill="var(--up)"/>
<line x1="224.0" y1="376.1" x2="224.0" y2="416.9" stroke="var(--up)" class="wick"/>
<rect x="222.79" y="390.2" width="2.45" height="4.3" fill="var(--up)"/>
<line x1="228.0" y1="373.3" x2="228.0" y2="405.3" stroke="var(--down)" class="wick"/>
<rect x="226.74" y="373.3" width="2.45" height="22.6" fill="var(--down)"/>
<line x1="231.9" y1="385.7" x2="231.9" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="230.70" y="388.7" width="2.45" height="6.7" fill="var(--down)"/>
<line x1="235.9" y1="381.7" x2="235.9" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="234.65" y="388.9" width="2.45" height="12.2" fill="var(--up)"/>
<line x1="239.8" y1="371.7" x2="239.8" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="238.60" y="376.8" width="2.45" height="6.4" fill="var(--up)"/>
<line x1="243.8" y1="357.9" x2="243.8" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="242.55" y="363.6" width="2.45" height="20.5" fill="var(--up)"/>
<line x1="247.7" y1="353.1" x2="247.7" y2="388.8" stroke="var(--down)" class="wick"/>
<rect x="246.50" y="363.7" width="2.45" height="10.1" fill="var(--down)"/>
<line x1="251.7" y1="347.3" x2="251.7" y2="383.8" stroke="var(--up)" class="wick"/>
<rect x="250.46" y="350.4" width="2.45" height="27.5" fill="var(--up)"/>
<line x1="255.6" y1="302.6" x2="255.6" y2="341.8" stroke="var(--up)" class="wick"/>
<rect x="254.41" y="323.4" width="2.45" height="18.4" fill="var(--up)"/>
<line x1="259.6" y1="280.4" x2="259.6" y2="320.3" stroke="var(--down)" class="wick"/>
<rect x="258.36" y="280.4" width="2.45" height="21.2" fill="var(--down)"/>
<line x1="263.5" y1="313.1" x2="263.5" y2="385.3" stroke="var(--up)" class="wick"/>
<rect x="262.31" y="336.5" width="2.45" height="7.9" fill="var(--up)"/>
<line x1="267.5" y1="316.8" x2="267.5" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="266.26" y="336.1" width="2.45" height="14.3" fill="var(--up)"/>
<line x1="271.4" y1="333.4" x2="271.4" y2="363.8" stroke="var(--down)" class="wick"/>
<rect x="270.22" y="341.0" width="2.45" height="13.5" fill="var(--down)"/>
<line x1="275.4" y1="338.5" x2="275.4" y2="354.1" stroke="var(--down)" class="wick"/>
<rect x="274.17" y="345.4" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="279.3" y1="335.1" x2="279.3" y2="372.1" stroke="var(--down)" class="wick"/>
<rect x="278.12" y="335.1" width="2.45" height="21.8" fill="var(--down)"/>
<line x1="283.3" y1="354.6" x2="283.3" y2="390.8" stroke="var(--up)" class="wick"/>
<rect x="282.07" y="364.4" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="287.3" y1="366.7" x2="287.3" y2="395.5" stroke="var(--down)" class="wick"/>
<rect x="286.03" y="368.8" width="2.45" height="14.9" fill="var(--down)"/>
<line x1="291.2" y1="385.0" x2="291.2" y2="415.0" stroke="var(--down)" class="wick"/>
<rect x="289.98" y="393.0" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="295.2" y1="387.3" x2="295.2" y2="412.9" stroke="var(--up)" class="wick"/>
<rect x="293.93" y="392.6" width="2.45" height="1.9" fill="var(--up)"/>
<line x1="299.1" y1="372.6" x2="299.1" y2="398.6" stroke="var(--up)" class="wick"/>
<rect x="297.88" y="379.2" width="2.45" height="8.2" fill="var(--up)"/>
<line x1="303.1" y1="386.6" x2="303.1" y2="423.1" stroke="var(--down)" class="wick"/>
<rect x="301.83" y="387.5" width="2.45" height="27.7" fill="var(--down)"/>
<line x1="307.0" y1="404.5" x2="307.0" y2="428.2" stroke="var(--down)" class="wick"/>
<rect x="305.79" y="406.9" width="2.45" height="18.6" fill="var(--down)"/>
<line x1="311.0" y1="418.8" x2="311.0" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="309.74" y="423.9" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="314.9" y1="411.3" x2="314.9" y2="442.4" stroke="var(--up)" class="wick"/>
<rect x="313.69" y="427.6" width="2.45" height="10.6" fill="var(--up)"/>
<line x1="318.9" y1="424.5" x2="318.9" y2="445.9" stroke="var(--down)" class="wick"/>
<rect x="317.64" y="432.4" width="2.45" height="7.8" fill="var(--down)"/>
<line x1="322.8" y1="443.5" x2="322.8" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="321.60" y="452.5" width="2.45" height="15.6" fill="var(--down)"/>
<line x1="326.8" y1="444.2" x2="326.8" y2="470.8" stroke="var(--up)" class="wick"/>
<rect x="325.55" y="455.8" width="2.45" height="8.8" fill="var(--up)"/>
<line x1="330.7" y1="421.5" x2="330.7" y2="473.6" stroke="var(--down)" class="wick"/>
<rect x="329.50" y="437.2" width="2.45" height="34.6" fill="var(--down)"/>
<line x1="334.7" y1="465.7" x2="334.7" y2="495.8" stroke="var(--down)" class="wick"/>
<rect x="333.45" y="472.5" width="2.45" height="4.6" fill="var(--down)"/>
<line x1="338.6" y1="459.4" x2="338.6" y2="480.4" stroke="var(--up)" class="wick"/>
<rect x="337.40" y="463.7" width="2.45" height="3.8" fill="var(--up)"/>
<line x1="342.6" y1="459.3" x2="342.6" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="341.36" y="466.5" width="2.45" height="10.1" fill="var(--up)"/>
<line x1="346.5" y1="450.9" x2="346.5" y2="465.3" stroke="var(--down)" class="wick"/>
<rect x="345.31" y="454.8" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="350.5" y1="437.9" x2="350.5" y2="457.3" stroke="var(--up)" class="wick"/>
<rect x="349.26" y="438.3" width="2.45" height="9.6" fill="var(--up)"/>
<line x1="354.4" y1="434.1" x2="354.4" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="353.21" y="435.5" width="2.45" height="10.4" fill="var(--down)"/>
<line x1="358.4" y1="413.3" x2="358.4" y2="440.4" stroke="var(--up)" class="wick"/>
<rect x="357.17" y="417.2" width="2.45" height="22.2" fill="var(--up)"/>
<line x1="362.3" y1="347.9" x2="362.3" y2="425.0" stroke="var(--up)" class="wick"/>
<rect x="361.12" y="354.4" width="2.45" height="70.2" fill="var(--up)"/>
<line x1="366.3" y1="342.4" x2="366.3" y2="360.6" stroke="var(--up)" class="wick"/>
<rect x="365.07" y="350.3" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="370.2" y1="337.4" x2="370.2" y2="354.3" stroke="var(--down)" class="wick"/>
<rect x="369.02" y="346.4" width="2.45" height="3.1" fill="var(--down)"/>
<line x1="374.2" y1="338.1" x2="374.2" y2="353.0" stroke="var(--down)" class="wick"/>
<rect x="372.97" y="347.9" width="2.45" height="2.4" fill="var(--down)"/>
<line x1="378.2" y1="347.8" x2="378.2" y2="363.6" stroke="var(--down)" class="wick"/>
<rect x="376.93" y="353.9" width="2.45" height="4.1" fill="var(--down)"/>
<line x1="382.1" y1="336.5" x2="382.1" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="380.88" y="347.7" width="2.45" height="12.5" fill="var(--up)"/>
<line x1="386.1" y1="347.9" x2="386.1" y2="377.8" stroke="var(--down)" class="wick"/>
<rect x="384.83" y="348.1" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="390.0" y1="357.4" x2="390.0" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="388.78" y="359.6" width="2.45" height="39.4" fill="var(--down)"/>
<line x1="394.0" y1="383.2" x2="394.0" y2="418.2" stroke="var(--down)" class="wick"/>
<rect x="392.73" y="396.0" width="2.45" height="19.5" fill="var(--down)"/>
<line x1="397.9" y1="399.7" x2="397.9" y2="422.5" stroke="var(--up)" class="wick"/>
<rect x="396.69" y="411.7" width="2.45" height="3.4" fill="var(--up)"/>
<line x1="401.9" y1="410.5" x2="401.9" y2="441.4" stroke="var(--down)" class="wick"/>
<rect x="400.64" y="413.5" width="2.45" height="20.7" fill="var(--down)"/>
<line x1="405.8" y1="401.8" x2="405.8" y2="429.6" stroke="var(--down)" class="wick"/>
<rect x="404.59" y="415.7" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="409.8" y1="412.6" x2="409.8" y2="431.6" stroke="var(--down)" class="wick"/>
<rect x="408.54" y="427.0" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="413.7" y1="415.8" x2="413.7" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="412.50" y="418.5" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="417.7" y1="419.1" x2="417.7" y2="429.0" stroke="var(--up)" class="wick"/>
<rect x="416.45" y="420.7" width="2.45" height="7.6" fill="var(--up)"/>
<line x1="421.6" y1="416.6" x2="421.6" y2="426.1" stroke="var(--up)" class="wick"/>
<rect x="420.40" y="417.8" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="425.6" y1="412.5" x2="425.6" y2="420.5" stroke="var(--up)" class="wick"/>
<rect x="424.35" y="413.9" width="2.45" height="3.1" fill="var(--up)"/>
<line x1="429.5" y1="404.3" x2="429.5" y2="421.9" stroke="var(--down)" class="wick"/>
<rect x="428.30" y="417.5" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="433.5" y1="413.5" x2="433.5" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="432.26" y="421.0" width="2.45" height="4.2" fill="var(--down)"/>
<line x1="437.4" y1="423.9" x2="437.4" y2="437.5" stroke="var(--down)" class="wick"/>
<rect x="436.21" y="424.7" width="2.45" height="11.1" fill="var(--down)"/>
<line x1="441.4" y1="423.9" x2="441.4" y2="457.0" stroke="var(--down)" class="wick"/>
<rect x="440.16" y="424.9" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="445.3" y1="430.2" x2="445.3" y2="477.8" stroke="var(--down)" class="wick"/>
<rect x="444.11" y="439.6" width="2.45" height="35.4" fill="var(--down)"/>
<line x1="449.3" y1="423.8" x2="449.3" y2="476.1" stroke="var(--up)" class="wick"/>
<rect x="448.07" y="428.6" width="2.45" height="45.4" fill="var(--up)"/>
<line x1="453.2" y1="393.8" x2="453.2" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="452.02" y="408.2" width="2.45" height="21.2" fill="var(--up)"/>
<line x1="457.2" y1="412.0" x2="457.2" y2="434.4" stroke="var(--up)" class="wick"/>
<rect x="455.97" y="414.2" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="461.1" y1="380.4" x2="461.1" y2="425.9" stroke="var(--up)" class="wick"/>
<rect x="459.92" y="384.8" width="2.45" height="25.6" fill="var(--up)"/>
<line x1="465.1" y1="380.7" x2="465.1" y2="406.6" stroke="var(--down)" class="wick"/>
<rect x="463.87" y="389.8" width="2.45" height="1.3" fill="var(--down)"/>
<line x1="469.1" y1="383.6" x2="469.1" y2="417.0" stroke="var(--up)" class="wick"/>
<rect x="467.83" y="399.5" width="2.45" height="1.5" fill="var(--up)"/>
<line x1="473.0" y1="408.3" x2="473.0" y2="444.9" stroke="var(--down)" class="wick"/>
<rect x="471.78" y="411.8" width="2.45" height="21.9" fill="var(--down)"/>
<line x1="477.0" y1="380.2" x2="477.0" y2="423.9" stroke="var(--up)" class="wick"/>
<rect x="475.73" y="408.0" width="2.45" height="10.9" fill="var(--up)"/>
<line x1="480.9" y1="401.6" x2="480.9" y2="429.1" stroke="var(--down)" class="wick"/>
<rect x="479.68" y="403.8" width="2.45" height="15.1" fill="var(--down)"/>
<line x1="484.9" y1="439.6" x2="484.9" y2="459.2" stroke="var(--down)" class="wick"/>
<rect x="483.64" y="442.7" width="2.45" height="12.3" fill="var(--down)"/>
<line x1="488.8" y1="423.4" x2="488.8" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="487.59" y="431.4" width="2.45" height="21.8" fill="var(--up)"/>
<line x1="492.8" y1="417.6" x2="492.8" y2="441.9" stroke="var(--up)" class="wick"/>
<rect x="491.54" y="420.1" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="496.7" y1="397.9" x2="496.7" y2="437.7" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="415.9" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="500.7" y1="397.6" x2="500.7" y2="430.6" stroke="var(--up)" class="wick"/>
<rect x="499.44" y="403.1" width="2.45" height="14.4" fill="var(--up)"/>
<line x1="504.6" y1="399.7" x2="504.6" y2="419.7" stroke="var(--down)" class="wick"/>
<rect x="503.40" y="404.2" width="2.45" height="11.5" fill="var(--down)"/>
<line x1="508.6" y1="392.2" x2="508.6" y2="422.3" stroke="var(--down)" class="wick"/>
<rect x="507.35" y="404.5" width="2.45" height="3.9" fill="var(--down)"/>
<line x1="512.5" y1="420.5" x2="512.5" y2="501.8" stroke="var(--down)" class="wick"/>
<rect x="511.30" y="421.8" width="2.45" height="48.2" fill="var(--down)"/>
<line x1="516.5" y1="483.1" x2="516.5" y2="501.2" stroke="var(--down)" class="wick"/>
<rect x="515.25" y="484.5" width="2.45" height="7.3" fill="var(--down)"/>
<line x1="520.4" y1="491.8" x2="520.4" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="519.21" y="496.1" width="2.45" height="20.4" fill="var(--down)"/>
<line x1="524.4" y1="527.6" x2="524.4" y2="607.9" stroke="var(--down)" class="wick"/>
<rect x="523.16" y="535.0" width="2.45" height="53.0" fill="var(--down)"/>
<line x1="528.3" y1="564.5" x2="528.3" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="527.11" y="577.9" width="2.45" height="5.4" fill="var(--up)"/>
<line x1="532.3" y1="560.7" x2="532.3" y2="596.2" stroke="var(--down)" class="wick"/>
<rect x="531.06" y="577.0" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="536.2" y1="529.8" x2="536.2" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="535.01" y="536.1" width="2.45" height="25.4" fill="var(--up)"/>
<line x1="540.2" y1="507.6" x2="540.2" y2="549.8" stroke="var(--up)" class="wick"/>
<rect x="538.97" y="510.3" width="2.45" height="25.9" fill="var(--up)"/>
<line x1="544.1" y1="475.5" x2="544.1" y2="503.4" stroke="var(--up)" class="wick"/>
<rect x="542.92" y="482.6" width="2.45" height="16.7" fill="var(--up)"/>
<line x1="548.1" y1="471.4" x2="548.1" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="546.87" y="475.1" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="552.0" y1="470.3" x2="552.0" y2="522.3" stroke="var(--down)" class="wick"/>
<rect x="550.82" y="483.6" width="2.45" height="35.9" fill="var(--down)"/>
<line x1="556.0" y1="476.7" x2="556.0" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="554.77" y="481.0" width="2.45" height="41.5" fill="var(--up)"/>
<line x1="560.0" y1="492.3" x2="560.0" y2="538.0" stroke="var(--down)" class="wick"/>
<rect x="558.73" y="497.2" width="2.45" height="39.1" fill="var(--down)"/>
<line x1="563.9" y1="438.8" x2="563.9" y2="482.0" stroke="var(--up)" class="wick"/>
<rect x="562.68" y="461.9" width="2.45" height="7.1" fill="var(--up)"/>
<line x1="567.9" y1="450.4" x2="567.9" y2="506.3" stroke="var(--down)" class="wick"/>
<rect x="566.63" y="450.4" width="2.45" height="40.6" fill="var(--down)"/>
<line x1="571.8" y1="467.3" x2="571.8" y2="505.4" stroke="var(--up)" class="wick"/>
<rect x="570.58" y="492.0" width="2.45" height="6.2" fill="var(--up)"/>
<line x1="575.8" y1="501.3" x2="575.8" y2="551.3" stroke="var(--down)" class="wick"/>
<rect x="574.54" y="508.8" width="2.45" height="40.2" fill="var(--down)"/>
<line x1="579.7" y1="500.4" x2="579.7" y2="557.6" stroke="var(--up)" class="wick"/>
<rect x="578.49" y="511.6" width="2.45" height="44.3" fill="var(--up)"/>
<line x1="583.7" y1="469.6" x2="583.7" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="582.44" y="472.8" width="2.45" height="25.4" fill="var(--up)"/>
<line x1="587.6" y1="458.6" x2="587.6" y2="503.7" stroke="var(--down)" class="wick"/>
<rect x="586.39" y="461.9" width="2.45" height="25.5" fill="var(--down)"/>
<line x1="591.6" y1="472.6" x2="591.6" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="590.34" y="474.3" width="2.45" height="43.7" fill="var(--up)"/>
<line x1="595.5" y1="462.7" x2="595.5" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="594.30" y="467.6" width="2.45" height="19.3" fill="var(--up)"/>
<line x1="599.5" y1="463.7" x2="599.5" y2="494.7" stroke="var(--up)" class="wick"/>
<rect x="598.25" y="477.0" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="603.4" y1="449.5" x2="603.4" y2="492.6" stroke="var(--up)" class="wick"/>
<rect x="602.20" y="460.4" width="2.45" height="18.1" fill="var(--up)"/>
<line x1="607.4" y1="440.4" x2="607.4" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="606.15" y="468.8" width="2.45" height="10.9" fill="var(--down)"/>
<line x1="611.3" y1="472.2" x2="611.3" y2="499.0" stroke="var(--up)" class="wick"/>
<rect x="610.11" y="489.8" width="2.45" height="6.9" fill="var(--up)"/>
<line x1="615.3" y1="478.2" x2="615.3" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="614.06" y="485.9" width="2.45" height="14.8" fill="var(--up)"/>
<line x1="619.2" y1="482.4" x2="619.2" y2="512.1" stroke="var(--down)" class="wick"/>
<rect x="618.01" y="482.4" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="623.2" y1="493.0" x2="623.2" y2="524.1" stroke="var(--down)" class="wick"/>
<rect x="621.96" y="497.2" width="2.45" height="2.2" fill="var(--down)"/>
<line x1="627.1" y1="491.2" x2="627.1" y2="516.5" stroke="var(--down)" class="wick"/>
<rect x="625.91" y="510.5" width="2.45" height="2.1" fill="var(--down)"/>
<line x1="631.1" y1="506.7" x2="631.1" y2="536.7" stroke="var(--down)" class="wick"/>
<rect x="629.87" y="511.0" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="635.0" y1="495.0" x2="635.0" y2="520.6" stroke="var(--up)" class="wick"/>
<rect x="633.82" y="504.3" width="2.45" height="11.7" fill="var(--up)"/>
<line x1="639.0" y1="475.9" x2="639.0" y2="505.1" stroke="var(--down)" class="wick"/>
<rect x="637.77" y="500.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="642.9" y1="495.4" x2="642.9" y2="515.5" stroke="var(--down)" class="wick"/>
<rect x="641.72" y="507.1" width="2.45" height="7.9" fill="var(--down)"/>
<line x1="646.9" y1="504.7" x2="646.9" y2="533.2" stroke="var(--down)" class="wick"/>
<rect x="645.68" y="517.5" width="2.45" height="5.3" fill="var(--down)"/>
<line x1="650.9" y1="522.7" x2="650.9" y2="543.2" stroke="var(--down)" class="wick"/>
<rect x="649.63" y="526.1" width="2.45" height="8.7" fill="var(--down)"/>
<line x1="654.8" y1="481.6" x2="654.8" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="653.58" y="505.0" width="2.45" height="11.5" fill="var(--up)"/>
<line x1="658.8" y1="512.0" x2="658.8" y2="558.6" stroke="var(--down)" class="wick"/>
<rect x="657.53" y="515.4" width="2.45" height="17.9" fill="var(--down)"/>
<line x1="662.7" y1="512.4" x2="662.7" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="661.48" y="518.3" width="2.45" height="25.2" fill="var(--down)"/>
<line x1="666.7" y1="533.9" x2="666.7" y2="555.2" stroke="var(--up)" class="wick"/>
<rect x="665.44" y="546.1" width="2.45" height="9.1" fill="var(--up)"/>
<line x1="670.6" y1="546.8" x2="670.6" y2="579.2" stroke="var(--down)" class="wick"/>
<rect x="669.39" y="554.3" width="2.45" height="22.4" fill="var(--down)"/>
<line x1="674.6" y1="560.8" x2="674.6" y2="587.0" stroke="var(--down)" class="wick"/>
<rect x="673.34" y="575.3" width="2.45" height="4.5" fill="var(--down)"/>
<line x1="678.5" y1="553.1" x2="678.5" y2="577.3" stroke="var(--up)" class="wick"/>
<rect x="677.29" y="555.6" width="2.45" height="15.9" fill="var(--up)"/>
<line x1="682.5" y1="542.7" x2="682.5" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="681.24" y="547.6" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="686.4" y1="547.4" x2="686.4" y2="578.2" stroke="var(--up)" class="wick"/>
<rect x="685.20" y="552.7" width="2.45" height="17.4" fill="var(--up)"/>
<line x1="690.4" y1="549.1" x2="690.4" y2="563.9" stroke="var(--up)" class="wick"/>
<rect x="689.15" y="550.4" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="694.3" y1="548.3" x2="694.3" y2="569.3" stroke="var(--up)" class="wick"/>
<rect x="693.10" y="550.1" width="2.45" height="5.0" fill="var(--up)"/>
<line x1="698.3" y1="509.1" x2="698.3" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="697.05" y="513.8" width="2.45" height="1.7" fill="var(--down)"/>
<line x1="702.2" y1="520.0" x2="702.2" y2="557.1" stroke="var(--down)" class="wick"/>
<rect x="701.01" y="521.9" width="2.45" height="22.8" fill="var(--down)"/>
<line x1="706.2" y1="543.4" x2="706.2" y2="605.7" stroke="var(--down)" class="wick"/>
<rect x="704.96" y="545.8" width="2.45" height="52.1" fill="var(--down)"/>
<line x1="710.1" y1="519.5" x2="710.1" y2="599.3" stroke="var(--up)" class="wick"/>
<rect x="708.91" y="519.9" width="2.45" height="76.5" fill="var(--up)"/>
<line x1="714.1" y1="488.9" x2="714.1" y2="512.8" stroke="var(--down)" class="wick"/>
<rect x="712.86" y="502.3" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="718.0" y1="453.4" x2="718.0" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="716.81" y="465.0" width="2.45" height="31.4" fill="var(--up)"/>
<line x1="722.0" y1="434.7" x2="722.0" y2="467.7" stroke="var(--down)" class="wick"/>
<rect x="720.77" y="446.5" width="2.45" height="8.6" fill="var(--down)"/>
<line x1="725.9" y1="417.0" x2="725.9" y2="450.2" stroke="var(--down)" class="wick"/>
<rect x="724.72" y="422.8" width="2.45" height="18.3" fill="var(--down)"/>
<line x1="729.9" y1="406.7" x2="729.9" y2="446.0" stroke="var(--up)" class="wick"/>
<rect x="728.67" y="415.3" width="2.45" height="20.4" fill="var(--up)"/>
<line x1="733.8" y1="371.3" x2="733.8" y2="413.9" stroke="var(--up)" class="wick"/>
<rect x="732.62" y="389.9" width="2.45" height="21.0" fill="var(--up)"/>
<line x1="737.8" y1="361.7" x2="737.8" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="736.58" y="365.7" width="2.45" height="4.3" fill="var(--down)"/>
<line x1="741.8" y1="386.0" x2="741.8" y2="441.2" stroke="var(--down)" class="wick"/>
<rect x="740.53" y="389.8" width="2.45" height="39.8" fill="var(--down)"/>
<line x1="745.7" y1="358.9" x2="745.7" y2="412.3" stroke="var(--up)" class="wick"/>
<rect x="744.48" y="365.6" width="2.45" height="44.3" fill="var(--up)"/>
<line x1="749.7" y1="347.3" x2="749.7" y2="375.5" stroke="var(--up)" class="wick"/>
<rect x="748.43" y="353.0" width="2.45" height="19.8" fill="var(--up)"/>
<line x1="753.6" y1="346.0" x2="753.6" y2="420.2" stroke="var(--down)" class="wick"/>
<rect x="752.38" y="376.6" width="2.45" height="15.2" fill="var(--down)"/>
<line x1="757.6" y1="370.8" x2="757.6" y2="425.6" stroke="var(--up)" class="wick"/>
<rect x="756.34" y="375.7" width="2.45" height="21.6" fill="var(--up)"/>
<line x1="761.5" y1="375.3" x2="761.5" y2="410.9" stroke="var(--up)" class="wick"/>
<rect x="760.29" y="377.0" width="2.45" height="2.9" fill="var(--up)"/>
<line x1="765.5" y1="332.8" x2="765.5" y2="361.7" stroke="var(--up)" class="wick"/>
<rect x="764.24" y="337.8" width="2.45" height="15.3" fill="var(--up)"/>
<line x1="769.4" y1="303.0" x2="769.4" y2="338.9" stroke="var(--up)" class="wick"/>
<rect x="768.19" y="308.1" width="2.45" height="24.6" fill="var(--up)"/>
<line x1="773.4" y1="289.6" x2="773.4" y2="319.8" stroke="var(--up)" class="wick"/>
<rect x="772.15" y="293.9" width="2.45" height="8.0" fill="var(--up)"/>
<line x1="777.3" y1="287.5" x2="777.3" y2="315.1" stroke="var(--up)" class="wick"/>
<rect x="776.10" y="289.5" width="2.45" height="4.8" fill="var(--up)"/>
<line x1="781.3" y1="262.5" x2="781.3" y2="289.6" stroke="var(--down)" class="wick"/>
<rect x="780.05" y="278.8" width="2.45" height="3.8" fill="var(--down)"/>
<line x1="785.2" y1="254.6" x2="785.2" y2="295.5" stroke="var(--up)" class="wick"/>
<rect x="784.00" y="262.6" width="2.45" height="22.9" fill="var(--up)"/>
<line x1="789.2" y1="254.6" x2="789.2" y2="278.7" stroke="var(--up)" class="wick"/>
<rect x="787.95" y="257.4" width="2.45" height="17.7" fill="var(--up)"/>
<line x1="793.1" y1="265.0" x2="793.1" y2="287.2" stroke="var(--down)" class="wick"/>
<rect x="791.91" y="268.1" width="2.45" height="10.6" fill="var(--down)"/>
<line x1="797.1" y1="268.4" x2="797.1" y2="304.6" stroke="var(--down)" class="wick"/>
<rect x="795.86" y="275.2" width="2.45" height="15.5" fill="var(--down)"/>
<line x1="801.0" y1="288.5" x2="801.0" y2="311.8" stroke="var(--up)" class="wick"/>
<rect x="799.81" y="296.6" width="2.45" height="9.7" fill="var(--up)"/>
<line x1="805.0" y1="299.5" x2="805.0" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="803.76" y="300.2" width="2.45" height="15.8" fill="var(--down)"/>
<line x1="808.9" y1="306.2" x2="808.9" y2="335.9" stroke="var(--down)" class="wick"/>
<rect x="807.72" y="317.1" width="2.45" height="3.2" fill="var(--down)"/>
<line x1="812.9" y1="312.9" x2="812.9" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="811.67" y="331.8" width="2.45" height="15.7" fill="var(--down)"/>
<line x1="816.8" y1="301.7" x2="816.8" y2="370.2" stroke="var(--up)" class="wick"/>
<rect x="815.62" y="303.4" width="2.45" height="53.5" fill="var(--up)"/>
<line x1="820.8" y1="264.3" x2="820.8" y2="314.9" stroke="var(--up)" class="wick"/>
<rect x="819.57" y="277.2" width="2.45" height="29.6" fill="var(--up)"/>
<line x1="824.7" y1="197.5" x2="824.7" y2="266.6" stroke="var(--up)" class="wick"/>
<rect x="823.52" y="225.0" width="2.45" height="40.5" fill="var(--up)"/>
<line x1="828.7" y1="191.6" x2="828.7" y2="238.7" stroke="var(--up)" class="wick"/>
<rect x="827.48" y="196.8" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="832.7" y1="189.7" x2="832.7" y2="236.2" stroke="var(--down)" class="wick"/>
<rect x="831.43" y="206.4" width="2.45" height="16.9" fill="var(--down)"/>
<line x1="836.6" y1="206.1" x2="836.6" y2="247.8" stroke="var(--down)" class="wick"/>
<rect x="835.38" y="220.5" width="2.45" height="3.6" fill="var(--down)"/>
<line x1="840.6" y1="209.6" x2="840.6" y2="229.5" stroke="var(--down)" class="wick"/>
<rect x="839.33" y="220.1" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="844.5" y1="82.2" x2="844.5" y2="189.2" stroke="var(--up)" class="wick"/>
<rect x="843.28" y="84.8" width="2.45" height="73.1" fill="var(--up)"/>
<line x1="848.5" y1="76.1" x2="848.5" y2="130.1" stroke="var(--up)" class="wick"/>
<rect x="847.24" y="77.1" width="2.45" height="36.0" fill="var(--up)"/>
<line x1="852.4" y1="95.6" x2="852.4" y2="130.2" stroke="var(--down)" class="wick"/>
<rect x="851.19" y="99.2" width="2.45" height="6.9" fill="var(--down)"/>
<line x1="856.4" y1="79.0" x2="856.4" y2="127.1" stroke="var(--up)" class="wick"/>
<rect x="855.14" y="93.4" width="2.45" height="13.6" fill="var(--up)"/>
<line x1="860.3" y1="109.5" x2="860.3" y2="225.1" stroke="var(--down)" class="wick"/>
<rect x="859.09" y="126.8" width="2.45" height="89.2" fill="var(--down)"/>
<line x1="864.3" y1="145.1" x2="864.3" y2="196.4" stroke="var(--up)" class="wick"/>
<rect x="863.05" y="153.6" width="2.45" height="38.8" fill="var(--up)"/>
<line x1="868.2" y1="110.7" x2="868.2" y2="212.8" stroke="var(--down)" class="wick"/>
<rect x="867.00" y="145.3" width="2.45" height="19.9" fill="var(--down)"/>
<line x1="872.2" y1="136.4" x2="872.2" y2="195.9" stroke="var(--up)" class="wick"/>
<rect x="870.95" y="185.1" width="2.45" height="5.8" fill="var(--up)"/>
<line x1="876.1" y1="169.9" x2="876.1" y2="212.5" stroke="var(--up)" class="wick"/>
<rect x="874.90" y="189.9" width="2.45" height="6.0" fill="var(--up)"/>
<line x1="880.1" y1="169.0" x2="880.1" y2="216.8" stroke="var(--up)" class="wick"/>
<rect x="878.85" y="185.7" width="2.45" height="12.9" fill="var(--up)"/>
<line x1="884.0" y1="141.3" x2="884.0" y2="170.6" stroke="var(--up)" class="wick"/>
<rect x="882.81" y="152.7" width="2.45" height="12.1" fill="var(--up)"/>
<line x1="888.0" y1="139.7" x2="888.0" y2="178.0" stroke="var(--up)" class="wick"/>
<rect x="886.76" y="175.7" width="2.45" height="2.3" fill="var(--up)"/>
<line x1="891.9" y1="122.1" x2="891.9" y2="180.5" stroke="var(--up)" class="wick"/>
<rect x="890.71" y="169.7" width="2.45" height="4.0" fill="var(--up)"/>
<line x1="895.9" y1="129.7" x2="895.9" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="894.66" y="164.5" width="2.45" height="12.8" fill="var(--down)"/>
<line x1="899.8" y1="161.4" x2="899.8" y2="209.0" stroke="var(--down)" class="wick"/>
<rect x="898.62" y="161.4" width="2.45" height="10.2" fill="var(--down)"/>
<line x1="903.8" y1="180.2" x2="903.8" y2="212.0" stroke="var(--down)" class="wick"/>
<rect x="902.57" y="191.9" width="2.45" height="14.2" fill="var(--down)"/>
<line x1="907.7" y1="204.1" x2="907.7" y2="231.9" stroke="var(--down)" class="wick"/>
<rect x="906.52" y="217.7" width="2.45" height="11.4" fill="var(--down)"/>
<line x1="911.7" y1="208.0" x2="911.7" y2="259.0" stroke="var(--down)" class="wick"/>
<rect x="910.47" y="208.0" width="2.45" height="35.4" fill="var(--down)"/>
<line x1="915.6" y1="196.3" x2="915.6" y2="276.2" stroke="var(--up)" class="wick"/>
<rect x="914.42" y="212.2" width="2.45" height="51.9" fill="var(--up)"/>
<line x1="919.6" y1="178.0" x2="919.6" y2="232.6" stroke="var(--down)" class="wick"/>
<rect x="918.38" y="197.7" width="2.45" height="30.3" fill="var(--down)"/>
<line x1="923.6" y1="197.4" x2="923.6" y2="242.8" stroke="var(--up)" class="wick"/>
<rect x="922.33" y="219.0" width="2.45" height="13.2" fill="var(--up)"/>
<line x1="927.5" y1="179.5" x2="927.5" y2="214.6" stroke="var(--down)" class="wick"/>
<rect x="926.28" y="189.4" width="2.45" height="21.2" fill="var(--down)"/>
<line x1="931.5" y1="196.7" x2="931.5" y2="235.6" stroke="var(--down)" class="wick"/>
<rect x="930.23" y="219.1" width="2.45" height="7.4" fill="var(--down)"/>
<line x1="935.4" y1="210.2" x2="935.4" y2="245.8" stroke="var(--up)" class="wick"/>
<rect x="934.19" y="217.4" width="2.45" height="21.3" fill="var(--up)"/>
<line x1="939.4" y1="202.9" x2="939.4" y2="252.5" stroke="var(--down)" class="wick"/>
<rect x="938.14" y="217.2" width="2.45" height="16.5" fill="var(--down)"/>
<line x1="943.3" y1="222.0" x2="943.3" y2="250.8" stroke="var(--up)" class="wick"/>
<rect x="942.09" y="223.3" width="2.45" height="23.2" fill="var(--up)"/>
<line x1="947.3" y1="180.9" x2="947.3" y2="243.1" stroke="var(--up)" class="wick"/>
<rect x="946.04" y="182.3" width="2.45" height="54.6" fill="var(--up)"/>
<line x1="951.2" y1="170.0" x2="951.2" y2="202.1" stroke="var(--down)" class="wick"/>
<rect x="949.99" y="175.4" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="955.2" y1="164.8" x2="955.2" y2="219.7" stroke="var(--down)" class="wick"/>
<rect x="953.95" y="166.1" width="2.45" height="43.9" fill="var(--down)"/>
<line x1="959.1" y1="192.5" x2="959.1" y2="234.3" stroke="var(--up)" class="wick"/>
<rect x="957.90" y="213.9" width="2.45" height="20.2" fill="var(--up)"/>
<line x1="963.1" y1="184.5" x2="963.1" y2="240.6" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="191.2" width="2.45" height="41.0" fill="var(--down)"/>
<line x1="967.0" y1="240.4" x2="967.0" y2="276.3" stroke="var(--down)" class="wick"/>
<rect x="965.80" y="251.1" width="2.45" height="4.7" fill="var(--down)"/>
<line x1="971.0" y1="333.1" x2="971.0" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="969.75" y="359.8" width="2.45" height="15.4" fill="var(--down)"/>
<line x1="974.9" y1="344.1" x2="974.9" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="973.71" y="365.1" width="2.45" height="10.7" fill="var(--down)"/>
<line x1="978.9" y1="316.4" x2="978.9" y2="381.2" stroke="var(--up)" class="wick"/>
<rect x="977.66" y="325.0" width="2.45" height="56.2" fill="var(--up)"/>
<line x1="982.8" y1="319.1" x2="982.8" y2="359.7" stroke="var(--down)" class="wick"/>
<rect x="981.61" y="344.2" width="2.45" height="7.1" fill="var(--down)"/>
<line x1="986.8" y1="340.0" x2="986.8" y2="379.4" stroke="var(--down)" class="wick"/>
<rect x="985.56" y="357.6" width="2.45" height="16.4" fill="var(--down)"/>
<line x1="990.7" y1="356.4" x2="990.7" y2="389.5" stroke="var(--down)" class="wick"/>
<rect x="989.52" y="357.4" width="2.45" height="31.1" fill="var(--down)"/>
<line x1="994.7" y1="333.2" x2="994.7" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="993.47" y="345.8" width="2.45" height="7.3" fill="var(--up)"/>
<line x1="998.6" y1="287.1" x2="998.6" y2="357.7" stroke="var(--up)" class="wick"/>
<rect x="997.42" y="324.7" width="2.45" height="33.0" fill="var(--up)"/>
<line x1="1002.6" y1="303.0" x2="1002.6" y2="366.7" stroke="var(--down)" class="wick"/>
<rect x="1001.37" y="309.9" width="2.45" height="56.1" fill="var(--down)"/>
<line x1="1006.5" y1="332.4" x2="1006.5" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="1005.32" y="352.7" width="2.45" height="13.1" fill="var(--down)"/>
<line x1="1010.5" y1="324.5" x2="1010.5" y2="360.9" stroke="var(--up)" class="wick"/>
<rect x="1009.28" y="340.9" width="2.45" height="16.4" fill="var(--up)"/>
<line x1="1014.5" y1="325.6" x2="1014.5" y2="369.7" stroke="var(--down)" class="wick"/>
<rect x="1013.23" y="327.9" width="2.45" height="26.4" fill="var(--down)"/>
<line x1="1018.4" y1="309.5" x2="1018.4" y2="343.5" stroke="var(--down)" class="wick"/>
<rect x="1017.18" y="338.2" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1022.4" y1="313.5" x2="1022.4" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="1021.13" y="313.5" width="2.45" height="37.6" fill="var(--down)"/>
<line x1="1026.3" y1="335.0" x2="1026.3" y2="365.2" stroke="var(--up)" class="wick"/>
<rect x="1025.09" y="346.5" width="2.45" height="9.9" fill="var(--up)"/>
<line x1="1030.3" y1="312.9" x2="1030.3" y2="356.3" stroke="var(--down)" class="wick"/>
<rect x="1029.04" y="330.6" width="2.45" height="13.0" fill="var(--down)"/>
<line x1="1034.2" y1="334.0" x2="1034.2" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="1032.99" y="350.3" width="2.45" height="18.7" fill="var(--down)"/>
<line x1="1038.2" y1="371.2" x2="1038.2" y2="399.1" stroke="var(--down)" class="wick"/>
<rect x="1036.94" y="373.6" width="2.45" height="10.5" fill="var(--down)"/>
<line x1="1042.1" y1="363.7" x2="1042.1" y2="402.8" stroke="var(--down)" class="wick"/>
<rect x="1040.89" y="375.5" width="2.45" height="23.8" fill="var(--down)"/>
<line x1="1046.1" y1="381.4" x2="1046.1" y2="406.3" stroke="var(--down)" class="wick"/>
<rect x="1044.85" y="396.3" width="2.45" height="1.0" fill="var(--down)"/>
<line x1="1050.0" y1="386.4" x2="1050.0" y2="412.0" stroke="var(--up)" class="wick"/>
<rect x="1048.80" y="393.4" width="2.45" height="1.0" fill="var(--up)"/>
<line x1="60" y1="392.2" x2="1052" y2="392.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="395.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$325 R1</text>
<text x="1058" y="407.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="274.4" x2="1052" y2="274.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="277.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$359 R2</text>
<text x="1058" y="289.9" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="422.7" x2="1052" y2="422.7" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="416.7" font-size="11.5" fill="var(--support)" font-weight="600">$316 S1</text>
<text x="1058" y="428.7" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="478.6" x2="1052" y2="478.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="472.6" font-size="11.5" fill="var(--support)" font-weight="600">$300 S2</text>
<text x="1058" y="484.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="600.2" x2="1052" y2="600.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="594.2" font-size="11.5" fill="var(--support)" font-weight="600">$265 S3</text>
<text x="1058" y="606.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="393.4" r="3" fill="var(--ink)"/>
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
| R2 | $359 | 5 | 2025-08~09(연초 구간), 2025-10-27(3분기 실적 발표 직후), 2026-05(실적 랠리 구간), 2026-07-28(2분기 실적 발표 직후) — 1년 내내 반복적으로 등장한 상단 저항대 |
| R1 | $325 | 3 | 2025-12-29~2026-01-28, 연말~연초 박스권 상단 |
| **현재가** | **$324.82** (2026-08-14 종가) | — | R1 바로 아래, R1과 S1 사이 |
| S1 | $316 | 3 | 2025-10-14, 2025-12-17, 2026-07-17(§3-B Kimi K3 급락 당일 저가) — 최근 급락 국면에서도 지지력이 확인된 구간 |
| S2 | $300 | 3 | 2025-11-21~2026-01-21, 연말 조정 구간의 저점대 |
| S3 | $265 | 3 | 2026-02-03~2026-04-10, 연중 최저 구간(52주 최저 $262.75와 인접) |
| 참고선 | $417 | — | 52주 최고(2026-06-02 종가 $416.39·장중 고가 $416.69) — §3-A ChipStack AI 발표 직후 형성된 단기 급등 고점으로, 이후 7월 급락(§3-B)으로 레짐이 바뀌어 근시일 저항으로 보기 어려움 |

---

## 3. 관측된 특이 구간

### 3-A. 2026-06-01 — ChipStack AI 발표·Samsung Foundry 협력 급등

- Computex 2026에서 칩 검증 시간을 5주에서 24시간 이내로 단축한다는 ChipStack AI Super Agent를 발표하고, 같은 시점 Samsung Foundry와 2nm·3D-IC 설계 협력 강화를 함께 발표 — Nvidia 엔지니어링팀이 이 기술을 실제 프로덕션에 적용 중이라는 내용도 포함됐다. 에이전틱 AI 전략([CEO / 경영진](./03_ceo.md) §2, [투자 판단](./07_investment.md) §1·§2)이 처음으로 명확한 가격 반영을 받은 사례로 볼 수 있다.
- 종가 기준 전일 대비 **+10.46%**($374.93 → $414.16), 거래량은 평소(일 평균 약 217만 주) 대비 약 **2.1배**인 452만 주. 다음 거래일(06-02)에도 추가 상승해 52주 최고 $416.39(장중 $416.69)를 경신했다.
- 이후 6월 상순 $410~416 레인지에서 한 단계 레짐이 위로 이동했으나, 아래 §3-B 급락으로 그 레짐은 오래 유지되지 못했다 — §2 참고선($417)을 근시일 저항으로 취급하지 않는 이유다.

### 3-B. 2026-07-17 — Moonshot Kimi K3 발표發 AI 밸류에이션 우려 급락

- 중국 스타트업 Moonshot AI가 상하이 WAIC에서 2.8조 파라미터급 오픈웨이트 모델 Kimi K3를 공개하며, 저비용 오픈소스 모델이 AI 인프라 투자 수익률을 훼손할 수 있다는 우려가 AI 관련주 전반으로 확산됐다 — Cadence의 밸류에이션 부담 리스크([투자 판단](./07_investment.md) §3)가 실제 가격 조정으로 나타난 사례.
- 종가 기준 전일 대비 **−9.47%**($364.65 → $330.11), 거래량은 평소 대비 약 **2.4배**인 519만 주로 최근 1년 중 최대 거래량을 기록했다. 이후 6거래일 연속 하락하며 누적 약 −14% 조정을 겪었다(Trefis 보도 기준).
- 낙폭은 S1($316) 부근에서 진정됐다(2026-07-17 저가 $320.07) — 이번 급락 국면에서 S1이 지지력을 보였다는 관측이나, 향후에도 같은 수준에서 지지가 작동할 것을 보장하는 것은 아니다(§4 한계).

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 251개 거래일, 2025-08-15~2026-08-14. 수집 시점: 2026-08-15. 원주가(과거 분할은 소급 반영, 배당은 미반영) — Cadence는 표 기간 내 주식분할 이력이 없어 소급조정 이슈 자체가 없음.
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py CDNS --name "Cadence Design Systems" --event 2026-06-01:"ChipStack AI 발표·Samsung Foundry 협력 급등" --event 2026-07-17:"Moonshot Kimi K3 발표發 AI 밸류에이션 우려 급락" --ref-line 416.69:"52주 최고" --close-on 2026-08-13`. 파라미터(창 5거래일·허용오차 ±2.5%)는 기본값 그대로 사용 — 회사 간 비교가 가능하도록 스크립트에 고정된 값.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 251개 표본에서 스크립트 기본값을 그대로 쓴 것이며, Cadence에 맞춰 최적화된 값이 아니다.
    - §3의 두 이벤트(2026-06-01 급등, 2026-07-17 급락)는 모두 EDA 펀더멘털이 아니라 **AI 서사(에이전틱 AI 기대·오픈소스 모델발 밸류에이션 우려)에 대한 반응**이라, 이 기간의 스윙 레벨은 실적·가이던스보다 AI 관련 뉴스 흐름에 더 민감하게 움직였을 가능성이 있다 — R2($359)·참고선($417)의 신뢰도를 해석할 때 이 점을 감안할 것.
    - 표 기간 내 주식분할·유상증자 등 가격 연속성을 깨는 이벤트는 없었다(확인 완료).

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

- [Yahoo Finance — CDNS 일봉 OHLCV](https://finance.yahoo.com/quote/CDNS/history/)
- [stockanalysis.com — CDNS 현재가/종가 대조용](https://stockanalysis.com/stocks/cdns/)
- [GuruFocus — Cadence Design Systems (CDNS) Shares Drop Amid AI Model Concerns](https://www.gurufocus.com/news/8965307/cadence-design-systems-cdns-shares-drop-amid-ai-model-concerns?mobile=true)
- [TradingKey — Cadence Design Systems Inc Stock (CDNS) Moved Down by 9.82% on Jul 17](https://www.tradingkey.com/news/market-movers/262038361-market-movers-cdns-20260717)
- [Trefis — Cadence Design Systems Stock Slides 14% Over 6 Straight Down Days](https://www.trefis.com/stock/cdns/articles/607964/cadence-design-systems-stock-slides-14-over-6-straight-down-days/2026-07-20)
- [GuruFocus — Cadence Design Systems (CDNS) Shares Surge 10.5%](https://www.gurufocus.com/news/8894566/cadence-design-systems-inc-cdns-shares-surge-105-what-gf-score-of-99-tells-investors)
- [Parameter — Cadence Design Systems (CDNS) Stock Soars Nearly 9% on AI Breakthrough That Slashes Verification Time](https://parameter.io/cadence-design-systems-cdns-stock-soars-nearly-9-on-ai-breakthrough-that-slashes-verification-time/)
- [Trefis — The AI Double-Tap That Lit Up Cadence](https://www.trefis.com/stock/cdns/articles/601032/the-ai-double-tap-that-lit-up-cadence/2026-06-02)

---

*작성일: 2026-08-15 (최종 수정일: 2026-08-22)*
