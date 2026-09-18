# 기술적 분석 (주봉 캔들차트 · 다년 구조)

> 최근 5년 주봉으로 여러 사이클에 걸친 구조적 지지/저항을 본다. 최근 1년 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: warning 이 차트에서 레벨이 하나만 잡힌 이유
5년 구간에서 **터치 2회 이상인 클러스터가 $140 하나뿐**이다. Coinbase 주가가 2021년 상장 후 $30대에서 $400대까지 10배 폭으로 움직여, ±2.5% 허용오차로는 스윙 포인트가 거의 묶이지 않기 때문이다. 스크립트가 현재가 행에 붙이는 "기간 내 상단 저항 없음(신고가 구간)" 라벨은 **"검출된 레벨이 전부 현재가 아래"라는 뜻이지 실제로 신고가라는 뜻이 아니다** — 5년 최고가는 현재가의 2배가 넘는다. 아래 표에서는 그 라벨을 쓰지 않고 실제 위치로 고쳐 적었다.

:::
::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 마지막 주봉 종가 **$173.97**(2026-09-17)은 [일봉 차트](./09_technical_daily.md)·[밸류에이션 / 적정주가](./06_valuation.md)와 **일치**한다.

:::
---

## 1. 차트 — 최근 5년 주봉 (2021-09-13 ~ 2026-09-17)

