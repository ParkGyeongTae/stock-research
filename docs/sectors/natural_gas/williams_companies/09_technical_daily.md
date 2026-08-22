# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로, 이 차트 작성을 위해 일봉 API에서 직접 수집한 것이다(1년 일봉은 핵심 지표가 다루는 범위 밖이라 단일 출처 규칙의 예외). 스크립트가 수집한 2026-08-21 종가는 $70.54로, [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값($70.13, Yahoo Finance 별도 조회)과 약 0.6% 차이가 있다 — 같은 날짜라도 데이터 제공처·조회 시점에 따라 종가가 소폭 갈리는 통상적 오차 범위이며, 방향성 판단에 영향을 줄 정도는 아니다.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-21 ~ 2026-08-21)

<div class="wmb-chart">
<style>
.wmb-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .wmb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .wmb-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.wmb-chart svg { width:100%; height:auto; display:block; }
.wmb-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.wmb-chart .title { fill: var(--ink); font-weight:600; }
.wmb-chart .grid { stroke: var(--grid); stroke-width:1; }
.wmb-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Williams Companies(WMB) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Williams Companies (WMB) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-21 ~ 2026-08-21 · 마지막 종가 $70.54 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">55</text>
<line x1="60" y1="516.4" x2="1052" y2="516.4" class="grid"/>
<text x="52" y="520.4" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="406.8" x2="1052" y2="406.8" class="grid"/>
<text x="52" y="410.8" font-size="11" text-anchor="end" fill="var(--muted)">65</text>
<line x1="60" y1="297.2" x2="1052" y2="297.2" class="grid"/>
<text x="52" y="301.2" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="187.5" x2="1052" y2="187.5" class="grid"/>
<text x="52" y="191.5" font-size="11" text-anchor="end" fill="var(--muted)">75</text>
<line x1="60" y1="77.9" x2="1052" y2="77.9" class="grid"/>
<text x="52" y="81.9" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="89.5" y1="626.0" x2="89.5" y2="631.0" class="axis"/>
<text x="89.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="172.2" y1="626.0" x2="172.2" y2="631.0" class="axis"/>
<text x="172.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="262.7" y1="626.0" x2="262.7" y2="631.0" class="axis"/>
<text x="262.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="337.5" y1="626.0" x2="337.5" y2="631.0" class="axis"/>
<text x="337.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="424.1" y1="626.0" x2="424.1" y2="631.0" class="axis"/>
<text x="424.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="502.9" y1="626.0" x2="502.9" y2="631.0" class="axis"/>
<text x="502.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="577.7" y1="626.0" x2="577.7" y2="631.0" class="axis"/>
<text x="577.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="664.3" y1="626.0" x2="664.3" y2="631.0" class="axis"/>
<text x="664.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="746.9" y1="626.0" x2="746.9" y2="631.0" class="axis"/>
<text x="746.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="825.7" y1="626.0" x2="825.7" y2="631.0" class="axis"/>
<text x="825.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="908.3" y1="626.0" x2="908.3" y2="631.0" class="axis"/>
<text x="908.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="994.9" y1="626.0" x2="994.9" y2="631.0" class="axis"/>
<text x="994.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="262.7" y1="56.0" x2="262.7" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="268.7" y="68.0" font-size="10.5" fill="var(--down)">2025-11-03 Q3 2025 실적 발표</text>
<line x1="526.5" y1="56.0" x2="526.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="532.5" y="68.0" font-size="10.5" fill="var(--down)">2026-02-10 FY2025 실적+2026 Analyst Day, 배당 5% 인상</text>
<line x1="750.9" y1="56.0" x2="750.9" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="756.9" y="68.0" font-size="10.5" fill="var(--down)">2026-05-04 Q1 2026 사상 최대 실적</text>
<line x1="994.9" y1="56.0" x2="994.9" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="1000.9" y="68.0" font-size="10.5" fill="var(--down)">2026-08-03 Q2 2026 실적+Momentum Midstream 인수 발표</text>
<line x1="62.0" y1="558.5" x2="62.0" y2="579.7" stroke="var(--up)" class="wick"/>
<rect x="60.75" y="564.6" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="65.9" y1="560.0" x2="65.9" y2="583.7" stroke="var(--down)" class="wick"/>
<rect x="64.68" y="563.5" width="2.44" height="17.1" fill="var(--down)"/>
<line x1="69.8" y1="570.5" x2="69.8" y2="591.8" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="582.4" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="73.8" y1="577.1" x2="73.8" y2="593.8" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="579.3" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="77.7" y1="567.9" x2="77.7" y2="584.3" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="571.4" width="2.44" height="11.4" fill="var(--up)"/>
<line x1="81.7" y1="558.3" x2="81.7" y2="584.1" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="560.2" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="85.6" y1="559.8" x2="85.6" y2="571.2" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="560.9" width="2.44" height="2.0" fill="var(--down)"/>
<line x1="89.5" y1="561.5" x2="89.5" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="571.0" width="2.44" height="2.8" fill="var(--down)"/>
<line x1="93.5" y1="560.4" x2="93.5" y2="583.2" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="566.2" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="97.4" y1="547.3" x2="97.4" y2="578.4" stroke="var(--down)" class="wick"/>
<rect x="96.18" y="560.2" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="101.3" y1="564.0" x2="101.3" y2="602.1" stroke="var(--down)" class="wick"/>
<rect x="100.11" y="571.4" width="2.44" height="6.4" fill="var(--down)"/>
<line x1="105.3" y1="567.2" x2="105.3" y2="594.0" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="575.6" width="2.44" height="9.9" fill="var(--down)"/>
<line x1="109.2" y1="560.9" x2="109.2" y2="582.8" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="569.7" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="113.1" y1="531.9" x2="113.1" y2="565.7" stroke="var(--up)" class="wick"/>
<rect x="111.92" y="543.6" width="2.44" height="21.9" fill="var(--up)"/>
<line x1="117.1" y1="530.6" x2="117.1" y2="552.3" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="531.1" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="121.0" y1="531.1" x2="121.0" y2="547.3" stroke="var(--down)" class="wick"/>
<rect x="119.80" y="541.6" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="125.0" y1="535.9" x2="125.0" y2="551.5" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="540.7" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="128.9" y1="546.4" x2="128.9" y2="567.7" stroke="var(--down)" class="wick"/>
<rect x="127.67" y="548.6" width="2.44" height="12.7" fill="var(--down)"/>
<line x1="132.8" y1="534.4" x2="132.8" y2="559.1" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="537.9" width="2.44" height="21.0" fill="var(--up)"/>
<line x1="136.8" y1="498.6" x2="136.8" y2="534.4" stroke="var(--up)" class="wick"/>
<rect x="135.54" y="508.1" width="2.44" height="22.6" fill="var(--up)"/>
<line x1="140.7" y1="488.3" x2="140.7" y2="516.2" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="491.4" width="2.44" height="22.6" fill="var(--down)"/>
<line x1="144.6" y1="501.7" x2="144.6" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="512.9" width="2.44" height="3.9" fill="var(--up)"/>
<line x1="148.6" y1="475.4" x2="148.6" y2="512.7" stroke="var(--up)" class="wick"/>
<rect x="147.35" y="485.9" width="2.44" height="26.5" fill="var(--up)"/>
<line x1="152.5" y1="441.4" x2="152.5" y2="475.8" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="453.7" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="156.4" y1="441.2" x2="156.4" y2="468.6" stroke="var(--up)" class="wick"/>
<rect x="155.22" y="443.8" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="160.4" y1="418.2" x2="160.4" y2="444.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="428.5" width="2.44" height="11.8" fill="var(--up)"/>
<line x1="164.3" y1="427.6" x2="164.3" y2="449.5" stroke="var(--up)" class="wick"/>
<rect x="163.10" y="429.3" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="168.3" y1="429.6" x2="168.3" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="441.4" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="172.2" y1="431.3" x2="172.2" y2="456.3" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="435.5" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="176.1" y1="394.7" x2="176.1" y2="444.7" stroke="var(--down)" class="wick"/>
<rect x="174.91" y="423.0" width="2.44" height="4.4" fill="var(--down)"/>
<line x1="180.1" y1="406.8" x2="180.1" y2="434.0" stroke="var(--up)" class="wick"/>
<rect x="178.84" y="418.2" width="2.44" height="9.0" fill="var(--up)"/>
<line x1="184.0" y1="403.3" x2="184.0" y2="438.1" stroke="var(--down)" class="wick"/>
<rect x="182.78" y="411.4" width="2.44" height="26.5" fill="var(--down)"/>
<line x1="187.9" y1="429.3" x2="187.9" y2="447.1" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="429.3" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="191.9" y1="428.0" x2="191.9" y2="449.3" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="431.1" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="195.8" y1="414.4" x2="195.8" y2="453.0" stroke="var(--down)" class="wick"/>
<rect x="194.59" y="425.2" width="2.44" height="23.2" fill="var(--down)"/>
<line x1="199.7" y1="416.4" x2="199.7" y2="460.3" stroke="var(--down)" class="wick"/>
<rect x="198.53" y="448.0" width="2.44" height="11.2" fill="var(--down)"/>
<line x1="203.7" y1="444.3" x2="203.7" y2="463.6" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="456.8" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="207.6" y1="455.2" x2="207.6" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="206.40" y="464.6" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="211.6" y1="422.3" x2="211.6" y2="460.7" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="433.5" width="2.44" height="21.7" fill="var(--up)"/>
<line x1="215.5" y1="426.3" x2="215.5" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="431.3" width="2.44" height="29.6" fill="var(--down)"/>
<line x1="219.4" y1="458.5" x2="219.4" y2="473.6" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="462.5" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="223.4" y1="441.0" x2="223.4" y2="462.7" stroke="var(--up)" class="wick"/>
<rect x="222.14" y="449.3" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="227.3" y1="443.8" x2="227.3" y2="467.9" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="446.2" width="2.44" height="18.9" fill="var(--down)"/>
<line x1="231.2" y1="457.0" x2="231.2" y2="492.9" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="458.3" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="235.2" y1="476.0" x2="235.2" y2="542.3" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="479.8" width="2.44" height="60.1" fill="var(--down)"/>
<line x1="239.1" y1="527.6" x2="239.1" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="530.6" width="2.44" height="41.0" fill="var(--down)"/>
<line x1="243.0" y1="554.8" x2="243.0" y2="577.3" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="567.5" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="247.0" y1="562.4" x2="247.0" y2="583.2" stroke="var(--up)" class="wick"/>
<rect x="245.76" y="569.2" width="2.44" height="2.0" fill="var(--up)"/>
<line x1="250.9" y1="559.4" x2="250.9" y2="584.6" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="569.0" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="254.9" y1="555.2" x2="254.9" y2="592.5" stroke="var(--up)" class="wick"/>
<rect x="253.64" y="568.6" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="258.8" y1="557.8" x2="258.8" y2="578.2" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="563.1" width="2.44" height="9.0" fill="var(--up)"/>
<line x1="262.7" y1="534.4" x2="262.7" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="537.7" width="2.44" height="17.5" fill="var(--up)"/>
<line x1="266.7" y1="543.1" x2="266.7" y2="599.9" stroke="var(--down)" class="wick"/>
<rect x="265.45" y="582.2" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="270.6" y1="551.7" x2="270.6" y2="598.4" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="570.3" width="2.44" height="22.4" fill="var(--up)"/>
<line x1="274.5" y1="551.7" x2="274.5" y2="571.2" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="561.5" width="2.44" height="9.2" fill="var(--up)"/>
<line x1="278.5" y1="521.4" x2="278.5" y2="564.6" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="525.6" width="2.44" height="34.6" fill="var(--up)"/>
<line x1="282.4" y1="500.6" x2="282.4" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="503.2" width="2.44" height="18.4" fill="var(--up)"/>
<line x1="286.3" y1="491.2" x2="286.3" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="503.2" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="290.3" y1="487.0" x2="290.3" y2="514.6" stroke="var(--down)" class="wick"/>
<rect x="289.07" y="504.8" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="294.2" y1="494.0" x2="294.2" y2="535.9" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="501.7" width="2.44" height="23.7" fill="var(--down)"/>
<line x1="298.2" y1="492.5" x2="298.2" y2="540.9" stroke="var(--up)" class="wick"/>
<rect x="296.94" y="494.7" width="2.44" height="40.6" fill="var(--up)"/>
<line x1="302.1" y1="494.9" x2="302.1" y2="526.3" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="498.0" width="2.44" height="20.4" fill="var(--down)"/>
<line x1="306.0" y1="509.4" x2="306.0" y2="535.5" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="520.1" width="2.44" height="14.5" fill="var(--down)"/>
<line x1="310.0" y1="539.2" x2="310.0" y2="556.1" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="540.7" width="2.44" height="10.5" fill="var(--up)"/>
<line x1="313.9" y1="501.0" x2="313.9" y2="540.9" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="530.9" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="317.8" y1="518.8" x2="317.8" y2="551.7" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="524.9" width="2.44" height="12.7" fill="var(--up)"/>
<line x1="321.8" y1="518.1" x2="321.8" y2="546.0" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="524.5" width="2.44" height="4.4" fill="var(--down)"/>
<line x1="325.7" y1="527.3" x2="325.7" y2="547.1" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="530.2" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="329.7" y1="501.7" x2="329.7" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="511.6" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="333.6" y1="491.8" x2="333.6" y2="514.2" stroke="var(--up)" class="wick"/>
<rect x="332.37" y="496.0" width="2.44" height="12.1" fill="var(--up)"/>
<line x1="337.5" y1="482.8" x2="337.5" y2="506.3" stroke="var(--up)" class="wick"/>
<rect x="336.30" y="484.8" width="2.44" height="16.0" fill="var(--up)"/>
<line x1="341.5" y1="480.9" x2="341.5" y2="512.4" stroke="var(--down)" class="wick"/>
<rect x="340.24" y="482.2" width="2.44" height="29.6" fill="var(--down)"/>
<line x1="345.4" y1="468.4" x2="345.4" y2="508.3" stroke="var(--up)" class="wick"/>
<rect x="344.18" y="482.4" width="2.44" height="24.6" fill="var(--up)"/>
<line x1="349.3" y1="432.0" x2="349.3" y2="490.5" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="436.1" width="2.44" height="46.3" fill="var(--up)"/>
<line x1="353.3" y1="431.3" x2="353.3" y2="455.4" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="436.1" width="2.44" height="18.6" fill="var(--down)"/>
<line x1="357.2" y1="458.9" x2="357.2" y2="481.7" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="461.1" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="361.1" y1="461.6" x2="361.1" y2="485.9" stroke="var(--down)" class="wick"/>
<rect x="359.92" y="471.4" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="365.1" y1="477.6" x2="365.1" y2="511.8" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="480.9" width="2.44" height="24.6" fill="var(--down)"/>
<line x1="369.0" y1="490.7" x2="369.0" y2="511.6" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="496.2" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="373.0" y1="498.4" x2="373.0" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="505.4" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="376.9" y1="523.2" x2="376.9" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="524.1" width="2.44" height="3.7" fill="var(--down)"/>
<line x1="380.8" y1="530.4" x2="380.8" y2="554.3" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="534.4" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="384.8" y1="535.5" x2="384.8" y2="558.3" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="541.8" width="2.44" height="5.5" fill="var(--up)"/>
<line x1="388.7" y1="517.7" x2="388.7" y2="546.9" stroke="var(--down)" class="wick"/>
<rect x="387.48" y="536.1" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="392.6" y1="536.6" x2="392.6" y2="555.4" stroke="var(--down)" class="wick"/>
<rect x="391.41" y="545.8" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="396.6" y1="537.2" x2="396.6" y2="550.8" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="540.1" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="400.5" y1="521.0" x2="400.5" y2="543.1" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="521.9" width="2.44" height="19.7" fill="var(--up)"/>
<line x1="404.4" y1="515.7" x2="404.4" y2="528.2" stroke="var(--down)" class="wick"/>
<rect x="403.22" y="522.3" width="2.44" height="5.9" fill="var(--down)"/>
<line x1="408.4" y1="521.0" x2="408.4" y2="534.4" stroke="var(--down)" class="wick"/>
<rect x="407.16" y="525.4" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="412.3" y1="516.6" x2="412.3" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="520.8" width="2.44" height="3.9" fill="var(--up)"/>
<line x1="416.3" y1="508.3" x2="416.3" y2="521.0" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="512.9" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="420.2" y1="511.8" x2="420.2" y2="523.4" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="511.8" width="2.44" height="2.2" fill="var(--down)"/>
<line x1="424.1" y1="491.0" x2="424.1" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="497.8" width="2.44" height="16.2" fill="var(--up)"/>
<line x1="428.1" y1="483.5" x2="428.1" y2="537.7" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="485.7" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="432.0" y1="498.4" x2="432.0" y2="549.5" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="504.8" width="2.44" height="22.6" fill="var(--down)"/>
<line x1="435.9" y1="498.6" x2="435.9" y2="524.9" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="507.8" width="2.44" height="12.3" fill="var(--up)"/>
<line x1="439.9" y1="483.3" x2="439.9" y2="510.9" stroke="var(--up)" class="wick"/>
<rect x="438.65" y="491.2" width="2.44" height="12.1" fill="var(--up)"/>
<line x1="443.8" y1="480.0" x2="443.8" y2="525.8" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="490.3" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="447.7" y1="505.6" x2="447.7" y2="536.8" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="512.0" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="451.7" y1="499.5" x2="451.7" y2="523.8" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="505.6" width="2.44" height="13.6" fill="var(--up)"/>
<line x1="455.6" y1="486.4" x2="455.6" y2="510.7" stroke="var(--up)" class="wick"/>
<rect x="454.40" y="500.8" width="2.44" height="6.8" fill="var(--up)"/>
<line x1="459.6" y1="490.5" x2="459.6" y2="512.9" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="503.9" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="463.5" y1="475.4" x2="463.5" y2="508.5" stroke="var(--up)" class="wick"/>
<rect x="462.27" y="482.4" width="2.44" height="25.9" fill="var(--up)"/>
<line x1="467.4" y1="460.5" x2="467.4" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="469.5" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="471.4" y1="446.7" x2="471.4" y2="468.6" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="446.7" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="475.3" y1="421.2" x2="475.3" y2="453.2" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="434.8" width="2.44" height="6.6" fill="var(--up)"/>
<line x1="479.2" y1="403.5" x2="479.2" y2="426.5" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="407.6" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="483.2" y1="389.0" x2="483.2" y2="432.4" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="397.3" width="2.44" height="25.0" fill="var(--down)"/>
<line x1="487.1" y1="391.2" x2="487.1" y2="423.9" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="396.2" width="2.44" height="23.2" fill="var(--up)"/>
<line x1="491.0" y1="362.7" x2="491.0" y2="394.3" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="364.7" width="2.44" height="21.9" fill="var(--up)"/>
<line x1="495.0" y1="335.1" x2="495.0" y2="367.7" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="342.5" width="2.44" height="15.1" fill="var(--down)"/>
<line x1="498.9" y1="352.8" x2="498.9" y2="391.6" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="357.2" width="2.44" height="1.3" fill="var(--up)"/>
<line x1="502.9" y1="365.1" x2="502.9" y2="388.6" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="376.3" width="2.44" height="1.1" fill="var(--down)"/>
<line x1="506.8" y1="325.7" x2="506.8" y2="368.6" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="330.0" width="2.44" height="34.6" fill="var(--up)"/>
<line x1="510.7" y1="320.2" x2="510.7" y2="394.7" stroke="var(--down)" class="wick"/>
<rect x="509.51" y="321.5" width="2.44" height="53.3" fill="var(--down)"/>
<line x1="514.7" y1="347.6" x2="514.7" y2="394.1" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="353.7" width="2.44" height="36.0" fill="var(--up)"/>
<line x1="518.6" y1="321.9" x2="518.6" y2="385.9" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="349.3" width="2.44" height="15.3" fill="var(--down)"/>
<line x1="522.5" y1="331.1" x2="522.5" y2="364.0" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="344.3" width="2.44" height="15.1" fill="var(--up)"/>
<line x1="526.5" y1="262.5" x2="526.5" y2="331.4" stroke="var(--down)" class="wick"/>
<rect x="525.26" y="297.2" width="2.44" height="25.4" fill="var(--down)"/>
<line x1="530.4" y1="262.3" x2="530.4" y2="306.6" stroke="var(--up)" class="wick"/>
<rect x="529.19" y="272.6" width="2.44" height="28.9" fill="var(--up)"/>
<line x1="534.3" y1="247.2" x2="534.3" y2="273.0" stroke="var(--down)" class="wick"/>
<rect x="533.13" y="258.4" width="2.44" height="14.0" fill="var(--down)"/>
<line x1="538.3" y1="239.5" x2="538.3" y2="276.8" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="247.2" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="542.2" y1="230.5" x2="542.2" y2="266.0" stroke="var(--down)" class="wick"/>
<rect x="541.00" y="232.9" width="2.44" height="21.3" fill="var(--down)"/>
<line x1="546.2" y1="232.0" x2="546.2" y2="257.3" stroke="var(--down)" class="wick"/>
<rect x="544.94" y="238.6" width="2.44" height="11.6" fill="var(--down)"/>
<line x1="550.1" y1="232.0" x2="550.1" y2="261.0" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="235.8" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="554.0" y1="231.8" x2="554.0" y2="253.3" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="231.8" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="558.0" y1="212.3" x2="558.0" y2="239.5" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="229.2" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="561.9" y1="217.8" x2="561.9" y2="256.8" stroke="var(--up)" class="wick"/>
<rect x="560.68" y="220.4" width="2.44" height="11.2" fill="var(--up)"/>
<line x1="565.8" y1="207.5" x2="565.8" y2="235.8" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="210.1" width="2.44" height="12.3" fill="var(--up)"/>
<line x1="569.8" y1="176.8" x2="569.8" y2="216.0" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="192.6" width="2.44" height="17.3" fill="var(--up)"/>
<line x1="573.7" y1="174.6" x2="573.7" y2="202.0" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="184.7" width="2.44" height="9.0" fill="var(--down)"/>
<line x1="577.7" y1="146.5" x2="577.7" y2="193.0" stroke="var(--up)" class="wick"/>
<rect x="576.43" y="159.9" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="581.6" y1="156.0" x2="581.6" y2="186.4" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="162.5" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="585.5" y1="167.4" x2="585.5" y2="194.1" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="170.7" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="589.5" y1="172.6" x2="589.5" y2="205.5" stroke="var(--down)" class="wick"/>
<rect x="588.24" y="187.8" width="2.44" height="4.8" fill="var(--down)"/>
<line x1="593.4" y1="184.5" x2="593.4" y2="210.8" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="185.1" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="597.3" y1="206.4" x2="597.3" y2="238.0" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="216.0" width="2.44" height="11.4" fill="var(--down)"/>
<line x1="601.3" y1="198.9" x2="601.3" y2="242.1" stroke="var(--up)" class="wick"/>
<rect x="600.05" y="213.0" width="2.44" height="15.8" fill="var(--up)"/>
<line x1="605.2" y1="199.2" x2="605.2" y2="225.2" stroke="var(--up)" class="wick"/>
<rect x="603.99" y="200.7" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="609.1" y1="180.1" x2="609.1" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="607.92" y="198.5" width="2.44" height="21.5" fill="var(--down)"/>
<line x1="613.1" y1="212.8" x2="613.1" y2="237.1" stroke="var(--down)" class="wick"/>
<rect x="611.86" y="221.1" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="617.0" y1="210.6" x2="617.0" y2="234.9" stroke="var(--up)" class="wick"/>
<rect x="615.80" y="211.9" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="621.0" y1="185.3" x2="621.0" y2="220.0" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="194.6" width="2.44" height="21.7" fill="var(--down)"/>
<line x1="624.9" y1="212.8" x2="624.9" y2="246.3" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="220.0" width="2.44" height="15.8" fill="var(--down)"/>
<line x1="628.8" y1="185.6" x2="628.8" y2="234.5" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="208.1" width="2.44" height="26.3" fill="var(--up)"/>
<line x1="632.8" y1="195.2" x2="632.8" y2="249.1" stroke="var(--down)" class="wick"/>
<rect x="631.54" y="208.8" width="2.44" height="35.5" fill="var(--down)"/>
<line x1="636.7" y1="207.5" x2="636.7" y2="253.3" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="218.2" width="2.44" height="17.8" fill="var(--up)"/>
<line x1="640.6" y1="186.9" x2="640.6" y2="223.1" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="199.4" width="2.44" height="20.8" fill="var(--up)"/>
<line x1="644.6" y1="193.5" x2="644.6" y2="216.0" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="196.7" width="2.44" height="16.9" fill="var(--down)"/>
<line x1="648.5" y1="197.8" x2="648.5" y2="227.2" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="204.0" width="2.44" height="4.2" fill="var(--down)"/>
<line x1="652.4" y1="179.4" x2="652.4" y2="220.2" stroke="var(--down)" class="wick"/>
<rect x="651.22" y="218.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="656.4" y1="191.5" x2="656.4" y2="245.2" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="205.3" width="2.44" height="37.7" fill="var(--down)"/>
<line x1="660.3" y1="223.3" x2="660.3" y2="261.0" stroke="var(--down)" class="wick"/>
<rect x="659.10" y="231.4" width="2.44" height="4.8" fill="var(--down)"/>
<line x1="664.3" y1="239.5" x2="664.3" y2="273.5" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="257.0" width="2.44" height="1.8" fill="var(--up)"/>
<line x1="668.2" y1="229.9" x2="668.2" y2="258.6" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="246.1" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="672.1" y1="231.4" x2="672.1" y2="259.2" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="240.4" width="2.44" height="9.0" fill="var(--up)"/>
<line x1="676.1" y1="197.6" x2="676.1" y2="242.1" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="208.6" width="2.44" height="30.9" fill="var(--up)"/>
<line x1="680.0" y1="225.0" x2="680.0" y2="274.6" stroke="var(--up)" class="wick"/>
<rect x="678.78" y="231.2" width="2.44" height="26.3" fill="var(--up)"/>
<line x1="683.9" y1="193.0" x2="683.9" y2="254.4" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="234.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="687.9" y1="230.9" x2="687.9" y2="260.8" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="237.1" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="691.8" y1="230.3" x2="691.8" y2="274.6" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="232.5" width="2.44" height="30.9" fill="var(--down)"/>
<line x1="695.7" y1="259.4" x2="695.7" y2="299.3" stroke="var(--up)" class="wick"/>
<rect x="694.53" y="265.6" width="2.44" height="5.0" fill="var(--up)"/>
<line x1="699.7" y1="264.7" x2="699.7" y2="282.9" stroke="var(--down)" class="wick"/>
<rect x="698.46" y="272.2" width="2.44" height="8.3" fill="var(--down)"/>
<line x1="703.6" y1="260.8" x2="703.6" y2="291.7" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="278.3" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="707.6" y1="263.4" x2="707.6" y2="311.8" stroke="var(--up)" class="wick"/>
<rect x="706.34" y="271.9" width="2.44" height="27.4" fill="var(--up)"/>
<line x1="711.5" y1="250.0" x2="711.5" y2="280.3" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="266.5" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="715.4" y1="258.6" x2="715.4" y2="303.3" stroke="var(--down)" class="wick"/>
<rect x="714.21" y="268.7" width="2.44" height="19.1" fill="var(--down)"/>
<line x1="719.4" y1="266.2" x2="719.4" y2="282.2" stroke="var(--up)" class="wick"/>
<rect x="718.14" y="273.0" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="723.3" y1="252.7" x2="723.3" y2="270.0" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="261.0" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="727.2" y1="247.8" x2="727.2" y2="275.0" stroke="var(--up)" class="wick"/>
<rect x="726.02" y="249.4" width="2.44" height="8.8" fill="var(--up)"/>
<line x1="731.2" y1="235.1" x2="731.2" y2="270.2" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="249.4" width="2.44" height="12.5" fill="var(--down)"/>
<line x1="735.1" y1="220.4" x2="735.1" y2="251.8" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="230.5" width="2.44" height="18.9" fill="var(--up)"/>
<line x1="739.0" y1="218.2" x2="739.0" y2="236.9" stroke="var(--up)" class="wick"/>
<rect x="737.83" y="224.4" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="743.0" y1="155.8" x2="743.0" y2="231.2" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="158.8" width="2.44" height="69.3" fill="var(--up)"/>
<line x1="746.9" y1="156.2" x2="746.9" y2="189.7" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="157.9" width="2.44" height="17.8" fill="var(--down)"/>
<line x1="750.9" y1="167.4" x2="750.9" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="178.5" width="2.44" height="1.5" fill="var(--up)"/>
<line x1="754.8" y1="134.7" x2="754.8" y2="183.2" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="163.0" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="758.7" y1="172.9" x2="758.7" y2="218.7" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="196.3" width="2.44" height="18.4" fill="var(--down)"/>
<line x1="762.7" y1="229.0" x2="762.7" y2="256.6" stroke="var(--up)" class="wick"/>
<rect x="761.45" y="232.5" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="766.6" y1="219.5" x2="766.6" y2="257.9" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="229.2" width="2.44" height="25.0" fill="var(--down)"/>
<line x1="770.5" y1="204.0" x2="770.5" y2="254.4" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="205.5" width="2.44" height="41.4" fill="var(--up)"/>
<line x1="774.5" y1="184.2" x2="774.5" y2="210.6" stroke="var(--up)" class="wick"/>
<rect x="773.26" y="193.5" width="2.44" height="2.4" fill="var(--up)"/>
<line x1="778.4" y1="163.9" x2="778.4" y2="203.5" stroke="var(--up)" class="wick"/>
<rect x="777.19" y="172.0" width="2.44" height="9.6" fill="var(--up)"/>
<line x1="782.3" y1="126.4" x2="782.3" y2="172.0" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="128.6" width="2.44" height="43.4" fill="var(--up)"/>
<line x1="786.3" y1="116.5" x2="786.3" y2="141.7" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="126.2" width="2.44" height="1.8" fill="var(--down)"/>
<line x1="790.2" y1="115.0" x2="790.2" y2="143.5" stroke="var(--down)" class="wick"/>
<rect x="789.00" y="122.4" width="2.44" height="6.1" fill="var(--down)"/>
<line x1="794.2" y1="86.9" x2="794.2" y2="141.5" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="91.1" width="2.44" height="34.4" fill="var(--up)"/>
<line x1="798.1" y1="76.2" x2="798.1" y2="131.4" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="88.0" width="2.44" height="36.4" fill="var(--down)"/>
<line x1="802.0" y1="115.4" x2="802.0" y2="138.6" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="117.6" width="2.44" height="14.7" fill="var(--down)"/>
<line x1="806.0" y1="108.2" x2="806.0" y2="133.4" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="111.5" width="2.44" height="14.3" fill="var(--up)"/>
<line x1="809.9" y1="111.5" x2="809.9" y2="159.0" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="116.3" width="2.44" height="41.9" fill="var(--down)"/>
<line x1="813.8" y1="168.0" x2="813.8" y2="205.1" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="177.0" width="2.44" height="24.3" fill="var(--down)"/>
<line x1="817.8" y1="188.9" x2="817.8" y2="229.9" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="189.5" width="2.44" height="39.0" fill="var(--down)"/>
<line x1="821.7" y1="231.8" x2="821.7" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="231.8" width="2.44" height="34.9" fill="var(--down)"/>
<line x1="825.7" y1="260.8" x2="825.7" y2="296.3" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="268.7" width="2.44" height="27.6" fill="var(--down)"/>
<line x1="829.6" y1="263.8" x2="829.6" y2="296.9" stroke="var(--up)" class="wick"/>
<rect x="828.37" y="268.4" width="2.44" height="22.4" fill="var(--up)"/>
<line x1="833.5" y1="237.5" x2="833.5" y2="272.4" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="260.8" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="837.5" y1="243.7" x2="837.5" y2="266.0" stroke="var(--up)" class="wick"/>
<rect x="836.24" y="243.9" width="2.44" height="17.8" fill="var(--up)"/>
<line x1="841.4" y1="237.3" x2="841.4" y2="259.2" stroke="var(--down)" class="wick"/>
<rect x="840.18" y="246.9" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="845.3" y1="240.8" x2="845.3" y2="270.4" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="245.9" width="2.44" height="16.4" fill="var(--down)"/>
<line x1="849.3" y1="245.6" x2="849.3" y2="282.5" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="262.3" width="2.44" height="3.3" fill="var(--up)"/>
<line x1="853.2" y1="232.5" x2="853.2" y2="260.5" stroke="var(--up)" class="wick"/>
<rect x="851.99" y="247.6" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="857.1" y1="235.6" x2="857.1" y2="263.0" stroke="var(--down)" class="wick"/>
<rect x="855.92" y="241.0" width="2.44" height="20.6" fill="var(--down)"/>
<line x1="861.1" y1="233.1" x2="861.1" y2="282.0" stroke="var(--up)" class="wick"/>
<rect x="859.86" y="251.6" width="2.44" height="21.0" fill="var(--up)"/>
<line x1="865.0" y1="249.4" x2="865.0" y2="296.7" stroke="var(--up)" class="wick"/>
<rect x="863.80" y="264.5" width="2.44" height="23.2" fill="var(--up)"/>
<line x1="869.0" y1="259.7" x2="869.0" y2="280.3" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="264.7" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="872.9" y1="259.2" x2="872.9" y2="279.8" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="269.8" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="876.8" y1="225.2" x2="876.8" y2="279.0" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="228.8" width="2.44" height="29.4" fill="var(--up)"/>
<line x1="880.8" y1="170.2" x2="880.8" y2="238.8" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="188.6" width="2.44" height="45.8" fill="var(--up)"/>
<line x1="884.7" y1="168.2" x2="884.7" y2="217.8" stroke="var(--up)" class="wick"/>
<rect x="883.48" y="170.2" width="2.44" height="34.6" fill="var(--up)"/>
<line x1="888.6" y1="161.9" x2="888.6" y2="196.5" stroke="var(--up)" class="wick"/>
<rect x="887.41" y="168.5" width="2.44" height="15.1" fill="var(--up)"/>
<line x1="892.6" y1="127.2" x2="892.6" y2="172.9" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="132.1" width="2.44" height="35.3" fill="var(--up)"/>
<line x1="896.5" y1="99.8" x2="896.5" y2="133.2" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="123.5" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="900.4" y1="111.2" x2="900.4" y2="214.9" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="130.3" width="2.44" height="55.9" fill="var(--down)"/>
<line x1="904.4" y1="173.7" x2="904.4" y2="204.0" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="188.9" width="2.44" height="13.2" fill="var(--down)"/>
<line x1="908.3" y1="197.8" x2="908.3" y2="247.4" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="206.0" width="2.44" height="30.5" fill="var(--down)"/>
<line x1="912.3" y1="210.3" x2="912.3" y2="250.9" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="219.1" width="2.44" height="9.2" fill="var(--down)"/>
<line x1="916.2" y1="211.9" x2="916.2" y2="244.5" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="229.9" width="2.44" height="5.5" fill="var(--down)"/>
<line x1="920.1" y1="178.3" x2="920.1" y2="223.5" stroke="var(--up)" class="wick"/>
<rect x="918.91" y="185.8" width="2.44" height="37.7" fill="var(--up)"/>
<line x1="924.1" y1="173.7" x2="924.1" y2="202.9" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="179.0" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="928.0" y1="155.1" x2="928.0" y2="182.1" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="174.6" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="931.9" y1="169.8" x2="931.9" y2="207.0" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="178.3" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="935.9" y1="175.0" x2="935.9" y2="235.6" stroke="var(--down)" class="wick"/>
<rect x="934.65" y="177.9" width="2.44" height="21.5" fill="var(--down)"/>
<line x1="939.8" y1="159.3" x2="939.8" y2="188.6" stroke="var(--up)" class="wick"/>
<rect x="938.59" y="166.1" width="2.44" height="21.9" fill="var(--up)"/>
<line x1="943.7" y1="158.2" x2="943.7" y2="205.5" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="165.6" width="2.44" height="35.5" fill="var(--down)"/>
<line x1="947.7" y1="182.9" x2="947.7" y2="209.5" stroke="var(--up)" class="wick"/>
<rect x="946.46" y="193.5" width="2.44" height="5.5" fill="var(--up)"/>
<line x1="951.6" y1="171.8" x2="951.6" y2="236.6" stroke="var(--down)" class="wick"/>
<rect x="950.40" y="172.9" width="2.44" height="50.2" fill="var(--down)"/>
<line x1="955.6" y1="178.1" x2="955.6" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="954.34" y="206.0" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="959.5" y1="193.2" x2="959.5" y2="236.6" stroke="var(--down)" class="wick"/>
<rect x="958.27" y="196.3" width="2.44" height="27.2" fill="var(--down)"/>
<line x1="963.4" y1="186.4" x2="963.4" y2="224.1" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="198.7" width="2.44" height="16.7" fill="var(--up)"/>
<line x1="967.4" y1="169.1" x2="967.4" y2="198.7" stroke="var(--down)" class="wick"/>
<rect x="966.14" y="179.4" width="2.44" height="2.6" fill="var(--down)"/>
<line x1="971.3" y1="156.4" x2="971.3" y2="212.8" stroke="var(--down)" class="wick"/>
<rect x="970.08" y="178.8" width="2.44" height="30.7" fill="var(--down)"/>
<line x1="975.2" y1="230.9" x2="975.2" y2="284.7" stroke="var(--down)" class="wick"/>
<rect x="974.02" y="235.3" width="2.44" height="44.5" fill="var(--down)"/>
<line x1="979.2" y1="268.0" x2="979.2" y2="313.2" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="280.1" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="983.1" y1="268.2" x2="983.1" y2="302.0" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="271.1" width="2.44" height="23.2" fill="var(--down)"/>
<line x1="987.0" y1="270.4" x2="987.0" y2="300.9" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="277.2" width="2.44" height="15.6" fill="var(--up)"/>
<line x1="991.0" y1="255.7" x2="991.0" y2="284.9" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="263.4" width="2.44" height="16.2" fill="var(--up)"/>
<line x1="994.9" y1="270.4" x2="994.9" y2="300.2" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="282.9" width="2.44" height="4.8" fill="var(--down)"/>
<line x1="998.9" y1="241.7" x2="998.9" y2="329.6" stroke="var(--up)" class="wick"/>
<rect x="997.64" y="264.0" width="2.44" height="42.5" fill="var(--up)"/>
<line x1="1002.8" y1="250.2" x2="1002.8" y2="276.1" stroke="var(--up)" class="wick"/>
<rect x="1001.57" y="257.5" width="2.44" height="6.4" fill="var(--up)"/>
<line x1="1006.7" y1="226.3" x2="1006.7" y2="270.6" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="231.4" width="2.44" height="27.2" fill="var(--down)"/>
<line x1="1010.7" y1="249.4" x2="1010.7" y2="291.9" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="265.6" width="2.44" height="22.8" fill="var(--down)"/>
<line x1="1014.6" y1="256.4" x2="1014.6" y2="284.2" stroke="var(--up)" class="wick"/>
<rect x="1013.38" y="256.6" width="2.44" height="18.6" fill="var(--up)"/>
<line x1="1018.5" y1="236.0" x2="1018.5" y2="261.2" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="246.5" width="2.44" height="3.9" fill="var(--up)"/>
<line x1="1022.5" y1="212.1" x2="1022.5" y2="248.9" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="216.0" width="2.44" height="30.3" fill="var(--up)"/>
<line x1="1026.4" y1="208.8" x2="1026.4" y2="230.5" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="220.4" width="2.44" height="10.1" fill="var(--down)"/>
<line x1="1030.3" y1="182.3" x2="1030.3" y2="226.8" stroke="var(--up)" class="wick"/>
<rect x="1029.13" y="183.2" width="2.44" height="38.8" fill="var(--up)"/>
<line x1="1034.3" y1="179.6" x2="1034.3" y2="222.8" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="182.9" width="2.44" height="38.6" fill="var(--down)"/>
<line x1="1038.2" y1="169.1" x2="1038.2" y2="202.9" stroke="var(--up)" class="wick"/>
<rect x="1037.00" y="184.7" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="1042.2" y1="168.2" x2="1042.2" y2="229.2" stroke="var(--down)" class="wick"/>
<rect x="1040.94" y="169.8" width="2.44" height="56.3" fill="var(--down)"/>
<line x1="1046.1" y1="210.1" x2="1046.1" y2="272.6" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="222.0" width="2.44" height="38.4" fill="var(--down)"/>
<line x1="1050.0" y1="224.4" x2="1050.0" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="249.6" width="2.44" height="35.7" fill="var(--down)"/>
<line x1="60" y1="201.6" x2="1052" y2="201.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="205.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$74 R1</text>
<text x="1058" y="217.1" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="148.2" x2="1052" y2="148.2" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="151.7" font-size="11.5" fill="var(--resistance)" font-weight="600">$77 R2</text>
<text x="1058" y="163.7" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="88.0" x2="1052" y2="88.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="91.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$80 R3</text>
<text x="1058" y="103.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="308.8" x2="1052" y2="308.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="302.8" font-size="11.5" fill="var(--support)" font-weight="600">$69 S1</text>
<text x="1058" y="314.8" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="554.6" x2="1052" y2="554.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="548.6" font-size="11.5" fill="var(--support)" font-weight="600">$58 S2</text>
<text x="1058" y="560.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="601.0" x2="1052" y2="601.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="595.0" font-size="11.5" fill="var(--support)" font-weight="600">$56 S3</text>
<text x="1058" y="607.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="285.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="277.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $71 (2026-08-21)</text>
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

