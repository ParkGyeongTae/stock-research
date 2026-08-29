# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-08-27 종가 **$67.53**은 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)가 기준일 종가로 쓰는 값과 **일치한다.**
    - **최종 거래일이 아니다.** 실제 최종 거래일은 2026-08-28(종가 $64.39)이고, 수집 시점에 Yahoo 일봉이 이 날을 아직 채우지 않아 두 문서와 같은 2026-08-27을 기준일로 맞췄다. 주봉 문서는 원자료 사정상 2026-08-28까지 들어가 마지막 캔들의 기준일이 다르다([기술적 분석 — 주봉·5년](./10_technical_weekly.md) 4. 방법론 · 한계 참고).

---

## 1. 차트 — 최근 1년 일봉 (2025-08-29 ~ 2026-08-27)

<div class="rklb-chart">
<style>
.rklb-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .rklb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .rklb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.rklb-chart svg { width:100%; height:auto; display:block; }
.rklb-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.rklb-chart .title { fill: var(--ink); font-weight:600; }
.rklb-chart .grid { stroke: var(--grid); stroke-width:1; }
.rklb-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Rocket Lab(RKLB) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Rocket Lab (RKLB) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-29 ~ 2026-08-27 · 마지막 종가 $67.53 (2026-08-27) · 단위 USD</text>
<line x1="60" y1="591.1" x2="1052" y2="591.1" class="grid"/>
<text x="52" y="595.1" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="498.0" x2="1052" y2="498.0" class="grid"/>
<text x="52" y="502.0" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="405.0" x2="1052" y2="405.0" class="grid"/>
<text x="52" y="409.0" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="60" y1="311.9" x2="1052" y2="311.9" class="grid"/>
<text x="52" y="315.9" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="218.9" x2="1052" y2="218.9" class="grid"/>
<text x="52" y="222.9" font-size="11" text-anchor="end" fill="var(--muted)">120</text>
<line x1="60" y1="125.8" x2="1052" y2="125.8" class="grid"/>
<text x="52" y="129.8" font-size="11" text-anchor="end" fill="var(--muted)">140</text>
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
<line x1="60" y1="78.2" x2="1052" y2="78.2" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="81.2" font-size="10.5" fill="var(--muted)">$150 52주 최고 종가</text>
<line x1="60" y1="593.5" x2="1052" y2="593.5" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="596.5" font-size="10.5" fill="var(--muted)">$39 52주 최저 종가</text>
<line x1="748.4" y1="56.0" x2="748.4" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="754.4" y="68.0" font-size="10.5" fill="var(--down)">2026-05-08 Q1 실적 + 최대 발사계약 (+34%)</text>
<line x1="883.4" y1="56.0" x2="883.4" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="889.4" y="68.0" font-size="10.5" fill="var(--down)">2026-06-29 Iridium 인수 공시 (+16%)</text>
<line x1="62.0" y1="550.2" x2="62.0" y2="563.1" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="551.1" width="2.46" height="3.5" fill="var(--up)"/>
<line x1="66.0" y1="546.7" x2="66.0" y2="564.7" stroke="var(--up)" class="wick"/>
<rect x="64.72" y="547.8" width="2.46" height="11.9" fill="var(--up)"/>
<line x1="69.9" y1="540.4" x2="69.9" y2="574.8" stroke="var(--down)" class="wick"/>
<rect x="68.69" y="543.3" width="2.46" height="31.4" fill="var(--down)"/>
<line x1="73.9" y1="569.8" x2="73.9" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="72.66" y="571.7" width="2.46" height="5.4" fill="var(--down)"/>
<line x1="77.9" y1="563.2" x2="77.9" y2="580.0" stroke="var(--up)" class="wick"/>
<rect x="76.63" y="563.9" width="2.46" height="10.6" fill="var(--up)"/>
<line x1="81.8" y1="552.9" x2="81.8" y2="565.6" stroke="var(--up)" class="wick"/>
<rect x="80.59" y="555.1" width="2.46" height="10.4" fill="var(--up)"/>
<line x1="85.8" y1="556.1" x2="85.8" y2="565.5" stroke="var(--up)" class="wick"/>
<rect x="84.56" y="558.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="89.8" y1="553.4" x2="89.8" y2="565.0" stroke="var(--down)" class="wick"/>
<rect x="88.53" y="556.1" width="2.46" height="6.3" fill="var(--down)"/>
<line x1="93.7" y1="546.1" x2="93.7" y2="562.9" stroke="var(--up)" class="wick"/>
<rect x="92.50" y="551.9" width="2.46" height="9.8" fill="var(--up)"/>
<line x1="97.7" y1="525.8" x2="97.7" y2="551.0" stroke="var(--up)" class="wick"/>
<rect x="96.47" y="529.0" width="2.46" height="20.3" fill="var(--up)"/>
<line x1="101.7" y1="520.5" x2="101.7" y2="531.9" stroke="var(--up)" class="wick"/>
<rect x="100.43" y="525.8" width="2.46" height="2.1" fill="var(--up)"/>
<line x1="105.6" y1="534.9" x2="105.6" y2="558.5" stroke="var(--down)" class="wick"/>
<rect x="104.40" y="535.3" width="2.46" height="22.1" fill="var(--down)"/>
<line x1="109.6" y1="551.4" x2="109.6" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="108.37" y="553.5" width="2.46" height="2.4" fill="var(--up)"/>
<line x1="113.6" y1="548.3" x2="113.6" y2="558.5" stroke="var(--down)" class="wick"/>
<rect x="112.34" y="549.6" width="2.46" height="8.1" fill="var(--down)"/>
<line x1="117.5" y1="549.6" x2="117.5" y2="557.9" stroke="var(--up)" class="wick"/>
<rect x="116.31" y="554.9" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="121.5" y1="543.4" x2="121.5" y2="559.5" stroke="var(--up)" class="wick"/>
<rect x="120.27" y="545.5" width="2.46" height="12.5" fill="var(--up)"/>
<line x1="125.5" y1="525.2" x2="125.5" y2="554.3" stroke="var(--up)" class="wick"/>
<rect x="124.24" y="531.0" width="2.46" height="18.1" fill="var(--up)"/>
<line x1="129.4" y1="533.0" x2="129.4" y2="551.9" stroke="var(--down)" class="wick"/>
<rect x="128.21" y="536.2" width="2.46" height="14.4" fill="var(--down)"/>
<line x1="133.4" y1="551.0" x2="133.4" y2="566.9" stroke="var(--down)" class="wick"/>
<rect x="132.18" y="553.9" width="2.46" height="6.4" fill="var(--down)"/>
<line x1="137.4" y1="555.3" x2="137.4" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="557.1" width="2.46" height="4.8" fill="var(--down)"/>
<line x1="141.3" y1="553.4" x2="141.3" y2="561.5" stroke="var(--down)" class="wick"/>
<rect x="140.11" y="556.7" width="2.46" height="1.8" fill="var(--down)"/>
<line x1="145.3" y1="553.9" x2="145.3" y2="560.8" stroke="var(--up)" class="wick"/>
<rect x="144.08" y="554.3" width="2.46" height="3.3" fill="var(--up)"/>
<line x1="149.3" y1="547.3" x2="149.3" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="148.05" y="554.0" width="2.46" height="2.7" fill="var(--up)"/>
<line x1="153.2" y1="532.2" x2="153.2" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="152.02" y="533.1" width="2.46" height="17.8" fill="var(--up)"/>
<line x1="157.2" y1="512.3" x2="157.2" y2="538.7" stroke="var(--up)" class="wick"/>
<rect x="155.99" y="515.9" width="2.46" height="19.1" fill="var(--up)"/>
<line x1="161.2" y1="501.5" x2="161.2" y2="517.6" stroke="var(--up)" class="wick"/>
<rect x="159.95" y="505.0" width="2.46" height="7.6" fill="var(--up)"/>
<line x1="165.2" y1="486.1" x2="165.2" y2="511.9" stroke="var(--up)" class="wick"/>
<rect x="163.92" y="491.0" width="2.46" height="11.6" fill="var(--up)"/>
<line x1="169.1" y1="458.3" x2="169.1" y2="481.1" stroke="var(--up)" class="wick"/>
<rect x="167.89" y="473.3" width="2.46" height="5.4" fill="var(--up)"/>
<line x1="173.1" y1="458.3" x2="173.1" y2="477.5" stroke="var(--up)" class="wick"/>
<rect x="171.86" y="468.2" width="2.46" height="7.1" fill="var(--up)"/>
<line x1="177.1" y1="435.2" x2="177.1" y2="478.8" stroke="var(--down)" class="wick"/>
<rect x="175.83" y="447.8" width="2.46" height="30.4" fill="var(--down)"/>
<line x1="181.0" y1="449.5" x2="181.0" y2="476.5" stroke="var(--down)" class="wick"/>
<rect x="179.79" y="461.4" width="2.46" height="11.4" fill="var(--down)"/>
<line x1="185.0" y1="453.0" x2="185.0" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="183.76" y="460.7" width="2.46" height="12.5" fill="var(--up)"/>
<line x1="189.0" y1="433.0" x2="189.0" y2="465.1" stroke="var(--down)" class="wick"/>
<rect x="187.73" y="451.4" width="2.46" height="3.5" fill="var(--down)"/>
<line x1="192.9" y1="441.0" x2="192.9" y2="468.1" stroke="var(--down)" class="wick"/>
<rect x="191.70" y="451.2" width="2.46" height="14.3" fill="var(--down)"/>
<line x1="196.9" y1="458.5" x2="196.9" y2="480.8" stroke="var(--up)" class="wick"/>
<rect x="195.67" y="468.9" width="2.46" height="1.8" fill="var(--up)"/>
<line x1="200.9" y1="441.4" x2="200.9" y2="467.0" stroke="var(--down)" class="wick"/>
<rect x="199.63" y="455.5" width="2.46" height="8.3" fill="var(--down)"/>
<line x1="204.8" y1="460.6" x2="204.8" y2="475.4" stroke="var(--down)" class="wick"/>
<rect x="203.60" y="460.6" width="2.46" height="12.3" fill="var(--down)"/>
<line x1="208.8" y1="479.3" x2="208.8" y2="505.4" stroke="var(--down)" class="wick"/>
<rect x="207.57" y="484.2" width="2.46" height="11.2" fill="var(--down)"/>
<line x1="212.8" y1="476.2" x2="212.8" y2="494.6" stroke="var(--up)" class="wick"/>
<rect x="211.54" y="481.4" width="2.46" height="9.4" fill="var(--up)"/>
<line x1="216.7" y1="469.3" x2="216.7" y2="481.1" stroke="var(--down)" class="wick"/>
<rect x="215.51" y="475.7" width="2.46" height="1.2" fill="var(--down)"/>
<line x1="220.7" y1="468.5" x2="220.7" y2="478.7" stroke="var(--down)" class="wick"/>
<rect x="219.47" y="469.2" width="2.46" height="2.7" fill="var(--down)"/>
<line x1="224.7" y1="467.6" x2="224.7" y2="481.2" stroke="var(--down)" class="wick"/>
<rect x="223.44" y="471.6" width="2.46" height="9.0" fill="var(--down)"/>
<line x1="228.6" y1="463.7" x2="228.6" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="227.41" y="469.4" width="2.46" height="9.4" fill="var(--up)"/>
<line x1="232.6" y1="473.9" x2="232.6" y2="493.9" stroke="var(--down)" class="wick"/>
<rect x="231.38" y="474.8" width="2.46" height="19.0" fill="var(--down)"/>
<line x1="236.6" y1="482.0" x2="236.6" y2="496.2" stroke="var(--up)" class="wick"/>
<rect x="235.35" y="484.2" width="2.46" height="5.6" fill="var(--up)"/>
<line x1="240.5" y1="483.6" x2="240.5" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="239.31" y="483.9" width="2.46" height="7.9" fill="var(--down)"/>
<line x1="244.5" y1="500.4" x2="244.5" y2="514.3" stroke="var(--down)" class="wick"/>
<rect x="243.28" y="508.3" width="2.46" height="5.7" fill="var(--down)"/>
<line x1="248.5" y1="510.7" x2="248.5" y2="521.9" stroke="var(--down)" class="wick"/>
<rect x="247.25" y="513.6" width="2.46" height="1.1" fill="var(--down)"/>
<line x1="252.4" y1="515.7" x2="252.4" y2="547.3" stroke="var(--down)" class="wick"/>
<rect x="251.22" y="515.7" width="2.46" height="30.7" fill="var(--down)"/>
<line x1="256.4" y1="534.8" x2="256.4" y2="561.7" stroke="var(--up)" class="wick"/>
<rect x="255.19" y="536.9" width="2.46" height="18.5" fill="var(--up)"/>
<line x1="260.4" y1="523.6" x2="260.4" y2="541.0" stroke="var(--down)" class="wick"/>
<rect x="259.15" y="527.2" width="2.46" height="8.6" fill="var(--down)"/>
<line x1="264.4" y1="512.2" x2="264.4" y2="538.9" stroke="var(--down)" class="wick"/>
<rect x="263.12" y="516.7" width="2.46" height="22.1" fill="var(--down)"/>
<line x1="268.3" y1="519.8" x2="268.3" y2="546.2" stroke="var(--down)" class="wick"/>
<rect x="267.09" y="535.6" width="2.46" height="9.1" fill="var(--down)"/>
<line x1="272.3" y1="547.5" x2="272.3" y2="570.8" stroke="var(--down)" class="wick"/>
<rect x="271.06" y="550.3" width="2.46" height="16.3" fill="var(--down)"/>
<line x1="276.3" y1="557.5" x2="276.3" y2="575.7" stroke="var(--up)" class="wick"/>
<rect x="275.03" y="565.3" width="2.46" height="8.5" fill="var(--up)"/>
<line x1="280.2" y1="564.7" x2="280.2" y2="580.7" stroke="var(--down)" class="wick"/>
<rect x="278.99" y="567.1" width="2.46" height="8.6" fill="var(--down)"/>
<line x1="284.2" y1="574.3" x2="284.2" y2="585.4" stroke="var(--up)" class="wick"/>
<rect x="282.96" y="578.2" width="2.46" height="2.6" fill="var(--up)"/>
<line x1="288.2" y1="570.0" x2="288.2" y2="579.8" stroke="var(--up)" class="wick"/>
<rect x="286.93" y="574.3" width="2.46" height="5.2" fill="var(--up)"/>
<line x1="292.1" y1="562.0" x2="292.1" y2="594.3" stroke="var(--down)" class="wick"/>
<rect x="290.90" y="562.8" width="2.46" height="30.7" fill="var(--down)"/>
<line x1="296.1" y1="586.2" x2="296.1" y2="602.4" stroke="var(--up)" class="wick"/>
<rect x="294.87" y="589.7" width="2.46" height="2.2" fill="var(--up)"/>
<line x1="300.1" y1="579.3" x2="300.1" y2="594.4" stroke="var(--up)" class="wick"/>
<rect x="298.83" y="579.7" width="2.46" height="7.9" fill="var(--up)"/>
<line x1="304.0" y1="578.1" x2="304.0" y2="589.3" stroke="var(--up)" class="wick"/>
<rect x="302.80" y="579.0" width="2.46" height="2.7" fill="var(--up)"/>
<line x1="308.0" y1="574.4" x2="308.0" y2="584.7" stroke="var(--down)" class="wick"/>
<rect x="306.77" y="576.0" width="2.46" height="6.1" fill="var(--down)"/>
<line x1="312.0" y1="578.5" x2="312.0" y2="582.7" stroke="var(--down)" class="wick"/>
<rect x="310.74" y="579.4" width="2.46" height="1.7" fill="var(--down)"/>
<line x1="315.9" y1="585.1" x2="315.9" y2="591.2" stroke="var(--down)" class="wick"/>
<rect x="314.71" y="585.8" width="2.46" height="3.6" fill="var(--down)"/>
<line x1="319.9" y1="577.2" x2="319.9" y2="589.1" stroke="var(--up)" class="wick"/>
<rect x="318.67" y="582.3" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="323.9" y1="569.0" x2="323.9" y2="584.1" stroke="var(--up)" class="wick"/>
<rect x="322.64" y="569.1" width="2.46" height="13.1" fill="var(--up)"/>
<line x1="327.8" y1="546.1" x2="327.8" y2="568.7" stroke="var(--up)" class="wick"/>
<rect x="326.61" y="547.5" width="2.46" height="17.3" fill="var(--up)"/>
<line x1="331.8" y1="546.0" x2="331.8" y2="555.3" stroke="var(--up)" class="wick"/>
<rect x="330.58" y="549.0" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="335.8" y1="533.5" x2="335.8" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="334.55" y="537.3" width="2.46" height="6.9" fill="var(--up)"/>
<line x1="339.7" y1="527.1" x2="339.7" y2="543.0" stroke="var(--up)" class="wick"/>
<rect x="338.51" y="528.6" width="2.46" height="10.2" fill="var(--up)"/>
<line x1="343.7" y1="503.5" x2="343.7" y2="534.1" stroke="var(--up)" class="wick"/>
<rect x="342.48" y="509.6" width="2.46" height="19.0" fill="var(--up)"/>
<line x1="347.7" y1="478.7" x2="347.7" y2="512.7" stroke="var(--up)" class="wick"/>
<rect x="346.45" y="481.6" width="2.46" height="28.0" fill="var(--up)"/>
<line x1="351.6" y1="473.9" x2="351.6" y2="499.0" stroke="var(--down)" class="wick"/>
<rect x="350.42" y="486.4" width="2.46" height="4.7" fill="var(--down)"/>
<line x1="355.6" y1="476.8" x2="355.6" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="354.39" y="483.8" width="2.46" height="35.6" fill="var(--down)"/>
<line x1="359.6" y1="513.3" x2="359.6" y2="532.1" stroke="var(--up)" class="wick"/>
<rect x="358.35" y="519.0" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="363.6" y1="512.4" x2="363.6" y2="530.2" stroke="var(--down)" class="wick"/>
<rect x="362.32" y="516.2" width="2.46" height="10.0" fill="var(--down)"/>
<line x1="367.5" y1="496.9" x2="367.5" y2="516.5" stroke="var(--up)" class="wick"/>
<rect x="366.29" y="498.4" width="2.46" height="17.3" fill="var(--up)"/>
<line x1="371.5" y1="448.9" x2="371.5" y2="494.6" stroke="var(--up)" class="wick"/>
<rect x="370.26" y="449.1" width="2.46" height="43.7" fill="var(--up)"/>
<line x1="375.5" y1="412.2" x2="375.5" y2="438.7" stroke="var(--up)" class="wick"/>
<rect x="374.23" y="416.4" width="2.46" height="21.5" fill="var(--up)"/>
<line x1="379.4" y1="408.8" x2="379.4" y2="436.2" stroke="var(--up)" class="wick"/>
<rect x="378.19" y="418.1" width="2.46" height="15.7" fill="var(--up)"/>
<line x1="383.4" y1="405.8" x2="383.4" y2="429.2" stroke="var(--down)" class="wick"/>
<rect x="382.16" y="414.1" width="2.46" height="4.0" fill="var(--down)"/>
<line x1="387.4" y1="419.0" x2="387.4" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="386.13" y="420.4" width="2.46" height="28.1" fill="var(--down)"/>
<line x1="391.3" y1="438.8" x2="391.3" y2="454.7" stroke="var(--up)" class="wick"/>
<rect x="390.10" y="451.0" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="395.3" y1="429.7" x2="395.3" y2="449.5" stroke="var(--down)" class="wick"/>
<rect x="394.07" y="437.4" width="2.46" height="12.0" fill="var(--down)"/>
<line x1="399.3" y1="436.6" x2="399.3" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="398.03" y="444.5" width="2.46" height="8.1" fill="var(--down)"/>
<line x1="403.2" y1="422.5" x2="403.2" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="402.00" y="423.6" width="2.46" height="24.9" fill="var(--up)"/>
<line x1="407.2" y1="413.1" x2="407.2" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="405.97" y="413.6" width="2.46" height="16.4" fill="var(--up)"/>
<line x1="411.2" y1="375.9" x2="411.2" y2="432.7" stroke="var(--up)" class="wick"/>
<rect x="409.94" y="376.9" width="2.46" height="38.5" fill="var(--up)"/>
<line x1="415.1" y1="377.2" x2="415.1" y2="396.4" stroke="var(--down)" class="wick"/>
<rect x="413.91" y="385.9" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="419.1" y1="359.1" x2="419.1" y2="394.5" stroke="var(--down)" class="wick"/>
<rect x="417.87" y="379.4" width="2.46" height="11.3" fill="var(--down)"/>
<line x1="423.1" y1="365.8" x2="423.1" y2="393.6" stroke="var(--up)" class="wick"/>
<rect x="421.84" y="382.4" width="2.46" height="1.5" fill="var(--up)"/>
<line x1="427.0" y1="363.8" x2="427.0" y2="389.1" stroke="var(--up)" class="wick"/>
<rect x="425.81" y="368.2" width="2.46" height="13.6" fill="var(--up)"/>
<line x1="431.0" y1="359.7" x2="431.0" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="429.78" y="362.5" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="435.0" y1="348.3" x2="435.0" y2="384.0" stroke="var(--up)" class="wick"/>
<rect x="433.75" y="350.1" width="2.46" height="25.4" fill="var(--up)"/>
<line x1="438.9" y1="347.0" x2="438.9" y2="374.0" stroke="var(--up)" class="wick"/>
<rect x="437.71" y="354.9" width="2.46" height="7.0" fill="var(--up)"/>
<line x1="442.9" y1="313.9" x2="442.9" y2="347.3" stroke="var(--up)" class="wick"/>
<rect x="441.68" y="329.1" width="2.46" height="17.6" fill="var(--up)"/>
<line x1="446.9" y1="320.0" x2="446.9" y2="366.4" stroke="var(--down)" class="wick"/>
<rect x="445.65" y="341.2" width="2.46" height="21.1" fill="var(--down)"/>
<line x1="450.8" y1="352.6" x2="450.8" y2="392.4" stroke="var(--down)" class="wick"/>
<rect x="449.62" y="358.4" width="2.46" height="10.2" fill="var(--down)"/>
<line x1="454.8" y1="361.2" x2="454.8" y2="398.7" stroke="var(--up)" class="wick"/>
<rect x="453.59" y="367.8" width="2.46" height="7.4" fill="var(--up)"/>
<line x1="458.8" y1="337.7" x2="458.8" y2="376.5" stroke="var(--down)" class="wick"/>
<rect x="457.55" y="362.8" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="462.8" y1="371.7" x2="462.8" y2="404.9" stroke="var(--down)" class="wick"/>
<rect x="461.52" y="373.6" width="2.46" height="29.2" fill="var(--down)"/>
<line x1="466.7" y1="372.4" x2="466.7" y2="395.7" stroke="var(--up)" class="wick"/>
<rect x="465.49" y="372.4" width="2.46" height="19.1" fill="var(--up)"/>
<line x1="470.7" y1="359.4" x2="470.7" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="469.46" y="365.1" width="2.46" height="6.3" fill="var(--up)"/>
<line x1="474.7" y1="363.1" x2="474.7" y2="391.0" stroke="var(--down)" class="wick"/>
<rect x="473.43" y="368.0" width="2.46" height="10.5" fill="var(--down)"/>
<line x1="478.6" y1="361.6" x2="478.6" y2="414.2" stroke="var(--down)" class="wick"/>
<rect x="477.39" y="381.7" width="2.46" height="22.9" fill="var(--down)"/>
<line x1="482.6" y1="401.7" x2="482.6" y2="433.5" stroke="var(--down)" class="wick"/>
<rect x="481.36" y="408.9" width="2.46" height="23.3" fill="var(--down)"/>
<line x1="486.6" y1="398.8" x2="486.6" y2="424.7" stroke="var(--up)" class="wick"/>
<rect x="485.33" y="399.1" width="2.46" height="12.4" fill="var(--up)"/>
<line x1="490.5" y1="398.7" x2="490.5" y2="458.2" stroke="var(--down)" class="wick"/>
<rect x="489.30" y="398.7" width="2.46" height="38.3" fill="var(--down)"/>
<line x1="494.5" y1="437.6" x2="494.5" y2="473.8" stroke="var(--down)" class="wick"/>
<rect x="493.27" y="451.6" width="2.46" height="17.0" fill="var(--down)"/>
<line x1="498.5" y1="439.1" x2="498.5" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="497.23" y="440.7" width="2.46" height="15.4" fill="var(--up)"/>
<line x1="502.4" y1="419.9" x2="502.4" y2="448.0" stroke="var(--up)" class="wick"/>
<rect x="501.20" y="424.3" width="2.46" height="17.8" fill="var(--up)"/>
<line x1="506.4" y1="424.2" x2="506.4" y2="444.3" stroke="var(--down)" class="wick"/>
<rect x="505.17" y="430.1" width="2.46" height="11.9" fill="var(--down)"/>
<line x1="510.4" y1="435.7" x2="510.4" y2="465.4" stroke="var(--down)" class="wick"/>
<rect x="509.14" y="436.9" width="2.46" height="16.3" fill="var(--down)"/>
<line x1="514.3" y1="458.7" x2="514.3" y2="480.0" stroke="var(--down)" class="wick"/>
<rect x="513.11" y="463.0" width="2.46" height="7.1" fill="var(--down)"/>
<line x1="518.3" y1="453.4" x2="518.3" y2="472.4" stroke="var(--up)" class="wick"/>
<rect x="517.07" y="463.4" width="2.46" height="3.5" fill="var(--up)"/>
<line x1="522.3" y1="446.9" x2="522.3" y2="474.8" stroke="var(--up)" class="wick"/>
<rect x="521.04" y="452.0" width="2.46" height="17.7" fill="var(--up)"/>
<line x1="526.2" y1="424.7" x2="526.2" y2="451.6" stroke="var(--up)" class="wick"/>
<rect x="525.01" y="430.9" width="2.46" height="15.9" fill="var(--up)"/>
<line x1="530.2" y1="418.4" x2="530.2" y2="440.6" stroke="var(--up)" class="wick"/>
<rect x="528.98" y="420.9" width="2.46" height="17.1" fill="var(--up)"/>
<line x1="534.2" y1="413.4" x2="534.2" y2="454.3" stroke="var(--down)" class="wick"/>
<rect x="532.95" y="426.0" width="2.46" height="21.5" fill="var(--down)"/>
<line x1="538.1" y1="445.7" x2="538.1" y2="458.5" stroke="var(--up)" class="wick"/>
<rect x="536.91" y="450.5" width="2.46" height="6.8" fill="var(--up)"/>
<line x1="542.1" y1="451.3" x2="542.1" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="540.88" y="451.6" width="2.46" height="5.1" fill="var(--up)"/>
<line x1="546.1" y1="442.9" x2="546.1" y2="456.7" stroke="var(--down)" class="wick"/>
<rect x="544.85" y="446.4" width="2.46" height="4.2" fill="var(--down)"/>
<line x1="550.0" y1="438.8" x2="550.0" y2="457.0" stroke="var(--up)" class="wick"/>
<rect x="548.82" y="439.2" width="2.46" height="12.1" fill="var(--up)"/>
<line x1="554.0" y1="453.4" x2="554.0" y2="479.0" stroke="var(--up)" class="wick"/>
<rect x="552.79" y="455.7" width="2.46" height="7.0" fill="var(--up)"/>
<line x1="558.0" y1="441.7" x2="558.0" y2="468.0" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="447.0" width="2.46" height="20.0" fill="var(--up)"/>
<line x1="562.0" y1="436.4" x2="562.0" y2="469.2" stroke="var(--up)" class="wick"/>
<rect x="560.72" y="450.9" width="2.46" height="5.9" fill="var(--up)"/>
<line x1="565.9" y1="432.4" x2="565.9" y2="454.0" stroke="var(--up)" class="wick"/>
<rect x="564.69" y="442.6" width="2.46" height="5.1" fill="var(--up)"/>
<line x1="569.9" y1="440.8" x2="569.9" y2="463.9" stroke="var(--down)" class="wick"/>
<rect x="568.66" y="447.2" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="573.9" y1="427.7" x2="573.9" y2="460.2" stroke="var(--up)" class="wick"/>
<rect x="572.63" y="451.0" width="2.46" height="9.2" fill="var(--up)"/>
<line x1="577.8" y1="441.6" x2="577.8" y2="461.7" stroke="var(--up)" class="wick"/>
<rect x="576.59" y="444.6" width="2.46" height="9.7" fill="var(--up)"/>
<line x1="581.8" y1="437.9" x2="581.8" y2="457.9" stroke="var(--down)" class="wick"/>
<rect x="580.56" y="449.9" width="2.46" height="6.6" fill="var(--down)"/>
<line x1="585.8" y1="436.2" x2="585.8" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="584.53" y="442.4" width="2.46" height="14.7" fill="var(--up)"/>
<line x1="589.7" y1="439.4" x2="589.7" y2="459.5" stroke="var(--down)" class="wick"/>
<rect x="588.50" y="442.4" width="2.46" height="16.7" fill="var(--down)"/>
<line x1="593.7" y1="445.4" x2="593.7" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="592.47" y="455.5" width="2.46" height="3.4" fill="var(--down)"/>
<line x1="597.7" y1="440.4" x2="597.7" y2="457.7" stroke="var(--up)" class="wick"/>
<rect x="596.43" y="445.4" width="2.46" height="9.2" fill="var(--up)"/>
<line x1="601.6" y1="411.2" x2="601.6" y2="445.6" stroke="var(--up)" class="wick"/>
<rect x="600.40" y="411.5" width="2.46" height="33.1" fill="var(--up)"/>
<line x1="605.6" y1="419.5" x2="605.6" y2="454.3" stroke="var(--down)" class="wick"/>
<rect x="604.37" y="423.4" width="2.46" height="30.5" fill="var(--down)"/>
<line x1="609.6" y1="438.8" x2="609.6" y2="460.8" stroke="var(--up)" class="wick"/>
<rect x="608.34" y="442.5" width="2.46" height="14.5" fill="var(--up)"/>
<line x1="613.5" y1="433.0" x2="613.5" y2="468.3" stroke="var(--down)" class="wick"/>
<rect x="612.31" y="442.2" width="2.46" height="22.2" fill="var(--down)"/>
<line x1="617.5" y1="454.1" x2="617.5" y2="469.9" stroke="var(--down)" class="wick"/>
<rect x="616.27" y="460.4" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="621.5" y1="458.0" x2="621.5" y2="477.3" stroke="var(--down)" class="wick"/>
<rect x="620.24" y="465.5" width="2.46" height="4.3" fill="var(--down)"/>
<line x1="625.4" y1="428.0" x2="625.4" y2="456.4" stroke="var(--up)" class="wick"/>
<rect x="624.21" y="438.1" width="2.46" height="18.3" fill="var(--up)"/>
<line x1="629.4" y1="441.8" x2="629.4" y2="472.0" stroke="var(--down)" class="wick"/>
<rect x="628.18" y="445.9" width="2.46" height="24.5" fill="var(--down)"/>
<line x1="633.4" y1="469.7" x2="633.4" y2="496.4" stroke="var(--down)" class="wick"/>
<rect x="632.15" y="470.1" width="2.46" height="23.6" fill="var(--down)"/>
<line x1="637.3" y1="490.4" x2="637.3" y2="516.0" stroke="var(--down)" class="wick"/>
<rect x="636.11" y="491.3" width="2.46" height="18.9" fill="var(--down)"/>
<line x1="641.3" y1="476.7" x2="641.3" y2="502.6" stroke="var(--up)" class="wick"/>
<rect x="640.08" y="478.4" width="2.46" height="11.7" fill="var(--up)"/>
<line x1="645.3" y1="457.7" x2="645.3" y2="473.4" stroke="var(--up)" class="wick"/>
<rect x="644.05" y="472.4" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="649.2" y1="454.3" x2="649.2" y2="489.4" stroke="var(--up)" class="wick"/>
<rect x="648.02" y="462.1" width="2.46" height="25.6" fill="var(--up)"/>
<line x1="653.2" y1="450.0" x2="653.2" y2="467.3" stroke="var(--down)" class="wick"/>
<rect x="651.99" y="462.1" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="657.2" y1="459.4" x2="657.2" y2="479.6" stroke="var(--down)" class="wick"/>
<rect x="655.95" y="464.9" width="2.46" height="3.7" fill="var(--down)"/>
<line x1="661.2" y1="434.4" x2="661.2" y2="461.7" stroke="var(--down)" class="wick"/>
<rect x="659.92" y="442.2" width="2.46" height="13.6" fill="var(--down)"/>
<line x1="665.1" y1="452.5" x2="665.1" y2="467.6" stroke="var(--down)" class="wick"/>
<rect x="663.89" y="455.9" width="2.46" height="10.8" fill="var(--down)"/>
<line x1="669.1" y1="451.2" x2="669.1" y2="468.5" stroke="var(--up)" class="wick"/>
<rect x="667.86" y="460.6" width="2.46" height="1.6" fill="var(--up)"/>
<line x1="673.1" y1="444.3" x2="673.1" y2="467.4" stroke="var(--up)" class="wick"/>
<rect x="671.83" y="448.6" width="2.46" height="16.6" fill="var(--up)"/>
<line x1="677.0" y1="429.4" x2="677.0" y2="449.3" stroke="var(--down)" class="wick"/>
<rect x="675.79" y="435.0" width="2.46" height="6.2" fill="var(--down)"/>
<line x1="681.0" y1="430.2" x2="681.0" y2="453.4" stroke="var(--up)" class="wick"/>
<rect x="679.76" y="434.8" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="685.0" y1="388.7" x2="685.0" y2="419.4" stroke="var(--up)" class="wick"/>
<rect x="683.73" y="391.3" width="2.46" height="27.7" fill="var(--up)"/>
<line x1="688.9" y1="372.5" x2="688.9" y2="388.2" stroke="var(--up)" class="wick"/>
<rect x="687.70" y="382.6" width="2.46" height="3.4" fill="var(--up)"/>
<line x1="692.9" y1="356.8" x2="692.9" y2="383.6" stroke="var(--up)" class="wick"/>
<rect x="691.67" y="361.0" width="2.46" height="21.5" fill="var(--up)"/>
<line x1="696.9" y1="349.4" x2="696.9" y2="378.2" stroke="var(--down)" class="wick"/>
<rect x="695.63" y="356.9" width="2.46" height="17.2" fill="var(--down)"/>
<line x1="700.8" y1="344.0" x2="700.8" y2="368.9" stroke="var(--down)" class="wick"/>
<rect x="699.60" y="356.3" width="2.46" height="2.0" fill="var(--down)"/>
<line x1="704.8" y1="357.1" x2="704.8" y2="397.7" stroke="var(--down)" class="wick"/>
<rect x="703.57" y="359.1" width="2.46" height="24.4" fill="var(--down)"/>
<line x1="708.8" y1="375.2" x2="708.8" y2="409.3" stroke="var(--down)" class="wick"/>
<rect x="707.54" y="375.5" width="2.46" height="31.0" fill="var(--down)"/>
<line x1="712.7" y1="393.4" x2="712.7" y2="418.7" stroke="var(--up)" class="wick"/>
<rect x="711.51" y="394.3" width="2.46" height="12.1" fill="var(--up)"/>
<line x1="716.7" y1="396.7" x2="716.7" y2="416.1" stroke="var(--down)" class="wick"/>
<rect x="715.47" y="404.6" width="2.46" height="6.9" fill="var(--down)"/>
<line x1="720.7" y1="414.2" x2="720.7" y2="432.9" stroke="var(--down)" class="wick"/>
<rect x="719.44" y="414.9" width="2.46" height="3.9" fill="var(--down)"/>
<line x1="724.6" y1="388.3" x2="724.6" y2="416.8" stroke="var(--up)" class="wick"/>
<rect x="723.41" y="393.3" width="2.46" height="23.1" fill="var(--up)"/>
<line x1="728.6" y1="387.3" x2="728.6" y2="412.3" stroke="var(--down)" class="wick"/>
<rect x="727.38" y="388.6" width="2.46" height="22.0" fill="var(--down)"/>
<line x1="732.6" y1="396.5" x2="732.6" y2="422.4" stroke="var(--up)" class="wick"/>
<rect x="731.35" y="403.5" width="2.46" height="9.1" fill="var(--up)"/>
<line x1="736.5" y1="391.0" x2="736.5" y2="421.0" stroke="var(--down)" class="wick"/>
<rect x="735.31" y="392.9" width="2.46" height="17.9" fill="var(--down)"/>
<line x1="740.5" y1="383.2" x2="740.5" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="739.28" y="383.3" width="2.46" height="23.4" fill="var(--up)"/>
<line x1="744.5" y1="382.7" x2="744.5" y2="414.6" stroke="var(--down)" class="wick"/>
<rect x="743.25" y="383.1" width="2.46" height="28.5" fill="var(--down)"/>
<line x1="748.4" y1="285.8" x2="748.4" y2="377.7" stroke="var(--up)" class="wick"/>
<rect x="747.22" y="286.5" width="2.46" height="90.4" fill="var(--up)"/>
<line x1="752.4" y1="200.5" x2="752.4" y2="293.3" stroke="var(--up)" class="wick"/>
<rect x="751.19" y="231.2" width="2.46" height="56.2" fill="var(--up)"/>
<line x1="756.4" y1="211.9" x2="756.4" y2="254.2" stroke="var(--up)" class="wick"/>
<rect x="755.15" y="230.2" width="2.46" height="22.3" fill="var(--up)"/>
<line x1="760.4" y1="185.2" x2="760.4" y2="233.3" stroke="var(--up)" class="wick"/>
<rect x="759.12" y="199.5" width="2.46" height="1.2" fill="var(--up)"/>
<line x1="764.3" y1="157.5" x2="764.3" y2="212.8" stroke="var(--up)" class="wick"/>
<rect x="763.09" y="160.5" width="2.46" height="44.0" fill="var(--up)"/>
<line x1="768.3" y1="170.6" x2="768.3" y2="210.5" stroke="var(--down)" class="wick"/>
<rect x="767.06" y="181.2" width="2.46" height="15.5" fill="var(--down)"/>
<line x1="772.3" y1="133.3" x2="772.3" y2="192.5" stroke="var(--down)" class="wick"/>
<rect x="771.03" y="159.5" width="2.46" height="7.4" fill="var(--down)"/>
<line x1="776.2" y1="174.3" x2="776.2" y2="241.1" stroke="var(--up)" class="wick"/>
<rect x="774.99" y="184.8" width="2.46" height="6.2" fill="var(--up)"/>
<line x1="780.2" y1="147.4" x2="780.2" y2="199.2" stroke="var(--up)" class="wick"/>
<rect x="778.96" y="152.4" width="2.46" height="31.6" fill="var(--up)"/>
<line x1="784.2" y1="168.3" x2="784.2" y2="201.2" stroke="var(--down)" class="wick"/>
<rect x="782.93" y="190.3" width="2.46" height="3.2" fill="var(--down)"/>
<line x1="788.1" y1="126.9" x2="788.1" y2="166.2" stroke="var(--up)" class="wick"/>
<rect x="786.90" y="145.5" width="2.46" height="20.2" fill="var(--up)"/>
<line x1="792.1" y1="97.9" x2="792.1" y2="132.5" stroke="var(--up)" class="wick"/>
<rect x="790.87" y="110.9" width="2.46" height="5.7" fill="var(--up)"/>
<line x1="796.1" y1="74.6" x2="796.1" y2="135.5" stroke="var(--up)" class="wick"/>
<rect x="794.83" y="78.2" width="2.46" height="2.4" fill="var(--up)"/>
<line x1="800.0" y1="75.4" x2="800.0" y2="114.8" stroke="var(--up)" class="wick"/>
<rect x="798.80" y="88.4" width="2.46" height="4.0" fill="var(--up)"/>
<line x1="804.0" y1="107.2" x2="804.0" y2="153.5" stroke="var(--up)" class="wick"/>
<rect x="802.77" y="109.6" width="2.46" height="16.5" fill="var(--up)"/>
<line x1="808.0" y1="146.1" x2="808.0" y2="214.2" stroke="var(--down)" class="wick"/>
<rect x="806.74" y="161.3" width="2.46" height="46.5" fill="var(--down)"/>
<line x1="811.9" y1="179.8" x2="811.9" y2="206.9" stroke="var(--down)" class="wick"/>
<rect x="810.71" y="194.0" width="2.46" height="9.4" fill="var(--down)"/>
<line x1="815.9" y1="207.2" x2="815.9" y2="248.4" stroke="var(--down)" class="wick"/>
<rect x="814.67" y="220.8" width="2.46" height="22.7" fill="var(--down)"/>
<line x1="819.9" y1="206.6" x2="819.9" y2="263.6" stroke="var(--up)" class="wick"/>
<rect x="818.64" y="219.1" width="2.46" height="31.9" fill="var(--up)"/>
<line x1="823.8" y1="228.3" x2="823.8" y2="280.6" stroke="var(--down)" class="wick"/>
<rect x="822.61" y="245.5" width="2.46" height="19.5" fill="var(--down)"/>
<line x1="827.8" y1="236.3" x2="827.8" y2="260.7" stroke="var(--down)" class="wick"/>
<rect x="826.58" y="243.7" width="2.46" height="4.7" fill="var(--down)"/>
<line x1="831.8" y1="219.8" x2="831.8" y2="306.3" stroke="var(--down)" class="wick"/>
<rect x="830.55" y="226.3" width="2.46" height="47.3" fill="var(--down)"/>
<line x1="835.7" y1="256.3" x2="835.7" y2="291.4" stroke="var(--down)" class="wick"/>
<rect x="834.51" y="276.1" width="2.46" height="12.3" fill="var(--down)"/>
<line x1="839.7" y1="241.9" x2="839.7" y2="286.8" stroke="var(--up)" class="wick"/>
<rect x="838.48" y="243.1" width="2.46" height="38.1" fill="var(--up)"/>
<line x1="843.7" y1="226.4" x2="843.7" y2="313.7" stroke="var(--down)" class="wick"/>
<rect x="842.45" y="228.1" width="2.46" height="72.7" fill="var(--down)"/>
<line x1="847.6" y1="261.8" x2="847.6" y2="284.9" stroke="var(--up)" class="wick"/>
<rect x="846.42" y="268.9" width="2.46" height="6.0" fill="var(--up)"/>
<line x1="851.6" y1="272.4" x2="851.6" y2="297.6" stroke="var(--down)" class="wick"/>
<rect x="850.39" y="276.0" width="2.46" height="14.3" fill="var(--down)"/>
<line x1="855.6" y1="259.2" x2="855.6" y2="293.1" stroke="var(--up)" class="wick"/>
<rect x="854.35" y="274.8" width="2.46" height="18.0" fill="var(--up)"/>
<line x1="859.6" y1="267.5" x2="859.6" y2="307.5" stroke="var(--down)" class="wick"/>
<rect x="858.32" y="270.8" width="2.46" height="7.4" fill="var(--down)"/>
<line x1="863.5" y1="277.5" x2="863.5" y2="328.2" stroke="var(--down)" class="wick"/>
<rect x="862.29" y="279.4" width="2.46" height="31.2" fill="var(--down)"/>
<line x1="867.5" y1="303.9" x2="867.5" y2="335.7" stroke="var(--down)" class="wick"/>
<rect x="866.26" y="330.4" width="2.46" height="4.2" fill="var(--down)"/>
<line x1="871.5" y1="338.4" x2="871.5" y2="382.4" stroke="var(--down)" class="wick"/>
<rect x="870.23" y="340.5" width="2.46" height="39.3" fill="var(--down)"/>
<line x1="875.4" y1="376.5" x2="875.4" y2="405.0" stroke="var(--down)" class="wick"/>
<rect x="874.19" y="376.5" width="2.46" height="25.2" fill="var(--down)"/>
<line x1="879.4" y1="375.8" x2="879.4" y2="401.6" stroke="var(--up)" class="wick"/>
<rect x="878.16" y="383.9" width="2.46" height="16.0" fill="var(--up)"/>
<line x1="883.4" y1="316.2" x2="883.4" y2="359.1" stroke="var(--up)" class="wick"/>
<rect x="882.13" y="321.2" width="2.46" height="31.2" fill="var(--up)"/>
<line x1="887.3" y1="292.6" x2="887.3" y2="332.2" stroke="var(--up)" class="wick"/>
<rect x="886.10" y="304.2" width="2.46" height="20.7" fill="var(--up)"/>
<line x1="891.3" y1="276.6" x2="891.3" y2="323.0" stroke="var(--down)" class="wick"/>
<rect x="890.07" y="306.4" width="2.46" height="5.2" fill="var(--down)"/>
<line x1="895.3" y1="279.4" x2="895.3" y2="321.6" stroke="var(--down)" class="wick"/>
<rect x="894.03" y="307.3" width="2.46" height="2.5" fill="var(--down)"/>
<line x1="899.2" y1="302.1" x2="899.2" y2="347.7" stroke="var(--down)" class="wick"/>
<rect x="898.00" y="309.9" width="2.46" height="34.2" fill="var(--down)"/>
<line x1="903.2" y1="355.0" x2="903.2" y2="391.7" stroke="var(--down)" class="wick"/>
<rect x="901.97" y="358.4" width="2.46" height="30.7" fill="var(--down)"/>
<line x1="907.2" y1="374.7" x2="907.2" y2="400.3" stroke="var(--down)" class="wick"/>
<rect x="905.94" y="374.7" width="2.46" height="14.7" fill="var(--down)"/>
<line x1="911.1" y1="375.7" x2="911.1" y2="393.8" stroke="var(--down)" class="wick"/>
<rect x="909.91" y="375.7" width="2.46" height="17.4" fill="var(--down)"/>
<line x1="915.1" y1="394.3" x2="915.1" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="913.87" y="394.3" width="2.46" height="5.8" fill="var(--down)"/>
<line x1="919.1" y1="405.1" x2="919.1" y2="425.5" stroke="var(--down)" class="wick"/>
<rect x="917.84" y="405.5" width="2.46" height="14.7" fill="var(--down)"/>
<line x1="923.0" y1="393.2" x2="923.0" y2="411.9" stroke="var(--up)" class="wick"/>
<rect x="921.81" y="410.5" width="2.46" height="1.0" fill="var(--up)"/>
<line x1="927.0" y1="400.1" x2="927.0" y2="429.0" stroke="var(--down)" class="wick"/>
<rect x="925.78" y="409.9" width="2.46" height="12.7" fill="var(--down)"/>
<line x1="931.0" y1="433.1" x2="931.0" y2="470.1" stroke="var(--down)" class="wick"/>
<rect x="929.75" y="435.8" width="2.46" height="28.1" fill="var(--down)"/>
<line x1="934.9" y1="448.6" x2="934.9" y2="477.1" stroke="var(--up)" class="wick"/>
<rect x="933.71" y="462.6" width="2.46" height="7.9" fill="var(--up)"/>
<line x1="938.9" y1="453.7" x2="938.9" y2="472.7" stroke="var(--down)" class="wick"/>
<rect x="937.68" y="459.0" width="2.46" height="12.3" fill="var(--down)"/>
<line x1="942.9" y1="452.7" x2="942.9" y2="470.6" stroke="var(--up)" class="wick"/>
<rect x="941.65" y="455.6" width="2.46" height="12.9" fill="var(--up)"/>
<line x1="946.8" y1="437.8" x2="946.8" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="945.62" y="449.2" width="2.46" height="3.4" fill="var(--down)"/>
<line x1="950.8" y1="447.7" x2="950.8" y2="466.2" stroke="var(--up)" class="wick"/>
<rect x="949.59" y="451.6" width="2.46" height="8.7" fill="var(--up)"/>
<line x1="954.8" y1="453.6" x2="954.8" y2="484.1" stroke="var(--down)" class="wick"/>
<rect x="953.55" y="454.8" width="2.46" height="25.1" fill="var(--down)"/>
<line x1="958.8" y1="459.2" x2="958.8" y2="479.3" stroke="var(--up)" class="wick"/>
<rect x="957.52" y="465.7" width="2.46" height="10.0" fill="var(--up)"/>
<line x1="962.7" y1="475.0" x2="962.7" y2="497.8" stroke="var(--down)" class="wick"/>
<rect x="961.49" y="477.1" width="2.46" height="2.8" fill="var(--down)"/>
<line x1="966.7" y1="479.0" x2="966.7" y2="506.4" stroke="var(--down)" class="wick"/>
<rect x="965.46" y="481.7" width="2.46" height="22.8" fill="var(--down)"/>
<line x1="970.7" y1="475.5" x2="970.7" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="969.43" y="476.3" width="2.46" height="17.4" fill="var(--up)"/>
<line x1="974.6" y1="461.6" x2="974.6" y2="485.7" stroke="var(--down)" class="wick"/>
<rect x="973.39" y="469.5" width="2.46" height="5.5" fill="var(--down)"/>
<line x1="978.6" y1="448.7" x2="978.6" y2="487.9" stroke="var(--up)" class="wick"/>
<rect x="977.36" y="449.5" width="2.46" height="33.0" fill="var(--up)"/>
<line x1="982.6" y1="425.5" x2="982.6" y2="440.5" stroke="var(--up)" class="wick"/>
<rect x="981.33" y="430.7" width="2.46" height="7.8" fill="var(--up)"/>
<line x1="986.5" y1="417.5" x2="986.5" y2="438.0" stroke="var(--down)" class="wick"/>
<rect x="985.30" y="428.8" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="990.5" y1="404.1" x2="990.5" y2="440.8" stroke="var(--up)" class="wick"/>
<rect x="989.27" y="425.1" width="2.46" height="15.6" fill="var(--up)"/>
<line x1="994.5" y1="389.9" x2="994.5" y2="417.2" stroke="var(--up)" class="wick"/>
<rect x="993.23" y="391.8" width="2.46" height="18.8" fill="var(--up)"/>
<line x1="998.4" y1="373.2" x2="998.4" y2="406.0" stroke="var(--down)" class="wick"/>
<rect x="997.20" y="386.1" width="2.46" height="18.7" fill="var(--down)"/>
<line x1="1002.4" y1="398.5" x2="1002.4" y2="426.1" stroke="var(--up)" class="wick"/>
<rect x="1001.17" y="404.9" width="2.46" height="17.4" fill="var(--up)"/>
<line x1="1006.4" y1="394.7" x2="1006.4" y2="414.0" stroke="var(--up)" class="wick"/>
<rect x="1005.14" y="399.5" width="2.46" height="4.9" fill="var(--up)"/>
<line x1="1010.3" y1="385.4" x2="1010.3" y2="415.6" stroke="var(--up)" class="wick"/>
<rect x="1009.11" y="404.5" width="2.46" height="7.4" fill="var(--up)"/>
<line x1="1014.3" y1="393.4" x2="1014.3" y2="411.9" stroke="var(--up)" class="wick"/>
<rect x="1013.07" y="403.8" width="2.46" height="3.1" fill="var(--up)"/>
<line x1="1018.3" y1="379.2" x2="1018.3" y2="402.5" stroke="var(--up)" class="wick"/>
<rect x="1017.04" y="395.3" width="2.46" height="5.0" fill="var(--up)"/>
<line x1="1022.2" y1="400.1" x2="1022.2" y2="419.5" stroke="var(--up)" class="wick"/>
<rect x="1021.01" y="408.9" width="2.46" height="2.8" fill="var(--up)"/>
<line x1="1026.2" y1="416.1" x2="1026.2" y2="433.5" stroke="var(--down)" class="wick"/>
<rect x="1024.98" y="418.8" width="2.46" height="5.5" fill="var(--down)"/>
<line x1="1030.2" y1="426.5" x2="1030.2" y2="443.4" stroke="var(--down)" class="wick"/>
<rect x="1028.95" y="428.5" width="2.46" height="9.3" fill="var(--down)"/>
<line x1="1034.1" y1="428.5" x2="1034.1" y2="444.8" stroke="var(--down)" class="wick"/>
<rect x="1032.91" y="432.2" width="2.46" height="7.4" fill="var(--down)"/>
<line x1="1038.1" y1="445.9" x2="1038.1" y2="460.0" stroke="var(--down)" class="wick"/>
<rect x="1036.88" y="445.9" width="2.46" height="13.6" fill="var(--down)"/>
<line x1="1042.1" y1="451.5" x2="1042.1" y2="467.9" stroke="var(--down)" class="wick"/>
<rect x="1040.85" y="451.9" width="2.46" height="14.0" fill="var(--down)"/>
<line x1="1046.0" y1="462.3" x2="1046.0" y2="471.1" stroke="var(--down)" class="wick"/>
<rect x="1044.82" y="468.3" width="2.46" height="1.0" fill="var(--down)"/>
<line x1="1050.0" y1="462.8" x2="1050.0" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="1048.79" y="463.0" width="2.46" height="2.9" fill="var(--up)"/>
<line x1="60" y1="430.4" x2="1052" y2="430.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="433.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$75 R1</text>
<text x="1058" y="445.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="410.1" x2="1052" y2="410.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="413.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$79 R2</text>
<text x="1058" y="425.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="479.5" x2="1052" y2="479.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="473.5" font-size="11.5" fill="var(--support)" font-weight="600">$64 S1</text>
<text x="1058" y="485.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="505.9" x2="1052" y2="505.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="499.9" font-size="11.5" fill="var(--support)" font-weight="600">$58 S2</text>
<text x="1058" y="511.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="463.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="455.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $68 (2026-08-27)</text>
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
| R2 | $79 | 3 | 2025-12-24·2026-02-20·2026-03-17 — 2026-05-08 갭업 이전 박스의 상단 |
| R1 | $75 | 2 | 2025-10-15·2026-03-06 — 같은 박스 안의 중간 고점대. 2026-08-20~21에도 $75 부근까지 되올랐다가 밀렸다 |
| **현재가** | **$67.53** (2026-08-27 종가) | — | R1과 S1 사이 |
| S1 | $64 | 2 | 2026-02-12·2026-02-27 — 현재가에 가장 근접한 지지 |
| S2 | $58 | 2 | 2025-10-22·2026-07-29 |
| 참고선 | $150 | — | 52주 최고 **종가** $150.23(2026-05-27, 장중 최고 $151.00). 단 한 번 찍고 되돌린 값이라 클러스터가 형성되지 않았다 — 근시일 저항이 아니라 낙폭의 기준점으로만 본다 |
| 참고선 | $39 | — | 52주 최저 **종가** $39.48(2025-11-20, 장중 최저 $37.57). 현재가에서 -42% 떨어져 있어 근시일 지지로 보기 어렵고, [밸류에이션 / 적정주가](./06_valuation.md)가 제시한 관심 구간 $31~$38의 상단과 겹친다는 점에서만 의미가 있다 |

