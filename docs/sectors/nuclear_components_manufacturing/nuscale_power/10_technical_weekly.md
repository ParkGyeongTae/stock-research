# 기술적 분석 (주봉 캔들차트 · 다년 구조)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. 최근 1년 세부 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)(일봉·1년)를 참고. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 핵심 지표의 원자료 표와는 별도로 수집됐다(5년 주봉은 핵심 지표가 다루는 범위 밖). **2026-08-18 종가 $8.64는 핵심 지표 A.2·밸류에이션 / 적정주가 6. 목표주가 요약에 인용된 값과 일치한다.**
>
> ⚠️ **데이터 시작 시점(2022-02-28)이 2022-05-02 SPAC 합병(NuScale 상장일)보다 앞선다** — 이는 Yahoo Finance가 SMR 티커 이력을 스팩 셸(Spring Valley Acquisition Corp) 상장 시점부터 이어 붙이기 때문이다. 2022년 2월~5월 구간의 가격은 NuScale 사업 자체가 아니라 스팩 셸의 신탁계좌 가치(대략 $10 내외)를 반영한 것이므로, 이 구간의 캔들을 NuScale 펀더멘털과 연결해 해석하지 말 것.

---

## 1. 차트 — 최근 5년 주봉 (2022-02-28 ~ 2026-08-18)

