# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 1년 단기 구조는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(주 마지막 거래일 기준). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
    - **대조 결과**: 마지막 주봉 종가 **$141.07(2026-08-28)**은 핵심 지표 A.2와 밸류에이션 / 적정주가가 기준으로 쓰는 종가와 **일치한다**. 같은 소스의 일봉 시계열은 수집 시점에 2026-08-28을 아직 포함하지 않아 하루 이른 값($139.72)에서 끝난다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-08-28)

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
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="PepsiCo(PEP) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">PepsiCo (PEP) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 $141.07 (2026-08-28) · 단위 USD</text>
<line x1="60" y1="587.5" x2="1052" y2="587.5" class="grid"/>
<text x="52" y="591.5" font-size="11" text-anchor="end" fill="var(--muted)">130</text>
<line x1="60" y1="510.5" x2="1052" y2="510.5" class="grid"/>
<text x="52" y="514.5" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="433.4" x2="1052" y2="433.4" class="grid"/>
<text x="52" y="437.4" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="356.4" x2="1052" y2="356.4" class="grid"/>
<text x="52" y="360.4" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="279.4" x2="1052" y2="279.4" class="grid"/>
<text x="52" y="283.4" font-size="11" text-anchor="end" fill="var(--muted)">170</text>
<line x1="60" y1="202.4" x2="1052" y2="202.4" class="grid"/>
<text x="52" y="206.4" font-size="11" text-anchor="end" fill="var(--muted)">180</text>
<line x1="60" y1="125.3" x2="1052" y2="125.3" class="grid"/>
<text x="52" y="129.3" font-size="11" text-anchor="end" fill="var(--muted)">190</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="130.0" y1="56.0" x2="130.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="130.0" y1="626.0" x2="130.0" y2="631.0" class="axis"/>
<text x="130.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="326.9" y1="56.0" x2="326.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="326.9" y1="626.0" x2="326.9" y2="631.0" class="axis"/>
<text x="326.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="523.8" y1="56.0" x2="523.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="523.8" y1="626.0" x2="523.8" y2="631.0" class="axis"/>
<text x="523.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="724.5" y1="56.0" x2="724.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="724.5" y1="626.0" x2="724.5" y2="631.0" class="axis"/>
<text x="724.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.4" y1="56.0" x2="921.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.4" y1="626.0" x2="921.4" y2="631.0" class="axis"/>
<text x="921.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="370.3" x2="61.9" y2="394.8" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="378.8" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="65.7" y1="379.7" x2="65.7" y2="405.1" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="383.5" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="69.5" y1="376.4" x2="69.5" y2="404.1" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="387.7" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="73.3" y1="386.3" x2="73.3" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="401.1" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="77.0" y1="401.5" x2="77.0" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="404.2" width="2.35" height="22.0" fill="var(--down)"/>
<line x1="80.8" y1="373.7" x2="80.8" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="387.0" width="2.35" height="39.7" fill="var(--up)"/>
<line x1="84.6" y1="359.0" x2="84.6" y2="389.8" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="365.6" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="88.4" y1="341.9" x2="88.4" y2="381.1" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="356.6" width="2.35" height="13.6" fill="var(--up)"/>
<line x1="92.2" y1="339.0" x2="92.2" y2="365.7" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="344.1" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="96.0" y1="306.9" x2="96.0" y2="355.0" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="310.2" width="2.35" height="37.0" fill="var(--up)"/>
<line x1="99.8" y1="309.4" x2="99.8" y2="347.5" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="311.7" width="2.35" height="24.3" fill="var(--down)"/>
<line x1="103.5" y1="317.7" x2="103.5" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="327.1" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="107.3" y1="304.0" x2="107.3" y2="349.6" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="331.8" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="111.1" y1="318.8" x2="111.1" y2="368.8" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="320.1" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="114.9" y1="286.2" x2="114.9" y2="325.4" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="287.3" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="118.7" y1="252.0" x2="118.7" y2="294.4" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="287.6" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="122.5" y1="274.5" x2="122.5" y2="304.4" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="281.1" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="126.3" y1="248.4" x2="126.3" y2="281.1" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="250.8" width="2.35" height="28.7" fill="var(--up)"/>
<line x1="130.0" y1="236.2" x2="130.0" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="248.0" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="133.8" y1="233.6" x2="133.8" y2="266.9" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="235.9" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="137.6" y1="223.6" x2="137.6" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="246.9" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="141.4" y1="229.3" x2="141.4" y2="306.7" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="237.1" width="2.35" height="21.7" fill="var(--down)"/>
<line x1="145.2" y1="228.1" x2="145.2" y2="282.8" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="260.2" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="149.0" y1="256.3" x2="149.0" y2="300.2" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="258.3" width="2.35" height="32.0" fill="var(--down)"/>
<line x1="152.8" y1="281.8" x2="152.8" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="283.8" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="156.5" y1="286.2" x2="156.5" y2="354.2" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="290.4" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="160.3" y1="306.3" x2="160.3" y2="349.3" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="312.1" width="2.35" height="13.2" fill="var(--up)"/>
<line x1="164.1" y1="316.7" x2="164.1" y2="407.5" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="325.1" width="2.35" height="79.6" fill="var(--down)"/>
<line x1="167.9" y1="333.8" x2="167.9" y2="398.8" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="334.9" width="2.35" height="58.8" fill="var(--up)"/>
<line x1="171.7" y1="311.0" x2="171.7" y2="348.2" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="316.0" width="2.35" height="22.9" fill="var(--up)"/>
<line x1="175.5" y1="279.9" x2="175.5" y2="327.8" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="281.2" width="2.35" height="35.9" fill="var(--up)"/>
<line x1="179.3" y1="251.0" x2="179.3" y2="299.0" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="255.3" width="2.35" height="31.0" fill="var(--up)"/>
<line x1="183.1" y1="241.1" x2="183.1" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="251.6" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="186.8" y1="223.6" x2="186.8" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="262.8" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="190.6" y1="220.7" x2="190.6" y2="271.7" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="254.7" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="194.4" y1="247.6" x2="194.4" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="256.3" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="198.2" y1="244.4" x2="198.2" y2="293.6" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="250.7" width="2.35" height="31.3" fill="var(--up)"/>
<line x1="202.0" y1="230.9" x2="202.0" y2="359.3" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="250.8" width="2.35" height="88.6" fill="var(--down)"/>
<line x1="205.8" y1="265.4" x2="205.8" y2="328.9" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="265.7" width="2.35" height="58.2" fill="var(--up)"/>
<line x1="209.6" y1="271.8" x2="209.6" y2="336.0" stroke="var(--down)" class="wick"/>
<rect x="208.38" y="271.8" width="2.35" height="47.2" fill="var(--down)"/>
<line x1="213.3" y1="297.7" x2="213.3" y2="360.6" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="306.6" width="2.35" height="30.3" fill="var(--down)"/>
<line x1="217.1" y1="334.3" x2="217.1" y2="396.0" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="352.3" width="2.35" height="26.7" fill="var(--down)"/>
<line x1="220.9" y1="308.7" x2="220.9" y2="376.8" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="309.2" width="2.35" height="61.3" fill="var(--up)"/>
<line x1="224.7" y1="283.1" x2="224.7" y2="326.7" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="284.1" width="2.35" height="27.1" fill="var(--up)"/>
<line x1="228.5" y1="258.6" x2="228.5" y2="315.3" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="264.9" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="232.3" y1="253.8" x2="232.3" y2="297.1" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="268.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="236.1" y1="269.8" x2="236.1" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="270.5" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="239.8" y1="237.2" x2="239.8" y2="286.8" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="241.2" width="2.35" height="35.8" fill="var(--up)"/>
<line x1="243.6" y1="220.1" x2="243.6" y2="260.9" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="244.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="247.4" y1="222.5" x2="247.4" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="222.9" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="251.2" y1="194.1" x2="251.2" y2="227.0" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="201.0" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="255.0" y1="198.7" x2="255.0" y2="243.4" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="201.3" width="2.35" height="39.3" fill="var(--down)"/>
<line x1="258.8" y1="238.6" x2="258.8" y2="280.2" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="244.3" width="2.35" height="30.0" fill="var(--down)"/>
<line x1="262.6" y1="244.3" x2="262.6" y2="286.1" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="254.6" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="266.4" y1="245.2" x2="266.4" y2="316.0" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="254.6" width="2.35" height="48.1" fill="var(--down)"/>
<line x1="270.1" y1="263.7" x2="270.1" y2="306.3" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="290.8" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="273.9" y1="279.3" x2="273.9" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="292.2" width="2.35" height="39.1" fill="var(--down)"/>
<line x1="277.7" y1="289.2" x2="277.7" y2="348.9" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="329.3" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="281.5" y1="231.2" x2="281.5" y2="347.2" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="277.9" width="2.35" height="63.2" fill="var(--up)"/>
<line x1="285.3" y1="226.2" x2="285.3" y2="274.9" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="255.8" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="289.1" y1="179.8" x2="289.1" y2="243.4" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="185.2" width="2.35" height="57.2" fill="var(--up)"/>
<line x1="292.9" y1="174.8" x2="292.9" y2="229.1" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="193.3" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="296.6" y1="179.9" x2="296.6" y2="237.5" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="206.0" width="2.35" height="11.3" fill="var(--down)"/>
<line x1="300.4" y1="188.2" x2="300.4" y2="237.6" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="192.1" width="2.35" height="20.5" fill="var(--up)"/>
<line x1="304.2" y1="151.4" x2="304.2" y2="186.3" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="170.7" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="308.0" y1="153.6" x2="308.0" y2="200.5" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="158.5" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="311.8" y1="169.3" x2="311.8" y2="197.0" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="175.9" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="315.6" y1="149.7" x2="315.6" y2="214.8" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="170.2" width="2.35" height="29.6" fill="var(--down)"/>
<line x1="319.4" y1="174.0" x2="319.4" y2="210.7" stroke="var(--up)" class="wick"/>
<rect x="318.19" y="184.9" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="323.1" y1="167.4" x2="323.1" y2="207.8" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="177.1" width="2.35" height="20.2" fill="var(--down)"/>
<line x1="326.9" y1="188.3" x2="326.9" y2="228.8" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="193.9" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="330.7" y1="181.0" x2="330.7" y2="247.3" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="199.0" width="2.35" height="40.1" fill="var(--down)"/>
<line x1="334.5" y1="221.2" x2="334.5" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="232.0" width="2.35" height="48.3" fill="var(--down)"/>
<line x1="338.3" y1="264.1" x2="338.3" y2="291.3" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="279.3" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="342.1" y1="261.5" x2="342.1" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="281.1" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="345.9" y1="228.6" x2="345.9" y2="285.1" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="231.6" width="2.35" height="49.8" fill="var(--up)"/>
<line x1="349.6" y1="216.0" x2="349.6" y2="244.4" stroke="var(--up)" class="wick"/>
<rect x="348.48" y="231.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="353.4" y1="222.1" x2="353.4" y2="246.3" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="233.5" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="357.2" y1="223.5" x2="357.2" y2="286.2" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="225.7" width="2.35" height="29.4" fill="var(--down)"/>
<line x1="361.0" y1="245.8" x2="361.0" y2="272.0" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="262.3" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="364.8" y1="223.7" x2="364.8" y2="267.3" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="239.9" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="368.6" y1="207.2" x2="368.6" y2="240.7" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="209.4" width="2.35" height="19.9" fill="var(--up)"/>
<line x1="372.4" y1="183.2" x2="372.4" y2="207.7" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="184.6" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="376.2" y1="164.1" x2="376.2" y2="199.3" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="168.8" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="379.9" y1="166.8" x2="379.9" y2="189.3" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="172.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="383.7" y1="153.2" x2="383.7" y2="175.5" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="160.7" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="387.5" y1="112.8" x2="387.5" y2="163.7" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="118.5" width="2.35" height="33.8" fill="var(--up)"/>
<line x1="391.3" y1="90.8" x2="391.3" y2="127.2" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="92.4" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="395.1" y1="77.4" x2="395.1" y2="104.9" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="78.2" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="398.9" y1="72.3" x2="398.9" y2="122.2" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="74.7" width="2.35" height="36.4" fill="var(--down)"/>
<line x1="402.7" y1="114.6" x2="402.7" y2="187.3" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="116.2" width="2.35" height="58.6" fill="var(--down)"/>
<line x1="406.4" y1="166.8" x2="406.4" y2="197.0" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="171.1" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="410.2" y1="154.8" x2="410.2" y2="207.5" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="172.7" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="414.0" y1="143.9" x2="414.0" y2="197.0" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="155.8" width="2.35" height="27.3" fill="var(--up)"/>
<line x1="417.8" y1="140.7" x2="417.8" y2="170.1" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="152.0" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="421.6" y1="150.4" x2="421.6" y2="191.6" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="154.9" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="425.4" y1="150.4" x2="425.4" y2="179.0" stroke="var(--down)" class="wick"/>
<rect x="424.20" y="169.2" width="2.35" height="9.4" fill="var(--down)"/>
<line x1="429.2" y1="135.9" x2="429.2" y2="183.7" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="139.1" width="2.35" height="31.9" fill="var(--up)"/>
<line x1="432.9" y1="114.0" x2="432.9" y2="172.9" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="124.1" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="436.7" y1="107.0" x2="436.7" y2="137.6" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="120.8" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="440.5" y1="125.6" x2="440.5" y2="168.8" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="129.6" width="2.35" height="37.4" fill="var(--down)"/>
<line x1="444.3" y1="144.7" x2="444.3" y2="182.1" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="161.7" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="448.1" y1="164.9" x2="448.1" y2="223.4" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="168.5" width="2.35" height="47.8" fill="var(--down)"/>
<line x1="451.9" y1="199.0" x2="451.9" y2="238.5" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="206.8" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="455.7" y1="184.9" x2="455.7" y2="243.6" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="196.0" width="2.35" height="42.4" fill="var(--down)"/>
<line x1="459.5" y1="224.3" x2="459.5" y2="252.6" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="231.1" width="2.35" height="7.7" fill="var(--up)"/>
<line x1="463.2" y1="188.3" x2="463.2" y2="226.8" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="203.6" width="2.35" height="23.2" fill="var(--up)"/>
<line x1="467.0" y1="194.6" x2="467.0" y2="245.7" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="194.6" width="2.35" height="44.1" fill="var(--down)"/>
<line x1="470.8" y1="237.5" x2="470.8" y2="294.5" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="243.3" width="2.35" height="40.4" fill="var(--down)"/>
<line x1="474.6" y1="279.4" x2="474.6" y2="388.5" stroke="var(--down)" class="wick"/>
<rect x="473.42" y="286.5" width="2.35" height="67.7" fill="var(--down)"/>
<line x1="478.4" y1="314.5" x2="478.4" y2="376.2" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="356.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="482.2" y1="330.2" x2="482.2" y2="362.9" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="348.7" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="486.0" y1="329.4" x2="486.0" y2="365.0" stroke="var(--up)" class="wick"/>
<rect x="484.78" y="359.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="489.7" y1="288.5" x2="489.7" y2="350.7" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="304.1" width="2.35" height="42.3" fill="var(--up)"/>
<line x1="493.5" y1="292.2" x2="493.5" y2="319.0" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="303.1" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="497.3" y1="279.4" x2="497.3" y2="312.0" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="302.5" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="501.1" y1="279.2" x2="501.1" y2="312.3" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="284.2" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="504.9" y1="281.2" x2="504.9" y2="319.3" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="281.7" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="508.7" y1="280.0" x2="508.7" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="291.7" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="512.5" y1="263.6" x2="512.5" y2="306.7" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="299.1" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="516.2" y1="277.5" x2="516.2" y2="314.9" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="294.3" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="520.0" y1="278.8" x2="520.0" y2="300.6" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="280.6" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="523.8" y1="239.3" x2="523.8" y2="298.2" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="283.1" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="527.6" y1="281.5" x2="527.6" y2="319.3" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="287.5" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="531.4" y1="298.5" x2="531.4" y2="318.0" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="300.4" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="535.2" y1="294.6" x2="535.2" y2="322.8" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="295.9" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="539.0" y1="264.3" x2="539.0" y2="301.2" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="271.9" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="542.7" y1="247.8" x2="542.7" y2="302.7" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="275.1" width="2.35" height="22.2" fill="var(--down)"/>
<line x1="546.5" y1="268.2" x2="546.5" y2="312.7" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="295.9" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="550.3" y1="277.5" x2="550.3" y2="309.4" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="282.5" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="554.1" y1="283.8" x2="554.1" y2="331.4" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="283.8" width="2.35" height="37.2" fill="var(--down)"/>
<line x1="557.9" y1="312.9" x2="557.9" y2="342.5" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="322.1" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="561.7" y1="308.2" x2="561.7" y2="330.9" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="320.5" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="565.5" y1="253.0" x2="565.5" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="263.8" width="2.35" height="38.3" fill="var(--up)"/>
<line x1="569.3" y1="234.6" x2="569.3" y2="265.4" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="240.8" width="2.35" height="21.6" fill="var(--up)"/>
<line x1="573.0" y1="231.4" x2="573.0" y2="294.2" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="236.5" width="2.35" height="49.5" fill="var(--down)"/>
<line x1="576.8" y1="273.8" x2="576.8" y2="300.0" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="285.9" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="580.6" y1="246.5" x2="580.6" y2="310.0" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="247.6" width="2.35" height="37.9" fill="var(--up)"/>
<line x1="584.4" y1="197.5" x2="584.4" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="236.4" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="588.2" y1="229.4" x2="588.2" y2="251.2" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="232.0" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="592.0" y1="201.1" x2="592.0" y2="239.9" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="204.0" width="2.35" height="23.3" fill="var(--up)"/>
<line x1="595.8" y1="176.1" x2="595.8" y2="213.1" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="185.5" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="599.5" y1="185.9" x2="599.5" y2="218.8" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="186.3" width="2.35" height="31.6" fill="var(--down)"/>
<line x1="603.3" y1="231.0" x2="603.3" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="231.4" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="607.1" y1="245.5" x2="607.1" y2="273.6" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="258.4" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="610.9" y1="276.5" x2="610.9" y2="344.5" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="278.5" width="2.35" height="48.5" fill="var(--down)"/>
<line x1="614.7" y1="286.5" x2="614.7" y2="334.9" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="300.3" width="2.35" height="29.2" fill="var(--up)"/>
<line x1="618.5" y1="282.4" x2="618.5" y2="320.8" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="298.6" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="622.3" y1="309.7" x2="622.3" y2="341.3" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="317.6" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="626.0" y1="294.6" x2="626.0" y2="371.6" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="307.3" width="2.35" height="25.6" fill="var(--up)"/>
<line x1="629.8" y1="258.8" x2="629.8" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="284.3" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="633.6" y1="252.5" x2="633.6" y2="318.3" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="258.2" width="2.35" height="26.9" fill="var(--up)"/>
<line x1="637.4" y1="202.7" x2="637.4" y2="272.8" stroke="var(--up)" class="wick"/>
<rect x="636.23" y="217.4" width="2.35" height="44.3" fill="var(--up)"/>
<line x1="641.2" y1="195.3" x2="641.2" y2="280.8" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="206.0" width="2.35" height="54.9" fill="var(--down)"/>
<line x1="645.0" y1="245.9" x2="645.0" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="259.2" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="648.8" y1="226.8" x2="648.8" y2="260.6" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="234.2" width="2.35" height="24.7" fill="var(--up)"/>
<line x1="652.5" y1="226.4" x2="652.5" y2="269.8" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="230.7" width="2.35" height="26.5" fill="var(--down)"/>
<line x1="656.3" y1="204.4" x2="656.3" y2="264.9" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="222.8" width="2.35" height="38.2" fill="var(--up)"/>
<line x1="660.1" y1="209.3" x2="660.1" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="222.7" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="663.9" y1="206.7" x2="663.9" y2="277.7" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="210.1" width="2.35" height="60.2" fill="var(--down)"/>
<line x1="667.7" y1="249.0" x2="667.7" y2="289.5" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="272.7" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="671.5" y1="264.4" x2="671.5" y2="303.9" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="274.9" width="2.35" height="20.1" fill="var(--down)"/>
<line x1="675.3" y1="239.5" x2="675.3" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="242.3" width="2.35" height="54.6" fill="var(--up)"/>
<line x1="679.1" y1="222.5" x2="679.1" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="240.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="682.8" y1="221.6" x2="682.8" y2="267.1" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="245.0" width="2.35" height="20.6" fill="var(--down)"/>
<line x1="686.6" y1="256.4" x2="686.6" y2="316.3" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="256.4" width="2.35" height="56.9" fill="var(--down)"/>
<line x1="690.4" y1="295.1" x2="690.4" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="313.3" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="694.2" y1="303.3" x2="694.2" y2="371.4" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="322.4" width="2.35" height="44.6" fill="var(--down)"/>
<line x1="698.0" y1="340.5" x2="698.0" y2="388.4" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="341.0" width="2.35" height="19.9" fill="var(--up)"/>
<line x1="701.8" y1="316.9" x2="701.8" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="329.8" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="705.6" y1="328.3" x2="705.6" y2="374.2" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="330.8" width="2.35" height="42.6" fill="var(--down)"/>
<line x1="709.3" y1="344.9" x2="709.3" y2="385.2" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="372.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="713.1" y1="365.5" x2="713.1" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="373.0" width="2.35" height="39.0" fill="var(--down)"/>
<line x1="716.9" y1="406.7" x2="716.9" y2="435.7" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="411.2" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="720.7" y1="405.2" x2="720.7" y2="436.8" stroke="var(--down)" class="wick"/>
<rect x="719.53" y="412.9" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="724.5" y1="433.8" x2="724.5" y2="498.8" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="436.5" width="2.35" height="53.6" fill="var(--down)"/>
<line x1="728.3" y1="444.1" x2="728.3" y2="494.0" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="446.9" width="2.35" height="42.1" fill="var(--up)"/>
<line x1="732.1" y1="435.1" x2="732.1" y2="459.5" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="440.2" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="735.8" y1="391.3" x2="735.8" y2="432.5" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="426.3" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="739.6" y1="424.7" x2="739.6" y2="489.7" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="435.3" width="2.35" height="39.9" fill="var(--down)"/>
<line x1="743.4" y1="462.9" x2="743.4" y2="487.3" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="477.0" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="747.2" y1="398.4" x2="747.2" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="406.5" width="2.35" height="81.6" fill="var(--up)"/>
<line x1="751.0" y1="368.3" x2="751.0" y2="434.0" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="406.7" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="754.8" y1="355.3" x2="754.8" y2="429.6" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="399.2" width="2.35" height="23.8" fill="var(--up)"/>
<line x1="758.6" y1="355.8" x2="758.6" y2="460.3" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="388.1" width="2.35" height="56.2" fill="var(--down)"/>
<line x1="762.4" y1="420.6" x2="762.4" y2="473.9" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="439.4" width="2.35" height="29.1" fill="var(--down)"/>
<line x1="766.1" y1="422.8" x2="766.1" y2="473.3" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="439.1" width="2.35" height="29.1" fill="var(--up)"/>
<line x1="769.9" y1="395.5" x2="769.9" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="431.9" width="2.35" height="27.7" fill="var(--down)"/>
<line x1="773.7" y1="455.5" x2="773.7" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="476.3" width="2.35" height="24.0" fill="var(--up)"/>
<line x1="777.5" y1="455.2" x2="777.5" y2="512.2" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="478.4" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="781.3" y1="477.5" x2="781.3" y2="573.6" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="491.2" width="2.35" height="70.2" fill="var(--down)"/>
<line x1="785.1" y1="539.9" x2="785.1" y2="575.8" stroke="var(--down)" class="wick"/>
<rect x="783.89" y="557.4" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="788.9" y1="556.4" x2="788.9" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="556.4" width="2.35" height="27.7" fill="var(--down)"/>
<line x1="792.6" y1="569.5" x2="792.6" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="572.2" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="796.4" y1="570.1" x2="796.4" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="571.1" width="2.35" height="21.5" fill="var(--down)"/>
<line x1="800.2" y1="566.5" x2="800.2" y2="594.2" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="576.3" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="804.0" y1="566.4" x2="804.0" y2="594.6" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="580.6" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="807.8" y1="563.9" x2="807.8" y2="593.8" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="580.9" width="2.35" height="7.9" fill="var(--up)"/>
<line x1="811.6" y1="571.4" x2="811.6" y2="598.3" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="577.4" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="815.4" y1="577.2" x2="815.4" y2="606.0" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="579.5" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="819.1" y1="533.6" x2="819.1" y2="582.9" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="546.0" width="2.35" height="32.2" fill="var(--up)"/>
<line x1="822.9" y1="536.0" x2="822.9" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="544.9" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="826.7" y1="461.5" x2="826.7" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="485.5" width="2.35" height="65.4" fill="var(--up)"/>
<line x1="830.5" y1="456.3" x2="830.5" y2="506.9" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="483.9" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="834.3" y1="476.6" x2="834.3" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="489.7" width="2.35" height="26.3" fill="var(--down)"/>
<line x1="838.1" y1="469.1" x2="838.1" y2="520.1" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="470.3" width="2.35" height="45.6" fill="var(--up)"/>
<line x1="841.9" y1="425.0" x2="841.9" y2="481.6" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="430.4" width="2.35" height="39.1" fill="var(--up)"/>
<line x1="845.6" y1="397.9" x2="845.6" y2="444.2" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="429.2" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="849.4" y1="439.4" x2="849.4" y2="465.7" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="443.8" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="853.2" y1="373.4" x2="853.2" y2="469.8" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="376.1" width="2.35" height="85.1" fill="var(--down)"/>
<line x1="857.0" y1="466.4" x2="857.0" y2="507.8" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="466.4" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="860.8" y1="483.3" x2="860.8" y2="511.2" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="484.3" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="864.6" y1="484.1" x2="864.6" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="502.1" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="868.4" y1="484.5" x2="868.4" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="495.2" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="872.2" y1="427.1" x2="872.2" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="432.8" width="2.35" height="64.0" fill="var(--up)"/>
<line x1="875.9" y1="399.7" x2="875.9" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="404.9" width="2.35" height="39.0" fill="var(--up)"/>
<line x1="879.7" y1="393.5" x2="879.7" y2="425.5" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="399.4" width="2.35" height="22.1" fill="var(--down)"/>
<line x1="883.5" y1="408.7" x2="883.5" y2="482.2" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="425.7" width="2.35" height="37.9" fill="var(--down)"/>
<line x1="887.3" y1="464.9" x2="887.3" y2="500.4" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="465.3" width="2.35" height="22.4" fill="var(--down)"/>
<line x1="891.1" y1="457.8" x2="891.1" y2="500.8" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="465.4" width="2.35" height="25.9" fill="var(--up)"/>
<line x1="894.9" y1="434.7" x2="894.9" y2="472.7" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="461.7" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="898.7" y1="442.5" x2="898.7" y2="473.8" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="443.1" width="2.35" height="22.4" fill="var(--up)"/>
<line x1="902.4" y1="428.0" x2="902.4" y2="475.7" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="444.0" width="2.35" height="27.8" fill="var(--down)"/>
<line x1="906.2" y1="426.6" x2="906.2" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="428.4" width="2.35" height="43.4" fill="var(--up)"/>
<line x1="910.0" y1="415.3" x2="910.0" y2="449.6" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="426.2" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="913.8" y1="441.3" x2="913.8" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="452.5" width="2.35" height="28.9" fill="var(--down)"/>
<line x1="917.6" y1="469.9" x2="917.6" y2="494.3" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="481.7" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="921.4" y1="496.5" x2="921.4" y2="541.2" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="497.7" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="925.2" y1="452.3" x2="925.2" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="461.8" width="2.35" height="49.4" fill="var(--up)"/>
<line x1="928.9" y1="448.8" x2="928.9" y2="486.9" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="462.5" width="2.35" height="12.6" fill="var(--down)"/>
<line x1="932.7" y1="403.5" x2="932.7" y2="478.6" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="405.5" width="2.35" height="68.0" fill="var(--up)"/>
<line x1="936.5" y1="273.6" x2="936.5" y2="408.9" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="275.6" width="2.35" height="126.6" fill="var(--up)"/>
<line x1="940.3" y1="268.0" x2="940.3" y2="327.6" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="283.2" width="2.35" height="27.4" fill="var(--down)"/>
<line x1="944.1" y1="298.3" x2="944.1" y2="351.6" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="309.3" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="947.9" y1="277.2" x2="947.9" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="281.4" width="2.35" height="40.4" fill="var(--up)"/>
<line x1="951.7" y1="282.9" x2="951.7" y2="386.5" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="286.7" width="2.35" height="74.1" fill="var(--down)"/>
<line x1="955.5" y1="334.4" x2="955.5" y2="372.7" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="357.3" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="959.2" y1="344.2" x2="959.2" y2="438.5" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="345.9" width="2.35" height="87.2" fill="var(--down)"/>
<line x1="963.0" y1="398.5" x2="963.0" y2="440.9" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="410.0" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="966.8" y1="368.8" x2="966.8" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="379.4" width="2.35" height="24.6" fill="var(--up)"/>
<line x1="970.6" y1="371.7" x2="970.6" y2="420.0" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="379.1" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="974.4" y1="356.2" x2="974.4" y2="407.7" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="374.4" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="978.2" y1="365.3" x2="978.2" y2="406.1" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="366.1" width="2.35" height="25.4" fill="var(--down)"/>
<line x1="982.0" y1="356.4" x2="982.0" y2="406.6" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="376.4" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="985.7" y1="376.8" x2="985.7" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="388.0" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="989.5" y1="397.2" x2="989.5" y2="447.7" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="399.6" width="2.35" height="40.6" fill="var(--down)"/>
<line x1="993.3" y1="413.6" x2="993.3" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="429.0" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="997.1" y1="431.5" x2="997.1" y2="483.1" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="435.7" width="2.35" height="42.5" fill="var(--down)"/>
<line x1="1000.9" y1="466.6" x2="1000.9" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="490.5" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="1004.7" y1="468.5" x2="1004.7" y2="516.2" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="477.6" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="1008.5" y1="451.6" x2="1008.5" y2="503.9" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="487.2" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="1012.2" y1="481.7" x2="1012.2" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="499.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1016.0" y1="473.9" x2="1016.0" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="478.0" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="1019.8" y1="440.8" x2="1019.8" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="477.8" width="2.35" height="52.8" fill="var(--down)"/>
<line x1="1023.6" y1="495.4" x2="1023.6" y2="551.7" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="525.7" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="1027.4" y1="529.0" x2="1027.4" y2="558.8" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="529.2" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="1031.2" y1="468.6" x2="1031.2" y2="533.5" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="513.8" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="1035.0" y1="498.5" x2="1035.0" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="502.1" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="1038.7" y1="500.7" x2="1038.7" y2="535.6" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="504.4" width="2.35" height="17.5" fill="var(--up)"/>
<line x1="1042.5" y1="482.5" x2="1042.5" y2="528.5" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="483.7" width="2.35" height="29.0" fill="var(--up)"/>
<line x1="1046.3" y1="465.0" x2="1046.3" y2="512.9" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="472.6" width="2.35" height="40.0" fill="var(--down)"/>
<line x1="1050.1" y1="500.5" x2="1050.1" y2="510.5" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="502.2" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="60" y1="428.1" x2="1052" y2="428.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="431.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$151 R1</text>
<text x="1058" y="443.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="374.0" x2="1052" y2="374.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="377.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$158 R2</text>
<text x="1058" y="389.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="233.9" x2="1052" y2="233.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="237.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$176 R3</text>
<text x="1058" y="249.4" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="504.8" x2="1052" y2="504.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="498.8" font-size="11.5" fill="var(--support)" font-weight="600">$141 S1</text>
<text x="1058" y="510.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="550.0" x2="1052" y2="550.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="544.0" font-size="11.5" fill="var(--support)" font-weight="600">$135 S2</text>
<text x="1058" y="556.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="605.4" x2="1052" y2="605.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="599.4" font-size="11.5" fill="var(--support)" font-weight="600">$128 S3</text>
<text x="1058" y="611.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="502.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="494.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $141 (2026-08-28)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $176 | 7 | 2022-01~2024-10에 걸쳐 7회 확인된 5년 최상단 저항. 2026-02에도 한 차례 닿았다 |
| R2 | $158 | 3 | 2025-03~10 하락 과정의 반등 고점대 |
| R1 | $151 | 2 | 2025-12·2026-07 반등 고점. 현재가 위 가장 가까운 저항 |
| **현재가** | **$141.07** (2026-08-28 종가) | — | R1과 S1 사이 |
| S1 | $141 | 4 | 2025-01~02와 2025-10~11에 확인된 지지대. **현재가 $141.07이 사실상 이 레벨 위에 걸쳐 있다** |
| S2 | $135 | 2 | 2026-01·2026-07 저점대. 1년 일봉 기준 52주 최저($133.73)와 가까운 구간 |
| S3 | $128 | 2 | 2025-05~06 저점대. 5년 구조상 마지막 지지 |