## 2. 지지선 / 저항선 요약

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R3 | $80 | 2 | 2026-05-20·2026-06-26 — 최근 1년 최고가($80.08, 2026-05-20)를 포함하는 상단 |
| R2 | $77 | 4 | 2026-03-02·2026-05-05·2026-07-09·2026-07-24 — 2026년 상반기~하반기 내내 반복적으로 저항받은 구간 |
| R1 | $74 | 3 | 2026-03-27·2026-04-09·2026-06-10 |
| **현재가** | **$70.54** (2026-08-21 종가) | — | R1과 S1 사이 |
| S1 | $69 | 4 | 2026-04-17·2026-06-02·2026-06-15·2026-08-04 — 최근 4개월간 반복적으로 지지받은 구간, 현재가에 가장 근접 |
| S2 | $58 | 3 | 2025-11-19·2025-12-17·2026-01-06 |
| S3 | $56 | 2 | 2025-09-05·2025-11-04 — 최근 1년 최저가($56.09, 2025-09-05)를 포함하는 하단 |

---

## 3. 관측된 특이 구간 — 2026-02-10~11 FY2025 실적·2026 Analyst Day 발표 후 랠리

- 2026-02-10 장중 FY2025 실적(Adjusted EBITDA $7.75B, 13년 연속 증가)과 2026 Analyst Day를 통해 2026년 가이던스(Adjusted EBITDA 중간값 $8.2B)·배당 5% 인상을 동시 발표([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 발표 당일 $67.85 → $68.84로 +1.5%, 다음 거래일(2026-02-11)에는 $68.84 → $71.12로 추가 +3.3% — 이틀 누적 +4.8%. 발표일 거래량은 약 1,558만 주로 최근 1년 평균(약 689만 주)의 2배 이상.
- 이 구간을 기점으로 주가는 이전 저항대였던 $58 부근(S2)을 넘어 $69~$74 레인지로 레짐이 한 단계 올라섰다 — 실적 발표+장기 가이던스 상향이 거래 밴드 자체를 위로 이동시킨 사례.
- 참고로 2025-11-03 Q3 2025 실적 발표는 정반대로 작동했다 — 발표 다음 거래일(2025-11-04) 종가가 $59.03 → $56.51로 −4.3%, 거래량은 평소의 약 2.2배(1,511만 주)로 급증했다. 같은 "실적 발표"라는 이벤트도 가이던스 방향(상향 vs 보합)에 따라 정반대 가격 반응을 낳을 수 있다는 예시로 남긴다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-08-21~2026-08-21. 수집 시점: 2026-08-22. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py WMB --name "Williams Companies" --event 2025-11-03:"Q3 2025 실적 발표" --event 2026-02-10:"FY2025 실적+2026 Analyst Day, 배당 5% 인상" --event 2026-05-04:"Q1 2026 사상 최대 실적" --event 2026-08-03:"Q2 2026 실적+Momentum Midstream 인수 발표" --close-on 2026-08-21` — 레벨 개수는 기본값(3) 그대로 사용.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 252개 표본에서 스크립트에 고정된 파라미터이며, 최적화된 값이 아니다.
    - 조사 기간(2025-08~2026-08) 중 주식분할·대규모 유상증자는 없었다(핵심 지표 상단 각주 참고).
    - 최근 1년 주가는 $56(2025-09) → $80(2026-05) → $70(2026-08)의 큰 사이클을 그렸다 — 이는 재무 / 실적·투자 판단에서 다룬 펀더멘털 재평가(성장 스토리에 대한 시장 신뢰 변화)와 맞물려 있을 가능성이 크며, 순수 기술적 패턴만으로는 이 변동의 근본 동인을 설명하지 못한다.

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
- [최종 보고서](./11_final_report.md)

---

## 참고 자료

- [Yahoo Finance — The Williams Companies (WMB)](https://finance.yahoo.com/quote/WMB/)
- [StockAnalysis — WMB 종가 이력](https://stockanalysis.com/stocks/wmb/history/)

---

*작성일: 2026-08-22*