<style>
.coin-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .coin-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.coin-chart svg { width:100%; height:auto; display:block; }
.coin-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.coin-chart .title { fill: var(--ink); font-weight:600; }
.coin-chart .grid { stroke: var(--grid); stroke-width:1; }
.coin-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="coin-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Coinbase(COIN) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Coinbase (COIN) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-13 ~ 2026-09-17 · 마지막 종가 $173.97 (2026-09-17) · 단위 USD</text>
<line x1="60" y1="517.1" x2="1052" y2="517.1" class="grid"/>
<text x="52" y="521.1" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="389.0" x2="1052" y2="389.0" class="grid"/>
<text x="52" y="393.0" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="260.9" x2="1052" y2="260.9" class="grid"/>
<text x="52" y="264.9" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="132.9" x2="1052" y2="132.9" class="grid"/>
<text x="52" y="136.9" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="122.2" y1="56.0" x2="122.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="122.2" y1="626.0" x2="122.2" y2="631.0" class="axis"/>
<text x="122.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="318.4" y1="56.0" x2="318.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="318.4" y1="626.0" x2="318.4" y2="631.0" class="axis"/>
<text x="318.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="514.5" y1="56.0" x2="514.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="514.5" y1="626.0" x2="514.5" y2="631.0" class="axis"/>
<text x="514.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="714.4" y1="56.0" x2="714.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="714.4" y1="626.0" x2="714.4" y2="631.0" class="axis"/>
<text x="714.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="910.6" y1="56.0" x2="910.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="910.6" y1="626.0" x2="910.6" y2="631.0" class="axis"/>
<text x="910.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="330.6" x2="61.9" y2="339.4" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="331.1" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="65.7" y1="330.4" x2="65.7" y2="351.7" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="344.9" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="69.4" y1="343.2" x2="69.4" y2="357.0" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="348.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="73.2" y1="317.1" x2="73.2" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="327.4" width="2.34" height="21.3" fill="var(--up)"/>
<line x1="77.0" y1="284.4" x2="77.0" y2="332.0" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="285.8" width="2.34" height="39.8" fill="var(--up)"/>
<line x1="80.7" y1="238.7" x2="80.7" y2="297.4" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="259.9" width="2.34" height="32.2" fill="var(--up)"/>
<line x1="84.5" y1="224.5" x2="84.5" y2="254.4" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="236.1" width="2.34" height="16.2" fill="var(--up)"/>
<line x1="88.3" y1="202.2" x2="88.3" y2="230.3" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="213.5" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="92.1" y1="172.7" x2="92.1" y2="235.3" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="197.5" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="95.8" y1="190.2" x2="95.8" y2="231.0" stroke="var(--down)" class="wick"/>
<rect x="94.66" y="203.2" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="99.6" y1="215.0" x2="99.6" y2="262.0" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="218.3" width="2.34" height="38.6" fill="var(--down)"/>
<line x1="103.4" y1="220.3" x2="103.4" y2="314.5" stroke="var(--down)" class="wick"/>
<rect x="102.21" y="245.3" width="2.34" height="59.7" fill="var(--down)"/>
<line x1="107.1" y1="273.5" x2="107.1" y2="332.1" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="317.6" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="110.9" y1="301.6" x2="110.9" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="322.2" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="114.7" y1="300.3" x2="114.7" y2="348.3" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="301.7" width="2.34" height="40.5" fill="var(--up)"/>
<line x1="118.5" y1="284.0" x2="118.5" y2="323.2" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="299.0" width="2.34" height="22.9" fill="var(--down)"/>
<line x1="122.2" y1="310.1" x2="122.2" y2="357.2" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="317.0" width="2.34" height="30.7" fill="var(--down)"/>
<line x1="126.0" y1="329.8" x2="126.0" y2="370.3" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="350.6" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="129.8" y1="348.0" x2="129.8" y2="405.9" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="354.7" width="2.34" height="44.6" fill="var(--down)"/>
<line x1="133.6" y1="391.5" x2="133.6" y2="437.5" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="417.8" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="137.3" y1="387.2" x2="137.3" y2="421.0" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="396.2" width="2.34" height="21.2" fill="var(--up)"/>
<line x1="141.1" y1="366.6" x2="141.1" y2="400.5" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="390.7" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="144.9" y1="371.1" x2="144.9" y2="414.0" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="397.4" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="148.6" y1="407.3" x2="148.6" y2="445.5" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="413.5" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="152.4" y1="381.5" x2="152.4" y2="437.5" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="424.3" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="156.2" y1="412.8" x2="156.2" y2="444.7" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="429.7" width="2.34" height="10.5" fill="var(--down)"/>
<line x1="160.0" y1="406.1" x2="160.0" y2="452.9" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="407.0" width="2.34" height="33.2" fill="var(--up)"/>
<line x1="163.7" y1="394.5" x2="163.7" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="406.1" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="167.5" y1="380.3" x2="167.5" y2="409.0" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="397.6" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="171.3" y1="397.9" x2="171.3" y2="440.1" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="405.2" width="2.34" height="33.8" fill="var(--down)"/>
<line x1="175.0" y1="437.1" x2="175.0" y2="457.2" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="444.7" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="178.8" y1="446.7" x2="178.8" y2="477.1" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="458.9" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="182.6" y1="469.3" x2="182.6" y2="501.6" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="478.7" width="2.34" height="22.2" fill="var(--down)"/>
<line x1="186.4" y1="475.1" x2="186.4" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="500.4" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="190.1" y1="521.7" x2="190.1" y2="592.9" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="522.2" width="2.34" height="36.0" fill="var(--down)"/>
<line x1="193.9" y1="553.2" x2="193.9" y2="567.7" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="558.0" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="197.7" y1="546.4" x2="197.7" y2="569.5" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="548.7" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="201.4" y1="538.5" x2="201.4" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="542.7" width="2.34" height="17.0" fill="var(--down)"/>
<line x1="205.2" y1="550.3" x2="205.2" y2="571.2" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="554.6" width="2.34" height="15.4" fill="var(--down)"/>
<line x1="209.0" y1="572.6" x2="209.0" y2="586.3" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="579.6" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="212.8" y1="563.1" x2="212.8" y2="579.2" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="564.9" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="216.5" y1="567.8" x2="216.5" y2="588.7" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="568.9" width="2.34" height="13.5" fill="var(--down)"/>
<line x1="220.3" y1="563.6" x2="220.3" y2="586.4" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="568.0" width="2.34" height="15.6" fill="var(--up)"/>
<line x1="224.1" y1="570.4" x2="224.1" y2="580.7" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="571.5" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="227.8" y1="544.0" x2="227.8" y2="572.6" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="554.5" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="231.6" y1="555.6" x2="231.6" y2="577.8" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="556.9" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="235.4" y1="496.2" x2="235.4" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="526.0" width="2.34" height="40.8" fill="var(--up)"/>
<line x1="239.2" y1="512.6" x2="239.2" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="519.9" width="2.34" height="9.4" fill="var(--down)"/>
<line x1="242.9" y1="522.9" x2="242.9" y2="550.4" stroke="var(--down)" class="wick"/>
<rect x="241.77" y="531.1" width="2.34" height="19.3" fill="var(--down)"/>
<line x1="246.7" y1="547.3" x2="246.7" y2="561.5" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="554.4" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="250.5" y1="555.1" x2="250.5" y2="565.9" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="561.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="254.3" y1="541.4" x2="254.3" y2="566.0" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="541.6" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="258.0" y1="536.9" x2="258.0" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="539.4" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="261.8" y1="552.3" x2="261.8" y2="569.1" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="553.1" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="265.6" y1="558.4" x2="265.6" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="562.6" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="269.3" y1="547.5" x2="269.3" y2="565.9" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="559.4" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="273.1" y1="550.7" x2="273.1" y2="567.0" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="558.7" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="276.9" y1="550.6" x2="276.9" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="560.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="280.7" y1="544.9" x2="280.7" y2="563.6" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="552.9" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="284.4" y1="549.6" x2="284.4" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="552.5" width="2.34" height="17.4" fill="var(--down)"/>
<line x1="288.2" y1="567.1" x2="288.2" y2="588.1" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="568.4" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="292.0" y1="570.9" x2="292.0" y2="588.5" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="573.9" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="295.7" y1="586.1" x2="295.7" y2="593.2" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="588.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="299.5" y1="584.1" x2="299.5" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="584.2" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="303.3" y1="581.4" x2="303.3" y2="593.8" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="583.8" width="2.34" height="9.9" fill="var(--down)"/>
<line x1="307.1" y1="585.9" x2="307.1" y2="600.8" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="594.0" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="310.8" y1="598.0" x2="310.8" y2="603.0" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="599.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="314.6" y1="599.3" x2="314.6" y2="604.4" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="599.9" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="318.4" y1="595.9" x2="318.4" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="598.5" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="322.1" y1="580.4" x2="322.1" y2="600.7" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="581.2" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="325.9" y1="571.8" x2="325.9" y2="583.8" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="574.6" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="329.7" y1="565.4" x2="329.7" y2="581.7" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="566.6" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="333.5" y1="533.0" x2="333.5" y2="573.9" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="549.6" width="2.34" height="18.7" fill="var(--up)"/>
<line x1="337.2" y1="547.9" x2="337.2" y2="573.5" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="551.5" width="2.34" height="20.6" fill="var(--down)"/>
<line x1="341.0" y1="551.3" x2="341.0" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="561.7" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="344.8" y1="558.8" x2="344.8" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="564.1" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="348.5" y1="558.8" x2="348.5" y2="571.6" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="562.6" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="352.3" y1="555.8" x2="352.3" y2="579.2" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="562.5" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="356.1" y1="546.8" x2="356.1" y2="580.2" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="549.2" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="359.9" y1="535.9" x2="359.9" y2="566.4" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="546.9" width="2.34" height="11.4" fill="var(--down)"/>
<line x1="363.6" y1="557.3" x2="363.6" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="558.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="367.4" y1="557.7" x2="367.4" y2="570.7" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="560.7" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="371.2" y1="552.2" x2="371.2" y2="568.8" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="555.7" width="2.34" height="10.9" fill="var(--up)"/>
<line x1="375.0" y1="553.3" x2="375.0" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="373.78" y="559.2" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="378.7" y1="569.0" x2="378.7" y2="578.4" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="569.7" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="382.5" y1="570.2" x2="382.5" y2="584.2" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="570.6" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="386.3" y1="563.6" x2="386.3" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="571.8" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="390.0" y1="566.2" x2="390.0" y2="572.7" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="570.4" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="393.8" y1="564.2" x2="393.8" y2="573.6" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="572.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="397.6" y1="560.2" x2="397.6" y2="569.4" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="562.5" width="2.34" height="5.7" fill="var(--up)"/>
<line x1="401.4" y1="562.7" x2="401.4" y2="585.7" stroke="var(--down)" class="wick"/>
<rect x="400.18" y="564.0" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="405.1" y1="573.1" x2="405.1" y2="581.0" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="574.0" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="408.9" y1="565.9" x2="408.9" y2="576.5" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="566.5" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="412.7" y1="549.2" x2="412.7" y2="567.1" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="553.6" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="416.4" y1="541.2" x2="416.4" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="544.4" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="420.2" y1="498.6" x2="420.2" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="510.3" width="2.34" height="33.6" fill="var(--up)"/>
<line x1="424.0" y1="501.9" x2="424.0" y2="518.8" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="511.3" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="427.8" y1="513.6" x2="427.8" y2="527.6" stroke="var(--down)" class="wick"/>
<rect x="426.59" y="518.1" width="2.34" height="5.7" fill="var(--down)"/>
<line x1="431.5" y1="516.9" x2="431.5" y2="534.2" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="523.8" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="435.3" y1="531.2" x2="435.3" y2="542.1" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="533.5" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="439.1" y1="538.8" x2="439.1" y2="552.7" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="542.7" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="442.8" y1="545.1" x2="442.8" y2="552.9" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="550.1" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="446.6" y1="534.4" x2="446.6" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="545.3" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="450.4" y1="539.3" x2="450.4" y2="548.6" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="540.1" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="454.2" y1="534.6" x2="454.2" y2="545.6" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="540.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="457.9" y1="537.2" x2="457.9" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="537.9" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="461.7" y1="545.9" x2="461.7" y2="556.0" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="549.0" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="465.5" y1="542.8" x2="465.5" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="544.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="469.2" y1="540.1" x2="469.2" y2="552.9" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="547.2" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="473.0" y1="543.6" x2="473.0" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="545.8" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="476.8" y1="530.7" x2="476.8" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="548.5" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="480.6" y1="532.1" x2="480.6" y2="553.1" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="535.3" width="2.34" height="17.6" fill="var(--up)"/>
<line x1="484.3" y1="517.4" x2="484.3" y2="537.5" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="526.2" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="488.1" y1="516.9" x2="488.1" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="518.3" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="491.9" y1="495.4" x2="491.9" y2="517.1" stroke="var(--up)" class="wick"/>
<rect x="490.71" y="497.2" width="2.34" height="19.0" fill="var(--up)"/>
<line x1="495.7" y1="473.2" x2="495.7" y2="501.5" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="473.9" width="2.34" height="27.1" fill="var(--up)"/>
<line x1="499.4" y1="455.8" x2="499.4" y2="478.5" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="457.4" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="503.2" y1="447.0" x2="503.2" y2="471.0" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="455.8" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="507.0" y1="416.3" x2="507.0" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="420.4" width="2.34" height="39.3" fill="var(--up)"/>
<line x1="510.7" y1="405.2" x2="510.7" y2="428.7" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="421.3" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="514.5" y1="420.3" x2="514.5" y2="460.6" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="423.6" width="2.34" height="24.4" fill="var(--down)"/>
<line x1="518.3" y1="438.5" x2="518.3" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="443.1" width="2.34" height="34.6" fill="var(--down)"/>
<line x1="522.1" y1="469.3" x2="522.1" y2="494.0" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="479.4" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="525.8" y1="476.4" x2="525.8" y2="492.9" stroke="var(--up)" class="wick"/>
<rect x="524.66" y="484.8" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="529.6" y1="469.9" x2="529.6" y2="486.1" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="479.7" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="533.4" y1="460.1" x2="533.4" y2="498.5" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="463.3" width="2.34" height="17.0" fill="var(--up)"/>
<line x1="537.1" y1="397.2" x2="537.1" y2="469.6" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="414.3" width="2.34" height="50.2" fill="var(--up)"/>
<line x1="540.9" y1="413.0" x2="540.9" y2="439.4" stroke="var(--down)" class="wick"/>
<rect x="539.74" y="414.8" width="2.34" height="17.8" fill="var(--down)"/>
<line x1="544.7" y1="373.4" x2="544.7" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="381.6" width="2.34" height="47.5" fill="var(--up)"/>
<line x1="548.5" y1="298.7" x2="548.5" y2="373.3" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="316.5" width="2.34" height="50.2" fill="var(--up)"/>
<line x1="552.2" y1="297.3" x2="552.2" y2="359.8" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="299.3" width="2.34" height="35.5" fill="var(--down)"/>
<line x1="556.0" y1="291.2" x2="556.0" y2="368.3" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="317.9" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="559.8" y1="282.1" x2="559.8" y2="319.9" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="305.6" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="563.5" y1="300.9" x2="563.5" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="309.8" width="2.34" height="26.9" fill="var(--down)"/>
<line x1="567.3" y1="306.7" x2="567.3" y2="345.3" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="321.3" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="571.1" y1="325.3" x2="571.1" y2="381.8" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="327.6" width="2.34" height="47.3" fill="var(--down)"/>
<line x1="574.9" y1="339.1" x2="574.9" y2="371.6" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="342.5" width="2.34" height="25.0" fill="var(--up)"/>
<line x1="578.6" y1="347.1" x2="578.6" y2="391.3" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="350.7" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="582.4" y1="343.2" x2="582.4" y2="388.4" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="355.9" width="2.34" height="31.9" fill="var(--down)"/>
<line x1="586.2" y1="361.6" x2="586.2" y2="395.5" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="379.3" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="589.9" y1="339.4" x2="589.9" y2="384.3" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="340.8" width="2.34" height="38.0" fill="var(--up)"/>
<line x1="593.7" y1="326.4" x2="593.7" y2="364.5" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="343.6" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="597.5" y1="307.3" x2="597.5" y2="357.4" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="332.5" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="601.3" y1="308.0" x2="601.3" y2="345.4" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="332.0" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="605.0" y1="326.7" x2="605.0" y2="362.5" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="338.0" width="2.34" height="17.9" fill="var(--down)"/>
<line x1="608.8" y1="356.0" x2="608.8" y2="379.2" stroke="var(--up)" class="wick"/>
<rect x="607.64" y="360.6" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="612.6" y1="342.9" x2="612.6" y2="376.9" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="355.7" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="616.3" y1="354.3" x2="616.3" y2="371.7" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="355.1" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="620.1" y1="312.4" x2="620.1" y2="353.2" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="315.0" width="2.34" height="36.4" fill="var(--up)"/>
<line x1="623.9" y1="296.1" x2="623.9" y2="355.3" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="311.6" width="2.34" height="22.5" fill="var(--down)"/>
<line x1="627.7" y1="318.0" x2="627.7" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="323.0" width="2.34" height="60.3" fill="var(--down)"/>
<line x1="631.4" y1="389.1" x2="631.4" y2="438.8" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="393.8" width="2.34" height="43.9" fill="var(--up)"/>
<line x1="635.2" y1="381.4" x2="635.2" y2="404.0" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="382.2" width="2.34" height="14.1" fill="var(--up)"/>
<line x1="639.0" y1="373.8" x2="639.0" y2="400.3" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="374.4" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="642.8" y1="375.1" x2="642.8" y2="414.6" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="377.1" width="2.34" height="33.2" fill="var(--down)"/>
<line x1="646.5" y1="411.2" x2="646.5" y2="458.0" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="412.1" width="2.34" height="44.4" fill="var(--down)"/>
<line x1="650.3" y1="428.8" x2="650.3" y2="453.7" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="436.4" width="2.34" height="15.1" fill="var(--up)"/>
<line x1="654.1" y1="420.6" x2="654.1" y2="445.5" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="427.3" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="657.8" y1="398.7" x2="657.8" y2="435.4" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="400.3" width="2.34" height="25.5" fill="var(--up)"/>
<line x1="661.6" y1="407.7" x2="661.6" y2="440.3" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="409.3" width="2.34" height="17.0" fill="var(--down)"/>
<line x1="665.4" y1="415.7" x2="665.4" y2="437.9" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="419.3" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="669.2" y1="363.1" x2="669.2" y2="416.9" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="363.1" width="2.34" height="50.0" fill="var(--up)"/>
<line x1="672.9" y1="367.4" x2="672.9" y2="396.0" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="369.3" width="2.34" height="13.3" fill="var(--down)"/>
<line x1="676.7" y1="358.4" x2="676.7" y2="416.2" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="371.9" width="2.34" height="39.0" fill="var(--down)"/>
<line x1="680.5" y1="294.9" x2="680.5" y2="419.3" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="298.4" width="2.34" height="116.1" fill="var(--up)"/>
<line x1="684.2" y1="216.3" x2="684.2" y2="293.9" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="253.5" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="688.0" y1="207.5" x2="688.0" y2="275.7" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="255.0" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="691.8" y1="238.6" x2="691.8" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="249.4" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="695.6" y1="197.2" x2="695.6" y2="265.2" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="205.1" width="2.34" height="53.3" fill="var(--up)"/>
<line x1="699.3" y1="209.5" x2="699.3" y2="262.8" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="209.8" width="2.34" height="37.6" fill="var(--down)"/>
<line x1="703.1" y1="227.3" x2="703.1" y2="309.8" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="239.3" width="2.34" height="48.9" fill="var(--down)"/>
<line x1="706.9" y1="281.4" x2="706.9" y2="308.2" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="293.6" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="710.6" y1="297.3" x2="710.6" y2="329.6" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="298.5" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="714.4" y1="269.1" x2="714.4" y2="327.5" stroke="var(--down)" class="wick"/>
<rect x="713.25" y="287.8" width="2.34" height="26.0" fill="var(--down)"/>
<line x1="718.2" y1="260.5" x2="718.2" y2="336.8" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="266.7" width="2.34" height="62.1" fill="var(--up)"/>
<line x1="722.0" y1="247.4" x2="722.0" y2="294.7" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="262.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="725.7" y1="253.3" x2="725.7" y2="305.5" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="272.0" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="729.5" y1="274.5" x2="729.5" y2="300.7" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="293.6" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="733.3" y1="257.9" x2="733.3" y2="307.7" stroke="var(--down)" class="wick"/>
<rect x="732.11" y="286.0" width="2.34" height="7.8" fill="var(--down)"/>
<line x1="737.0" y1="287.6" x2="737.0" y2="344.5" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="288.1" width="2.34" height="55.6" fill="var(--down)"/>
<line x1="740.8" y1="337.5" x2="740.8" y2="387.6" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="338.9" width="2.34" height="30.1" fill="var(--down)"/>
<line x1="744.6" y1="346.3" x2="744.6" y2="397.9" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="347.8" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="748.4" y1="380.3" x2="748.4" y2="418.7" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="382.5" width="2.34" height="28.1" fill="var(--down)"/>
<line x1="752.1" y1="396.8" x2="752.1" y2="416.2" stroke="var(--up)" class="wick"/>
<rect x="750.97" y="402.0" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="755.9" y1="380.2" x2="755.9" y2="423.6" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="392.2" width="2.34" height="30.2" fill="var(--down)"/>
<line x1="759.7" y1="409.4" x2="759.7" y2="456.7" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="428.3" width="2.34" height="11.3" fill="var(--down)"/>
<line x1="763.5" y1="409.7" x2="763.5" y2="462.6" stroke="var(--up)" class="wick"/>
<rect x="762.28" y="420.4" width="2.34" height="37.7" fill="var(--up)"/>
<line x1="767.2" y1="411.6" x2="767.2" y2="429.4" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="414.0" width="2.34" height="7.0" fill="var(--down)"/>
<line x1="771.0" y1="374.1" x2="771.0" y2="425.7" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="376.7" width="2.34" height="44.2" fill="var(--up)"/>
<line x1="774.8" y1="377.5" x2="774.8" y2="394.7" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="378.5" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="778.5" y1="370.9" x2="778.5" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="777.37" y="386.8" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="782.3" y1="298.8" x2="782.3" y2="381.8" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="303.9" width="2.34" height="73.7" fill="var(--up)"/>
<line x1="786.1" y1="290.4" x2="786.1" y2="315.7" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="308.1" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="789.9" y1="299.2" x2="789.9" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="300.6" width="2.34" height="28.7" fill="var(--down)"/>
<line x1="793.6" y1="304.9" x2="793.6" y2="337.7" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="323.4" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="797.4" y1="309.1" x2="797.4" y2="343.8" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="317.7" width="2.34" height="16.6" fill="var(--down)"/>
<line x1="801.2" y1="247.2" x2="801.2" y2="331.0" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="250.2" width="2.34" height="77.6" fill="var(--up)"/>
<line x1="804.9" y1="155.9" x2="804.9" y2="267.9" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="192.5" width="2.34" height="65.8" fill="var(--up)"/>
<line x1="808.7" y1="183.5" x2="808.7" y2="217.4" stroke="var(--down)" class="wick"/>
<rect x="807.55" y="185.1" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="812.5" y1="138.6" x2="812.5" y2="199.5" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="149.4" width="2.34" height="42.1" fill="var(--up)"/>
<line x1="816.3" y1="75.7" x2="816.3" y2="167.4" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="107.5" width="2.34" height="34.9" fill="var(--up)"/>
<line x1="820.0" y1="86.3" x2="820.0" y2="150.3" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="100.1" width="2.34" height="43.4" fill="var(--down)"/>
<line x1="823.8" y1="138.8" x2="823.8" y2="247.4" stroke="var(--down)" class="wick"/>
<rect x="822.63" y="139.7" width="2.34" height="102.4" fill="var(--down)"/>
<line x1="827.6" y1="230.2" x2="827.6" y2="269.5" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="235.9" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="831.3" y1="202.8" x2="831.3" y2="242.8" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="232.6" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="835.1" y1="229.8" x2="835.1" y2="271.9" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="235.5" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="838.9" y1="240.5" x2="838.9" y2="260.5" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="245.3" width="2.34" height="9.8" fill="var(--down)"/>
<line x1="842.7" y1="240.8" x2="842.7" y2="270.5" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="261.0" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="846.4" y1="223.2" x2="846.4" y2="264.6" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="231.4" width="2.34" height="27.1" fill="var(--up)"/>
<line x1="850.2" y1="194.5" x2="850.2" y2="246.5" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="206.6" width="2.34" height="25.1" fill="var(--up)"/>
<line x1="854.0" y1="214.6" x2="854.0" y2="256.6" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="218.1" width="2.34" height="26.7" fill="var(--down)"/>
<line x1="857.7" y1="154.0" x2="857.7" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="158.4" width="2.34" height="79.4" fill="var(--up)"/>
<line x1="861.5" y1="130.1" x2="861.5" y2="194.8" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="145.2" width="2.34" height="42.7" fill="var(--down)"/>
<line x1="865.3" y1="177.8" x2="865.3" y2="238.2" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="180.0" width="2.34" height="34.8" fill="var(--down)"/>
<line x1="869.1" y1="188.1" x2="869.1" y2="247.5" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="191.2" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="872.8" y1="167.1" x2="872.8" y2="224.8" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="180.5" width="2.34" height="24.4" fill="var(--down)"/>
<line x1="876.6" y1="206.1" x2="876.6" y2="281.9" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="208.6" width="2.34" height="40.6" fill="var(--down)"/>
<line x1="880.4" y1="229.2" x2="880.4" y2="301.7" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="231.5" width="2.34" height="50.0" fill="var(--down)"/>
<line x1="884.2" y1="289.3" x2="884.2" y2="349.1" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="293.1" width="2.34" height="44.2" fill="var(--down)"/>
<line x1="887.9" y1="286.7" x2="887.9" y2="336.8" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="295.8" width="2.34" height="36.0" fill="var(--up)"/>
<line x1="891.7" y1="281.1" x2="891.7" y2="322.2" stroke="var(--up)" class="wick"/>
<rect x="890.53" y="299.7" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="895.5" y1="280.5" x2="895.5" y2="313.8" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="295.8" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="899.2" y1="301.2" x2="899.2" y2="339.0" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="301.9" width="2.34" height="29.3" fill="var(--down)"/>
<line x1="903.0" y1="318.8" x2="903.0" y2="347.0" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="322.8" width="2.34" height="18.9" fill="var(--down)"/>
<line x1="906.8" y1="337.9" x2="906.8" y2="356.4" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="342.2" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="910.6" y1="313.6" x2="910.6" y2="341.4" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="328.7" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="914.3" y1="308.2" x2="914.3" y2="342.7" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="336.3" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="918.1" y1="344.3" x2="918.1" y2="368.9" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="347.2" width="2.34" height="20.1" fill="var(--down)"/>
<line x1="921.9" y1="369.0" x2="921.9" y2="400.6" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="373.4" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="925.6" y1="400.6" x2="925.6" y2="459.3" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="402.1" width="2.34" height="31.6" fill="var(--down)"/>
<line x1="929.4" y1="430.1" x2="929.4" y2="466.7" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="434.7" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="933.2" y1="420.4" x2="933.2" y2="442.3" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="425.7" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="937.0" y1="406.5" x2="937.0" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="420.0" width="2.34" height="12.4" fill="var(--up)"/>
<line x1="940.7" y1="371.7" x2="940.7" y2="424.8" stroke="var(--up)" class="wick"/>
<rect x="939.56" y="392.6" width="2.34" height="31.7" fill="var(--up)"/>
<line x1="944.5" y1="379.9" x2="944.5" y2="398.7" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="391.6" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="948.3" y1="371.8" x2="948.3" y2="399.4" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="386.7" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="952.0" y1="384.0" x2="952.0" y2="440.5" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="390.8" width="2.34" height="48.0" fill="var(--down)"/>
<line x1="955.8" y1="415.5" x2="955.8" y2="442.2" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="425.6" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="959.6" y1="402.4" x2="959.6" y2="436.3" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="420.9" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="963.4" y1="368.5" x2="963.4" y2="434.7" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="380.9" width="2.34" height="53.2" fill="var(--up)"/>
<line x1="967.1" y1="373.3" x2="967.1" y2="396.8" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="387.7" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="970.9" y1="383.3" x2="970.9" y2="417.7" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="390.2" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="974.7" y1="377.7" x2="974.7" y2="411.1" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="387.5" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="978.4" y1="360.4" x2="978.4" y2="398.9" stroke="var(--down)" class="wick"/>
<rect x="977.28" y="388.5" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="982.2" y1="393.4" x2="982.2" y2="409.3" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="401.5" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="986.0" y1="399.5" x2="986.0" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="403.1" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="989.8" y1="406.2" x2="989.8" y2="455.8" stroke="var(--down)" class="wick"/>
<rect x="988.59" y="415.7" width="2.34" height="34.3" fill="var(--down)"/>
<line x1="993.5" y1="433.2" x2="993.5" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="440.6" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="997.3" y1="421.8" x2="997.3" y2="439.6" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="427.5" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="1001.1" y1="419.2" x2="1001.1" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="433.9" width="2.34" height="20.4" fill="var(--down)"/>
<line x1="1004.9" y1="423.5" x2="1004.9" y2="462.9" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="433.3" width="2.34" height="18.8" fill="var(--up)"/>
<line x1="1008.6" y1="425.3" x2="1008.6" y2="447.0" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="438.5" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="1012.4" y1="429.4" x2="1012.4" y2="449.8" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="444.0" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="1016.2" y1="412.7" x2="1016.2" y2="448.2" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="442.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1019.9" y1="427.9" x2="1019.9" y2="467.0" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="436.0" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="1023.7" y1="446.2" x2="1023.7" y2="464.6" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="448.5" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="1027.5" y1="447.4" x2="1027.5" y2="457.8" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="448.8" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="1031.3" y1="400.1" x2="1031.3" y2="458.2" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="406.3" width="2.34" height="48.8" fill="var(--up)"/>
<line x1="1035.0" y1="397.0" x2="1035.0" y2="421.4" stroke="var(--down)" class="wick"/>
<rect x="1033.86" y="403.4" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="1038.8" y1="394.3" x2="1038.8" y2="424.9" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="408.7" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="1042.6" y1="408.3" x2="1042.6" y2="427.0" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="413.8" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="1046.3" y1="397.7" x2="1046.3" y2="438.8" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="413.6" width="2.34" height="8.8" fill="var(--down)"/>
<line x1="1050.1" y1="422.1" x2="1050.1" y2="432.9" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="422.4" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="60" y1="465.8" x2="1052" y2="465.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="459.8" font-size="11.5" fill="var(--support)" font-weight="600">$140 S1</text>
<text x="1058" y="471.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="422.4" r="3" fill="var(--ink)"/>
<text x="1046.0" y="414.4" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $174 (2026-09-17)</text>
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
| **현재가** | **$173.97** (2026-09-17 종가) | — | 검출된 유일한 레벨 S1($140)보다 24% 위. **위쪽에 검출된 저항이 없는 것은 신고가여서가 아니라 5년 구간의 가격 분산이 너무 커 클러스터가 만들어지지 않았기 때문**이다(위 경고 블록 참고) |
| S1 | $140 | 4 | 2025-04-07·2026-02-09·2026-06-22·2026-07-27 — **1년 반에 걸쳐 네 번 지지된 구간**이며, 최근 1년 최저($139.11)도 여기다. 이 표에서 유일하게 통계적 의미가 있는 레벨 |

