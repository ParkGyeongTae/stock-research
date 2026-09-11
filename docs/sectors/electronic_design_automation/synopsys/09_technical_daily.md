# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표(SEC XBRL·10-Q)와는 계보가 다르다(일봉은 핵심 지표가 다루는 범위 밖이다).
- **대조 결과**: **2026-09-04 종가 $393.84는 [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 일치**한다(스크립트 `--close-on` 출력으로 확인).

:::
---

## 1. 차트 — 최근 1년 일봉 (2025-09-05 ~ 2026-09-04)

<div class="snps-chart">
<style>
.snps-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .snps-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.snps-chart svg { width:100%; height:auto; display:block; }
.snps-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.snps-chart .title { fill: var(--ink); font-weight:600; }
.snps-chart .grid { stroke: var(--grid); stroke-width:1; }
.snps-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Synopsys(SNPS) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Synopsys (SNPS) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-09-05 ~ 2026-09-04 · 마지막 종가 $393.84 (2026-09-04) · 단위 USD</text>
<line x1="60" y1="531.0" x2="1052" y2="531.0" class="grid"/>
<text x="52" y="535.0" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="60" y1="425.4" x2="1052" y2="425.4" class="grid"/>
<text x="52" y="429.4" font-size="11" text-anchor="end" fill="var(--muted)">450</text>
<line x1="60" y1="319.9" x2="1052" y2="319.9" class="grid"/>
<text x="52" y="323.9" font-size="11" text-anchor="end" fill="var(--muted)">500</text>
<line x1="60" y1="214.3" x2="1052" y2="214.3" class="grid"/>
<text x="52" y="218.3" font-size="11" text-anchor="end" fill="var(--muted)">550</text>
<line x1="60" y1="108.8" x2="1052" y2="108.8" class="grid"/>
<text x="52" y="112.8" font-size="11" text-anchor="end" fill="var(--muted)">600</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="132.8" y1="626.0" x2="132.8" y2="631.0" class="axis"/>
<text x="132.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="223.4" y1="626.0" x2="223.4" y2="631.0" class="axis"/>
<text x="223.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="298.2" y1="626.0" x2="298.2" y2="631.0" class="axis"/>
<text x="298.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="384.8" y1="626.0" x2="384.8" y2="631.0" class="axis"/>
<text x="384.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="463.5" y1="626.0" x2="463.5" y2="631.0" class="axis"/>
<text x="463.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="538.3" y1="626.0" x2="538.3" y2="631.0" class="axis"/>
<text x="538.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="624.9" y1="626.0" x2="624.9" y2="631.0" class="axis"/>
<text x="624.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="707.6" y1="626.0" x2="707.6" y2="631.0" class="axis"/>
<text x="707.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="786.3" y1="626.0" x2="786.3" y2="631.0" class="axis"/>
<text x="786.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="869.0" y1="626.0" x2="869.0" y2="631.0" class="axis"/>
<text x="869.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="955.6" y1="626.0" x2="955.6" y2="631.0" class="axis"/>
<text x="955.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="1038.2" y1="626.0" x2="1038.2" y2="631.0" class="axis"/>
<text x="1038.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-09</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="75.4" x2="1052" y2="75.4" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="78.4" font-size="10.5" fill="var(--muted)">$616 52주 최고</text>
<line x1="912.3" y1="56.0" x2="912.3" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="918.3" y="68.0" font-size="10.5" fill="var(--down)">2026-07-17 오픈소스 EDA 우려 급락</text>
<line x1="1022.5" y1="56.0" x2="1022.5" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="1028.5" y="68.0" font-size="10.5" fill="var(--down)">2026-08-26 3Q26 실적·가이던스 상향</text>
<line x1="62.0" y1="75.5" x2="62.0" y2="120.2" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="88.2" width="2.44" height="24.6" fill="var(--down)"/>
<line x1="65.9" y1="75.4" x2="65.9" y2="110.4" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="89.6" width="2.44" height="17.2" fill="var(--up)"/>
<line x1="69.8" y1="77.3" x2="69.8" y2="103.5" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="85.7" width="2.44" height="13.9" fill="var(--down)"/>
<line x1="73.8" y1="468.4" x2="73.8" y2="571.4" stroke="var(--down)" class="wick"/>
<rect x="72.56" y="472.3" width="2.44" height="84.5" fill="var(--down)"/>
<line x1="77.7" y1="447.2" x2="77.7" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="76.49" y="450.6" width="2.44" height="46.7" fill="var(--up)"/>
<line x1="81.7" y1="437.7" x2="81.7" y2="484.7" stroke="var(--down)" class="wick"/>
<rect x="80.43" y="438.5" width="2.44" height="38.8" fill="var(--down)"/>
<line x1="85.6" y1="459.2" x2="85.6" y2="495.6" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="464.5" width="2.44" height="26.0" fill="var(--down)"/>
<line x1="89.5" y1="473.2" x2="89.5" y2="495.1" stroke="var(--up)" class="wick"/>
<rect x="88.30" y="476.2" width="2.44" height="11.4" fill="var(--up)"/>
<line x1="93.5" y1="469.2" x2="93.5" y2="494.0" stroke="var(--up)" class="wick"/>
<rect x="92.24" y="477.4" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="97.4" y1="355.3" x2="97.4" y2="429.7" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="361.9" width="2.44" height="42.5" fill="var(--up)"/>
<line x1="101.3" y1="324.0" x2="101.3" y2="372.1" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="329.4" width="2.44" height="34.8" fill="var(--up)"/>
<line x1="105.3" y1="286.9" x2="105.3" y2="359.0" stroke="var(--up)" class="wick"/>
<rect x="104.05" y="288.7" width="2.44" height="52.3" fill="var(--up)"/>
<line x1="109.2" y1="292.4" x2="109.2" y2="344.0" stroke="var(--down)" class="wick"/>
<rect x="107.99" y="295.7" width="2.44" height="44.6" fill="var(--down)"/>
<line x1="113.1" y1="338.2" x2="113.1" y2="395.4" stroke="var(--down)" class="wick"/>
<rect x="111.92" y="338.9" width="2.44" height="48.4" fill="var(--down)"/>
<line x1="117.1" y1="346.1" x2="117.1" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="346.9" width="2.44" height="52.1" fill="var(--up)"/>
<line x1="121.0" y1="334.7" x2="121.0" y2="368.1" stroke="var(--up)" class="wick"/>
<rect x="119.80" y="345.7" width="2.44" height="22.4" fill="var(--up)"/>
<line x1="125.0" y1="336.9" x2="125.0" y2="365.7" stroke="var(--down)" class="wick"/>
<rect x="123.73" y="345.2" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="128.9" y1="330.0" x2="128.9" y2="360.4" stroke="var(--up)" class="wick"/>
<rect x="127.67" y="333.8" width="2.44" height="23.9" fill="var(--up)"/>
<line x1="132.8" y1="328.9" x2="132.8" y2="352.6" stroke="var(--up)" class="wick"/>
<rect x="131.61" y="343.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="136.8" y1="342.5" x2="136.8" y2="382.5" stroke="var(--down)" class="wick"/>
<rect x="135.54" y="352.2" width="2.44" height="28.6" fill="var(--down)"/>
<line x1="140.7" y1="371.0" x2="140.7" y2="390.4" stroke="var(--down)" class="wick"/>
<rect x="139.48" y="375.8" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="144.6" y1="359.5" x2="144.6" y2="384.2" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="365.9" width="2.44" height="13.2" fill="var(--up)"/>
<line x1="148.6" y1="353.4" x2="148.6" y2="386.5" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="353.4" width="2.44" height="13.3" fill="var(--down)"/>
<line x1="152.5" y1="336.0" x2="152.5" y2="369.0" stroke="var(--up)" class="wick"/>
<rect x="151.29" y="342.4" width="2.44" height="26.5" fill="var(--up)"/>
<line x1="156.4" y1="345.1" x2="156.4" y2="360.7" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="346.3" width="2.44" height="6.5" fill="var(--down)"/>
<line x1="160.4" y1="346.1" x2="160.4" y2="452.3" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="352.8" width="2.44" height="96.0" fill="var(--down)"/>
<line x1="164.3" y1="417.4" x2="164.3" y2="446.6" stroke="var(--down)" class="wick"/>
<rect x="163.10" y="426.5" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="168.3" y1="419.5" x2="168.3" y2="460.6" stroke="var(--up)" class="wick"/>
<rect x="167.03" y="438.6" width="2.44" height="15.5" fill="var(--up)"/>
<line x1="172.2" y1="427.8" x2="172.2" y2="463.4" stroke="var(--down)" class="wick"/>
<rect x="170.97" y="433.3" width="2.44" height="21.9" fill="var(--down)"/>
<line x1="176.1" y1="434.9" x2="176.1" y2="455.9" stroke="var(--up)" class="wick"/>
<rect x="174.91" y="446.1" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="180.1" y1="411.0" x2="180.1" y2="456.6" stroke="var(--up)" class="wick"/>
<rect x="178.84" y="430.4" width="2.44" height="25.3" fill="var(--up)"/>
<line x1="184.0" y1="408.9" x2="184.0" y2="427.6" stroke="var(--up)" class="wick"/>
<rect x="182.78" y="418.4" width="2.44" height="5.7" fill="var(--up)"/>
<line x1="187.9" y1="405.0" x2="187.9" y2="436.0" stroke="var(--up)" class="wick"/>
<rect x="186.72" y="406.4" width="2.44" height="22.8" fill="var(--up)"/>
<line x1="191.9" y1="392.2" x2="191.9" y2="437.4" stroke="var(--down)" class="wick"/>
<rect x="190.65" y="411.8" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="195.8" y1="403.5" x2="195.8" y2="424.4" stroke="var(--up)" class="wick"/>
<rect x="194.59" y="412.6" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="199.7" y1="375.9" x2="199.7" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="395.5" width="2.44" height="5.3" fill="var(--up)"/>
<line x1="203.7" y1="371.8" x2="203.7" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="380.5" width="2.44" height="12.4" fill="var(--down)"/>
<line x1="207.6" y1="399.3" x2="207.6" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="206.40" y="400.8" width="2.44" height="10.2" fill="var(--down)"/>
<line x1="211.6" y1="410.4" x2="211.6" y2="437.1" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="414.2" width="2.44" height="1.2" fill="var(--up)"/>
<line x1="215.5" y1="419.6" x2="215.5" y2="449.6" stroke="var(--down)" class="wick"/>
<rect x="214.27" y="425.4" width="2.44" height="14.9" fill="var(--down)"/>
<line x1="219.4" y1="412.3" x2="219.4" y2="440.9" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="417.4" width="2.44" height="18.0" fill="var(--up)"/>
<line x1="223.4" y1="420.1" x2="223.4" y2="451.7" stroke="var(--down)" class="wick"/>
<rect x="222.14" y="421.6" width="2.44" height="12.9" fill="var(--down)"/>
<line x1="227.3" y1="452.7" x2="227.3" y2="498.9" stroke="var(--down)" class="wick"/>
<rect x="226.08" y="457.1" width="2.44" height="39.4" fill="var(--down)"/>
<line x1="231.2" y1="495.3" x2="231.2" y2="525.3" stroke="var(--down)" class="wick"/>
<rect x="230.02" y="496.2" width="2.44" height="15.6" fill="var(--down)"/>
<line x1="235.2" y1="506.6" x2="235.2" y2="548.9" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="507.8" width="2.44" height="31.4" fill="var(--down)"/>
<line x1="239.1" y1="530.3" x2="239.1" y2="558.6" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="543.0" width="2.44" height="1.9" fill="var(--down)"/>
<line x1="243.0" y1="528.3" x2="243.0" y2="555.4" stroke="var(--up)" class="wick"/>
<rect x="241.83" y="529.4" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="247.0" y1="531.7" x2="247.0" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="535.0" width="2.44" height="5.3" fill="var(--down)"/>
<line x1="250.9" y1="523.1" x2="250.9" y2="542.7" stroke="var(--down)" class="wick"/>
<rect x="249.70" y="529.7" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="254.9" y1="523.3" x2="254.9" y2="547.0" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="538.9" width="2.44" height="4.9" fill="var(--down)"/>
<line x1="258.8" y1="535.5" x2="258.8" y2="560.1" stroke="var(--up)" class="wick"/>
<rect x="257.57" y="552.5" width="2.44" height="3.7" fill="var(--up)"/>
<line x1="262.7" y1="532.9" x2="262.7" y2="556.3" stroke="var(--up)" class="wick"/>
<rect x="261.51" y="551.6" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="266.7" y1="553.0" x2="266.7" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="265.45" y="556.3" width="2.44" height="8.8" fill="var(--down)"/>
<line x1="270.6" y1="529.7" x2="270.6" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="559.9" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="274.5" y1="519.3" x2="274.5" y2="566.4" stroke="var(--down)" class="wick"/>
<rect x="273.32" y="527.2" width="2.44" height="34.2" fill="var(--down)"/>
<line x1="278.5" y1="547.6" x2="278.5" y2="580.2" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="555.6" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="282.4" y1="518.5" x2="282.4" y2="548.7" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="521.2" width="2.44" height="20.3" fill="var(--up)"/>
<line x1="286.3" y1="519.1" x2="286.3" y2="542.8" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="527.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="290.3" y1="506.4" x2="290.3" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="510.6" width="2.44" height="13.8" fill="var(--up)"/>
<line x1="294.2" y1="491.1" x2="294.2" y2="511.2" stroke="var(--up)" class="wick"/>
<rect x="293.00" y="493.0" width="2.44" height="14.6" fill="var(--up)"/>
<line x1="298.2" y1="431.8" x2="298.2" y2="469.4" stroke="var(--down)" class="wick"/>
<rect x="296.94" y="433.9" width="2.44" height="16.3" fill="var(--down)"/>
<line x1="302.1" y1="418.0" x2="302.1" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="300.87" y="426.8" width="2.44" height="16.4" fill="var(--up)"/>
<line x1="306.0" y1="386.8" x2="306.0" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="304.81" y="390.7" width="2.44" height="44.7" fill="var(--up)"/>
<line x1="310.0" y1="392.3" x2="310.0" y2="403.9" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="396.4" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="313.9" y1="380.9" x2="313.9" y2="395.1" stroke="var(--up)" class="wick"/>
<rect x="312.68" y="390.1" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="317.8" y1="385.7" x2="317.8" y2="404.0" stroke="var(--down)" class="wick"/>
<rect x="316.62" y="387.9" width="2.44" height="4.3" fill="var(--down)"/>
<line x1="321.8" y1="379.8" x2="321.8" y2="403.0" stroke="var(--down)" class="wick"/>
<rect x="320.56" y="386.5" width="2.44" height="5.5" fill="var(--down)"/>
<line x1="325.7" y1="365.0" x2="325.7" y2="400.4" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="370.9" width="2.44" height="25.7" fill="var(--up)"/>
<line x1="329.7" y1="357.4" x2="329.7" y2="413.6" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="367.9" width="2.44" height="1.4" fill="var(--up)"/>
<line x1="333.6" y1="367.4" x2="333.6" y2="420.1" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="370.0" width="2.44" height="49.2" fill="var(--down)"/>
<line x1="337.5" y1="381.7" x2="337.5" y2="418.1" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="408.6" width="2.44" height="7.0" fill="var(--down)"/>
<line x1="341.5" y1="393.8" x2="341.5" y2="420.2" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="397.3" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="345.4" y1="389.6" x2="345.4" y2="419.2" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="391.9" width="2.44" height="27.1" fill="var(--down)"/>
<line x1="349.3" y1="387.8" x2="349.3" y2="415.5" stroke="var(--down)" class="wick"/>
<rect x="348.11" y="403.7" width="2.44" height="4.6" fill="var(--down)"/>
<line x1="353.3" y1="384.1" x2="353.3" y2="405.2" stroke="var(--up)" class="wick"/>
<rect x="352.05" y="396.5" width="2.44" height="6.2" fill="var(--up)"/>
<line x1="357.2" y1="353.9" x2="357.2" y2="387.8" stroke="var(--up)" class="wick"/>
<rect x="355.99" y="359.5" width="2.44" height="27.4" fill="var(--up)"/>
<line x1="361.1" y1="365.9" x2="361.1" y2="383.5" stroke="var(--down)" class="wick"/>
<rect x="359.92" y="367.3" width="2.44" height="4.3" fill="var(--down)"/>
<line x1="365.1" y1="369.9" x2="365.1" y2="378.5" stroke="var(--up)" class="wick"/>
<rect x="363.86" y="371.1" width="2.44" height="4.4" fill="var(--up)"/>
<line x1="369.0" y1="365.1" x2="369.0" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="367.80" y="368.1" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="373.0" y1="352.4" x2="373.0" y2="379.0" stroke="var(--up)" class="wick"/>
<rect x="371.73" y="364.3" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="376.9" y1="364.7" x2="376.9" y2="378.9" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="373.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="380.8" y1="373.4" x2="380.8" y2="385.2" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="376.6" width="2.44" height="7.2" fill="var(--down)"/>
<line x1="384.8" y1="349.7" x2="384.8" y2="380.1" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="361.2" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="388.7" y1="306.6" x2="388.7" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="332.2" width="2.44" height="19.3" fill="var(--up)"/>
<line x1="392.6" y1="299.9" x2="392.6" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="301.4" width="2.44" height="27.8" fill="var(--up)"/>
<line x1="396.6" y1="267.2" x2="396.6" y2="311.7" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="278.3" width="2.44" height="24.7" fill="var(--up)"/>
<line x1="400.5" y1="281.8" x2="400.5" y2="300.0" stroke="var(--up)" class="wick"/>
<rect x="399.29" y="289.3" width="2.44" height="7.1" fill="var(--up)"/>
<line x1="404.4" y1="258.8" x2="404.4" y2="296.5" stroke="var(--up)" class="wick"/>
<rect x="403.22" y="266.7" width="2.44" height="20.5" fill="var(--up)"/>
<line x1="408.4" y1="245.6" x2="408.4" y2="269.7" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="249.3" width="2.44" height="19.4" fill="var(--up)"/>
<line x1="412.3" y1="261.8" x2="412.3" y2="295.7" stroke="var(--down)" class="wick"/>
<rect x="411.10" y="275.2" width="2.44" height="19.8" fill="var(--down)"/>
<line x1="416.3" y1="304.3" x2="416.3" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="308.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="420.2" y1="279.6" x2="420.2" y2="315.7" stroke="var(--down)" class="wick"/>
<rect x="418.97" y="298.8" width="2.44" height="3.8" fill="var(--down)"/>
<line x1="424.1" y1="277.2" x2="424.1" y2="303.0" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="285.5" width="2.44" height="15.5" fill="var(--up)"/>
<line x1="428.1" y1="292.8" x2="428.1" y2="335.5" stroke="var(--up)" class="wick"/>
<rect x="426.84" y="296.7" width="2.44" height="25.0" fill="var(--up)"/>
<line x1="432.0" y1="266.1" x2="432.0" y2="312.4" stroke="var(--up)" class="wick"/>
<rect x="430.78" y="273.5" width="2.44" height="25.7" fill="var(--up)"/>
<line x1="435.9" y1="267.0" x2="435.9" y2="319.9" stroke="var(--down)" class="wick"/>
<rect x="434.72" y="271.9" width="2.44" height="28.0" fill="var(--down)"/>
<line x1="439.9" y1="299.4" x2="439.9" y2="326.7" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="304.1" width="2.44" height="12.8" fill="var(--down)"/>
<line x1="443.8" y1="303.0" x2="443.8" y2="334.1" stroke="var(--up)" class="wick"/>
<rect x="442.59" y="313.5" width="2.44" height="6.5" fill="var(--up)"/>
<line x1="447.7" y1="307.6" x2="447.7" y2="328.3" stroke="var(--down)" class="wick"/>
<rect x="446.53" y="312.5" width="2.44" height="1.7" fill="var(--down)"/>
<line x1="451.7" y1="286.5" x2="451.7" y2="309.7" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="295.9" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="455.6" y1="297.3" x2="455.6" y2="372.9" stroke="var(--down)" class="wick"/>
<rect x="454.40" y="308.6" width="2.44" height="53.5" fill="var(--down)"/>
<line x1="459.6" y1="372.2" x2="459.6" y2="397.6" stroke="var(--down)" class="wick"/>
<rect x="458.34" y="373.6" width="2.44" height="20.0" fill="var(--down)"/>
<line x1="463.5" y1="380.7" x2="463.5" y2="409.4" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="402.9" width="2.44" height="5.9" fill="var(--down)"/>
<line x1="467.4" y1="410.7" x2="467.4" y2="503.5" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="413.4" width="2.44" height="77.2" fill="var(--down)"/>
<line x1="471.4" y1="477.2" x2="471.4" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="470.14" y="490.9" width="2.44" height="10.7" fill="var(--up)"/>
<line x1="475.3" y1="476.5" x2="475.3" y2="517.9" stroke="var(--down)" class="wick"/>
<rect x="474.08" y="490.7" width="2.44" height="18.3" fill="var(--down)"/>
<line x1="479.2" y1="465.3" x2="479.2" y2="496.9" stroke="var(--up)" class="wick"/>
<rect x="478.02" y="474.3" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="483.2" y1="440.3" x2="483.2" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="481.95" y="448.9" width="2.44" height="23.3" fill="var(--up)"/>
<line x1="487.1" y1="421.2" x2="487.1" y2="455.0" stroke="var(--down)" class="wick"/>
<rect x="485.89" y="446.7" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="491.0" y1="439.7" x2="491.0" y2="478.2" stroke="var(--down)" class="wick"/>
<rect x="489.83" y="442.1" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="495.0" y1="449.7" x2="495.0" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="493.76" y="450.1" width="2.44" height="31.6" fill="var(--down)"/>
<line x1="498.9" y1="443.5" x2="498.9" y2="487.7" stroke="var(--up)" class="wick"/>
<rect x="497.70" y="452.7" width="2.44" height="29.0" fill="var(--up)"/>
<line x1="502.9" y1="474.3" x2="502.9" y2="504.9" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="477.0" width="2.44" height="7.7" fill="var(--down)"/>
<line x1="506.8" y1="432.0" x2="506.8" y2="460.9" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="441.7" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="510.7" y1="439.8" x2="510.7" y2="460.4" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="441.4" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="514.7" y1="424.6" x2="514.7" y2="452.5" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="446.7" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="518.6" y1="460.5" x2="518.6" y2="494.5" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="469.0" width="2.44" height="18.1" fill="var(--down)"/>
<line x1="522.5" y1="439.4" x2="522.5" y2="499.3" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="445.0" width="2.44" height="45.0" fill="var(--up)"/>
<line x1="526.5" y1="416.7" x2="526.5" y2="446.9" stroke="var(--up)" class="wick"/>
<rect x="525.26" y="427.2" width="2.44" height="11.5" fill="var(--up)"/>
<line x1="530.4" y1="439.0" x2="530.4" y2="481.6" stroke="var(--down)" class="wick"/>
<rect x="529.19" y="467.9" width="2.44" height="8.2" fill="var(--down)"/>
<line x1="534.3" y1="494.8" x2="534.3" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="501.4" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="538.3" y1="475.6" x2="538.3" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="478.9" width="2.44" height="23.8" fill="var(--up)"/>
<line x1="542.2" y1="465.0" x2="542.2" y2="508.6" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="479.7" width="2.44" height="25.0" fill="var(--up)"/>
<line x1="546.2" y1="447.6" x2="546.2" y2="488.1" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="465.6" width="2.44" height="12.4" fill="var(--up)"/>
<line x1="550.1" y1="430.3" x2="550.1" y2="476.6" stroke="var(--up)" class="wick"/>
<rect x="548.87" y="441.7" width="2.44" height="34.9" fill="var(--up)"/>
<line x1="554.0" y1="435.3" x2="554.0" y2="463.9" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="452.0" width="2.44" height="10.2" fill="var(--up)"/>
<line x1="558.0" y1="444.6" x2="558.0" y2="468.4" stroke="var(--up)" class="wick"/>
<rect x="556.75" y="452.4" width="2.44" height="9.8" fill="var(--up)"/>
<line x1="561.9" y1="448.6" x2="561.9" y2="471.9" stroke="var(--down)" class="wick"/>
<rect x="560.68" y="452.7" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="565.8" y1="454.2" x2="565.8" y2="477.5" stroke="var(--up)" class="wick"/>
<rect x="564.62" y="461.4" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="569.8" y1="454.2" x2="569.8" y2="492.2" stroke="var(--down)" class="wick"/>
<rect x="568.56" y="463.7" width="2.44" height="27.8" fill="var(--down)"/>
<line x1="573.7" y1="477.2" x2="573.7" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="572.49" y="490.9" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="577.7" y1="471.0" x2="577.7" y2="493.8" stroke="var(--up)" class="wick"/>
<rect x="576.43" y="476.4" width="2.44" height="12.0" fill="var(--up)"/>
<line x1="581.6" y1="456.1" x2="581.6" y2="472.8" stroke="var(--up)" class="wick"/>
<rect x="580.37" y="469.2" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="585.5" y1="455.6" x2="585.5" y2="480.3" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="470.5" width="2.44" height="7.8" fill="var(--up)"/>
<line x1="589.5" y1="460.8" x2="589.5" y2="483.4" stroke="var(--up)" class="wick"/>
<rect x="588.24" y="471.4" width="2.44" height="7.5" fill="var(--up)"/>
<line x1="593.4" y1="467.9" x2="593.4" y2="490.9" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="476.3" width="2.44" height="11.8" fill="var(--down)"/>
<line x1="597.3" y1="442.8" x2="597.3" y2="468.4" stroke="var(--up)" class="wick"/>
<rect x="596.11" y="462.4" width="2.44" height="4.8" fill="var(--up)"/>
<line x1="601.3" y1="469.2" x2="601.3" y2="510.2" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="474.7" width="2.44" height="23.3" fill="var(--down)"/>
<line x1="605.2" y1="476.3" x2="605.2" y2="524.0" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="483.5" width="2.44" height="26.1" fill="var(--down)"/>
<line x1="609.1" y1="502.4" x2="609.1" y2="530.2" stroke="var(--down)" class="wick"/>
<rect x="607.92" y="519.9" width="2.44" height="7.0" fill="var(--down)"/>
<line x1="613.1" y1="527.7" x2="613.1" y2="574.3" stroke="var(--down)" class="wick"/>
<rect x="611.86" y="531.0" width="2.44" height="41.2" fill="var(--down)"/>
<line x1="617.0" y1="550.5" x2="617.0" y2="573.3" stroke="var(--up)" class="wick"/>
<rect x="615.80" y="566.6" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="621.0" y1="536.3" x2="621.0" y2="558.0" stroke="var(--up)" class="wick"/>
<rect x="619.73" y="538.4" width="2.44" height="13.3" fill="var(--up)"/>
<line x1="624.9" y1="523.7" x2="624.9" y2="542.6" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="524.0" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="628.8" y1="528.7" x2="628.8" y2="559.3" stroke="var(--up)" class="wick"/>
<rect x="627.61" y="539.5" width="2.44" height="13.3" fill="var(--up)"/>
<line x1="632.8" y1="533.9" x2="632.8" y2="551.9" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="537.2" width="2.44" height="2.2" fill="var(--up)"/>
<line x1="636.7" y1="535.0" x2="636.7" y2="554.5" stroke="var(--up)" class="wick"/>
<rect x="635.48" y="535.4" width="2.44" height="8.9" fill="var(--up)"/>
<line x1="640.6" y1="499.0" x2="640.6" y2="519.4" stroke="var(--down)" class="wick"/>
<rect x="639.41" y="506.2" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="644.6" y1="507.8" x2="644.6" y2="543.1" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="510.0" width="2.44" height="10.6" fill="var(--down)"/>
<line x1="648.5" y1="522.7" x2="648.5" y2="553.9" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="527.6" width="2.44" height="19.8" fill="var(--down)"/>
<line x1="652.4" y1="492.1" x2="652.4" y2="556.2" stroke="var(--up)" class="wick"/>
<rect x="651.22" y="493.5" width="2.44" height="53.3" fill="var(--up)"/>
<line x1="656.4" y1="467.4" x2="656.4" y2="492.6" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="478.6" width="2.44" height="12.7" fill="var(--down)"/>
<line x1="660.3" y1="446.8" x2="660.3" y2="485.8" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="449.8" width="2.44" height="30.0" fill="var(--up)"/>
<line x1="664.3" y1="426.2" x2="664.3" y2="454.0" stroke="var(--down)" class="wick"/>
<rect x="663.03" y="433.1" width="2.44" height="11.0" fill="var(--down)"/>
<line x1="668.2" y1="406.4" x2="668.2" y2="431.4" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="420.1" width="2.44" height="6.3" fill="var(--down)"/>
<line x1="672.1" y1="397.7" x2="672.1" y2="430.9" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="402.3" width="2.44" height="27.2" fill="var(--up)"/>
<line x1="676.1" y1="361.6" x2="676.1" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="388.3" width="2.44" height="7.0" fill="var(--up)"/>
<line x1="680.0" y1="364.8" x2="680.0" y2="381.3" stroke="var(--up)" class="wick"/>
<rect x="678.78" y="367.9" width="2.44" height="13.4" fill="var(--up)"/>
<line x1="683.9" y1="388.9" x2="683.9" y2="425.2" stroke="var(--down)" class="wick"/>
<rect x="682.72" y="391.4" width="2.44" height="19.5" fill="var(--down)"/>
<line x1="687.9" y1="315.1" x2="687.9" y2="384.9" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="318.2" width="2.44" height="66.4" fill="var(--up)"/>
<line x1="691.8" y1="317.8" x2="691.8" y2="345.2" stroke="var(--up)" class="wick"/>
<rect x="690.59" y="323.0" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="695.7" y1="324.1" x2="695.7" y2="364.2" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="326.2" width="2.44" height="27.7" fill="var(--down)"/>
<line x1="699.7" y1="358.7" x2="699.7" y2="379.6" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="359.5" width="2.44" height="2.6" fill="var(--up)"/>
<line x1="703.6" y1="354.3" x2="703.6" y2="379.8" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="356.6" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="707.6" y1="324.2" x2="707.6" y2="350.6" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="338.6" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="711.5" y1="319.4" x2="711.5" y2="344.5" stroke="var(--up)" class="wick"/>
<rect x="710.27" y="325.2" width="2.44" height="7.7" fill="var(--up)"/>
<line x1="715.4" y1="293.4" x2="715.4" y2="319.9" stroke="var(--up)" class="wick"/>
<rect x="714.21" y="314.6" width="2.44" height="1.7" fill="var(--up)"/>
<line x1="719.4" y1="304.4" x2="719.4" y2="325.1" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="310.2" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="723.3" y1="284.0" x2="723.3" y2="312.5" stroke="var(--down)" class="wick"/>
<rect x="722.08" y="306.6" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="727.2" y1="279.5" x2="727.2" y2="318.6" stroke="var(--up)" class="wick"/>
<rect x="726.02" y="285.1" width="2.44" height="25.6" fill="var(--up)"/>
<line x1="731.2" y1="278.3" x2="731.2" y2="294.6" stroke="var(--up)" class="wick"/>
<rect x="729.95" y="285.7" width="2.44" height="4.9" fill="var(--up)"/>
<line x1="735.1" y1="283.6" x2="735.1" y2="302.7" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="292.0" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="739.0" y1="288.8" x2="739.0" y2="315.1" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="289.1" width="2.44" height="11.2" fill="var(--down)"/>
<line x1="743.0" y1="291.1" x2="743.0" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="741.76" y="298.7" width="2.44" height="3.0" fill="var(--up)"/>
<line x1="746.9" y1="300.9" x2="746.9" y2="338.8" stroke="var(--up)" class="wick"/>
<rect x="745.70" y="314.8" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="750.9" y1="316.0" x2="750.9" y2="342.9" stroke="var(--down)" class="wick"/>
<rect x="749.64" y="321.6" width="2.44" height="1.6" fill="var(--down)"/>
<line x1="754.8" y1="317.8" x2="754.8" y2="339.8" stroke="var(--down)" class="wick"/>
<rect x="753.57" y="331.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="758.7" y1="321.5" x2="758.7" y2="375.3" stroke="var(--up)" class="wick"/>
<rect x="757.51" y="322.1" width="2.44" height="41.4" fill="var(--up)"/>
<line x1="762.7" y1="309.9" x2="762.7" y2="343.8" stroke="var(--up)" class="wick"/>
<rect x="761.45" y="311.5" width="2.44" height="26.9" fill="var(--up)"/>
<line x1="766.6" y1="247.9" x2="766.6" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="765.38" y="267.7" width="2.44" height="31.1" fill="var(--up)"/>
<line x1="770.5" y1="236.5" x2="770.5" y2="268.8" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="246.9" width="2.44" height="9.7" fill="var(--up)"/>
<line x1="774.5" y1="246.8" x2="774.5" y2="271.0" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="246.9" width="2.44" height="18.2" fill="var(--down)"/>
<line x1="778.4" y1="264.8" x2="778.4" y2="379.7" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="298.8" width="2.44" height="62.0" fill="var(--down)"/>
<line x1="782.3" y1="352.6" x2="782.3" y2="384.6" stroke="var(--down)" class="wick"/>
<rect x="781.13" y="360.7" width="2.44" height="10.7" fill="var(--down)"/>
<line x1="786.3" y1="332.0" x2="786.3" y2="381.7" stroke="var(--up)" class="wick"/>
<rect x="785.07" y="336.2" width="2.44" height="17.4" fill="var(--up)"/>
<line x1="790.2" y1="301.5" x2="790.2" y2="350.2" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="302.3" width="2.44" height="48.0" fill="var(--up)"/>
<line x1="794.2" y1="311.2" x2="794.2" y2="338.5" stroke="var(--down)" class="wick"/>
<rect x="792.94" y="314.0" width="2.44" height="10.0" fill="var(--down)"/>
<line x1="798.1" y1="319.1" x2="798.1" y2="351.6" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="319.1" width="2.44" height="12.4" fill="var(--down)"/>
<line x1="802.0" y1="343.2" x2="802.0" y2="407.4" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="345.3" width="2.44" height="48.8" fill="var(--down)"/>
<line x1="806.0" y1="365.3" x2="806.0" y2="397.2" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="375.9" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="809.9" y1="346.2" x2="809.9" y2="423.3" stroke="var(--down)" class="wick"/>
<rect x="808.68" y="371.0" width="2.44" height="22.3" fill="var(--down)"/>
<line x1="813.8" y1="378.1" x2="813.8" y2="418.5" stroke="var(--up)" class="wick"/>
<rect x="812.62" y="403.2" width="2.44" height="11.9" fill="var(--up)"/>
<line x1="817.8" y1="395.1" x2="817.8" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="409.1" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="821.7" y1="402.0" x2="821.7" y2="436.0" stroke="var(--down)" class="wick"/>
<rect x="820.49" y="410.5" width="2.44" height="6.8" fill="var(--down)"/>
<line x1="825.7" y1="396.9" x2="825.7" y2="419.1" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="399.5" width="2.44" height="16.7" fill="var(--down)"/>
<line x1="829.6" y1="413.8" x2="829.6" y2="436.4" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="421.2" width="2.44" height="7.6" fill="var(--down)"/>
<line x1="833.5" y1="365.2" x2="833.5" y2="433.5" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="400.7" width="2.44" height="28.3" fill="var(--up)"/>
<line x1="837.5" y1="391.5" x2="837.5" y2="420.5" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="400.1" width="2.44" height="13.7" fill="var(--down)"/>
<line x1="841.4" y1="384.5" x2="841.4" y2="419.5" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="394.7" width="2.44" height="19.1" fill="var(--up)"/>
<line x1="845.3" y1="362.5" x2="845.3" y2="401.2" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="393.8" width="2.44" height="7.4" fill="var(--down)"/>
<line x1="849.3" y1="376.5" x2="849.3" y2="408.3" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="396.0" width="2.44" height="8.0" fill="var(--up)"/>
<line x1="853.2" y1="392.6" x2="853.2" y2="426.9" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="397.7" width="2.44" height="17.1" fill="var(--down)"/>
<line x1="857.1" y1="408.5" x2="857.1" y2="449.6" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="416.3" width="2.44" height="11.0" fill="var(--up)"/>
<line x1="861.1" y1="403.7" x2="861.1" y2="449.7" stroke="var(--down)" class="wick"/>
<rect x="859.86" y="408.7" width="2.44" height="22.5" fill="var(--down)"/>
<line x1="865.0" y1="426.4" x2="865.0" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="863.80" y="433.7" width="2.44" height="8.6" fill="var(--up)"/>
<line x1="869.0" y1="394.9" x2="869.0" y2="418.2" stroke="var(--up)" class="wick"/>
<rect x="867.73" y="415.9" width="2.44" height="1.1" fill="var(--up)"/>
<line x1="872.9" y1="418.1" x2="872.9" y2="458.7" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="423.0" width="2.44" height="29.5" fill="var(--down)"/>
<line x1="876.8" y1="439.4" x2="876.8" y2="462.1" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="441.8" width="2.44" height="14.8" fill="var(--up)"/>
<line x1="880.8" y1="422.1" x2="880.8" y2="466.9" stroke="var(--down)" class="wick"/>
<rect x="879.54" y="430.0" width="2.44" height="23.7" fill="var(--down)"/>
<line x1="884.7" y1="453.9" x2="884.7" y2="476.5" stroke="var(--down)" class="wick"/>
<rect x="883.48" y="454.7" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="888.6" y1="439.2" x2="888.6" y2="474.5" stroke="var(--up)" class="wick"/>
<rect x="887.41" y="439.4" width="2.44" height="28.6" fill="var(--up)"/>
<line x1="892.6" y1="429.9" x2="892.6" y2="449.8" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="434.9" width="2.44" height="4.2" fill="var(--up)"/>
<line x1="896.5" y1="417.2" x2="896.5" y2="461.9" stroke="var(--down)" class="wick"/>
<rect x="895.29" y="427.9" width="2.44" height="31.7" fill="var(--down)"/>
<line x1="900.4" y1="458.1" x2="900.4" y2="479.8" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="475.7" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="904.4" y1="462.7" x2="904.4" y2="486.7" stroke="var(--down)" class="wick"/>
<rect x="903.16" y="468.0" width="2.44" height="9.7" fill="var(--down)"/>
<line x1="908.3" y1="476.9" x2="908.3" y2="496.5" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="476.9" width="2.44" height="18.2" fill="var(--down)"/>
<line x1="912.3" y1="525.3" x2="912.3" y2="602.8" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="527.6" width="2.44" height="36.5" fill="var(--down)"/>
<line x1="916.2" y1="562.3" x2="916.2" y2="586.2" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="569.0" width="2.44" height="7.5" fill="var(--down)"/>
<line x1="920.1" y1="549.9" x2="920.1" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="918.91" y="554.1" width="2.44" height="25.1" fill="var(--up)"/>
<line x1="924.1" y1="552.0" x2="924.1" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="922.84" y="555.0" width="2.44" height="23.2" fill="var(--down)"/>
<line x1="928.0" y1="575.5" x2="928.0" y2="591.4" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="579.8" width="2.44" height="7.1" fill="var(--down)"/>
<line x1="931.9" y1="573.6" x2="931.9" y2="596.4" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="577.4" width="2.44" height="9.6" fill="var(--down)"/>
<line x1="935.9" y1="539.8" x2="935.9" y2="566.2" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="554.2" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="939.8" y1="526.2" x2="939.8" y2="573.6" stroke="var(--down)" class="wick"/>
<rect x="938.59" y="546.7" width="2.44" height="18.5" fill="var(--down)"/>
<line x1="943.7" y1="557.1" x2="943.7" y2="587.1" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="561.6" width="2.44" height="24.9" fill="var(--down)"/>
<line x1="947.7" y1="571.0" x2="947.7" y2="593.9" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="581.7" width="2.44" height="7.7" fill="var(--down)"/>
<line x1="951.6" y1="552.9" x2="951.6" y2="582.7" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="554.7" width="2.44" height="22.9" fill="var(--up)"/>
<line x1="955.6" y1="539.3" x2="955.6" y2="560.6" stroke="var(--down)" class="wick"/>
<rect x="954.34" y="543.2" width="2.44" height="4.5" fill="var(--down)"/>
<line x1="959.5" y1="521.9" x2="959.5" y2="543.7" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="522.9" width="2.44" height="18.9" fill="var(--up)"/>
<line x1="963.4" y1="505.7" x2="963.4" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="962.21" y="510.6" width="2.44" height="18.7" fill="var(--down)"/>
<line x1="967.4" y1="510.1" x2="967.4" y2="538.9" stroke="var(--up)" class="wick"/>
<rect x="966.14" y="518.4" width="2.44" height="16.8" fill="var(--up)"/>
<line x1="971.3" y1="496.3" x2="971.3" y2="519.1" stroke="var(--up)" class="wick"/>
<rect x="970.08" y="497.2" width="2.44" height="15.2" fill="var(--up)"/>
<line x1="975.2" y1="485.9" x2="975.2" y2="507.2" stroke="var(--down)" class="wick"/>
<rect x="974.02" y="497.2" width="2.44" height="9.1" fill="var(--down)"/>
<line x1="979.2" y1="504.9" x2="979.2" y2="526.4" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="505.7" width="2.44" height="2.3" fill="var(--down)"/>
<line x1="983.1" y1="492.2" x2="983.1" y2="509.5" stroke="var(--down)" class="wick"/>
<rect x="981.89" y="502.0" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="987.0" y1="495.3" x2="987.0" y2="523.1" stroke="var(--down)" class="wick"/>
<rect x="985.83" y="505.0" width="2.44" height="1.2" fill="var(--down)"/>
<line x1="991.0" y1="480.4" x2="991.0" y2="511.2" stroke="var(--up)" class="wick"/>
<rect x="989.76" y="485.6" width="2.44" height="15.6" fill="var(--up)"/>
<line x1="994.9" y1="476.6" x2="994.9" y2="506.7" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="493.8" width="2.44" height="9.3" fill="var(--down)"/>
<line x1="998.9" y1="503.9" x2="998.9" y2="525.9" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="508.2" width="2.44" height="13.5" fill="var(--down)"/>
<line x1="1002.8" y1="513.6" x2="1002.8" y2="529.3" stroke="var(--down)" class="wick"/>
<rect x="1001.57" y="520.0" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="1006.7" y1="528.0" x2="1006.7" y2="542.5" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="531.8" width="2.44" height="3.5" fill="var(--down)"/>
<line x1="1010.7" y1="526.8" x2="1010.7" y2="542.0" stroke="var(--down)" class="wick"/>
<rect x="1009.45" y="529.6" width="2.44" height="5.9" fill="var(--down)"/>
<line x1="1014.6" y1="539.5" x2="1014.6" y2="556.1" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="541.1" width="2.44" height="1.5" fill="var(--down)"/>
<line x1="1018.5" y1="507.9" x2="1018.5" y2="541.0" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="512.4" width="2.44" height="26.3" fill="var(--up)"/>
<line x1="1022.5" y1="489.6" x2="1022.5" y2="523.5" stroke="var(--up)" class="wick"/>
<rect x="1021.26" y="509.9" width="2.44" height="10.3" fill="var(--up)"/>
<line x1="1026.4" y1="393.8" x2="1026.4" y2="498.7" stroke="var(--up)" class="wick"/>
<rect x="1025.19" y="394.0" width="2.44" height="95.5" fill="var(--up)"/>
<line x1="1030.3" y1="399.2" x2="1030.3" y2="445.3" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="400.4" width="2.44" height="40.6" fill="var(--down)"/>
<line x1="1034.3" y1="434.2" x2="1034.3" y2="458.3" stroke="var(--up)" class="wick"/>
<rect x="1033.07" y="447.4" width="2.44" height="3.5" fill="var(--up)"/>
<line x1="1038.2" y1="465.8" x2="1038.2" y2="501.5" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="471.4" width="2.44" height="28.3" fill="var(--down)"/>
<line x1="1042.2" y1="491.5" x2="1042.2" y2="508.8" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="497.3" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="1046.1" y1="489.1" x2="1046.1" y2="503.3" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="490.7" width="2.44" height="5.9" fill="var(--down)"/>
<line x1="1050.0" y1="492.7" x2="1050.0" y2="572.5" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="492.7" width="2.44" height="51.3" fill="var(--down)"/>
<line x1="60" y1="426.7" x2="1052" y2="426.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="430.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$449 R1</text>
<text x="1058" y="442.2" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="371.4" x2="1052" y2="371.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="374.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$476 R2</text>
<text x="1058" y="386.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="322.0" x2="1052" y2="322.0" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="325.5" font-size="11.5" fill="var(--resistance)" font-weight="600">$499 R3</text>
<text x="1058" y="337.5" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="556.1" x2="1052" y2="556.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="550.1" font-size="11.5" fill="var(--support)" font-weight="600">$388 S1</text>
<text x="1058" y="562.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="577.8" x2="1052" y2="577.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="571.8" font-size="11.5" fill="var(--support)" font-weight="600">$378 S2</text>
<text x="1058" y="583.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="602.8" x2="1052" y2="602.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="596.8" font-size="11.5" fill="var(--support)" font-weight="600">$366 S3 (52주 최저)</text>
<text x="1058" y="608.8" font-size="9.5" fill="var(--muted)">터치 1회</text>
<circle cx="1052.0" cy="544.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="536.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $394 (2026-09-04)</text>
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
| R3 | $499 | 2 | 2025-10-01·2026-04-24 스윙 고점대 — 1년 창의 앞부분과 2026년 봄 반등의 상단이 겹친다 |
| R2 | $476 | 4 | 2025-10-27·2025-12-11·2026-06-23·2026-08-27 스윙 고점대 — **2026-08-27 실적 급등일의 종가($464.89)가 여기서 막혔다** |
| R1 | $449 | 4 | 2026-02-25·2026-03-05·2026-03-23·2026-07-13 스윙 고점대 — 현재가 위쪽에서 가장 가까운 저항 |
| **현재가** | **$393.84** (2026-09-04 종가) | — | R1과 S1 사이 |
| S1 | $388 | 2 | 2026-04-13·2026-08-24 스윙 저점대 — 현재가($393.84) 바로 아래 |
| S2 | $378 | 2 | 2025-11-18·2026-03-27 스윙 저점대 |
| S3 (52주 최저) | $366 | 1 | 2026-07-17 단일 저점(오픈소스 EDA 시연發 급락일의 장중 최저 $366.00). 터치 1회라 `--force-level`로 강제 포함했으므로 **지지선으로서의 신뢰도는 낮다** |
| 참고선 | $616 | — | 52주 최고(2025-09-08 $615.79). 1년 창의 첫 주 값이고 그 뒤 Ansys 통합·부채 상환으로 재무구조가 크게 달라져 **현재 레짐과 단절된 수준**이라 저항으로 보지 않는다 |

> **현재가($393.84)와 S1($388)의 간격이 1.5%에 불과하다.** 지지·저항 관점에서는 현재가가 지지 바로 위에 붙어 있는 상태이며, 그 아래로는 S2($378)·S3($366)까지 좁은 간격으로 이어진다 — **이 구간을 하향 이탈하면 최근 1년 안에 참고할 레벨이 사라진다.**

---

## 3. 관측된 특이 구간

### 3-1. 2026-07-17 — 오픈소스 EDA 자율설계 시연發 급락 (52주 최저)

- 중국 Moonshot AI가 오픈소스 EDA 도구만으로 칩 설계 플로우를 자율 완주했다고 공개한 날이다([최근 뉴스 / 이슈](./08_news.md) 로그 참고).
- 종가 기준 전일 대비 **−7.85%** ($417.03 → $384.28), 장중 **$366.00**으로 52주 최저. 거래량은 평소(일 229만 주 내외) 대비 약 **2.2배**인 **504만 주**.
- 같은 날 [Cadence](../cadence_design_systems/09_technical_daily.md)도 −9.47%로 동반 급락해 **업종 공통 재평가** 성격이었다.

### 3-2. 2026-08-27 — FY2026 Q3 실적發 급등, 그리고 6거래일 만의 전량 반납

- 8월 26일 장 마감 후 발표된 FY2026 3분기 실적·가이던스 상향에 다음날 종가가 **+13.39%**($410.00 → $464.89) 급등했다. 거래량 **407만 주**(평소의 1.8배).
- **그러나 이후 6거래일 만에 $393.84까지 −15.28% 되돌리며 발표 전 수준($410.00)마저 밑돌았다.** 이 구간의 하락은 회사 고유 악재 없이 금리 상승發 고밸류 성장주 디레이팅으로 설명된다(9월 1일 −5.63%, 9월 4일 −5.40%).
- 급등일 종가($464.89)가 R2($476)를 넘지 못하고 막힌 뒤 되돌려진 형태다. **실적이라는 펀더멘털 이벤트가 만든 상승분이 6거래일 만에 사라졌다는 사실 자체가, 지금 이 종목의 가격을 매크로가 지배하고 있음을 보여준다.**

---

## 4. 방법론 · 한계

@@FACTS@@
- **생성**: `scripts/gen_technical_chart.py SNPS --name Synopsys --event 2026-07-17:"오픈소스 EDA 우려 급락" --event 2026-08-26:"3Q26 실적·가이던스 상향" --ref-line 615.79:"52주 최고" --force-level '366.00:(52주 최저)' --close-on 2026-09-04 --emit all`
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **S3($366)는 터치 1회짜리 강제 포함 레벨이다.** 2026-07-17 하루의 장중 저점이므로 클러스터가 아니며, **지지선으로서의 통계적 근거가 없다** — 참고 하한으로만 볼 것.
    - **52주 최고 $615.79(2025-09-08)는 참고선으로만 두었다.** 1년 창의 첫 주에 형성된 값이고, 그 사이 Ansys 통합·부채 상환으로 회사의 재무구조가 크게 달라져 **현재 레짐과 단절돼 있다**([핵심 지표](./04_metrics.md) A.3).
    - 해당 기간에 주식분할·병합은 없었다. Ansys 인수 대가로 발행한 신주는 2025-07-17(이 차트 구간 이전)에 발행돼 가격 연속성에 영향을 주지 않는다.

---

*작성일: 2026-09-11*
