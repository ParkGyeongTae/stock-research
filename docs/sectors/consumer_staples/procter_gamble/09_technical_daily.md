# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-08-27 종가 $143.14는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치**한다. 다만 같은 스크립트의 주봉 산출물은 한 거래일 뒤인 **2026-08-28 종가 $143.78**을 최신으로 잡는다 — 일봉 원자료에 2026-08-28이 아직 들어오지 않은 탓이며, 이 저장소의 회사 문서는 모두 일봉 기준(2026-08-27 $143.14)으로 통일했다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

<div class="pg-chart">
<style>
.pg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .pg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .pg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.pg-chart svg { width:100%; height:auto; display:block; }
.pg-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.pg-chart .title { fill: var(--ink); font-weight:600; }
.pg-chart .grid { stroke: var(--grid); stroke-width:1; }
.pg-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="프록터 앤 갬블(PG) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">프록터 앤 갬블 (PG) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $143.14 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="563.7" x2="1052" y2="563.7" class="grid"/>
<text x="52" y="567.7" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
<line x1="60" y1="474.6" x2="1052" y2="474.6" class="grid"/>
<text x="52" y="478.6" font-size="11" text-anchor="end" fill="var(--muted)">145</text>
<line x1="60" y1="385.5" x2="1052" y2="385.5" class="grid"/>
<text x="52" y="389.5" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="296.5" x2="1052" y2="296.5" class="grid"/>
<text x="52" y="300.5" font-size="11" text-anchor="end" fill="var(--muted)">155</text>
<line x1="60" y1="207.4" x2="1052" y2="207.4" class="grid"/>
<text x="52" y="211.4" font-size="11" text-anchor="end" fill="var(--muted)">160</text>
<line x1="60" y1="118.3" x2="1052" y2="118.3" class="grid"/>
<text x="52" y="122.3" font-size="11" text-anchor="end" fill="var(--muted)">165</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="66.0" y1="626.0" x2="66.0" y2="631.0" class="axis"/>
<text x="66.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="149.3" y1="626.0" x2="149.3" y2="631.0" class="axis"/>
<text x="149.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="240.5" y1="626.0" x2="240.5" y2="631.0" class="axis"/>
<text x="240.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="315.9" y1="626.0" x2="315.9" y2="631.0" class="axis"/>
<text x="315.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="403.2" y1="626.0" x2="403.2" y2="631.0" class="axis"/>
<text x="403.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="482.6" y1="626.0" x2="482.6" y2="631.0" class="axis"/>
<text x="482.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="558.0" y1="626.0" x2="558.0" y2="631.0" class="axis"/>
<text x="558.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="645.3" y1="626.0" x2="645.3" y2="631.0" class="axis"/>
<text x="645.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="728.6" y1="626.0" x2="728.6" y2="631.0" class="axis"/>
<text x="728.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="808.0" y1="626.0" x2="808.0" y2="631.0" class="axis"/>
<text x="808.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="891.3" y1="626.0" x2="891.3" y2="631.0" class="axis"/>
<text x="891.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="978.6" y1="626.0" x2="978.6" y2="631.0" class="axis"/>
<text x="978.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.0" y1="250.9" x2="62.0" y2="284.9" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="260.1" width="2.46" height="16.9" fill="var(--up)"/>
<line x1="66.0" y1="227.7" x2="66.0" y2="261.2" stroke="var(--up)" class="wick"/>
<rect x="64.72" y="243.2" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="69.9" y1="231.6" x2="69.9" y2="269.8" stroke="var(--up)" class="wick"/>
<rect x="68.69" y="240.0" width="2.46" height="9.3" fill="var(--up)"/>
<line x1="73.9" y1="211.9" x2="73.9" y2="246.4" stroke="var(--up)" class="wick"/>
<rect x="72.66" y="221.8" width="2.46" height="11.9" fill="var(--up)"/>
<line x1="77.9" y1="197.4" x2="77.9" y2="235.7" stroke="var(--up)" class="wick"/>
<rect x="76.63" y="207.0" width="2.46" height="26.2" fill="var(--up)"/>
<line x1="81.8" y1="202.6" x2="81.8" y2="238.6" stroke="var(--down)" class="wick"/>
<rect x="80.59" y="214.4" width="2.46" height="10.7" fill="var(--down)"/>
<line x1="85.8" y1="209.7" x2="85.8" y2="239.5" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="217.0" width="2.46" height="15.1" fill="var(--up)"/>
<line x1="89.8" y1="226.3" x2="89.8" y2="280.6" stroke="var(--down)" class="wick"/>
<rect x="88.53" y="232.3" width="2.46" height="22.3" fill="var(--down)"/>
<line x1="93.7" y1="219.0" x2="93.7" y2="253.9" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="231.8" width="2.46" height="16.2" fill="var(--up)"/>
<line x1="97.7" y1="222.9" x2="97.7" y2="247.0" stroke="var(--down)" class="wick"/>
<rect x="96.47" y="244.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="101.7" y1="233.8" x2="101.7" y2="275.1" stroke="var(--down)" class="wick"/>
<rect x="100.43" y="245.2" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="105.6" y1="236.1" x2="105.6" y2="262.8" stroke="var(--up)" class="wick"/>
<rect x="104.40" y="242.1" width="2.46" height="16.2" fill="var(--up)"/>
<line x1="109.6" y1="177.7" x2="109.6" y2="235.4" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="201.5" width="2.46" height="33.8" fill="var(--up)"/>
<line x1="113.6" y1="224.9" x2="113.6" y2="258.0" stroke="var(--down)" class="wick"/>
<rect x="112.34" y="240.4" width="2.46" height="14.8" fill="var(--down)"/>
<line x1="117.5" y1="249.8" x2="117.5" y2="279.2" stroke="var(--down)" class="wick"/>
<rect x="116.31" y="250.0" width="2.46" height="28.0" fill="var(--down)"/>
<line x1="121.5" y1="277.2" x2="121.5" y2="331.2" stroke="var(--down)" class="wick"/>
<rect x="120.27" y="277.2" width="2.46" height="53.6" fill="var(--down)"/>
<line x1="125.5" y1="326.9" x2="125.5" y2="368.3" stroke="var(--down)" class="wick"/>
<rect x="124.24" y="328.5" width="2.46" height="12.5" fill="var(--down)"/>
<line x1="129.4" y1="320.9" x2="129.4" y2="353.6" stroke="var(--up)" class="wick"/>
<rect x="128.21" y="342.4" width="2.46" height="6.6" fill="var(--up)"/>
<line x1="133.4" y1="316.4" x2="133.4" y2="353.8" stroke="var(--down)" class="wick"/>
<rect x="132.18" y="328.0" width="2.46" height="19.2" fill="var(--down)"/>
<line x1="137.4" y1="337.8" x2="137.4" y2="358.3" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="341.0" width="2.46" height="4.8" fill="var(--up)"/>
<line x1="141.3" y1="319.3" x2="141.3" y2="353.6" stroke="var(--up)" class="wick"/>
<rect x="140.11" y="322.7" width="2.46" height="19.8" fill="var(--up)"/>
<line x1="145.3" y1="307.5" x2="145.3" y2="334.9" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="320.5" width="2.46" height="3.4" fill="var(--up)"/>
<line x1="149.3" y1="316.2" x2="149.3" y2="360.4" stroke="var(--down)" class="wick"/>
<rect x="148.05" y="319.6" width="2.46" height="9.3" fill="var(--down)"/>
<line x1="153.2" y1="335.7" x2="153.2" y2="356.5" stroke="var(--down)" class="wick"/>
<rect x="152.02" y="337.1" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="157.2" y1="324.4" x2="157.2" y2="349.9" stroke="var(--up)" class="wick"/>
<rect x="155.99" y="345.1" width="2.46" height="4.8" fill="var(--up)"/>
<line x1="161.2" y1="344.2" x2="161.2" y2="378.4" stroke="var(--down)" class="wick"/>
<rect x="159.95" y="358.8" width="2.46" height="19.4" fill="var(--down)"/>
<line x1="165.2" y1="329.1" x2="165.2" y2="384.6" stroke="var(--up)" class="wick"/>
<rect x="163.92" y="340.3" width="2.46" height="31.7" fill="var(--up)"/>
<line x1="169.1" y1="335.8" x2="169.1" y2="374.3" stroke="var(--down)" class="wick"/>
<rect x="167.89" y="335.8" width="2.46" height="37.4" fill="var(--down)"/>
<line x1="173.1" y1="370.0" x2="173.1" y2="393.0" stroke="var(--down)" class="wick"/>
<rect x="171.86" y="372.3" width="2.46" height="2.9" fill="var(--down)"/>
<line x1="177.1" y1="358.6" x2="177.1" y2="395.3" stroke="var(--down)" class="wick"/>
<rect x="175.83" y="368.8" width="2.46" height="22.3" fill="var(--down)"/>
<line x1="181.0" y1="395.7" x2="181.0" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="179.79" y="403.3" width="2.46" height="26.9" fill="var(--down)"/>
<line x1="185.0" y1="398.9" x2="185.0" y2="437.5" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="400.5" width="2.46" height="28.3" fill="var(--up)"/>
<line x1="189.0" y1="396.0" x2="189.0" y2="434.2" stroke="var(--down)" class="wick"/>
<rect x="187.73" y="411.7" width="2.46" height="19.8" fill="var(--down)"/>
<line x1="192.9" y1="378.4" x2="192.9" y2="422.6" stroke="var(--up)" class="wick"/>
<rect x="191.70" y="392.7" width="2.46" height="28.3" fill="var(--up)"/>
<line x1="196.9" y1="349.4" x2="196.9" y2="377.9" stroke="var(--up)" class="wick"/>
<rect x="195.67" y="360.6" width="2.46" height="14.8" fill="var(--up)"/>
<line x1="200.9" y1="343.0" x2="200.9" y2="362.4" stroke="var(--up)" class="wick"/>
<rect x="199.63" y="350.6" width="2.46" height="6.6" fill="var(--up)"/>
<line x1="204.8" y1="344.9" x2="204.8" y2="370.0" stroke="var(--down)" class="wick"/>
<rect x="203.60" y="350.6" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="208.8" y1="323.9" x2="208.8" y2="371.5" stroke="var(--up)" class="wick"/>
<rect x="207.57" y="346.3" width="2.46" height="16.0" fill="var(--up)"/>
<line x1="212.8" y1="326.7" x2="212.8" y2="375.2" stroke="var(--down)" class="wick"/>
<rect x="211.54" y="343.7" width="2.46" height="2.5" fill="var(--down)"/>
<line x1="216.7" y1="253.7" x2="216.7" y2="358.3" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="271.5" width="2.46" height="69.6" fill="var(--down)"/>
<line x1="220.7" y1="354.2" x2="220.7" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="219.47" y="354.5" width="2.46" height="2.3" fill="var(--up)"/>
<line x1="224.7" y1="329.1" x2="224.7" y2="374.5" stroke="var(--up)" class="wick"/>
<rect x="223.44" y="361.1" width="2.46" height="4.5" fill="var(--up)"/>
<line x1="228.6" y1="368.3" x2="228.6" y2="412.8" stroke="var(--down)" class="wick"/>
<rect x="227.41" y="373.8" width="2.46" height="33.7" fill="var(--down)"/>
<line x1="232.6" y1="371.3" x2="232.6" y2="397.3" stroke="var(--up)" class="wick"/>
<rect x="231.38" y="393.0" width="2.46" height="2.0" fill="var(--up)"/>
<line x1="236.6" y1="365.9" x2="236.6" y2="411.7" stroke="var(--up)" class="wick"/>
<rect x="235.35" y="378.9" width="2.46" height="29.6" fill="var(--up)"/>
<line x1="240.5" y1="381.6" x2="240.5" y2="425.3" stroke="var(--down)" class="wick"/>
<rect x="239.31" y="383.7" width="2.46" height="37.1" fill="var(--down)"/>
<line x1="244.5" y1="394.4" x2="244.5" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="243.28" y="410.5" width="2.46" height="25.5" fill="var(--down)"/>
<line x1="248.5" y1="431.5" x2="248.5" y2="463.0" stroke="var(--down)" class="wick"/>
<rect x="247.25" y="441.3" width="2.46" height="19.2" fill="var(--down)"/>
<line x1="252.4" y1="444.7" x2="252.4" y2="484.2" stroke="var(--up)" class="wick"/>
<rect x="251.22" y="454.5" width="2.46" height="4.5" fill="var(--up)"/>
<line x1="256.4" y1="422.2" x2="256.4" y2="456.8" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="439.3" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="260.4" y1="445.7" x2="260.4" y2="490.8" stroke="var(--down)" class="wick"/>
<rect x="259.15" y="450.0" width="2.46" height="15.7" fill="var(--down)"/>
<line x1="264.4" y1="409.6" x2="264.4" y2="462.7" stroke="var(--up)" class="wick"/>
<rect x="263.12" y="411.5" width="2.46" height="46.0" fill="var(--up)"/>
<line x1="268.3" y1="400.7" x2="268.3" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="267.09" y="411.7" width="2.46" height="9.3" fill="var(--down)"/>
<line x1="272.3" y1="403.3" x2="272.3" y2="427.6" stroke="var(--down)" class="wick"/>
<rect x="271.06" y="418.0" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="276.3" y1="396.6" x2="276.3" y2="428.1" stroke="var(--down)" class="wick"/>
<rect x="275.03" y="401.6" width="2.46" height="25.5" fill="var(--down)"/>
<line x1="280.2" y1="421.5" x2="280.2" y2="474.4" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="425.6" width="2.46" height="34.4" fill="var(--down)"/>
<line x1="284.2" y1="432.0" x2="284.2" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="282.96" y="439.1" width="2.46" height="11.8" fill="var(--up)"/>
<line x1="288.2" y1="429.4" x2="288.2" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="286.93" y="439.1" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="292.1" y1="409.4" x2="292.1" y2="454.5" stroke="var(--up)" class="wick"/>
<rect x="290.90" y="417.8" width="2.46" height="27.6" fill="var(--up)"/>
<line x1="296.1" y1="358.8" x2="296.1" y2="415.8" stroke="var(--up)" class="wick"/>
<rect x="294.87" y="369.1" width="2.46" height="45.2" fill="var(--up)"/>
<line x1="300.1" y1="378.2" x2="300.1" y2="447.2" stroke="var(--down)" class="wick"/>
<rect x="298.83" y="383.7" width="2.46" height="55.6" fill="var(--down)"/>
<line x1="304.0" y1="409.6" x2="304.0" y2="435.0" stroke="var(--up)" class="wick"/>
<rect x="302.80" y="412.4" width="2.46" height="20.8" fill="var(--up)"/>
<line x1="308.0" y1="403.9" x2="308.0" y2="428.1" stroke="var(--up)" class="wick"/>
<rect x="306.77" y="416.7" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="312.0" y1="408.5" x2="312.0" y2="435.8" stroke="var(--up)" class="wick"/>
<rect x="310.74" y="418.3" width="2.46" height="6.4" fill="var(--up)"/>
<line x1="315.9" y1="405.3" x2="315.9" y2="432.7" stroke="var(--down)" class="wick"/>
<rect x="314.71" y="419.4" width="2.46" height="11.8" fill="var(--down)"/>
<line x1="319.9" y1="453.4" x2="319.9" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="318.67" y="459.3" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="323.9" y1="416.0" x2="323.9" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="444.1" width="2.46" height="14.1" fill="var(--up)"/>
<line x1="327.8" y1="431.5" x2="327.8" y2="483.5" stroke="var(--down)" class="wick"/>
<rect x="326.61" y="444.8" width="2.46" height="23.3" fill="var(--down)"/>
<line x1="331.8" y1="463.4" x2="331.8" y2="505.8" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="471.7" width="2.46" height="30.5" fill="var(--down)"/>
<line x1="335.8" y1="511.8" x2="335.8" y2="596.8" stroke="var(--down)" class="wick"/>
<rect x="334.55" y="511.8" width="2.46" height="81.4" fill="var(--down)"/>
<line x1="339.7" y1="548.0" x2="339.7" y2="581.5" stroke="var(--up)" class="wick"/>
<rect x="338.51" y="570.2" width="2.46" height="7.8" fill="var(--up)"/>
<line x1="343.7" y1="540.9" x2="343.7" y2="571.9" stroke="var(--up)" class="wick"/>
<rect x="342.48" y="566.9" width="2.46" height="3.0" fill="var(--up)"/>
<line x1="347.7" y1="530.9" x2="347.7" y2="557.2" stroke="var(--down)" class="wick"/>
<rect x="346.45" y="545.8" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="351.6" y1="508.3" x2="351.6" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="350.42" y="513.1" width="2.46" height="32.8" fill="var(--up)"/>
<line x1="355.6" y1="468.9" x2="355.6" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="354.39" y="472.3" width="2.46" height="33.1" fill="var(--up)"/>
<line x1="359.6" y1="447.2" x2="359.6" y2="480.8" stroke="var(--down)" class="wick"/>
<rect x="358.35" y="455.0" width="2.46" height="15.9" fill="var(--down)"/>
<line x1="363.6" y1="413.1" x2="363.6" y2="448.8" stroke="var(--up)" class="wick"/>
<rect x="362.32" y="424.5" width="2.46" height="19.9" fill="var(--up)"/>
<line x1="367.5" y1="430.1" x2="367.5" y2="468.4" stroke="var(--down)" class="wick"/>
<rect x="366.29" y="445.7" width="2.46" height="19.6" fill="var(--down)"/>
<line x1="371.5" y1="455.9" x2="371.5" y2="493.5" stroke="var(--down)" class="wick"/>
<rect x="370.26" y="465.5" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="375.5" y1="485.3" x2="375.5" y2="520.6" stroke="var(--down)" class="wick"/>
<rect x="374.23" y="497.6" width="2.46" height="18.2" fill="var(--down)"/>
<line x1="379.4" y1="497.2" x2="379.4" y2="526.6" stroke="var(--up)" class="wick"/>
<rect x="378.19" y="507.0" width="2.46" height="12.3" fill="var(--up)"/>
<line x1="383.4" y1="479.2" x2="383.4" y2="513.2" stroke="var(--up)" class="wick"/>
<rect x="382.16" y="483.7" width="2.46" height="28.3" fill="var(--up)"/>
<line x1="387.4" y1="463.2" x2="387.4" y2="486.9" stroke="var(--up)" class="wick"/>
<rect x="386.13" y="479.2" width="2.46" height="7.7" fill="var(--up)"/>
<line x1="391.3" y1="473.3" x2="391.3" y2="493.3" stroke="var(--down)" class="wick"/>
<rect x="390.10" y="478.2" width="2.46" height="4.1" fill="var(--down)"/>
<line x1="395.3" y1="484.2" x2="395.3" y2="500.1" stroke="var(--down)" class="wick"/>
<rect x="394.07" y="487.2" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="399.3" y1="489.9" x2="399.3" y2="506.1" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="492.4" width="2.46" height="12.3" fill="var(--down)"/>
<line x1="403.2" y1="504.2" x2="403.2" y2="541.6" stroke="var(--down)" class="wick"/>
<rect x="402.00" y="508.3" width="2.46" height="23.5" fill="var(--down)"/>
<line x1="407.2" y1="539.6" x2="407.2" y2="570.8" stroke="var(--down)" class="wick"/>
<rect x="405.97" y="544.1" width="2.46" height="13.0" fill="var(--down)"/>
<line x1="411.2" y1="538.4" x2="411.2" y2="572.4" stroke="var(--down)" class="wick"/>
<rect x="409.94" y="556.7" width="2.46" height="8.5" fill="var(--down)"/>
<line x1="415.1" y1="567.2" x2="415.1" y2="606.1" stroke="var(--down)" class="wick"/>
<rect x="413.91" y="567.2" width="2.46" height="31.4" fill="var(--down)"/>
<line x1="419.1" y1="532.0" x2="419.1" y2="602.5" stroke="var(--up)" class="wick"/>
<rect x="417.87" y="536.4" width="2.46" height="64.8" fill="var(--up)"/>
<line x1="423.1" y1="522.2" x2="423.1" y2="548.9" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="530.3" width="2.46" height="3.0" fill="var(--up)"/>
<line x1="427.0" y1="494.5" x2="427.0" y2="533.2" stroke="var(--up)" class="wick"/>
<rect x="425.81" y="502.0" width="2.46" height="21.0" fill="var(--up)"/>
<line x1="431.0" y1="486.4" x2="431.0" y2="510.8" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="488.1" width="2.46" height="4.3" fill="var(--up)"/>
<line x1="435.0" y1="440.8" x2="435.0" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="433.75" y="450.5" width="2.46" height="29.7" fill="var(--up)"/>
<line x1="438.9" y1="450.5" x2="438.9" y2="486.2" stroke="var(--down)" class="wick"/>
<rect x="437.71" y="462.5" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="442.9" y1="479.4" x2="442.9" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="441.68" y="483.0" width="2.46" height="13.7" fill="var(--up)"/>
<line x1="446.9" y1="439.0" x2="446.9" y2="490.3" stroke="var(--up)" class="wick"/>
<rect x="445.65" y="439.0" width="2.46" height="45.2" fill="var(--up)"/>
<line x1="450.8" y1="432.4" x2="450.8" y2="475.1" stroke="var(--down)" class="wick"/>
<rect x="449.62" y="437.9" width="2.46" height="17.8" fill="var(--down)"/>
<line x1="454.8" y1="369.3" x2="454.8" y2="430.1" stroke="var(--up)" class="wick"/>
<rect x="453.59" y="386.8" width="2.46" height="33.0" fill="var(--up)"/>
<line x1="458.8" y1="356.1" x2="458.8" y2="389.1" stroke="var(--down)" class="wick"/>
<rect x="457.55" y="370.6" width="2.46" height="12.3" fill="var(--down)"/>
<line x1="462.8" y1="369.9" x2="462.8" y2="411.9" stroke="var(--down)" class="wick"/>
<rect x="461.52" y="383.4" width="2.46" height="11.2" fill="var(--down)"/>
<line x1="466.7" y1="391.9" x2="466.7" y2="422.4" stroke="var(--up)" class="wick"/>
<rect x="465.49" y="415.1" width="2.46" height="4.8" fill="var(--up)"/>
<line x1="470.7" y1="408.5" x2="470.7" y2="442.7" stroke="var(--down)" class="wick"/>
<rect x="469.46" y="421.2" width="2.46" height="11.8" fill="var(--down)"/>
<line x1="474.7" y1="383.2" x2="474.7" y2="437.0" stroke="var(--up)" class="wick"/>
<rect x="473.43" y="387.3" width="2.46" height="46.5" fill="var(--up)"/>
<line x1="478.6" y1="350.4" x2="478.6" y2="400.7" stroke="var(--up)" class="wick"/>
<rect x="477.39" y="354.0" width="2.46" height="23.9" fill="var(--up)"/>
<line x1="482.6" y1="319.1" x2="482.6" y2="363.3" stroke="var(--up)" class="wick"/>
<rect x="481.36" y="328.7" width="2.46" height="13.7" fill="var(--up)"/>
<line x1="486.6" y1="269.2" x2="486.6" y2="346.3" stroke="var(--up)" class="wick"/>
<rect x="485.33" y="290.8" width="2.46" height="48.6" fill="var(--up)"/>
<line x1="490.5" y1="236.4" x2="490.5" y2="282.9" stroke="var(--up)" class="wick"/>
<rect x="489.30" y="263.2" width="2.46" height="13.2" fill="var(--up)"/>
<line x1="494.5" y1="213.6" x2="494.5" y2="276.5" stroke="var(--down)" class="wick"/>
<rect x="493.27" y="228.1" width="2.46" height="4.1" fill="var(--down)"/>
<line x1="498.5" y1="207.6" x2="498.5" y2="242.9" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="222.2" width="2.46" height="16.6" fill="var(--up)"/>
<line x1="502.4" y1="220.2" x2="502.4" y2="278.3" stroke="var(--down)" class="wick"/>
<rect x="501.20" y="229.5" width="2.46" height="25.5" fill="var(--down)"/>
<line x1="506.4" y1="204.7" x2="506.4" y2="265.8" stroke="var(--up)" class="wick"/>
<rect x="505.17" y="223.8" width="2.46" height="27.6" fill="var(--up)"/>
<line x1="510.4" y1="187.1" x2="510.4" y2="239.6" stroke="var(--up)" class="wick"/>
<rect x="509.14" y="207.4" width="2.46" height="24.2" fill="var(--up)"/>
<line x1="514.3" y1="151.5" x2="514.3" y2="213.6" stroke="var(--up)" class="wick"/>
<rect x="513.11" y="185.9" width="2.46" height="21.2" fill="var(--up)"/>
<line x1="518.3" y1="161.6" x2="518.3" y2="212.6" stroke="var(--down)" class="wick"/>
<rect x="517.07" y="176.4" width="2.46" height="29.7" fill="var(--down)"/>
<line x1="522.3" y1="168.8" x2="522.3" y2="227.4" stroke="var(--down)" class="wick"/>
<rect x="521.04" y="208.3" width="2.46" height="7.1" fill="var(--down)"/>
<line x1="526.2" y1="225.6" x2="526.2" y2="282.8" stroke="var(--down)" class="wick"/>
<rect x="525.01" y="225.6" width="2.46" height="37.8" fill="var(--down)"/>
<line x1="530.2" y1="208.1" x2="530.2" y2="263.9" stroke="var(--up)" class="wick"/>
<rect x="528.98" y="233.1" width="2.46" height="30.8" fill="var(--up)"/>
<line x1="534.2" y1="188.5" x2="534.2" y2="240.2" stroke="var(--up)" class="wick"/>
<rect x="532.95" y="193.5" width="2.46" height="29.4" fill="var(--up)"/>
<line x1="538.1" y1="111.9" x2="538.1" y2="202.1" stroke="var(--up)" class="wick"/>
<rect x="536.91" y="115.3" width="2.46" height="86.4" fill="var(--up)"/>
<line x1="542.1" y1="85.0" x2="542.1" y2="137.2" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="113.4" width="2.46" height="6.8" fill="var(--up)"/>
<line x1="546.1" y1="118.3" x2="546.1" y2="170.0" stroke="var(--down)" class="wick"/>
<rect x="544.85" y="126.5" width="2.46" height="20.5" fill="var(--down)"/>
<line x1="550.0" y1="127.2" x2="550.0" y2="156.5" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="132.2" width="2.46" height="8.4" fill="var(--down)"/>
<line x1="554.0" y1="78.3" x2="554.0" y2="141.7" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="79.2" width="2.46" height="56.3" fill="var(--up)"/>
<line x1="558.0" y1="90.7" x2="558.0" y2="146.0" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="113.2" width="2.46" height="31.7" fill="var(--down)"/>
<line x1="562.0" y1="168.4" x2="562.0" y2="232.0" stroke="var(--down)" class="wick"/>
<rect x="560.72" y="168.4" width="2.46" height="44.0" fill="var(--down)"/>
<line x1="565.9" y1="214.4" x2="565.9" y2="255.3" stroke="var(--down)" class="wick"/>
<rect x="564.69" y="217.4" width="2.46" height="20.3" fill="var(--down)"/>
<line x1="569.9" y1="259.1" x2="569.9" y2="318.4" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="261.9" width="2.46" height="52.5" fill="var(--down)"/>
<line x1="573.9" y1="306.6" x2="573.9" y2="351.9" stroke="var(--down)" class="wick"/>
<rect x="572.63" y="320.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="577.8" y1="274.6" x2="577.8" y2="333.9" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="292.5" width="2.46" height="36.9" fill="var(--up)"/>
<line x1="581.8" y1="258.2" x2="581.8" y2="321.4" stroke="var(--up)" class="wick"/>
<rect x="580.56" y="278.5" width="2.46" height="9.3" fill="var(--up)"/>
<line x1="585.8" y1="289.7" x2="585.8" y2="360.1" stroke="var(--down)" class="wick"/>
<rect x="584.53" y="292.4" width="2.46" height="34.0" fill="var(--down)"/>
<line x1="589.7" y1="331.2" x2="589.7" y2="379.7" stroke="var(--down)" class="wick"/>
<rect x="588.50" y="346.2" width="2.46" height="30.5" fill="var(--down)"/>
<line x1="593.7" y1="340.1" x2="593.7" y2="382.3" stroke="var(--down)" class="wick"/>
<rect x="592.47" y="361.1" width="2.46" height="12.8" fill="var(--down)"/>
<line x1="597.7" y1="338.5" x2="597.7" y2="374.0" stroke="var(--up)" class="wick"/>
<rect x="596.43" y="347.8" width="2.46" height="4.6" fill="var(--up)"/>
<line x1="601.6" y1="323.9" x2="601.6" y2="364.2" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="331.9" width="2.46" height="27.3" fill="var(--down)"/>
<line x1="605.6" y1="392.3" x2="605.6" y2="448.6" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="397.8" width="2.46" height="46.3" fill="var(--down)"/>
<line x1="609.6" y1="432.2" x2="609.6" y2="478.3" stroke="var(--down)" class="wick"/>
<rect x="608.34" y="452.9" width="2.46" height="24.6" fill="var(--down)"/>
<line x1="613.5" y1="460.0" x2="613.5" y2="488.0" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="474.8" width="2.46" height="12.6" fill="var(--down)"/>
<line x1="617.5" y1="454.1" x2="617.5" y2="501.7" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="454.1" width="2.46" height="38.5" fill="var(--down)"/>
<line x1="621.5" y1="470.5" x2="621.5" y2="523.9" stroke="var(--down)" class="wick"/>
<rect x="620.24" y="504.3" width="2.46" height="3.0" fill="var(--down)"/>
<line x1="625.4" y1="490.6" x2="625.4" y2="523.9" stroke="var(--up)" class="wick"/>
<rect x="624.21" y="493.8" width="2.46" height="3.2" fill="var(--up)"/>
<line x1="629.4" y1="482.3" x2="629.4" y2="523.8" stroke="var(--down)" class="wick"/>
<rect x="628.18" y="497.9" width="2.46" height="22.6" fill="var(--down)"/>
<line x1="633.4" y1="491.0" x2="633.4" y2="527.9" stroke="var(--down)" class="wick"/>
<rect x="632.15" y="515.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="637.3" y1="464.4" x2="637.3" y2="517.9" stroke="var(--up)" class="wick"/>
<rect x="636.11" y="479.6" width="2.46" height="29.9" fill="var(--up)"/>
<line x1="641.3" y1="476.0" x2="641.3" y2="523.0" stroke="var(--down)" class="wick"/>
<rect x="640.08" y="477.8" width="2.46" height="6.8" fill="var(--down)"/>
<line x1="645.3" y1="475.1" x2="645.3" y2="506.5" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="490.8" width="2.46" height="3.0" fill="var(--up)"/>
<line x1="649.2" y1="488.7" x2="649.2" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="648.02" y="490.8" width="2.46" height="17.3" fill="var(--down)"/>
<line x1="653.2" y1="498.3" x2="653.2" y2="529.5" stroke="var(--down)" class="wick"/>
<rect x="651.99" y="510.0" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="657.2" y1="514.3" x2="657.2" y2="550.5" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="518.8" width="2.46" height="21.7" fill="var(--down)"/>
<line x1="661.2" y1="472.6" x2="661.2" y2="530.3" stroke="var(--up)" class="wick"/>
<rect x="659.92" y="476.4" width="2.46" height="31.2" fill="var(--up)"/>
<line x1="665.1" y1="440.0" x2="665.1" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="663.89" y="445.0" width="2.46" height="40.4" fill="var(--up)"/>
<line x1="669.1" y1="440.9" x2="669.1" y2="478.9" stroke="var(--down)" class="wick"/>
<rect x="667.86" y="440.9" width="2.46" height="30.8" fill="var(--down)"/>
<line x1="673.1" y1="473.0" x2="673.1" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="671.83" y="474.6" width="2.46" height="25.3" fill="var(--down)"/>
<line x1="677.0" y1="479.6" x2="677.0" y2="514.3" stroke="var(--up)" class="wick"/>
<rect x="675.79" y="485.6" width="2.46" height="20.3" fill="var(--up)"/>
<line x1="681.0" y1="485.3" x2="681.0" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="679.76" y="486.0" width="2.46" height="17.5" fill="var(--down)"/>
<line x1="685.0" y1="487.2" x2="685.0" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="683.73" y="506.7" width="2.46" height="1.6" fill="var(--down)"/>
<line x1="688.9" y1="428.5" x2="688.9" y2="507.4" stroke="var(--up)" class="wick"/>
<rect x="687.70" y="440.2" width="2.46" height="62.7" fill="var(--up)"/>
<line x1="692.9" y1="445.0" x2="692.9" y2="499.7" stroke="var(--down)" class="wick"/>
<rect x="691.67" y="455.7" width="2.46" height="28.0" fill="var(--down)"/>
<line x1="696.9" y1="481.4" x2="696.9" y2="522.3" stroke="var(--down)" class="wick"/>
<rect x="695.63" y="481.4" width="2.46" height="41.0" fill="var(--down)"/>
<line x1="700.8" y1="504.9" x2="700.8" y2="524.1" stroke="var(--up)" class="wick"/>
<rect x="699.60" y="512.9" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="704.8" y1="452.7" x2="704.8" y2="503.1" stroke="var(--up)" class="wick"/>
<rect x="703.57" y="461.9" width="2.46" height="41.1" fill="var(--up)"/>
<line x1="708.8" y1="342.4" x2="708.8" y2="427.9" stroke="var(--down)" class="wick"/>
<rect x="707.54" y="349.7" width="2.46" height="68.2" fill="var(--down)"/>
<line x1="712.7" y1="390.9" x2="712.7" y2="431.5" stroke="var(--up)" class="wick"/>
<rect x="711.51" y="414.0" width="2.46" height="17.5" fill="var(--up)"/>
<line x1="716.7" y1="364.3" x2="716.7" y2="413.5" stroke="var(--down)" class="wick"/>
<rect x="715.47" y="385.0" width="2.46" height="15.3" fill="var(--down)"/>
<line x1="720.7" y1="407.8" x2="720.7" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="719.44" y="415.8" width="2.46" height="32.8" fill="var(--down)"/>
<line x1="724.6" y1="426.1" x2="724.6" y2="457.7" stroke="var(--up)" class="wick"/>
<rect x="723.41" y="437.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="728.6" y1="398.4" x2="728.6" y2="448.6" stroke="var(--down)" class="wick"/>
<rect x="727.38" y="423.5" width="2.46" height="10.9" fill="var(--down)"/>
<line x1="732.6" y1="455.7" x2="732.6" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="731.35" y="455.7" width="2.46" height="47.0" fill="var(--down)"/>
<line x1="736.5" y1="458.6" x2="736.5" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="735.31" y="476.4" width="2.46" height="27.1" fill="var(--up)"/>
<line x1="740.5" y1="404.2" x2="740.5" y2="457.8" stroke="var(--up)" class="wick"/>
<rect x="739.28" y="422.9" width="2.46" height="26.7" fill="var(--up)"/>
<line x1="744.5" y1="421.3" x2="744.5" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="743.25" y="421.3" width="2.46" height="34.4" fill="var(--down)"/>
<line x1="748.4" y1="429.7" x2="748.4" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="747.22" y="447.0" width="2.46" height="2.3" fill="var(--down)"/>
<line x1="752.4" y1="457.7" x2="752.4" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="751.19" y="460.5" width="2.46" height="43.3" fill="var(--down)"/>
<line x1="756.4" y1="459.3" x2="756.4" y2="512.7" stroke="var(--down)" class="wick"/>
<rect x="755.15" y="486.2" width="2.46" height="7.8" fill="var(--down)"/>
<line x1="760.4" y1="480.5" x2="760.4" y2="534.1" stroke="var(--down)" class="wick"/>
<rect x="759.12" y="507.5" width="2.46" height="16.2" fill="var(--down)"/>
<line x1="764.3" y1="487.4" x2="764.3" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="763.09" y="507.0" width="2.46" height="8.4" fill="var(--down)"/>
<line x1="768.3" y1="503.1" x2="768.3" y2="542.3" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="503.1" width="2.46" height="32.6" fill="var(--down)"/>
<line x1="772.3" y1="484.7" x2="772.3" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="771.03" y="521.1" width="2.46" height="5.2" fill="var(--up)"/>
<line x1="776.2" y1="497.6" x2="776.2" y2="548.5" stroke="var(--down)" class="wick"/>
<rect x="774.99" y="519.7" width="2.46" height="20.8" fill="var(--down)"/>
<line x1="780.2" y1="506.3" x2="780.2" y2="552.6" stroke="var(--up)" class="wick"/>
<rect x="778.96" y="520.2" width="2.46" height="17.6" fill="var(--up)"/>
<line x1="784.2" y1="497.4" x2="784.2" y2="562.1" stroke="var(--up)" class="wick"/>
<rect x="782.93" y="503.1" width="2.46" height="27.1" fill="var(--up)"/>
<line x1="788.1" y1="481.0" x2="788.1" y2="500.8" stroke="var(--up)" class="wick"/>
<rect x="786.90" y="484.6" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="792.1" y1="463.7" x2="792.1" y2="518.6" stroke="var(--down)" class="wick"/>
<rect x="790.87" y="483.3" width="2.46" height="27.6" fill="var(--down)"/>
<line x1="796.1" y1="411.5" x2="796.1" y2="502.0" stroke="var(--up)" class="wick"/>
<rect x="794.83" y="430.2" width="2.46" height="71.8" fill="var(--up)"/>
<line x1="800.0" y1="444.3" x2="800.0" y2="474.4" stroke="var(--down)" class="wick"/>
<rect x="798.80" y="444.3" width="2.46" height="14.1" fill="var(--down)"/>
<line x1="804.0" y1="463.2" x2="804.0" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="465.3" width="2.46" height="34.9" fill="var(--down)"/>
<line x1="808.0" y1="531.2" x2="808.0" y2="584.0" stroke="var(--down)" class="wick"/>
<rect x="806.74" y="536.6" width="2.46" height="22.1" fill="var(--down)"/>
<line x1="811.9" y1="543.7" x2="811.9" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="810.71" y="549.0" width="2.46" height="12.5" fill="var(--up)"/>
<line x1="815.9" y1="520.0" x2="815.9" y2="563.7" stroke="var(--down)" class="wick"/>
<rect x="814.67" y="547.1" width="2.46" height="13.2" fill="var(--down)"/>
<line x1="819.9" y1="507.7" x2="819.9" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="818.64" y="515.6" width="2.46" height="34.2" fill="var(--down)"/>
<line x1="823.8" y1="417.1" x2="823.8" y2="531.6" stroke="var(--up)" class="wick"/>
<rect x="822.61" y="447.2" width="2.46" height="76.9" fill="var(--up)"/>
<line x1="827.8" y1="447.0" x2="827.8" y2="474.2" stroke="var(--down)" class="wick"/>
<rect x="826.58" y="460.5" width="2.46" height="12.3" fill="var(--down)"/>
<line x1="831.8" y1="394.8" x2="831.8" y2="483.0" stroke="var(--up)" class="wick"/>
<rect x="830.55" y="409.2" width="2.46" height="71.2" fill="var(--up)"/>
<line x1="835.7" y1="377.9" x2="835.7" y2="414.4" stroke="var(--down)" class="wick"/>
<rect x="834.51" y="387.1" width="2.46" height="15.3" fill="var(--down)"/>
<line x1="839.7" y1="392.3" x2="839.7" y2="425.3" stroke="var(--down)" class="wick"/>
<rect x="838.48" y="408.7" width="2.46" height="6.4" fill="var(--down)"/>
<line x1="843.7" y1="382.0" x2="843.7" y2="415.8" stroke="var(--up)" class="wick"/>
<rect x="842.45" y="392.5" width="2.46" height="4.1" fill="var(--up)"/>
<line x1="847.6" y1="358.8" x2="847.6" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="377.3" width="2.46" height="30.3" fill="var(--up)"/>
<line x1="851.6" y1="331.7" x2="851.6" y2="375.7" stroke="var(--up)" class="wick"/>
<rect x="850.39" y="341.2" width="2.46" height="17.5" fill="var(--up)"/>
<line x1="855.6" y1="333.2" x2="855.6" y2="389.6" stroke="var(--down)" class="wick"/>
<rect x="854.35" y="343.1" width="2.46" height="32.4" fill="var(--down)"/>
<line x1="859.6" y1="344.7" x2="859.6" y2="382.3" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="370.0" width="2.46" height="8.7" fill="var(--down)"/>
<line x1="863.5" y1="369.7" x2="863.5" y2="428.8" stroke="var(--down)" class="wick"/>
<rect x="862.29" y="383.6" width="2.46" height="43.3" fill="var(--down)"/>
<line x1="867.5" y1="361.1" x2="867.5" y2="396.8" stroke="var(--up)" class="wick"/>
<rect x="866.26" y="370.2" width="2.46" height="21.4" fill="var(--up)"/>
<line x1="871.5" y1="325.9" x2="871.5" y2="369.1" stroke="var(--up)" class="wick"/>
<rect x="870.23" y="349.2" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="875.4" y1="344.7" x2="875.4" y2="424.4" stroke="var(--down)" class="wick"/>
<rect x="874.19" y="357.6" width="2.46" height="54.7" fill="var(--down)"/>
<line x1="879.4" y1="369.9" x2="879.4" y2="413.7" stroke="var(--down)" class="wick"/>
<rect x="878.16" y="379.5" width="2.46" height="23.5" fill="var(--down)"/>
<line x1="883.4" y1="402.5" x2="883.4" y2="438.3" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="408.2" width="2.46" height="5.0" fill="var(--down)"/>
<line x1="887.3" y1="429.5" x2="887.3" y2="489.4" stroke="var(--down)" class="wick"/>
<rect x="886.10" y="429.5" width="2.46" height="15.9" fill="var(--down)"/>
<line x1="891.3" y1="430.1" x2="891.3" y2="464.8" stroke="var(--up)" class="wick"/>
<rect x="890.07" y="431.3" width="2.46" height="16.0" fill="var(--up)"/>
<line x1="895.3" y1="355.8" x2="895.3" y2="425.8" stroke="var(--up)" class="wick"/>
<rect x="894.03" y="360.4" width="2.46" height="50.4" fill="var(--up)"/>
<line x1="899.2" y1="363.8" x2="899.2" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="898.00" y="373.4" width="2.46" height="24.4" fill="var(--down)"/>
<line x1="903.2" y1="323.4" x2="903.2" y2="374.7" stroke="var(--up)" class="wick"/>
<rect x="901.97" y="336.5" width="2.46" height="1.6" fill="var(--up)"/>
<line x1="907.2" y1="366.5" x2="907.2" y2="414.9" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="368.4" width="2.46" height="45.6" fill="var(--down)"/>
<line x1="911.1" y1="427.2" x2="911.1" y2="463.9" stroke="var(--up)" class="wick"/>
<rect x="909.91" y="441.6" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="915.1" y1="410.6" x2="915.1" y2="444.1" stroke="var(--down)" class="wick"/>
<rect x="913.87" y="437.2" width="2.46" height="1.1" fill="var(--down)"/>
<line x1="919.1" y1="384.6" x2="919.1" y2="437.0" stroke="var(--up)" class="wick"/>
<rect x="917.84" y="414.6" width="2.46" height="5.2" fill="var(--up)"/>
<line x1="923.0" y1="407.8" x2="923.0" y2="464.1" stroke="var(--down)" class="wick"/>
<rect x="921.81" y="414.6" width="2.46" height="40.8" fill="var(--down)"/>
<line x1="927.0" y1="410.6" x2="927.0" y2="480.6" stroke="var(--up)" class="wick"/>
<rect x="925.78" y="420.3" width="2.46" height="49.3" fill="var(--up)"/>
<line x1="931.0" y1="358.5" x2="931.0" y2="418.0" stroke="var(--up)" class="wick"/>
<rect x="929.75" y="358.8" width="2.46" height="35.8" fill="var(--up)"/>
<line x1="934.9" y1="308.6" x2="934.9" y2="397.8" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="334.6" width="2.46" height="51.3" fill="var(--down)"/>
<line x1="938.9" y1="383.7" x2="938.9" y2="413.5" stroke="var(--down)" class="wick"/>
<rect x="937.68" y="393.4" width="2.46" height="7.7" fill="var(--down)"/>
<line x1="942.9" y1="413.9" x2="942.9" y2="441.1" stroke="var(--up)" class="wick"/>
<rect x="941.65" y="419.4" width="2.46" height="4.3" fill="var(--up)"/>
<line x1="946.8" y1="377.3" x2="946.8" y2="406.5" stroke="var(--down)" class="wick"/>
<rect x="945.62" y="394.4" width="2.46" height="6.6" fill="var(--down)"/>
<line x1="950.8" y1="428.1" x2="950.8" y2="464.1" stroke="var(--up)" class="wick"/>
<rect x="949.59" y="439.5" width="2.46" height="14.8" fill="var(--up)"/>
<line x1="954.8" y1="421.3" x2="954.8" y2="467.5" stroke="var(--up)" class="wick"/>
<rect x="953.55" y="431.7" width="2.46" height="17.1" fill="var(--up)"/>
<line x1="958.8" y1="381.1" x2="958.8" y2="423.8" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="409.9" width="2.46" height="13.9" fill="var(--up)"/>
<line x1="962.7" y1="320.0" x2="962.7" y2="411.9" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="358.8" width="2.46" height="46.7" fill="var(--down)"/>
<line x1="966.7" y1="450.0" x2="966.7" y2="560.1" stroke="var(--up)" class="wick"/>
<rect x="965.46" y="455.0" width="2.46" height="84.1" fill="var(--up)"/>
<line x1="970.7" y1="484.4" x2="970.7" y2="523.6" stroke="var(--up)" class="wick"/>
<rect x="969.43" y="493.1" width="2.46" height="3.6" fill="var(--up)"/>
<line x1="974.6" y1="479.9" x2="974.6" y2="537.6" stroke="var(--up)" class="wick"/>
<rect x="973.39" y="483.7" width="2.46" height="17.5" fill="var(--up)"/>
<line x1="978.6" y1="436.3" x2="978.6" y2="487.8" stroke="var(--down)" class="wick"/>
<rect x="977.36" y="459.5" width="2.46" height="15.7" fill="var(--down)"/>
<line x1="982.6" y1="416.7" x2="982.6" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="421.0" width="2.46" height="70.7" fill="var(--up)"/>
<line x1="986.5" y1="423.8" x2="986.5" y2="480.6" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="423.8" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="990.5" y1="412.2" x2="990.5" y2="466.6" stroke="var(--down)" class="wick"/>
<rect x="989.27" y="424.4" width="2.46" height="15.1" fill="var(--down)"/>
<line x1="994.5" y1="456.8" x2="994.5" y2="494.5" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="460.5" width="2.46" height="15.9" fill="var(--up)"/>
<line x1="998.4" y1="448.6" x2="998.4" y2="489.7" stroke="var(--up)" class="wick"/>
<rect x="997.20" y="448.9" width="2.46" height="30.5" fill="var(--up)"/>
<line x1="1002.4" y1="461.9" x2="1002.4" y2="493.7" stroke="var(--down)" class="wick"/>
<rect x="1001.17" y="467.3" width="2.46" height="3.6" fill="var(--down)"/>
<line x1="1006.4" y1="475.7" x2="1006.4" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="1005.14" y="491.0" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="1010.3" y1="460.3" x2="1010.3" y2="492.4" stroke="var(--down)" class="wick"/>
<rect x="1009.11" y="481.9" width="2.46" height="5.9" fill="var(--down)"/>
<line x1="1014.3" y1="476.2" x2="1014.3" y2="502.7" stroke="var(--up)" class="wick"/>
<rect x="1013.07" y="482.6" width="2.46" height="3.9" fill="var(--up)"/>
<line x1="1018.3" y1="492.9" x2="1018.3" y2="519.5" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="498.8" width="2.46" height="9.3" fill="var(--down)"/>
<line x1="1022.2" y1="484.9" x2="1022.2" y2="515.9" stroke="var(--up)" class="wick"/>
<rect x="1021.01" y="502.2" width="2.46" height="3.0" fill="var(--up)"/>
<line x1="1026.2" y1="452.7" x2="1026.2" y2="499.2" stroke="var(--up)" class="wick"/>
<rect x="1024.98" y="485.6" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="1030.2" y1="476.0" x2="1030.2" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="1028.95" y="484.0" width="2.46" height="26.7" fill="var(--down)"/>
<line x1="1034.1" y1="469.8" x2="1034.1" y2="525.5" stroke="var(--up)" class="wick"/>
<rect x="1032.91" y="480.3" width="2.46" height="29.6" fill="var(--up)"/>
<line x1="1038.1" y1="442.5" x2="1038.1" y2="474.6" stroke="var(--up)" class="wick"/>
<rect x="1036.88" y="446.1" width="2.46" height="24.2" fill="var(--up)"/>
<line x1="1042.1" y1="454.6" x2="1042.1" y2="475.5" stroke="var(--down)" class="wick"/>
<rect x="1040.85" y="461.6" width="2.46" height="5.9" fill="var(--down)"/>
<line x1="1046.0" y1="458.0" x2="1046.0" y2="483.5" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="469.6" width="2.46" height="5.0" fill="var(--down)"/>
<line x1="1050.0" y1="489.7" x2="1050.0" y2="515.4" stroke="var(--down)" class="wick"/>
<rect x="1048.79" y="497.8" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="60" y1="396.4" x2="1052" y2="396.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="399.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$149 R1</text>
<text x="1058" y="411.9" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="306.5" x2="1052" y2="306.5" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="310.0" font-size="11.5" fill="var(--resistance)" font-weight="600">$154 R2</text>
<text x="1058" y="322.0" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="164.6" x2="1052" y2="164.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="168.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$162 R3</text>
<text x="1058" y="180.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="563.8" x2="1052" y2="563.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="557.8" font-size="11.5" fill="var(--support)" font-weight="600">$140 S1</text>
<text x="1058" y="569.8" font-size="9.5" fill="var(--muted)">터치 8회</text>
<circle cx="1052.0" cy="507.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="499.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $143 (2026-08-27)</text>
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
| R3 | $162 | 2 | 2025-09-17·2026-02-12 — 1년 구간의 상단. 2026년 2월 52주 최고($167.20, 2026-02-27) 직전에 만들어진 고점대다 |
| R2 | $154 | 6 | 2025-09-30·2025-10-24·2026-06-24·2026-07-07·2026-07-17·2026-07-28 — **1년의 앞뒤 양끝에서 모두 터치된 유일한 레벨.** 마지막 터치(2026-07-28)는 FY2026 실적 발표 직전이다 |
| R1 | $149 | 6 | 2025-11-21·2025-12-17·2026-04-09·2026-04-24·2026-05-27·2026-08-06 — 현재가에서 가장 가까운 저항. 가장 최근 터치가 2026-08-06으로 3주 전이다 |
| **현재가** | **$143.14** (2026-08-27 종가) | — | R1($149)과 S1($140) 사이, S1 쪽에 가깝다(S1까지 −2.2%, R1까지 +4.1%) |
| S1 | $140 | 8 | 2025-12-08·2025-12-23·2026-01-07·2026-04-07·2026-04-22·2026-05-21·2026-06-01·2026-07-29 — **1년 중 터치 8회로 가장 두꺼운 레벨**이고, 최근 터치(2026-07-29)가 FY2026 실적 발표일이다 |
| 참고선 | $167.25 | — | 52주 최고가(장중, 종가 기준 2026-02-27 $167.20). 이후 6개월간 한 번도 되돌리지 못해 근시일 저항으로 보지 않고 참고선으로만 둔다 |
| 참고선 | $137.62 | — | 52주 최저가(장중, 종가 기준 2026-01-07 $138.04). S1 클러스터($140)와 1.7% 차이라 별도 지지로 세우지 않는다 |