**레벨이 4개인 이유 — 위쪽에 R3이 없다.** 2026-05-08 갭업 이후 주가가 오간 $80~$150 구간에는 스윙 고점이 있지만 **같은 가격대를 두 번 이상 시험한 클러스터가 없다.** 상승도 하락도 한 방향으로 빠르게 지나간 구간이라 가격이 머문 흔적이 남지 않았다는 뜻이고, 그래서 이 차트가 잡아낸 저항은 전부 **갭업 이전($75~$79) 가격대**다. 지금 주가는 그 옛 박스의 안쪽으로 되돌아와 있다.

---

## 3. 관측된 특이 구간 — 2026-05-08 Q1 실적 갭업과 그 이후의 되돌림

- **계기**: 2026-05-07 장 마감 후 Q1 2026 실적 발표(매출 $200.3M, YoY +63.5%, 수주잔고 $2.2B, Q2 가이던스 $225~240M)와 함께 **회사 사상 최대 규모의 발사 계약**(Neutron 5회 · Electron 3회, 2029년까지)을 공시했다.[^q1]
- 종가 기준 전일 대비 **+34.2%** ($78.58 → $105.47)로 상장 이래 최대 상승률이었고, 거래량은 평소(일 중앙값 약 2,166만 주) 대비 약 **3.7배**인 **7,993만 주**였다. 처음으로 $100을 넘긴 날이다.
- 이후 3주 만에 **2026-05-27 사상 최고 종가 $150.23**까지 갔다가 되돌렸다(2026-06-01 하루 -14.7%, $143.48 → $122.39). 그사이 **2026-06-29 Iridium 인수 공시**에 +15.9%($84.54 → $98.01, 거래량 평소의 2.0배)로 한 번 더 튀었으나 추세를 되돌리지는 못했다 → [최근 뉴스 / 이슈](./08_news.md) · [역사 / 주요 이벤트](./02_history.md)
- **레짐 변화**: 갭업 전까지 주가는 $58~$79 박스 안에 있었고, 갭업 후 4개월은 $80~$150의 훨씬 넓은 구간을 빠르게 오갔다. 기준일 종가 $67.53은 사상 최고 대비 **-55.0%**(최종 거래일 $64.39 기준 -57.1%)로 **갭업 이전 박스 안으로 되돌아온 상태**다. 위 2절이 갭업 이후 구간에서 저항 클러스터를 하나도 잡지 못한 것은 이 때문이며, $80~$150 구간의 스윙 고점들은 레벨이 아니라 통과 지점으로 처리했다.

