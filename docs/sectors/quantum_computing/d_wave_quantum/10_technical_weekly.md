# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-09-02 종가 $16.49는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)의 값과 일치한다. 2022-08 상장 이후 주식분할이 없어 원주가와 수정주가가 같다.
    - **주의**: 이 5년 창에는 **2022-08 상장 이전 SPAC(DPCM Capital) 거래 구간**이 포함돼 있다. 그 구간의 가격은 D-Wave 사업이 아니라 SPAC 신탁가치($10 안팎)를 반영한 것이라 성격이 전혀 다르다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-09-02)

<div class="qbts-chart">
<style>
.qbts-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .qbts-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .qbts-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.qbts-chart svg { width:100%; height:auto; display:block; }
.qbts-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.qbts-chart .title { fill: var(--ink); font-weight:600; }
.qbts-chart .grid { stroke: var(--grid); stroke-width:1; }
.qbts-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="D-Wave Quantum(QBTS) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">D-Wave Quantum (QBTS) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-09-02 · 마지막 종가 $16.49 (2026-09-02) · 단위 USD</text>
<line x1="60" y1="614.5" x2="1052" y2="614.5" class="grid"/>
<text x="52" y="618.5" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="499.3" x2="1052" y2="499.3" class="grid"/>
<text x="52" y="503.3" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
<line x1="60" y1="384.2" x2="1052" y2="384.2" class="grid"/>
<text x="52" y="388.2" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="269.0" x2="1052" y2="269.0" class="grid"/>
<text x="52" y="273.0" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="153.9" x2="1052" y2="153.9" class="grid"/>
<text x="52" y="157.9" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
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
<line x1="61.9" y1="501.9" x2="61.9" y2="502.8" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="502.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="502.0" x2="65.7" y2="503.1" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="502.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="69.4" y1="501.3" x2="69.4" y2="502.3" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="502.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="73.2" y1="501.8" x2="73.2" y2="502.6" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="501.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="77.0" y1="501.6" x2="77.0" y2="502.2" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="501.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="80.7" y1="501.5" x2="80.7" y2="502.0" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="501.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="84.5" y1="501.4" x2="84.5" y2="502.0" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="501.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="88.3" y1="501.4" x2="88.3" y2="502.0" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="501.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="92.1" y1="501.4" x2="92.1" y2="501.8" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="501.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="95.8" y1="501.3" x2="95.8" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="501.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="99.6" y1="501.1" x2="99.6" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="501.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="103.4" y1="500.8" x2="103.4" y2="501.5" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="501.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="107.1" y1="500.6" x2="107.1" y2="501.2" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="500.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="110.9" y1="500.7" x2="110.9" y2="501.5" stroke="var(--down)" class="wick"/>
<rect x="109.75" y="501.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="114.7" y1="501.1" x2="114.7" y2="501.5" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="501.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="118.5" y1="500.6" x2="118.5" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="501.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="122.2" y1="501.4" x2="122.2" y2="501.9" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="501.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="126.0" y1="501.3" x2="126.0" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="501.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="129.8" y1="501.1" x2="129.8" y2="501.6" stroke="var(--down)" class="wick"/>
<rect x="128.61" y="501.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="133.6" y1="501.3" x2="133.6" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="501.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="137.3" y1="501.1" x2="137.3" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="501.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="141.1" y1="501.5" x2="141.1" y2="502.0" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="501.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="144.9" y1="501.4" x2="144.9" y2="501.9" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="501.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="148.6" y1="495.5" x2="148.6" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="500.3" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="152.4" y1="499.8" x2="152.4" y2="500.5" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="499.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="156.2" y1="500.1" x2="156.2" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="500.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="160.0" y1="500.4" x2="160.0" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="500.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="163.7" y1="500.5" x2="163.7" y2="501.1" stroke="var(--down)" class="wick"/>
<rect x="162.56" y="500.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="167.5" y1="500.7" x2="167.5" y2="501.1" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="500.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="171.3" y1="500.4" x2="171.3" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="170.10" y="500.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="175.0" y1="500.5" x2="175.0" y2="500.9" stroke="var(--down)" class="wick"/>
<rect x="173.87" y="500.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="178.8" y1="500.5" x2="178.8" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="177.64" y="500.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="182.6" y1="500.5" x2="182.6" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="500.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="186.4" y1="500.5" x2="186.4" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="500.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="190.1" y1="500.5" x2="190.1" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="500.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="193.9" y1="500.4" x2="193.9" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="500.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="197.7" y1="500.6" x2="197.7" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="500.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="201.4" y1="500.6" x2="201.4" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="500.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="205.2" y1="500.6" x2="205.2" y2="500.9" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="500.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="209.0" y1="500.5" x2="209.0" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="500.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="212.8" y1="500.4" x2="212.8" y2="500.7" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="500.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="216.5" y1="500.4" x2="216.5" y2="500.7" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="500.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="220.3" y1="500.3" x2="220.3" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="500.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="224.1" y1="500.1" x2="224.1" y2="500.5" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="500.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="227.8" y1="500.1" x2="227.8" y2="500.4" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="500.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="231.6" y1="499.4" x2="231.6" y2="500.2" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="499.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="235.4" y1="499.3" x2="235.4" y2="499.8" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="499.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="239.2" y1="499.3" x2="239.2" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="499.6" width="2.34" height="14.0" fill="var(--down)"/>
<line x1="242.9" y1="507.3" x2="242.9" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="514.8" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="246.7" y1="462.1" x2="246.7" y2="528.1" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="489.4" width="2.34" height="21.6" fill="var(--up)"/>
<line x1="250.5" y1="482.1" x2="250.5" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="249.31" y="487.8" width="2.34" height="23.6" fill="var(--down)"/>
<line x1="254.3" y1="505.1" x2="254.3" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="509.9" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="258.0" y1="509.1" x2="258.0" y2="545.6" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="509.6" width="2.34" height="34.7" fill="var(--down)"/>
<line x1="261.8" y1="531.5" x2="261.8" y2="552.3" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="536.4" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="265.6" y1="516.6" x2="265.6" y2="540.9" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="530.4" width="2.34" height="7.6" fill="var(--down)"/>
<line x1="269.3" y1="524.1" x2="269.3" y2="549.7" stroke="var(--down)" class="wick"/>
<rect x="268.17" y="531.6" width="2.34" height="8.9" fill="var(--down)"/>
<line x1="273.1" y1="518.9" x2="273.1" y2="544.9" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="523.9" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="276.9" y1="519.0" x2="276.9" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="520.3" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="280.7" y1="520.6" x2="280.7" y2="539.5" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="522.0" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="284.4" y1="529.3" x2="284.4" y2="560.6" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="536.2" width="2.34" height="23.0" fill="var(--down)"/>
<line x1="288.2" y1="555.9" x2="288.2" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="556.9" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="292.0" y1="568.9" x2="292.0" y2="587.7" stroke="var(--down)" class="wick"/>
<rect x="290.80" y="570.4" width="2.34" height="15.8" fill="var(--down)"/>
<line x1="295.7" y1="582.3" x2="295.7" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="582.7" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="299.5" y1="582.2" x2="299.5" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="583.0" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="303.3" y1="583.6" x2="303.3" y2="588.0" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="585.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="307.1" y1="583.4" x2="307.1" y2="590.9" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="585.0" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="310.8" y1="584.8" x2="310.8" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="587.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="314.6" y1="585.2" x2="314.6" y2="593.1" stroke="var(--down)" class="wick"/>
<rect x="313.43" y="586.4" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="318.4" y1="589.3" x2="318.4" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="589.5" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="322.1" y1="593.6" x2="322.1" y2="599.1" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="595.0" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="325.9" y1="596.9" x2="325.9" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="597.2" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="329.7" y1="591.5" x2="329.7" y2="602.7" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="595.1" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="333.5" y1="595.2" x2="333.5" y2="600.6" stroke="var(--down)" class="wick"/>
<rect x="332.29" y="595.3" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="337.2" y1="599.2" x2="337.2" y2="601.1" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="599.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="341.0" y1="596.1" x2="341.0" y2="601.6" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="596.3" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="344.8" y1="593.2" x2="344.8" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="343.61" y="593.8" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="348.5" y1="601.2" x2="348.5" y2="604.5" stroke="var(--down)" class="wick"/>
<rect x="347.38" y="601.2" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="352.3" y1="603.5" x2="352.3" y2="606.0" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="603.6" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="356.1" y1="605.3" x2="356.1" y2="606.8" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="605.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="359.9" y1="604.9" x2="359.9" y2="607.3" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="604.9" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="363.6" y1="607.1" x2="363.6" y2="608.8" stroke="var(--down)" class="wick"/>
<rect x="362.47" y="607.4" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="367.4" y1="607.8" x2="367.4" y2="608.8" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="608.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="371.2" y1="606.7" x2="371.2" y2="608.7" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="606.8" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="375.0" y1="605.0" x2="375.0" y2="606.7" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="605.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="378.7" y1="604.5" x2="378.7" y2="608.8" stroke="var(--down)" class="wick"/>
<rect x="377.55" y="605.2" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="382.5" y1="606.8" x2="382.5" y2="608.6" stroke="var(--up)" class="wick"/>
<rect x="381.33" y="608.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="386.3" y1="607.5" x2="386.3" y2="609.0" stroke="var(--down)" class="wick"/>
<rect x="385.10" y="607.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="390.0" y1="608.7" x2="390.0" y2="609.7" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="608.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="393.8" y1="609.1" x2="393.8" y2="609.9" stroke="var(--down)" class="wick"/>
<rect x="392.64" y="609.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="397.6" y1="607.2" x2="397.6" y2="609.7" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="608.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="401.4" y1="595.3" x2="401.4" y2="608.7" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="595.3" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="405.1" y1="594.7" x2="405.1" y2="601.2" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="595.0" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="408.9" y1="583.6" x2="408.9" y2="598.1" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="588.5" width="2.34" height="8.3" fill="var(--up)"/>
<line x1="412.7" y1="587.9" x2="412.7" y2="593.6" stroke="var(--down)" class="wick"/>
<rect x="411.50" y="588.1" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="416.4" y1="591.6" x2="416.4" y2="597.6" stroke="var(--down)" class="wick"/>
<rect x="415.27" y="592.5" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="420.2" y1="587.2" x2="420.2" y2="596.5" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="590.4" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="424.0" y1="586.8" x2="424.0" y2="593.2" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="589.4" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="427.8" y1="582.2" x2="427.8" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="589.2" width="2.34" height="3.8" fill="var(--up)"/>
<line x1="431.5" y1="577.6" x2="431.5" y2="589.4" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="586.7" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="435.3" y1="584.9" x2="435.3" y2="593.1" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="585.9" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="439.1" y1="583.2" x2="439.1" y2="592.5" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="590.4" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="442.8" y1="592.0" x2="442.8" y2="598.4" stroke="var(--down)" class="wick"/>
<rect x="441.67" y="592.3" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="446.6" y1="595.4" x2="446.6" y2="600.3" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="597.1" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="450.4" y1="597.8" x2="450.4" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="598.7" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="454.2" y1="599.9" x2="454.2" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="601.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="457.9" y1="600.6" x2="457.9" y2="604.6" stroke="var(--down)" class="wick"/>
<rect x="456.76" y="601.6" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="461.7" y1="601.5" x2="461.7" y2="604.0" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="602.5" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="465.5" y1="602.4" x2="465.5" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="602.5" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="469.2" y1="602.5" x2="469.2" y2="604.4" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="603.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="473.0" y1="603.1" x2="473.0" y2="604.8" stroke="var(--up)" class="wick"/>
<rect x="471.85" y="603.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="476.8" y1="601.1" x2="476.8" y2="603.7" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="603.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="480.6" y1="602.7" x2="480.6" y2="605.7" stroke="var(--down)" class="wick"/>
<rect x="479.39" y="603.5" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="484.3" y1="605.0" x2="484.3" y2="607.6" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="605.7" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="488.1" y1="603.2" x2="488.1" y2="607.9" stroke="var(--up)" class="wick"/>
<rect x="486.94" y="604.4" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="491.9" y1="603.8" x2="491.9" y2="607.9" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="604.1" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="495.7" y1="603.7" x2="495.7" y2="606.5" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="604.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="499.4" y1="603.5" x2="499.4" y2="605.5" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="604.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="503.2" y1="603.5" x2="503.2" y2="605.3" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="603.6" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="507.0" y1="601.9" x2="507.0" y2="604.3" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="602.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="510.7" y1="602.2" x2="510.7" y2="604.8" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="602.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="514.5" y1="602.5" x2="514.5" y2="604.2" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="603.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="518.3" y1="603.2" x2="518.3" y2="604.7" stroke="var(--down)" class="wick"/>
<rect x="517.11" y="603.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="522.1" y1="604.3" x2="522.1" y2="605.5" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="604.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="525.8" y1="604.4" x2="525.8" y2="606.0" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="604.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="529.6" y1="605.6" x2="529.6" y2="606.6" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="605.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="533.4" y1="604.5" x2="533.4" y2="606.3" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="605.0" width="2.34" height="1.1" fill="var(--up)"/>
<line x1="537.1" y1="603.3" x2="537.1" y2="605.5" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="603.3" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="540.9" y1="601.9" x2="540.9" y2="604.5" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="601.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="544.7" y1="590.5" x2="544.7" y2="600.8" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="594.4" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="548.5" y1="589.5" x2="548.5" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="589.7" width="2.34" height="4.1" fill="var(--down)"/>
<line x1="552.2" y1="590.2" x2="552.2" y2="596.8" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="593.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="556.0" y1="591.2" x2="556.0" y2="599.6" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="593.0" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="559.8" y1="586.4" x2="559.8" y2="594.1" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="590.5" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="563.5" y1="586.6" x2="563.5" y2="593.2" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="589.8" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="567.3" y1="589.6" x2="567.3" y2="593.1" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="591.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="571.1" y1="589.2" x2="571.1" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="569.92" y="591.1" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="574.9" y1="591.7" x2="574.9" y2="596.3" stroke="var(--down)" class="wick"/>
<rect x="573.69" y="591.9" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="578.6" y1="593.7" x2="578.6" y2="597.0" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="595.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="582.4" y1="595.1" x2="582.4" y2="598.4" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="596.3" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="586.2" y1="597.0" x2="586.2" y2="599.7" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="597.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="589.9" y1="596.9" x2="589.9" y2="600.0" stroke="var(--down)" class="wick"/>
<rect x="588.78" y="597.9" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="593.7" y1="597.2" x2="593.7" y2="600.3" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="599.5" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="597.5" y1="599.4" x2="597.5" y2="601.2" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="599.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="601.3" y1="595.3" x2="601.3" y2="600.1" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="598.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="605.0" y1="598.2" x2="605.0" y2="601.5" stroke="var(--down)" class="wick"/>
<rect x="603.86" y="598.7" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="608.8" y1="600.4" x2="608.8" y2="601.9" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="600.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="612.6" y1="600.2" x2="612.6" y2="601.7" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="600.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="616.3" y1="600.4" x2="616.3" y2="602.5" stroke="var(--down)" class="wick"/>
<rect x="615.18" y="600.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="620.1" y1="601.1" x2="620.1" y2="602.4" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="601.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="623.9" y1="599.1" x2="623.9" y2="601.8" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="600.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="627.7" y1="598.4" x2="627.7" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="600.3" width="2.34" height="2.4" fill="var(--down)"/>
<line x1="631.4" y1="601.5" x2="631.4" y2="603.5" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="602.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="635.2" y1="602.3" x2="635.2" y2="604.7" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="602.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="639.0" y1="604.0" x2="639.0" y2="605.8" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="604.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="642.8" y1="603.0" x2="642.8" y2="604.8" stroke="var(--up)" class="wick"/>
<rect x="641.58" y="603.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="646.5" y1="601.7" x2="646.5" y2="604.2" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="602.2" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="650.3" y1="602.2" x2="650.3" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="602.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="654.1" y1="602.9" x2="654.1" y2="604.6" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="602.9" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="657.8" y1="602.6" x2="657.8" y2="605.3" stroke="var(--up)" class="wick"/>
<rect x="656.67" y="602.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="661.6" y1="602.7" x2="661.6" y2="603.8" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="603.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="665.4" y1="602.2" x2="665.4" y2="604.1" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="602.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="669.2" y1="602.6" x2="669.2" y2="604.1" stroke="var(--down)" class="wick"/>
<rect x="667.99" y="602.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="672.9" y1="603.0" x2="672.9" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="603.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="676.7" y1="600.6" x2="676.7" y2="603.2" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="601.0" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="680.5" y1="598.5" x2="680.5" y2="602.5" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="600.6" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="684.2" y1="600.1" x2="684.2" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="683.07" y="602.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="688.0" y1="596.1" x2="688.0" y2="603.3" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="596.1" width="2.34" height="6.3" fill="var(--up)"/>
<line x1="691.8" y1="589.7" x2="691.8" y2="597.6" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="594.4" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="695.6" y1="579.9" x2="695.6" y2="598.2" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="580.7" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="699.3" y1="571.1" x2="699.3" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="575.1" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="703.1" y1="554.4" x2="703.1" y2="585.7" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="556.2" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="706.9" y1="552.5" x2="706.9" y2="571.8" stroke="var(--down)" class="wick"/>
<rect x="705.71" y="553.9" width="2.34" height="3.0" fill="var(--down)"/>
<line x1="710.6" y1="493.6" x2="710.6" y2="558.8" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="540.3" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="714.4" y1="483.1" x2="714.4" y2="533.1" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="500.4" width="2.34" height="21.8" fill="var(--up)"/>
<line x1="718.2" y1="497.6" x2="718.2" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="508.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="722.0" y1="492.7" x2="722.0" y2="560.9" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="508.9" width="2.34" height="39.2" fill="var(--down)"/>
<line x1="725.7" y1="540.3" x2="725.7" y2="571.4" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="553.8" width="2.34" height="7.0" fill="var(--up)"/>
<line x1="729.5" y1="532.6" x2="729.5" y2="552.5" stroke="var(--up)" class="wick"/>
<rect x="728.34" y="544.4" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="733.3" y1="540.9" x2="733.3" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="546.1" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="737.0" y1="537.8" x2="737.0" y2="552.8" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="547.6" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="740.8" y1="536.2" x2="740.8" y2="553.3" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="541.1" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="744.6" y1="519.9" x2="744.6" y2="548.5" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="531.0" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="748.4" y1="530.8" x2="748.4" y2="553.0" stroke="var(--down)" class="wick"/>
<rect x="747.20" y="530.8" width="2.34" height="20.6" fill="var(--down)"/>
<line x1="752.1" y1="548.0" x2="752.1" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="550.2" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="755.9" y1="497.0" x2="755.9" y2="562.8" stroke="var(--up)" class="wick"/>
<rect x="754.74" y="497.6" width="2.34" height="59.2" fill="var(--up)"/>
<line x1="759.7" y1="476.9" x2="759.7" y2="520.5" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="488.9" width="2.34" height="29.4" fill="var(--down)"/>
<line x1="763.5" y1="506.8" x2="763.5" y2="531.0" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="512.0" width="2.34" height="15.2" fill="var(--down)"/>
<line x1="767.2" y1="521.3" x2="767.2" y2="543.8" stroke="var(--down)" class="wick"/>
<rect x="766.06" y="531.5" width="2.34" height="10.0" fill="var(--down)"/>
<line x1="771.0" y1="527.0" x2="771.0" y2="548.0" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="531.0" width="2.34" height="15.8" fill="var(--up)"/>
<line x1="774.8" y1="525.0" x2="774.8" y2="542.3" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="527.3" width="2.34" height="13.2" fill="var(--down)"/>
<line x1="778.5" y1="526.2" x2="778.5" y2="545.7" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="527.8" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="782.3" y1="520.8" x2="782.3" y2="539.4" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="523.4" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="786.1" y1="479.9" x2="786.1" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="486.8" width="2.34" height="38.9" fill="var(--up)"/>
<line x1="789.9" y1="468.7" x2="789.9" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="473.4" width="2.34" height="5.3" fill="var(--up)"/>
<line x1="793.6" y1="386.9" x2="793.6" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="398.0" width="2.34" height="72.3" fill="var(--up)"/>
<line x1="797.4" y1="390.7" x2="797.4" y2="436.3" stroke="var(--down)" class="wick"/>
<rect x="796.23" y="392.5" width="2.34" height="34.0" fill="var(--down)"/>
<line x1="801.2" y1="398.1" x2="801.2" y2="440.0" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="400.1" width="2.34" height="27.5" fill="var(--up)"/>
<line x1="804.9" y1="396.3" x2="804.9" y2="443.6" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="397.1" width="2.34" height="42.7" fill="var(--down)"/>
<line x1="808.7" y1="421.1" x2="808.7" y2="441.5" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="434.3" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="812.5" y1="436.7" x2="812.5" y2="458.2" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="441.5" width="2.34" height="11.5" fill="var(--down)"/>
<line x1="816.3" y1="420.7" x2="816.3" y2="455.2" stroke="var(--up)" class="wick"/>
<rect x="815.09" y="421.1" width="2.34" height="30.7" fill="var(--up)"/>
<line x1="820.0" y1="412.5" x2="820.0" y2="444.5" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="422.1" width="2.34" height="21.9" fill="var(--down)"/>
<line x1="823.8" y1="389.6" x2="823.8" y2="443.0" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="397.0" width="2.34" height="43.9" fill="var(--up)"/>
<line x1="827.6" y1="377.7" x2="827.6" y2="421.3" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="390.5" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="831.3" y1="390.6" x2="831.3" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="392.2" width="2.34" height="33.6" fill="var(--down)"/>
<line x1="835.1" y1="393.7" x2="835.1" y2="426.2" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="419.9" width="2.34" height="1.6" fill="var(--up)"/>
<line x1="838.9" y1="394.7" x2="838.9" y2="424.3" stroke="var(--up)" class="wick"/>
<rect x="837.72" y="418.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="842.7" y1="417.9" x2="842.7" y2="451.0" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="418.8" width="2.34" height="16.8" fill="var(--down)"/>
<line x1="846.4" y1="426.9" x2="846.4" y2="444.5" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="434.6" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="850.2" y1="428.9" x2="850.2" y2="444.3" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="437.5" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="854.0" y1="407.4" x2="854.0" y2="439.1" stroke="var(--up)" class="wick"/>
<rect x="852.81" y="410.0" width="2.34" height="26.0" fill="var(--up)"/>
<line x1="857.7" y1="299.8" x2="857.7" y2="415.7" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="305.0" width="2.34" height="105.7" fill="var(--up)"/>
<line x1="861.5" y1="278.5" x2="861.5" y2="351.5" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="306.3" width="2.34" height="26.1" fill="var(--up)"/>
<line x1="865.3" y1="231.3" x2="865.3" y2="341.9" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="237.9" width="2.34" height="65.4" fill="var(--up)"/>
<line x1="869.1" y1="159.1" x2="869.1" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="867.90" y="234.3" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="872.8" y1="76.2" x2="872.8" y2="238.9" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="173.1" width="2.34" height="46.6" fill="var(--up)"/>
<line x1="876.6" y1="157.6" x2="876.6" y2="310.8" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="159.4" width="2.34" height="79.1" fill="var(--down)"/>
<line x1="880.4" y1="183.4" x2="880.4" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="187.7" width="2.34" height="35.4" fill="var(--up)"/>
<line x1="884.2" y1="181.3" x2="884.2" y2="310.3" stroke="var(--down)" class="wick"/>
<rect x="882.98" y="183.6" width="2.34" height="91.2" fill="var(--down)"/>
<line x1="887.9" y1="250.6" x2="887.9" y2="367.3" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="267.8" width="2.34" height="74.8" fill="var(--down)"/>
<line x1="891.7" y1="330.2" x2="891.7" y2="400.9" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="347.0" width="2.34" height="32.5" fill="var(--down)"/>
<line x1="895.5" y1="345.7" x2="895.5" y2="379.0" stroke="var(--up)" class="wick"/>
<rect x="894.30" y="353.4" width="2.34" height="24.8" fill="var(--up)"/>
<line x1="899.2" y1="281.7" x2="899.2" y2="369.0" stroke="var(--up)" class="wick"/>
<rect x="898.07" y="303.6" width="2.34" height="57.5" fill="var(--up)"/>
<line x1="903.0" y1="278.8" x2="903.0" y2="324.1" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="293.0" width="2.34" height="21.0" fill="var(--down)"/>
<line x1="906.8" y1="300.2" x2="906.8" y2="343.1" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="305.6" width="2.34" height="4.8" fill="var(--up)"/>
<line x1="910.6" y1="241.5" x2="910.6" y2="329.3" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="296.0" width="2.34" height="27.3" fill="var(--down)"/>
<line x1="914.3" y1="288.0" x2="914.3" y2="325.8" stroke="var(--up)" class="wick"/>
<rect x="913.16" y="290.6" width="2.34" height="32.1" fill="var(--up)"/>
<line x1="918.1" y1="244.2" x2="918.1" y2="295.3" stroke="var(--down)" class="wick"/>
<rect x="916.93" y="284.5" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="921.9" y1="253.4" x2="921.9" y2="297.7" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="282.5" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="925.6" y1="286.5" x2="925.6" y2="329.6" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="297.0" width="2.34" height="22.3" fill="var(--down)"/>
<line x1="929.4" y1="314.8" x2="929.4" y2="376.1" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="319.7" width="2.34" height="50.4" fill="var(--down)"/>
<line x1="933.2" y1="366.1" x2="933.2" y2="419.6" stroke="var(--down)" class="wick"/>
<rect x="932.02" y="366.7" width="2.34" height="9.2" fill="var(--down)"/>
<line x1="937.0" y1="366.7" x2="937.0" y2="402.0" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="379.3" width="2.34" height="8.6" fill="var(--down)"/>
<line x1="940.7" y1="388.6" x2="940.7" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="394.5" width="2.34" height="12.0" fill="var(--down)"/>
<line x1="944.5" y1="364.6" x2="944.5" y2="414.0" stroke="var(--up)" class="wick"/>
<rect x="943.33" y="398.2" width="2.34" height="13.9" fill="var(--up)"/>
<line x1="948.3" y1="388.7" x2="948.3" y2="415.7" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="400.4" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="952.0" y1="389.7" x2="952.0" y2="413.8" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="405.7" width="2.34" height="6.7" fill="var(--down)"/>
<line x1="955.8" y1="402.4" x2="955.8" y2="439.2" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="407.4" width="2.34" height="25.9" fill="var(--down)"/>
<line x1="959.6" y1="421.9" x2="959.6" y2="456.7" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="433.6" width="2.34" height="20.8" fill="var(--down)"/>
<line x1="963.4" y1="441.9" x2="963.4" y2="467.7" stroke="var(--up)" class="wick"/>
<rect x="962.19" y="449.6" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="967.1" y1="437.7" x2="967.1" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="450.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="970.9" y1="355.5" x2="970.9" y2="455.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="364.7" width="2.34" height="87.6" fill="var(--up)"/>
<line x1="974.7" y1="362.0" x2="974.7" y2="408.4" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="372.4" width="2.34" height="29.2" fill="var(--down)"/>
<line x1="978.4" y1="376.5" x2="978.4" y2="417.5" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="378.5" width="2.34" height="27.1" fill="var(--up)"/>
<line x1="982.2" y1="337.7" x2="982.2" y2="382.6" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="354.6" width="2.34" height="24.5" fill="var(--up)"/>
<line x1="986.0" y1="329.1" x2="986.0" y2="381.9" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="358.8" width="2.34" height="21.3" fill="var(--down)"/>
<line x1="989.8" y1="251.2" x2="989.8" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="275.9" width="2.34" height="107.0" fill="var(--up)"/>
<line x1="993.5" y1="266.5" x2="993.5" y2="318.6" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="267.4" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="997.3" y1="254.1" x2="997.3" y2="346.4" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="281.1" width="2.34" height="58.7" fill="var(--down)"/>
<line x1="1001.1" y1="306.7" x2="1001.1" y2="357.1" stroke="var(--down)" class="wick"/>
<rect x="999.91" y="330.1" width="2.34" height="15.3" fill="var(--down)"/>
<line x1="1004.9" y1="301.8" x2="1004.9" y2="354.9" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="327.6" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="1008.6" y1="306.9" x2="1008.6" y2="373.5" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="333.6" width="2.34" height="18.8" fill="var(--down)"/>
<line x1="1012.4" y1="329.7" x2="1012.4" y2="357.7" stroke="var(--down)" class="wick"/>
<rect x="1011.23" y="347.7" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="1016.2" y1="342.4" x2="1016.2" y2="384.8" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="356.1" width="2.34" height="27.1" fill="var(--down)"/>
<line x1="1019.9" y1="387.8" x2="1019.9" y2="430.0" stroke="var(--down)" class="wick"/>
<rect x="1018.77" y="387.8" width="2.34" height="34.1" fill="var(--down)"/>
<line x1="1023.7" y1="407.0" x2="1023.7" y2="428.2" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="418.7" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="1027.5" y1="389.5" x2="1027.5" y2="429.4" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="406.3" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="1031.3" y1="361.2" x2="1031.3" y2="407.2" stroke="var(--up)" class="wick"/>
<rect x="1030.09" y="375.4" width="2.34" height="30.7" fill="var(--up)"/>
<line x1="1035.0" y1="364.0" x2="1035.0" y2="386.6" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="370.7" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="1038.8" y1="368.6" x2="1038.8" y2="402.1" stroke="var(--down)" class="wick"/>
<rect x="1037.63" y="375.2" width="2.34" height="4.5" fill="var(--down)"/>
<line x1="1042.6" y1="384.8" x2="1042.6" y2="422.5" stroke="var(--down)" class="wick"/>
<rect x="1041.40" y="387.1" width="2.34" height="31.8" fill="var(--down)"/>
<line x1="1046.3" y1="414.7" x2="1046.3" y2="425.8" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="422.4" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="1050.1" y1="422.1" x2="1050.1" y2="428.1" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="424.6" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="60" y1="501.2" x2="1052" y2="501.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="495.2" font-size="11.5" fill="var(--support)" font-weight="600">$9.84 S1</text>
<text x="1058" y="507.2" font-size="9.5" fill="var(--muted)">터치 5회</text>
<line x1="60" y1="607.9" x2="1052" y2="607.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="601.9" font-size="11.5" fill="var(--support)" font-weight="600">$0.57 S2</text>
<text x="1058" y="613.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="424.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="416.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $16.49 (2026-09-02)</text>
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
| **현재가** | **$16.49** (2026-09-02 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $9.84 | 5 | 2022-01-24·2022-03-14·2022-05-09·2022-05-16·2022-05-23 — 상장 직전 SPAC 거래 구간. 5년 창에서 가장 두껍지만 현재 레짐과 4년 이상 떨어져 있다 |
| S2 | $0.57 | 2 | 2023-10-30·2023-11-06 — 자기자본이 마이너스였던 FY2023 저점 국면 |
| 참고선 | $46.75 / $0.40 | — | 최근 5년 장중 최고/최저. 최저($0.40)는 시가총액이 $140M대이던 시기라 현재 지지로 읽지 않는다 |

**현재가 위쪽에 유효한 클러스터가 하나도 없다.** 2025년 하반기~2026년 상반기의 $20~$46 구간은 상승과 하락이 모두 빨라 같은 가격대를 반복해서 눌러본 흔적(터치 2회 이상)이 남지 않았기 때문이다 — 주봉 배율에서는 이 회사의 최근 2년이 "레벨이 형성되지 않은 구간"으로 잡힌다. 아래쪽 S1($9.84)·S2($0.57)는 각각 SPAC 거래 구간과 FY2023 저점 국면의 값이라 현재 레짐과 단절돼 있다.

---

## 3. 관측된 특이 구간 — 2024년 하반기 이후의 구조 전환

- 상장(2022-08) 후 2024년 상반기까지 약 2년 동안 이 종목은 대체로 $0.5~$3 범위에서 움직였다(§2의 S2가 그 시기의 레벨이다). FY2023 말 시가총액은 $140.75M, 자기자본은 **마이너스 $24.0M**이었다([핵심 지표](./04_metrics.md) A.2·A.3).
- 2024년 하반기부터 2026-01까지 $46.75(장중 최고)까지 올라가며 가격대가 한 자릿수 이하에서 두 자릿수로 **구조적으로 재설정**됐다. 같은 기간 시가총액은 $140.75M → $9,160M(FY2025말)으로 **65배**가 됐는데, 매출은 $8.8M → $24.6M으로 2.8배 늘었을 뿐이다 — 이 재설정의 대부분은 실적이 아니라 **배수 확장**(PSR 16.0x → 372.4x)이었다.
- 2026-01 이후 현재까지는 $16~$32 사이에서 저항대를 낮춰가며 되돌리는 국면이다. 5년 창 전체로 보면 현재가($16.49)는 여전히 2024년 이전 레짐의 5배 이상 높은 자리에 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 263개 주, 2021-08-30~2026-09-02. 수집 시점: 2026-09-03. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py QBTS --name "D-Wave Quantum" --interval 1wk --close-on 2026-09-02 --emit all` (주봉·5년 기본 파라미터, 옵션 변경 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨이 2개뿐이고 둘 다 현재가 아래에 있다.** 유효 클러스터가 그것뿐이라 개수를 억지로 늘리지 않았다. 근시일 판단에 이 문서의 레벨을 쓰기는 어렵고, [기술적 분석 — 일봉·1년](./09_technical_daily.md) 쪽을 보는 편이 낫다.
    - S1($9.84)은 **상장 이전 SPAC 거래 구간**의 가격이라 D-Wave 사업에 대한 시장 평가가 아니다. 5년 창을 쓰는 이 문서의 구조적 한계다.
    - 해당 기간 주식분할은 없었다. 다만 발행주식수가 약 1.6억 주(FY2023말) → 3.72억 주(2026-09-02)로 2.3배가 됐으므로, **같은 주가라도 그 주가가 대표하는 시가총액은 크게 달라졌다**([핵심 지표](./04_metrics.md) A.4).

---

*작성일: 2026-09-03*