**지지 레벨이 S1 하나뿐이다.** 터치 2회 이상 기준을 만족하는 저점 클러스터가 $140 하나밖에 나오지 않았고, 그 아래는 52주 최저 참고선($137.62)까지 비어 있다. 이는 **최근 1년의 하단이 좁은 가격대에 반복해서 눌려 왔다**는 뜻이기도 하지만, 동시에 그 레벨이 뚫렸을 때 참고할 다음 지지가 이 차트 안에 없다는 뜻이기도 하다 — 5년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)에서 본다.

---

## 3. 관측된 특이 구간 — 2026-07-29 FY2026 연간 실적 발표

- FY2026 4분기·연간 실적과 FY2027 가이던스 발표일이다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **−1.9%** ($148.88 → $146.10), 거래량은 평소(일 948만 주 내외) 대비 약 **1.5배**인 **1,462만 주**. 이튿날에도 −1.5%($143.96)로 이어져 이틀 누적 −3.3%였다.
- **이 구간은 가격대를 재설정한 갭이 아니다.** 최근 1년에서 일간 변동이 가장 컸던 날조차 +4.1%(2026-06-05)로, 스윙 레벨을 무효화할 만한 불연속은 관측되지 않았다. 이 차트의 하락은 사건 하나가 만든 것이 아니라 **2026-02-27 고점($167.20)에서 6개월에 걸쳐 −14.4% 밀려 내려온 완만한 흐름**이며, 그래서 2절의 레벨은 전 구간에 걸쳐 그대로 유효한 것으로 다뤘다. 다만 실적 발표 당일 종가가 **S1($140) 클러스터의 마지막 터치일과 겹친다**는 점은 기록해 둔다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py PG --name "프록터 앤 갬블" --close-on 2026-08-27 --emit all` (기본 옵션 그대로, `--force-level`·`--levels` 변경 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **지지 클러스터가 1개뿐**이라 하단 구조의 표본이 얇다. 기본 `--levels 3`을 그대로 뒀지만 유효 클러스터가 부족해 S2·S3는 생성되지 않았고, 억지로 채우지 않았다.
    - 기간 내 주식분할·유상증자는 없었다. **배당은 4회 지급됐고 이 차트는 원주가라 배당이 반영되지 않았다** — 총수익률이 아니므로 장기 성과 비교에 그대로 쓰면 안 된다.

---

*작성일: 2026-08-30*
