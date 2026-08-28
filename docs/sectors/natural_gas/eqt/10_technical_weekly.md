# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV(2026-08-28 수집). 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-08-27 종가 **$54.77**은 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)가 "현재가"로 쓰는 값과 일치한다.
    - **배당 처리**: 이 차트는 원주가(분할은 소급 반영, **배당은 미반영**)다. 5년간 분기배당이 19회 지급됐으므로 총수익률과는 다르다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-27)

<div class="eqt-chart">
<style>
.eqt-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .eqt-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.eqt-chart svg { width:100%; height:auto; display:block; }
.eqt-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.eqt-chart .title { fill: var(--ink); font-weight:600; }
.eqt-chart .grid { stroke: var(--grid); stroke-width:1; }
.eqt-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="EQT(EQT) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">EQT (EQT) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-27 · 마지막 종가 $54.77 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="583.8" x2="1052" y2="583.8" class="grid"/>
<text x="52" y="587.8" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="478.2" x2="1052" y2="478.2" class="grid"/>
<text x="52" y="482.2" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="372.7" x2="1052" y2="372.7" class="grid"/>
<text x="52" y="376.7" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="267.1" x2="1052" y2="267.1" class="grid"/>
<text x="52" y="271.1" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="161.6" x2="1052" y2="161.6" class="grid"/>
<text x="52" y="165.6" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="133.6" y1="56.0" x2="133.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="133.6" y1="626.0" x2="133.6" y2="631.0" class="axis"/>
<text x="133.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="329.7" y1="56.0" x2="329.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="329.7" y1="626.0" x2="329.7" y2="631.0" class="axis"/>
<text x="329.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="525.8" y1="56.0" x2="525.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="525.8" y1="626.0" x2="525.8" y2="631.0" class="axis"/>
<text x="525.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="725.7" y1="56.0" x2="725.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="725.7" y1="626.0" x2="725.7" y2="631.0" class="axis"/>
<text x="725.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.9" y1="56.0" x2="921.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.9" y1="626.0" x2="921.9" y2="631.0" class="axis"/>
<text x="921.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="74.6" x2="1052" y2="74.6" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="77.6" font-size="10.5" fill="var(--muted)">$68 5년 최고</text>
<line x1="60" y1="608.2" x2="1052" y2="608.2" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="611.2" font-size="10.5" fill="var(--muted)">$17.69 5년 최저</text>
<line x1="635.2" y1="56.0" x2="635.2" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="641.2" y="68.0" font-size="10.5" fill="var(--down)">2024-07-22 Equitrans 인수 완료</text>
<line x1="61.9" y1="595.1" x2="61.9" y2="608.2" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="598.3" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="65.7" y1="575.9" x2="65.7" y2="606.5" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="578.2" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="69.4" y1="570.0" x2="69.4" y2="590.9" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="577.2" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="73.2" y1="574.9" x2="73.2" y2="596.8" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="585.4" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="77.0" y1="579.2" x2="77.0" y2="604.6" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="583.9" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="80.7" y1="553.2" x2="80.7" y2="581.6" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="574.8" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="84.5" y1="558.1" x2="84.5" y2="579.7" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="574.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="88.3" y1="570.5" x2="88.3" y2="590.5" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="571.9" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="92.1" y1="568.4" x2="92.1" y2="588.3" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="569.0" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="95.8" y1="553.3" x2="95.8" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="563.8" width="2.34" height="20.9" fill="var(--down)"/>
<line x1="99.6" y1="571.7" x2="99.6" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="577.7" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="103.4" y1="565.8" x2="103.4" y2="592.5" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="569.4" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="107.1" y1="559.3" x2="107.1" y2="579.7" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="567.6" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="110.9" y1="566.1" x2="110.9" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="573.3" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="114.7" y1="570.7" x2="114.7" y2="605.4" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="573.4" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="118.5" y1="571.2" x2="118.5" y2="598.7" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="574.7" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="122.2" y1="560.8" x2="122.2" y2="584.0" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="570.5" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="126.0" y1="557.8" x2="126.0" y2="578.5" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="561.3" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="129.8" y1="548.2" x2="129.8" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="557.1" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="133.6" y1="548.9" x2="133.6" y2="568.3" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="554.1" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="137.3" y1="532.7" x2="137.3" y2="558.2" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="543.8" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="141.1" y1="542.4" x2="141.1" y2="579.9" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="542.6" width="2.34" height="35.3" fill="var(--down)"/>
<line x1="144.9" y1="568.5" x2="144.9" y2="592.2" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="571.7" width="2.34" height="12.0" fill="var(--up)"/>
<line x1="148.6" y1="558.7" x2="148.6" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="567.3" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="152.4" y1="551.9" x2="152.4" y2="577.1" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="552.8" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="156.2" y1="541.4" x2="156.2" y2="560.0" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="551.9" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="160.0" y1="552.1" x2="160.0" y2="569.8" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="553.2" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="163.7" y1="511.1" x2="163.7" y2="558.6" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="516.6" width="2.34" height="41.7" fill="var(--up)"/>
<line x1="167.5" y1="504.0" x2="167.5" y2="536.1" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="509.9" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="171.3" y1="507.4" x2="171.3" y2="538.4" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="508.6" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="175.0" y1="431.0" x2="175.0" y2="503.9" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="432.5" width="2.34" height="71.4" fill="var(--up)"/>
<line x1="178.8" y1="414.0" x2="178.8" y2="451.3" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="414.6" width="2.34" height="27.0" fill="var(--up)"/>
<line x1="182.6" y1="386.1" x2="182.6" y2="420.7" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="390.5" width="2.34" height="17.1" fill="var(--up)"/>
<line x1="186.4" y1="345.4" x2="186.4" y2="398.8" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="347.8" width="2.34" height="43.5" fill="var(--up)"/>
<line x1="190.1" y1="314.6" x2="190.1" y2="377.0" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="336.1" width="2.34" height="39.3" fill="var(--down)"/>
<line x1="193.9" y1="352.7" x2="193.9" y2="395.9" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="375.3" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="197.7" y1="337.2" x2="197.7" y2="391.7" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="361.6" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="201.4" y1="372.8" x2="201.4" y2="429.5" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="373.2" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="205.2" y1="338.4" x2="205.2" y2="388.0" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="363.7" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="209.0" y1="276.0" x2="209.0" y2="362.1" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="283.7" width="2.34" height="76.2" fill="var(--up)"/>
<line x1="212.8" y1="262.8" x2="212.8" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="275.5" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="216.5" y1="263.9" x2="216.5" y2="300.9" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="277.4" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="220.3" y1="301.5" x2="220.3" y2="424.2" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="304.2" width="2.34" height="111.4" fill="var(--down)"/>
<line x1="224.1" y1="400.8" x2="224.1" y2="450.8" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="407.7" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="227.8" y1="380.8" x2="227.8" y2="439.7" stroke="var(--down)" class="wick"/>
<rect x="226.68" y="418.9" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="231.6" y1="424.8" x2="231.6" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="433.9" width="2.34" height="5.8" fill="var(--up)"/>
<line x1="235.4" y1="397.7" x2="235.4" y2="445.1" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="408.3" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="239.2" y1="331.1" x2="239.2" y2="401.2" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="349.1" width="2.34" height="52.0" fill="var(--up)"/>
<line x1="242.9" y1="301.8" x2="242.9" y2="350.9" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="330.1" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="246.7" y1="337.0" x2="246.7" y2="370.7" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="340.6" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="250.5" y1="306.2" x2="250.5" y2="359.2" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="307.3" width="2.34" height="45.5" fill="var(--up)"/>
<line x1="254.3" y1="277.1" x2="254.3" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="291.4" width="2.34" height="39.1" fill="var(--up)"/>
<line x1="258.0" y1="248.9" x2="258.0" y2="297.3" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="270.6" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="261.8" y1="252.3" x2="261.8" y2="315.8" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="278.2" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="265.6" y1="277.1" x2="265.6" y2="326.9" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="284.5" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="269.3" y1="246.3" x2="269.3" y2="323.7" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="280.7" width="2.34" height="28.0" fill="var(--down)"/>
<line x1="273.1" y1="287.5" x2="273.1" y2="375.6" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="320.2" width="2.34" height="39.2" fill="var(--down)"/>
<line x1="276.9" y1="358.1" x2="276.9" y2="392.2" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="364.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="280.7" y1="310.3" x2="280.7" y2="364.8" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="339.2" width="2.34" height="25.0" fill="var(--up)"/>
<line x1="284.4" y1="321.6" x2="284.4" y2="361.5" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="332.0" width="2.34" height="28.7" fill="var(--down)"/>
<line x1="288.2" y1="333.3" x2="288.2" y2="399.3" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="361.2" width="2.34" height="33.9" fill="var(--down)"/>
<line x1="292.0" y1="361.1" x2="292.0" y2="406.7" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="386.6" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="295.7" y1="346.1" x2="295.7" y2="380.1" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="361.3" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="299.5" y1="322.5" x2="299.5" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="345.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="303.3" y1="324.9" x2="303.3" y2="373.9" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="336.7" width="2.34" height="25.1" fill="var(--down)"/>
<line x1="307.1" y1="320.1" x2="307.1" y2="379.7" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="340.7" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="310.8" y1="336.9" x2="310.8" y2="377.7" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="357.4" width="2.34" height="16.0" fill="var(--down)"/>
<line x1="314.6" y1="374.5" x2="314.6" y2="421.8" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="378.8" width="2.34" height="39.6" fill="var(--down)"/>
<line x1="318.4" y1="381.4" x2="318.4" y2="411.9" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="401.8" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="322.1" y1="403.2" x2="322.1" y2="431.2" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="408.8" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="325.9" y1="404.1" x2="325.9" y2="446.2" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="409.6" width="2.34" height="28.2" fill="var(--down)"/>
<line x1="329.7" y1="435.4" x2="329.7" y2="462.4" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="443.0" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="333.5" y1="422.0" x2="333.5" y2="445.2" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="427.4" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="337.2" y1="415.1" x2="337.2" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="421.6" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="341.0" y1="420.7" x2="341.0" y2="457.7" stroke="var(--down)" class="wick"/>
<rect x="339.83" y="430.9" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="344.8" y1="448.1" x2="344.8" y2="468.9" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="455.0" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="348.5" y1="459.6" x2="348.5" y2="488.7" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="460.6" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="352.3" y1="444.8" x2="352.3" y2="478.6" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="464.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="356.1" y1="427.9" x2="356.1" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="428.3" width="2.34" height="36.3" fill="var(--up)"/>
<line x1="359.9" y1="427.6" x2="359.9" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="428.1" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="363.6" y1="441.0" x2="363.6" y2="476.6" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="444.2" width="2.34" height="29.7" fill="var(--down)"/>
<line x1="367.4" y1="463.6" x2="367.4" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="481.2" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="371.2" y1="465.9" x2="371.2" y2="488.3" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="472.3" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="375.0" y1="452.6" x2="375.0" y2="482.3" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="458.1" width="2.34" height="12.2" fill="var(--up)"/>
<line x1="378.7" y1="447.6" x2="378.7" y2="464.4" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="448.2" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="382.5" y1="437.2" x2="382.5" y2="454.4" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="445.1" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="386.3" y1="433.7" x2="386.3" y2="455.4" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="437.2" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="390.0" y1="423.3" x2="390.0" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="427.1" width="2.34" height="24.5" fill="var(--up)"/>
<line x1="393.8" y1="426.9" x2="393.8" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="431.8" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="397.6" y1="440.3" x2="397.6" y2="461.5" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="441.8" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="401.4" y1="399.1" x2="401.4" y2="439.2" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="412.5" width="2.34" height="24.7" fill="var(--up)"/>
<line x1="405.1" y1="406.5" x2="405.1" y2="421.5" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="413.9" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="408.9" y1="404.9" x2="408.9" y2="434.3" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="409.1" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="412.7" y1="381.0" x2="412.7" y2="419.6" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="388.0" width="2.34" height="13.2" fill="var(--up)"/>
<line x1="416.4" y1="371.5" x2="416.4" y2="396.1" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="376.5" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="420.2" y1="372.7" x2="420.2" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="419.04" y="375.8" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="424.0" y1="357.8" x2="424.0" y2="379.6" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="360.7" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="427.8" y1="358.6" x2="427.8" y2="387.0" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="363.2" width="2.34" height="12.6" fill="var(--down)"/>
<line x1="431.5" y1="362.1" x2="431.5" y2="392.7" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="377.6" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="435.3" y1="360.9" x2="435.3" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="373.7" width="2.34" height="19.4" fill="var(--up)"/>
<line x1="439.1" y1="344.7" x2="439.1" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="348.6" width="2.34" height="26.7" fill="var(--up)"/>
<line x1="442.8" y1="345.5" x2="442.8" y2="373.4" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="353.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="446.6" y1="326.6" x2="446.6" y2="362.1" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="340.5" width="2.34" height="9.4" fill="var(--up)"/>
<line x1="450.4" y1="334.8" x2="450.4" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="336.0" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="454.2" y1="321.2" x2="454.2" y2="358.1" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="330.4" width="2.34" height="20.7" fill="var(--down)"/>
<line x1="457.9" y1="327.9" x2="457.9" y2="354.0" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="328.1" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="461.7" y1="330.3" x2="461.7" y2="356.0" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="331.1" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="465.5" y1="330.5" x2="465.5" y2="358.3" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="343.9" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="469.2" y1="352.6" x2="469.2" y2="390.4" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="357.5" width="2.34" height="31.6" fill="var(--down)"/>
<line x1="473.0" y1="364.6" x2="473.0" y2="392.0" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="366.5" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="476.8" y1="339.1" x2="476.8" y2="386.9" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="343.2" width="2.34" height="26.1" fill="var(--up)"/>
<line x1="480.6" y1="324.6" x2="480.6" y2="344.9" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="337.1" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="484.3" y1="323.5" x2="484.3" y2="353.6" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="335.7" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="488.1" y1="338.8" x2="488.1" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="352.1" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="491.9" y1="317.5" x2="491.9" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="322.8" width="2.34" height="34.2" fill="var(--up)"/>
<line x1="495.7" y1="325.5" x2="495.7" y2="387.2" stroke="var(--down)" class="wick"/>
<rect x="494.48" y="328.4" width="2.34" height="53.4" fill="var(--down)"/>
<line x1="499.4" y1="354.5" x2="499.4" y2="381.0" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="368.8" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="503.2" y1="361.1" x2="503.2" y2="381.3" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="363.7" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="507.0" y1="364.3" x2="507.0" y2="380.6" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="367.3" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="510.7" y1="373.6" x2="510.7" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="376.4" width="2.34" height="26.6" fill="var(--down)"/>
<line x1="514.5" y1="384.7" x2="514.5" y2="416.5" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="389.1" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="518.3" y1="377.3" x2="518.3" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="380.8" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="522.1" y1="373.9" x2="522.1" y2="386.8" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="383.2" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="525.8" y1="379.0" x2="525.8" y2="398.5" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="382.1" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="529.6" y1="387.5" x2="529.6" y2="404.1" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="393.6" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="533.4" y1="400.4" x2="533.4" y2="429.2" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="405.3" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="537.1" y1="412.4" x2="537.1" y2="427.9" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="416.2" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="540.9" y1="409.6" x2="540.9" y2="429.9" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="417.3" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="544.7" y1="426.7" x2="544.7" y2="437.7" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="427.8" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="548.5" y1="421.6" x2="548.5" y2="456.4" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="428.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="552.2" y1="391.2" x2="552.2" y2="440.8" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="404.2" width="2.34" height="25.4" fill="var(--up)"/>
<line x1="556.0" y1="396.9" x2="556.0" y2="410.8" stroke="var(--down)" class="wick"/>
<rect x="554.83" y="399.8" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="559.8" y1="390.5" x2="559.8" y2="403.3" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="395.4" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="563.5" y1="420.5" x2="563.5" y2="446.7" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="426.5" width="2.34" height="15.5" fill="var(--down)"/>
<line x1="567.3" y1="431.7" x2="567.3" y2="444.8" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="432.2" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="571.1" y1="400.1" x2="571.1" y2="431.5" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="403.6" width="2.34" height="27.3" fill="var(--up)"/>
<line x1="574.9" y1="395.5" x2="574.9" y2="413.9" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="400.8" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="578.6" y1="389.5" x2="578.6" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="577.46" y="401.7" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="582.4" y1="397.6" x2="582.4" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="401.2" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="586.2" y1="361.7" x2="586.2" y2="410.1" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="366.2" width="2.34" height="43.5" fill="var(--up)"/>
<line x1="589.9" y1="357.1" x2="589.9" y2="390.6" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="367.2" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="593.7" y1="357.1" x2="593.7" y2="386.0" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="363.9" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="597.5" y1="350.2" x2="597.5" y2="385.5" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="360.3" width="2.34" height="21.1" fill="var(--up)"/>
<line x1="601.3" y1="346.8" x2="601.3" y2="375.5" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="357.6" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="605.0" y1="354.7" x2="605.0" y2="369.1" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="361.2" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="608.8" y1="350.7" x2="608.8" y2="372.2" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="352.6" width="2.34" height="14.4" fill="var(--down)"/>
<line x1="612.6" y1="353.9" x2="612.6" y2="380.1" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="363.8" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="616.3" y1="378.2" x2="616.3" y2="405.3" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="381.6" width="2.34" height="23.0" fill="var(--down)"/>
<line x1="620.1" y1="386.7" x2="620.1" y2="406.4" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="401.7" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="623.9" y1="397.6" x2="623.9" y2="414.6" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="405.4" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="627.7" y1="398.3" x2="627.7" y2="418.4" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="402.1" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="631.4" y1="400.2" x2="631.4" y2="426.0" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="401.7" width="2.34" height="14.5" fill="var(--down)"/>
<line x1="635.2" y1="407.8" x2="635.2" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="411.8" width="2.34" height="20.9" fill="var(--down)"/>
<line x1="639.0" y1="421.8" x2="639.0" y2="463.3" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="430.8" width="2.34" height="30.8" fill="var(--down)"/>
<line x1="642.8" y1="460.6" x2="642.8" y2="478.0" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="466.6" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="646.5" y1="453.1" x2="646.5" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="455.5" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="650.3" y1="437.1" x2="650.3" y2="453.9" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="439.8" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="654.1" y1="434.4" x2="654.1" y2="456.6" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="437.3" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="657.8" y1="438.6" x2="657.8" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="446.1" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="661.6" y1="437.1" x2="661.6" y2="462.8" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="444.6" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="665.4" y1="423.9" x2="665.4" y2="447.7" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="427.2" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="669.2" y1="403.2" x2="669.2" y2="426.6" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="409.3" width="2.34" height="16.1" fill="var(--up)"/>
<line x1="672.9" y1="392.1" x2="672.9" y2="416.1" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="405.0" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="676.7" y1="398.4" x2="676.7" y2="412.9" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="400.0" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="680.5" y1="402.2" x2="680.5" y2="415.0" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="403.0" width="2.34" height="6.8" fill="var(--down)"/>
<line x1="684.2" y1="396.2" x2="684.2" y2="418.1" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="399.3" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="688.0" y1="385.0" x2="688.0" y2="420.7" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="405.4" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="691.8" y1="356.0" x2="691.8" y2="419.1" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="359.8" width="2.34" height="58.3" fill="var(--up)"/>
<line x1="695.6" y1="327.5" x2="695.6" y2="352.3" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="344.1" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="699.3" y1="288.0" x2="699.3" y2="344.8" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="310.2" width="2.34" height="30.9" fill="var(--up)"/>
<line x1="703.1" y1="289.1" x2="703.1" y2="322.0" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="292.7" width="2.34" height="22.6" fill="var(--down)"/>
<line x1="706.9" y1="314.2" x2="706.9" y2="338.8" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="319.9" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="710.6" y1="306.1" x2="710.6" y2="343.9" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="313.7" width="2.34" height="16.9" fill="var(--up)"/>
<line x1="714.4" y1="311.2" x2="714.4" y2="348.7" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="313.7" width="2.34" height="27.4" fill="var(--down)"/>
<line x1="718.2" y1="320.1" x2="718.2" y2="342.6" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="327.1" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="722.0" y1="284.7" x2="722.0" y2="319.3" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="298.6" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="725.7" y1="266.8" x2="725.7" y2="295.6" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="277.7" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="729.5" y1="225.1" x2="729.5" y2="279.9" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="235.9" width="2.34" height="40.7" fill="var(--up)"/>
<line x1="733.3" y1="215.9" x2="733.3" y2="243.6" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="228.3" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="737.0" y1="245.3" x2="737.0" y2="292.5" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="253.8" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="740.8" y1="229.5" x2="740.8" y2="259.3" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="248.0" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="744.6" y1="219.3" x2="744.6" y2="251.2" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="230.9" width="2.34" height="19.5" fill="var(--up)"/>
<line x1="748.4" y1="196.8" x2="748.4" y2="269.3" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="228.9" width="2.34" height="35.7" fill="var(--down)"/>
<line x1="752.1" y1="260.2" x2="752.1" y2="307.2" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="266.4" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="755.9" y1="254.3" x2="755.9" y2="318.0" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="279.3" width="2.34" height="19.5" fill="var(--down)"/>
<line x1="759.7" y1="257.8" x2="759.7" y2="304.8" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="259.5" width="2.34" height="34.7" fill="var(--up)"/>
<line x1="763.5" y1="219.6" x2="763.5" y2="261.9" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="236.7" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="767.2" y1="210.7" x2="767.2" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="230.9" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="771.0" y1="211.7" x2="771.0" y2="335.0" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="238.7" width="2.34" height="69.5" fill="var(--down)"/>
<line x1="774.8" y1="258.0" x2="774.8" y2="324.6" stroke="var(--up)" class="wick"/>
<rect x="773.60" y="270.8" width="2.34" height="53.0" fill="var(--up)"/>
<line x1="778.5" y1="246.6" x2="778.5" y2="271.7" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="256.8" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="782.3" y1="262.8" x2="782.3" y2="297.3" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="264.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="786.1" y1="247.0" x2="786.1" y2="278.4" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="247.6" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="789.9" y1="207.5" x2="789.9" y2="247.5" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="207.8" width="2.34" height="38.7" fill="var(--up)"/>
<line x1="793.6" y1="192.8" x2="793.6" y2="224.8" stroke="var(--down)" class="wick"/>
<rect x="792.46" y="203.3" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="797.4" y1="189.3" x2="797.4" y2="215.2" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="207.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="801.2" y1="192.9" x2="801.2" y2="219.8" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="202.9" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="804.9" y1="191.2" x2="804.9" y2="215.0" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="199.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="808.7" y1="193.6" x2="808.7" y2="231.2" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="194.9" width="2.34" height="8.0" fill="var(--up)"/>
<line x1="812.5" y1="153.1" x2="812.5" y2="194.4" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="156.9" width="2.34" height="37.0" fill="var(--up)"/>
<line x1="816.3" y1="150.8" x2="816.3" y2="187.2" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="153.1" width="2.34" height="26.3" fill="var(--down)"/>
<line x1="820.0" y1="173.4" x2="820.0" y2="217.4" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="182.9" width="2.34" height="28.2" fill="var(--down)"/>
<line x1="823.8" y1="194.3" x2="823.8" y2="231.0" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="210.8" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="827.6" y1="158.3" x2="827.6" y2="210.2" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="170.1" width="2.34" height="39.5" fill="var(--up)"/>
<line x1="831.3" y1="182.8" x2="831.3" y2="253.8" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="184.8" width="2.34" height="59.2" fill="var(--down)"/>
<line x1="835.1" y1="219.8" x2="835.1" y2="255.8" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="240.2" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="838.9" y1="237.6" x2="838.9" y2="260.5" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="241.0" width="2.34" height="12.5" fill="var(--down)"/>
<line x1="842.7" y1="231.4" x2="842.7" y2="262.7" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="237.0" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="846.4" y1="237.1" x2="846.4" y2="273.4" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="246.3" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="850.2" y1="233.7" x2="850.2" y2="258.7" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="247.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="854.0" y1="235.4" x2="854.0" y2="261.7" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="250.2" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="857.7" y1="240.1" x2="857.7" y2="266.7" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="241.9" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="861.5" y1="255.9" x2="861.5" y2="283.3" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="258.6" width="2.34" height="17.1" fill="var(--down)"/>
<line x1="865.3" y1="214.8" x2="865.3" y2="281.9" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="224.3" width="2.34" height="53.2" fill="var(--up)"/>
<line x1="869.1" y1="189.5" x2="869.1" y2="229.0" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="203.5" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="872.8" y1="187.4" x2="872.8" y2="234.3" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="197.5" width="2.34" height="36.6" fill="var(--down)"/>
<line x1="876.6" y1="201.4" x2="876.6" y2="249.6" stroke="var(--up)" class="wick"/>
<rect x="875.44" y="224.0" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="880.4" y1="192.7" x2="880.4" y2="245.2" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="210.6" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="884.2" y1="221.2" x2="884.2" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="226.6" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="887.9" y1="182.8" x2="887.9" y2="230.9" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="183.0" width="2.34" height="44.6" fill="var(--up)"/>
<line x1="891.7" y1="148.3" x2="891.7" y2="183.7" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="162.6" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="895.5" y1="154.6" x2="895.5" y2="213.0" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="165.9" width="2.34" height="27.0" fill="var(--down)"/>
<line x1="899.2" y1="149.2" x2="899.2" y2="211.6" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="152.5" width="2.34" height="43.3" fill="var(--up)"/>
<line x1="903.0" y1="138.0" x2="903.0" y2="177.5" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="154.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="906.8" y1="156.4" x2="906.8" y2="214.1" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="157.1" width="2.34" height="51.2" fill="var(--down)"/>
<line x1="910.6" y1="208.2" x2="910.6" y2="238.2" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="208.3" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="914.3" y1="217.1" x2="914.3" y2="234.1" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="225.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="918.1" y1="212.2" x2="918.1" y2="240.4" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="224.9" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="921.9" y1="217.6" x2="921.9" y2="262.4" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="236.5" width="2.34" height="19.1" fill="var(--down)"/>
<line x1="925.6" y1="234.0" x2="925.6" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="251.3" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="929.4" y1="199.2" x2="929.4" y2="257.4" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="208.8" width="2.34" height="28.4" fill="var(--up)"/>
<line x1="933.2" y1="179.7" x2="933.2" y2="228.1" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="185.5" width="2.34" height="15.0" fill="var(--up)"/>
<line x1="937.0" y1="193.3" x2="937.0" y2="224.8" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="195.4" width="2.34" height="13.6" fill="var(--up)"/>
<line x1="940.7" y1="172.0" x2="940.7" y2="213.1" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="175.3" width="2.34" height="33.1" fill="var(--up)"/>
<line x1="944.5" y1="148.5" x2="944.5" y2="205.8" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="156.3" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="948.3" y1="142.9" x2="948.3" y2="186.6" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="146.6" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="952.0" y1="129.3" x2="952.0" y2="160.3" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="137.4" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="955.8" y1="105.2" x2="955.8" y2="147.5" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="115.4" width="2.34" height="21.4" fill="var(--up)"/>
<line x1="959.6" y1="86.1" x2="959.6" y2="166.8" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="112.3" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="963.4" y1="74.6" x2="963.4" y2="129.8" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="81.9" width="2.34" height="44.5" fill="var(--up)"/>
<line x1="967.1" y1="79.9" x2="967.1" y2="167.9" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="82.8" width="2.34" height="81.9" fill="var(--down)"/>
<line x1="970.9" y1="145.2" x2="970.9" y2="181.7" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="166.3" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="974.7" y1="172.4" x2="974.7" y2="199.8" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="174.4" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="978.4" y1="166.8" x2="978.4" y2="201.0" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="173.1" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="982.2" y1="153.1" x2="982.2" y2="181.3" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="166.2" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="986.0" y1="163.3" x2="986.0" y2="211.1" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="174.2" width="2.34" height="30.0" fill="var(--down)"/>
<line x1="989.8" y1="190.9" x2="989.8" y2="213.2" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="198.5" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="993.5" y1="163.7" x2="993.5" y2="202.8" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="183.5" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="997.3" y1="183.4" x2="997.3" y2="219.3" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="186.2" width="2.34" height="28.9" fill="var(--down)"/>
<line x1="1001.1" y1="206.7" x2="1001.1" y2="228.4" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="215.4" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="1004.9" y1="224.7" x2="1004.9" y2="255.6" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="230.2" width="2.34" height="16.5" fill="var(--down)"/>
<line x1="1008.6" y1="244.2" x2="1008.6" y2="264.5" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="259.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1012.4" y1="229.1" x2="1012.4" y2="261.1" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="238.6" width="2.34" height="16.3" fill="var(--up)"/>
<line x1="1016.2" y1="227.6" x2="1016.2" y2="247.8" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="239.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1019.9" y1="238.4" x2="1019.9" y2="288.9" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="240.1" width="2.34" height="39.2" fill="var(--down)"/>
<line x1="1023.7" y1="261.8" x2="1023.7" y2="279.0" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="271.8" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="1027.5" y1="216.3" x2="1027.5" y2="282.3" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="235.1" width="2.34" height="38.4" fill="var(--up)"/>
<line x1="1031.3" y1="231.8" x2="1031.3" y2="254.2" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="232.4" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="1035.0" y1="227.6" x2="1035.0" y2="255.7" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="238.5" width="2.34" height="10.8" fill="var(--down)"/>
<line x1="1038.8" y1="212.7" x2="1038.8" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="220.5" width="2.34" height="20.9" fill="var(--up)"/>
<line x1="1042.6" y1="217.8" x2="1042.6" y2="242.0" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="221.0" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="1046.3" y1="198.8" x2="1046.3" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="216.8" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="1050.1" y1="214.0" x2="1050.1" y2="226.4" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="216.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="60" y1="203.8" x2="1052" y2="203.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="207.3" font-size="11.5" fill="var(--resistance)" font-weight="600">$56 R1</text>
<text x="1058" y="219.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="144.4" x2="1052" y2="144.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="147.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$62 R2</text>
<text x="1058" y="159.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="282.3" x2="1052" y2="282.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="276.3" font-size="11.5" fill="var(--support)" font-weight="600">$49 S1</text>
<text x="1058" y="288.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="393.2" x2="1052" y2="393.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="387.2" font-size="11.5" fill="var(--support)" font-weight="600">$38 S2</text>
<text x="1058" y="399.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="422.2" x2="1052" y2="422.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="416.2" font-size="11.5" fill="var(--support)" font-weight="600">$35 S3</text>
<text x="1058" y="428.2" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="216.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="208.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $55 (2026-08-27)</text>
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
| R2 | $62 | 2 | 2025-06-23·2025-12-01 주. 2026년 3월 고점으로 가는 길에 두 번 멈춘 자리이며, 터치 2회로 얇다 |
| R1 | $56 | 2 | 2025-02-17·2025-03-24 주. Equitrans 인수 이후 재평가가 처음 $50대 중반에 닿았던 구간이고, 현재가 바로 위다 |
| **현재가** | **$54.77** (2026-08-27 종가) | — | R1과 S1 사이 |
| S1 | $49 | 3 | 2025-09-15·2026-01-12·2026-07-06 주. **최근 1년의 저점대와 겹치는 유일한 레벨**로, 일봉 S3($49)과 같은 대역이다 |
| S2 | $38 | 2 | 2023-07-17·2023-09-25 주 — **Equitrans 인수(2024.07) 이전**, 순수 E&P였을 때의 가격대 |
| S3 | $35 | 3 | 2022-05-09·2023-12-11·2024-10-28 주 — 인수 전후에 걸쳐 있으나 셋 다 재평가가 시작되기 전이다 |
| 참고선 | $68 | — | 5년 최고(2026-03-23 주 장중 $68.24). 그 다음 주에 종가 −11.6%로 밀렸고 이후 넉 달간 회복하지 못했다 — 근시일 저항으로 보지 않는다 |
| 참고선 | $17.69 | — | 5년 최저이지만 **창의 첫 주(2021-08-23)** 값이다. 관측 창을 하루만 밀어도 사라지는 수준이라 구조적 저점으로 읽지 않는다 |