<div class="smr-chart">
<style>
.smr-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .smr-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .smr-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.smr-chart svg { width:100%; height:auto; display:block; }
.smr-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.smr-chart .title { fill: var(--ink); font-weight:600; }
.smr-chart .grid { stroke: var(--grid); stroke-width:1; }
.smr-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="NuScale Power(SMR) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">NuScale Power (SMR) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2022-02-28 ~ 2026-08-18 · 마지막 종가 $8.64 (2026-08-18) · 단위 USD</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="grid"/>
<text x="52" y="630.0" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="531.0" x2="1052" y2="531.0" class="grid"/>
<text x="52" y="535.0" font-size="11" text-anchor="end" fill="var(--muted)">10.00</text>
<line x1="60" y1="436.0" x2="1052" y2="436.0" class="grid"/>
<text x="52" y="440.0" font-size="11" text-anchor="end" fill="var(--muted)">20</text>
<line x1="60" y1="341.0" x2="1052" y2="341.0" class="grid"/>
<text x="52" y="345.0" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="246.0" x2="1052" y2="246.0" class="grid"/>
<text x="52" y="250.0" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="151.0" x2="1052" y2="151.0" class="grid"/>
<text x="52" y="155.0" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="56.0" x2="1052" y2="56.0" class="grid"/>
<text x="52" y="60.0" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="62.1" y1="626.0" x2="62.1" y2="631.0" class="axis"/>
<text x="62.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="247.8" y1="626.0" x2="247.8" y2="631.0" class="axis"/>
<text x="247.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="467.4" y1="626.0" x2="467.4" y2="631.0" class="axis"/>
<text x="467.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="691.1" y1="626.0" x2="691.1" y2="631.0" class="axis"/>
<text x="691.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="910.6" y1="626.0" x2="910.6" y2="631.0" class="axis"/>
<text x="910.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="62.1" y1="529.9" x2="62.1" y2="530.6" stroke="var(--down)" class="wick"/>
<rect x="60.80" y="530.5" width="2.62" height="1.0" fill="var(--down)"/>
<line x1="66.3" y1="528.6" x2="66.3" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="65.02" y="528.9" width="2.62" height="1.3" fill="var(--up)"/>
<line x1="70.6" y1="528.7" x2="70.6" y2="530.5" stroke="var(--down)" class="wick"/>
<rect x="69.24" y="528.8" width="2.62" height="1.0" fill="var(--down)"/>
<line x1="74.8" y1="528.4" x2="74.8" y2="530.0" stroke="var(--up)" class="wick"/>
<rect x="73.47" y="529.5" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="79.0" y1="522.4" x2="79.0" y2="529.9" stroke="var(--up)" class="wick"/>
<rect x="77.69" y="525.5" width="2.62" height="3.3" fill="var(--up)"/>
<line x1="83.2" y1="522.5" x2="83.2" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="81.91" y="524.1" width="2.62" height="1.4" fill="var(--up)"/>
<line x1="87.4" y1="519.3" x2="87.4" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="86.13" y="521.7" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="91.7" y1="519.9" x2="91.7" y2="530.3" stroke="var(--down)" class="wick"/>
<rect x="90.35" y="520.7" width="2.62" height="9.4" fill="var(--down)"/>
<line x1="95.9" y1="527.6" x2="95.9" y2="537.2" stroke="var(--down)" class="wick"/>
<rect x="94.57" y="532.0" width="2.62" height="3.3" fill="var(--down)"/>
<line x1="100.1" y1="524.0" x2="100.1" y2="536.7" stroke="var(--up)" class="wick"/>
<rect x="98.79" y="525.2" width="2.62" height="8.9" fill="var(--up)"/>
<line x1="104.3" y1="523.4" x2="104.3" y2="537.6" stroke="var(--down)" class="wick"/>
<rect x="103.01" y="525.4" width="2.62" height="9.2" fill="var(--down)"/>
<line x1="108.5" y1="528.7" x2="108.5" y2="537.6" stroke="var(--up)" class="wick"/>
<rect x="107.24" y="532.0" width="2.62" height="1.9" fill="var(--up)"/>
<line x1="112.8" y1="530.3" x2="112.8" y2="541.7" stroke="var(--down)" class="wick"/>
<rect x="111.46" y="530.3" width="2.62" height="1.6" fill="var(--down)"/>
<line x1="117.0" y1="529.8" x2="117.0" y2="538.3" stroke="var(--down)" class="wick"/>
<rect x="115.68" y="530.5" width="2.62" height="5.8" fill="var(--down)"/>
<line x1="121.2" y1="525.0" x2="121.2" y2="534.4" stroke="var(--up)" class="wick"/>
<rect x="119.90" y="531.1" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="125.4" y1="527.1" x2="125.4" y2="538.6" stroke="var(--up)" class="wick"/>
<rect x="124.12" y="528.0" width="2.62" height="6.9" fill="var(--up)"/>
<line x1="129.7" y1="523.4" x2="129.7" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="128.34" y="526.4" width="2.62" height="2.1" fill="var(--down)"/>
<line x1="133.9" y1="521.9" x2="133.9" y2="536.2" stroke="var(--down)" class="wick"/>
<rect x="132.56" y="523.6" width="2.62" height="1.2" fill="var(--down)"/>
<line x1="138.1" y1="522.1" x2="138.1" y2="529.2" stroke="var(--down)" class="wick"/>
<rect x="136.79" y="527.6" width="2.62" height="1.5" fill="var(--down)"/>
<line x1="142.3" y1="525.6" x2="142.3" y2="533.4" stroke="var(--down)" class="wick"/>
<rect x="141.01" y="528.1" width="2.62" height="1.0" fill="var(--down)"/>
<line x1="146.5" y1="499.4" x2="146.5" y2="528.4" stroke="var(--up)" class="wick"/>
<rect x="145.23" y="505.7" width="2.62" height="21.6" fill="var(--up)"/>
<line x1="150.8" y1="488.2" x2="150.8" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="149.45" y="489.8" width="2.62" height="13.6" fill="var(--up)"/>
<line x1="155.0" y1="475.4" x2="155.0" y2="490.1" stroke="var(--down)" class="wick"/>
<rect x="153.67" y="477.5" width="2.62" height="9.6" fill="var(--down)"/>
<line x1="159.2" y1="477.6" x2="159.2" y2="495.9" stroke="var(--down)" class="wick"/>
<rect x="157.89" y="482.5" width="2.62" height="2.2" fill="var(--down)"/>
<line x1="163.4" y1="483.5" x2="163.4" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="162.11" y="485.4" width="2.62" height="7.1" fill="var(--down)"/>
<line x1="167.6" y1="475.7" x2="167.6" y2="496.6" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="494.3" width="2.62" height="1.0" fill="var(--down)"/>
<line x1="171.9" y1="485.4" x2="171.9" y2="507.2" stroke="var(--down)" class="wick"/>
<rect x="170.56" y="495.9" width="2.62" height="1.0" fill="var(--down)"/>
<line x1="176.1" y1="486.4" x2="176.1" y2="496.8" stroke="var(--up)" class="wick"/>
<rect x="174.78" y="493.9" width="2.62" height="2.1" fill="var(--up)"/>
<line x1="180.3" y1="488.2" x2="180.3" y2="498.1" stroke="var(--down)" class="wick"/>
<rect x="179.00" y="492.3" width="2.62" height="1.3" fill="var(--down)"/>
<line x1="184.5" y1="494.1" x2="184.5" y2="507.2" stroke="var(--down)" class="wick"/>
<rect x="183.22" y="495.3" width="2.62" height="11.3" fill="var(--down)"/>
<line x1="188.7" y1="505.9" x2="188.7" y2="519.4" stroke="var(--down)" class="wick"/>
<rect x="187.44" y="507.9" width="2.62" height="7.1" fill="var(--down)"/>
<line x1="193.0" y1="508.2" x2="193.0" y2="519.0" stroke="var(--down)" class="wick"/>
<rect x="191.66" y="514.1" width="2.62" height="3.2" fill="var(--down)"/>
<line x1="197.2" y1="516.1" x2="197.2" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="195.88" y="516.8" width="2.62" height="4.4" fill="var(--down)"/>
<line x1="201.4" y1="509.9" x2="201.4" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="200.10" y="511.0" width="2.62" height="8.2" fill="var(--up)"/>
<line x1="205.6" y1="508.6" x2="205.6" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="204.33" y="511.6" width="2.62" height="5.3" fill="var(--down)"/>
<line x1="209.9" y1="514.1" x2="209.9" y2="521.9" stroke="var(--up)" class="wick"/>
<rect x="208.55" y="515.3" width="2.62" height="1.4" fill="var(--up)"/>
<line x1="214.1" y1="511.7" x2="214.1" y2="517.9" stroke="var(--down)" class="wick"/>
<rect x="212.77" y="514.6" width="2.62" height="1.0" fill="var(--down)"/>
<line x1="218.3" y1="510.7" x2="218.3" y2="524.4" stroke="var(--down)" class="wick"/>
<rect x="216.99" y="514.9" width="2.62" height="5.5" fill="var(--down)"/>
<line x1="222.5" y1="517.6" x2="222.5" y2="525.6" stroke="var(--up)" class="wick"/>
<rect x="221.21" y="519.4" width="2.62" height="1.5" fill="var(--up)"/>
<line x1="226.7" y1="517.7" x2="226.7" y2="524.5" stroke="var(--up)" class="wick"/>
<rect x="225.43" y="520.2" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="231.0" y1="520.0" x2="231.0" y2="524.7" stroke="var(--down)" class="wick"/>
<rect x="229.65" y="520.1" width="2.62" height="3.5" fill="var(--down)"/>
<line x1="235.2" y1="519.2" x2="235.2" y2="534.8" stroke="var(--down)" class="wick"/>
<rect x="233.87" y="523.1" width="2.62" height="10.6" fill="var(--down)"/>
<line x1="239.4" y1="526.3" x2="239.4" y2="534.3" stroke="var(--up)" class="wick"/>
<rect x="238.10" y="530.0" width="2.62" height="3.4" fill="var(--up)"/>
<line x1="243.6" y1="526.0" x2="243.6" y2="532.6" stroke="var(--up)" class="wick"/>
<rect x="242.32" y="528.5" width="2.62" height="1.9" fill="var(--up)"/>
<line x1="247.8" y1="525.2" x2="247.8" y2="530.8" stroke="var(--up)" class="wick"/>
<rect x="246.54" y="528.4" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="252.1" y1="519.7" x2="252.1" y2="528.2" stroke="var(--up)" class="wick"/>
<rect x="250.76" y="522.5" width="2.62" height="4.5" fill="var(--up)"/>
<line x1="256.3" y1="519.7" x2="256.3" y2="528.4" stroke="var(--down)" class="wick"/>
<rect x="254.98" y="521.5" width="2.62" height="6.7" fill="var(--down)"/>
<line x1="260.5" y1="518.5" x2="260.5" y2="528.9" stroke="var(--up)" class="wick"/>
<rect x="259.20" y="521.0" width="2.62" height="4.1" fill="var(--up)"/>
<line x1="264.7" y1="519.7" x2="264.7" y2="526.5" stroke="var(--down)" class="wick"/>
<rect x="263.42" y="521.0" width="2.62" height="3.7" fill="var(--down)"/>
<line x1="269.0" y1="522.6" x2="269.0" y2="529.5" stroke="var(--up)" class="wick"/>
<rect x="267.64" y="524.4" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="273.2" y1="523.6" x2="273.2" y2="528.6" stroke="var(--down)" class="wick"/>
<rect x="271.87" y="523.6" width="2.62" height="2.3" fill="var(--down)"/>
<line x1="277.4" y1="526.2" x2="277.4" y2="530.9" stroke="var(--down)" class="wick"/>
<rect x="276.09" y="526.2" width="2.62" height="3.7" fill="var(--down)"/>
<line x1="281.6" y1="526.5" x2="281.6" y2="532.4" stroke="var(--up)" class="wick"/>
<rect x="280.31" y="528.1" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="285.8" y1="527.2" x2="285.8" y2="536.9" stroke="var(--down)" class="wick"/>
<rect x="284.53" y="528.1" width="2.62" height="8.2" fill="var(--down)"/>
<line x1="290.1" y1="532.5" x2="290.1" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="288.75" y="537.7" width="2.62" height="5.0" fill="var(--down)"/>
<line x1="294.3" y1="540.9" x2="294.3" y2="548.0" stroke="var(--down)" class="wick"/>
<rect x="292.97" y="542.8" width="2.62" height="4.0" fill="var(--down)"/>
<line x1="298.5" y1="539.1" x2="298.5" y2="549.1" stroke="var(--up)" class="wick"/>
<rect x="297.19" y="539.6" width="2.62" height="6.6" fill="var(--up)"/>
<line x1="302.7" y1="537.9" x2="302.7" y2="547.7" stroke="var(--down)" class="wick"/>
<rect x="301.41" y="539.0" width="2.62" height="8.5" fill="var(--down)"/>
<line x1="306.9" y1="539.6" x2="306.9" y2="548.2" stroke="var(--up)" class="wick"/>
<rect x="305.64" y="540.8" width="2.62" height="7.4" fill="var(--up)"/>
<line x1="311.2" y1="538.1" x2="311.2" y2="544.7" stroke="var(--down)" class="wick"/>
<rect x="309.86" y="540.4" width="2.62" height="2.8" fill="var(--down)"/>
<line x1="315.4" y1="540.5" x2="315.4" y2="546.7" stroke="var(--up)" class="wick"/>
<rect x="314.08" y="541.7" width="2.62" height="1.1" fill="var(--up)"/>
<line x1="319.6" y1="540.4" x2="319.6" y2="553.7" stroke="var(--down)" class="wick"/>
<rect x="318.30" y="540.5" width="2.62" height="8.9" fill="var(--down)"/>
<line x1="323.8" y1="545.2" x2="323.8" y2="553.8" stroke="var(--up)" class="wick"/>
<rect x="322.52" y="547.1" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="328.1" y1="545.3" x2="328.1" y2="553.1" stroke="var(--down)" class="wick"/>
<rect x="326.74" y="546.3" width="2.62" height="6.7" fill="var(--down)"/>
<line x1="332.3" y1="540.8" x2="332.3" y2="552.6" stroke="var(--down)" class="wick"/>
<rect x="330.96" y="549.9" width="2.62" height="2.1" fill="var(--down)"/>
<line x1="336.5" y1="551.5" x2="336.5" y2="557.0" stroke="var(--down)" class="wick"/>
<rect x="335.19" y="551.9" width="2.62" height="1.2" fill="var(--down)"/>
<line x1="340.7" y1="546.3" x2="340.7" y2="553.7" stroke="var(--up)" class="wick"/>
<rect x="339.41" y="551.1" width="2.62" height="1.3" fill="var(--up)"/>
<line x1="344.9" y1="543.3" x2="344.9" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="343.63" y="548.4" width="2.62" height="2.8" fill="var(--up)"/>
<line x1="349.2" y1="547.1" x2="349.2" y2="557.3" stroke="var(--down)" class="wick"/>
<rect x="347.85" y="548.4" width="2.62" height="8.6" fill="var(--down)"/>
<line x1="353.4" y1="556.5" x2="353.4" y2="565.1" stroke="var(--down)" class="wick"/>
<rect x="352.07" y="556.6" width="2.62" height="4.8" fill="var(--down)"/>
<line x1="357.6" y1="555.5" x2="357.6" y2="564.5" stroke="var(--up)" class="wick"/>
<rect x="356.29" y="557.0" width="2.62" height="3.8" fill="var(--up)"/>
<line x1="361.8" y1="549.5" x2="361.8" y2="557.0" stroke="var(--up)" class="wick"/>
<rect x="360.51" y="553.3" width="2.62" height="3.4" fill="var(--up)"/>
<line x1="366.0" y1="549.5" x2="366.0" y2="555.7" stroke="var(--down)" class="wick"/>
<rect x="364.73" y="553.4" width="2.62" height="1.9" fill="var(--down)"/>
<line x1="370.3" y1="552.6" x2="370.3" y2="561.4" stroke="var(--down)" class="wick"/>
<rect x="368.96" y="554.8" width="2.62" height="4.2" fill="var(--down)"/>
<line x1="374.5" y1="551.6" x2="374.5" y2="558.8" stroke="var(--up)" class="wick"/>
<rect x="373.18" y="555.8" width="2.62" height="2.3" fill="var(--up)"/>
<line x1="378.7" y1="550.6" x2="378.7" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="377.40" y="555.7" width="2.62" height="1.9" fill="var(--down)"/>
<line x1="382.9" y1="556.5" x2="382.9" y2="564.1" stroke="var(--down)" class="wick"/>
<rect x="381.62" y="558.6" width="2.62" height="4.1" fill="var(--down)"/>
<line x1="387.1" y1="560.5" x2="387.1" y2="571.4" stroke="var(--down)" class="wick"/>
<rect x="385.84" y="562.5" width="2.62" height="7.9" fill="var(--down)"/>
<line x1="391.4" y1="565.6" x2="391.4" y2="571.5" stroke="var(--up)" class="wick"/>
<rect x="390.06" y="566.5" width="2.62" height="3.1" fill="var(--up)"/>
<line x1="395.6" y1="565.7" x2="395.6" y2="571.9" stroke="var(--down)" class="wick"/>
<rect x="394.28" y="566.0" width="2.62" height="3.8" fill="var(--down)"/>
<line x1="399.8" y1="562.3" x2="399.8" y2="569.9" stroke="var(--up)" class="wick"/>
<rect x="398.50" y="569.0" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="404.0" y1="568.8" x2="404.0" y2="576.4" stroke="var(--down)" class="wick"/>
<rect x="402.73" y="568.8" width="2.62" height="7.4" fill="var(--down)"/>
<line x1="408.3" y1="574.6" x2="408.3" y2="579.6" stroke="var(--down)" class="wick"/>
<rect x="406.95" y="576.2" width="2.62" height="3.2" fill="var(--down)"/>
<line x1="412.5" y1="570.5" x2="412.5" y2="583.5" stroke="var(--up)" class="wick"/>
<rect x="411.17" y="571.4" width="2.62" height="8.1" fill="var(--up)"/>
<line x1="416.7" y1="570.3" x2="416.7" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="415.39" y="571.1" width="2.62" height="1.1" fill="var(--up)"/>
<line x1="420.9" y1="569.9" x2="420.9" y2="590.0" stroke="var(--down)" class="wick"/>
<rect x="419.61" y="570.9" width="2.62" height="19.0" fill="var(--down)"/>
<line x1="425.1" y1="589.2" x2="425.1" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="423.83" y="590.4" width="2.62" height="5.2" fill="var(--down)"/>
<line x1="429.4" y1="591.3" x2="429.4" y2="597.4" stroke="var(--up)" class="wick"/>
<rect x="428.05" y="593.2" width="2.62" height="1.7" fill="var(--up)"/>
<line x1="433.6" y1="592.4" x2="433.6" y2="608.8" stroke="var(--down)" class="wick"/>
<rect x="432.27" y="592.5" width="2.62" height="13.7" fill="var(--down)"/>
<line x1="437.8" y1="599.4" x2="437.8" y2="607.0" stroke="var(--up)" class="wick"/>
<rect x="436.50" y="602.2" width="2.62" height="4.1" fill="var(--up)"/>
<line x1="442.0" y1="598.7" x2="442.0" y2="603.2" stroke="var(--up)" class="wick"/>
<rect x="440.72" y="599.1" width="2.62" height="1.2" fill="var(--up)"/>
<line x1="446.2" y1="595.9" x2="446.2" y2="601.4" stroke="var(--up)" class="wick"/>
<rect x="444.94" y="597.1" width="2.62" height="1.7" fill="var(--up)"/>
<line x1="450.5" y1="592.9" x2="450.5" y2="597.7" stroke="var(--up)" class="wick"/>
<rect x="449.16" y="595.3" width="2.62" height="1.5" fill="var(--up)"/>
<line x1="454.7" y1="590.3" x2="454.7" y2="599.3" stroke="var(--up)" class="wick"/>
<rect x="453.38" y="592.4" width="2.62" height="2.8" fill="var(--up)"/>
<line x1="458.9" y1="591.2" x2="458.9" y2="595.8" stroke="var(--down)" class="wick"/>
<rect x="457.60" y="592.2" width="2.62" height="2.7" fill="var(--down)"/>
<line x1="463.1" y1="592.8" x2="463.1" y2="595.6" stroke="var(--up)" class="wick"/>
<rect x="461.82" y="594.7" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="467.4" y1="593.5" x2="467.4" y2="601.4" stroke="var(--down)" class="wick"/>
<rect x="466.04" y="595.2" width="2.62" height="5.9" fill="var(--down)"/>
<line x1="471.6" y1="600.6" x2="471.6" y2="603.9" stroke="var(--down)" class="wick"/>
<rect x="470.27" y="600.6" width="2.62" height="3.0" fill="var(--down)"/>
<line x1="475.8" y1="603.5" x2="475.8" y2="608.1" stroke="var(--down)" class="wick"/>
<rect x="474.49" y="603.7" width="2.62" height="3.4" fill="var(--down)"/>
<line x1="480.0" y1="599.6" x2="480.0" y2="606.9" stroke="var(--up)" class="wick"/>
<rect x="478.71" y="599.9" width="2.62" height="6.8" fill="var(--up)"/>
<line x1="484.2" y1="595.4" x2="484.2" y2="600.5" stroke="var(--up)" class="wick"/>
<rect x="482.93" y="596.1" width="2.62" height="3.1" fill="var(--up)"/>
<line x1="488.5" y1="596.3" x2="488.5" y2="602.7" stroke="var(--down)" class="wick"/>
<rect x="487.15" y="596.5" width="2.62" height="3.9" fill="var(--down)"/>
<line x1="492.7" y1="598.4" x2="492.7" y2="601.8" stroke="var(--up)" class="wick"/>
<rect x="491.37" y="600.4" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="496.9" y1="598.9" x2="496.9" y2="602.5" stroke="var(--down)" class="wick"/>
<rect x="495.59" y="599.9" width="2.62" height="1.4" fill="var(--down)"/>
<line x1="501.1" y1="592.5" x2="501.1" y2="601.7" stroke="var(--up)" class="wick"/>
<rect x="499.81" y="593.2" width="2.62" height="8.0" fill="var(--up)"/>
<line x1="505.3" y1="571.6" x2="505.3" y2="592.3" stroke="var(--up)" class="wick"/>
<rect x="504.04" y="573.8" width="2.62" height="13.2" fill="var(--up)"/>
<line x1="509.6" y1="548.5" x2="509.6" y2="575.6" stroke="var(--up)" class="wick"/>
<rect x="508.26" y="551.4" width="2.62" height="16.6" fill="var(--up)"/>
<line x1="513.8" y1="519.5" x2="513.8" y2="586.4" stroke="var(--down)" class="wick"/>
<rect x="512.48" y="543.5" width="2.62" height="42.1" fill="var(--down)"/>
<line x1="518.0" y1="570.9" x2="518.0" y2="590.0" stroke="var(--up)" class="wick"/>
<rect x="516.70" y="575.6" width="2.62" height="9.5" fill="var(--up)"/>
<line x1="522.2" y1="556.0" x2="522.2" y2="579.4" stroke="var(--up)" class="wick"/>
<rect x="520.92" y="568.1" width="2.62" height="2.8" fill="var(--up)"/>
<line x1="526.5" y1="561.4" x2="526.5" y2="577.2" stroke="var(--down)" class="wick"/>
<rect x="525.14" y="566.6" width="2.62" height="9.3" fill="var(--down)"/>
<line x1="530.7" y1="574.4" x2="530.7" y2="581.4" stroke="var(--down)" class="wick"/>
<rect x="529.36" y="575.6" width="2.62" height="4.4" fill="var(--down)"/>
<line x1="534.9" y1="565.5" x2="534.9" y2="582.2" stroke="var(--up)" class="wick"/>
<rect x="533.59" y="568.4" width="2.62" height="11.4" fill="var(--up)"/>
<line x1="539.1" y1="566.1" x2="539.1" y2="573.0" stroke="var(--up)" class="wick"/>
<rect x="537.81" y="567.5" width="2.62" height="1.2" fill="var(--up)"/>
<line x1="543.3" y1="561.6" x2="543.3" y2="573.8" stroke="var(--down)" class="wick"/>
<rect x="542.03" y="565.9" width="2.62" height="1.0" fill="var(--down)"/>
<line x1="547.6" y1="551.8" x2="547.6" y2="570.3" stroke="var(--down)" class="wick"/>
<rect x="546.25" y="564.6" width="2.62" height="1.4" fill="var(--down)"/>
<line x1="551.8" y1="551.4" x2="551.8" y2="565.5" stroke="var(--up)" class="wick"/>
<rect x="550.47" y="552.1" width="2.62" height="13.4" fill="var(--up)"/>
<line x1="556.0" y1="534.5" x2="556.0" y2="549.6" stroke="var(--down)" class="wick"/>
<rect x="554.69" y="542.3" width="2.62" height="1.0" fill="var(--down)"/>
<line x1="560.2" y1="536.3" x2="560.2" y2="563.2" stroke="var(--down)" class="wick"/>
<rect x="558.91" y="542.7" width="2.62" height="6.6" fill="var(--down)"/>
<line x1="564.4" y1="538.5" x2="564.4" y2="551.5" stroke="var(--up)" class="wick"/>
<rect x="563.13" y="548.2" width="2.62" height="2.1" fill="var(--up)"/>
<line x1="568.7" y1="525.3" x2="568.7" y2="549.4" stroke="var(--up)" class="wick"/>
<rect x="567.36" y="530.8" width="2.62" height="17.1" fill="var(--up)"/>
<line x1="572.9" y1="508.2" x2="572.9" y2="537.5" stroke="var(--up)" class="wick"/>
<rect x="571.58" y="514.9" width="2.62" height="16.1" fill="var(--up)"/>
<line x1="577.1" y1="499.8" x2="577.1" y2="526.9" stroke="var(--up)" class="wick"/>
<rect x="575.80" y="509.9" width="2.62" height="4.4" fill="var(--up)"/>
<line x1="581.3" y1="476.9" x2="581.3" y2="509.3" stroke="var(--up)" class="wick"/>
<rect x="580.02" y="480.3" width="2.62" height="23.6" fill="var(--up)"/>
<line x1="585.5" y1="465.4" x2="585.5" y2="519.4" stroke="var(--down)" class="wick"/>
<rect x="584.24" y="466.9" width="2.62" height="51.8" fill="var(--down)"/>
<line x1="589.8" y1="507.2" x2="589.8" y2="534.0" stroke="var(--down)" class="wick"/>
<rect x="588.46" y="516.6" width="2.62" height="6.4" fill="var(--down)"/>
<line x1="594.0" y1="519.9" x2="594.0" y2="550.0" stroke="var(--down)" class="wick"/>
<rect x="592.68" y="519.9" width="2.62" height="24.5" fill="var(--down)"/>
<line x1="598.2" y1="535.3" x2="598.2" y2="557.0" stroke="var(--up)" class="wick"/>
<rect x="596.90" y="537.9" width="2.62" height="18.5" fill="var(--up)"/>
<line x1="602.4" y1="528.4" x2="602.4" y2="542.2" stroke="var(--down)" class="wick"/>
<rect x="601.13" y="535.8" width="2.62" height="4.0" fill="var(--down)"/>
<line x1="606.7" y1="532.0" x2="606.7" y2="550.2" stroke="var(--down)" class="wick"/>
<rect x="605.35" y="539.5" width="2.62" height="4.1" fill="var(--down)"/>
<line x1="610.9" y1="542.5" x2="610.9" y2="551.2" stroke="var(--down)" class="wick"/>
<rect x="609.57" y="544.1" width="2.62" height="3.8" fill="var(--down)"/>
<line x1="615.1" y1="548.9" x2="615.1" y2="560.6" stroke="var(--down)" class="wick"/>
<rect x="613.79" y="549.3" width="2.62" height="10.4" fill="var(--down)"/>
<line x1="619.3" y1="530.4" x2="619.3" y2="559.3" stroke="var(--up)" class="wick"/>
<rect x="618.01" y="534.0" width="2.62" height="24.9" fill="var(--up)"/>
<line x1="623.5" y1="515.5" x2="623.5" y2="542.4" stroke="var(--up)" class="wick"/>
<rect x="622.23" y="524.4" width="2.62" height="9.3" fill="var(--up)"/>
<line x1="627.8" y1="501.5" x2="627.8" y2="527.2" stroke="var(--up)" class="wick"/>
<rect x="626.45" y="506.8" width="2.62" height="15.9" fill="var(--up)"/>
<line x1="632.0" y1="497.8" x2="632.0" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="630.67" y="501.1" width="2.62" height="8.5" fill="var(--up)"/>
<line x1="636.2" y1="497.4" x2="636.2" y2="519.0" stroke="var(--up)" class="wick"/>
<rect x="634.90" y="501.2" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="640.4" y1="432.7" x2="640.4" y2="500.6" stroke="var(--up)" class="wick"/>
<rect x="639.12" y="453.0" width="2.62" height="47.2" fill="var(--up)"/>
<line x1="644.6" y1="438.9" x2="644.6" y2="467.3" stroke="var(--down)" class="wick"/>
<rect x="643.34" y="447.7" width="2.62" height="3.4" fill="var(--down)"/>
<line x1="648.9" y1="409.9" x2="648.9" y2="448.4" stroke="var(--up)" class="wick"/>
<rect x="647.56" y="445.4" width="2.62" height="1.1" fill="var(--up)"/>
<line x1="653.1" y1="380.7" x2="653.1" y2="460.1" stroke="var(--up)" class="wick"/>
<rect x="651.78" y="393.3" width="2.62" height="59.2" fill="var(--up)"/>
<line x1="657.3" y1="364.4" x2="657.3" y2="423.7" stroke="var(--down)" class="wick"/>
<rect x="656.00" y="399.7" width="2.62" height="7.7" fill="var(--down)"/>
<line x1="661.5" y1="333.0" x2="661.5" y2="410.3" stroke="var(--up)" class="wick"/>
<rect x="660.22" y="339.0" width="2.62" height="61.4" fill="var(--up)"/>
<line x1="665.8" y1="319.2" x2="665.8" y2="379.7" stroke="var(--down)" class="wick"/>
<rect x="664.44" y="322.3" width="2.62" height="22.0" fill="var(--down)"/>
<line x1="670.0" y1="323.2" x2="670.0" y2="409.7" stroke="var(--down)" class="wick"/>
<rect x="668.67" y="327.0" width="2.62" height="54.8" fill="var(--down)"/>
<line x1="674.2" y1="371.9" x2="674.2" y2="432.2" stroke="var(--down)" class="wick"/>
<rect x="672.89" y="375.8" width="2.62" height="49.5" fill="var(--down)"/>
<line x1="678.4" y1="402.8" x2="678.4" y2="454.3" stroke="var(--down)" class="wick"/>
<rect x="677.11" y="433.3" width="2.62" height="4.8" fill="var(--down)"/>
<line x1="682.6" y1="413.7" x2="682.6" y2="446.9" stroke="var(--down)" class="wick"/>
<rect x="681.33" y="438.8" width="2.62" height="1.9" fill="var(--down)"/>
<line x1="686.9" y1="426.6" x2="686.9" y2="462.4" stroke="var(--up)" class="wick"/>
<rect x="685.55" y="427.9" width="2.62" height="17.1" fill="var(--up)"/>
<line x1="691.1" y1="397.0" x2="691.1" y2="448.8" stroke="var(--down)" class="wick"/>
<rect x="689.77" y="414.6" width="2.62" height="20.1" fill="var(--down)"/>
<line x1="695.3" y1="405.3" x2="695.3" y2="453.8" stroke="var(--up)" class="wick"/>
<rect x="693.99" y="417.3" width="2.62" height="29.5" fill="var(--up)"/>
<line x1="699.5" y1="344.2" x2="699.5" y2="412.8" stroke="var(--up)" class="wick"/>
<rect x="698.21" y="360.3" width="2.62" height="39.0" fill="var(--up)"/>
<line x1="703.7" y1="371.9" x2="703.7" y2="445.4" stroke="var(--up)" class="wick"/>
<rect x="702.44" y="399.5" width="2.62" height="6.6" fill="var(--up)"/>
<line x1="708.0" y1="366.7" x2="708.0" y2="425.5" stroke="var(--up)" class="wick"/>
<rect x="706.66" y="380.5" width="2.62" height="41.7" fill="var(--up)"/>
<line x1="712.2" y1="357.9" x2="712.2" y2="408.3" stroke="var(--down)" class="wick"/>
<rect x="710.88" y="382.4" width="2.62" height="24.3" fill="var(--down)"/>
<line x1="716.4" y1="402.7" x2="716.4" y2="446.2" stroke="var(--down)" class="wick"/>
<rect x="715.10" y="404.6" width="2.62" height="40.5" fill="var(--down)"/>
<line x1="720.6" y1="443.4" x2="720.6" y2="475.5" stroke="var(--down)" class="wick"/>
<rect x="719.32" y="448.4" width="2.62" height="14.2" fill="var(--down)"/>
<line x1="724.9" y1="453.1" x2="724.9" y2="489.2" stroke="var(--down)" class="wick"/>
<rect x="723.54" y="455.7" width="2.62" height="21.8" fill="var(--down)"/>
<line x1="729.1" y1="458.8" x2="729.1" y2="488.9" stroke="var(--up)" class="wick"/>
<rect x="727.76" y="459.7" width="2.62" height="22.3" fill="var(--up)"/>
<line x1="733.3" y1="444.6" x2="733.3" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="731.99" y="453.8" width="2.62" height="5.2" fill="var(--up)"/>
<line x1="737.5" y1="439.0" x2="737.5" y2="485.9" stroke="var(--down)" class="wick"/>
<rect x="736.21" y="445.7" width="2.62" height="38.1" fill="var(--down)"/>
<line x1="741.7" y1="478.8" x2="741.7" y2="520.7" stroke="var(--down)" class="wick"/>
<rect x="740.43" y="489.5" width="2.62" height="16.8" fill="var(--down)"/>
<line x1="746.0" y1="468.9" x2="746.0" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="744.65" y="482.1" width="2.62" height="32.4" fill="var(--up)"/>
<line x1="750.2" y1="471.2" x2="750.2" y2="491.5" stroke="var(--down)" class="wick"/>
<rect x="748.87" y="476.2" width="2.62" height="11.0" fill="var(--down)"/>
<line x1="754.4" y1="465.9" x2="754.4" y2="499.4" stroke="var(--up)" class="wick"/>
<rect x="753.09" y="467.7" width="2.62" height="22.8" fill="var(--up)"/>
<line x1="758.6" y1="454.7" x2="758.6" y2="477.5" stroke="var(--up)" class="wick"/>
<rect x="757.31" y="460.1" width="2.62" height="5.3" fill="var(--up)"/>
<line x1="762.8" y1="452.7" x2="762.8" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="761.53" y="460.2" width="2.62" height="4.3" fill="var(--up)"/>
<line x1="767.1" y1="387.4" x2="767.1" y2="458.4" stroke="var(--up)" class="wick"/>
<rect x="765.76" y="396.4" width="2.62" height="54.3" fill="var(--up)"/>
<line x1="771.3" y1="327.9" x2="771.3" y2="412.3" stroke="var(--up)" class="wick"/>
<rect x="769.98" y="338.7" width="2.62" height="73.6" fill="var(--up)"/>
<line x1="775.5" y1="275.9" x2="775.5" y2="346.4" stroke="var(--up)" class="wick"/>
<rect x="774.20" y="322.1" width="2.62" height="15.4" fill="var(--up)"/>
<line x1="779.7" y1="279.2" x2="779.7" y2="344.2" stroke="var(--up)" class="wick"/>
<rect x="778.42" y="299.6" width="2.62" height="26.2" fill="var(--up)"/>
<line x1="783.9" y1="218.4" x2="783.9" y2="310.1" stroke="var(--up)" class="wick"/>
<rect x="782.64" y="257.2" width="2.62" height="35.3" fill="var(--up)"/>
<line x1="788.2" y1="195.6" x2="788.2" y2="274.2" stroke="var(--down)" class="wick"/>
<rect x="786.86" y="232.5" width="2.62" height="40.1" fill="var(--down)"/>
<line x1="792.4" y1="213.7" x2="792.4" y2="293.3" stroke="var(--up)" class="wick"/>
<rect x="791.08" y="263.1" width="2.62" height="4.6" fill="var(--up)"/>
<line x1="796.6" y1="244.4" x2="796.6" y2="297.2" stroke="var(--down)" class="wick"/>
<rect x="795.30" y="254.2" width="2.62" height="31.0" fill="var(--down)"/>
<line x1="800.8" y1="265.6" x2="800.8" y2="306.5" stroke="var(--up)" class="wick"/>
<rect x="799.53" y="269.9" width="2.62" height="18.8" fill="var(--up)"/>
<line x1="805.1" y1="142.6" x2="805.1" y2="278.2" stroke="var(--up)" class="wick"/>
<rect x="803.75" y="148.6" width="2.62" height="121.0" fill="var(--up)"/>
<line x1="809.3" y1="118.8" x2="809.3" y2="225.9" stroke="var(--up)" class="wick"/>
<rect x="807.97" y="135.1" width="2.62" height="8.5" fill="var(--up)"/>
<line x1="813.5" y1="117.8" x2="813.5" y2="227.9" stroke="var(--down)" class="wick"/>
<rect x="812.19" y="119.7" width="2.62" height="84.3" fill="var(--down)"/>
<line x1="817.7" y1="164.7" x2="817.7" y2="256.9" stroke="var(--down)" class="wick"/>
<rect x="816.41" y="187.3" width="2.62" height="64.9" fill="var(--down)"/>
<line x1="821.9" y1="239.0" x2="821.9" y2="298.9" stroke="var(--down)" class="wick"/>
<rect x="820.63" y="246.2" width="2.62" height="42.8" fill="var(--down)"/>
<line x1="826.2" y1="284.0" x2="826.2" y2="335.1" stroke="var(--down)" class="wick"/>
<rect x="824.85" y="289.4" width="2.62" height="3.7" fill="var(--down)"/>
<line x1="830.4" y1="263.1" x2="830.4" y2="300.2" stroke="var(--down)" class="wick"/>
<rect x="829.07" y="283.6" width="2.62" height="13.2" fill="var(--down)"/>
<line x1="834.6" y1="216.5" x2="834.6" y2="316.3" stroke="var(--up)" class="wick"/>
<rect x="833.30" y="298.0" width="2.62" height="13.6" fill="var(--up)"/>
<line x1="838.8" y1="277.3" x2="838.8" y2="304.7" stroke="var(--up)" class="wick"/>
<rect x="837.52" y="280.8" width="2.62" height="13.5" fill="var(--up)"/>
<line x1="843.0" y1="179.5" x2="843.0" y2="292.3" stroke="var(--up)" class="wick"/>
<rect x="841.74" y="181.7" width="2.62" height="85.3" fill="var(--up)"/>
<line x1="847.3" y1="177.0" x2="847.3" y2="282.2" stroke="var(--down)" class="wick"/>
<rect x="845.96" y="201.3" width="2.62" height="63.7" fill="var(--down)"/>
<line x1="851.5" y1="234.1" x2="851.5" y2="291.1" stroke="var(--up)" class="wick"/>
<rect x="850.18" y="244.9" width="2.62" height="3.5" fill="var(--up)"/>
<line x1="855.7" y1="200.1" x2="855.7" y2="265.7" stroke="var(--down)" class="wick"/>
<rect x="854.40" y="231.6" width="2.62" height="21.6" fill="var(--down)"/>
<line x1="859.9" y1="80.5" x2="859.9" y2="230.6" stroke="var(--up)" class="wick"/>
<rect x="858.62" y="205.6" width="2.62" height="22.9" fill="var(--up)"/>
<line x1="864.2" y1="185.2" x2="864.2" y2="315.4" stroke="var(--down)" class="wick"/>
<rect x="862.84" y="185.2" width="2.62" height="82.3" fill="var(--down)"/>
<line x1="868.4" y1="193.4" x2="868.4" y2="275.2" stroke="var(--up)" class="wick"/>
<rect x="867.07" y="199.7" width="2.62" height="57.0" fill="var(--up)"/>
<line x1="872.6" y1="208.1" x2="872.6" y2="371.7" stroke="var(--down)" class="wick"/>
<rect x="871.29" y="210.5" width="2.62" height="127.3" fill="var(--down)"/>
<line x1="876.8" y1="321.1" x2="876.8" y2="421.2" stroke="var(--down)" class="wick"/>
<rect x="875.51" y="321.4" width="2.62" height="91.3" fill="var(--down)"/>
<line x1="881.0" y1="410.4" x2="881.0" y2="464.9" stroke="var(--down)" class="wick"/>
<rect x="879.73" y="414.2" width="2.62" height="35.1" fill="var(--down)"/>
<line x1="885.3" y1="433.3" x2="885.3" y2="453.1" stroke="var(--up)" class="wick"/>
<rect x="883.95" y="436.0" width="2.62" height="9.5" fill="var(--up)"/>
<line x1="889.5" y1="404.2" x2="889.5" y2="454.5" stroke="var(--up)" class="wick"/>
<rect x="888.17" y="422.8" width="2.62" height="20.0" fill="var(--up)"/>
<line x1="893.7" y1="407.9" x2="893.7" y2="451.9" stroke="var(--down)" class="wick"/>
<rect x="892.39" y="413.7" width="2.62" height="38.1" fill="var(--down)"/>
<line x1="897.9" y1="448.2" x2="897.9" y2="477.3" stroke="var(--down)" class="wick"/>
<rect x="896.61" y="448.5" width="2.62" height="24.8" fill="var(--down)"/>
<line x1="902.1" y1="462.1" x2="902.1" y2="485.8" stroke="var(--down)" class="wick"/>
<rect x="900.84" y="468.9" width="2.62" height="16.1" fill="var(--down)"/>
<line x1="906.4" y1="469.5" x2="906.4" y2="493.2" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="471.1" width="2.62" height="19.0" fill="var(--up)"/>
<line x1="910.6" y1="414.2" x2="910.6" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="909.28" y="431.2" width="2.62" height="24.4" fill="var(--up)"/>
<line x1="914.8" y1="430.8" x2="914.8" y2="450.5" stroke="var(--down)" class="wick"/>
<rect x="913.50" y="433.0" width="2.62" height="1.2" fill="var(--down)"/>
<line x1="919.0" y1="425.1" x2="919.0" y2="450.9" stroke="var(--up)" class="wick"/>
<rect x="917.72" y="438.2" width="2.62" height="3.7" fill="var(--up)"/>
<line x1="923.3" y1="427.2" x2="923.3" y2="461.4" stroke="var(--down)" class="wick"/>
<rect x="921.94" y="440.7" width="2.62" height="19.2" fill="var(--down)"/>
<line x1="927.5" y1="455.4" x2="927.5" y2="486.5" stroke="var(--up)" class="wick"/>
<rect x="926.16" y="459.5" width="2.62" height="2.5" fill="var(--up)"/>
<line x1="931.7" y1="456.7" x2="931.7" y2="496.2" stroke="var(--down)" class="wick"/>
<rect x="930.39" y="463.1" width="2.62" height="27.0" fill="var(--down)"/>
<line x1="935.9" y1="486.7" x2="935.9" y2="499.4" stroke="var(--down)" class="wick"/>
<rect x="934.61" y="491.9" width="2.62" height="6.5" fill="var(--down)"/>
<line x1="940.1" y1="497.1" x2="940.1" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="938.83" y="501.4" width="2.62" height="2.6" fill="var(--down)"/>
<line x1="944.4" y1="497.9" x2="944.4" y2="515.7" stroke="var(--down)" class="wick"/>
<rect x="943.05" y="509.2" width="2.62" height="5.9" fill="var(--down)"/>
<line x1="948.6" y1="506.7" x2="948.6" y2="519.4" stroke="var(--up)" class="wick"/>
<rect x="947.27" y="513.9" width="2.62" height="3.9" fill="var(--up)"/>
<line x1="952.8" y1="505.4" x2="952.8" y2="519.8" stroke="var(--down)" class="wick"/>
<rect x="951.49" y="512.3" width="2.62" height="5.0" fill="var(--down)"/>
<line x1="957.0" y1="511.0" x2="957.0" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="955.71" y="516.4" width="2.62" height="11.8" fill="var(--down)"/>
<line x1="961.2" y1="521.5" x2="961.2" y2="534.3" stroke="var(--down)" class="wick"/>
<rect x="959.93" y="526.5" width="2.62" height="3.1" fill="var(--down)"/>
<line x1="965.5" y1="526.2" x2="965.5" y2="539.2" stroke="var(--down)" class="wick"/>
<rect x="964.16" y="530.0" width="2.62" height="8.5" fill="var(--down)"/>
<line x1="969.7" y1="499.6" x2="969.7" y2="541.9" stroke="var(--up)" class="wick"/>
<rect x="968.38" y="505.8" width="2.62" height="34.2" fill="var(--up)"/>
<line x1="973.9" y1="491.1" x2="973.9" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="972.60" y="509.4" width="2.62" height="3.0" fill="var(--down)"/>
<line x1="978.1" y1="505.0" x2="978.1" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="976.82" y="510.7" width="2.62" height="3.6" fill="var(--up)"/>
<line x1="982.3" y1="496.1" x2="982.3" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="981.04" y="506.8" width="2.62" height="4.2" fill="var(--up)"/>
<line x1="986.6" y1="496.5" x2="986.6" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="985.26" y="509.3" width="2.62" height="10.0" fill="var(--down)"/>
<line x1="990.8" y1="513.8" x2="990.8" y2="534.2" stroke="var(--up)" class="wick"/>
<rect x="989.48" y="517.7" width="2.62" height="1.9" fill="var(--up)"/>
<line x1="995.0" y1="501.5" x2="995.0" y2="516.4" stroke="var(--up)" class="wick"/>
<rect x="993.70" y="505.6" width="2.62" height="6.5" fill="var(--up)"/>
<line x1="999.2" y1="490.1" x2="999.2" y2="529.6" stroke="var(--down)" class="wick"/>
<rect x="997.93" y="507.5" width="2.62" height="18.8" fill="var(--down)"/>
<line x1="1003.5" y1="521.3" x2="1003.5" y2="539.4" stroke="var(--down)" class="wick"/>
<rect x="1002.15" y="522.5" width="2.62" height="9.6" fill="var(--down)"/>
<line x1="1007.7" y1="513.9" x2="1007.7" y2="532.7" stroke="var(--up)" class="wick"/>
<rect x="1006.37" y="514.5" width="2.62" height="12.4" fill="var(--up)"/>
<line x1="1011.9" y1="513.4" x2="1011.9" y2="533.5" stroke="var(--down)" class="wick"/>
<rect x="1010.59" y="519.4" width="2.62" height="10.6" fill="var(--down)"/>
<line x1="1016.1" y1="522.7" x2="1016.1" y2="534.8" stroke="var(--down)" class="wick"/>
<rect x="1014.81" y="528.4" width="2.62" height="4.9" fill="var(--down)"/>
<line x1="1020.3" y1="529.9" x2="1020.3" y2="544.8" stroke="var(--down)" class="wick"/>
<rect x="1019.03" y="533.7" width="2.62" height="6.5" fill="var(--down)"/>
<line x1="1024.6" y1="540.8" x2="1024.6" y2="557.5" stroke="var(--down)" class="wick"/>
<rect x="1023.25" y="541.7" width="2.62" height="10.9" fill="var(--down)"/>
<line x1="1028.8" y1="541.0" x2="1028.8" y2="554.0" stroke="var(--up)" class="wick"/>
<rect x="1027.47" y="549.1" width="2.62" height="3.0" fill="var(--up)"/>
<line x1="1033.0" y1="540.4" x2="1033.0" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="1031.70" y="546.0" width="2.62" height="1.0" fill="var(--up)"/>
<line x1="1037.2" y1="530.8" x2="1037.2" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="1035.92" y="532.7" width="2.62" height="12.8" fill="var(--up)"/>
<line x1="1041.4" y1="529.7" x2="1041.4" y2="538.9" stroke="var(--down)" class="wick"/>
<rect x="1040.14" y="533.0" width="2.62" height="3.8" fill="var(--down)"/>
<line x1="1045.7" y1="534.7" x2="1045.7" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="1044.36" y="535.8" width="2.62" height="8.1" fill="var(--down)"/>
<line x1="1049.9" y1="538.7" x2="1049.9" y2="544.5" stroke="var(--down)" class="wick"/>
<rect x="1048.58" y="541.5" width="2.62" height="2.4" fill="var(--down)"/>
<line x1="60" y1="519.1" x2="1052" y2="519.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="522.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$11.25 R1</text>
<text x="1058" y="534.6" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="490.6" x2="1052" y2="490.6" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="494.1" font-size="11.5" fill="var(--resistance)" font-weight="600">$14.25 R2</text>
<text x="1058" y="506.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="543.9" r="3" fill="var(--ink)"/>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $14.25 | 2 | 2022년 7~9월(SPAC 상장 초기 박스권 상단)·2025년 3월·2025년 12월~2026년 상반기(11월 실적 충격 이후 반등 상단)에 걸쳐 반복 형성 |
| R1 | $11.25 | 3 | 2022년 상장 초기(9~12월)·2024년 하반기(랠리 이전 바닥)·2026년 3~6월(실적 충격 이후 조정) — 5년 내내 반복적으로 나타난 다년 구조적 레벨 |
| **현재가** | **$8.64** (2026-08-18 종가) | — | 기간 내 하단 지지 없음(신저가 구간) — 가장 가까운 저항은 R1 |

