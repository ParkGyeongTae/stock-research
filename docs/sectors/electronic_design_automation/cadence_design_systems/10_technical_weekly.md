# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)를 따로 참고할 것.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(5년 주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 2026-08-24 종가 **$315.92**는 [기술적 분석 — 일봉·1년](./09_technical_daily.md)의 동일 시점 종가와 일치하며(같은 스크립트·같은 원자료 출처), [핵심 지표](./04_metrics.md) A.2·[밸류에이션 / 적정주가](./06_valuation.md)가 인용한 stockanalysis.com 값과도 일치한다. 이 폴더의 11개 문서 전체가 같은 기준일(2026-08-24)을 쓴다.
    - 원주가(배당 미반영) 기준이며, Cadence는 표 기간 내 주식분할 이력이 없어 소급조정 이슈 자체가 없다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-24)

<div class="cdns-chart">
<style>
.cdns-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .cdns-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .cdns-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.cdns-chart svg { width:100%; height:auto; display:block; }
.cdns-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.cdns-chart .title { fill: var(--ink); font-weight:600; }
.cdns-chart .grid { stroke: var(--grid); stroke-width:1; }
.cdns-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Cadence Design Systems(CDNS) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Cadence Design Systems (CDNS) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-24 · 마지막 종가 $315.92 (2026-08-24) · 단위 USD</text>
<line x1="60" y1="570.8" x2="1052" y2="570.8" class="grid"/>
<text x="52" y="574.8" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="478.9" x2="1052" y2="478.9" class="grid"/>
<text x="52" y="482.9" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="387.0" x2="1052" y2="387.0" class="grid"/>
<text x="52" y="391.0" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="295.0" x2="1052" y2="295.0" class="grid"/>
<text x="52" y="299.0" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="203.1" x2="1052" y2="203.1" class="grid"/>
<text x="52" y="207.1" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="111.2" x2="1052" y2="111.2" class="grid"/>
<text x="52" y="115.2" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="133.8" y1="56.0" x2="133.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="133.8" y1="626.0" x2="133.8" y2="631.0" class="axis"/>
<text x="133.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="330.7" y1="56.0" x2="330.7" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="330.7" y1="626.0" x2="330.7" y2="631.0" class="axis"/>
<text x="330.7" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="527.6" y1="56.0" x2="527.6" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="527.6" y1="626.0" x2="527.6" y2="631.0" class="axis"/>
<text x="527.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="728.3" y1="56.0" x2="728.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="728.3" y1="626.0" x2="728.3" y2="631.0" class="axis"/>
<text x="728.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.2" y1="56.0" x2="925.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="925.2" y1="626.0" x2="925.2" y2="631.0" class="axis"/>
<text x="925.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="60" y1="80.5" x2="1052" y2="80.5" stroke="var(--ref)" stroke-width="1" stroke-dasharray="2,3" opacity="0.7"/>
<text x="1058" y="83.5" font-size="10.5" fill="var(--muted)">$417 5년 최고(2026-06-01, ChipStack AI 발표)</text>
<line x1="202.0" y1="56.0" x2="202.0" y2="626.0" stroke="var(--down)" stroke-width="1" stroke-dasharray="1,3" opacity="0.55"/>
<text x="208.0" y="68.0" font-size="10.5" fill="var(--down)">2022-05-09 2022 금리인상기 성장주 조정 저점</text>
<line x1="61.9" y1="547.0" x2="61.9" y2="556.7" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="547.9" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="65.7" y1="539.3" x2="65.7" y2="547.9" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="542.0" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="69.5" y1="536.6" x2="69.5" y2="546.2" stroke="var(--up)" class="wick"/>
<rect x="68.29" y="539.8" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="73.3" y1="537.4" x2="73.3" y2="548.6" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="538.1" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="77.0" y1="545.1" x2="77.0" y2="554.4" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="545.9" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="80.8" y1="549.0" x2="80.8" y2="572.2" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="549.7" width="2.35" height="15.6" fill="var(--down)"/>
<line x1="84.6" y1="564.9" x2="84.6" y2="578.5" stroke="var(--down)" class="wick"/>
<rect x="83.44" y="567.4" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="88.4" y1="556.2" x2="88.4" y2="572.8" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="560.2" width="2.35" height="11.4" fill="var(--up)"/>
<line x1="92.2" y1="538.7" x2="92.2" y2="562.6" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="540.0" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="96.0" y1="524.7" x2="96.0" y2="543.9" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="528.3" width="2.35" height="9.4" fill="var(--up)"/>
<line x1="99.8" y1="514.5" x2="99.8" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="519.4" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="103.5" y1="510.9" x2="103.5" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="513.0" width="2.35" height="3.3" fill="var(--up)"/>
<line x1="107.3" y1="497.1" x2="107.3" y2="516.0" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="500.7" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="111.1" y1="497.5" x2="111.1" y2="520.9" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="500.6" width="2.35" height="18.1" fill="var(--down)"/>
<line x1="114.9" y1="501.9" x2="114.9" y2="524.8" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="513.2" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="118.7" y1="504.6" x2="118.7" y2="528.8" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="508.1" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="122.5" y1="506.0" x2="122.5" y2="533.1" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="508.3" width="2.35" height="8.9" fill="var(--down)"/>
<line x1="126.3" y1="499.7" x2="126.3" y2="524.4" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="501.9" width="2.35" height="21.4" fill="var(--up)"/>
<line x1="130.0" y1="492.3" x2="130.0" y2="506.6" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="499.3" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="133.8" y1="499.9" x2="133.8" y2="541.5" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="505.2" width="2.35" height="36.1" fill="var(--down)"/>
<line x1="137.6" y1="529.2" x2="137.6" y2="553.5" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="547.3" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="141.4" y1="557.6" x2="141.4" y2="574.4" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="559.8" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="145.2" y1="567.2" x2="145.2" y2="595.4" stroke="var(--down)" class="wick"/>
<rect x="144.02" y="577.8" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="149.0" y1="564.5" x2="149.0" y2="580.7" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="575.4" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="152.8" y1="562.7" x2="152.8" y2="586.8" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="574.2" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="156.5" y1="576.7" x2="156.5" y2="600.2" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="584.6" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="160.3" y1="564.7" x2="160.3" y2="601.9" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="565.5" width="2.35" height="33.6" fill="var(--up)"/>
<line x1="164.1" y1="553.4" x2="164.1" y2="573.1" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="562.2" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="167.9" y1="560.9" x2="167.9" y2="582.9" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="561.8" width="2.35" height="18.4" fill="var(--down)"/>
<line x1="171.7" y1="553.0" x2="171.7" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="554.5" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="175.5" y1="546.5" x2="175.5" y2="563.6" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="554.6" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="179.3" y1="538.9" x2="179.3" y2="555.0" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="542.1" width="2.35" height="12.2" fill="var(--up)"/>
<line x1="183.1" y1="536.4" x2="183.1" y2="556.5" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="541.5" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="186.8" y1="554.3" x2="186.8" y2="572.6" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="557.6" width="2.35" height="13.6" fill="var(--down)"/>
<line x1="190.6" y1="550.7" x2="190.6" y2="574.9" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="573.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="194.4" y1="550.7" x2="194.4" y2="576.0" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="569.3" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="198.2" y1="554.8" x2="198.2" y2="584.0" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="569.8" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="202.0" y1="581.2" x2="202.0" y2="603.3" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="583.0" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="205.8" y1="575.5" x2="205.8" y2="597.6" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="577.1" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="209.6" y1="559.2" x2="209.6" y2="585.5" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="559.4" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="213.3" y1="549.3" x2="213.3" y2="567.5" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="555.1" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="217.1" y1="544.8" x2="217.1" y2="574.8" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="550.8" width="2.35" height="21.7" fill="var(--down)"/>
<line x1="220.9" y1="571.0" x2="220.9" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="581.1" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="224.7" y1="556.3" x2="224.7" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="556.8" width="2.35" height="22.0" fill="var(--up)"/>
<line x1="228.5" y1="555.5" x2="228.5" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="557.5" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="232.3" y1="549.8" x2="232.3" y2="576.4" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="551.7" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="236.1" y1="548.4" x2="236.1" y2="573.0" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="554.5" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="239.8" y1="532.0" x2="239.8" y2="563.1" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="538.3" width="2.35" height="17.7" fill="var(--up)"/>
<line x1="243.6" y1="503.6" x2="243.6" y2="542.9" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="504.5" width="2.35" height="33.8" fill="var(--up)"/>
<line x1="247.4" y1="501.9" x2="247.4" y2="522.6" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="503.6" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="251.2" y1="497.4" x2="251.2" y2="509.9" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="499.4" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="255.0" y1="488.2" x2="255.0" y2="503.5" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="499.4" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="258.8" y1="502.6" x2="258.8" y2="520.3" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="504.0" width="2.35" height="15.6" fill="var(--down)"/>
<line x1="262.6" y1="520.3" x2="262.6" y2="539.8" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="523.7" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="266.4" y1="523.1" x2="266.4" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="525.5" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="270.1" y1="524.0" x2="270.1" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="524.7" width="2.35" height="19.9" fill="var(--down)"/>
<line x1="273.9" y1="530.3" x2="273.9" y2="554.1" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="547.6" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="277.7" y1="538.4" x2="277.7" y2="551.3" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="546.1" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="281.5" y1="526.1" x2="281.5" y2="556.1" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="544.4" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="285.3" y1="552.7" x2="285.3" y2="584.9" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="553.4" width="2.35" height="22.1" fill="var(--down)"/>
<line x1="289.1" y1="552.8" x2="289.1" y2="569.6" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="555.5" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="292.9" y1="549.9" x2="292.9" y2="577.5" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="552.4" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="296.6" y1="563.9" x2="296.6" y2="591.5" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="570.5" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="300.4" y1="537.8" x2="300.4" y2="586.2" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="539.8" width="2.35" height="42.6" fill="var(--up)"/>
<line x1="304.2" y1="529.7" x2="304.2" y2="547.2" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="541.4" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="308.0" y1="536.5" x2="308.0" y2="550.9" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="539.0" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="311.8" y1="520.7" x2="311.8" y2="549.0" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="529.6" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="315.6" y1="532.4" x2="315.6" y2="553.0" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="533.2" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="319.4" y1="525.8" x2="319.4" y2="551.8" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="545.2" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="323.1" y1="541.8" x2="323.1" y2="554.4" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="546.7" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="326.9" y1="546.6" x2="326.9" y2="555.8" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="550.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="330.7" y1="545.1" x2="330.7" y2="561.9" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="547.2" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="334.5" y1="535.2" x2="334.5" y2="550.0" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="535.4" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="338.3" y1="517.6" x2="338.3" y2="535.1" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="518.9" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="342.1" y1="504.2" x2="342.1" y2="522.1" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="506.4" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="345.9" y1="493.8" x2="345.9" y2="514.5" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="504.9" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="349.6" y1="496.2" x2="349.6" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="507.5" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="353.4" y1="473.5" x2="353.4" y2="508.7" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="489.1" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="357.2" y1="481.5" x2="357.2" y2="494.6" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="490.4" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="361.0" y1="484.8" x2="361.0" y2="498.6" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="485.3" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="364.8" y1="475.3" x2="364.8" y2="492.2" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="484.5" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="368.6" y1="461.4" x2="368.6" y2="491.6" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="466.3" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="372.4" y1="461.9" x2="372.4" y2="473.3" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="466.0" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="376.2" y1="460.1" x2="376.2" y2="476.4" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="460.4" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="379.9" y1="452.9" x2="379.9" y2="469.1" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="462.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="383.7" y1="446.4" x2="383.7" y2="466.0" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="452.1" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="387.5" y1="449.9" x2="387.5" y2="459.9" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="451.3" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="391.3" y1="451.7" x2="391.3" y2="489.9" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="455.4" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="395.1" y1="455.2" x2="395.1" y2="472.7" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="461.8" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="398.9" y1="467.3" x2="398.9" y2="480.2" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="468.9" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="402.7" y1="443.8" x2="402.7" y2="480.9" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="448.2" width="2.35" height="29.1" fill="var(--up)"/>
<line x1="406.4" y1="419.8" x2="406.4" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="426.8" width="2.35" height="23.5" fill="var(--up)"/>
<line x1="410.2" y1="407.2" x2="410.2" y2="428.1" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="420.1" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="414.0" y1="416.2" x2="414.0" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="425.0" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="417.8" y1="400.5" x2="417.8" y2="427.0" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="413.0" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="421.6" y1="411.4" x2="421.6" y2="436.9" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="415.4" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="425.4" y1="413.2" x2="425.4" y2="436.8" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="415.4" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="429.2" y1="409.6" x2="429.2" y2="430.9" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="415.7" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="432.9" y1="397.2" x2="432.9" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="404.0" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="436.7" y1="390.4" x2="436.7" y2="408.8" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="400.1" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="440.5" y1="399.3" x2="440.5" y2="420.9" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="400.8" width="2.35" height="15.2" fill="var(--down)"/>
<line x1="444.3" y1="412.2" x2="444.3" y2="430.3" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="414.8" width="2.35" height="10.8" fill="var(--down)"/>
<line x1="448.1" y1="416.9" x2="448.1" y2="438.0" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="422.8" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="451.9" y1="426.7" x2="451.9" y2="446.2" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="433.0" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="455.7" y1="409.2" x2="455.7" y2="439.1" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="419.1" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="459.5" y1="398.3" x2="459.5" y2="422.2" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="398.8" width="2.35" height="17.6" fill="var(--up)"/>
<line x1="463.2" y1="391.6" x2="463.2" y2="413.0" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="399.0" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="467.0" y1="397.7" x2="467.0" y2="419.7" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="407.6" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="470.8" y1="408.5" x2="470.8" y2="426.5" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="418.0" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="474.6" y1="407.0" x2="474.6" y2="429.2" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="415.8" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="478.4" y1="396.4" x2="478.4" y2="427.8" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="398.1" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="482.2" y1="376.2" x2="482.2" y2="404.8" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="386.5" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="486.0" y1="382.0" x2="486.0" y2="409.0" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="383.4" width="2.35" height="24.5" fill="var(--down)"/>
<line x1="489.7" y1="398.1" x2="489.7" y2="426.2" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="407.0" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="493.5" y1="385.1" x2="493.5" y2="422.5" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="387.8" width="2.35" height="30.4" fill="var(--up)"/>
<line x1="497.3" y1="364.1" x2="497.3" y2="391.9" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="365.7" width="2.35" height="21.1" fill="var(--up)"/>
<line x1="501.1" y1="342.3" x2="501.1" y2="369.4" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="353.4" width="2.35" height="14.1" fill="var(--up)"/>
<line x1="504.9" y1="343.0" x2="504.9" y2="358.1" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="349.1" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="508.7" y1="333.0" x2="508.7" y2="353.5" stroke="var(--down)" class="wick"/>
<rect x="507.50" y="348.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="512.5" y1="353.7" x2="512.5" y2="374.2" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="354.7" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="516.2" y1="335.1" x2="516.2" y2="365.6" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="347.4" width="2.35" height="18.2" fill="var(--up)"/>
<line x1="520.0" y1="335.9" x2="520.0" y2="352.0" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="339.5" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="523.8" y1="333.3" x2="523.8" y2="348.6" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="338.0" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="527.6" y1="351.7" x2="527.6" y2="383.4" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="351.7" width="2.35" height="30.2" fill="var(--down)"/>
<line x1="531.4" y1="352.4" x2="531.4" y2="380.1" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="353.0" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="535.2" y1="308.7" x2="535.2" y2="353.7" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="309.5" width="2.35" height="43.3" fill="var(--up)"/>
<line x1="539.0" y1="292.1" x2="539.0" y2="318.6" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="302.5" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="542.7" y1="297.7" x2="542.7" y2="318.9" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="301.4" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="546.5" y1="270.9" x2="546.5" y2="313.9" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="273.1" width="2.35" height="29.9" fill="var(--up)"/>
<line x1="550.3" y1="266.2" x2="550.3" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="267.5" width="2.35" height="45.4" fill="var(--down)"/>
<line x1="554.1" y1="279.8" x2="554.1" y2="323.0" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="288.5" width="2.35" height="25.0" fill="var(--up)"/>
<line x1="557.9" y1="266.0" x2="557.9" y2="298.7" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="267.0" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="561.7" y1="256.8" x2="561.7" y2="287.2" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="267.0" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="565.5" y1="271.3" x2="565.5" y2="298.5" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="282.2" width="2.35" height="15.7" fill="var(--down)"/>
<line x1="569.3" y1="244.7" x2="569.3" y2="294.6" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="253.2" width="2.35" height="40.2" fill="var(--up)"/>
<line x1="573.0" y1="255.8" x2="573.0" y2="277.9" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="260.8" width="2.35" height="13.5" fill="var(--down)"/>
<line x1="576.8" y1="263.6" x2="576.8" y2="288.5" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="275.8" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="580.6" y1="270.3" x2="580.6" y2="289.5" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="278.4" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="584.4" y1="275.3" x2="584.4" y2="332.5" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="275.7" width="2.35" height="55.6" fill="var(--down)"/>
<line x1="588.2" y1="318.1" x2="588.2" y2="343.8" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="324.5" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="592.0" y1="321.3" x2="592.0" y2="349.5" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="324.9" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="595.8" y1="312.4" x2="595.8" y2="331.3" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="318.1" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="599.5" y1="304.7" x2="599.5" y2="327.9" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="314.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="603.3" y1="291.5" x2="603.3" y2="318.4" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="305.5" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="607.1" y1="298.9" x2="607.1" y2="333.6" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="307.8" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="610.9" y1="296.1" x2="610.9" y2="329.5" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="305.3" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="614.7" y1="263.9" x2="614.7" y2="309.3" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="272.8" width="2.35" height="33.8" fill="var(--up)"/>
<line x1="618.5" y1="241.7" x2="618.5" y2="275.8" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="261.2" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="622.3" y1="262.8" x2="622.3" y2="282.0" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="262.8" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="626.0" y1="254.1" x2="626.0" y2="287.5" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="256.2" width="2.35" height="24.6" fill="var(--up)"/>
<line x1="629.8" y1="254.6" x2="629.8" y2="274.3" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="258.3" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="633.6" y1="262.8" x2="633.6" y2="344.4" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="268.2" width="2.35" height="63.7" fill="var(--down)"/>
<line x1="637.4" y1="310.1" x2="637.4" y2="372.7" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="325.2" width="2.35" height="45.7" fill="var(--down)"/>
<line x1="641.2" y1="348.5" x2="641.2" y2="402.7" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="367.7" width="2.35" height="20.0" fill="var(--down)"/>
<line x1="645.0" y1="348.2" x2="645.0" y2="403.0" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="350.0" width="2.35" height="38.0" fill="var(--up)"/>
<line x1="648.8" y1="326.3" x2="648.8" y2="362.3" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="330.0" width="2.35" height="22.2" fill="var(--up)"/>
<line x1="652.5" y1="318.1" x2="652.5" y2="345.1" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="329.6" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="656.3" y1="346.6" x2="656.3" y2="367.3" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="347.6" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="660.1" y1="353.0" x2="660.1" y2="395.3" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="355.9" width="2.35" height="35.6" fill="var(--down)"/>
<line x1="663.9" y1="346.0" x2="663.9" y2="394.7" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="352.5" width="2.35" height="32.0" fill="var(--up)"/>
<line x1="667.7" y1="322.7" x2="667.7" y2="356.0" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="343.3" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="671.5" y1="330.1" x2="671.5" y2="353.2" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="341.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="675.3" y1="342.2" x2="675.3" y2="364.4" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="346.3" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="679.1" y1="326.0" x2="679.1" y2="366.1" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="327.4" width="2.35" height="31.6" fill="var(--up)"/>
<line x1="682.8" y1="322.6" x2="682.8" y2="371.8" stroke="var(--down)" class="wick"/>
<rect x="681.67" y="323.1" width="2.35" height="48.2" fill="var(--down)"/>
<line x1="686.6" y1="368.4" x2="686.6" y2="393.2" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="373.5" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="690.4" y1="313.1" x2="690.4" y2="383.6" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="328.0" width="2.35" height="43.0" fill="var(--up)"/>
<line x1="694.2" y1="284.9" x2="694.2" y2="327.0" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="292.7" width="2.35" height="30.8" fill="var(--up)"/>
<line x1="698.0" y1="276.7" x2="698.0" y2="318.0" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="294.1" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="701.8" y1="270.5" x2="701.8" y2="315.7" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="273.2" width="2.35" height="37.7" fill="var(--up)"/>
<line x1="705.6" y1="264.9" x2="705.6" y2="290.5" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="267.5" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="709.3" y1="246.9" x2="709.3" y2="290.2" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="281.2" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="713.1" y1="267.4" x2="713.1" y2="294.6" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="276.6" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="716.9" y1="263.3" x2="716.9" y2="302.4" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="277.5" width="2.35" height="14.8" fill="var(--down)"/>
<line x1="720.7" y1="276.2" x2="720.7" y2="295.3" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="285.8" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="724.5" y1="283.6" x2="724.5" y2="302.8" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="287.9" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="728.3" y1="266.4" x2="728.3" y2="300.0" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="283.2" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="732.1" y1="282.1" x2="732.1" y2="315.3" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="284.7" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="735.8" y1="249.0" x2="735.8" y2="287.0" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="257.4" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="739.6" y1="276.8" x2="739.6" y2="322.5" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="284.7" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="743.4" y1="276.8" x2="743.4" y2="313.7" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="295.6" width="2.35" height="13.5" fill="var(--up)"/>
<line x1="747.2" y1="284.2" x2="747.2" y2="309.8" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="288.0" width="2.35" height="15.9" fill="var(--down)"/>
<line x1="751.0" y1="293.5" x2="751.0" y2="374.4" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="300.4" width="2.35" height="71.3" fill="var(--down)"/>
<line x1="754.8" y1="364.1" x2="754.8" y2="394.7" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="365.3" width="2.35" height="20.8" fill="var(--down)"/>
<line x1="758.6" y1="380.6" x2="758.6" y2="416.9" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="381.4" width="2.35" height="18.0" fill="var(--down)"/>
<line x1="762.4" y1="390.6" x2="762.4" y2="423.6" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="391.7" width="2.35" height="17.0" fill="var(--up)"/>
<line x1="766.1" y1="355.8" x2="766.1" y2="393.9" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="364.1" width="2.35" height="29.7" fill="var(--up)"/>
<line x1="769.9" y1="350.7" x2="769.9" y2="376.2" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="357.5" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="773.7" y1="358.0" x2="773.7" y2="419.4" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="381.3" width="2.35" height="37.2" fill="var(--down)"/>
<line x1="777.5" y1="356.4" x2="777.5" y2="439.3" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="369.6" width="2.35" height="54.8" fill="var(--up)"/>
<line x1="781.3" y1="357.4" x2="781.3" y2="378.7" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="360.1" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="785.1" y1="312.5" x2="785.1" y2="391.2" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="314.1" width="2.35" height="60.0" fill="var(--up)"/>
<line x1="788.9" y1="275.6" x2="788.9" y2="328.7" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="280.0" width="2.35" height="37.0" fill="var(--up)"/>
<line x1="792.6" y1="271.1" x2="792.6" y2="290.8" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="282.2" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="796.4" y1="254.2" x2="796.4" y2="279.3" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="255.4" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="800.2" y1="253.4" x2="800.2" y2="273.6" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="260.5" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="804.0" y1="252.0" x2="804.0" y2="338.0" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="259.3" width="2.35" height="59.6" fill="var(--down)"/>
<line x1="807.8" y1="291.4" x2="807.8" y2="321.7" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="300.6" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="811.6" y1="274.9" x2="811.6" y2="295.7" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="281.1" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="815.4" y1="286.9" x2="815.4" y2="306.4" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="293.8" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="819.1" y1="265.8" x2="819.1" y2="314.0" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="285.5" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="822.9" y1="239.7" x2="822.9" y2="286.3" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="245.7" width="2.35" height="38.0" fill="var(--up)"/>
<line x1="826.7" y1="243.6" x2="826.7" y2="261.6" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="245.7" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="830.5" y1="250.0" x2="830.5" y2="274.7" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="258.0" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="834.3" y1="230.4" x2="834.3" y2="271.1" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="235.8" width="2.35" height="31.5" fill="var(--up)"/>
<line x1="838.1" y1="154.5" x2="838.1" y2="242.7" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="190.3" width="2.35" height="41.4" fill="var(--up)"/>
<line x1="841.9" y1="167.9" x2="841.9" y2="203.7" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="187.0" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="845.6" y1="191.3" x2="845.6" y2="212.7" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="199.3" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="849.4" y1="190.4" x2="849.4" y2="222.2" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="203.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="853.2" y1="193.0" x2="853.2" y2="215.8" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="202.3" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="857.0" y1="193.3" x2="857.0" y2="220.4" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="201.2" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="860.8" y1="179.7" x2="860.8" y2="246.6" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="196.3" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="864.6" y1="158.4" x2="864.6" y2="219.3" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="160.2" width="2.35" height="55.5" fill="var(--up)"/>
<line x1="868.4" y1="159.2" x2="868.4" y2="208.6" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="166.3" width="2.35" height="36.6" fill="var(--down)"/>
<line x1="872.2" y1="193.6" x2="872.2" y2="212.3" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="197.8" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="875.9" y1="194.2" x2="875.9" y2="247.5" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="203.1" width="2.35" height="42.3" fill="var(--down)"/>
<line x1="879.7" y1="232.1" x2="879.7" y2="261.9" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="240.3" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="883.5" y1="201.0" x2="883.5" y2="246.9" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="212.1" width="2.35" height="31.8" fill="var(--up)"/>
<line x1="887.3" y1="189.3" x2="887.3" y2="245.1" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="189.3" width="2.35" height="34.6" fill="var(--down)"/>
<line x1="891.1" y1="218.3" x2="891.1" y2="260.9" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="218.3" width="2.35" height="30.6" fill="var(--down)"/>
<line x1="894.9" y1="238.3" x2="894.9" y2="275.5" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="246.2" width="2.35" height="21.4" fill="var(--down)"/>
<line x1="898.7" y1="264.3" x2="898.7" y2="303.9" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="270.1" width="2.35" height="23.8" fill="var(--down)"/>
<line x1="902.4" y1="273.0" x2="902.4" y2="298.4" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="273.3" width="2.35" height="15.6" fill="var(--up)"/>
<line x1="906.2" y1="219.6" x2="906.2" y2="282.5" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="226.0" width="2.35" height="45.8" fill="var(--up)"/>
<line x1="910.0" y1="219.1" x2="910.0" y2="253.4" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="225.2" width="2.35" height="27.2" fill="var(--down)"/>
<line x1="913.8" y1="244.0" x2="913.8" y2="274.9" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="250.8" width="2.35" height="16.9" fill="var(--down)"/>
<line x1="917.6" y1="259.5" x2="917.6" y2="268.3" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="260.3" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="921.4" y1="255.2" x2="921.4" y2="283.2" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="262.2" width="2.35" height="13.7" fill="var(--down)"/>
<line x1="925.2" y1="242.5" x2="925.2" y2="294.3" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="244.8" width="2.35" height="29.1" fill="var(--up)"/>
<line x1="928.9" y1="242.4" x2="928.9" y2="276.8" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="247.4" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="932.7" y1="251.7" x2="932.7" y2="285.9" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="261.3" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="936.5" y1="248.7" x2="936.5" y2="307.1" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="262.2" width="2.35" height="39.5" fill="var(--down)"/>
<line x1="940.3" y1="301.8" x2="940.3" y2="363.5" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="304.1" width="2.35" height="21.3" fill="var(--down)"/>
<line x1="944.1" y1="290.3" x2="944.1" y2="332.6" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="296.0" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="947.9" y1="273.5" x2="947.9" y2="326.4" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="301.9" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="951.7" y1="284.1" x2="951.7" y2="336.8" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="292.5" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="955.5" y1="274.4" x2="955.5" y2="305.6" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="299.1" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="959.2" y1="294.5" x2="959.2" y2="325.6" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="306.5" width="2.35" height="12.4" fill="var(--down)"/>
<line x1="963.0" y1="293.3" x2="963.0" y2="329.1" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="314.7" width="2.35" height="10.0" fill="var(--down)"/>
<line x1="966.8" y1="296.3" x2="966.8" y2="348.3" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="314.9" width="2.35" height="32.0" fill="var(--down)"/>
<line x1="970.6" y1="328.9" x2="970.6" y2="352.4" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="334.2" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="974.4" y1="310.9" x2="974.4" y2="362.4" stroke="var(--down)" class="wick"/>
<rect x="973.21" y="335.5" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="978.2" y1="261.9" x2="978.2" y2="359.0" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="274.8" width="2.35" height="82.7" fill="var(--up)"/>
<line x1="982.0" y1="231.0" x2="982.0" y2="277.4" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="234.6" width="2.35" height="37.3" fill="var(--up)"/>
<line x1="985.7" y1="217.1" x2="985.7" y2="266.5" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="219.8" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="989.5" y1="175.5" x2="989.5" y2="220.4" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="179.7" width="2.35" height="37.4" fill="var(--up)"/>
<line x1="993.3" y1="175.5" x2="993.3" y2="211.0" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="186.4" width="2.35" height="21.8" fill="var(--down)"/>
<line x1="997.1" y1="145.1" x2="997.1" y2="237.0" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="159.7" width="2.35" height="49.1" fill="var(--up)"/>
<line x1="1000.9" y1="140.9" x2="1000.9" y2="171.9" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="147.9" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="1004.7" y1="80.5" x2="1004.7" y2="159.8" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="124.0" width="2.35" height="30.9" fill="var(--down)"/>
<line x1="1008.5" y1="98.9" x2="1008.5" y2="155.4" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="138.8" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="1012.2" y1="104.9" x2="1012.2" y2="138.0" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="127.7" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="1016.0" y1="125.9" x2="1016.0" y2="187.0" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="125.9" width="2.35" height="27.1" fill="var(--down)"/>
<line x1="1019.8" y1="134.7" x2="1019.8" y2="169.2" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="145.2" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="1023.6" y1="130.5" x2="1023.6" y2="174.4" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="140.3" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="1027.4" y1="127.7" x2="1027.4" y2="258.1" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="128.4" width="2.35" height="111.3" fill="var(--down)"/>
<line x1="1031.2" y1="208.4" x2="1031.2" y2="247.3" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="234.3" width="2.35" height="12.5" fill="var(--down)"/>
<line x1="1035.0" y1="192.8" x2="1035.0" y2="240.6" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="221.4" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="1038.7" y1="204.7" x2="1038.7" y2="236.8" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="214.5" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="1042.5" y1="217.8" x2="1042.5" y2="259.3" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="226.4" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="1046.3" y1="233.5" x2="1046.3" y2="273.9" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="251.3" width="2.35" height="8.8" fill="var(--down)"/>
<line x1="1050.1" y1="263.1" x2="1050.1" y2="274.0" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="265.8" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="60" y1="246.1" x2="1052" y2="246.1" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="249.6" font-size="11.5" fill="var(--resistance)" font-weight="600">$327 R1</text>
<text x="1058" y="261.6" font-size="9.5" fill="var(--muted)">터치 6회</text>
<line x1="60" y1="156.4" x2="1052" y2="156.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="159.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$375 R2</text>
<text x="1058" y="171.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="343.8" x2="1052" y2="343.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="337.8" font-size="11.5" fill="var(--support)" font-weight="600">$274 S1</text>
<text x="1058" y="349.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="362.9" x2="1052" y2="362.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="356.9" font-size="11.5" fill="var(--support)" font-weight="600">$263 S2</text>
<text x="1058" y="368.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="398.1" x2="1052" y2="398.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="392.1" font-size="11.5" fill="var(--support)" font-weight="600">$244 S3</text>
<text x="1058" y="404.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="602.6" x2="1052" y2="602.6" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="596.6" font-size="11.5" fill="var(--support)" font-weight="600">$133 S4 (2022년 저점)</text>
<text x="1058" y="608.6" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="265.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="257.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $316 (2026-08-24)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). 기술적 분석 — 일봉·1년의 레벨(전후 5거래일 기준)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다 — 둘을 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R2 | $375 | 2 | 2025년 7~9월(2025-07-28·2025-09-15, 2분기·3분기 실적 발표 전후) 스윙 고점대 |
| R1 | $327 | 6 | 2024년 3월~2026년 1월(2024-03-18·2024-06-17·2024-12-02·2025-01-20·2025-05-26·2026-01-12)에 걸쳐 6회 반복 등장한 스윙 고점대(6개 레벨 중 최다 터치) |
| **현재가** | **$315.92** (2026-08-24 종가) | — | R1 아래, R1과 S1 사이 |
| S1 | $274 | 2 | 2024-04-29·2025-05-26 스윙 저점대 |
| S2 | $263 | 2 | 2026-02-02·2026-04-06 스윙 저점대 |
| S3 | $244 | 2 | 2024-08-05·2024-10-21 스윙 저점대 |
| S4 (2022년 저점) | $133 | 2 | 2022년 2~5월(2022-02-21·2022-05-09) 형성된 5년 최저치 구간. 현재가에서 58% 이상 떨어져 있어 기본 표시 범위(현재가 기준 상하 3개) 밖이지만, 2022년 금리인상기 성장주 조정의 저점이라는 구조적 의미가 커 `--force-level`로 예외 포함(3. 관측된 특이 구간 — 2022-05-09 금리인상기 성장주 조정 저점 참고) |
| 참고선 | $417 | — | 5년 최고(2026-06-01, ChipStack AI 발표·Samsung Foundry 협력 강화 — 기술적 분석 — 일봉·1년 3-A. 2026-06-01 — ChipStack AI 발표·Samsung Foundry 협력 급등 참고). 2026-07-17 Moonshot Kimi K3 발표發 AI 밸류에이션 우려 급락(기술적 분석 — 일봉·1년 3-B. 2026-07-17 — Moonshot Kimi K3 발표發 AI 밸류에이션 우려 급락) 이후 레짐이 바뀌어 근시일 저항으로 보기 어려움 |