---

## 3. 관측된 특이 구간 — 2024-07-22 Equitrans Midstream 인수 완료

- 2024-07-22 Equitrans Midstream 재인수가 완료되면서 **보통주 152,427,848주가 신규 발행돼 주식수가 약 42% 늘었고**, 단일 세그먼트 E&P에서 Upstream/Gathering/Transmission 3개 세그먼트로 바뀌었다([역사 / 주요 이벤트](./02_history.md)·[최근 뉴스 / 이슈](./08_news.md) 아카이브).
- 시장은 이를 즉시 재평가로 받지 않았다 — 완료 주 종가는 $34.31(전주 $35.88 대비 **−4.4%**), 2주 뒤에는 장중 $30.02까지 밀렸다. 재평가는 그로부터 한 분기 뒤에 시작돼(2024-11-04 주 **+15.7%**) 2024년 말 $47.02, 2025년 6월 $58대까지 이어졌다.
- 그래서 이 표의 **S2 $38·S3 $35는 지금과 다른 자본구조·다른 사업범위의 회사가 거래되던 가격대다.** 주식수가 42% 늘었으므로 같은 시가총액이라도 주당 가격의 의미가 다르고, 미드스트림 수익이 없던 시절의 이익 기반이다 — 하방 목표로 인용하기 전에 [핵심 지표](./04_metrics.md) 상단 주의사항의 배수 단절 설명을 먼저 볼 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-23~2026-08-27. 수집 시점: 2026-08-28. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 일봉(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py EQT --name EQT --interval 1wk --event 2024-07-22:"Equitrans 인수 완료" --ref-line 68.24:"5년 최고" --ref-line 17.69:"5년 최저" --close-on 2026-08-27 --emit all` (기본 파라미터 그대로, `--force-level` 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨이 5개(저항 2 · 지지 3)뿐이고 저항 쪽은 둘 다 터치 2회다.** 3개를 억지로 채우지 않았다 — 현재가 위쪽에서 반복 확인된 가격대 자체가 얇다는 뜻이며, 그만큼 R1·R2의 신뢰도는 낮다.
    - **5년 창 안에서 회사의 사업 구조가 두 번 바뀌었다** — 2024-07 Equitrans 인수(수직통합·주식수 +42%), 2025-07 Olympus Energy 인수(보통주 25,229,166주 추가 발행). 3. 관측된 특이 구간대로 S2·S3는 현재 펀더멘털과 연결되지 않는다.
    - 이 구간에 주식분할·액면병합은 없었다. 위 두 인수는 주식 대가 지급이라 주식수를 늘렸지만 **가격 자체의 연속성을 깨는 이벤트는 아니므로 소급 조정 대상이 아니다**(분할과 달리 과거 주가를 되돌려 조정하지 않는다).
    - 5년 창의 시작점(2021-08, $17.69)은 헨리허브 가격이 본격적으로 오르기 전이다. **창의 시작·끝을 어디로 잡느냐에 따라 "5년 수익률"과 최저 레벨이 크게 달라진다** — 이 차트의 레벨은 창 밖으로 나가면 유효하지 않다.

---

*작성일: 2026-08-28*
