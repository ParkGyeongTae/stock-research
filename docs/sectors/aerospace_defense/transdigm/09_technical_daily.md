# 기술적 분석 (일봉 캔들차트 · 지지/저항)

> 최근 1년 일봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 여러 사이클에 걸친 다년 구조는 [기술적 분석 — 주봉·5년](./10_technical_weekly.md)(주봉·5년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 일봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(일봉 데이터는 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: **2026-08-24 종가 $1,199.08**이 [핵심 지표](./04_metrics.md) A.2와 [밸류에이션 / 적정주가](./06_valuation.md)에 인용된 값과 **일치**한다.
    - ⚠️ **차트의 마지막 봉(2026-08-25)은 수집 시점에 아직 장중이었다.** 거래량이 71,128주로 1년 평균(367,839주)의 5분의 1에 그쳐 미확정 봉임이 확인된다. 그래서 이 문서와 다른 문서의 기준 종가는 **마지막으로 정규장이 마감된 2026-08-24**로 통일했다.
    - **배당 조정 없음**: 원주가 기준이라 2025-09-12 지급된 주당 $90.00 특별배당이 반영돼 있지 않다 — 아래 3. 관측된 특이 구간 참고.

---

## 1. 차트 — 최근 1년 일봉 (2025-08-25 ~ 2026-08-25)

<div class="tdg-chart">
<style>
.tdg-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .tdg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .tdg-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.tdg-chart svg { width:100%; height:auto; display:block; }
.tdg-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.tdg-chart .title { fill: var(--ink); font-weight:600; }
.tdg-chart .grid { stroke: var(--grid); stroke-width:1; }
.tdg-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="TransDigm Group(TDG) 최근 1년 일봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">TransDigm Group (TDG) — 최근 1년 일봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-08-25 ~ 2026-08-25 · 마지막 종가 $1,185.54 (2026-08-25) · 단위 USD</text>
<line x1="60" y1="563.5" x2="1052" y2="563.5" class="grid"/>
<text x="52" y="567.5" font-size="11" text-anchor="end" fill="var(--muted)">1,150</text>
<line x1="60" y1="485.5" x2="1052" y2="485.5" class="grid"/>
<text x="52" y="489.5" font-size="11" text-anchor="end" fill="var(--muted)">1,200</text>
<line x1="60" y1="407.4" x2="1052" y2="407.4" class="grid"/>
<text x="52" y="411.4" font-size="11" text-anchor="end" fill="var(--muted)">1,250</text>
<line x1="60" y1="329.3" x2="1052" y2="329.3" class="grid"/>
<text x="52" y="333.3" font-size="11" text-anchor="end" fill="var(--muted)">1,300</text>
<line x1="60" y1="251.2" x2="1052" y2="251.2" class="grid"/>
<text x="52" y="255.2" font-size="11" text-anchor="end" fill="var(--muted)">1,350</text>
<line x1="60" y1="173.1" x2="1052" y2="173.1" class="grid"/>
<text x="52" y="177.1" font-size="11" text-anchor="end" fill="var(--muted)">1,400</text>
<line x1="60" y1="95.0" x2="1052" y2="95.0" class="grid"/>
<text x="52" y="99.0" font-size="11" text-anchor="end" fill="var(--muted)">1,450</text>
<line x1="62.0" y1="626.0" x2="62.0" y2="631.0" class="axis"/>
<text x="62.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-08</text>
<line x1="81.7" y1="626.0" x2="81.7" y2="631.0" class="axis"/>
<text x="81.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-09</text>
<line x1="164.3" y1="626.0" x2="164.3" y2="631.0" class="axis"/>
<text x="164.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-10</text>
<line x1="254.9" y1="626.0" x2="254.9" y2="631.0" class="axis"/>
<text x="254.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-11</text>
<line x1="329.7" y1="626.0" x2="329.7" y2="631.0" class="axis"/>
<text x="329.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">25-12</text>
<line x1="416.3" y1="626.0" x2="416.3" y2="631.0" class="axis"/>
<text x="416.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-01</text>
<line x1="495.0" y1="626.0" x2="495.0" y2="631.0" class="axis"/>
<text x="495.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-02</text>
<line x1="569.8" y1="626.0" x2="569.8" y2="631.0" class="axis"/>
<text x="569.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-03</text>
<line x1="656.4" y1="626.0" x2="656.4" y2="631.0" class="axis"/>
<text x="656.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-04</text>
<line x1="739.0" y1="626.0" x2="739.0" y2="631.0" class="axis"/>
<text x="739.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-05</text>
<line x1="817.8" y1="626.0" x2="817.8" y2="631.0" class="axis"/>
<text x="817.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-06</text>
<line x1="900.4" y1="626.0" x2="900.4" y2="631.0" class="axis"/>
<text x="900.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-07</text>
<line x1="987.0" y1="626.0" x2="987.0" y2="631.0" class="axis"/>
<text x="987.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">26-08</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="74.7" x2="1052" y2="74.7" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="77.7" font-size="10.5" fill="var(--muted)">$1,463 52주 최고</text>
<line x1="113.1" y1="56.0" x2="113.1" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="119.1" y="68.0" font-size="10.5" fill="var(--down)">2025-09-12 주당 $90 특별배당 지급</text>
<line x1="668.2" y1="56.0" x2="668.2" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="674.2" y="68.0" font-size="10.5" fill="var(--down)">2026-04-07 JPE·Victor Sierra 인수</text>
<line x1="991.0" y1="56.0" x2="991.0" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="997.0" y="68.0" font-size="10.5" fill="var(--down)">2026-08-04 FY26 Q3 실적·가이던스 상향</text>
<line x1="62.0" y1="141.6" x2="62.0" y2="193.9" stroke="var(--down)" class="wick"/>
<rect x="60.75" y="159.1" width="2.44" height="29.7" fill="var(--down)"/>
<line x1="65.9" y1="150.6" x2="65.9" y2="184.4" stroke="var(--up)" class="wick"/>
<rect x="64.68" y="152.3" width="2.44" height="30.4" fill="var(--up)"/>
<line x1="69.8" y1="130.3" x2="69.8" y2="180.9" stroke="var(--down)" class="wick"/>
<rect x="68.62" y="153.0" width="2.44" height="27.9" fill="var(--down)"/>
<line x1="73.8" y1="153.6" x2="73.8" y2="192.3" stroke="var(--up)" class="wick"/>
<rect x="72.56" y="176.2" width="2.44" height="1.9" fill="var(--up)"/>
<line x1="77.7" y1="169.2" x2="77.7" y2="185.2" stroke="var(--down)" class="wick"/>
<rect x="76.49" y="171.7" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="81.7" y1="302.6" x2="81.7" y2="346.1" stroke="var(--up)" class="wick"/>
<rect x="80.43" y="321.7" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="85.6" y1="321.5" x2="85.6" y2="368.9" stroke="var(--down)" class="wick"/>
<rect x="84.37" y="323.0" width="2.44" height="39.9" fill="var(--down)"/>
<line x1="89.5" y1="355.6" x2="89.5" y2="387.1" stroke="var(--down)" class="wick"/>
<rect x="88.30" y="356.3" width="2.44" height="1.4" fill="var(--down)"/>
<line x1="93.5" y1="352.6" x2="93.5" y2="391.1" stroke="var(--down)" class="wick"/>
<rect x="92.24" y="353.6" width="2.44" height="20.9" fill="var(--down)"/>
<line x1="97.4" y1="336.4" x2="97.4" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="96.18" y="339.8" width="2.44" height="64.4" fill="var(--up)"/>
<line x1="101.3" y1="306.4" x2="101.3" y2="363.9" stroke="var(--up)" class="wick"/>
<rect x="100.11" y="310.4" width="2.44" height="35.3" fill="var(--up)"/>
<line x1="105.3" y1="290.4" x2="105.3" y2="368.1" stroke="var(--down)" class="wick"/>
<rect x="104.05" y="306.7" width="2.44" height="42.4" fill="var(--down)"/>
<line x1="109.2" y1="325.1" x2="109.2" y2="353.9" stroke="var(--up)" class="wick"/>
<rect x="107.99" y="339.8" width="2.44" height="5.8" fill="var(--up)"/>
<line x1="113.1" y1="323.6" x2="113.1" y2="377.2" stroke="var(--down)" class="wick"/>
<rect x="111.92" y="339.4" width="2.44" height="34.5" fill="var(--down)"/>
<line x1="117.1" y1="330.0" x2="117.1" y2="370.4" stroke="var(--up)" class="wick"/>
<rect x="115.86" y="347.8" width="2.44" height="19.6" fill="var(--up)"/>
<line x1="121.0" y1="322.5" x2="121.0" y2="361.1" stroke="var(--down)" class="wick"/>
<rect x="119.80" y="325.8" width="2.44" height="32.0" fill="var(--down)"/>
<line x1="125.0" y1="341.0" x2="125.0" y2="383.2" stroke="var(--up)" class="wick"/>
<rect x="123.73" y="366.8" width="2.44" height="4.6" fill="var(--up)"/>
<line x1="128.9" y1="345.0" x2="128.9" y2="372.6" stroke="var(--up)" class="wick"/>
<rect x="127.67" y="351.0" width="2.44" height="13.4" fill="var(--up)"/>
<line x1="132.8" y1="332.5" x2="132.8" y2="370.5" stroke="var(--down)" class="wick"/>
<rect x="131.61" y="341.0" width="2.44" height="15.7" fill="var(--down)"/>
<line x1="136.8" y1="335.2" x2="136.8" y2="374.3" stroke="var(--up)" class="wick"/>
<rect x="135.54" y="336.6" width="2.44" height="30.0" fill="var(--up)"/>
<line x1="140.7" y1="322.2" x2="140.7" y2="342.9" stroke="var(--up)" class="wick"/>
<rect x="139.48" y="330.3" width="2.44" height="9.9" fill="var(--up)"/>
<line x1="144.6" y1="298.1" x2="144.6" y2="332.5" stroke="var(--up)" class="wick"/>
<rect x="143.41" y="329.3" width="2.44" height="1.0" fill="var(--up)"/>
<line x1="148.6" y1="334.1" x2="148.6" y2="377.9" stroke="var(--down)" class="wick"/>
<rect x="147.35" y="334.1" width="2.44" height="10.8" fill="var(--down)"/>
<line x1="152.5" y1="323.8" x2="152.5" y2="342.7" stroke="var(--down)" class="wick"/>
<rect x="151.29" y="330.8" width="2.44" height="5.2" fill="var(--down)"/>
<line x1="156.4" y1="316.7" x2="156.4" y2="358.8" stroke="var(--down)" class="wick"/>
<rect x="155.22" y="330.8" width="2.44" height="15.2" fill="var(--down)"/>
<line x1="160.4" y1="293.0" x2="160.4" y2="352.6" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="301.1" width="2.44" height="42.4" fill="var(--up)"/>
<line x1="164.3" y1="277.7" x2="164.3" y2="331.9" stroke="var(--down)" class="wick"/>
<rect x="163.10" y="321.9" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="168.3" y1="321.7" x2="168.3" y2="365.7" stroke="var(--down)" class="wick"/>
<rect x="167.03" y="335.7" width="2.44" height="18.8" fill="var(--down)"/>
<line x1="172.2" y1="339.8" x2="172.2" y2="364.3" stroke="var(--up)" class="wick"/>
<rect x="170.97" y="346.7" width="2.44" height="14.0" fill="var(--up)"/>
<line x1="176.1" y1="334.6" x2="176.1" y2="369.1" stroke="var(--up)" class="wick"/>
<rect x="174.91" y="342.2" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="180.1" y1="323.6" x2="180.1" y2="354.5" stroke="var(--down)" class="wick"/>
<rect x="178.84" y="342.2" width="2.44" height="11.5" fill="var(--down)"/>
<line x1="184.0" y1="343.5" x2="184.0" y2="364.5" stroke="var(--up)" class="wick"/>
<rect x="182.78" y="351.4" width="2.44" height="13.1" fill="var(--up)"/>
<line x1="187.9" y1="350.0" x2="187.9" y2="372.9" stroke="var(--down)" class="wick"/>
<rect x="186.72" y="352.7" width="2.44" height="14.9" fill="var(--down)"/>
<line x1="191.9" y1="348.3" x2="191.9" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="190.65" y="363.7" width="2.44" height="7.6" fill="var(--up)"/>
<line x1="195.8" y1="338.8" x2="195.8" y2="376.3" stroke="var(--up)" class="wick"/>
<rect x="194.59" y="340.1" width="2.44" height="17.1" fill="var(--up)"/>
<line x1="199.7" y1="294.5" x2="199.7" y2="354.3" stroke="var(--up)" class="wick"/>
<rect x="198.53" y="309.8" width="2.44" height="39.9" fill="var(--up)"/>
<line x1="203.7" y1="308.6" x2="203.7" y2="429.7" stroke="var(--down)" class="wick"/>
<rect x="202.46" y="330.3" width="2.44" height="96.3" fill="var(--down)"/>
<line x1="207.6" y1="376.1" x2="207.6" y2="422.4" stroke="var(--up)" class="wick"/>
<rect x="206.40" y="408.3" width="2.44" height="9.8" fill="var(--up)"/>
<line x1="211.6" y1="376.0" x2="211.6" y2="407.6" stroke="var(--up)" class="wick"/>
<rect x="210.34" y="382.6" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="215.5" y1="311.9" x2="215.5" y2="376.9" stroke="var(--up)" class="wick"/>
<rect x="214.27" y="326.7" width="2.44" height="49.5" fill="var(--up)"/>
<line x1="219.4" y1="279.6" x2="219.4" y2="314.5" stroke="var(--up)" class="wick"/>
<rect x="218.21" y="283.7" width="2.44" height="24.4" fill="var(--up)"/>
<line x1="223.4" y1="278.5" x2="223.4" y2="307.8" stroke="var(--down)" class="wick"/>
<rect x="222.14" y="292.3" width="2.44" height="14.8" fill="var(--down)"/>
<line x1="227.3" y1="248.5" x2="227.3" y2="307.1" stroke="var(--up)" class="wick"/>
<rect x="226.08" y="251.2" width="2.44" height="55.9" fill="var(--up)"/>
<line x1="231.2" y1="233.2" x2="231.2" y2="255.1" stroke="var(--up)" class="wick"/>
<rect x="230.02" y="236.7" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="235.2" y1="226.5" x2="235.2" y2="256.5" stroke="var(--down)" class="wick"/>
<rect x="233.95" y="243.8" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="239.1" y1="240.4" x2="239.1" y2="275.7" stroke="var(--down)" class="wick"/>
<rect x="237.89" y="244.2" width="2.44" height="30.2" fill="var(--down)"/>
<line x1="243.0" y1="270.2" x2="243.0" y2="326.8" stroke="var(--down)" class="wick"/>
<rect x="241.83" y="286.8" width="2.44" height="17.5" fill="var(--down)"/>
<line x1="247.0" y1="276.8" x2="247.0" y2="322.8" stroke="var(--down)" class="wick"/>
<rect x="245.76" y="309.3" width="2.44" height="10.4" fill="var(--down)"/>
<line x1="250.9" y1="311.5" x2="250.9" y2="328.4" stroke="var(--up)" class="wick"/>
<rect x="249.70" y="316.0" width="2.44" height="11.7" fill="var(--up)"/>
<line x1="254.9" y1="312.4" x2="254.9" y2="340.5" stroke="var(--down)" class="wick"/>
<rect x="253.64" y="315.5" width="2.44" height="13.8" fill="var(--down)"/>
<line x1="258.8" y1="316.5" x2="258.8" y2="355.8" stroke="var(--down)" class="wick"/>
<rect x="257.57" y="340.9" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="262.7" y1="330.3" x2="262.7" y2="389.5" stroke="var(--down)" class="wick"/>
<rect x="261.51" y="367.5" width="2.44" height="14.4" fill="var(--down)"/>
<line x1="266.7" y1="361.0" x2="266.7" y2="405.5" stroke="var(--up)" class="wick"/>
<rect x="265.45" y="373.6" width="2.44" height="17.2" fill="var(--up)"/>
<line x1="270.6" y1="350.6" x2="270.6" y2="398.8" stroke="var(--up)" class="wick"/>
<rect x="269.38" y="353.1" width="2.44" height="37.0" fill="var(--up)"/>
<line x1="274.5" y1="335.2" x2="274.5" y2="376.1" stroke="var(--up)" class="wick"/>
<rect x="273.32" y="346.6" width="2.44" height="11.6" fill="var(--up)"/>
<line x1="278.5" y1="334.9" x2="278.5" y2="371.1" stroke="var(--up)" class="wick"/>
<rect x="277.26" y="338.7" width="2.44" height="13.7" fill="var(--up)"/>
<line x1="282.4" y1="264.3" x2="282.4" y2="361.9" stroke="var(--up)" class="wick"/>
<rect x="281.19" y="316.8" width="2.44" height="45.0" fill="var(--up)"/>
<line x1="286.3" y1="238.7" x2="286.3" y2="310.3" stroke="var(--up)" class="wick"/>
<rect x="285.13" y="290.2" width="2.44" height="3.9" fill="var(--up)"/>
<line x1="290.3" y1="236.9" x2="290.3" y2="294.3" stroke="var(--up)" class="wick"/>
<rect x="289.07" y="265.9" width="2.44" height="18.0" fill="var(--up)"/>
<line x1="294.2" y1="241.3" x2="294.2" y2="288.4" stroke="var(--down)" class="wick"/>
<rect x="293.00" y="255.4" width="2.44" height="18.0" fill="var(--down)"/>
<line x1="298.2" y1="226.7" x2="298.2" y2="269.6" stroke="var(--up)" class="wick"/>
<rect x="296.94" y="249.6" width="2.44" height="9.4" fill="var(--up)"/>
<line x1="302.1" y1="237.4" x2="302.1" y2="290.9" stroke="var(--down)" class="wick"/>
<rect x="300.87" y="261.7" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="306.0" y1="229.1" x2="306.0" y2="296.0" stroke="var(--down)" class="wick"/>
<rect x="304.81" y="246.7" width="2.44" height="39.1" fill="var(--down)"/>
<line x1="310.0" y1="234.3" x2="310.0" y2="302.7" stroke="var(--up)" class="wick"/>
<rect x="308.75" y="255.5" width="2.44" height="27.5" fill="var(--up)"/>
<line x1="313.9" y1="245.2" x2="313.9" y2="279.6" stroke="var(--down)" class="wick"/>
<rect x="312.68" y="264.7" width="2.44" height="8.7" fill="var(--down)"/>
<line x1="317.8" y1="232.4" x2="317.8" y2="279.4" stroke="var(--up)" class="wick"/>
<rect x="316.62" y="247.2" width="2.44" height="21.5" fill="var(--up)"/>
<line x1="321.8" y1="235.0" x2="321.8" y2="251.7" stroke="var(--up)" class="wick"/>
<rect x="320.56" y="243.4" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="325.7" y1="231.1" x2="325.7" y2="258.9" stroke="var(--up)" class="wick"/>
<rect x="324.49" y="235.3" width="2.44" height="8.1" fill="var(--up)"/>
<line x1="329.7" y1="236.9" x2="329.7" y2="266.8" stroke="var(--up)" class="wick"/>
<rect x="328.43" y="243.6" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="333.6" y1="235.6" x2="333.6" y2="278.3" stroke="var(--down)" class="wick"/>
<rect x="332.37" y="235.6" width="2.44" height="25.5" fill="var(--down)"/>
<line x1="337.5" y1="252.0" x2="337.5" y2="279.1" stroke="var(--down)" class="wick"/>
<rect x="336.30" y="255.1" width="2.44" height="15.9" fill="var(--down)"/>
<line x1="341.5" y1="223.6" x2="341.5" y2="270.6" stroke="var(--up)" class="wick"/>
<rect x="340.24" y="235.4" width="2.44" height="26.3" fill="var(--up)"/>
<line x1="345.4" y1="236.9" x2="345.4" y2="265.1" stroke="var(--down)" class="wick"/>
<rect x="344.18" y="241.1" width="2.44" height="15.0" fill="var(--down)"/>
<line x1="349.3" y1="246.3" x2="349.3" y2="278.1" stroke="var(--up)" class="wick"/>
<rect x="348.11" y="255.6" width="2.44" height="4.1" fill="var(--up)"/>
<line x1="353.3" y1="240.4" x2="353.3" y2="306.5" stroke="var(--down)" class="wick"/>
<rect x="352.05" y="255.4" width="2.44" height="45.8" fill="var(--down)"/>
<line x1="357.2" y1="294.2" x2="357.2" y2="365.2" stroke="var(--down)" class="wick"/>
<rect x="355.99" y="298.1" width="2.44" height="26.7" fill="var(--down)"/>
<line x1="361.1" y1="299.4" x2="361.1" y2="323.0" stroke="var(--up)" class="wick"/>
<rect x="359.92" y="302.0" width="2.44" height="10.6" fill="var(--up)"/>
<line x1="365.1" y1="296.1" x2="365.1" y2="340.1" stroke="var(--down)" class="wick"/>
<rect x="363.86" y="298.1" width="2.44" height="39.6" fill="var(--down)"/>
<line x1="369.0" y1="310.0" x2="369.0" y2="357.2" stroke="var(--down)" class="wick"/>
<rect x="367.80" y="319.0" width="2.44" height="22.6" fill="var(--down)"/>
<line x1="373.0" y1="341.0" x2="373.0" y2="385.1" stroke="var(--down)" class="wick"/>
<rect x="371.73" y="345.2" width="2.44" height="30.0" fill="var(--down)"/>
<line x1="376.9" y1="349.9" x2="376.9" y2="397.2" stroke="var(--down)" class="wick"/>
<rect x="375.67" y="385.8" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="380.8" y1="365.6" x2="380.8" y2="427.5" stroke="var(--down)" class="wick"/>
<rect x="379.61" y="374.6" width="2.44" height="12.8" fill="var(--down)"/>
<line x1="384.8" y1="359.0" x2="384.8" y2="390.2" stroke="var(--up)" class="wick"/>
<rect x="383.54" y="365.5" width="2.44" height="20.7" fill="var(--up)"/>
<line x1="388.7" y1="324.4" x2="388.7" y2="365.9" stroke="var(--up)" class="wick"/>
<rect x="387.48" y="326.5" width="2.44" height="34.0" fill="var(--up)"/>
<line x1="392.6" y1="300.9" x2="392.6" y2="335.1" stroke="var(--up)" class="wick"/>
<rect x="391.41" y="306.6" width="2.44" height="14.2" fill="var(--up)"/>
<line x1="396.6" y1="298.2" x2="396.6" y2="312.3" stroke="var(--up)" class="wick"/>
<rect x="395.35" y="308.1" width="2.44" height="3.2" fill="var(--up)"/>
<line x1="400.5" y1="303.2" x2="400.5" y2="321.5" stroke="var(--down)" class="wick"/>
<rect x="399.29" y="314.5" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="404.4" y1="297.0" x2="404.4" y2="313.7" stroke="var(--up)" class="wick"/>
<rect x="403.22" y="304.4" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="408.4" y1="298.2" x2="408.4" y2="322.4" stroke="var(--up)" class="wick"/>
<rect x="407.16" y="303.6" width="2.44" height="5.9" fill="var(--up)"/>
<line x1="412.3" y1="265.2" x2="412.3" y2="291.9" stroke="var(--up)" class="wick"/>
<rect x="411.10" y="282.7" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="416.3" y1="235.6" x2="416.3" y2="298.4" stroke="var(--up)" class="wick"/>
<rect x="415.03" y="237.9" width="2.44" height="46.1" fill="var(--up)"/>
<line x1="420.2" y1="191.9" x2="420.2" y2="238.3" stroke="var(--up)" class="wick"/>
<rect x="418.97" y="223.3" width="2.44" height="15.0" fill="var(--up)"/>
<line x1="424.1" y1="189.9" x2="424.1" y2="225.2" stroke="var(--up)" class="wick"/>
<rect x="422.91" y="197.5" width="2.44" height="25.4" fill="var(--up)"/>
<line x1="428.1" y1="180.9" x2="428.1" y2="203.8" stroke="var(--down)" class="wick"/>
<rect x="426.84" y="193.2" width="2.44" height="3.0" fill="var(--down)"/>
<line x1="432.0" y1="150.4" x2="432.0" y2="241.5" stroke="var(--down)" class="wick"/>
<rect x="430.78" y="168.1" width="2.44" height="40.2" fill="var(--down)"/>
<line x1="435.9" y1="180.9" x2="435.9" y2="242.5" stroke="var(--up)" class="wick"/>
<rect x="434.72" y="185.5" width="2.44" height="20.2" fill="var(--up)"/>
<line x1="439.9" y1="173.9" x2="439.9" y2="210.4" stroke="var(--down)" class="wick"/>
<rect x="438.65" y="186.4" width="2.44" height="8.4" fill="var(--down)"/>
<line x1="443.8" y1="177.2" x2="443.8" y2="211.8" stroke="var(--down)" class="wick"/>
<rect x="442.59" y="177.2" width="2.44" height="24.1" fill="var(--down)"/>
<line x1="447.7" y1="135.9" x2="447.7" y2="213.0" stroke="var(--up)" class="wick"/>
<rect x="446.53" y="135.9" width="2.44" height="59.8" fill="var(--up)"/>
<line x1="451.7" y1="111.6" x2="451.7" y2="144.2" stroke="var(--up)" class="wick"/>
<rect x="450.46" y="120.7" width="2.44" height="13.5" fill="var(--up)"/>
<line x1="455.6" y1="74.7" x2="455.6" y2="116.2" stroke="var(--up)" class="wick"/>
<rect x="454.40" y="95.0" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="459.6" y1="86.8" x2="459.6" y2="113.2" stroke="var(--up)" class="wick"/>
<rect x="458.34" y="97.3" width="2.44" height="6.2" fill="var(--up)"/>
<line x1="463.5" y1="79.4" x2="463.5" y2="138.6" stroke="var(--down)" class="wick"/>
<rect x="462.27" y="89.4" width="2.44" height="5.7" fill="var(--down)"/>
<line x1="467.4" y1="93.5" x2="467.4" y2="142.9" stroke="var(--down)" class="wick"/>
<rect x="466.21" y="98.6" width="2.44" height="42.5" fill="var(--down)"/>
<line x1="471.4" y1="115.7" x2="471.4" y2="183.5" stroke="var(--down)" class="wick"/>
<rect x="470.14" y="136.9" width="2.44" height="6.2" fill="var(--down)"/>
<line x1="475.3" y1="100.7" x2="475.3" y2="156.3" stroke="var(--up)" class="wick"/>
<rect x="474.08" y="117.0" width="2.44" height="35.5" fill="var(--up)"/>
<line x1="479.2" y1="96.7" x2="479.2" y2="137.7" stroke="var(--down)" class="wick"/>
<rect x="478.02" y="112.7" width="2.44" height="18.0" fill="var(--down)"/>
<line x1="483.2" y1="135.6" x2="483.2" y2="171.4" stroke="var(--down)" class="wick"/>
<rect x="481.95" y="146.3" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="487.1" y1="117.2" x2="487.1" y2="153.5" stroke="var(--up)" class="wick"/>
<rect x="485.89" y="138.8" width="2.44" height="14.7" fill="var(--up)"/>
<line x1="491.0" y1="124.2" x2="491.0" y2="154.9" stroke="var(--up)" class="wick"/>
<rect x="489.83" y="130.1" width="2.44" height="2.5" fill="var(--up)"/>
<line x1="495.0" y1="109.3" x2="495.0" y2="165.8" stroke="var(--up)" class="wick"/>
<rect x="493.76" y="117.7" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="498.9" y1="206.9" x2="498.9" y2="391.7" stroke="var(--down)" class="wick"/>
<rect x="497.70" y="207.5" width="2.44" height="118.8" fill="var(--down)"/>
<line x1="502.9" y1="343.2" x2="502.9" y2="409.8" stroke="var(--down)" class="wick"/>
<rect x="501.64" y="357.0" width="2.44" height="27.3" fill="var(--down)"/>
<line x1="506.8" y1="376.9" x2="506.8" y2="413.9" stroke="var(--up)" class="wick"/>
<rect x="505.57" y="386.7" width="2.44" height="9.5" fill="var(--up)"/>
<line x1="510.7" y1="328.3" x2="510.7" y2="375.7" stroke="var(--up)" class="wick"/>
<rect x="509.51" y="351.9" width="2.44" height="19.6" fill="var(--up)"/>
<line x1="514.7" y1="320.2" x2="514.7" y2="366.6" stroke="var(--up)" class="wick"/>
<rect x="513.45" y="329.1" width="2.44" height="32.4" fill="var(--up)"/>
<line x1="518.6" y1="278.7" x2="518.6" y2="328.0" stroke="var(--down)" class="wick"/>
<rect x="517.38" y="297.8" width="2.44" height="12.8" fill="var(--down)"/>
<line x1="522.5" y1="281.2" x2="522.5" y2="318.8" stroke="var(--up)" class="wick"/>
<rect x="521.32" y="288.4" width="2.44" height="18.2" fill="var(--up)"/>
<line x1="526.5" y1="267.1" x2="526.5" y2="344.1" stroke="var(--down)" class="wick"/>
<rect x="525.26" y="276.5" width="2.44" height="59.0" fill="var(--down)"/>
<line x1="530.4" y1="300.1" x2="530.4" y2="359.3" stroke="var(--down)" class="wick"/>
<rect x="529.19" y="323.8" width="2.44" height="26.3" fill="var(--down)"/>
<line x1="534.3" y1="319.4" x2="534.3" y2="362.4" stroke="var(--up)" class="wick"/>
<rect x="533.13" y="326.0" width="2.44" height="5.1" fill="var(--up)"/>
<line x1="538.3" y1="290.3" x2="538.3" y2="332.9" stroke="var(--up)" class="wick"/>
<rect x="537.07" y="305.3" width="2.44" height="3.1" fill="var(--up)"/>
<line x1="542.2" y1="266.8" x2="542.2" y2="316.9" stroke="var(--up)" class="wick"/>
<rect x="541.00" y="282.2" width="2.44" height="27.3" fill="var(--up)"/>
<line x1="546.2" y1="251.2" x2="546.2" y2="292.8" stroke="var(--up)" class="wick"/>
<rect x="544.94" y="268.4" width="2.44" height="15.2" fill="var(--up)"/>
<line x1="550.1" y1="275.1" x2="550.1" y2="339.4" stroke="var(--down)" class="wick"/>
<rect x="548.87" y="280.4" width="2.44" height="54.9" fill="var(--down)"/>
<line x1="554.0" y1="326.5" x2="554.0" y2="368.3" stroke="var(--up)" class="wick"/>
<rect x="552.81" y="338.9" width="2.44" height="3.8" fill="var(--up)"/>
<line x1="558.0" y1="325.4" x2="558.0" y2="386.7" stroke="var(--down)" class="wick"/>
<rect x="556.75" y="329.6" width="2.44" height="7.3" fill="var(--down)"/>
<line x1="561.9" y1="306.7" x2="561.9" y2="350.0" stroke="var(--up)" class="wick"/>
<rect x="560.68" y="307.0" width="2.44" height="22.4" fill="var(--up)"/>
<line x1="565.8" y1="310.3" x2="565.8" y2="344.2" stroke="var(--down)" class="wick"/>
<rect x="564.62" y="321.6" width="2.44" height="3.3" fill="var(--down)"/>
<line x1="569.8" y1="287.0" x2="569.8" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="568.56" y="303.9" width="2.44" height="9.3" fill="var(--up)"/>
<line x1="573.7" y1="275.8" x2="573.7" y2="352.7" stroke="var(--up)" class="wick"/>
<rect x="572.49" y="288.2" width="2.44" height="31.8" fill="var(--up)"/>
<line x1="577.7" y1="281.4" x2="577.7" y2="323.1" stroke="var(--down)" class="wick"/>
<rect x="576.43" y="287.1" width="2.44" height="18.6" fill="var(--down)"/>
<line x1="581.6" y1="313.0" x2="581.6" y2="361.0" stroke="var(--down)" class="wick"/>
<rect x="580.37" y="317.3" width="2.44" height="19.9" fill="var(--down)"/>
<line x1="585.5" y1="299.9" x2="585.5" y2="357.4" stroke="var(--up)" class="wick"/>
<rect x="584.30" y="337.8" width="2.44" height="10.8" fill="var(--up)"/>
<line x1="589.5" y1="348.3" x2="589.5" y2="405.2" stroke="var(--down)" class="wick"/>
<rect x="588.24" y="348.3" width="2.44" height="15.4" fill="var(--down)"/>
<line x1="593.4" y1="368.6" x2="593.4" y2="403.4" stroke="var(--down)" class="wick"/>
<rect x="592.18" y="374.4" width="2.44" height="4.4" fill="var(--down)"/>
<line x1="597.3" y1="380.0" x2="597.3" y2="412.4" stroke="var(--down)" class="wick"/>
<rect x="596.11" y="387.1" width="2.44" height="7.3" fill="var(--down)"/>
<line x1="601.3" y1="385.4" x2="601.3" y2="450.1" stroke="var(--down)" class="wick"/>
<rect x="600.05" y="413.2" width="2.44" height="31.7" fill="var(--down)"/>
<line x1="605.2" y1="404.9" x2="605.2" y2="472.2" stroke="var(--down)" class="wick"/>
<rect x="603.99" y="431.4" width="2.44" height="31.2" fill="var(--down)"/>
<line x1="609.1" y1="405.3" x2="609.1" y2="449.9" stroke="var(--up)" class="wick"/>
<rect x="607.92" y="410.8" width="2.44" height="39.1" fill="var(--up)"/>
<line x1="613.1" y1="384.9" x2="613.1" y2="448.0" stroke="var(--down)" class="wick"/>
<rect x="611.86" y="400.6" width="2.44" height="34.0" fill="var(--down)"/>
<line x1="617.0" y1="431.8" x2="617.0" y2="488.2" stroke="var(--down)" class="wick"/>
<rect x="615.80" y="439.2" width="2.44" height="46.3" fill="var(--down)"/>
<line x1="621.0" y1="483.9" x2="621.0" y2="521.3" stroke="var(--down)" class="wick"/>
<rect x="619.73" y="490.3" width="2.44" height="7.7" fill="var(--down)"/>
<line x1="624.9" y1="479.6" x2="624.9" y2="533.3" stroke="var(--down)" class="wick"/>
<rect x="623.67" y="497.2" width="2.44" height="23.5" fill="var(--down)"/>
<line x1="628.8" y1="467.1" x2="628.8" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="627.61" y="497.8" width="2.44" height="61.1" fill="var(--down)"/>
<line x1="632.8" y1="543.5" x2="632.8" y2="583.7" stroke="var(--up)" class="wick"/>
<rect x="631.54" y="543.6" width="2.44" height="26.1" fill="var(--up)"/>
<line x1="636.7" y1="513.9" x2="636.7" y2="565.1" stroke="var(--down)" class="wick"/>
<rect x="635.48" y="525.8" width="2.44" height="27.6" fill="var(--down)"/>
<line x1="640.6" y1="545.8" x2="640.6" y2="577.6" stroke="var(--up)" class="wick"/>
<rect x="639.41" y="560.5" width="2.44" height="12.5" fill="var(--up)"/>
<line x1="644.6" y1="558.1" x2="644.6" y2="581.0" stroke="var(--down)" class="wick"/>
<rect x="643.35" y="568.0" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="648.5" y1="556.7" x2="648.5" y2="598.6" stroke="var(--down)" class="wick"/>
<rect x="647.29" y="566.5" width="2.44" height="23.8" fill="var(--down)"/>
<line x1="652.4" y1="534.9" x2="652.4" y2="599.9" stroke="var(--up)" class="wick"/>
<rect x="651.22" y="549.5" width="2.44" height="29.6" fill="var(--up)"/>
<line x1="656.4" y1="510.5" x2="656.4" y2="604.7" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="527.2" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="660.3" y1="524.0" x2="660.3" y2="571.3" stroke="var(--up)" class="wick"/>
<rect x="659.10" y="537.0" width="2.44" height="1.6" fill="var(--up)"/>
<line x1="664.3" y1="501.0" x2="664.3" y2="550.3" stroke="var(--up)" class="wick"/>
<rect x="663.03" y="501.6" width="2.44" height="33.8" fill="var(--up)"/>
<line x1="668.2" y1="512.2" x2="668.2" y2="540.0" stroke="var(--down)" class="wick"/>
<rect x="666.97" y="512.2" width="2.44" height="20.8" fill="var(--down)"/>
<line x1="672.1" y1="446.0" x2="672.1" y2="499.2" stroke="var(--up)" class="wick"/>
<rect x="670.91" y="454.4" width="2.44" height="44.8" fill="var(--up)"/>
<line x1="676.1" y1="432.2" x2="676.1" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="674.84" y="445.6" width="2.44" height="21.3" fill="var(--up)"/>
<line x1="680.0" y1="452.7" x2="680.0" y2="486.4" stroke="var(--down)" class="wick"/>
<rect x="678.78" y="452.7" width="2.44" height="21.6" fill="var(--down)"/>
<line x1="683.9" y1="430.0" x2="683.9" y2="483.8" stroke="var(--up)" class="wick"/>
<rect x="682.72" y="433.7" width="2.44" height="40.5" fill="var(--up)"/>
<line x1="687.9" y1="324.5" x2="687.9" y2="377.9" stroke="var(--up)" class="wick"/>
<rect x="686.65" y="334.6" width="2.44" height="27.1" fill="var(--up)"/>
<line x1="691.8" y1="327.1" x2="691.8" y2="370.3" stroke="var(--down)" class="wick"/>
<rect x="690.59" y="333.8" width="2.44" height="35.0" fill="var(--down)"/>
<line x1="695.7" y1="362.9" x2="695.7" y2="456.9" stroke="var(--down)" class="wick"/>
<rect x="694.53" y="367.3" width="2.44" height="74.1" fill="var(--down)"/>
<line x1="699.7" y1="344.7" x2="699.7" y2="430.8" stroke="var(--up)" class="wick"/>
<rect x="698.46" y="382.6" width="2.44" height="42.0" fill="var(--up)"/>
<line x1="703.6" y1="368.7" x2="703.6" y2="391.8" stroke="var(--up)" class="wick"/>
<rect x="702.40" y="368.9" width="2.44" height="14.6" fill="var(--up)"/>
<line x1="707.6" y1="369.1" x2="707.6" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="706.34" y="380.4" width="2.44" height="96.2" fill="var(--down)"/>
<line x1="711.5" y1="462.8" x2="711.5" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="710.27" y="473.0" width="2.44" height="31.6" fill="var(--down)"/>
<line x1="715.4" y1="488.7" x2="715.4" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="714.21" y="503.7" width="2.44" height="35.2" fill="var(--down)"/>
<line x1="719.4" y1="546.2" x2="719.4" y2="585.0" stroke="var(--down)" class="wick"/>
<rect x="718.14" y="552.8" width="2.44" height="13.6" fill="var(--down)"/>
<line x1="723.3" y1="538.7" x2="723.3" y2="569.2" stroke="var(--up)" class="wick"/>
<rect x="722.08" y="550.5" width="2.44" height="18.7" fill="var(--up)"/>
<line x1="727.2" y1="527.6" x2="727.2" y2="584.8" stroke="var(--down)" class="wick"/>
<rect x="726.02" y="536.1" width="2.44" height="21.1" fill="var(--down)"/>
<line x1="731.2" y1="555.7" x2="731.2" y2="597.6" stroke="var(--down)" class="wick"/>
<rect x="729.95" y="557.0" width="2.44" height="17.9" fill="var(--down)"/>
<line x1="735.1" y1="541.1" x2="735.1" y2="576.1" stroke="var(--up)" class="wick"/>
<rect x="733.89" y="547.9" width="2.44" height="25.8" fill="var(--up)"/>
<line x1="739.0" y1="529.7" x2="739.0" y2="569.9" stroke="var(--down)" class="wick"/>
<rect x="737.83" y="529.8" width="2.44" height="26.8" fill="var(--down)"/>
<line x1="743.0" y1="528.8" x2="743.0" y2="564.8" stroke="var(--down)" class="wick"/>
<rect x="741.76" y="552.9" width="2.44" height="11.1" fill="var(--down)"/>
<line x1="746.9" y1="432.4" x2="746.9" y2="527.3" stroke="var(--down)" class="wick"/>
<rect x="745.70" y="454.2" width="2.44" height="44.8" fill="var(--down)"/>
<line x1="750.9" y1="398.9" x2="750.9" y2="451.3" stroke="var(--up)" class="wick"/>
<rect x="749.64" y="433.3" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="754.8" y1="388.2" x2="754.8" y2="429.6" stroke="var(--up)" class="wick"/>
<rect x="753.57" y="419.9" width="2.44" height="3.4" fill="var(--up)"/>
<line x1="758.7" y1="406.9" x2="758.7" y2="471.3" stroke="var(--down)" class="wick"/>
<rect x="757.51" y="418.7" width="2.44" height="43.2" fill="var(--down)"/>
<line x1="762.7" y1="444.0" x2="762.7" y2="498.1" stroke="var(--down)" class="wick"/>
<rect x="761.45" y="456.2" width="2.44" height="31.3" fill="var(--down)"/>
<line x1="766.6" y1="476.4" x2="766.6" y2="517.9" stroke="var(--down)" class="wick"/>
<rect x="765.38" y="489.8" width="2.44" height="9.4" fill="var(--down)"/>
<line x1="770.5" y1="478.5" x2="770.5" y2="535.7" stroke="var(--up)" class="wick"/>
<rect x="769.32" y="483.3" width="2.44" height="29.4" fill="var(--up)"/>
<line x1="774.5" y1="469.8" x2="774.5" y2="531.3" stroke="var(--down)" class="wick"/>
<rect x="773.26" y="478.2" width="2.44" height="40.3" fill="var(--down)"/>
<line x1="778.4" y1="519.7" x2="778.4" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="777.19" y="524.9" width="2.44" height="40.2" fill="var(--down)"/>
<line x1="782.3" y1="499.3" x2="782.3" y2="571.3" stroke="var(--up)" class="wick"/>
<rect x="781.13" y="513.0" width="2.44" height="53.4" fill="var(--up)"/>
<line x1="786.3" y1="486.7" x2="786.3" y2="520.4" stroke="var(--down)" class="wick"/>
<rect x="785.07" y="514.7" width="2.44" height="3.4" fill="var(--down)"/>
<line x1="790.2" y1="475.6" x2="790.2" y2="532.8" stroke="var(--up)" class="wick"/>
<rect x="789.00" y="488.4" width="2.44" height="23.1" fill="var(--up)"/>
<line x1="794.2" y1="453.1" x2="794.2" y2="508.9" stroke="var(--up)" class="wick"/>
<rect x="792.94" y="470.9" width="2.44" height="33.7" fill="var(--up)"/>
<line x1="798.1" y1="452.3" x2="798.1" y2="474.0" stroke="var(--down)" class="wick"/>
<rect x="796.87" y="463.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="802.0" y1="432.4" x2="802.0" y2="467.8" stroke="var(--down)" class="wick"/>
<rect x="800.81" y="444.4" width="2.44" height="1.0" fill="var(--down)"/>
<line x1="806.0" y1="409.2" x2="806.0" y2="448.5" stroke="var(--up)" class="wick"/>
<rect x="804.75" y="421.6" width="2.44" height="20.0" fill="var(--up)"/>
<line x1="809.9" y1="360.3" x2="809.9" y2="420.0" stroke="var(--up)" class="wick"/>
<rect x="808.68" y="383.9" width="2.44" height="36.0" fill="var(--up)"/>
<line x1="813.8" y1="352.7" x2="813.8" y2="415.9" stroke="var(--down)" class="wick"/>
<rect x="812.62" y="383.5" width="2.44" height="10.9" fill="var(--down)"/>
<line x1="817.8" y1="399.2" x2="817.8" y2="434.7" stroke="var(--down)" class="wick"/>
<rect x="816.56" y="416.9" width="2.44" height="8.5" fill="var(--down)"/>
<line x1="821.7" y1="406.4" x2="821.7" y2="447.2" stroke="var(--up)" class="wick"/>
<rect x="820.49" y="412.1" width="2.44" height="35.1" fill="var(--up)"/>
<line x1="825.7" y1="419.3" x2="825.7" y2="482.5" stroke="var(--down)" class="wick"/>
<rect x="824.43" y="429.5" width="2.44" height="37.8" fill="var(--down)"/>
<line x1="829.6" y1="424.1" x2="829.6" y2="448.2" stroke="var(--down)" class="wick"/>
<rect x="828.37" y="433.7" width="2.44" height="7.9" fill="var(--down)"/>
<line x1="833.5" y1="419.5" x2="833.5" y2="454.2" stroke="var(--up)" class="wick"/>
<rect x="832.30" y="425.0" width="2.44" height="7.3" fill="var(--up)"/>
<line x1="837.5" y1="417.0" x2="837.5" y2="480.2" stroke="var(--down)" class="wick"/>
<rect x="836.24" y="425.2" width="2.44" height="50.5" fill="var(--down)"/>
<line x1="841.4" y1="394.7" x2="841.4" y2="463.7" stroke="var(--up)" class="wick"/>
<rect x="840.18" y="396.1" width="2.44" height="66.7" fill="var(--up)"/>
<line x1="845.3" y1="384.2" x2="845.3" y2="473.4" stroke="var(--down)" class="wick"/>
<rect x="844.11" y="385.1" width="2.44" height="81.1" fill="var(--down)"/>
<line x1="849.3" y1="392.7" x2="849.3" y2="477.6" stroke="var(--up)" class="wick"/>
<rect x="848.05" y="395.5" width="2.44" height="74.5" fill="var(--up)"/>
<line x1="853.2" y1="383.3" x2="853.2" y2="437.0" stroke="var(--down)" class="wick"/>
<rect x="851.99" y="390.3" width="2.44" height="7.7" fill="var(--down)"/>
<line x1="857.1" y1="347.8" x2="857.1" y2="382.5" stroke="var(--up)" class="wick"/>
<rect x="855.92" y="364.7" width="2.44" height="6.2" fill="var(--up)"/>
<line x1="861.1" y1="312.1" x2="861.1" y2="363.6" stroke="var(--up)" class="wick"/>
<rect x="859.86" y="327.4" width="2.44" height="22.9" fill="var(--up)"/>
<line x1="865.0" y1="280.4" x2="865.0" y2="352.8" stroke="var(--up)" class="wick"/>
<rect x="863.80" y="303.1" width="2.44" height="38.9" fill="var(--up)"/>
<line x1="869.0" y1="271.0" x2="869.0" y2="321.7" stroke="var(--down)" class="wick"/>
<rect x="867.73" y="282.2" width="2.44" height="2.9" fill="var(--down)"/>
<line x1="872.9" y1="296.5" x2="872.9" y2="357.5" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="298.1" width="2.44" height="37.6" fill="var(--down)"/>
<line x1="876.8" y1="316.3" x2="876.8" y2="359.4" stroke="var(--up)" class="wick"/>
<rect x="875.61" y="332.9" width="2.44" height="9.1" fill="var(--up)"/>
<line x1="880.8" y1="277.6" x2="880.8" y2="345.5" stroke="var(--up)" class="wick"/>
<rect x="879.54" y="293.9" width="2.44" height="44.1" fill="var(--up)"/>
<line x1="884.7" y1="232.8" x2="884.7" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="883.48" y="278.4" width="2.44" height="7.1" fill="var(--up)"/>
<line x1="888.6" y1="280.5" x2="888.6" y2="307.3" stroke="var(--down)" class="wick"/>
<rect x="887.41" y="285.6" width="2.44" height="5.4" fill="var(--down)"/>
<line x1="892.6" y1="261.5" x2="892.6" y2="305.5" stroke="var(--up)" class="wick"/>
<rect x="891.35" y="292.7" width="2.44" height="7.3" fill="var(--up)"/>
<line x1="896.5" y1="272.8" x2="896.5" y2="315.1" stroke="var(--up)" class="wick"/>
<rect x="895.29" y="279.3" width="2.44" height="2.9" fill="var(--up)"/>
<line x1="900.4" y1="258.9" x2="900.4" y2="321.9" stroke="var(--down)" class="wick"/>
<rect x="899.22" y="265.8" width="2.44" height="49.1" fill="var(--down)"/>
<line x1="904.4" y1="250.0" x2="904.4" y2="300.6" stroke="var(--up)" class="wick"/>
<rect x="903.16" y="253.6" width="2.44" height="37.7" fill="var(--up)"/>
<line x1="908.3" y1="235.6" x2="908.3" y2="274.8" stroke="var(--down)" class="wick"/>
<rect x="907.10" y="235.6" width="2.44" height="21.7" fill="var(--down)"/>
<line x1="912.3" y1="237.9" x2="912.3" y2="294.2" stroke="var(--down)" class="wick"/>
<rect x="911.03" y="246.6" width="2.44" height="36.4" fill="var(--down)"/>
<line x1="916.2" y1="299.8" x2="916.2" y2="348.0" stroke="var(--down)" class="wick"/>
<rect x="914.97" y="312.3" width="2.44" height="22.6" fill="var(--down)"/>
<line x1="920.1" y1="322.5" x2="920.1" y2="345.9" stroke="var(--down)" class="wick"/>
<rect x="918.91" y="332.8" width="2.44" height="3.2" fill="var(--down)"/>
<line x1="924.1" y1="331.3" x2="924.1" y2="359.7" stroke="var(--up)" class="wick"/>
<rect x="922.84" y="342.8" width="2.44" height="4.0" fill="var(--up)"/>
<line x1="928.0" y1="359.2" x2="928.0" y2="465.6" stroke="var(--down)" class="wick"/>
<rect x="926.78" y="364.2" width="2.44" height="66.6" fill="var(--down)"/>
<line x1="931.9" y1="416.5" x2="931.9" y2="461.8" stroke="var(--down)" class="wick"/>
<rect x="930.72" y="440.7" width="2.44" height="20.8" fill="var(--down)"/>
<line x1="935.9" y1="431.8" x2="935.9" y2="493.3" stroke="var(--up)" class="wick"/>
<rect x="934.65" y="435.2" width="2.44" height="48.3" fill="var(--up)"/>
<line x1="939.8" y1="422.4" x2="939.8" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="938.59" y="436.9" width="2.44" height="8.5" fill="var(--up)"/>
<line x1="943.7" y1="401.7" x2="943.7" y2="470.8" stroke="var(--down)" class="wick"/>
<rect x="942.53" y="445.3" width="2.44" height="17.6" fill="var(--down)"/>
<line x1="947.7" y1="443.2" x2="947.7" y2="479.9" stroke="var(--down)" class="wick"/>
<rect x="946.46" y="451.7" width="2.44" height="26.4" fill="var(--down)"/>
<line x1="951.6" y1="465.2" x2="951.6" y2="489.0" stroke="var(--up)" class="wick"/>
<rect x="950.40" y="476.9" width="2.44" height="3.5" fill="var(--up)"/>
<line x1="955.6" y1="462.8" x2="955.6" y2="497.8" stroke="var(--down)" class="wick"/>
<rect x="954.34" y="470.2" width="2.44" height="23.6" fill="var(--down)"/>
<line x1="959.5" y1="442.1" x2="959.5" y2="478.8" stroke="var(--up)" class="wick"/>
<rect x="958.27" y="463.9" width="2.44" height="12.2" fill="var(--up)"/>
<line x1="963.4" y1="398.5" x2="963.4" y2="458.7" stroke="var(--up)" class="wick"/>
<rect x="962.21" y="428.1" width="2.44" height="30.5" fill="var(--up)"/>
<line x1="967.4" y1="342.0" x2="967.4" y2="411.0" stroke="var(--up)" class="wick"/>
<rect x="966.14" y="350.7" width="2.44" height="55.1" fill="var(--up)"/>
<line x1="971.3" y1="301.7" x2="971.3" y2="346.6" stroke="var(--up)" class="wick"/>
<rect x="970.08" y="316.8" width="2.44" height="17.5" fill="var(--up)"/>
<line x1="975.2" y1="331.6" x2="975.2" y2="389.8" stroke="var(--down)" class="wick"/>
<rect x="974.02" y="331.6" width="2.44" height="52.9" fill="var(--down)"/>
<line x1="979.2" y1="383.9" x2="979.2" y2="427.9" stroke="var(--down)" class="wick"/>
<rect x="977.95" y="384.6" width="2.44" height="22.9" fill="var(--down)"/>
<line x1="983.1" y1="383.8" x2="983.1" y2="421.6" stroke="var(--up)" class="wick"/>
<rect x="981.89" y="400.5" width="2.44" height="7.2" fill="var(--up)"/>
<line x1="987.0" y1="342.6" x2="987.0" y2="391.7" stroke="var(--up)" class="wick"/>
<rect x="985.83" y="351.8" width="2.44" height="8.3" fill="var(--up)"/>
<line x1="991.0" y1="236.7" x2="991.0" y2="433.7" stroke="var(--down)" class="wick"/>
<rect x="989.76" y="242.5" width="2.44" height="125.8" fill="var(--down)"/>
<line x1="994.9" y1="373.8" x2="994.9" y2="432.0" stroke="var(--down)" class="wick"/>
<rect x="993.70" y="373.8" width="2.44" height="26.2" fill="var(--down)"/>
<line x1="998.9" y1="360.3" x2="998.9" y2="406.2" stroke="var(--down)" class="wick"/>
<rect x="997.64" y="385.4" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="1002.8" y1="371.3" x2="1002.8" y2="453.6" stroke="var(--down)" class="wick"/>
<rect x="1001.57" y="371.5" width="2.44" height="74.5" fill="var(--down)"/>
<line x1="1006.7" y1="430.8" x2="1006.7" y2="466.4" stroke="var(--down)" class="wick"/>
<rect x="1005.51" y="438.6" width="2.44" height="10.2" fill="var(--down)"/>
<line x1="1010.7" y1="406.5" x2="1010.7" y2="452.5" stroke="var(--up)" class="wick"/>
<rect x="1009.45" y="419.8" width="2.44" height="26.6" fill="var(--up)"/>
<line x1="1014.6" y1="405.7" x2="1014.6" y2="432.3" stroke="var(--down)" class="wick"/>
<rect x="1013.38" y="415.7" width="2.44" height="14.4" fill="var(--down)"/>
<line x1="1018.5" y1="408.3" x2="1018.5" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="1017.32" y="413.1" width="2.44" height="6.7" fill="var(--up)"/>
<line x1="1022.5" y1="382.8" x2="1022.5" y2="425.5" stroke="var(--down)" class="wick"/>
<rect x="1021.26" y="393.5" width="2.44" height="3.1" fill="var(--down)"/>
<line x1="1026.4" y1="396.3" x2="1026.4" y2="435.0" stroke="var(--down)" class="wick"/>
<rect x="1025.19" y="396.4" width="2.44" height="30.0" fill="var(--down)"/>
<line x1="1030.3" y1="418.0" x2="1030.3" y2="446.1" stroke="var(--down)" class="wick"/>
<rect x="1029.13" y="425.8" width="2.44" height="6.9" fill="var(--down)"/>
<line x1="1034.3" y1="422.7" x2="1034.3" y2="453.7" stroke="var(--down)" class="wick"/>
<rect x="1033.07" y="430.8" width="2.44" height="18.9" fill="var(--down)"/>
<line x1="1038.2" y1="452.3" x2="1038.2" y2="516.8" stroke="var(--down)" class="wick"/>
<rect x="1037.00" y="454.8" width="2.44" height="61.2" fill="var(--down)"/>
<line x1="1042.2" y1="475.8" x2="1042.2" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="1040.94" y="484.9" width="2.44" height="19.2" fill="var(--up)"/>
<line x1="1046.1" y1="479.7" x2="1046.1" y2="504.4" stroke="var(--down)" class="wick"/>
<rect x="1044.87" y="485.6" width="2.44" height="1.2" fill="var(--down)"/>
<line x1="1050.0" y1="466.1" x2="1050.0" y2="510.6" stroke="var(--down)" class="wick"/>
<rect x="1048.81" y="467.8" width="2.44" height="40.3" fill="var(--down)"/>
<line x1="60" y1="355.1" x2="1052" y2="355.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="358.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,283 R1</text>
<text x="1058" y="370.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="247.7" x2="1052" y2="247.7" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="251.2" font-size="11.5" fill="var(--resistance)" font-weight="600">$1,352 R2</text>
<text x="1058" y="263.2" font-size="9.5" fill="var(--muted)">터치 10회</text>
<line x1="60" y1="592.0" x2="1052" y2="592.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="586.0" font-size="11.5" fill="var(--support)" font-weight="600">$1,132 S1</text>
<text x="1058" y="598.0" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="508.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="500.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $1,186 (2026-08-25)</text>
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

각 레벨은 "전후 5거래일 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $1,352 | 10 | 2025-09-10·10-01·10-27·11-18·12-04, 2026-02-20·03-03·06-25·07-06·08-04. **1년 내내 반복해서 되돌려진 가장 두꺼운 스윙 고점대**이며, 2026-08-04 실적 발표 당일에도 이 대역에서 되밀렸다 |
| R1 | $1,283 | 3 | 2026-04-14·05-07·05-29. 4~5월 반등 국면의 고점대 |
| **현재가** | **$1,199.08** (2026-08-24 종가) | — | R1과 S1 사이 |
| S1 | $1,132 | 3 | 2026-04-01·04-29·05-15. **현재가에 가장 근접한 지지대**이자 최근 1년 최저(1,123.61)와 맞닿아 있다 |
| 참고선 | $1,463 | — | 최근 1년 최고(2025-08~09 국면). 아래 3. 관측된 특이 구간의 특별배당 이전 가격대라 **현재 레짐과 단절**돼 있어 근시일 저항으로 보지 않는다 |

> 유효한 클러스터가 저항 2개·지지 1개뿐이라 스크립트 기본값(각 3개)을 채우지 않고 그대로 뒀다. 특히 **현재가 아래에는 S1 하나밖에 없다** — 1년 내 저점권에 근접해 있어 아래쪽 표본 자체가 적기 때문이며, S1이 무너질 경우 참고할 다음 클러스터가 이 창 안에는 없다.

---

## 3. 관측된 특이 구간 — 2025-09-12 주당 $90.00 특별배당 지급

- 2025-08-20 이사회가 주당 $90.00 특별배당을 선언하고 2025-09-12에 지급했다([최근 뉴스 / 이슈](./08_news.md) 로그 참고). 재원은 하루 앞선 2025-08-19에 조달한 **$50억 신규 부채**였다.
- **이 차트는 원주가(배당 미조정) 기준이라, 배당락일에 주가가 배당액만큼 계단식으로 내려온 것이 그대로 그려져 있다.** 즉 이 구간의 하락은 기업가치 훼손이 아니라 현금이 주주에게 이전된 결과이며, **총주주수익률과 차트상의 가격 흐름이 이 지점에서 갈라진다.**
- 그 결과 **배당 이전 가격대(최근 1년 최고 $1,463)와 이후 가격대는 같은 잣대로 비교할 수 없다.** 위 2. 지지선 / 저항선 요약에서 $1,463을 저항이 아니라 참고선으로만 처리한 이유가 이것이다.
- 나머지 두 이벤트선은 참고용이다 — 2026-04-07 Jet Parts Engineering·Victor Sierra 인수 완료($2.2B), 2026-08-04 FY2026 3분기 실적·가이던스 상향. **두 이벤트 모두 배당락 같은 가격 단절을 만들지는 않았다.**

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 일봉 OHLCV(Open/High/Low/Close/Volume), 252개 거래일, 2025-08-25~2026-08-25. 수집 시점: 2026-08-26. 원주가(과거 분할은 소급 반영, 배당은 미반영).
- **스윙 포인트 탐지**: 각 거래일의 고가/저가가 전후 5거래일(총 11거래일 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py TDG --name "TransDigm Group" --event 2025-09-12:"주당 $90 특별배당 지급" --event 2026-04-07:"JPE·Victor Sierra 인수" --event 2026-08-04:"FY26 Q3 실적·가이던스 상향" --ref-line 1463.03:"52주 최고" --close-on 2026-08-24 --emit all`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(5거래일)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 252개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - **가격 연속성이 깨진 구간이 있다** — 2025-09-12 주당 $90.00 특별배당(3. 관측된 특이 구간). 원주가 기준이라 소급 조정하지 않았고, 그 결과 배당 전후 스윙 레벨을 같은 잣대로 묶을 수 없다. 이 회사는 특별배당을 부정기적으로 반복하므로 **이 한계는 앞으로도 재발한다.**
    - **마지막 봉(2026-08-25)은 미확정 세션**이다(거래량 71,128주 vs 1년 평균 367,839주). 그 봉의 고가·저가가 스윙 탐지에 들어갔을 수 있으나, 전후 5거래일 창을 채우지 못해 스윙 포인트로 분류되지는 않는다.
    - 주식분할·대규모 유상증자 등 주식수 자체를 바꾸는 이벤트는 이 기간에 없었다.

---

*작성일: 2026-08-26*