> 표시 기준은 "현재가에서 가까운 순으로 각 방향 3개"다(4. 방법론 · 한계 생성 스크립트 기본값). 저항 쪽은 유효 클러스터가 2개뿐이라 R3 없이 R1·R2만 표시했다 — 억지로 3개를 채우지 않았다. S4($133)는 이 기본값 밖에서 강제로 추가한 예외 레벨.

---

## 3. 관측된 특이 구간 — 2022-05-09 금리인상기 성장주 조정 저점

- 2021년 말부터 미 연준의 공격적 금리인상 사이클이 본격화되며, 고밸류에이션 성장주 전반이 큰 폭으로 조정받았다. Cadence도 예외가 아니어서, 2021-12-27 주간 고점 $192.70에서 2022-05-09 주간 저점 $132.32까지 약 4.5개월간 **-31.3%** 하락했다(주간 종가 기준이 아닌 고가·저가 기준).
- 이후 등락을 거치며 완만하게 회복해 2023-02-13 무렵에야 하락 전 고점($192.70)을 다시 상회했다 — 저점 형성 후 약 9개월 만의 회복으로, 같은 사건에서 약 3개월 만에 회복한 [Synopsys](../synopsys/10_technical_weekly.md)보다 회복 속도가 더뎠다.
- 이 조정은 회사 고유 이슈(실적·사업 리스크)가 아니라 거시 금리 환경에 따른 밸류에이션 디레이팅 성격이 강하다. 기술적 분석 — 일봉·1년 3-A. 2026-06-01 — ChipStack AI 발표·Samsung Foundry 협력 급등·3-B. 2026-07-17 — Moonshot Kimi K3 발표發 AI 밸류에이션 우려 급락의 2026년 AI 서사發 급등락(회사 고유 이벤트라기보다 AI 밸류에이션 서사 변화)과도 원인이 다르므로 혼동하지 말 것.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-23~2026-08-24. 수집 시점: 2026-08-25. 원주가(과거 분할은 소급 반영, 배당은 미반영) — 조사 기간 중 Cadence의 주식분할 이력은 확인되지 않음(기술적 분석 — 일봉·1년 4. 방법론 · 한계와 동일 확인).
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류. 기술적 분석 — 일봉·1년(전후 5거래일)보다 창이 넓어 단기 노이즈보다 다년 구조적 레벨을 잡는다.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산.
- **생성**: `scripts/gen_technical_chart.py CDNS --name "Cadence Design Systems" --interval 1wk --ref-line 416.69:"5년 최고(2026-06-01, ChipStack AI 발표)" --force-level '132.32:(2022년 저점)' --event '2022-05-09:2022 금리인상기 성장주 조정 저점' --close-on 2026-08-24`. 파라미터는 회사 간 비교가 가능하도록 스크립트에 고정돼 있다.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 스크립트 기본값을 그대로 쓴 것이며, 최적화된 값이 아니다.
    - **주봉 레벨은 일봉보다 안정적이지만 고정된 실체는 아니다.** 이번 갱신(기준일 2026-08-14 → 2026-08-24)에서 여섯 레벨의 가격·터치 횟수는 그대로였고 현재가 위치만 바뀌었다 — 반면 같은 갱신에서 일봉 레벨은 재편됐다(기술적 분석 — 일봉·1년 2. 지지선 / 저항선 요약 각주). 창이 5년이라 열흘 정도의 표본 변화에는 둔감할 뿐, 창이 크게 밀리면 주봉 레벨도 달라진다.
    - 5년 구간 안에 연속적인 M&A(OpenEye 2022.9, BETA CAE 2024.5, Hexagon D&E 2026 등, 역사 / 주요 이벤트)로 사업 구조가 점진적으로 바뀌어왔다 — Synopsys의 Ansys 인수처럼 단절적 재편은 아니지만, 오래된 레벨일수록 현재 펀더멘털과의 연관성이 약해질 수 있다.
    - 기술적 분석 — 일봉·1년 3-A. 2026-06-01 — ChipStack AI 발표·Samsung Foundry 협력 급등·3-B. 2026-07-17 — Moonshot Kimi K3 발표發 AI 밸류에이션 우려 급락의 2026년 급등락(AI 서사發)처럼 뉴스 이벤트로 인한 불연속 구간은 통상적인 지지/저항 해석이 적용되기 어렵다 — 참고선($417)을 근시일 저항으로 취급하지 않은 이유이기도 하다.

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-25)*
