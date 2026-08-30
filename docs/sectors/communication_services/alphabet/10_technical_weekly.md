# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 참고 자료. [기술적 분석 — 일봉·1년](./09_technical_daily.md)이 단기 구간을 본다면 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

??? note "이 차트의 데이터 출처와 대조 결과"
    - **출처**: Yahoo Finance 주봉 OHLCV. 이 차트용으로 따로 수집한 값이라 [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다(주봉은 핵심 지표가 다루는 범위 밖이다).
    - **대조 결과**: 마지막 주봉 종가 **2026-08-28 $346.59**는 [핵심 지표](./04_metrics.md)·[밸류에이션 / 적정주가](./06_valuation.md)가 쓰는 기준 종가와 일치한다. 같은 스크립트의 일봉 산출물은 피드 반영 시차로 하루 전인 2026-08-27 $340.65에서 끝나며, 그 사정은 일봉 문서에 적어 뒀다.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-30 ~ 2026-08-28)

<div class="googl-chart">
<style>
.googl-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .googl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .googl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.googl-chart svg { width:100%; height:auto; display:block; }
.googl-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.googl-chart .title { fill: var(--ink); font-weight:600; }
.googl-chart .grid { stroke: var(--grid); stroke-width:1; }
.googl-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Alphabet(GOOGL) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Alphabet (GOOGL) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-30 ~ 2026-08-28 · 마지막 종가 $346.59 (2026-08-28) · 단위 USD</text>
<line x1="60" y1="577.1" x2="1052" y2="577.1" class="grid"/>
<text x="52" y="581.1" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="495.7" x2="1052" y2="495.7" class="grid"/>
<text x="52" y="499.7" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="414.3" x2="1052" y2="414.3" class="grid"/>
<text x="52" y="418.3" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="332.9" x2="1052" y2="332.9" class="grid"/>
<text x="52" y="336.9" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="251.4" x2="1052" y2="251.4" class="grid"/>
<text x="52" y="255.4" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="60" y1="170.0" x2="1052" y2="170.0" class="grid"/>
<text x="52" y="174.0" font-size="11" text-anchor="end" fill="var(--muted)">350</text>
<line x1="60" y1="88.6" x2="1052" y2="88.6" class="grid"/>
<text x="52" y="92.6" font-size="11" text-anchor="end" fill="var(--muted)">400</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="130.0" y1="56.0" x2="130.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="130.0" y1="626.0" x2="130.0" y2="631.0" class="axis"/>
<text x="130.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="326.9" y1="56.0" x2="326.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="326.9" y1="626.0" x2="326.9" y2="631.0" class="axis"/>
<text x="326.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="523.8" y1="56.0" x2="523.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="523.8" y1="626.0" x2="523.8" y2="631.0" class="axis"/>
<text x="523.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="724.5" y1="56.0" x2="724.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="724.5" y1="626.0" x2="724.5" y2="631.0" class="axis"/>
<text x="724.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="921.4" y1="56.0" x2="921.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="921.4" y1="626.0" x2="921.4" y2="631.0" class="axis"/>
<text x="921.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="501.8" x2="61.9" y2="508.1" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="504.8" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="65.7" y1="504.3" x2="65.7" y2="510.8" stroke="var(--down)" class="wick"/>
<rect x="64.51" y="505.8" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="69.5" y1="504.8" x2="69.5" y2="511.2" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="508.8" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="73.3" y1="508.2" x2="73.3" y2="518.0" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="508.4" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="77.0" y1="508.8" x2="77.0" y2="522.5" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="510.7" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="80.8" y1="511.5" x2="80.8" y2="526.6" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="512.3" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="84.6" y1="509.2" x2="84.6" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="509.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="88.4" y1="506.0" x2="88.4" y2="518.4" stroke="var(--down)" class="wick"/>
<rect x="87.22" y="510.2" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="92.2" y1="497.9" x2="92.2" y2="519.5" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="498.9" width="2.35" height="17.1" fill="var(--up)"/>
<line x1="96.0" y1="495.2" x2="96.0" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="497.6" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="99.8" y1="494.7" x2="99.8" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="496.0" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="103.5" y1="494.1" x2="103.5" y2="500.2" stroke="var(--up)" class="wick"/>
<rect x="102.37" y="497.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="107.3" y1="496.0" x2="107.3" y2="509.0" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="496.8" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="111.1" y1="501.7" x2="111.1" y2="511.7" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="505.5" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="114.9" y1="497.2" x2="114.9" y2="511.8" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="499.0" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="118.7" y1="499.0" x2="118.7" y2="510.0" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="499.3" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="122.5" y1="498.6" x2="122.5" y2="513.1" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="500.7" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="126.3" y1="498.4" x2="126.3" y2="504.1" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="500.2" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="130.0" y1="501.4" x2="130.0" y2="518.9" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="503.8" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="133.8" y1="507.4" x2="133.8" y2="523.1" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="512.8" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="137.6" y1="515.3" x2="137.6" y2="528.1" stroke="var(--down)" class="wick"/>
<rect x="136.44" y="518.2" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="141.4" y1="522.8" x2="141.4" y2="537.2" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="522.8" width="2.35" height="12.0" fill="var(--up)"/>
<line x1="145.2" y1="493.2" x2="145.2" y2="524.7" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="506.6" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="149.0" y1="505.1" x2="149.0" y2="522.7" stroke="var(--down)" class="wick"/>
<rect x="147.80" y="505.1" width="2.35" height="16.2" fill="var(--down)"/>
<line x1="152.8" y1="515.1" x2="152.8" y2="528.0" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="523.0" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="156.5" y1="519.7" x2="156.5" y2="536.5" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="521.0" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="160.3" y1="517.8" x2="160.3" y2="527.7" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="523.3" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="164.1" y1="522.1" x2="164.1" y2="535.3" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="525.9" width="2.35" height="2.6" fill="var(--down)"/>
<line x1="167.9" y1="518.1" x2="167.9" y2="536.0" stroke="var(--up)" class="wick"/>
<rect x="166.73" y="518.3" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="171.7" y1="508.7" x2="171.7" y2="521.6" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="509.3" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="175.5" y1="505.8" x2="175.5" y2="514.8" stroke="var(--down)" class="wick"/>
<rect x="174.31" y="510.5" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="179.3" y1="506.0" x2="179.3" y2="523.5" stroke="var(--down)" class="wick"/>
<rect x="178.09" y="511.4" width="2.35" height="11.5" fill="var(--down)"/>
<line x1="183.1" y1="524.9" x2="183.1" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="525.3" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="186.8" y1="526.0" x2="186.8" y2="546.3" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="533.2" width="2.35" height="12.0" fill="var(--down)"/>
<line x1="190.6" y1="539.2" x2="190.6" y2="556.4" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="546.0" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="194.4" y1="539.9" x2="194.4" y2="556.6" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="551.5" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="198.2" y1="548.0" x2="198.2" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="551.0" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="202.0" y1="549.6" x2="202.0" y2="567.7" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="552.8" width="2.35" height="9.8" fill="var(--down)"/>
<line x1="205.8" y1="557.1" x2="205.8" y2="574.1" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="557.1" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="209.6" y1="548.0" x2="209.6" y2="557.5" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="553.5" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="213.3" y1="545.6" x2="213.3" y2="560.3" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="549.9" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="217.1" y1="558.5" x2="217.1" y2="568.9" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="565.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="220.9" y1="547.7" x2="220.9" y2="563.1" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="547.9" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="224.7" y1="546.9" x2="224.7" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="547.4" width="2.35" height="15.5" fill="var(--down)"/>
<line x1="228.5" y1="545.1" x2="228.5" y2="567.8" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="545.6" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="232.3" y1="547.8" x2="232.3" y2="563.5" stroke="var(--down)" class="wick"/>
<rect x="231.10" y="547.8" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="236.1" y1="552.1" x2="236.1" y2="566.6" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="556.6" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="239.8" y1="549.9" x2="239.8" y2="570.5" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="550.6" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="243.6" y1="546.6" x2="243.6" y2="554.8" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="548.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="247.4" y1="541.8" x2="247.4" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="541.8" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="251.2" y1="540.6" x2="251.2" y2="549.8" stroke="var(--down)" class="wick"/>
<rect x="250.03" y="542.7" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="255.0" y1="549.9" x2="255.0" y2="560.5" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="552.4" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="258.8" y1="559.3" x2="258.8" y2="565.3" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="560.9" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="262.6" y1="559.2" x2="262.6" y2="567.7" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="559.8" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="266.4" y1="558.2" x2="266.4" y2="575.6" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="559.2" width="2.35" height="13.3" fill="var(--down)"/>
<line x1="270.1" y1="571.7" x2="270.1" y2="581.3" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="574.3" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="273.9" y1="576.0" x2="273.9" y2="584.4" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="580.2" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="277.7" y1="572.4" x2="277.7" y2="582.8" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="579.3" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="281.5" y1="576.0" x2="281.5" y2="586.3" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="578.8" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="285.3" y1="571.5" x2="285.3" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="575.3" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="289.1" y1="569.3" x2="289.1" y2="590.5" stroke="var(--down)" class="wick"/>
<rect x="287.89" y="574.2" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="292.9" y1="583.6" x2="292.9" y2="604.3" stroke="var(--down)" class="wick"/>
<rect x="291.68" y="584.6" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="296.6" y1="582.1" x2="296.6" y2="598.6" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="583.0" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="300.4" y1="576.9" x2="300.4" y2="586.1" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="581.3" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="304.2" y1="579.2" x2="304.2" y2="586.8" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="581.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="308.0" y1="573.5" x2="308.0" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="576.4" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="311.8" y1="574.9" x2="311.8" y2="589.0" stroke="var(--down)" class="wick"/>
<rect x="310.61" y="578.1" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="315.6" y1="577.9" x2="315.6" y2="594.2" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="589.0" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="319.4" y1="592.5" x2="319.4" y2="599.4" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="593.0" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="323.1" y1="595.2" x2="323.1" y2="600.0" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="595.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="326.9" y1="591.7" x2="326.9" y2="601.8" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="594.1" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="330.7" y1="589.9" x2="330.7" y2="600.2" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="590.0" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="334.5" y1="579.9" x2="334.5" y2="593.3" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="580.4" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="338.3" y1="576.6" x2="338.3" y2="587.3" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="578.2" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="342.1" y1="564.4" x2="342.1" y2="583.0" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="569.4" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="345.9" y1="563.8" x2="345.9" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="344.69" y="573.2" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="349.6" y1="580.9" x2="349.6" y2="589.7" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="585.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="353.4" y1="588.4" x2="353.4" y2="595.7" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="588.5" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="357.2" y1="587.4" x2="357.2" y2="594.5" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="587.5" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="361.0" y1="583.7" x2="361.0" y2="592.8" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="586.9" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="364.8" y1="572.5" x2="364.8" y2="594.4" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="574.5" width="2.35" height="18.8" fill="var(--up)"/>
<line x1="368.6" y1="566.4" x2="368.6" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="568.3" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="372.4" y1="569.4" x2="372.4" y2="577.6" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="569.6" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="376.2" y1="562.2" x2="376.2" y2="574.0" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="563.4" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="379.9" y1="562.6" x2="379.9" y2="570.1" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="562.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="383.7" y1="566.5" x2="383.7" y2="572.1" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="568.3" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="387.5" y1="563.5" x2="387.5" y2="572.9" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="565.2" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="391.3" y1="564.1" x2="391.3" y2="571.1" stroke="var(--down)" class="wick"/>
<rect x="390.12" y="566.0" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="395.1" y1="547.8" x2="395.1" y2="568.7" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="548.6" width="2.35" height="20.1" fill="var(--up)"/>
<line x1="398.9" y1="534.8" x2="398.9" y2="551.1" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="540.1" width="2.35" height="10.8" fill="var(--up)"/>
<line x1="402.7" y1="534.1" x2="402.7" y2="544.8" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="537.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="406.4" y1="534.6" x2="406.4" y2="541.3" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="535.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="410.2" y1="529.8" x2="410.2" y2="542.6" stroke="var(--down)" class="wick"/>
<rect x="409.06" y="538.0" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="414.0" y1="534.6" x2="414.0" y2="542.2" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="538.8" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="417.8" y1="537.1" x2="417.8" y2="546.5" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="539.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="421.6" y1="541.3" x2="421.6" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="543.3" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="425.4" y1="540.3" x2="425.4" y2="547.2" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="545.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="429.2" y1="533.5" x2="429.2" y2="552.1" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="535.7" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="432.9" y1="533.0" x2="432.9" y2="547.5" stroke="var(--down)" class="wick"/>
<rect x="431.77" y="534.9" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="436.7" y1="522.2" x2="436.7" y2="543.0" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="524.1" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="440.5" y1="522.5" x2="440.5" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="439.35" y="523.8" width="2.35" height="7.5" fill="var(--down)"/>
<line x1="444.3" y1="524.9" x2="444.3" y2="531.3" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="529.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="448.1" y1="525.0" x2="448.1" y2="534.2" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="529.3" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="451.9" y1="521.4" x2="451.9" y2="533.9" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="528.5" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="455.7" y1="515.3" x2="455.7" y2="528.1" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="519.1" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="459.5" y1="517.4" x2="459.5" y2="523.5" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="517.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="463.2" y1="514.1" x2="463.2" y2="521.5" stroke="var(--up)" class="wick"/>
<rect x="462.06" y="516.2" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="467.0" y1="513.4" x2="467.0" y2="528.9" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="517.5" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="470.8" y1="521.7" x2="470.8" y2="532.8" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="526.9" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="474.6" y1="515.0" x2="474.6" y2="526.4" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="515.9" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="478.4" y1="510.0" x2="478.4" y2="519.1" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="516.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="482.2" y1="510.8" x2="482.2" y2="520.0" stroke="var(--down)" class="wick"/>
<rect x="480.99" y="515.0" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="486.0" y1="513.0" x2="486.0" y2="544.2" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="520.1" width="2.35" height="21.0" fill="var(--down)"/>
<line x1="489.7" y1="529.1" x2="489.7" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="488.57" y="529.8" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="493.5" y1="523.7" x2="493.5" y2="530.5" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="524.1" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="497.3" y1="516.5" x2="497.3" y2="526.2" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="519.6" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="501.1" y1="512.9" x2="501.1" y2="522.4" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="517.4" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="504.9" y1="514.6" x2="504.9" y2="527.2" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="518.5" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="508.7" y1="514.3" x2="508.7" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="520.2" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="512.5" y1="522.2" x2="512.5" y2="528.8" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="524.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="516.2" y1="508.8" x2="516.2" y2="524.3" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="509.6" width="2.35" height="14.4" fill="var(--up)"/>
<line x1="520.0" y1="507.6" x2="520.0" y2="514.0" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="509.4" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="523.8" y1="512.6" x2="523.8" y2="519.9" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="514.4" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="527.6" y1="503.5" x2="527.6" y2="518.1" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="507.7" width="2.35" height="10.4" fill="var(--up)"/>
<line x1="531.4" y1="501.5" x2="531.4" y2="513.8" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="501.6" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="535.2" y1="490.7" x2="535.2" y2="503.0" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="492.1" width="2.35" height="8.3" fill="var(--up)"/>
<line x1="539.0" y1="489.6" x2="539.0" y2="517.7" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="492.4" width="2.35" height="15.8" fill="var(--down)"/>
<line x1="542.7" y1="496.6" x2="542.7" y2="507.5" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="497.3" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="546.5" y1="496.8" x2="546.5" y2="511.8" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="498.3" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="550.3" y1="503.9" x2="550.3" y2="512.8" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="505.6" width="2.35" height="7.0" fill="var(--up)"/>
<line x1="554.1" y1="508.0" x2="554.1" y2="519.5" stroke="var(--down)" class="wick"/>
<rect x="552.93" y="508.5" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="557.9" y1="515.1" x2="557.9" y2="527.2" stroke="var(--down)" class="wick"/>
<rect x="556.72" y="519.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="561.7" y1="506.2" x2="561.7" y2="518.3" stroke="var(--up)" class="wick"/>
<rect x="560.51" y="510.1" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="565.5" y1="492.2" x2="565.5" y2="502.1" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="494.5" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="569.3" y1="492.0" x2="569.3" y2="499.3" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="494.2" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="573.0" y1="486.4" x2="573.0" y2="496.4" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="491.6" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="576.8" y1="479.1" x2="576.8" y2="491.5" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="483.1" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="580.6" y1="480.7" x2="580.6" y2="492.0" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="481.3" width="2.35" height="7.8" fill="var(--down)"/>
<line x1="584.4" y1="455.5" x2="584.4" y2="494.3" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="460.0" width="2.35" height="28.7" fill="var(--up)"/>
<line x1="588.2" y1="463.9" x2="588.2" y2="475.2" stroke="var(--down)" class="wick"/>
<rect x="587.01" y="464.7" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="592.0" y1="460.3" x2="592.0" y2="469.6" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="465.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="595.8" y1="452.9" x2="595.8" y2="472.9" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="453.3" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="599.5" y1="448.9" x2="599.5" y2="458.3" stroke="var(--down)" class="wick"/>
<rect x="598.37" y="453.1" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="603.3" y1="451.3" x2="603.3" y2="464.1" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="455.9" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="607.1" y1="450.3" x2="607.1" y2="461.3" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="455.9" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="610.9" y1="446.2" x2="610.9" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="452.1" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="614.7" y1="445.5" x2="614.7" y2="456.5" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="447.5" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="618.5" y1="437.0" x2="618.5" y2="449.0" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="443.4" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="622.3" y1="429.2" x2="622.3" y2="444.7" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="429.6" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="626.0" y1="427.7" x2="626.0" y2="439.5" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="430.7" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="629.8" y1="432.7" x2="629.8" y2="452.6" stroke="var(--down)" class="wick"/>
<rect x="628.66" y="438.8" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="633.6" y1="441.0" x2="633.6" y2="472.8" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="445.9" width="2.35" height="22.1" fill="var(--down)"/>
<line x1="637.4" y1="456.2" x2="637.4" y2="471.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="465.0" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="641.2" y1="472.2" x2="641.2" y2="487.7" stroke="var(--up)" class="wick"/>
<rect x="640.02" y="473.5" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="645.0" y1="471.2" x2="645.0" y2="483.2" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="472.3" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="648.8" y1="465.4" x2="648.8" y2="474.0" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="470.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="652.5" y1="467.1" x2="652.5" y2="479.0" stroke="var(--down)" class="wick"/>
<rect x="651.38" y="469.0" width="2.35" height="4.9" fill="var(--down)"/>
<line x1="656.3" y1="476.4" x2="656.3" y2="494.8" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="476.6" width="2.35" height="17.6" fill="var(--down)"/>
<line x1="660.1" y1="482.1" x2="660.1" y2="500.2" stroke="var(--up)" class="wick"/>
<rect x="658.95" y="483.6" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="663.9" y1="473.3" x2="663.9" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="473.6" width="2.35" height="10.2" fill="var(--up)"/>
<line x1="667.7" y1="470.1" x2="667.7" y2="478.3" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="472.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="671.5" y1="464.5" x2="671.5" y2="474.1" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="467.9" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="675.3" y1="465.6" x2="675.3" y2="479.9" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="466.9" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="679.1" y1="466.9" x2="679.1" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="677.88" y="473.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="682.8" y1="470.0" x2="682.8" y2="477.8" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="470.8" width="2.35" height="3.8" fill="var(--up)"/>
<line x1="686.6" y1="443.6" x2="686.6" y2="473.0" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="461.0" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="690.4" y1="445.1" x2="690.4" y2="466.4" stroke="var(--up)" class="wick"/>
<rect x="689.24" y="449.5" width="2.35" height="13.7" fill="var(--up)"/>
<line x1="694.2" y1="442.8" x2="694.2" y2="461.2" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="449.2" width="2.35" height="9.9" fill="var(--down)"/>
<line x1="698.0" y1="448.7" x2="698.0" y2="473.4" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="457.6" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="701.8" y1="463.4" x2="701.8" y2="470.3" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="464.9" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="705.6" y1="453.3" x2="705.6" y2="465.5" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="455.5" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="709.3" y1="421.4" x2="709.3" y2="457.2" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="430.9" width="2.35" height="25.8" fill="var(--up)"/>
<line x1="713.1" y1="412.0" x2="713.1" y2="438.4" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="425.9" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="716.9" y1="419.6" x2="716.9" y2="430.3" stroke="var(--up)" class="wick"/>
<rect x="715.74" y="426.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="720.7" y1="425.3" x2="720.7" y2="434.6" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="427.7" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="724.5" y1="412.7" x2="724.5" y2="430.1" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="424.1" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="728.3" y1="418.8" x2="728.3" y2="434.9" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="420.8" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="732.1" y1="410.6" x2="732.1" y2="422.1" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="413.9" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="735.8" y1="405.4" x2="735.8" y2="429.5" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="407.7" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="739.6" y1="402.8" x2="739.6" y2="441.6" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="413.2" width="2.35" height="25.0" fill="var(--down)"/>
<line x1="743.4" y1="433.5" x2="743.4" y2="443.9" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="434.9" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="747.2" y1="437.2" x2="747.2" y2="448.4" stroke="var(--down)" class="wick"/>
<rect x="746.03" y="437.7" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="751.0" y1="441.8" x2="751.0" y2="468.4" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="443.6" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="754.8" y1="455.0" x2="754.8" y2="470.0" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="456.9" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="758.6" y1="465.7" x2="758.6" y2="477.2" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="466.0" width="2.35" height="4.5" fill="var(--down)"/>
<line x1="762.4" y1="469.2" x2="762.4" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="471.2" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="766.1" y1="462.1" x2="766.1" y2="489.8" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="467.9" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="769.9" y1="482.0" x2="769.9" y2="503.2" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="490.6" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="773.7" y1="480.2" x2="773.7" y2="511.1" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="484.1" width="2.35" height="25.4" fill="var(--up)"/>
<line x1="777.5" y1="476.6" x2="777.5" y2="498.2" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="479.4" width="2.35" height="14.4" fill="var(--down)"/>
<line x1="781.3" y1="469.5" x2="781.3" y2="502.1" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="476.2" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="785.1" y1="471.3" x2="785.1" y2="486.9" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="472.9" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="788.9" y1="470.7" x2="788.9" y2="499.2" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="474.5" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="792.6" y1="464.2" x2="792.6" y2="485.7" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="469.3" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="796.4" y1="452.1" x2="796.4" y2="474.7" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="465.6" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="800.2" y1="454.6" x2="800.2" y2="467.3" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="460.3" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="804.0" y1="455.8" x2="804.0" y2="470.8" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="457.1" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="807.8" y1="445.0" x2="807.8" y2="459.3" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="455.5" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="811.6" y1="451.2" x2="811.6" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="455.4" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="815.4" y1="449.0" x2="815.4" y2="476.2" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="449.3" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="819.1" y1="444.9" x2="819.1" y2="457.4" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="445.6" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="822.9" y1="444.5" x2="822.9" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="446.5" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="826.7" y1="436.4" x2="826.7" y2="447.4" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="438.6" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="830.5" y1="417.6" x2="830.5" y2="436.8" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="425.4" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="834.3" y1="418.2" x2="834.3" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="424.6" width="2.35" height="7.4" fill="var(--down)"/>
<line x1="838.1" y1="410.0" x2="838.1" y2="430.4" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="412.0" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="841.9" y1="403.8" x2="841.9" y2="418.3" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="407.9" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="845.6" y1="400.4" x2="845.6" y2="419.8" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="404.4" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="849.4" y1="390.4" x2="849.4" y2="405.7" stroke="var(--up)" class="wick"/>
<rect x="848.26" y="393.3" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="853.2" y1="356.0" x2="853.2" y2="404.2" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="357.3" width="2.35" height="43.3" fill="var(--up)"/>
<line x1="857.0" y1="345.5" x2="857.0" y2="360.2" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="347.8" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="860.8" y1="323.1" x2="860.8" y2="341.6" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="325.2" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="864.6" y1="323.4" x2="864.6" y2="347.9" stroke="var(--down)" class="wick"/>
<rect x="863.41" y="325.6" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="868.4" y1="331.0" x2="868.4" y2="351.4" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="336.4" width="2.35" height="4.1" fill="var(--down)"/>
<line x1="872.2" y1="330.7" x2="872.2" y2="355.9" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="341.4" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="875.9" y1="321.5" x2="875.9" y2="349.6" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="327.5" width="2.35" height="21.3" fill="var(--up)"/>
<line x1="879.7" y1="313.8" x2="879.7" y2="342.4" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="316.7" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="883.5" y1="265.1" x2="883.5" y2="309.6" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="282.1" width="2.35" height="26.7" fill="var(--up)"/>
<line x1="887.3" y1="270.4" x2="887.3" y2="291.8" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="280.4" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="891.1" y1="264.4" x2="891.1" y2="299.1" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="276.8" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="894.9" y1="241.0" x2="894.9" y2="286.9" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="252.0" width="2.35" height="22.6" fill="var(--up)"/>
<line x1="898.7" y1="204.5" x2="898.7" y2="235.8" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="218.6" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="902.4" y1="213.7" x2="902.4" y2="228.8" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="216.8" width="2.35" height="5.8" fill="var(--up)"/>
<line x1="906.2" y1="216.7" x2="906.2" y2="242.4" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="218.8" width="2.35" height="17.5" fill="var(--down)"/>
<line x1="910.0" y1="232.8" x2="910.0" y2="257.7" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="233.0" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="913.8" y1="226.9" x2="913.8" y2="242.8" stroke="var(--up)" class="wick"/>
<rect x="912.63" y="229.4" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="917.6" y1="214.8" x2="917.6" y2="234.6" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="226.8" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="921.4" y1="201.2" x2="921.4" y2="232.2" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="204.9" width="2.35" height="17.8" fill="var(--up)"/>
<line x1="925.2" y1="185.5" x2="925.2" y2="210.7" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="202.6" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="928.9" y1="194.2" x2="928.9" y2="219.9" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="205.9" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="932.7" y1="182.6" x2="932.7" y2="208.2" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="189.5" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="936.5" y1="171.6" x2="936.5" y2="240.9" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="192.4" width="2.35" height="21.8" fill="var(--down)"/>
<line x1="940.3" y1="206.3" x2="940.3" y2="245.4" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="217.3" width="2.35" height="24.8" fill="var(--down)"/>
<line x1="944.1" y1="224.6" x2="944.1" y2="257.5" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="227.0" width="2.35" height="24.3" fill="var(--up)"/>
<line x1="947.9" y1="219.6" x2="947.9" y2="247.6" stroke="var(--down)" class="wick"/>
<rect x="946.70" y="220.4" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="951.7" y1="237.6" x2="951.7" y2="259.3" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="246.2" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="955.5" y1="232.8" x2="955.5" y2="261.1" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="247.7" width="2.35" height="12.9" fill="var(--up)"/>
<line x1="959.2" y1="231.1" x2="959.2" y2="254.2" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="244.3" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="963.0" y1="241.7" x2="963.0" y2="293.9" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="248.0" width="2.35" height="45.2" fill="var(--down)"/>
<line x1="966.8" y1="250.6" x2="966.8" y2="296.8" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="258.3" width="2.35" height="31.5" fill="var(--up)"/>
<line x1="970.6" y1="215.5" x2="970.6" y2="259.3" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="223.4" width="2.35" height="34.8" fill="var(--up)"/>
<line x1="974.4" y1="182.5" x2="974.4" y2="226.2" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="183.5" width="2.35" height="40.0" fill="var(--up)"/>
<line x1="978.2" y1="177.7" x2="978.2" y2="200.4" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="179.1" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="982.0" y1="110.1" x2="982.0" y2="181.8" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="111.9" width="2.35" height="64.7" fill="var(--up)"/>
<line x1="985.7" y1="85.3" x2="985.7" y2="121.5" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="87.3" width="2.35" height="24.7" fill="var(--up)"/>
<line x1="989.5" y1="82.5" x2="989.5" y2="116.6" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="93.8" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="993.3" y1="74.5" x2="993.3" y2="118.3" stroke="var(--down)" class="wick"/>
<rect x="992.14" y="95.6" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="997.1" y1="98.5" x2="997.1" y2="123.7" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="113.8" width="2.35" height="6.8" fill="var(--down)"/>
<line x1="1000.9" y1="123.5" x2="1000.9" y2="156.8" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="126.8" width="2.35" height="13.0" fill="var(--down)"/>
<line x1="1004.7" y1="134.0" x2="1004.7" y2="175.9" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="145.3" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="1008.5" y1="127.7" x2="1008.5" y2="155.9" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="140.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1012.2" y1="155.5" x2="1012.2" y2="202.2" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="157.1" width="2.35" height="33.5" fill="var(--down)"/>
<line x1="1016.0" y1="146.9" x2="1016.0" y2="185.2" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="153.9" width="2.35" height="29.4" fill="var(--up)"/>
<line x1="1019.8" y1="132.3" x2="1019.8" y2="168.2" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="151.2" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="1023.6" y1="128.8" x2="1023.6" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="1022.43" y="159.9" width="2.35" height="15.3" fill="var(--down)"/>
<line x1="1027.4" y1="154.2" x2="1027.4" y2="227.2" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="168.6" width="2.35" height="50.7" fill="var(--down)"/>
<line x1="1031.2" y1="156.0" x2="1031.2" y2="211.6" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="160.0" width="2.35" height="50.6" fill="var(--up)"/>
<line x1="1035.0" y1="113.8" x2="1035.0" y2="163.8" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="144.8" width="2.35" height="18.2" fill="var(--down)"/>
<line x1="1038.7" y1="157.6" x2="1038.7" y2="184.9" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="161.6" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="1042.5" y1="174.5" x2="1042.5" y2="188.6" stroke="var(--down)" class="wick"/>
<rect x="1041.36" y="176.1" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="1046.3" y1="167.4" x2="1046.3" y2="188.7" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="180.4" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="1050.1" y1="171.4" x2="1050.1" y2="185.8" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="175.6" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="60" y1="528.5" x2="1052" y2="528.5" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="522.5" font-size="11.5" fill="var(--support)" font-weight="600">$130 S1</text>
<text x="1058" y="534.5" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="572.3" x2="1052" y2="572.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="566.3" font-size="11.5" fill="var(--support)" font-weight="600">$103 S2</text>
<text x="1058" y="578.3" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="603.0" x2="1052" y2="603.0" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="597.0" font-size="11.5" fill="var(--support)" font-weight="600">$84 S3</text>
<text x="1058" y="609.0" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="175.6" r="3" fill="var(--ink)"/>
<text x="1046.0" y="167.6" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $347 (2026-08-28)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고). **기술적 분석 — 일봉·1년의 레벨(전후 5거래일)과는 탐지 창 자체가 달라 값이 다르게 나오는 게 정상이다** — 같은 방법론의 다른 배율로 혼동하지 말 것.

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| **현재가** | **$346.59** (2026-08-28 종가) | — | 기간 내 상단 저항 없음(신고가 구간) — 가장 가까운 지지는 S1 |
| S1 | $130 | 3 | 2021년 10월 고점과 2023년 말~2024년 초 저점이 겹치는 구간(2021-10-04·2023-12-04·2024-03-04) — 현재가의 40% 미만 수준 |
| S2 | $103 | 2 | 2022년 상반기 하락장 저점대(2022-05-23·2022-07-25) |
| S3 | $84 | 2 | 2022년 10월~2023년 1월 바닥권(2022-10-31·2023-01-02) — 5년 최저 $83.34 부근 |
| 참고선 | $408.61 | — | 최근 5년 최고가. 현재가 바로 위이지만 터치가 1회뿐이라 클러스터에서 제외됐다 |
| 참고선 | $83.34 | — | 최근 5년 최저가(2022년 하락장). 분할 소급 반영 기준이며 현재 사업 구조와 무관한 수준이다 |