> $11~15 구간은 이 회사의 상장 이후 5년 내내 반복적으로 되돌아온 몇 안 되는 "안정적" 가격대다 — 다만 2022년(스팩 상장 초기)·2024년(랠리 전 바닥)·2026년(실적 충격 후 조정)이라는 **서로 완전히 다른 국면**에서 형성된 레벨이 우연히 겹친 것일 수 있어, 이 자체를 강한 구조적 지지/저항으로 과신하지 말 것(4. 방법론 · 한계 참고). 5년 중 상당 기간(2025년 8~11월) 주가가 이 구간을 크게 벗어나 있었다는 점도 함께 봐야 한다.

---

## 3. 관측된 특이 구간 — 2025년 하반기 급등·급락 사이클

- 2025년 여름부터 10월까지 AI 데이터센터발 SMR 재조명 테마 속에 주가가 5년 최저권($1.81, 2023~2024년경 형성)에서 52주 최고 $57.42(2025년 10월경)까지 단기간에 급등했다.
- 2025-11-06 3분기 실적 발표(Milestone Contribution $507.4M 비용 인식, 최근 뉴스 / 이슈 참고)를 기점으로 급락이 시작돼 2026-08-18 기준 $8.64까지 되돌림 — 52주 최고 대비 약 −85%.
- 이 사건 전후로 거래 레짐이 완전히 바뀌었다 — 급등 구간(2025년 여름~10월)은 스윙 클러스터를 형성할 만큼 충분히 머물지 못해 2. 지지선 / 저항선 요약 레벨 표에는 반영되지 않았고, 참고용 배경으로만 남긴다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 235개 주, 2022-02-28~2026-08-18. 수집 시점: 2026-08-19. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 2. 지지선 / 저항선 요약 비고).
- **생성**: `scripts/gen_technical_chart.py SMR --name "NuScale Power" --interval 1wk --event 2025-11-06:"3분기 실적발표(Milestone Contribution 갭다운)" --close-on 2026-08-18` (재현용 — 2025-11-06은 주봉 마감일이 아니라 이벤트선은 실제로 그려지지 않았다는 경고가 있었음, 스크립트 출력 로그 참고)
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 235개 표본에서 임의로 선택한 파라미터이며, 최적화된 값이 아니다.
    - 2025년 하반기 급등·급락(3. 관측된 특이 구간 — 2025년 하반기 급등·급락 사이클)으로 가격대가 두 차례 구조적으로 재설정됐다 — 5년 구간 전체를 하나의 연속된 레짐으로 해석하면 안 된다.
    - 2022-02-28~2022-05-02 구간은 NuScale이 아니라 SPAC 셸의 가격이라는 점(위 상단 각주 참고), 이 기간 중 주식분할은 없었으나 대규모 신주 발행이 반복돼 시가총액 기준 밸류에이션과 이 문서의 "주가 자체" 기술적 분석은 별개로 봐야 한다.

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
- [기술적 분석 — 일봉·1년](./09_technical_daily.md)
- [최종 보고서](./11_final_report.md)

---

## 참고 자료

- [Yahoo Finance — SMR 주봉 OHLCV 원자료](https://finance.yahoo.com/quote/SMR/history/)
- [stockanalysis.com — SMR 시황 (조회 2026-08-19)](https://stockanalysis.com/stocks/smr/)

---

*작성일: 2026-08-19*