[^q1]: 출처 — [Rocket Lab IR "Rocket Lab Announces First Quarter 2026 Financial Results"(2026-05-07)](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-first-quarter-2026-financial-results) · [CNBC(2026-05-08)](https://www.cnbc.com/2026/05/08/rocket-lab-rklb-q1-earnings-2026.html). 이 문서가 다루는 것은 **가격 반응**이며, 실적 수치 자체는 [핵심 지표](./04_metrics.md) B절이 마스터다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 250개 거래일, 2025-08-29~2026-08-27. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py RKLB --name "Rocket Lab" --event 2026-05-08:"Q1 실적 + 최대 발사계약 (+34%)" --event 2026-06-29:"Iridium 인수 공시 (+16%)" --ref-line 150.23:"52주 최고 종가" --ref-line 39.48:"52주 최저 종가" --close-on 2026-08-27 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **레벨 개수를 3개로 채우지 않았다.** 저항 2개·지지 2개만 유효했고, 위쪽에 R3을 억지로 넣지 않은 사유는 2절에 적었다. `--force-level`은 쓰지 않았다.
    - **이 1년 구간에 가격 연속성을 깨는 주식분할은 없다.** 다만 **희석은 계속 진행 중이다** — H1 2026 가중평균 희석주식수가 YoY +21.0%이고 ATM 유상증자로만 15.3억 달러를 조달했다([핵심 지표](./04_metrics.md) A.4). 주가 차트는 이 희석을 보여주지 않으므로 주당 가격 흐름만으로 기업가치 변화를 읽으면 안 된다.

---

*작성일: 2026-08-30*
