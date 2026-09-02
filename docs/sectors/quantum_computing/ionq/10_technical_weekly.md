# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-02 종가 $37.64는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)의 값과 일치한다. 상장 이후 주식분할이 없어 원주가와 수정주가가 같다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-09-02)

<div class="ionq-chart">
<style>
.ionq-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ionq-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ionq-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ionq-chart svg { width:100%; height:auto; display:block; }
.ionq-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ionq-chart .title { fill: var(--ink); font-weight:600; }
.ionq-chart .grid { stroke: var(--grid); stroke-width:1; }
.ionq-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="IonQ(IONQ) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">IonQ (IONQ) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-09-02 · 마지막 종가 $37.64 (2026-09-02) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="496.5" x2="1052" y2="496.5" class="grid"/>
<text x="52" y="500.5" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="366.9" x2="1052" y2="366.9" class="grid"/>
<text x="52" y="370.9" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="237.4" x2="1052" y2="237.4" class="grid"/>
<text x="52" y="241.4" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="107.8" x2="1052" y2="107.8" class="grid"/>
<text x="52" y="111.8" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="129.8" y1="56.0" x2="129.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="129.8" y1="626.0" x2="129.8" y2="631.0" class="axis"/>
<text x="129.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="325.9" y1="56.0" x2="325.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="325.9" y1="626.0" x2="325.9" y2="631.0" class="axis"/>
<text x="325.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="522.1" y1="56.0" x2="522.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="522.1" y1="626.0" x2="522.1" y2="631.0" class="axis"/>
<text x="522.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="722.0" y1="56.0" x2="722.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="722.0" y1="626.0" x2="722.0" y2="631.0" class="axis"/>
<text x="722.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="918.1" y1="56.0" x2="918.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="918.1" y1="626.0" x2="918.1" y2="631.0" class="axis"/>
<text x="918.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="561.2" x2="61.9" y2="561.5" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="561.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="560.6" x2="65.7" y2="561.4" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="561.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="69.4" y1="558.2" x2="69.4" y2="561.3" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="560.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="73.2" y1="551.7" x2="73.2" y2="561.4" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="552.8" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="77.0" y1="542.1" x2="77.0" y2="572.0" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="551.8" width="2.34" height="14.6" fill="var(--down)"/>
<line x1="80.7" y1="564.5" x2="80.7" y2="580.2" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="565.1" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="84.5" y1="558.0" x2="84.5" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="560.9" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="88.3" y1="549.1" x2="88.3" y2="565.2" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="560.9" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="92.1" y1="522.2" x2="92.1" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="528.6" width="2.34" height="35.2" fill="var(--up)"/>
<line x1="95.8" y1="500.4" x2="95.8" y2="534.0" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="501.2" width="2.34" height="22.0" fill="var(--up)"/>
<line x1="99.6" y1="476.1" x2="99.6" y2="515.8" stroke="var(--down)" class="wick"/>
<rect x="98.44" y="487.1" width="2.34" height="8.4" fill="var(--down)"/>
<line x1="103.4" y1="393.5" x2="103.4" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="444.6" width="2.34" height="47.4" fill="var(--up)"/>
<line x1="107.1" y1="446.1" x2="107.1" y2="486.1" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="450.4" width="2.34" height="19.0" fill="var(--down)"/>
<line x1="110.9" y1="458.6" x2="110.9" y2="506.2" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="464.1" width="2.34" height="40.3" fill="var(--down)"/>
<line x1="114.7" y1="481.4" x2="114.7" y2="514.6" stroke="var(--up)" class="wick"/>
<rect x="113.52" y="505.7" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="118.5" y1="501.4" x2="118.5" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="505.7" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="122.2" y1="507.5" x2="122.2" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="510.3" width="2.34" height="10.1" fill="var(--up)"/>
<line x1="126.0" y1="503.9" x2="126.0" y2="521.5" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="506.2" width="2.34" height="11.7" fill="var(--down)"/>
<line x1="129.8" y1="510.3" x2="129.8" y2="534.6" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="515.4" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="133.6" y1="528.7" x2="133.6" y2="544.3" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="536.9" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="137.3" y1="543.0" x2="137.3" y2="556.2" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="545.5" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="141.1" y1="550.8" x2="141.1" y2="566.7" stroke="var(--down)" class="wick"/>
<rect x="139.93" y="559.3" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="144.9" y1="541.8" x2="144.9" y2="561.2" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="542.4" width="2.34" height="18.2" fill="var(--up)"/>
<line x1="148.6" y1="514.4" x2="148.6" y2="544.8" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="517.1" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="152.4" y1="511.6" x2="152.4" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="521.4" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="156.2" y1="524.2" x2="156.2" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="155.01" y="528.2" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="160.0" y1="518.7" x2="160.0" y2="547.1" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="527.0" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="163.7" y1="541.8" x2="163.7" y2="551.4" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="545.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="167.5" y1="533.0" x2="167.5" y2="553.3" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="533.0" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="171.3" y1="526.0" x2="171.3" y2="542.1" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="532.1" width="2.34" height="8.5" fill="var(--down)"/>
<line x1="175.0" y1="538.1" x2="175.0" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="540.2" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="178.8" y1="536.9" x2="178.8" y2="550.0" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="541.8" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="182.6" y1="549.2" x2="182.6" y2="557.1" stroke="var(--down)" class="wick"/>
<rect x="181.42" y="549.2" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="186.4" y1="554.6" x2="186.4" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="555.9" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="190.1" y1="565.4" x2="190.1" y2="575.7" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="567.5" width="2.34" height="7.5" fill="var(--down)"/>
<line x1="193.9" y1="573.5" x2="193.9" y2="589.3" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="575.0" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="197.7" y1="588.2" x2="197.7" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="588.8" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="201.4" y1="584.9" x2="201.4" y2="594.8" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="589.5" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="205.2" y1="586.4" x2="205.2" y2="591.8" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="587.6" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="209.0" y1="586.4" x2="209.0" y2="592.2" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="586.9" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="212.8" y1="586.9" x2="212.8" y2="594.3" stroke="var(--down)" class="wick"/>
<rect x="211.59" y="588.8" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="216.5" y1="592.8" x2="216.5" y2="597.6" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="593.4" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="220.3" y1="590.6" x2="220.3" y2="594.6" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="592.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="224.1" y1="591.8" x2="224.1" y2="598.7" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="592.3" width="2.34" height="5.3" fill="var(--down)"/>
<line x1="227.8" y1="592.8" x2="227.8" y2="598.7" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="593.2" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="231.6" y1="593.6" x2="231.6" y2="598.2" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="593.9" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="235.4" y1="591.9" x2="235.4" y2="596.5" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="594.4" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="239.2" y1="591.0" x2="239.2" y2="595.8" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="591.0" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="242.9" y1="584.3" x2="242.9" y2="592.6" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="584.4" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="246.7" y1="582.9" x2="246.7" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="245.54" y="583.8" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="250.5" y1="570.2" x2="250.5" y2="585.9" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="583.1" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="254.3" y1="579.9" x2="254.3" y2="586.2" stroke="var(--down)" class="wick"/>
<rect x="253.08" y="584.4" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="258.0" y1="584.8" x2="258.0" y2="589.8" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="587.1" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="261.8" y1="588.4" x2="261.8" y2="593.0" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="588.5" width="2.34" height="2.6" fill="var(--down)"/>
<line x1="265.6" y1="587.3" x2="265.6" y2="591.0" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="590.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="269.3" y1="590.2" x2="269.3" y2="595.9" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="591.0" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="273.1" y1="590.4" x2="273.1" y2="595.8" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="593.2" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="276.9" y1="587.3" x2="276.9" y2="593.8" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="591.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="280.7" y1="591.4" x2="280.7" y2="596.7" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="591.5" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="284.4" y1="591.1" x2="284.4" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="592.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="288.2" y1="588.8" x2="288.2" y2="594.1" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="589.1" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="292.0" y1="586.6" x2="292.0" y2="593.5" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="589.4" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="295.7" y1="587.6" x2="295.7" y2="596.1" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="588.2" width="2.34" height="4.0" fill="var(--up)"/>
<line x1="299.5" y1="585.4" x2="299.5" y2="594.9" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="588.6" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="303.3" y1="593.5" x2="303.3" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="302.12" y="594.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="307.1" y1="591.9" x2="307.1" y2="595.3" stroke="var(--up)" class="wick"/>
<rect x="305.89" y="594.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="310.8" y1="594.3" x2="310.8" y2="598.1" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="594.5" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="314.6" y1="595.2" x2="314.6" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="597.3" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="318.4" y1="600.7" x2="318.4" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="600.9" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="322.1" y1="602.2" x2="322.1" y2="606.3" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="603.7" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="325.9" y1="601.5" x2="325.9" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="324.75" y="601.6" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="329.7" y1="597.4" x2="329.7" y2="602.2" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="597.4" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="333.5" y1="596.5" x2="333.5" y2="600.0" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="597.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="337.2" y1="595.4" x2="337.2" y2="598.4" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="596.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="341.0" y1="589.0" x2="341.0" y2="597.5" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="590.4" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="344.8" y1="587.1" x2="344.8" y2="595.8" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="588.4" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="348.5" y1="589.4" x2="348.5" y2="595.8" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="594.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="352.3" y1="594.1" x2="352.3" y2="596.8" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="594.5" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="356.1" y1="593.3" x2="356.1" y2="597.1" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="593.4" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="359.9" y1="592.3" x2="359.9" y2="596.9" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="593.2" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="363.6" y1="594.1" x2="363.6" y2="597.6" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="595.4" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="367.4" y1="593.1" x2="367.4" y2="596.1" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="594.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="371.2" y1="582.1" x2="371.2" y2="595.9" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="586.2" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="375.0" y1="579.3" x2="375.0" y2="587.7" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="581.9" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="378.7" y1="578.4" x2="378.7" y2="583.8" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="581.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="382.5" y1="581.5" x2="382.5" y2="587.1" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="582.7" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="386.3" y1="584.9" x2="386.3" y2="591.2" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="585.3" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="390.0" y1="587.4" x2="390.0" y2="591.7" stroke="var(--up)" class="wick"/>
<rect x="388.87" y="587.8" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="393.8" y1="579.9" x2="393.8" y2="587.1" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="584.9" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="397.6" y1="564.8" x2="397.6" y2="585.0" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="568.5" width="2.34" height="16.5" fill="var(--up)"/>
<line x1="401.4" y1="550.5" x2="401.4" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="561.2" width="2.34" height="6.4" fill="var(--up)"/>
<line x1="405.1" y1="552.5" x2="405.1" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="559.9" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="408.9" y1="552.7" x2="408.9" y2="568.4" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="557.7" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="412.7" y1="551.1" x2="412.7" y2="563.7" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="557.0" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="416.4" y1="556.9" x2="416.4" y2="568.8" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="563.5" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="420.2" y1="530.1" x2="420.2" y2="564.3" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="538.4" width="2.34" height="24.4" fill="var(--up)"/>
<line x1="424.0" y1="528.4" x2="424.0" y2="543.8" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="536.7" width="2.34" height="3.3" fill="var(--down)"/>
<line x1="427.8" y1="526.5" x2="427.8" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="538.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="431.5" y1="520.4" x2="431.5" y2="538.8" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="532.6" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="435.3" y1="509.3" x2="435.3" y2="534.3" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="509.9" width="2.34" height="21.7" fill="var(--up)"/>
<line x1="439.1" y1="495.5" x2="439.1" y2="514.9" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="504.1" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="442.8" y1="511.1" x2="442.8" y2="534.7" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="513.2" width="2.34" height="11.0" fill="var(--down)"/>
<line x1="446.6" y1="517.3" x2="446.6" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="518.8" width="2.34" height="20.3" fill="var(--down)"/>
<line x1="450.4" y1="519.6" x2="450.4" y2="539.5" stroke="var(--up)" class="wick"/>
<rect x="449.22" y="531.0" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="454.2" y1="511.9" x2="454.2" y2="533.2" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="512.6" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="457.9" y1="496.1" x2="457.9" y2="518.5" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="500.7" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="461.7" y1="486.1" x2="461.7" y2="517.5" stroke="var(--down)" class="wick"/>
<rect x="460.53" y="501.6" width="2.34" height="13.7" fill="var(--down)"/>
<line x1="465.5" y1="511.5" x2="465.5" y2="540.6" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="515.7" width="2.34" height="24.3" fill="var(--down)"/>
<line x1="469.2" y1="523.2" x2="469.2" y2="542.1" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="529.6" width="2.34" height="10.8" fill="var(--up)"/>
<line x1="473.0" y1="526.6" x2="473.0" y2="537.3" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="527.0" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="476.8" y1="518.5" x2="476.8" y2="534.1" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="531.7" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="480.6" y1="530.4" x2="480.6" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="534.0" width="2.34" height="10.4" fill="var(--down)"/>
<line x1="484.3" y1="542.6" x2="484.3" y2="562.2" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="546.1" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="488.1" y1="547.7" x2="488.1" y2="566.2" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="551.0" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="491.9" y1="544.5" x2="491.9" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="549.5" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="495.7" y1="538.0" x2="495.7" y2="557.8" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="543.7" width="2.34" height="13.7" fill="var(--up)"/>
<line x1="499.4" y1="539.3" x2="499.4" y2="547.8" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="542.7" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="503.2" y1="537.5" x2="503.2" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="537.8" width="2.34" height="9.2" fill="var(--up)"/>
<line x1="507.0" y1="534.7" x2="507.0" y2="544.1" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="537.3" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="510.7" y1="525.6" x2="510.7" y2="546.5" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="529.3" width="2.34" height="11.4" fill="var(--up)"/>
<line x1="514.5" y1="527.4" x2="514.5" y2="539.7" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="531.4" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="518.3" y1="535.9" x2="518.3" y2="546.1" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="537.5" width="2.34" height="8.3" fill="var(--down)"/>
<line x1="522.1" y1="544.3" x2="522.1" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="546.0" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="525.8" y1="543.5" x2="525.8" y2="552.4" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="547.5" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="529.6" y1="552.2" x2="529.6" y2="559.2" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="553.5" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="533.4" y1="547.5" x2="533.4" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="532.20" y="553.6" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="537.1" y1="553.3" x2="537.1" y2="561.9" stroke="var(--down)" class="wick"/>
<rect x="535.97" y="555.5" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="540.9" y1="553.1" x2="540.9" y2="563.8" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="553.7" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="544.7" y1="548.1" x2="544.7" y2="558.3" stroke="var(--down)" class="wick"/>
<rect x="543.52" y="553.9" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="548.5" y1="553.7" x2="548.5" y2="559.0" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="555.6" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="552.2" y1="550.1" x2="552.2" y2="560.1" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="555.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="556.0" y1="546.2" x2="556.0" y2="566.7" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="556.0" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="559.8" y1="556.2" x2="559.8" y2="567.3" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="556.2" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="563.5" y1="562.6" x2="563.5" y2="567.3" stroke="var(--up)" class="wick"/>
<rect x="562.37" y="565.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="567.3" y1="561.2" x2="567.3" y2="567.1" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="561.3" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="571.1" y1="560.6" x2="571.1" y2="567.5" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="561.4" width="2.34" height="5.0" fill="var(--down)"/>
<line x1="574.9" y1="565.4" x2="574.9" y2="574.6" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="566.0" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="578.6" y1="574.0" x2="578.6" y2="580.8" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="574.1" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="582.4" y1="567.9" x2="582.4" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="581.23" y="567.9" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="586.2" y1="565.7" x2="586.2" y2="571.3" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="568.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="589.9" y1="564.7" x2="589.9" y2="571.1" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="566.6" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="593.7" y1="564.1" x2="593.7" y2="570.0" stroke="var(--down)" class="wick"/>
<rect x="592.55" y="569.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="597.5" y1="567.7" x2="597.5" y2="572.4" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="568.9" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="601.3" y1="570.2" x2="601.3" y2="574.0" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="571.5" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="605.0" y1="572.1" x2="605.0" y2="576.3" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="572.3" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="608.8" y1="571.8" x2="608.8" y2="577.1" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="575.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="612.6" y1="576.5" x2="612.6" y2="585.0" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="576.7" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="616.3" y1="579.4" x2="616.3" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="580.5" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="620.1" y1="576.7" x2="620.1" y2="582.0" stroke="var(--up)" class="wick"/>
<rect x="618.95" y="578.0" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="623.9" y1="569.2" x2="623.9" y2="577.7" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="571.3" width="2.34" height="6.0" fill="var(--up)"/>
<line x1="627.7" y1="567.4" x2="627.7" y2="578.3" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="570.7" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="631.4" y1="571.8" x2="631.4" y2="577.5" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="572.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="635.2" y1="571.2" x2="635.2" y2="581.0" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="572.0" width="2.34" height="8.2" fill="var(--down)"/>
<line x1="639.0" y1="577.3" x2="639.0" y2="585.7" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="579.9" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="642.8" y1="576.4" x2="642.8" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="578.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="646.5" y1="575.5" x2="646.5" y2="580.1" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="578.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="650.3" y1="576.4" x2="650.3" y2="581.2" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="577.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="654.1" y1="578.3" x2="654.1" y2="582.5" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="578.7" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="657.8" y1="575.3" x2="657.8" y2="583.6" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="575.7" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="661.6" y1="572.4" x2="661.6" y2="578.1" stroke="var(--up)" class="wick"/>
<rect x="660.44" y="572.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="665.4" y1="561.2" x2="665.4" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="563.1" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="669.2" y1="560.5" x2="669.2" y2="574.2" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="562.8" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="672.9" y1="556.6" x2="672.9" y2="568.6" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="557.0" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="676.7" y1="536.6" x2="676.7" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="539.9" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="680.5" y1="515.6" x2="680.5" y2="541.9" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="516.1" width="2.34" height="24.2" fill="var(--up)"/>
<line x1="684.2" y1="508.1" x2="684.2" y2="531.9" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="512.5" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="688.0" y1="459.7" x2="688.0" y2="534.3" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="465.4" width="2.34" height="64.1" fill="var(--up)"/>
<line x1="691.8" y1="435.1" x2="691.8" y2="488.0" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="437.3" width="2.34" height="30.8" fill="var(--up)"/>
<line x1="695.6" y1="407.1" x2="695.6" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="420.0" width="2.34" height="23.6" fill="var(--up)"/>
<line x1="699.3" y1="384.5" x2="699.3" y2="442.6" stroke="var(--up)" class="wick"/>
<rect x="698.16" y="389.6" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="703.1" y1="377.0" x2="703.1" y2="426.4" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="380.1" width="2.34" height="9.3" fill="var(--up)"/>
<line x1="706.9" y1="378.2" x2="706.9" y2="444.4" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="379.9" width="2.34" height="27.0" fill="var(--down)"/>
<line x1="710.6" y1="318.9" x2="710.6" y2="416.2" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="338.3" width="2.34" height="77.4" fill="var(--up)"/>
<line x1="714.4" y1="311.5" x2="714.4" y2="367.9" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="331.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="718.2" y1="315.7" x2="718.2" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="316.6" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="722.0" y1="271.4" x2="722.0" y2="458.1" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="313.1" width="2.34" height="103.4" fill="var(--down)"/>
<line x1="725.7" y1="351.7" x2="725.7" y2="453.5" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="374.1" width="2.34" height="60.5" fill="var(--up)"/>
<line x1="729.5" y1="330.9" x2="729.5" y2="374.7" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="362.0" width="2.34" height="10.2" fill="var(--up)"/>
<line x1="733.3" y1="347.6" x2="733.3" y2="394.4" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="370.2" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="737.0" y1="337.2" x2="737.0" y2="385.0" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="363.2" width="2.34" height="20.5" fill="var(--up)"/>
<line x1="740.8" y1="348.4" x2="740.8" y2="389.4" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="370.2" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="744.6" y1="390.7" x2="744.6" y2="422.9" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="392.8" width="2.34" height="27.6" fill="var(--down)"/>
<line x1="748.4" y1="415.2" x2="748.4" y2="477.0" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="424.2" width="2.34" height="42.7" fill="var(--down)"/>
<line x1="752.1" y1="460.3" x2="752.1" y2="497.0" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="462.0" width="2.34" height="30.9" fill="var(--down)"/>
<line x1="755.9" y1="462.5" x2="755.9" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="464.1" width="2.34" height="32.4" fill="var(--up)"/>
<line x1="759.7" y1="460.8" x2="759.7" y2="492.5" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="464.2" width="2.34" height="17.6" fill="var(--down)"/>
<line x1="763.5" y1="445.7" x2="763.5" y2="484.0" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="475.5" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="767.2" y1="458.7" x2="767.2" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="485.6" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="771.0" y1="449.5" x2="771.0" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="457.0" width="2.34" height="42.0" fill="var(--up)"/>
<line x1="774.8" y1="443.0" x2="774.8" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="446.6" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="778.5" y1="419.7" x2="778.5" y2="473.9" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="438.8" width="2.34" height="24.3" fill="var(--up)"/>
<line x1="782.3" y1="423.1" x2="782.3" y2="455.5" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="425.7" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="786.1" y1="409.0" x2="786.1" y2="444.8" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="423.5" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="789.9" y1="397.4" x2="789.9" y2="419.2" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="399.4" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="793.6" y1="309.1" x2="793.6" y2="413.4" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="330.1" width="2.34" height="78.3" fill="var(--up)"/>
<line x1="797.4" y1="309.0" x2="797.4" y2="371.4" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="324.5" width="2.34" height="40.2" fill="var(--down)"/>
<line x1="801.2" y1="351.4" x2="801.2" y2="393.3" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="366.8" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="804.9" y1="340.7" x2="804.9" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="350.5" width="2.34" height="30.4" fill="var(--down)"/>
<line x1="808.7" y1="357.6" x2="808.7" y2="392.6" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="364.6" width="2.34" height="20.2" fill="var(--up)"/>
<line x1="812.5" y1="348.7" x2="812.5" y2="383.9" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="365.3" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="816.3" y1="330.8" x2="816.3" y2="368.7" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="338.5" width="2.34" height="20.6" fill="var(--up)"/>
<line x1="820.0" y1="315.9" x2="820.0" y2="355.4" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="325.6" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="823.8" y1="317.4" x2="823.8" y2="361.5" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="324.7" width="2.34" height="28.6" fill="var(--up)"/>
<line x1="827.6" y1="316.9" x2="827.6" y2="358.6" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="322.8" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="831.3" y1="337.6" x2="831.3" y2="384.7" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="341.5" width="2.34" height="37.6" fill="var(--down)"/>
<line x1="835.1" y1="343.6" x2="835.1" y2="377.1" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="354.9" width="2.34" height="18.5" fill="var(--up)"/>
<line x1="838.9" y1="322.7" x2="838.9" y2="371.6" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="354.3" width="2.34" height="11.1" fill="var(--down)"/>
<line x1="842.7" y1="363.7" x2="842.7" y2="400.8" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="366.9" width="2.34" height="1.4" fill="var(--down)"/>
<line x1="846.4" y1="342.7" x2="846.4" y2="376.4" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="349.2" width="2.34" height="19.7" fill="var(--up)"/>
<line x1="850.2" y1="346.1" x2="850.2" y2="365.5" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="355.3" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="854.0" y1="262.8" x2="854.0" y2="364.4" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="265.8" width="2.34" height="87.6" fill="var(--up)"/>
<line x1="857.7" y1="164.2" x2="857.7" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="169.9" width="2.34" height="87.6" fill="var(--up)"/>
<line x1="861.5" y1="132.9" x2="861.5" y2="202.8" stroke="var(--down)" class="wick"/>
<rect x="860.35" y="184.8" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="865.3" y1="148.2" x2="865.3" y2="236.5" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="151.3" width="2.34" height="31.7" fill="var(--up)"/>
<line x1="869.1" y1="88.6" x2="869.1" y2="168.4" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="159.6" width="2.34" height="8.7" fill="var(--down)"/>
<line x1="872.8" y1="77.8" x2="872.8" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="146.0" width="2.34" height="72.4" fill="var(--down)"/>
<line x1="876.6" y1="201.7" x2="876.6" y2="287.4" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="203.0" width="2.34" height="32.5" fill="var(--down)"/>
<line x1="880.4" y1="201.7" x2="880.4" y2="256.3" stroke="var(--down)" class="wick"/>
<rect x="879.21" y="217.9" width="2.34" height="4.0" fill="var(--down)"/>
<line x1="884.2" y1="219.9" x2="884.2" y2="295.3" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="222.1" width="2.34" height="19.9" fill="var(--down)"/>
<line x1="887.9" y1="243.7" x2="887.9" y2="348.6" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="247.1" width="2.34" height="73.3" fill="var(--down)"/>
<line x1="891.7" y1="297.7" x2="891.7" y2="379.9" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="323.3" width="2.34" height="32.5" fill="var(--down)"/>
<line x1="895.5" y1="303.1" x2="895.5" y2="350.8" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="306.7" width="2.34" height="42.4" fill="var(--up)"/>
<line x1="899.2" y1="267.7" x2="899.2" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="284.7" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="903.0" y1="265.5" x2="903.0" y2="308.6" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="276.3" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="906.8" y1="288.2" x2="906.8" y2="333.4" stroke="var(--down)" class="wick"/>
<rect x="905.61" y="297.1" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="910.6" y1="265.9" x2="910.6" y2="329.6" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="302.9" width="2.34" height="25.1" fill="var(--down)"/>
<line x1="914.3" y1="321.0" x2="914.3" y2="342.3" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="323.1" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="918.1" y1="285.2" x2="918.1" y2="324.7" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="305.7" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="921.9" y1="289.7" x2="921.9" y2="319.4" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="297.0" width="2.34" height="14.3" fill="var(--up)"/>
<line x1="925.6" y1="274.7" x2="925.6" y2="330.1" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="306.8" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="929.4" y1="298.3" x2="929.4" y2="373.9" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="313.0" width="2.34" height="54.0" fill="var(--down)"/>
<line x1="933.2" y1="362.2" x2="933.2" y2="431.7" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="362.8" width="2.34" height="36.5" fill="var(--down)"/>
<line x1="937.0" y1="389.1" x2="937.0" y2="426.2" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="401.4" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="940.7" y1="400.0" x2="940.7" y2="422.7" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="409.1" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="944.5" y1="354.6" x2="944.5" y2="430.6" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="377.5" width="2.34" height="47.6" fill="var(--up)"/>
<line x1="948.3" y1="377.0" x2="948.3" y2="403.8" stroke="var(--down)" class="wick"/>
<rect x="947.10" y="390.0" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="952.0" y1="386.9" x2="952.0" y2="413.3" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="400.8" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="955.8" y1="403.1" x2="955.8" y2="428.4" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="408.9" width="2.34" height="15.0" fill="var(--down)"/>
<line x1="959.6" y1="404.6" x2="959.6" y2="448.7" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="421.1" width="2.34" height="26.8" fill="var(--down)"/>
<line x1="963.4" y1="432.3" x2="963.4" y2="458.3" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="436.2" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="967.1" y1="424.6" x2="967.1" y2="449.2" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="436.0" width="2.34" height="3.5" fill="var(--down)"/>
<line x1="970.9" y1="323.6" x2="970.9" y2="445.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="327.5" width="2.34" height="115.5" fill="var(--up)"/>
<line x1="974.7" y1="307.8" x2="974.7" y2="358.7" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="332.3" width="2.34" height="17.2" fill="var(--down)"/>
<line x1="978.4" y1="326.0" x2="978.4" y2="368.4" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="326.7" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="982.2" y1="279.6" x2="982.2" y2="335.9" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="307.1" width="2.34" height="17.6" fill="var(--up)"/>
<line x1="986.0" y1="242.9" x2="986.0" y2="315.8" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="289.5" width="2.34" height="24.7" fill="var(--up)"/>
<line x1="989.8" y1="199.8" x2="989.8" y2="331.2" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="213.8" width="2.34" height="76.6" fill="var(--up)"/>
<line x1="993.5" y1="158.5" x2="993.5" y2="239.2" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="159.2" width="2.34" height="50.3" fill="var(--up)"/>
<line x1="997.3" y1="148.9" x2="997.3" y2="264.3" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="174.9" width="2.34" height="83.3" fill="var(--down)"/>
<line x1="1001.1" y1="205.6" x2="1001.1" y2="281.0" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="240.3" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="1004.9" y1="214.3" x2="1004.9" y2="283.2" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="228.3" width="2.34" height="31.4" fill="var(--down)"/>
<line x1="1008.6" y1="224.5" x2="1008.6" y2="311.9" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="259.5" width="2.34" height="47.1" fill="var(--down)"/>
<line x1="1012.4" y1="270.8" x2="1012.4" y2="313.9" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="298.1" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="1016.2" y1="293.5" x2="1016.2" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="308.4" width="2.34" height="40.0" fill="var(--down)"/>
<line x1="1019.9" y1="352.8" x2="1019.9" y2="410.4" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="353.5" width="2.34" height="47.2" fill="var(--down)"/>
<line x1="1023.7" y1="390.9" x2="1023.7" y2="415.1" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="399.0" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="1027.5" y1="382.2" x2="1027.5" y2="420.0" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="390.0" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="1031.3" y1="337.0" x2="1031.3" y2="396.5" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="338.2" width="2.34" height="55.7" fill="var(--up)"/>
<line x1="1035.0" y1="315.4" x2="1035.0" y2="352.8" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="326.4" width="2.34" height="19.6" fill="var(--up)"/>
<line x1="1038.8" y1="320.2" x2="1038.8" y2="364.8" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="328.0" width="2.34" height="7.4" fill="var(--down)"/>
<line x1="1042.6" y1="343.9" x2="1042.6" y2="375.7" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="345.3" width="2.34" height="26.8" fill="var(--down)"/>
<line x1="1046.3" y1="363.3" x2="1046.3" y2="382.5" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="374.7" width="2.34" height="6.6" fill="var(--down)"/>
<line x1="1050.1" y1="378.4" x2="1050.1" y2="387.7" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="382.2" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="60" y1="313.4" x2="1052" y2="313.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="316.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$48 R1</text>
<text x="1058" y="328.9" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="458.2" x2="1052" y2="458.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="452.2" font-size="11.5" fill="var(--support)" font-weight="600">$26 S1</text>
<text x="1058" y="464.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="566.4" x2="1052" y2="566.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="560.4" font-size="11.5" fill="var(--support)" font-weight="600">$9.19 S2</text>
<text x="1058" y="572.4" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="580.5" x2="1052" y2="580.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="574.5" font-size="11.5" fill="var(--support)" font-weight="600">$7.03 S3</text>
<text x="1058" y="586.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="382.2" r="3" fill="var(--ink)"/>
<text x="1046.0" y="374.2" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $38 (2026-09-02)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). **[기술적 분석 — 일봉·1년](./09_technical_daily.md)의 레벨(전후 5거래일)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다** — 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $48 | 3 | 2025-05-26·2025-07-07·2026-08-10 주간 스윙 고점대 — 1년 넘게 반복해서 눌린 자리 |
| **현재가** | **$37.64** (2026-09-02 종가) | — | R1과 S1 사이 |
| S1 | $26 | 2 | 2025-01-06·2026-03-30 주간 스윙 저점대 — 현재가 아래 첫 지지 |
| S2 | $9.19 | 2 | 2022-01-24·2023-10-30 — SPAC 상장 초기~2023년 저평가 국면의 레벨 |
| S3 | $7.03 | 2 | 2021-10-04·2024-04-15 — 상장 직후와 2024년 초 저점. 현재 레짐과 단절돼 참고용 |
| 참고선 | $84.64 / $3.04 | — | 최근 5년 장중 최고/최저. 최저($3.04, 2022~2023년 국면)는 매출 규모가 지금의 1/10 이하이던 시기라 현재 지지로 읽지 않는다 |

