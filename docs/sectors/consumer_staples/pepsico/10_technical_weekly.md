# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: 2026-09-10 종가 **$136.65**는 [핵심 지표 A.2](./04_metrics.md)·[밸류에이션 / 적정주가 5. 결론 — 목표주가와 판단](./06_valuation.md)에 인용된 값과 **일치**한다.

:::

---

## 1. 차트 — 최근 5년 주봉 (2021-09-06 ~ 2026-09-10)

<style>
.pep-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .pep-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.pep-chart svg { width:100%; height:auto; display:block; }
.pep-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.pep-chart .title { fill: var(--ink); font-weight:600; }
.pep-chart .grid { stroke: var(--grid); stroke-width:1; }
.pep-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="pep-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="펩시코(PEP) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">펩시코 (PEP) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-10 · 마지막 종가 $136.65 (2026-09-10) · 단위 USD</text>
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
<line x1="126.0" y1="56.0" x2="126.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="126.0" y1="626.0" x2="126.0" y2="631.0" class="axis"/>
<text x="126.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="322.1" y1="56.0" x2="322.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="322.1" y1="626.0" x2="322.1" y2="631.0" class="axis"/>
<text x="322.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="518.3" y1="56.0" x2="518.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="518.3" y1="626.0" x2="518.3" y2="631.0" class="axis"/>
<text x="518.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="718.2" y1="56.0" x2="718.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="718.2" y1="626.0" x2="718.2" y2="631.0" class="axis"/>
<text x="718.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="914.3" y1="56.0" x2="914.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="914.3" y1="626.0" x2="914.3" y2="631.0" class="axis"/>
<text x="914.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="385.3" x2="61.9" y2="394.8" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="387.4" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="65.7" y1="376.4" x2="65.7" y2="404.1" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="387.7" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="69.4" y1="386.3" x2="69.4" y2="414.8" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="401.1" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="73.2" y1="401.5" x2="73.2" y2="437.1" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="404.2" width="2.34" height="22.0" fill="var(--down)"/>
<line x1="77.0" y1="373.7" x2="77.0" y2="437.4" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="387.0" width="2.34" height="39.7" fill="var(--up)"/>
<line x1="80.7" y1="359.0" x2="80.7" y2="389.8" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="365.6" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="84.5" y1="341.9" x2="84.5" y2="381.1" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="356.6" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="88.3" y1="339.0" x2="88.3" y2="365.7" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="344.1" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="92.1" y1="306.9" x2="92.1" y2="355.0" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="310.2" width="2.34" height="37.0" fill="var(--up)"/>
<line x1="95.8" y1="309.4" x2="95.8" y2="347.5" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="311.7" width="2.34" height="24.3" fill="var(--down)"/>
<line x1="99.6" y1="317.7" x2="99.6" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="327.1" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="103.4" y1="304.0" x2="103.4" y2="349.6" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="331.8" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="107.1" y1="318.8" x2="107.1" y2="368.8" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="320.1" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="110.9" y1="286.2" x2="110.9" y2="325.4" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="287.3" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="114.7" y1="252.0" x2="114.7" y2="294.4" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="287.6" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="118.5" y1="274.5" x2="118.5" y2="304.4" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="281.1" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="122.2" y1="248.4" x2="122.2" y2="281.1" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="250.8" width="2.34" height="28.7" fill="var(--up)"/>
<line x1="126.0" y1="236.2" x2="126.0" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="248.0" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="129.8" y1="233.6" x2="129.8" y2="266.9" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="235.9" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="133.6" y1="223.6" x2="133.6" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="246.9" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="137.3" y1="229.3" x2="137.3" y2="306.7" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="237.1" width="2.34" height="21.7" fill="var(--down)"/>
<line x1="141.1" y1="228.1" x2="141.1" y2="282.8" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="260.2" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="144.9" y1="256.3" x2="144.9" y2="300.2" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="258.3" width="2.34" height="32.0" fill="var(--down)"/>
<line x1="148.6" y1="281.8" x2="148.6" y2="321.4" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="283.8" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="152.4" y1="286.2" x2="152.4" y2="354.2" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="290.4" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="156.2" y1="306.3" x2="156.2" y2="349.3" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="312.1" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="160.0" y1="316.7" x2="160.0" y2="407.5" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="325.1" width="2.34" height="79.6" fill="var(--down)"/>
<line x1="163.7" y1="333.8" x2="163.7" y2="398.8" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="334.9" width="2.34" height="58.8" fill="var(--up)"/>
<line x1="167.5" y1="311.0" x2="167.5" y2="348.2" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="316.0" width="2.34" height="22.9" fill="var(--up)"/>
<line x1="171.3" y1="279.9" x2="171.3" y2="327.8" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="281.2" width="2.34" height="35.9" fill="var(--up)"/>
<line x1="175.0" y1="251.0" x2="175.0" y2="299.0" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="255.3" width="2.34" height="31.0" fill="var(--up)"/>
<line x1="178.8" y1="241.1" x2="178.8" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="251.6" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="182.6" y1="223.6" x2="182.6" y2="280.6" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="262.8" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="186.4" y1="220.7" x2="186.4" y2="271.7" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="254.7" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="190.1" y1="247.6" x2="190.1" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="256.3" width="2.34" height="19.9" fill="var(--down)"/>
<line x1="193.9" y1="244.4" x2="193.9" y2="293.6" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="250.7" width="2.34" height="31.3" fill="var(--up)"/>
<line x1="197.7" y1="230.9" x2="197.7" y2="359.3" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="250.8" width="2.34" height="88.6" fill="var(--down)"/>
<line x1="201.4" y1="265.4" x2="201.4" y2="328.9" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="265.7" width="2.34" height="58.2" fill="var(--up)"/>
<line x1="205.2" y1="271.8" x2="205.2" y2="336.0" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="271.8" width="2.34" height="47.2" fill="var(--down)"/>
<line x1="209.0" y1="297.7" x2="209.0" y2="360.6" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="306.6" width="2.34" height="30.3" fill="var(--down)"/>
<line x1="212.8" y1="334.3" x2="212.8" y2="396.0" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="352.3" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="216.5" y1="308.7" x2="216.5" y2="376.8" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="309.2" width="2.34" height="61.3" fill="var(--up)"/>
<line x1="220.3" y1="283.1" x2="220.3" y2="326.7" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="284.1" width="2.34" height="27.1" fill="var(--up)"/>
<line x1="224.1" y1="258.6" x2="224.1" y2="315.3" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="264.9" width="2.34" height="25.0" fill="var(--up)"/>
<line x1="227.8" y1="253.8" x2="227.8" y2="297.1" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="268.5" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="231.6" y1="269.8" x2="231.6" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="270.5" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="235.4" y1="237.2" x2="235.4" y2="286.8" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="241.2" width="2.34" height="35.8" fill="var(--up)"/>
<line x1="239.2" y1="220.1" x2="239.2" y2="260.9" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="244.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="242.9" y1="222.5" x2="242.9" y2="253.8" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="222.9" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="246.7" y1="194.1" x2="246.7" y2="227.0" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="201.0" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="250.5" y1="198.7" x2="250.5" y2="243.4" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="201.3" width="2.34" height="39.3" fill="var(--down)"/>
<line x1="254.3" y1="238.6" x2="254.3" y2="280.2" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="244.3" width="2.34" height="30.0" fill="var(--down)"/>
<line x1="258.0" y1="244.3" x2="258.0" y2="286.1" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="254.6" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="261.8" y1="245.2" x2="261.8" y2="316.0" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="254.6" width="2.34" height="48.1" fill="var(--down)"/>
<line x1="265.6" y1="263.7" x2="265.6" y2="306.3" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="290.8" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="269.3" y1="279.3" x2="269.3" y2="333.2" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="292.2" width="2.34" height="39.1" fill="var(--down)"/>
<line x1="273.1" y1="289.2" x2="273.1" y2="348.9" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="329.3" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="276.9" y1="231.2" x2="276.9" y2="347.2" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="277.9" width="2.34" height="63.2" fill="var(--up)"/>
<line x1="280.7" y1="226.2" x2="280.7" y2="274.9" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="255.8" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="284.4" y1="179.8" x2="284.4" y2="243.4" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="185.2" width="2.34" height="57.2" fill="var(--up)"/>
<line x1="288.2" y1="174.8" x2="288.2" y2="229.1" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="193.3" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="292.0" y1="179.9" x2="292.0" y2="237.5" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="206.0" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="295.7" y1="188.2" x2="295.7" y2="237.6" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="192.1" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="299.5" y1="151.4" x2="299.5" y2="186.3" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="170.7" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="303.3" y1="153.6" x2="303.3" y2="200.5" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="158.5" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="307.1" y1="169.3" x2="307.1" y2="197.0" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="175.9" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="310.8" y1="149.7" x2="310.8" y2="214.8" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="170.2" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="314.6" y1="174.0" x2="314.6" y2="210.7" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="184.9" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="318.4" y1="167.4" x2="318.4" y2="207.8" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="177.1" width="2.34" height="20.2" fill="var(--down)"/>
<line x1="322.1" y1="188.3" x2="322.1" y2="228.8" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="193.9" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="325.9" y1="181.0" x2="325.9" y2="247.3" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="199.0" width="2.34" height="40.1" fill="var(--down)"/>
<line x1="329.7" y1="221.2" x2="329.7" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="328.52" y="232.0" width="2.34" height="48.3" fill="var(--down)"/>
<line x1="333.5" y1="264.1" x2="333.5" y2="291.3" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="279.3" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="337.2" y1="261.5" x2="337.2" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="281.1" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="341.0" y1="228.6" x2="341.0" y2="285.1" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="231.6" width="2.34" height="49.8" fill="var(--up)"/>
<line x1="344.8" y1="216.0" x2="344.8" y2="244.4" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="231.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="348.5" y1="222.1" x2="348.5" y2="246.3" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="233.5" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="352.3" y1="223.5" x2="352.3" y2="286.2" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="225.7" width="2.34" height="29.4" fill="var(--down)"/>
<line x1="356.1" y1="245.8" x2="356.1" y2="272.0" stroke="var(--down)" class="wick"/>
<rect x="354.92" y="262.3" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="359.9" y1="223.7" x2="359.9" y2="267.3" stroke="var(--up)" class="wick"/>
<rect x="358.69" y="239.9" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="363.6" y1="207.2" x2="363.6" y2="240.7" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="209.4" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="367.4" y1="183.2" x2="367.4" y2="207.7" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="184.6" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="371.2" y1="164.1" x2="371.2" y2="199.3" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="168.8" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="375.0" y1="166.8" x2="375.0" y2="189.3" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="172.8" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="378.7" y1="153.2" x2="378.7" y2="175.5" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="160.7" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="382.5" y1="112.8" x2="382.5" y2="163.7" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="118.5" width="2.34" height="33.8" fill="var(--up)"/>
<line x1="386.3" y1="90.8" x2="386.3" y2="127.2" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="92.4" width="2.34" height="29.4" fill="var(--up)"/>
<line x1="390.0" y1="77.4" x2="390.0" y2="104.9" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="78.2" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="393.8" y1="72.3" x2="393.8" y2="122.2" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="74.7" width="2.34" height="36.4" fill="var(--down)"/>
<line x1="397.6" y1="114.6" x2="397.6" y2="187.3" stroke="var(--down)" class="wick"/>
<rect x="396.41" y="116.2" width="2.34" height="58.6" fill="var(--down)"/>
<line x1="401.4" y1="166.8" x2="401.4" y2="197.0" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="171.1" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="405.1" y1="154.8" x2="405.1" y2="207.5" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="172.7" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="408.9" y1="143.9" x2="408.9" y2="197.0" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="155.8" width="2.34" height="27.3" fill="var(--up)"/>
<line x1="412.7" y1="140.7" x2="412.7" y2="170.1" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="152.0" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="416.4" y1="150.4" x2="416.4" y2="191.6" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="154.9" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="420.2" y1="150.4" x2="420.2" y2="179.0" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="169.2" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="424.0" y1="135.9" x2="424.0" y2="183.7" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="139.1" width="2.34" height="31.9" fill="var(--up)"/>
<line x1="427.8" y1="114.0" x2="427.8" y2="172.9" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="124.1" width="2.34" height="29.4" fill="var(--up)"/>
<line x1="431.5" y1="107.0" x2="431.5" y2="137.6" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="120.8" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="435.3" y1="125.6" x2="435.3" y2="168.8" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="129.6" width="2.34" height="37.4" fill="var(--down)"/>
<line x1="439.1" y1="144.7" x2="439.1" y2="182.1" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="161.7" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="442.8" y1="164.9" x2="442.8" y2="223.4" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="168.5" width="2.34" height="47.8" fill="var(--down)"/>
<line x1="446.6" y1="199.0" x2="446.6" y2="238.5" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="206.8" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="450.4" y1="184.9" x2="450.4" y2="243.6" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="196.0" width="2.34" height="42.4" fill="var(--down)"/>
<line x1="454.2" y1="224.3" x2="454.2" y2="252.6" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="231.1" width="2.34" height="7.7" fill="var(--up)"/>
<line x1="457.9" y1="188.3" x2="457.9" y2="226.8" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="203.6" width="2.34" height="23.2" fill="var(--up)"/>
<line x1="461.7" y1="194.6" x2="461.7" y2="245.7" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="194.6" width="2.34" height="44.1" fill="var(--down)"/>
<line x1="465.5" y1="237.5" x2="465.5" y2="294.5" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="243.3" width="2.34" height="40.4" fill="var(--down)"/>
<line x1="469.2" y1="279.4" x2="469.2" y2="388.5" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="286.5" width="2.34" height="67.7" fill="var(--down)"/>
<line x1="473.0" y1="314.5" x2="473.0" y2="376.2" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="356.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="476.8" y1="330.2" x2="476.8" y2="362.9" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="348.7" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="480.6" y1="329.4" x2="480.6" y2="365.0" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="359.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="484.3" y1="288.5" x2="484.3" y2="350.7" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="304.1" width="2.34" height="42.3" fill="var(--up)"/>
<line x1="488.1" y1="292.2" x2="488.1" y2="319.0" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="303.1" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="491.9" y1="279.4" x2="491.9" y2="312.0" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="302.5" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="495.7" y1="279.2" x2="495.7" y2="312.3" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="284.2" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="499.4" y1="281.2" x2="499.4" y2="319.3" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="281.7" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="503.2" y1="280.0" x2="503.2" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="502.02" y="291.7" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="507.0" y1="263.6" x2="507.0" y2="306.7" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="299.1" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="510.7" y1="277.5" x2="510.7" y2="314.9" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="294.3" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="514.5" y1="278.8" x2="514.5" y2="300.6" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="280.6" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="518.3" y1="239.3" x2="518.3" y2="298.2" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="283.1" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="522.1" y1="281.5" x2="522.1" y2="319.3" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="287.5" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="525.8" y1="298.5" x2="525.8" y2="318.0" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="300.4" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="529.6" y1="294.6" x2="529.6" y2="322.8" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="295.9" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="533.4" y1="264.3" x2="533.4" y2="301.2" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="271.9" width="2.34" height="26.5" fill="var(--up)"/>
<line x1="537.1" y1="247.8" x2="537.1" y2="302.7" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="275.1" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="540.9" y1="268.2" x2="540.9" y2="312.7" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="295.9" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="544.7" y1="277.5" x2="544.7" y2="309.4" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="282.5" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="548.5" y1="283.8" x2="548.5" y2="331.4" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="283.8" width="2.34" height="37.2" fill="var(--down)"/>
<line x1="552.2" y1="312.9" x2="552.2" y2="342.5" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="322.1" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="556.0" y1="308.2" x2="556.0" y2="330.9" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="320.5" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="559.8" y1="253.0" x2="559.8" y2="302.9" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="263.8" width="2.34" height="38.3" fill="var(--up)"/>
<line x1="563.5" y1="234.6" x2="563.5" y2="265.4" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="240.8" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="567.3" y1="231.4" x2="567.3" y2="294.2" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="236.5" width="2.34" height="49.5" fill="var(--down)"/>
<line x1="571.1" y1="273.8" x2="571.1" y2="300.0" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="285.9" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="574.9" y1="246.5" x2="574.9" y2="310.0" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="247.6" width="2.34" height="37.9" fill="var(--up)"/>
<line x1="578.6" y1="197.5" x2="578.6" y2="297.5" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="236.4" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="582.4" y1="229.4" x2="582.4" y2="251.2" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="232.0" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="586.2" y1="201.1" x2="586.2" y2="239.9" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="204.0" width="2.34" height="23.3" fill="var(--up)"/>
<line x1="589.9" y1="176.1" x2="589.9" y2="213.1" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="185.5" width="2.34" height="12.9" fill="var(--up)"/>
<line x1="593.7" y1="185.9" x2="593.7" y2="218.8" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="186.3" width="2.34" height="31.6" fill="var(--down)"/>
<line x1="597.5" y1="231.0" x2="597.5" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="231.4" width="2.34" height="25.7" fill="var(--down)"/>
<line x1="601.3" y1="245.5" x2="601.3" y2="273.6" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="258.4" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="605.0" y1="276.5" x2="605.0" y2="344.5" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="278.5" width="2.34" height="48.5" fill="var(--down)"/>
<line x1="608.8" y1="286.5" x2="608.8" y2="334.9" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="300.3" width="2.34" height="29.2" fill="var(--up)"/>
<line x1="612.6" y1="282.4" x2="612.6" y2="320.8" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="298.6" width="2.34" height="19.8" fill="var(--down)"/>
<line x1="616.3" y1="309.7" x2="616.3" y2="341.3" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="317.6" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="620.1" y1="294.6" x2="620.1" y2="371.6" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="307.3" width="2.34" height="25.6" fill="var(--up)"/>
<line x1="623.9" y1="258.8" x2="623.9" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="284.3" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="627.7" y1="252.5" x2="627.7" y2="318.3" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="258.2" width="2.34" height="26.9" fill="var(--up)"/>
<line x1="631.4" y1="202.7" x2="631.4" y2="272.8" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="217.4" width="2.34" height="44.3" fill="var(--up)"/>
<line x1="635.2" y1="195.3" x2="635.2" y2="280.8" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="206.0" width="2.34" height="54.9" fill="var(--down)"/>
<line x1="639.0" y1="245.9" x2="639.0" y2="277.7" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="259.2" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="642.8" y1="226.8" x2="642.8" y2="260.6" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="234.2" width="2.34" height="24.7" fill="var(--up)"/>
<line x1="646.5" y1="226.4" x2="646.5" y2="269.8" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="230.7" width="2.34" height="26.5" fill="var(--down)"/>
<line x1="650.3" y1="204.4" x2="650.3" y2="264.9" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="222.8" width="2.34" height="38.2" fill="var(--up)"/>
<line x1="654.1" y1="209.3" x2="654.1" y2="249.0" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="222.7" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="657.8" y1="206.7" x2="657.8" y2="277.7" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="210.1" width="2.34" height="60.2" fill="var(--down)"/>
<line x1="661.6" y1="249.0" x2="661.6" y2="289.5" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="272.7" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="665.4" y1="264.4" x2="665.4" y2="303.9" stroke="var(--down)" class="wick"/>
<rect x="664.21" y="274.9" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="669.2" y1="239.5" x2="669.2" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="242.3" width="2.34" height="54.6" fill="var(--up)"/>
<line x1="672.9" y1="222.5" x2="672.9" y2="263.0" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="240.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="676.7" y1="221.6" x2="676.7" y2="267.1" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="245.0" width="2.34" height="20.6" fill="var(--down)"/>
<line x1="680.5" y1="256.4" x2="680.5" y2="316.3" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="256.4" width="2.34" height="56.9" fill="var(--down)"/>
<line x1="684.2" y1="295.1" x2="684.2" y2="329.7" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="313.3" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="688.0" y1="303.3" x2="688.0" y2="371.4" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="322.4" width="2.34" height="44.6" fill="var(--down)"/>
<line x1="691.8" y1="340.5" x2="691.8" y2="388.4" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="341.0" width="2.34" height="19.9" fill="var(--up)"/>
<line x1="695.6" y1="316.9" x2="695.6" y2="349.1" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="329.8" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="699.3" y1="328.3" x2="699.3" y2="374.2" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="330.8" width="2.34" height="42.6" fill="var(--down)"/>
<line x1="703.1" y1="344.9" x2="703.1" y2="385.2" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="372.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="706.9" y1="365.5" x2="706.9" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="373.0" width="2.34" height="39.0" fill="var(--down)"/>
<line x1="710.6" y1="406.7" x2="710.6" y2="435.7" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="411.2" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="714.4" y1="405.2" x2="714.4" y2="436.8" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="412.9" width="2.34" height="23.2" fill="var(--down)"/>
<line x1="718.2" y1="433.8" x2="718.2" y2="498.8" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="436.5" width="2.34" height="53.6" fill="var(--down)"/>
<line x1="722.0" y1="444.1" x2="722.0" y2="494.0" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="446.9" width="2.34" height="42.1" fill="var(--up)"/>
<line x1="725.7" y1="435.1" x2="725.7" y2="459.5" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="440.2" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="729.5" y1="391.3" x2="729.5" y2="432.5" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="426.3" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="733.3" y1="424.7" x2="733.3" y2="489.7" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="435.3" width="2.34" height="39.9" fill="var(--down)"/>
<line x1="737.0" y1="462.9" x2="737.0" y2="487.3" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="477.0" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="740.8" y1="398.4" x2="740.8" y2="498.1" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="406.5" width="2.34" height="81.6" fill="var(--up)"/>
<line x1="744.6" y1="368.3" x2="744.6" y2="434.0" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="406.7" width="2.34" height="8.7" fill="var(--up)"/>
<line x1="748.4" y1="355.3" x2="748.4" y2="429.6" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="399.2" width="2.34" height="23.8" fill="var(--up)"/>
<line x1="752.1" y1="355.8" x2="752.1" y2="460.3" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="388.1" width="2.34" height="56.2" fill="var(--down)"/>
<line x1="755.9" y1="420.6" x2="755.9" y2="473.9" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="439.4" width="2.34" height="29.1" fill="var(--down)"/>
<line x1="759.7" y1="422.8" x2="759.7" y2="473.3" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="439.1" width="2.34" height="29.1" fill="var(--up)"/>
<line x1="763.5" y1="395.5" x2="763.5" y2="460.9" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="431.9" width="2.34" height="27.7" fill="var(--down)"/>
<line x1="767.2" y1="455.5" x2="767.2" y2="523.3" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="476.3" width="2.34" height="24.0" fill="var(--up)"/>
<line x1="771.0" y1="455.2" x2="771.0" y2="512.2" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="478.4" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="774.8" y1="477.5" x2="774.8" y2="573.6" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="491.2" width="2.34" height="70.2" fill="var(--down)"/>
<line x1="778.5" y1="539.9" x2="778.5" y2="575.8" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="557.4" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="782.3" y1="556.4" x2="782.3" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="556.4" width="2.34" height="27.7" fill="var(--down)"/>
<line x1="786.1" y1="569.5" x2="786.1" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="572.2" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="789.9" y1="570.1" x2="789.9" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="571.1" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="793.6" y1="566.5" x2="793.6" y2="594.2" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="576.3" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="797.4" y1="566.4" x2="797.4" y2="594.6" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="580.6" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="801.2" y1="563.9" x2="801.2" y2="593.8" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="580.9" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="804.9" y1="571.4" x2="804.9" y2="598.3" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="577.4" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="808.7" y1="577.2" x2="808.7" y2="606.0" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="579.5" width="2.34" height="13.5" fill="var(--up)"/>
<line x1="812.5" y1="533.6" x2="812.5" y2="582.9" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="546.0" width="2.34" height="32.2" fill="var(--up)"/>
<line x1="816.3" y1="536.0" x2="816.3" y2="564.7" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="544.9" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="820.0" y1="461.5" x2="820.0" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="485.5" width="2.34" height="65.4" fill="var(--up)"/>
<line x1="823.8" y1="456.3" x2="823.8" y2="506.9" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="483.9" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="827.6" y1="476.6" x2="827.6" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="489.7" width="2.34" height="26.3" fill="var(--down)"/>
<line x1="831.3" y1="469.1" x2="831.3" y2="520.1" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="470.3" width="2.34" height="45.6" fill="var(--up)"/>
<line x1="835.1" y1="425.0" x2="835.1" y2="481.6" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="430.4" width="2.34" height="39.1" fill="var(--up)"/>
<line x1="838.9" y1="397.9" x2="838.9" y2="444.2" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="429.2" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="842.7" y1="439.4" x2="842.7" y2="465.7" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="443.8" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="846.4" y1="373.4" x2="846.4" y2="469.8" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="376.1" width="2.34" height="85.1" fill="var(--down)"/>
<line x1="850.2" y1="466.4" x2="850.2" y2="507.8" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="466.4" width="2.34" height="16.9" fill="var(--down)"/>
<line x1="854.0" y1="483.3" x2="854.0" y2="511.2" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="484.3" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="857.7" y1="484.1" x2="857.7" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="502.1" width="2.34" height="4.9" fill="var(--down)"/>
<line x1="861.5" y1="484.5" x2="861.5" y2="517.2" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="495.2" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="865.3" y1="427.1" x2="865.3" y2="521.3" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="432.8" width="2.34" height="64.0" fill="var(--up)"/>
<line x1="869.1" y1="399.7" x2="869.1" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="404.9" width="2.34" height="39.0" fill="var(--up)"/>
<line x1="872.8" y1="393.5" x2="872.8" y2="425.5" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="399.4" width="2.34" height="22.1" fill="var(--down)"/>
<line x1="876.6" y1="408.7" x2="876.6" y2="482.2" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="425.7" width="2.34" height="37.9" fill="var(--down)"/>
<line x1="880.4" y1="464.9" x2="880.4" y2="500.4" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="465.3" width="2.34" height="22.4" fill="var(--down)"/>
<line x1="884.2" y1="457.8" x2="884.2" y2="500.8" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="465.4" width="2.34" height="25.9" fill="var(--up)"/>
<line x1="887.9" y1="434.7" x2="887.9" y2="472.7" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="461.7" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="891.7" y1="442.5" x2="891.7" y2="473.8" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="443.1" width="2.34" height="22.4" fill="var(--up)"/>
<line x1="895.5" y1="428.0" x2="895.5" y2="475.7" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="444.0" width="2.34" height="27.8" fill="var(--down)"/>
<line x1="899.2" y1="426.6" x2="899.2" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="428.4" width="2.34" height="43.4" fill="var(--up)"/>
<line x1="903.0" y1="415.3" x2="903.0" y2="449.6" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="426.2" width="2.34" height="21.4" fill="var(--down)"/>
<line x1="906.8" y1="441.3" x2="906.8" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="452.5" width="2.34" height="28.9" fill="var(--down)"/>
<line x1="910.6" y1="469.9" x2="910.6" y2="494.3" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="481.7" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="914.3" y1="496.5" x2="914.3" y2="541.2" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="497.7" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="918.1" y1="452.3" x2="918.1" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="461.8" width="2.34" height="49.4" fill="var(--up)"/>
<line x1="921.9" y1="448.8" x2="921.9" y2="486.9" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="462.5" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="925.6" y1="403.5" x2="925.6" y2="478.6" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="405.5" width="2.34" height="68.0" fill="var(--up)"/>
<line x1="929.4" y1="273.6" x2="929.4" y2="408.9" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="275.6" width="2.34" height="126.6" fill="var(--up)"/>
<line x1="933.2" y1="268.0" x2="933.2" y2="327.6" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="283.2" width="2.34" height="27.4" fill="var(--down)"/>
<line x1="937.0" y1="298.3" x2="937.0" y2="351.6" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="309.3" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="940.7" y1="277.2" x2="940.7" y2="323.7" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="281.4" width="2.34" height="40.4" fill="var(--up)"/>
<line x1="944.5" y1="282.9" x2="944.5" y2="386.5" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="286.7" width="2.34" height="74.1" fill="var(--down)"/>
<line x1="948.3" y1="334.4" x2="948.3" y2="372.7" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="357.3" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="952.0" y1="344.2" x2="952.0" y2="438.5" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="345.9" width="2.34" height="87.2" fill="var(--down)"/>
<line x1="955.8" y1="398.5" x2="955.8" y2="440.9" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="410.0" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="959.6" y1="368.8" x2="959.6" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="379.4" width="2.34" height="24.6" fill="var(--up)"/>
<line x1="963.4" y1="371.7" x2="963.4" y2="420.0" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="379.1" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="967.1" y1="356.2" x2="967.1" y2="407.7" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="374.4" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="970.9" y1="365.3" x2="970.9" y2="406.1" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="366.1" width="2.34" height="25.4" fill="var(--down)"/>
<line x1="974.7" y1="356.4" x2="974.7" y2="406.6" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="376.4" width="2.34" height="14.5" fill="var(--up)"/>
<line x1="978.4" y1="376.8" x2="978.4" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="388.0" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="982.2" y1="397.2" x2="982.2" y2="447.7" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="399.6" width="2.34" height="40.6" fill="var(--down)"/>
<line x1="986.0" y1="413.6" x2="986.0" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="429.0" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="989.8" y1="431.5" x2="989.8" y2="483.1" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="435.7" width="2.34" height="42.5" fill="var(--down)"/>
<line x1="993.5" y1="466.6" x2="993.5" y2="504.2" stroke="var(--down)" class="wick"/>
<rect x="992.37" y="490.5" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="997.3" y1="468.5" x2="997.3" y2="516.2" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="477.6" width="2.34" height="25.8" fill="var(--up)"/>
<line x1="1001.1" y1="451.6" x2="1001.1" y2="503.9" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="487.2" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="1004.9" y1="481.7" x2="1004.9" y2="515.3" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="499.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1008.6" y1="473.9" x2="1008.6" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="478.0" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="1012.4" y1="440.8" x2="1012.4" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="477.8" width="2.34" height="52.8" fill="var(--down)"/>
<line x1="1016.2" y1="495.4" x2="1016.2" y2="551.7" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="525.7" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="1019.9" y1="529.0" x2="1019.9" y2="558.8" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="529.2" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="1023.7" y1="468.6" x2="1023.7" y2="533.5" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="513.8" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="1027.5" y1="498.5" x2="1027.5" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="502.1" width="2.34" height="15.9" fill="var(--down)"/>
<line x1="1031.3" y1="500.7" x2="1031.3" y2="535.6" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="504.4" width="2.34" height="17.5" fill="var(--up)"/>
<line x1="1035.0" y1="482.5" x2="1035.0" y2="528.5" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="483.7" width="2.34" height="29.0" fill="var(--up)"/>
<line x1="1038.8" y1="465.0" x2="1038.8" y2="512.9" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="472.6" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="1042.6" y1="497.3" x2="1042.6" y2="530.3" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="502.4" width="2.34" height="26.3" fill="var(--down)"/>
<line x1="1046.3" y1="518.3" x2="1046.3" y2="538.7" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="533.6" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="1050.1" y1="527.5" x2="1050.1" y2="537.6" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="530.7" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="60" y1="428.1" x2="1052" y2="428.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="431.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$151 R1</text>
<text x="1058" y="443.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="374.0" x2="1052" y2="374.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="377.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$158 R2</text>
<text x="1058" y="389.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="233.9" x2="1052" y2="233.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="237.4" font-size="11.5" fill="var(--resistance)" font-weight="600">$176 R3</text>
<text x="1058" y="249.4" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="550.0" x2="1052" y2="550.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="544.0" font-size="11.5" fill="var(--support)" font-weight="600">$135 S1</text>
<text x="1058" y="556.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="605.4" x2="1052" y2="605.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="599.4" font-size="11.5" fill="var(--support)" font-weight="600">$128 S2</text>
<text x="1058" y="611.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="536.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="528.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $137 (2026-09-10)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). **기술적 분석 — 일봉·1년의 레벨(전후 5거래일)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다** — 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $176 | 7 | 2022-01·2022-04·2023-02·2024-01·2024-02·2024-10·2026-02 — **5년 구간에서 가장 많이 닿은 레벨**(터치 7회). 2022~2024년의 거래 상단이자 2026-02 반등의 꼭대기다 |
| R2 | $158 | 3 | 2025-03-03·2025-09-01·2025-10-20 — 2025년의 반등 고점대 |
| R1 | $151 | 2 | 2025-12-15·2026-07-06 — 하락 추세 안에서의 최근 반등 상단 |
| **현재가** | **$136.65** (2026-09-10 종가) | — | R1과 S1 사이 |
| S1 | $135 | 2 | 2026-01-05·2026-07-20 — 2026년에 두 번 닿은 하단. 현재가에 가장 근접한 지지 |
| S2 | $128 | 2 | 2025-05-19·2025-06-23 — 2025년 중반의 저점대 |
| 참고선 | $196.88 | — | 5년 최고(2023년). 현재가에서 44% 위라 **근시일 저항으로 보지 않는다** |