**이 표에서 읽을 것은 하나다** — $140은 서로 다른 시기(2025년 4월 / 2026년 2·6·7월)에 네 번 확인된 구간이고, 2026년 들어서만 세 번 시험받았다. 반대로 상단은 이 모델이 아무것도 말해주지 않으므로 [일봉 차트](./09_technical_daily.md)의 R1~R3을 함께 봐야 한다.

---

## 3. 관측된 특이 구간 — 2021년 이후 세 국면

- **2021.11~2022.12 — 첫 사이클 붕괴**: 상장 첫해 고점(2021년 11월 $357 부근)에서 2022년 말 $32 수준까지 약 91% 하락했다. FTX 파산과 크립토 겨울이 겹친 구간이며, **이 구간의 가격대는 현재와 자릿수가 달라 지지/저항 클러스터링에 사실상 기여하지 않는다.**
- **2023~2024 — 회복과 제도화**: 현물 비트코인 ETF 승인(2024년 1월)을 전후로 $100대를 회복했고, 2024년 말 $300대까지 올랐다.
- **2025.02~2026.09 — 고점 이후 하락**: SEC 소송 취하(2025-02)·S&P500 편입(2025-05)이라는 호재가 나온 뒤 오히려 고점을 찍고, 2026년 들어 $402 → $139까지 65% 하락했다. **회사에 관한 호재가 정점에서 나왔고 그 뒤 크립토 시장 자체가 축소된 구간**이며, [핵심 지표](./04_metrics.md) C절의 고객 예치자산 반토막과 시기가 겹친다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-09-13~2026-09-17. 수집 시점: 2026-09-18. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py COIN --name Coinbase --interval 1wk --close-on 2026-09-17` (옵션 기본값 그대로)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨이 1개뿐이라는 것 자체가 이 차트의 가장 큰 한계다.** 5년간 주가가 $32~$402로 12배 폭을 움직여 ±2.5% 고정 허용오차로는 서로 먼 시기의 스윙이 묶이지 않는다. `--levels`를 올려도 해결되지 않는다 — 제약은 개수 상한이 아니라 **터치 2회 이상 조건**이기 때문이다. 이 파라미터는 회사 간 비교를 위해 고정돼 있으므로 바꾸지 않았다(변경 시 다른 회사 문서를 전부 재생성해야 한다).
    - 위 한계 때문에 이 문서는 **"$140이 반복 확인된 바닥"이라는 사실 하나만** 신뢰하고, 상단 구조는 [일봉 차트](./09_technical_daily.md)에 맡긴다.
    - 해당 기간에 주식분할·병합은 없었다(2019.05 6:1 분할은 상장 전).

---

*작성일: 2026-09-18*