현재가 위쪽 유효 클러스터가 R1($48) 하나뿐이라 R2·R3는 두지 않았다 — 2025-10 고점($84.64) 부근은 짧게 스쳐 지나가며 터치가 쌓이지 않아 참고선으로만 처리했다. 아래쪽 S2·S3는 매출 규모가 지금과 자릿수가 다르던 2021~2024년 국면의 레벨이라 실질적인 근시일 지지로 보기 어렵다.

---

## 3. 관측된 특이 구간 — 2024년 하반기 이후의 구조 전환

- 상장(2021-10) 후 2024년 상반기까지 약 2년 반 동안 이 종목은 대체로 $7~$20 범위에서 움직였다(§2의 S2·S3가 그 시기의 레벨이다). FY2023 매출이 $22M 수준이던 국면이다.
- 2024년 하반기부터 2025-10까지 $84.64(장중 최고)까지 밀어올린 구간에서 가격대가 한 자릿수에서 두 자릿수 후반으로 **구조적으로 재설정**됐다. 같은 기간 매출이 FY2023 $22M → FY2025 $130M으로 6배가 됐고, 자기자본도 연쇄 M&A로 $384M → $3,800M으로 10배가 됐다([핵심 지표](./04_metrics.md) A.1·A.3) — 즉 이 재설정에는 실적과 자본 규모의 실제 변화가 함께 있다.
- 2025-10 이후 현재까지는 $26~$55 사이의 넓은 박스에 갇힌 모습이다. R1($48)은 2025-05·2025-07·2026-08 세 차례 눌린 자리로, 5년 창에서 가장 반복적으로 확인된 저항대다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-30~2026-09-02. 수집 시점: 2026-09-03. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py IONQ --name "IonQ" --interval 1wk --close-on 2026-09-02 --emit all` (주봉·5년 기본 파라미터, 옵션 변경 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - §3의 구조 전환 때문에 S2($9.19)·S3($7.03)는 **현재 레짐과 단절된 레벨**이다. 5년 창을 쓰는 이 문서의 한계이며, 근시일 판단에는 S1($26) 위쪽만 참고하는 편이 낫다.
    - 해당 기간 주식분할은 없었다. 다만 발행주식수가 199.9M(FY2022말) → 397.3M(2026-09-02)으로 약 2배가 됐으므로, **같은 주가라도 그 주가가 대표하는 시가총액은 크게 달라졌다** — 가격 레벨을 기업가치와 동일시하지 말 것([핵심 지표](./04_metrics.md) A.4).

---

*작성일: 2026-09-03*