> **저항 클러스터가 하나도 잡히지 않았다.** 현재가가 5년 구간의 신고가권이라 위쪽에 터치 2회 이상인 스윙 고점대가 존재하지 않기 때문이며, `--force-level`로 억지로 만들지 않았다. 반대로 잡힌 지지 3개는 전부 2021~2024년 값이라 현재가의 24~38% 수준에 불과하다 — **실질적으로 이 표는 "5년 관점에서 참고할 지지가 없다"는 뜻이고, 근시일 지지는 일봉 문서의 S1($311)·S2($295)를 봐야 한다.**

---

## 3. 관측된 특이 구간 — 2025년 9월 반독점 구제안 발표 후 재평가

- 2025년 9월 미 연방법원이 검색 독점 사건의 구제안에서 **Chrome·Android 강제 매각을 기각**하고 행태적 구제만 부과하자, 2020년 소 제기 이후 5년간 주가를 눌러 온 "분할 리스크"가 크게 걷혔다([역사 / 주요 이벤트](./02_history.md) 참고).
- 발표 직후 주간 종가 기준 전주 대비 **+10.4%** ($212.91 → $235.00)였고, 발표 다음 거래일 하루에만 1억 주가 넘게 거래됐다(평소 주간 거래량의 3배 수준).
- 이후 레짐이 완전히 바뀌었다 — 2025년 8월 말 $206대에서 2026년 2월 $349, 7월 $408대까지 11개월 만에 두 배가 됐다. 그 결과 **2021~2024년에 형성된 스윙 레벨은 전부 현재가의 절반 이하로 남겨졌고**, 위 2절에서 지지선을 참고용으로만 처리한 이유가 된다. 2026년 들어서는 반독점이 아니라 AI CapEx 규모가 주가의 주된 변수로 바뀌었다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-30~2026-08-28. 수집 시점: 2026-08-30. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시(예외는 §2 비고).
- **생성**: `scripts/gen_technical_chart.py GOOGL --name Alphabet --interval 1wk --emit all` (기본 옵션 — `--close-on`·`--force-level`·`--event`·`--ref-line` 미사용, 수집일 2026-08-30)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **5년 구간 안에서 회사의 손익 구조가 크게 바뀌었다.** 2021년에는 사실상 광고 단일 사업에 클라우드가 적자였던 반면, 2026년 2분기 클라우드는 매출의 20.7%·부문 영업이익률 35.6%를 차지한다. 여기에 2026년 CapEx가 연 $200B 규모로 뛰며 현금흐름 구조도 단절됐다 — 2022~2023년 저점대 레벨을 현재 펀더멘털과 연결해 해석하지 말 것.
    - **기간 내 주식분할이 있다.** 2022-07-18 20:1 분할이 이 창 안에 있으며, 원자료는 분할을 **소급 반영한** 값이다(따라서 차트에 분할 시점의 단절이 나타나지 않는다). 배당은 9회 있었으나 원주가라 반영되지 않았다.

---

*작성일: 2026-08-30*
