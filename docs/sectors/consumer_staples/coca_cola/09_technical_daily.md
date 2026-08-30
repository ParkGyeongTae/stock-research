# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-08-27 종가 $89.06은 [핵심 지표 A.2](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치**한다. 다만 같은 스크립트의 주봉 산출물은 한 거래일 뒤인 **2026-08-28 종가 $89.66**을 최신으로 잡는다 — 일봉 원자료에 2026-08-28이 아직 들어오지 않은 탓이며, 이 저장소의 회사 문서는 모두 일봉 기준(2026-08-27 $89.06)으로 통일했다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

<div class="ko-chart">
<style>
.ko-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ko-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ko-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ko-chart svg { width:100%; height:auto; display:block; }
.ko-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ko-chart .title { fill: var(--ink); font-weight:600; }
.ko-chart .grid { stroke: var(--grid); stroke-width:1; }
.ko-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="코카콜라(KO) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">코카콜라 (KO) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $89.06 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="616.2" x2="1052" y2="616.2" class="grid"/>
<text x="52" y="620.2" font-size="11" text-anchor="end" fill="var(--muted)">65</text>
<line x1="60" y1="517.9" x2="1052" y2="517.9" class="grid"/>
<text x="52" y="521.9" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="419.6" x2="1052" y2="419.6" class="grid"/>
<text x="52" y="423.6" font-size="11" text-anchor="end" fill="var(--muted)">75</text>
<line x1="60" y1="321.3" x2="1052" y2="321.3" class="grid"/>
<text x="52" y="325.3" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="223.1" x2="1052" y2="223.1" class="grid"/>
<text x="52" y="227.1" font-size="11" text-anchor="end" fill="var(--muted)">85</text>
<line x1="60" y1="124.8" x2="1052" y2="124.8" class="grid"/>
<text x="52" y="128.8" font-size="11" text-anchor="end" fill="var(--muted)">90</text>
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
<line x1="62.0" y1="534.8" x2="62.0" y2="548.8" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="537.7" width="2.46" height="6.3" fill="var(--up)"/>
<line x1="66.0" y1="530.9" x2="66.0" y2="552.1" stroke="var(--up)" class="wick"/>
<rect x="64.72" y="536.4" width="2.46" height="2.0" fill="var(--up)"/>
<line x1="69.9" y1="535.6" x2="69.9" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="68.69" y="537.7" width="2.46" height="6.5" fill="var(--up)"/>
<line x1="73.9" y1="528.5" x2="73.9" y2="555.0" stroke="var(--down)" class="wick"/>
<rect x="72.66" y="535.4" width="2.46" height="16.9" fill="var(--down)"/>
<line x1="77.9" y1="545.8" x2="77.9" y2="559.8" stroke="var(--down)" class="wick"/>
<rect x="76.63" y="557.0" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="81.8" y1="559.6" x2="81.8" y2="573.7" stroke="var(--down)" class="wick"/>
<rect x="80.59" y="560.0" width="2.46" height="8.5" fill="var(--down)"/>
<line x1="85.8" y1="555.0" x2="85.8" y2="571.4" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="560.0" width="2.46" height="11.4" fill="var(--up)"/>
<line x1="89.8" y1="555.4" x2="89.8" y2="572.7" stroke="var(--up)" class="wick"/>
<rect x="88.53" y="560.7" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="93.7" y1="553.9" x2="93.7" y2="565.5" stroke="var(--down)" class="wick"/>
<rect x="92.50" y="558.8" width="2.46" height="5.9" fill="var(--down)"/>
<line x1="97.7" y1="562.7" x2="97.7" y2="578.0" stroke="var(--down)" class="wick"/>
<rect x="96.47" y="565.1" width="2.46" height="11.6" fill="var(--down)"/>
<line x1="101.7" y1="581.2" x2="101.7" y2="594.6" stroke="var(--down)" class="wick"/>
<rect x="100.43" y="583.2" width="2.46" height="9.2" fill="var(--down)"/>
<line x1="105.6" y1="586.5" x2="105.6" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="589.6" width="2.46" height="2.2" fill="var(--down)"/>
<line x1="109.6" y1="574.3" x2="109.6" y2="588.5" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="576.1" width="2.46" height="12.4" fill="var(--up)"/>
<line x1="113.6" y1="576.1" x2="113.6" y2="589.6" stroke="var(--down)" class="wick"/>
<rect x="112.34" y="580.8" width="2.46" height="6.7" fill="var(--down)"/>
<line x1="117.5" y1="582.2" x2="117.5" y2="595.5" stroke="var(--down)" class="wick"/>
<rect x="116.31" y="586.9" width="2.46" height="1.2" fill="var(--down)"/>
<line x1="121.5" y1="584.9" x2="121.5" y2="594.9" stroke="var(--up)" class="wick"/>
<rect x="120.27" y="592.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="125.5" y1="581.6" x2="125.5" y2="598.5" stroke="var(--up)" class="wick"/>
<rect x="124.24" y="582.6" width="2.46" height="7.1" fill="var(--up)"/>
<line x1="129.4" y1="581.2" x2="129.4" y2="597.3" stroke="var(--up)" class="wick"/>
<rect x="128.21" y="587.7" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="133.4" y1="578.4" x2="133.4" y2="597.5" stroke="var(--down)" class="wick"/>
<rect x="132.18" y="581.8" width="2.46" height="15.1" fill="var(--down)"/>
<line x1="137.4" y1="590.0" x2="137.4" y2="606.3" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="595.1" width="2.46" height="7.9" fill="var(--down)"/>
<line x1="141.3" y1="594.6" x2="141.3" y2="609.3" stroke="var(--up)" class="wick"/>
<rect x="140.11" y="595.7" width="2.46" height="7.3" fill="var(--up)"/>
<line x1="145.3" y1="583.9" x2="145.3" y2="597.3" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="590.2" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="149.3" y1="580.2" x2="149.3" y2="590.8" stroke="var(--up)" class="wick"/>
<rect x="148.05" y="581.2" width="2.46" height="5.3" fill="var(--up)"/>
<line x1="153.2" y1="583.7" x2="153.2" y2="599.3" stroke="var(--down)" class="wick"/>
<rect x="152.02" y="586.1" width="2.46" height="8.5" fill="var(--down)"/>
<line x1="157.2" y1="577.1" x2="157.2" y2="595.7" stroke="var(--up)" class="wick"/>
<rect x="155.99" y="583.7" width="2.46" height="10.8" fill="var(--up)"/>
<line x1="161.2" y1="586.7" x2="161.2" y2="599.7" stroke="var(--down)" class="wick"/>
<rect x="159.95" y="586.9" width="2.46" height="7.7" fill="var(--down)"/>
<line x1="165.2" y1="571.8" x2="165.2" y2="599.1" stroke="var(--up)" class="wick"/>
<rect x="163.92" y="581.0" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="169.1" y1="579.4" x2="169.1" y2="595.3" stroke="var(--down)" class="wick"/>
<rect x="167.89" y="583.3" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="173.1" y1="580.8" x2="173.1" y2="594.2" stroke="var(--up)" class="wick"/>
<rect x="171.86" y="589.2" width="2.46" height="1.6" fill="var(--up)"/>
<line x1="177.1" y1="569.0" x2="177.1" y2="589.0" stroke="var(--up)" class="wick"/>
<rect x="175.83" y="576.1" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="181.0" y1="580.8" x2="181.0" y2="596.5" stroke="var(--up)" class="wick"/>
<rect x="179.79" y="580.8" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="185.0" y1="565.7" x2="185.0" y2="581.8" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="566.8" width="2.46" height="12.6" fill="var(--up)"/>
<line x1="189.0" y1="562.7" x2="189.0" y2="578.4" stroke="var(--down)" class="wick"/>
<rect x="187.73" y="571.6" width="2.46" height="3.7" fill="var(--down)"/>
<line x1="192.9" y1="555.0" x2="192.9" y2="573.7" stroke="var(--up)" class="wick"/>
<rect x="191.70" y="565.3" width="2.46" height="8.1" fill="var(--up)"/>
<line x1="196.9" y1="547.4" x2="196.9" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="195.67" y="548.6" width="2.46" height="8.6" fill="var(--up)"/>
<line x1="200.9" y1="544.6" x2="200.9" y2="558.8" stroke="var(--up)" class="wick"/>
<rect x="199.63" y="548.6" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="204.8" y1="490.6" x2="204.8" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="203.60" y="493.9" width="2.46" height="12.8" fill="var(--up)"/>
<line x1="208.8" y1="486.1" x2="208.8" y2="507.9" stroke="var(--down)" class="wick"/>
<rect x="207.57" y="491.2" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="212.8" y1="499.6" x2="212.8" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="211.54" y="502.0" width="2.46" height="17.1" fill="var(--down)"/>
<line x1="216.7" y1="516.9" x2="216.7" y2="524.8" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="519.7" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="220.7" y1="515.5" x2="220.7" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="219.47" y="516.7" width="2.46" height="5.5" fill="var(--up)"/>
<line x1="224.7" y1="500.2" x2="224.7" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="223.44" y="514.8" width="2.46" height="2.2" fill="var(--up)"/>
<line x1="228.6" y1="517.3" x2="228.6" y2="554.1" stroke="var(--down)" class="wick"/>
<rect x="227.41" y="519.5" width="2.46" height="30.9" fill="var(--down)"/>
<line x1="232.6" y1="531.9" x2="232.6" y2="549.5" stroke="var(--up)" class="wick"/>
<rect x="231.38" y="537.9" width="2.46" height="10.4" fill="var(--up)"/>
<line x1="236.6" y1="536.2" x2="236.6" y2="559.2" stroke="var(--up)" class="wick"/>
<rect x="235.35" y="539.5" width="2.46" height="6.9" fill="var(--up)"/>
<line x1="240.5" y1="539.7" x2="240.5" y2="563.9" stroke="var(--down)" class="wick"/>
<rect x="239.31" y="541.5" width="2.46" height="16.3" fill="var(--down)"/>
<line x1="244.5" y1="542.9" x2="244.5" y2="554.1" stroke="var(--up)" class="wick"/>
<rect x="243.28" y="544.2" width="2.46" height="3.7" fill="var(--up)"/>
<line x1="248.5" y1="540.9" x2="248.5" y2="553.7" stroke="var(--down)" class="wick"/>
<rect x="247.25" y="544.2" width="2.46" height="2.9" fill="var(--down)"/>
<line x1="252.4" y1="534.8" x2="252.4" y2="558.8" stroke="var(--up)" class="wick"/>
<rect x="251.22" y="536.4" width="2.46" height="14.9" fill="var(--up)"/>
<line x1="256.4" y1="500.8" x2="256.4" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="507.1" width="2.46" height="14.5" fill="var(--up)"/>
<line x1="260.4" y1="504.9" x2="260.4" y2="528.9" stroke="var(--up)" class="wick"/>
<rect x="259.15" y="507.7" width="2.46" height="10.0" fill="var(--up)"/>
<line x1="264.4" y1="483.5" x2="264.4" y2="504.9" stroke="var(--up)" class="wick"/>
<rect x="263.12" y="486.3" width="2.46" height="12.4" fill="var(--up)"/>
<line x1="268.3" y1="480.7" x2="268.3" y2="491.6" stroke="var(--up)" class="wick"/>
<rect x="267.09" y="488.2" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="272.3" y1="485.1" x2="272.3" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="271.06" y="490.0" width="2.46" height="6.9" fill="var(--down)"/>
<line x1="276.3" y1="485.7" x2="276.3" y2="506.1" stroke="var(--down)" class="wick"/>
<rect x="275.03" y="490.2" width="2.46" height="4.9" fill="var(--down)"/>
<line x1="280.2" y1="487.8" x2="280.2" y2="505.7" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="494.3" width="2.46" height="10.2" fill="var(--down)"/>
<line x1="284.2" y1="491.6" x2="284.2" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="282.96" y="493.9" width="2.46" height="4.5" fill="var(--up)"/>
<line x1="288.2" y1="489.4" x2="288.2" y2="502.0" stroke="var(--down)" class="wick"/>
<rect x="286.93" y="494.3" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="292.1" y1="488.8" x2="292.1" y2="505.9" stroke="var(--up)" class="wick"/>
<rect x="290.90" y="494.1" width="2.46" height="5.1" fill="var(--up)"/>
<line x1="296.1" y1="455.2" x2="296.1" y2="488.6" stroke="var(--up)" class="wick"/>
<rect x="294.87" y="459.9" width="2.46" height="25.0" fill="var(--up)"/>
<line x1="300.1" y1="455.8" x2="300.1" y2="487.0" stroke="var(--down)" class="wick"/>
<rect x="298.83" y="455.8" width="2.46" height="11.2" fill="var(--down)"/>
<line x1="304.0" y1="460.3" x2="304.0" y2="475.8" stroke="var(--down)" class="wick"/>
<rect x="302.80" y="462.9" width="2.46" height="3.7" fill="var(--down)"/>
<line x1="308.0" y1="457.2" x2="308.0" y2="470.9" stroke="var(--up)" class="wick"/>
<rect x="306.77" y="461.3" width="2.46" height="5.5" fill="var(--up)"/>
<line x1="312.0" y1="454.4" x2="312.0" y2="463.6" stroke="var(--up)" class="wick"/>
<rect x="310.74" y="456.6" width="2.46" height="2.4" fill="var(--up)"/>
<line x1="315.9" y1="460.7" x2="315.9" y2="480.0" stroke="var(--down)" class="wick"/>
<rect x="314.71" y="466.8" width="2.46" height="12.8" fill="var(--down)"/>
<line x1="319.9" y1="482.5" x2="319.9" y2="509.4" stroke="var(--down)" class="wick"/>
<rect x="318.67" y="482.5" width="2.46" height="22.2" fill="var(--down)"/>
<line x1="323.9" y1="490.4" x2="323.9" y2="505.9" stroke="var(--down)" class="wick"/>
<rect x="322.64" y="500.6" width="2.46" height="1.4" fill="var(--down)"/>
<line x1="327.8" y1="491.6" x2="327.8" y2="510.6" stroke="var(--down)" class="wick"/>
<rect x="326.61" y="501.6" width="2.46" height="7.5" fill="var(--down)"/>
<line x1="331.8" y1="503.9" x2="331.8" y2="520.5" stroke="var(--down)" class="wick"/>
<rect x="330.58" y="511.6" width="2.46" height="6.3" fill="var(--down)"/>
<line x1="335.8" y1="510.4" x2="335.8" y2="527.9" stroke="var(--up)" class="wick"/>
<rect x="334.55" y="513.0" width="2.46" height="8.1" fill="var(--up)"/>
<line x1="339.7" y1="505.5" x2="339.7" y2="521.2" stroke="var(--down)" class="wick"/>
<rect x="338.51" y="510.6" width="2.46" height="5.5" fill="var(--down)"/>
<line x1="343.7" y1="507.5" x2="343.7" y2="522.2" stroke="var(--down)" class="wick"/>
<rect x="342.48" y="510.2" width="2.46" height="3.5" fill="var(--down)"/>
<line x1="347.7" y1="504.3" x2="347.7" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="346.45" y="507.1" width="2.46" height="28.3" fill="var(--down)"/>
<line x1="351.6" y1="505.7" x2="351.6" y2="536.8" stroke="var(--up)" class="wick"/>
<rect x="350.42" y="507.7" width="2.46" height="27.7" fill="var(--up)"/>
<line x1="355.6" y1="492.0" x2="355.6" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="354.39" y="498.8" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="359.6" y1="492.3" x2="359.6" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="358.35" y="492.3" width="2.46" height="18.3" fill="var(--down)"/>
<line x1="363.6" y1="499.8" x2="363.6" y2="511.8" stroke="var(--up)" class="wick"/>
<rect x="362.32" y="504.7" width="2.46" height="2.0" fill="var(--up)"/>
<line x1="367.5" y1="502.2" x2="367.5" y2="514.6" stroke="var(--up)" class="wick"/>
<rect x="366.29" y="510.8" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="371.5" y1="502.8" x2="371.5" y2="517.3" stroke="var(--up)" class="wick"/>
<rect x="370.26" y="516.7" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="375.5" y1="513.6" x2="375.5" y2="524.6" stroke="var(--up)" class="wick"/>
<rect x="374.23" y="513.8" width="2.46" height="5.5" fill="var(--up)"/>
<line x1="379.4" y1="512.8" x2="379.4" y2="524.0" stroke="var(--down)" class="wick"/>
<rect x="378.19" y="514.0" width="2.46" height="6.5" fill="var(--down)"/>
<line x1="383.4" y1="514.8" x2="383.4" y2="522.8" stroke="var(--up)" class="wick"/>
<rect x="382.16" y="515.7" width="2.46" height="4.1" fill="var(--up)"/>
<line x1="387.4" y1="514.8" x2="387.4" y2="523.2" stroke="var(--down)" class="wick"/>
<rect x="386.13" y="518.9" width="2.46" height="1.6" fill="var(--down)"/>
<line x1="391.3" y1="509.6" x2="391.3" y2="520.8" stroke="var(--up)" class="wick"/>
<rect x="390.10" y="514.8" width="2.46" height="3.1" fill="var(--up)"/>
<line x1="395.3" y1="513.2" x2="395.3" y2="521.8" stroke="var(--up)" class="wick"/>
<rect x="394.07" y="516.5" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="399.3" y1="514.8" x2="399.3" y2="520.3" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="516.5" width="2.46" height="3.1" fill="var(--down)"/>
<line x1="403.2" y1="520.5" x2="403.2" y2="537.9" stroke="var(--down)" class="wick"/>
<rect x="402.00" y="520.8" width="2.46" height="14.3" fill="var(--down)"/>
<line x1="407.2" y1="539.1" x2="407.2" y2="558.8" stroke="var(--down)" class="wick"/>
<rect x="405.97" y="539.1" width="2.46" height="19.3" fill="var(--down)"/>
<line x1="411.2" y1="552.3" x2="411.2" y2="565.3" stroke="var(--down)" class="wick"/>
<rect x="409.94" y="557.0" width="2.46" height="3.3" fill="var(--down)"/>
<line x1="415.1" y1="555.8" x2="415.1" y2="571.6" stroke="var(--down)" class="wick"/>
<rect x="413.91" y="557.4" width="2.46" height="8.8" fill="var(--down)"/>
<line x1="419.1" y1="528.5" x2="419.1" y2="568.0" stroke="var(--up)" class="wick"/>
<rect x="417.87" y="530.3" width="2.46" height="36.0" fill="var(--up)"/>
<line x1="423.1" y1="504.9" x2="423.1" y2="535.2" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="507.9" width="2.46" height="21.2" fill="var(--up)"/>
<line x1="427.0" y1="498.8" x2="427.0" y2="513.2" stroke="var(--down)" class="wick"/>
<rect x="425.81" y="500.2" width="2.46" height="7.9" fill="var(--down)"/>
<line x1="431.0" y1="493.5" x2="431.0" y2="512.6" stroke="var(--up)" class="wick"/>
<rect x="429.78" y="493.5" width="2.46" height="16.1" fill="var(--up)"/>
<line x1="435.0" y1="484.3" x2="435.0" y2="502.0" stroke="var(--up)" class="wick"/>
<rect x="433.75" y="489.6" width="2.46" height="5.3" fill="var(--up)"/>
<line x1="438.9" y1="486.4" x2="438.9" y2="510.6" stroke="var(--down)" class="wick"/>
<rect x="437.71" y="486.6" width="2.46" height="21.8" fill="var(--down)"/>
<line x1="442.9" y1="503.4" x2="442.9" y2="517.1" stroke="var(--up)" class="wick"/>
<rect x="441.68" y="509.2" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="446.9" y1="482.9" x2="446.9" y2="522.0" stroke="var(--up)" class="wick"/>
<rect x="445.65" y="483.5" width="2.46" height="34.4" fill="var(--up)"/>
<line x1="450.8" y1="473.9" x2="450.8" y2="501.6" stroke="var(--up)" class="wick"/>
<rect x="449.62" y="478.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="454.8" y1="477.8" x2="454.8" y2="489.6" stroke="var(--up)" class="wick"/>
<rect x="453.59" y="481.1" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="458.8" y1="457.8" x2="458.8" y2="482.9" stroke="var(--up)" class="wick"/>
<rect x="457.55" y="461.3" width="2.46" height="16.9" fill="var(--up)"/>
<line x1="462.8" y1="453.0" x2="462.8" y2="468.0" stroke="var(--down)" class="wick"/>
<rect x="461.52" y="461.7" width="2.46" height="5.9" fill="var(--down)"/>
<line x1="466.7" y1="447.9" x2="466.7" y2="473.3" stroke="var(--up)" class="wick"/>
<rect x="465.49" y="448.1" width="2.46" height="21.8" fill="var(--up)"/>
<line x1="470.7" y1="446.7" x2="470.7" y2="467.4" stroke="var(--down)" class="wick"/>
<rect x="469.46" y="454.8" width="2.46" height="2.9" fill="var(--down)"/>
<line x1="474.7" y1="437.5" x2="474.7" y2="456.2" stroke="var(--up)" class="wick"/>
<rect x="473.43" y="450.5" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="478.6" y1="421.6" x2="478.6" y2="448.3" stroke="var(--up)" class="wick"/>
<rect x="477.39" y="423.4" width="2.46" height="21.6" fill="var(--up)"/>
<line x1="482.6" y1="405.9" x2="482.6" y2="431.4" stroke="var(--up)" class="wick"/>
<rect x="481.36" y="413.1" width="2.46" height="6.3" fill="var(--up)"/>
<line x1="486.6" y1="370.5" x2="486.6" y2="417.1" stroke="var(--up)" class="wick"/>
<rect x="485.33" y="382.5" width="2.46" height="31.8" fill="var(--up)"/>
<line x1="490.5" y1="358.5" x2="490.5" y2="378.7" stroke="var(--up)" class="wick"/>
<rect x="489.30" y="373.4" width="2.46" height="1.6" fill="var(--up)"/>
<line x1="494.5" y1="343.8" x2="494.5" y2="368.7" stroke="var(--up)" class="wick"/>
<rect x="493.27" y="350.6" width="2.46" height="13.6" fill="var(--up)"/>
<line x1="498.5" y1="337.1" x2="498.5" y2="355.5" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="340.4" width="2.46" height="10.4" fill="var(--up)"/>
<line x1="502.4" y1="338.8" x2="502.4" y2="369.7" stroke="var(--down)" class="wick"/>
<rect x="501.20" y="347.5" width="2.46" height="13.8" fill="var(--down)"/>
<line x1="506.4" y1="370.3" x2="506.4" y2="399.8" stroke="var(--up)" class="wick"/>
<rect x="505.17" y="384.0" width="2.46" height="3.5" fill="var(--up)"/>
<line x1="510.4" y1="340.0" x2="510.4" y2="388.6" stroke="var(--up)" class="wick"/>
<rect x="509.14" y="348.9" width="2.46" height="33.8" fill="var(--up)"/>
<line x1="514.3" y1="313.3" x2="514.3" y2="345.1" stroke="var(--up)" class="wick"/>
<rect x="513.11" y="341.0" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="518.3" y1="333.1" x2="518.3" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="517.07" y="347.3" width="2.46" height="4.5" fill="var(--up)"/>
<line x1="522.3" y1="328.4" x2="522.3" y2="346.1" stroke="var(--up)" class="wick"/>
<rect x="521.04" y="330.0" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="526.2" y1="324.5" x2="526.2" y2="342.6" stroke="var(--down)" class="wick"/>
<rect x="525.01" y="331.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="530.2" y1="327.8" x2="530.2" y2="349.1" stroke="var(--down)" class="wick"/>
<rect x="528.98" y="332.0" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="534.2" y1="324.5" x2="534.2" y2="343.2" stroke="var(--up)" class="wick"/>
<rect x="532.95" y="324.5" width="2.46" height="10.0" fill="var(--up)"/>
<line x1="538.1" y1="304.6" x2="538.1" y2="331.2" stroke="var(--up)" class="wick"/>
<rect x="536.91" y="310.3" width="2.46" height="20.4" fill="var(--up)"/>
<line x1="542.1" y1="299.9" x2="542.1" y2="324.3" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="307.2" width="2.46" height="3.5" fill="var(--up)"/>
<line x1="546.1" y1="307.8" x2="546.1" y2="330.0" stroke="var(--up)" class="wick"/>
<rect x="544.85" y="312.1" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="550.0" y1="303.9" x2="550.0" y2="321.0" stroke="var(--down)" class="wick"/>
<rect x="548.82" y="306.6" width="2.46" height="4.9" fill="var(--down)"/>
<line x1="554.0" y1="282.0" x2="554.0" y2="305.2" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="290.7" width="2.46" height="12.2" fill="var(--up)"/>
<line x1="558.0" y1="293.8" x2="558.0" y2="318.4" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="296.8" width="2.46" height="20.2" fill="var(--down)"/>
<line x1="562.0" y1="319.8" x2="562.0" y2="349.6" stroke="var(--down)" class="wick"/>
<rect x="560.72" y="324.1" width="2.46" height="10.2" fill="var(--down)"/>
<line x1="565.9" y1="331.8" x2="565.9" y2="365.6" stroke="var(--down)" class="wick"/>
<rect x="564.69" y="335.3" width="2.46" height="23.4" fill="var(--down)"/>
<line x1="569.9" y1="366.2" x2="569.9" y2="390.1" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="366.9" width="2.46" height="12.8" fill="var(--down)"/>
<line x1="573.9" y1="376.6" x2="573.9" y2="393.1" stroke="var(--up)" class="wick"/>
<rect x="572.63" y="379.5" width="2.46" height="4.7" fill="var(--up)"/>
<line x1="577.8" y1="359.3" x2="577.8" y2="389.5" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="364.6" width="2.46" height="23.2" fill="var(--up)"/>
<line x1="581.8" y1="352.6" x2="581.8" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="580.56" y="363.0" width="2.46" height="7.9" fill="var(--up)"/>
<line x1="585.8" y1="366.4" x2="585.8" y2="388.2" stroke="var(--down)" class="wick"/>
<rect x="584.53" y="366.4" width="2.46" height="1.6" fill="var(--down)"/>
<line x1="589.7" y1="357.5" x2="589.7" y2="382.3" stroke="var(--up)" class="wick"/>
<rect x="588.50" y="368.3" width="2.46" height="3.7" fill="var(--up)"/>
<line x1="593.7" y1="359.7" x2="593.7" y2="376.6" stroke="var(--down)" class="wick"/>
<rect x="592.47" y="371.1" width="2.46" height="2.6" fill="var(--down)"/>
<line x1="597.7" y1="352.2" x2="597.7" y2="365.8" stroke="var(--down)" class="wick"/>
<rect x="596.43" y="360.7" width="2.46" height="3.5" fill="var(--down)"/>
<line x1="601.6" y1="354.8" x2="601.6" y2="371.5" stroke="var(--down)" class="wick"/>
<rect x="600.40" y="360.7" width="2.46" height="8.3" fill="var(--down)"/>
<line x1="605.6" y1="377.8" x2="605.6" y2="402.9" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="378.7" width="2.46" height="21.8" fill="var(--down)"/>
<line x1="609.6" y1="391.1" x2="609.6" y2="409.2" stroke="var(--down)" class="wick"/>
<rect x="608.34" y="400.0" width="2.46" height="8.8" fill="var(--down)"/>
<line x1="613.5" y1="399.0" x2="613.5" y2="431.6" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="408.4" width="2.46" height="16.1" fill="var(--down)"/>
<line x1="617.5" y1="410.8" x2="617.5" y2="428.5" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="412.9" width="2.46" height="4.5" fill="var(--down)"/>
<line x1="621.5" y1="406.1" x2="621.5" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="620.24" y="422.4" width="2.46" height="3.7" fill="var(--down)"/>
<line x1="625.4" y1="406.8" x2="625.4" y2="437.9" stroke="var(--up)" class="wick"/>
<rect x="624.21" y="414.7" width="2.46" height="13.0" fill="var(--up)"/>
<line x1="629.4" y1="404.9" x2="629.4" y2="426.5" stroke="var(--down)" class="wick"/>
<rect x="628.18" y="415.9" width="2.46" height="9.8" fill="var(--down)"/>
<line x1="633.4" y1="399.0" x2="633.4" y2="425.5" stroke="var(--up)" class="wick"/>
<rect x="632.15" y="405.7" width="2.46" height="17.5" fill="var(--up)"/>
<line x1="637.3" y1="380.3" x2="637.3" y2="405.5" stroke="var(--up)" class="wick"/>
<rect x="636.11" y="394.7" width="2.46" height="6.7" fill="var(--up)"/>
<line x1="641.3" y1="379.9" x2="641.3" y2="409.6" stroke="var(--down)" class="wick"/>
<rect x="640.08" y="389.5" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="645.3" y1="392.9" x2="645.3" y2="414.5" stroke="var(--down)" class="wick"/>
<rect x="644.05" y="397.0" width="2.46" height="1.4" fill="var(--down)"/>
<line x1="649.2" y1="381.1" x2="649.2" y2="397.6" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="385.8" width="2.46" height="2.8" fill="var(--up)"/>
<line x1="653.2" y1="374.8" x2="653.2" y2="395.6" stroke="var(--up)" class="wick"/>
<rect x="651.99" y="376.0" width="2.46" height="11.4" fill="var(--up)"/>
<line x1="657.2" y1="368.5" x2="657.2" y2="407.2" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="376.4" width="2.46" height="25.4" fill="var(--down)"/>
<line x1="661.2" y1="373.0" x2="661.2" y2="413.3" stroke="var(--up)" class="wick"/>
<rect x="659.92" y="374.6" width="2.46" height="29.1" fill="var(--up)"/>
<line x1="665.1" y1="355.0" x2="665.1" y2="392.7" stroke="var(--up)" class="wick"/>
<rect x="663.89" y="357.1" width="2.46" height="30.1" fill="var(--up)"/>
<line x1="669.1" y1="357.3" x2="669.1" y2="374.2" stroke="var(--down)" class="wick"/>
<rect x="667.86" y="361.0" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="673.1" y1="371.5" x2="673.1" y2="403.3" stroke="var(--down)" class="wick"/>
<rect x="671.83" y="374.0" width="2.46" height="17.9" fill="var(--down)"/>
<line x1="677.0" y1="387.8" x2="677.0" y2="403.9" stroke="var(--down)" class="wick"/>
<rect x="675.79" y="400.6" width="2.46" height="1.4" fill="var(--down)"/>
<line x1="681.0" y1="405.1" x2="681.0" y2="425.1" stroke="var(--down)" class="wick"/>
<rect x="679.76" y="405.1" width="2.46" height="8.5" fill="var(--down)"/>
<line x1="685.0" y1="403.1" x2="685.0" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="683.73" y="416.1" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="688.9" y1="398.8" x2="688.9" y2="423.6" stroke="var(--up)" class="wick"/>
<rect x="687.70" y="405.1" width="2.46" height="15.5" fill="var(--up)"/>
<line x1="692.9" y1="395.6" x2="692.9" y2="412.5" stroke="var(--down)" class="wick"/>
<rect x="691.67" y="403.5" width="2.46" height="6.7" fill="var(--down)"/>
<line x1="696.9" y1="409.2" x2="696.9" y2="427.1" stroke="var(--down)" class="wick"/>
<rect x="695.63" y="410.2" width="2.46" height="15.3" fill="var(--down)"/>
<line x1="700.8" y1="412.2" x2="700.8" y2="428.5" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="421.6" width="2.46" height="5.3" fill="var(--down)"/>
<line x1="704.8" y1="387.0" x2="704.8" y2="416.5" stroke="var(--up)" class="wick"/>
<rect x="703.57" y="394.5" width="2.46" height="16.5" fill="var(--up)"/>
<line x1="708.8" y1="380.1" x2="708.8" y2="396.6" stroke="var(--down)" class="wick"/>
<rect x="707.54" y="386.0" width="2.46" height="1.6" fill="var(--down)"/>
<line x1="712.7" y1="386.0" x2="712.7" y2="411.8" stroke="var(--down)" class="wick"/>
<rect x="711.51" y="386.0" width="2.46" height="25.0" fill="var(--down)"/>
<line x1="716.7" y1="315.1" x2="716.7" y2="359.1" stroke="var(--down)" class="wick"/>
<rect x="715.47" y="330.8" width="2.46" height="23.0" fill="var(--down)"/>
<line x1="720.7" y1="335.5" x2="720.7" y2="356.9" stroke="var(--up)" class="wick"/>
<rect x="719.44" y="343.6" width="2.46" height="9.8" fill="var(--up)"/>
<line x1="724.6" y1="338.6" x2="724.6" y2="354.2" stroke="var(--down)" class="wick"/>
<rect x="723.41" y="344.9" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="728.6" y1="328.4" x2="728.6" y2="359.9" stroke="var(--down)" class="wick"/>
<rect x="727.38" y="335.3" width="2.46" height="14.0" fill="var(--down)"/>
<line x1="732.6" y1="345.5" x2="732.6" y2="366.0" stroke="var(--up)" class="wick"/>
<rect x="731.35" y="356.9" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="736.5" y1="345.3" x2="736.5" y2="365.8" stroke="var(--up)" class="wick"/>
<rect x="735.31" y="351.2" width="2.46" height="5.7" fill="var(--up)"/>
<line x1="740.5" y1="334.5" x2="740.5" y2="349.5" stroke="var(--up)" class="wick"/>
<rect x="739.28" y="336.5" width="2.46" height="8.8" fill="var(--up)"/>
<line x1="744.5" y1="338.1" x2="744.5" y2="358.7" stroke="var(--down)" class="wick"/>
<rect x="743.25" y="345.1" width="2.46" height="7.1" fill="var(--down)"/>
<line x1="748.4" y1="337.1" x2="748.4" y2="358.3" stroke="var(--down)" class="wick"/>
<rect x="747.22" y="349.5" width="2.46" height="2.9" fill="var(--down)"/>
<line x1="752.4" y1="346.3" x2="752.4" y2="363.8" stroke="var(--up)" class="wick"/>
<rect x="751.19" y="347.7" width="2.46" height="9.8" fill="var(--up)"/>
<line x1="756.4" y1="315.1" x2="756.4" y2="355.2" stroke="var(--up)" class="wick"/>
<rect x="755.15" y="320.8" width="2.46" height="20.2" fill="var(--up)"/>
<line x1="760.4" y1="301.1" x2="760.4" y2="324.5" stroke="var(--up)" class="wick"/>
<rect x="759.12" y="316.2" width="2.46" height="7.7" fill="var(--up)"/>
<line x1="764.3" y1="303.3" x2="764.3" y2="323.1" stroke="var(--down)" class="wick"/>
<rect x="763.09" y="307.0" width="2.46" height="5.5" fill="var(--down)"/>
<line x1="768.3" y1="294.6" x2="768.3" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="294.6" width="2.46" height="10.6" fill="var(--down)"/>
<line x1="772.3" y1="294.0" x2="772.3" y2="313.7" stroke="var(--up)" class="wick"/>
<rect x="771.03" y="297.8" width="2.46" height="6.5" fill="var(--up)"/>
<line x1="776.2" y1="269.1" x2="776.2" y2="296.6" stroke="var(--up)" class="wick"/>
<rect x="774.99" y="283.6" width="2.46" height="10.0" fill="var(--up)"/>
<line x1="780.2" y1="274.2" x2="780.2" y2="291.5" stroke="var(--down)" class="wick"/>
<rect x="778.96" y="278.7" width="2.46" height="12.2" fill="var(--down)"/>
<line x1="784.2" y1="286.0" x2="784.2" y2="307.2" stroke="var(--down)" class="wick"/>
<rect x="782.93" y="286.2" width="2.46" height="12.2" fill="var(--down)"/>
<line x1="788.1" y1="288.3" x2="788.1" y2="303.3" stroke="var(--up)" class="wick"/>
<rect x="786.90" y="292.3" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="792.1" y1="289.9" x2="792.1" y2="316.6" stroke="var(--down)" class="wick"/>
<rect x="790.87" y="304.8" width="2.46" height="7.5" fill="var(--down)"/>
<line x1="796.1" y1="272.0" x2="796.1" y2="305.6" stroke="var(--up)" class="wick"/>
<rect x="794.83" y="289.5" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="800.0" y1="286.8" x2="800.0" y2="314.7" stroke="var(--down)" class="wick"/>
<rect x="798.80" y="295.4" width="2.46" height="17.9" fill="var(--down)"/>
<line x1="804.0" y1="314.9" x2="804.0" y2="342.8" stroke="var(--down)" class="wick"/>
<rect x="802.77" y="320.6" width="2.46" height="20.2" fill="var(--down)"/>
<line x1="808.0" y1="337.1" x2="808.0" y2="352.2" stroke="var(--up)" class="wick"/>
<rect x="806.74" y="348.1" width="2.46" height="1.2" fill="var(--up)"/>
<line x1="811.9" y1="337.1" x2="811.9" y2="355.7" stroke="var(--down)" class="wick"/>
<rect x="810.71" y="343.4" width="2.46" height="9.2" fill="var(--down)"/>
<line x1="815.9" y1="340.4" x2="815.9" y2="358.5" stroke="var(--up)" class="wick"/>
<rect x="814.67" y="345.7" width="2.46" height="9.2" fill="var(--up)"/>
<line x1="819.9" y1="320.6" x2="819.9" y2="384.0" stroke="var(--down)" class="wick"/>
<rect x="818.64" y="325.7" width="2.46" height="58.2" fill="var(--down)"/>
<line x1="823.8" y1="306.8" x2="823.8" y2="370.9" stroke="var(--up)" class="wick"/>
<rect x="822.61" y="331.6" width="2.46" height="38.7" fill="var(--up)"/>
<line x1="827.8" y1="322.7" x2="827.8" y2="339.0" stroke="var(--up)" class="wick"/>
<rect x="826.58" y="330.4" width="2.46" height="4.5" fill="var(--up)"/>
<line x1="831.8" y1="286.8" x2="831.8" y2="333.5" stroke="var(--up)" class="wick"/>
<rect x="830.55" y="295.0" width="2.46" height="35.2" fill="var(--up)"/>
<line x1="835.7" y1="245.7" x2="835.7" y2="279.7" stroke="var(--up)" class="wick"/>
<rect x="834.51" y="250.8" width="2.46" height="17.9" fill="var(--up)"/>
<line x1="839.7" y1="241.9" x2="839.7" y2="272.4" stroke="var(--down)" class="wick"/>
<rect x="838.48" y="244.3" width="2.46" height="27.3" fill="var(--down)"/>
<line x1="843.7" y1="264.5" x2="843.7" y2="284.6" stroke="var(--down)" class="wick"/>
<rect x="842.45" y="268.1" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="847.6" y1="297.8" x2="847.6" y2="316.4" stroke="var(--down)" class="wick"/>
<rect x="846.42" y="300.1" width="2.46" height="3.3" fill="var(--down)"/>
<line x1="851.6" y1="294.0" x2="851.6" y2="324.5" stroke="var(--down)" class="wick"/>
<rect x="850.39" y="298.7" width="2.46" height="17.1" fill="var(--down)"/>
<line x1="855.6" y1="314.9" x2="855.6" y2="341.2" stroke="var(--down)" class="wick"/>
<rect x="854.35" y="322.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="859.6" y1="321.1" x2="859.6" y2="346.1" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="323.9" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="863.5" y1="320.2" x2="863.5" y2="339.8" stroke="var(--up)" class="wick"/>
<rect x="862.29" y="330.6" width="2.46" height="5.5" fill="var(--up)"/>
<line x1="867.5" y1="295.2" x2="867.5" y2="324.7" stroke="var(--down)" class="wick"/>
<rect x="866.26" y="295.2" width="2.46" height="20.0" fill="var(--down)"/>
<line x1="871.5" y1="290.3" x2="871.5" y2="310.3" stroke="var(--down)" class="wick"/>
<rect x="870.23" y="303.9" width="2.46" height="5.7" fill="var(--down)"/>
<line x1="875.4" y1="294.2" x2="875.4" y2="321.9" stroke="var(--down)" class="wick"/>
<rect x="874.19" y="310.9" width="2.46" height="2.2" fill="var(--down)"/>
<line x1="879.4" y1="266.1" x2="879.4" y2="307.6" stroke="var(--up)" class="wick"/>
<rect x="878.16" y="269.7" width="2.46" height="32.8" fill="var(--up)"/>
<line x1="883.4" y1="250.2" x2="883.4" y2="277.9" stroke="var(--down)" class="wick"/>
<rect x="882.13" y="265.7" width="2.46" height="3.5" fill="var(--down)"/>
<line x1="887.3" y1="271.4" x2="887.3" y2="301.5" stroke="var(--down)" class="wick"/>
<rect x="886.10" y="272.2" width="2.46" height="24.2" fill="var(--down)"/>
<line x1="891.3" y1="282.4" x2="891.3" y2="302.5" stroke="var(--down)" class="wick"/>
<rect x="890.07" y="287.9" width="2.46" height="8.1" fill="var(--down)"/>
<line x1="895.3" y1="240.0" x2="895.3" y2="293.8" stroke="var(--up)" class="wick"/>
<rect x="894.03" y="240.0" width="2.46" height="49.3" fill="var(--up)"/>
<line x1="899.2" y1="231.7" x2="899.2" y2="275.7" stroke="var(--down)" class="wick"/>
<rect x="898.00" y="240.8" width="2.46" height="22.4" fill="var(--down)"/>
<line x1="903.2" y1="209.7" x2="903.2" y2="249.8" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="230.9" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="907.2" y1="226.4" x2="907.2" y2="257.1" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="239.4" width="2.46" height="15.1" fill="var(--down)"/>
<line x1="911.1" y1="265.9" x2="911.1" y2="287.7" stroke="var(--up)" class="wick"/>
<rect x="909.91" y="269.7" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="915.1" y1="247.8" x2="915.1" y2="274.0" stroke="var(--up)" class="wick"/>
<rect x="913.87" y="252.7" width="2.46" height="14.9" fill="var(--up)"/>
<line x1="919.1" y1="229.4" x2="919.1" y2="249.2" stroke="var(--up)" class="wick"/>
<rect x="917.84" y="237.8" width="2.46" height="6.9" fill="var(--up)"/>
<line x1="923.0" y1="230.3" x2="923.0" y2="260.8" stroke="var(--down)" class="wick"/>
<rect x="921.81" y="239.4" width="2.46" height="21.4" fill="var(--down)"/>
<line x1="927.0" y1="257.7" x2="927.0" y2="277.5" stroke="var(--down)" class="wick"/>
<rect x="925.78" y="263.8" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="931.0" y1="224.1" x2="931.0" y2="256.9" stroke="var(--up)" class="wick"/>
<rect x="929.75" y="224.6" width="2.46" height="27.9" fill="var(--up)"/>
<line x1="934.9" y1="212.1" x2="934.9" y2="305.0" stroke="var(--down)" class="wick"/>
<rect x="933.71" y="215.8" width="2.46" height="74.9" fill="var(--down)"/>
<line x1="938.9" y1="274.8" x2="938.9" y2="295.8" stroke="var(--up)" class="wick"/>
<rect x="937.68" y="279.7" width="2.46" height="11.2" fill="var(--up)"/>
<line x1="942.9" y1="274.2" x2="942.9" y2="295.4" stroke="var(--up)" class="wick"/>
<rect x="941.65" y="282.6" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="946.8" y1="264.0" x2="946.8" y2="282.8" stroke="var(--down)" class="wick"/>
<rect x="945.62" y="265.3" width="2.46" height="12.8" fill="var(--down)"/>
<line x1="950.8" y1="284.6" x2="950.8" y2="304.0" stroke="var(--down)" class="wick"/>
<rect x="949.59" y="288.5" width="2.46" height="9.8" fill="var(--down)"/>
<line x1="954.8" y1="275.5" x2="954.8" y2="303.7" stroke="var(--up)" class="wick"/>
<rect x="953.55" y="277.1" width="2.46" height="13.4" fill="var(--up)"/>
<line x1="958.8" y1="240.0" x2="958.8" y2="272.2" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="241.3" width="2.46" height="19.5" fill="var(--up)"/>
<line x1="962.7" y1="120.5" x2="962.7" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="158.2" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="966.7" y1="106.7" x2="966.7" y2="151.5" stroke="var(--up)" class="wick"/>
<rect x="965.46" y="142.9" width="2.46" height="8.5" fill="var(--up)"/>
<line x1="970.7" y1="151.5" x2="970.7" y2="179.6" stroke="var(--up)" class="wick"/>
<rect x="969.43" y="154.5" width="2.46" height="16.9" fill="var(--up)"/>
<line x1="974.6" y1="164.1" x2="974.6" y2="187.3" stroke="var(--down)" class="wick"/>
<rect x="973.39" y="170.8" width="2.46" height="1.4" fill="var(--down)"/>
<line x1="978.6" y1="154.7" x2="978.6" y2="191.0" stroke="var(--down)" class="wick"/>
<rect x="977.36" y="154.7" width="2.46" height="31.8" fill="var(--down)"/>
<line x1="982.6" y1="190.0" x2="982.6" y2="219.9" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="192.4" width="2.46" height="15.1" fill="var(--up)"/>
<line x1="986.5" y1="180.8" x2="986.5" y2="199.7" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="182.8" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="990.5" y1="164.7" x2="990.5" y2="195.2" stroke="var(--down)" class="wick"/>
<rect x="989.27" y="166.9" width="2.46" height="19.9" fill="var(--down)"/>
<line x1="994.5" y1="180.4" x2="994.5" y2="199.7" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="182.8" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="998.4" y1="173.3" x2="998.4" y2="195.0" stroke="var(--down)" class="wick"/>
<rect x="997.20" y="181.6" width="2.46" height="4.7" fill="var(--down)"/>
<line x1="1002.4" y1="182.8" x2="1002.4" y2="201.3" stroke="var(--down)" class="wick"/>
<rect x="1001.17" y="191.2" width="2.46" height="2.8" fill="var(--down)"/>
<line x1="1006.4" y1="178.1" x2="1006.4" y2="210.1" stroke="var(--up)" class="wick"/>
<rect x="1005.14" y="189.5" width="2.46" height="18.3" fill="var(--up)"/>
<line x1="1010.3" y1="169.0" x2="1010.3" y2="185.5" stroke="var(--up)" class="wick"/>
<rect x="1009.11" y="175.5" width="2.46" height="5.5" fill="var(--up)"/>
<line x1="1014.3" y1="164.7" x2="1014.3" y2="179.8" stroke="var(--up)" class="wick"/>
<rect x="1013.07" y="169.8" width="2.46" height="8.1" fill="var(--up)"/>
<line x1="1018.3" y1="163.7" x2="1018.3" y2="186.7" stroke="var(--down)" class="wick"/>
<rect x="1017.04" y="177.9" width="2.46" height="6.3" fill="var(--down)"/>
<line x1="1022.2" y1="145.2" x2="1022.2" y2="166.5" stroke="var(--up)" class="wick"/>
<rect x="1021.01" y="148.0" width="2.46" height="8.3" fill="var(--up)"/>
<line x1="1026.2" y1="109.9" x2="1026.2" y2="152.5" stroke="var(--up)" class="wick"/>
<rect x="1024.98" y="117.9" width="2.46" height="34.6" fill="var(--up)"/>
<line x1="1030.2" y1="88.0" x2="1030.2" y2="130.1" stroke="var(--up)" class="wick"/>
<rect x="1028.95" y="115.0" width="2.46" height="6.3" fill="var(--up)"/>
<line x1="1034.1" y1="101.2" x2="1034.1" y2="118.5" stroke="var(--up)" class="wick"/>
<rect x="1032.91" y="103.2" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="1038.1" y1="75.9" x2="1038.1" y2="96.3" stroke="var(--down)" class="wick"/>
<rect x="1036.88" y="83.1" width="2.46" height="2.6" fill="var(--down)"/>
<line x1="1042.1" y1="83.9" x2="1042.1" y2="99.2" stroke="var(--up)" class="wick"/>
<rect x="1040.85" y="92.6" width="2.46" height="1.4" fill="var(--up)"/>
<line x1="1046.0" y1="81.4" x2="1046.0" y2="124.8" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="81.4" width="2.46" height="41.9" fill="var(--down)"/>
<line x1="1050.0" y1="124.2" x2="1050.0" y2="145.2" stroke="var(--down)" class="wick"/>
<rect x="1048.79" y="136.4" width="2.46" height="6.9" fill="var(--down)"/>
<line x1="60" y1="215.0" x2="1052" y2="215.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="209.0" font-size="11.5" fill="var(--support)" font-weight="600">$85 S1</text>
<text x="1058" y="221.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="388.6" x2="1052" y2="388.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="382.6" font-size="11.5" fill="var(--support)" font-weight="600">$77 S2</text>
<text x="1058" y="394.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="433.2" x2="1052" y2="433.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="427.2" font-size="11.5" fill="var(--support)" font-weight="600">$74 S3</text>
<text x="1058" y="439.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="143.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="135.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $89 (2026-08-27)</text>
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
| **현재가** | **$89.06** (2026-08-27 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $85 | 2 | 2026-08-04·2026-08-12 스윙 저점대. 7월 실적 갭업 직후 눌림목이 만든 가장 최근 지지 |
| S2 | $77 | 2 | 2026-03-06·2026-06-04 스윙 저점대. 2월 실적 이후 상반기 내내 오간 박스권의 바닥 |
| S3 | $74 | 2 | 2026-03-25·2026-04-22 스윙 저점대. 4월 실적 갭업(2026-04-28 +3.9%) 직전의 저점 구간 |
| 참고선 | $92.49 | — | 52주 최고(2026-08-24). 터치가 1회뿐이라 클러스터로 잡히지 않았고, 저항으로 검증된 가격대가 아니다 |
| 참고선 | $65.35 | — | 52주 최저. 현재가에서 −27% 떨어져 있어 근시일 지지로 보기 어렵다 |

레벨이 전부 지지선(S)이고 저항선(R)이 하나도 없다 — **최근 1년 고점이 곧 현재가 부근**이라 위쪽에 스윙 고점 클러스터가 만들어지지 않았기 때문이다. 신고가 구간에서는 이 표가 하방 참고로만 쓰인다.

---

## 3. 관측된 특이 구간 — 2026-07-28 FY2026 Q2 실적발표

- FY2026 2분기 실적과 **연간 가이던스 상향**(유기적 매출 4~5%→약 5%, 비교 EPS 8~9%→9~10% 성장) 발표. [최근 뉴스 / 이슈](./08_news.md) 로그의 최상단 항목이다.
- 종가 기준 전일 대비 **+5.0%** ($84.07 → $88.27), 거래량은 평소(일 1,684만 주 내외) 대비 약 **2.1배**인 **3,498만 주**. 최근 1년 중 일간 변동폭·거래량 모두 최대인 날이다.
- 이 하루가 주가를 직전 박스권 상단($84~85) 위로 올려놓았고, 이후 8월 내내 $85 아래로 돌아가지 않았다. **S1($85)이 지지로 의미를 갖는 것은 이 갭 이후 눌림목이 그 가격에서 두 번 멈췄기 때문**이며, 그 이전 구간의 스윙 레벨(S2 $77·S3 $74)은 같은 레짐의 가격대가 아니다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 2. 지지선 / 저항선 요약 비고).
- **생성**: `scripts/gen_technical_chart.py KO --name "코카콜라" --close-on 2026-08-27 --emit all` (기본 옵션 그대로, `--force-level`·`--levels` 변경 없음)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - 3. 관측된 특이 구간의 2026-07-28 갭 이후 거래 레짐이 바뀌었으므로, **S2·S3는 갭 이전 구간의 가격대**라는 점을 감안해야 한다.
    - 기간 내 배당이 4회 있었고 이 차트는 원주가(배당 미반영)라, 실제 총수익 기준 저점은 표시된 값보다 낮다. 주식분할·유상증자 등 가격 연속성을 깨는 이벤트는 없었다(마지막 2:1 분할은 2012-08).

---

*작성일: 2026-08-30*