> **현재가가 S1($141)과 사실상 겹쳐 있다는 점이 이 차트의 핵심**이다. 2025-01~02와 2025-10~11에 네 차례 확인된 이 지지대를 종가 기준으로 밑돌면, 다음 지지는 $135(S2)까지 비어 있다.

---

## 3. 관측된 특이 구간 — 2024년 이후의 다년 하락 추세

- 5년 구조에서 가장 두드러진 것은 **2023년 중반 $196 부근에서 시작된 하락이 3년째 이어지고 있다**는 점이다. R3($176)는 2022-01~2024-10에 7회 확인된 5년 최상단 저항이고, 그 아래 R2($158)·R1($151)이 차례로 지지에서 저항으로 뒤집혔다.
- 이 하락은 단일 사건이 아니라 **북미 물량 감소와 배수 축소(코어 PER 22.3배 → 17.7배)가 3년에 걸쳐 누적된 결과**다. 특정 갭이나 급락 구간으로 설명되지 않으므로 일봉 문서와 달리 여기서는 개별 이벤트를 짚지 않는다.
- 결과적으로 현재가 $141.07은 5년 최고가($176 클러스터) 대비 약 20% 낮고, 5년 구조상 마지막 지지대인 S3($128)까지는 약 9% 여유가 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-30~2026-08-28. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py` (`PEP --name "PepsiCo" --interval 1wk --close-on 2026-08-27`)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3개월 이상 이어진 다년 하락 추세에서는 **과거 지지대가 저항으로 뒤집히는 경우가 많다** — R1($151)·R2($158)은 원래 지지대였던 구간이다.
    - 기간 내 주식분할·유상증자는 없었다. **원주가(배당 미반영)**이며 5년간 분기배당이 매 분기 지급됐으므로, 총수익 기준으로 보면 실제 투자 성과는 이 차트가 보여주는 가격 하락보다 낫다.

---

*작성일: 2026-08-30*