> **레벨 구조 자체가 하락 추세를 보여준다** — 저항이 $176 → $158 → $151로 계단식으로 낮아졌고, 각 반등이 앞선 반등보다 낮은 곳에서 막혔다. 현재가는 S1($135) 바로 위이며, 그 아래 다음 지지는 $128로 **5.7% 아래**다.

---

## 3. 관측된 특이 구간 — 2026-02-02 주 FY2025 실적발표 이후의 되돌림

- 일봉 문서가 다루는 2026-07-09 하락은 이 흐름의 한 지점일 뿐이고, 주봉에서 보면 **2026-02 반등과 그 이후 7개월의 되돌림이 하나의 구간**이다.
- FY2025 실적·배당 인상·$100억 자사주 프로그램이 발표된 주(2026-02-02)에 주가는 전주 대비 **+11.0%**($153.63 → $170.49) 급등했고, 다음 주 $171.48로 최근 1년 최고를 찍었다. **손상차손 $1,860M으로 GAAP EPS가 −13.7% 꺾인 분기였는데도 시장은 구조조정 기대에 반응했다**([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 그 뒤 7개월 동안 $171 → $137로 되밀렸다. 위 §2의 R3($176) 클러스터에 2026-02가 포함된 것은 이 반등이 **2022~2024년의 거래 상단까지 닿았다가 실패했다**는 뜻이다. **즉 Elliott 개입으로 생긴 기대가 가격에 한 번 반영됐다가 실적으로 확인되지 않아 되돌려진 구간**이며, 앞으로 $151·$158을 넘으려면 기대가 아니라 [핵심 지표 C절](./04_metrics.md)의 코어 영업이익률이 답을 줘야 한다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-06~2026-09-10. 수집 시점: 2026-09-11. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py PEP --name "펩시코" --interval 1wk --close-on 2026-09-10 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **5년 구간 안에 사업 구조가 두 번 바뀌었다** — 2021년 Tropicana 등 주스 사업 매각, FY2025부터 FLNA·QFNA를 PFNA로 통합한 부문 재편이다. 매출 계보가 끊긴 구간이 있으므로 2022년 이전 레벨($176)을 현재 펀더멘털과 직접 연결해 읽지 말 것.
    - 기간 내 **주식분할은 없었다**(마지막 분할 1996년). 이 차트는 **원주가**라 5년간의 배당(누적 약 $26)이 반영돼 있지 않다 — 주가는 5년 전 대비 하락했지만 배당을 포함한 총수익률은 그보다 낫다.

---

*작성일: 2026-09-11*
