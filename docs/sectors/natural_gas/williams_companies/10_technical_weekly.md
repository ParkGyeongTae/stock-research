# 기술적 분석 (주봉 캔들차트 · 5년 지지/저항)

> 최근 5년 주봉 가격 흐름을 지지선·저항선과 함께 정리한 기술적(가격 패턴) 참고 자료. [`09_technical_daily.md`](./09_technical_daily.md)(일봉·1년)가 단기 구간을 보여준다면, 이 문서는 여러 사이클에 걸친 구조적 레벨을 본다. **이 문서는 과거 가격 패턴에 대한 객관적 서술이며, 매수/매도 신호나 목표가 예측이 아니다** — 펀더멘털 기반 적정주가 판단은 [`06_valuation.md`](./06_valuation.md), 투자 결론은 [`07_investment.md`](./07_investment.md)를 따로 참고할 것.

> ⚠️ 이 문서의 가격 데이터는 `04_metrics.md`의 원자료 표와는 별도로, 이 차트 작성을 위해 주봉 API에서 직접 수집한 것이다. 가장 가까운 주봉 종가(2026-08-21 기준 최근 주) $70.60은 [`04_metrics.md`](./04_metrics.md)·[`06_valuation.md`](./06_valuation.md)의 2026-08-21 종가 $70.13과 약 0.7% 차이가 있다 — [`09_technical_daily.md`](./09_technical_daily.md)에서 설명한 것과 같은 통상적인 데이터 제공처 간 오차 범위.
>
> ⚠️ 5년 조사 기간(2021-08~2026-08) 동안 EQT처럼 자본구조가 단절적으로 바뀐 M&A는 없었다(`04_metrics.md` 상단 각주 참고) — 다만 2025.07 CEO 교체, Power Innovation(데이터센터向 전력) 신사업 등장 등 사업 구성 자체는 이 기간 동안 점진적으로 바뀌어왔다(`02_history.md`). 5년 전 형성된 하단 지지 레벨(S3 등)은 순수 파이프라인 사업 시기의 가격대라는 점을 감안해서 볼 것.

---

## 1. 차트 — 최근 5년 주봉 (2021-08-23 ~ 2026-08-21)

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
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Williams Companies(WMB) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Williams Companies (WMB) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 $70.60 (2026-08-21) · 단위 USD</text>
<line x1="60" y1="550.0" x2="1052" y2="550.0" class="grid"/>
<text x="52" y="554.0" font-size="11" text-anchor="end" fill="var(--muted)">30</text>
<line x1="60" y1="455.0" x2="1052" y2="455.0" class="grid"/>
<text x="52" y="459.0" font-size="11" text-anchor="end" fill="var(--muted)">40</text>
<line x1="60" y1="360.0" x2="1052" y2="360.0" class="grid"/>
<text x="52" y="364.0" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="265.0" x2="1052" y2="265.0" class="grid"/>
<text x="52" y="269.0" font-size="11" text-anchor="end" fill="var(--muted)">60</text>
<line x1="60" y1="170.0" x2="1052" y2="170.0" class="grid"/>
<text x="52" y="174.0" font-size="11" text-anchor="end" fill="var(--muted)">70</text>
<line x1="60" y1="75.0" x2="1052" y2="75.0" class="grid"/>
<text x="52" y="79.0" font-size="11" text-anchor="end" fill="var(--muted)">80</text>
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
<line x1="61.9" y1="599.0" x2="61.9" y2="605.7" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="601.2" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="65.7" y1="595.9" x2="65.7" y2="602.8" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="597.8" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="69.5" y1="595.8" x2="69.5" y2="607.2" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="598.8" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="73.3" y1="589.7" x2="73.3" y2="602.2" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="594.8" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="77.0" y1="591.7" x2="77.0" y2="601.1" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="593.7" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="80.8" y1="582.2" x2="80.8" y2="590.5" stroke="var(--up)" class="wick"/>
<rect x="79.65" y="584.2" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="84.6" y1="565.7" x2="84.6" y2="581.9" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="566.0" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="88.4" y1="552.4" x2="88.4" y2="564.7" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="554.3" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="92.2" y1="551.0" x2="92.2" y2="565.6" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="552.5" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="96.0" y1="559.6" x2="96.0" y2="569.6" stroke="var(--down)" class="wick"/>
<rect x="94.80" y="561.5" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="99.8" y1="560.2" x2="99.8" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="563.7" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="103.5" y1="559.5" x2="103.5" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="562.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="107.3" y1="561.2" x2="107.3" y2="575.0" stroke="var(--down)" class="wick"/>
<rect x="106.15" y="562.9" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="111.1" y1="563.5" x2="111.1" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="566.7" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="114.9" y1="562.7" x2="114.9" y2="582.9" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="563.5" width="2.35" height="14.0" fill="var(--down)"/>
<line x1="118.7" y1="568.7" x2="118.7" y2="585.5" stroke="var(--down)" class="wick"/>
<rect x="117.51" y="574.2" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="122.5" y1="582.5" x2="122.5" y2="594.0" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="583.4" width="2.35" height="6.6" fill="var(--down)"/>
<line x1="126.3" y1="587.8" x2="126.3" y2="598.8" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="589.4" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="130.0" y1="584.2" x2="130.0" y2="591.6" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="587.6" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="133.8" y1="568.4" x2="133.8" y2="587.8" stroke="var(--up)" class="wick"/>
<rect x="132.66" y="568.9" width="2.35" height="17.9" fill="var(--up)"/>
<line x1="137.6" y1="555.5" x2="137.6" y2="572.4" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="556.7" width="2.35" height="11.5" fill="var(--up)"/>
<line x1="141.4" y1="551.5" x2="141.4" y2="566.0" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="555.0" width="2.35" height="6.7" fill="var(--down)"/>
<line x1="145.2" y1="550.8" x2="145.2" y2="575.5" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="553.4" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="149.0" y1="541.3" x2="149.0" y2="557.3" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="544.5" width="2.35" height="10.1" fill="var(--up)"/>
<line x1="152.8" y1="540.3" x2="152.8" y2="550.0" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="543.3" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="156.5" y1="543.0" x2="156.5" y2="556.6" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="543.3" width="2.35" height="10.4" fill="var(--down)"/>
<line x1="160.3" y1="542.9" x2="160.3" y2="560.1" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="542.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="164.1" y1="516.5" x2="164.1" y2="546.3" stroke="var(--up)" class="wick"/>
<rect x="162.95" y="517.0" width="2.35" height="28.3" fill="var(--up)"/>
<line x1="167.9" y1="508.3" x2="167.9" y2="533.1" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="514.6" width="2.35" height="17.4" fill="var(--down)"/>
<line x1="171.7" y1="532.2" x2="171.7" y2="546.6" stroke="var(--down)" class="wick"/>
<rect x="170.52" y="535.0" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="175.5" y1="512.9" x2="175.5" y2="533.3" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="513.1" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="179.3" y1="511.8" x2="179.3" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="513.6" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="183.1" y1="507.1" x2="183.1" y2="522.9" stroke="var(--up)" class="wick"/>
<rect x="181.88" y="508.0" width="2.35" height="4.0" fill="var(--up)"/>
<line x1="186.8" y1="494.9" x2="186.8" y2="513.0" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="497.6" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="190.6" y1="489.5" x2="190.6" y2="502.4" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="496.9" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="194.4" y1="501.8" x2="194.4" y2="521.3" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="508.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="198.2" y1="483.0" x2="198.2" y2="514.1" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="486.6" width="2.35" height="23.6" fill="var(--up)"/>
<line x1="202.0" y1="491.3" x2="202.0" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="492.8" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="205.8" y1="491.4" x2="205.8" y2="507.5" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="498.9" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="209.6" y1="477.8" x2="209.6" y2="498.7" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="479.1" width="2.35" height="16.9" fill="var(--up)"/>
<line x1="213.3" y1="474.3" x2="213.3" y2="487.7" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="476.8" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="217.1" y1="474.9" x2="217.1" y2="506.2" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="477.3" width="2.35" height="26.2" fill="var(--down)"/>
<line x1="220.9" y1="510.7" x2="220.9" y2="559.3" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="511.6" width="2.35" height="40.9" fill="var(--down)"/>
<line x1="224.7" y1="539.4" x2="224.7" y2="551.9" stroke="var(--down)" class="wick"/>
<rect x="223.53" y="546.9" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="228.5" y1="529.0" x2="228.5" y2="547.9" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="537.7" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="232.3" y1="533.8" x2="232.3" y2="558.9" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="537.5" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="236.1" y1="532.1" x2="236.1" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="536.9" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="239.8" y1="522.5" x2="239.8" y2="536.7" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="527.8" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="243.6" y1="508.8" x2="243.6" y2="529.0" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="511.1" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="247.4" y1="508.9" x2="247.4" y2="536.7" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="514.2" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="251.2" y1="510.1" x2="251.2" y2="528.9" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="510.5" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="255.0" y1="498.9" x2="255.0" y2="521.4" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="503.2" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="258.8" y1="495.0" x2="258.8" y2="507.7" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="502.2" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="262.6" y1="496.8" x2="262.6" y2="520.7" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="502.5" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="266.4" y1="512.0" x2="266.4" y2="535.0" stroke="var(--down)" class="wick"/>
<rect x="265.18" y="512.7" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="270.1" y1="512.7" x2="270.1" y2="537.5" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="520.6" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="273.9" y1="526.6" x2="273.9" y2="561.2" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="539.5" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="277.7" y1="554.7" x2="277.7" y2="566.2" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="560.0" width="2.35" height="3.0" fill="var(--down)"/>
<line x1="281.5" y1="542.2" x2="281.5" y2="556.8" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="552.0" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="285.3" y1="543.5" x2="285.3" y2="559.9" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="551.0" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="289.1" y1="533.3" x2="289.1" y2="553.0" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="535.6" width="2.35" height="16.2" fill="var(--up)"/>
<line x1="292.9" y1="522.5" x2="292.9" y2="541.2" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="524.6" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="296.6" y1="513.5" x2="296.6" y2="526.7" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="516.4" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="300.4" y1="509.7" x2="300.4" y2="525.4" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="511.2" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="304.2" y1="507.0" x2="304.2" y2="525.4" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="511.2" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="308.0" y1="509.1" x2="308.0" y2="527.8" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="512.9" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="311.8" y1="498.1" x2="311.8" y2="519.7" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="502.9" width="2.35" height="15.5" fill="var(--up)"/>
<line x1="315.6" y1="500.4" x2="315.6" y2="526.2" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="501.0" width="2.35" height="24.4" fill="var(--down)"/>
<line x1="319.4" y1="510.2" x2="319.4" y2="532.8" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="524.2" width="2.35" height="3.5" fill="var(--down)"/>
<line x1="323.1" y1="517.6" x2="323.1" y2="532.2" stroke="var(--up)" class="wick"/>
<rect x="321.97" y="518.5" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="326.9" y1="516.4" x2="326.9" y2="525.5" stroke="var(--down)" class="wick"/>
<rect x="325.76" y="517.8" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="330.7" y1="522.3" x2="330.7" y2="533.8" stroke="var(--down)" class="wick"/>
<rect x="329.54" y="524.3" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="334.5" y1="520.8" x2="334.5" y2="531.6" stroke="var(--down)" class="wick"/>
<rect x="333.33" y="522.2" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="338.3" y1="520.7" x2="338.3" y2="537.0" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="521.9" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="342.1" y1="525.8" x2="342.1" y2="545.2" stroke="var(--down)" class="wick"/>
<rect x="340.90" y="534.2" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="345.9" y1="526.8" x2="345.9" y2="540.4" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="530.2" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="349.6" y1="528.8" x2="349.6" y2="538.4" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="530.8" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="353.4" y1="527.1" x2="353.4" y2="538.8" stroke="var(--down)" class="wick"/>
<rect x="352.26" y="534.0" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="357.2" y1="537.6" x2="357.2" y2="545.5" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="538.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="361.0" y1="538.3" x2="361.0" y2="552.1" stroke="var(--down)" class="wick"/>
<rect x="359.83" y="540.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="364.8" y1="540.3" x2="364.8" y2="562.3" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="542.3" width="2.35" height="18.1" fill="var(--down)"/>
<line x1="368.6" y1="553.0" x2="368.6" y2="568.4" stroke="var(--down)" class="wick"/>
<rect x="367.41" y="564.2" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="372.4" y1="556.2" x2="372.4" y2="570.9" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="562.0" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="376.2" y1="551.1" x2="376.2" y2="566.5" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="551.3" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="379.9" y1="546.1" x2="379.9" y2="556.7" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="547.1" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="383.7" y1="542.6" x2="383.7" y2="554.7" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="546.3" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="387.5" y1="544.6" x2="387.5" y2="554.5" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="545.2" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="391.3" y1="545.8" x2="391.3" y2="557.3" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="547.5" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="395.1" y1="545.2" x2="395.1" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="548.3" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="398.9" y1="545.4" x2="398.9" y2="561.8" stroke="var(--down)" class="wick"/>
<rect x="397.70" y="545.8" width="2.35" height="11.0" fill="var(--down)"/>
<line x1="402.7" y1="554.8" x2="402.7" y2="564.0" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="556.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="406.4" y1="553.8" x2="406.4" y2="563.0" stroke="var(--down)" class="wick"/>
<rect x="405.27" y="557.7" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="410.2" y1="545.0" x2="410.2" y2="566.4" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="547.8" width="2.35" height="16.4" fill="var(--up)"/>
<line x1="414.0" y1="533.7" x2="414.0" y2="551.3" stroke="var(--down)" class="wick"/>
<rect x="412.84" y="544.3" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="417.8" y1="540.6" x2="417.8" y2="549.0" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="545.0" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="421.6" y1="540.1" x2="421.6" y2="547.7" stroke="var(--up)" class="wick"/>
<rect x="420.41" y="544.4" width="2.35" height="1.1" fill="var(--up)"/>
<line x1="425.4" y1="523.8" x2="425.4" y2="544.4" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="525.0" width="2.35" height="19.1" fill="var(--up)"/>
<line x1="429.2" y1="521.0" x2="429.2" y2="529.1" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="524.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="432.9" y1="509.2" x2="432.9" y2="525.9" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="517.9" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="436.7" y1="512.3" x2="436.7" y2="521.8" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="513.4" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="440.5" y1="508.1" x2="440.5" y2="514.9" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="511.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="444.3" y1="501.8" x2="444.3" y2="518.9" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="508.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="448.1" y1="498.1" x2="448.1" y2="512.0" stroke="var(--up)" class="wick"/>
<rect x="446.92" y="498.9" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="451.9" y1="498.5" x2="451.9" y2="509.4" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="498.8" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="455.7" y1="501.2" x2="455.7" y2="510.5" stroke="var(--down)" class="wick"/>
<rect x="454.49" y="504.2" width="2.35" height="1.4" fill="var(--down)"/>
<line x1="459.5" y1="501.5" x2="459.5" y2="507.0" stroke="var(--down)" class="wick"/>
<rect x="458.28" y="504.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="463.2" y1="503.7" x2="463.2" y2="516.3" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="505.3" width="2.35" height="8.4" fill="var(--down)"/>
<line x1="467.0" y1="504.0" x2="467.0" y2="516.3" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="508.8" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="470.8" y1="505.4" x2="470.8" y2="518.1" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="507.4" width="2.35" height="8.2" fill="var(--down)"/>
<line x1="474.6" y1="505.7" x2="474.6" y2="516.8" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="514.9" width="2.35" height="1.6" fill="var(--up)"/>
<line x1="478.4" y1="513.0" x2="478.4" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="515.0" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="482.2" y1="498.7" x2="482.2" y2="511.7" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="500.7" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="486.0" y1="490.9" x2="486.0" y2="504.6" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="498.6" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="489.7" y1="502.0" x2="489.7" y2="513.0" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="505.6" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="493.5" y1="491.0" x2="493.5" y2="514.6" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="492.2" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="497.3" y1="490.0" x2="497.3" y2="505.3" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="490.5" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="501.1" y1="495.2" x2="501.1" y2="506.0" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="498.4" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="504.9" y1="488.3" x2="504.9" y2="499.5" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="490.0" width="2.35" height="8.0" fill="var(--up)"/>
<line x1="508.7" y1="479.2" x2="508.7" y2="491.8" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="480.8" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="512.5" y1="480.5" x2="512.5" y2="506.0" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="483.5" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="516.2" y1="498.1" x2="516.2" y2="511.9" stroke="var(--down)" class="wick"/>
<rect x="515.07" y="498.5" width="2.35" height="7.6" fill="var(--down)"/>
<line x1="520.0" y1="498.9" x2="520.0" y2="506.7" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="501.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="523.8" y1="498.9" x2="523.8" y2="505.0" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="500.3" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="527.6" y1="486.4" x2="527.6" y2="503.1" stroke="var(--up)" class="wick"/>
<rect x="526.43" y="497.3" width="2.35" height="5.7" fill="var(--up)"/>
<line x1="531.4" y1="496.1" x2="531.4" y2="508.4" stroke="var(--down)" class="wick"/>
<rect x="530.22" y="500.6" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="535.2" y1="503.1" x2="535.2" y2="516.9" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="504.2" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="539.0" y1="503.4" x2="539.0" y2="515.2" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="503.7" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="542.7" y1="498.8" x2="542.7" y2="509.6" stroke="var(--down)" class="wick"/>
<rect x="541.57" y="504.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="546.5" y1="505.3" x2="546.5" y2="513.4" stroke="var(--down)" class="wick"/>
<rect x="545.36" y="506.7" width="2.35" height="5.0" fill="var(--down)"/>
<line x1="550.3" y1="505.4" x2="550.3" y2="524.8" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="509.1" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="554.1" y1="499.7" x2="554.1" y2="513.4" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="503.1" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="557.9" y1="489.1" x2="557.9" y2="506.8" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="489.2" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="561.7" y1="482.5" x2="561.7" y2="495.5" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="489.2" width="2.35" height="3.3" fill="var(--down)"/>
<line x1="565.5" y1="480.1" x2="565.5" y2="494.0" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="483.5" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="569.3" y1="466.8" x2="569.3" y2="485.0" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="471.6" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="573.0" y1="463.6" x2="573.0" y2="474.2" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="464.8" width="2.35" height="6.0" fill="var(--up)"/>
<line x1="576.8" y1="457.3" x2="576.8" y2="468.6" stroke="var(--up)" class="wick"/>
<rect x="575.65" y="462.3" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="580.6" y1="460.5" x2="580.6" y2="474.9" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="461.4" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="584.4" y1="468.7" x2="584.4" y2="481.8" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="469.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="588.2" y1="459.6" x2="588.2" y2="473.1" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="462.0" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="592.0" y1="459.2" x2="592.0" y2="476.9" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="460.6" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="595.8" y1="455.1" x2="595.8" y2="468.0" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="458.4" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="599.5" y1="442.2" x2="599.5" y2="459.1" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="442.9" width="2.35" height="14.5" fill="var(--up)"/>
<line x1="603.3" y1="437.0" x2="603.3" y2="456.1" stroke="var(--down)" class="wick"/>
<rect x="602.15" y="442.6" width="2.35" height="11.2" fill="var(--down)"/>
<line x1="607.1" y1="440.2" x2="607.1" y2="454.4" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="440.7" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="610.9" y1="439.3" x2="610.9" y2="449.4" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="441.1" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="614.7" y1="438.1" x2="614.7" y2="446.2" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="443.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="618.5" y1="424.6" x2="618.5" y2="446.3" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="435.4" width="2.35" height="9.2" fill="var(--up)"/>
<line x1="622.3" y1="424.4" x2="622.3" y2="437.2" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="431.2" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="626.0" y1="426.1" x2="626.0" y2="435.2" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="429.4" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="629.8" y1="424.5" x2="629.8" y2="436.2" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="426.7" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="633.6" y1="415.3" x2="633.6" y2="433.6" stroke="var(--up)" class="wick"/>
<rect x="632.44" y="417.0" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="637.4" y1="406.6" x2="637.4" y2="438.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="416.0" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="641.2" y1="421.8" x2="641.2" y2="439.0" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="429.9" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="645.0" y1="414.2" x2="645.0" y2="451.1" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="424.0" width="2.35" height="21.5" fill="var(--up)"/>
<line x1="648.8" y1="414.5" x2="648.8" y2="428.5" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="415.8" width="2.35" height="8.7" fill="var(--up)"/>
<line x1="652.5" y1="404.2" x2="652.5" y2="417.4" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="404.7" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="656.3" y1="399.8" x2="656.3" y2="410.8" stroke="var(--up)" class="wick"/>
<rect x="655.16" y="400.2" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="660.1" y1="400.9" x2="660.1" y2="416.1" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="403.1" width="2.35" height="11.4" fill="var(--down)"/>
<line x1="663.9" y1="403.9" x2="663.9" y2="417.2" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="407.2" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="667.7" y1="399.7" x2="667.7" y2="412.2" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="403.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="671.5" y1="393.4" x2="671.5" y2="411.7" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="403.3" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="675.3" y1="363.1" x2="675.3" y2="409.6" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="363.5" width="2.35" height="42.6" fill="var(--up)"/>
<line x1="679.1" y1="355.0" x2="679.1" y2="374.2" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="355.4" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="682.8" y1="336.8" x2="682.8" y2="357.6" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="337.6" width="2.35" height="18.7" fill="var(--up)"/>
<line x1="686.6" y1="332.9" x2="686.6" y2="343.9" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="336.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="690.4" y1="333.0" x2="690.4" y2="346.1" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="341.0" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="694.2" y1="295.4" x2="694.2" y2="345.9" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="300.1" width="2.35" height="44.5" fill="var(--up)"/>
<line x1="698.0" y1="290.4" x2="698.0" y2="310.6" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="296.4" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="701.8" y1="261.6" x2="701.8" y2="296.8" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="268.3" width="2.35" height="26.0" fill="var(--up)"/>
<line x1="705.6" y1="265.9" x2="705.6" y2="294.1" stroke="var(--down)" class="wick"/>
<rect x="704.38" y="266.8" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="709.3" y1="277.4" x2="709.3" y2="307.6" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="278.3" width="2.35" height="16.6" fill="var(--down)"/>
<line x1="713.1" y1="293.5" x2="713.1" y2="320.7" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="294.3" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="716.9" y1="318.0" x2="716.9" y2="342.0" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="318.2" width="2.35" height="8.6" fill="var(--down)"/>
<line x1="720.7" y1="315.9" x2="720.7" y2="334.1" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="322.6" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="724.5" y1="294.5" x2="724.5" y2="329.3" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="297.3" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="728.3" y1="291.1" x2="728.3" y2="310.0" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="293.3" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="732.1" y1="268.8" x2="732.1" y2="307.9" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="273.2" width="2.35" height="33.9" fill="var(--up)"/>
<line x1="735.8" y1="251.1" x2="735.8" y2="278.8" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="269.1" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="739.6" y1="285.2" x2="739.6" y2="331.1" stroke="var(--down)" class="wick"/>
<rect x="738.46" y="285.4" width="2.35" height="23.0" fill="var(--down)"/>
<line x1="743.4" y1="289.8" x2="743.4" y2="316.3" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="303.6" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="747.2" y1="284.9" x2="747.2" y2="329.9" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="293.7" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="751.0" y1="273.1" x2="751.0" y2="294.3" stroke="var(--up)" class="wick"/>
<rect x="749.82" y="289.3" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="754.8" y1="278.4" x2="754.8" y2="316.4" stroke="var(--up)" class="wick"/>
<rect x="753.60" y="282.3" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="758.6" y1="274.1" x2="758.6" y2="333.5" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="279.3" width="2.35" height="39.0" fill="var(--down)"/>
<line x1="762.4" y1="286.3" x2="762.4" y2="328.7" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="290.9" width="2.35" height="31.5" fill="var(--up)"/>
<line x1="766.1" y1="266.1" x2="766.1" y2="292.9" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="268.8" width="2.35" height="22.1" fill="var(--up)"/>
<line x1="769.9" y1="249.1" x2="769.9" y2="277.6" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="264.4" width="2.35" height="8.3" fill="var(--down)"/>
<line x1="773.7" y1="249.3" x2="773.7" y2="326.3" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="277.3" width="2.35" height="39.2" fill="var(--down)"/>
<line x1="777.5" y1="289.4" x2="777.5" y2="345.0" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="299.3" width="2.35" height="35.6" fill="var(--up)"/>
<line x1="781.3" y1="264.9" x2="781.3" y2="295.9" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="278.1" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="785.1" y1="264.0" x2="785.1" y2="307.2" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="274.2" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="788.9" y1="264.1" x2="788.9" y2="287.8" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="265.0" width="2.35" height="10.9" fill="var(--up)"/>
<line x1="792.6" y1="261.1" x2="792.6" y2="294.8" stroke="var(--down)" class="wick"/>
<rect x="791.47" y="269.4" width="2.35" height="17.9" fill="var(--down)"/>
<line x1="796.4" y1="273.1" x2="796.4" y2="299.0" stroke="var(--down)" class="wick"/>
<rect x="795.25" y="276.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="800.2" y1="272.9" x2="800.2" y2="291.4" stroke="var(--up)" class="wick"/>
<rect x="799.04" y="274.6" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="804.0" y1="256.7" x2="804.0" y2="269.8" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="260.2" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="807.8" y1="251.2" x2="807.8" y2="266.1" stroke="var(--down)" class="wick"/>
<rect x="806.61" y="254.0" width="2.35" height="5.7" fill="var(--down)"/>
<line x1="811.6" y1="258.3" x2="811.6" y2="279.4" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="260.1" width="2.35" height="7.0" fill="var(--down)"/>
<line x1="815.4" y1="258.7" x2="815.4" y2="282.1" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="260.3" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="819.1" y1="234.8" x2="819.1" y2="264.9" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="239.6" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="822.9" y1="232.2" x2="822.9" y2="284.9" stroke="var(--down)" class="wick"/>
<rect x="821.76" y="239.6" width="2.35" height="38.3" fill="var(--down)"/>
<line x1="826.7" y1="273.1" x2="826.7" y2="298.2" stroke="var(--down)" class="wick"/>
<rect x="825.54" y="277.9" width="2.35" height="4.0" fill="var(--down)"/>
<line x1="830.5" y1="265.3" x2="830.5" y2="289.3" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="271.2" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="834.3" y1="271.8" x2="834.3" y2="293.9" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="275.0" width="2.35" height="10.7" fill="var(--down)"/>
<line x1="838.1" y1="258.3" x2="838.1" y2="291.3" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="262.4" width="2.35" height="20.2" fill="var(--up)"/>
<line x1="841.9" y1="254.3" x2="841.9" y2="293.6" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="259.4" width="2.35" height="25.7" fill="var(--down)"/>
<line x1="845.6" y1="277.7" x2="845.6" y2="294.8" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="284.3" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="849.4" y1="283.2" x2="849.4" y2="304.7" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="292.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="853.2" y1="283.1" x2="853.2" y2="298.5" stroke="var(--up)" class="wick"/>
<rect x="852.05" y="285.1" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="857.0" y1="278.4" x2="857.0" y2="302.1" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="288.7" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="860.8" y1="271.2" x2="860.8" y2="298.6" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="276.3" width="2.35" height="14.3" fill="var(--up)"/>
<line x1="864.6" y1="252.8" x2="864.6" y2="287.2" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="264.0" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="868.4" y1="222.4" x2="868.4" y2="268.4" stroke="var(--up)" class="wick"/>
<rect x="867.19" y="226.9" width="2.35" height="38.3" fill="var(--up)"/>
<line x1="872.2" y1="212.3" x2="872.2" y2="239.0" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="222.4" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="875.9" y1="216.0" x2="875.9" y2="240.7" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="219.5" width="2.35" height="20.7" fill="var(--down)"/>
<line x1="879.7" y1="224.2" x2="879.7" y2="248.2" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="239.2" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="883.5" y1="232.3" x2="883.5" y2="291.5" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="240.2" width="2.35" height="48.7" fill="var(--down)"/>
<line x1="887.3" y1="281.6" x2="887.3" y2="298.0" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="285.2" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="891.1" y1="267.2" x2="891.1" y2="301.2" stroke="var(--up)" class="wick"/>
<rect x="889.91" y="269.0" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="894.9" y1="252.3" x2="894.9" y2="275.6" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="255.6" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="898.7" y1="255.7" x2="898.7" y2="282.2" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="257.0" width="2.35" height="11.7" fill="var(--down)"/>
<line x1="902.4" y1="254.4" x2="902.4" y2="278.3" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="256.2" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="906.2" y1="228.1" x2="906.2" y2="263.3" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="238.3" width="2.35" height="20.0" fill="var(--up)"/>
<line x1="910.0" y1="240.1" x2="910.0" y2="273.8" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="241.1" width="2.35" height="26.4" fill="var(--down)"/>
<line x1="913.8" y1="265.6" x2="913.8" y2="283.1" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="268.3" width="2.35" height="13.2" fill="var(--down)"/>
<line x1="917.6" y1="264.7" x2="917.6" y2="279.9" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="269.6" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="921.4" y1="254.0" x2="921.4" y2="269.0" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="256.9" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="925.2" y1="249.2" x2="925.2" y2="279.3" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="251.7" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="928.9" y1="247.2" x2="928.9" y2="273.8" stroke="var(--up)" class="wick"/>
<rect x="927.77" y="250.3" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="932.7" y1="216.1" x2="932.7" y2="251.3" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="217.9" width="2.35" height="26.8" fill="var(--up)"/>
<line x1="936.5" y1="186.4" x2="936.5" y2="228.6" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="196.0" width="2.35" height="17.4" fill="var(--up)"/>
<line x1="940.3" y1="180.0" x2="940.3" y2="212.3" stroke="var(--up)" class="wick"/>
<rect x="939.13" y="199.3" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="944.1" y1="145.0" x2="944.1" y2="199.0" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="148.3" width="2.35" height="48.6" fill="var(--up)"/>
<line x1="947.9" y1="141.1" x2="947.9" y2="156.5" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="141.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="951.7" y1="116.9" x2="951.7" y2="152.5" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="125.2" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="955.5" y1="104.7" x2="955.5" y2="132.6" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="110.6" width="2.35" height="19.1" fill="var(--down)"/>
<line x1="959.2" y1="119.3" x2="959.2" y2="146.2" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="134.9" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="963.0" y1="121.6" x2="963.0" y2="149.2" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="135.3" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="966.8" y1="119.0" x2="966.8" y2="151.0" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="136.0" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="970.6" y1="124.2" x2="970.6" y2="159.7" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="130.2" width="2.35" height="20.8" fill="var(--down)"/>
<line x1="974.4" y1="124.9" x2="974.4" y2="160.2" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="144.0" width="2.35" height="5.3" fill="var(--up)"/>
<line x1="978.2" y1="141.0" x2="978.2" y2="176.4" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="142.0" width="2.35" height="17.1" fill="var(--down)"/>
<line x1="982.0" y1="148.6" x2="982.0" y2="172.7" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="149.3" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="985.7" y1="108.7" x2="985.7" y2="158.3" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="117.4" width="2.35" height="31.9" fill="var(--up)"/>
<line x1="989.5" y1="99.6" x2="989.5" y2="153.0" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="119.3" width="2.35" height="32.1" fill="var(--down)"/>
<line x1="993.3" y1="91.7" x2="993.3" y2="151.5" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="96.7" width="2.35" height="51.6" fill="var(--up)"/>
<line x1="997.1" y1="74.2" x2="997.1" y2="103.4" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="89.5" width="2.35" height="4.8" fill="var(--up)"/>
<line x1="1000.9" y1="89.5" x2="1000.9" y2="158.5" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="91.6" width="2.35" height="65.2" fill="var(--down)"/>
<line x1="1004.7" y1="144.1" x2="1004.7" y2="169.9" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="151.4" width="2.35" height="6.3" fill="var(--up)"/>
<line x1="1008.5" y1="142.0" x2="1008.5" y2="163.6" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="147.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="1012.2" y1="138.8" x2="1012.2" y2="169.8" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="140.4" width="2.35" height="25.6" fill="var(--up)"/>
<line x1="1016.0" y1="84.5" x2="1016.0" y2="144.7" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="94.8" width="2.35" height="48.1" fill="var(--up)"/>
<line x1="1019.8" y1="89.4" x2="1019.8" y2="150.0" stroke="var(--down)" class="wick"/>
<rect x="1018.64" y="97.7" width="2.35" height="42.5" fill="var(--down)"/>
<line x1="1023.6" y1="108.4" x2="1023.6" y2="147.2" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="122.3" width="2.35" height="18.5" fill="var(--up)"/>
<line x1="1027.4" y1="109.8" x2="1027.4" y2="143.8" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="118.3" width="2.35" height="19.6" fill="var(--down)"/>
<line x1="1031.2" y1="109.0" x2="1031.2" y2="143.8" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="132.0" width="2.35" height="6.4" fill="var(--up)"/>
<line x1="1035.0" y1="141.3" x2="1035.0" y2="176.9" stroke="var(--down)" class="wick"/>
<rect x="1033.79" y="143.2" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="1038.7" y1="139.3" x2="1038.7" y2="184.1" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="163.8" width="2.35" height="2.4" fill="var(--down)"/>
<line x1="1042.5" y1="120.2" x2="1042.5" y2="164.4" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="120.6" width="2.35" height="39.9" fill="var(--up)"/>
<line x1="1046.3" y1="114.1" x2="1046.3" y2="159.4" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="120.5" width="2.35" height="33.5" fill="var(--down)"/>
<line x1="1050.1" y1="138.5" x2="1050.1" y2="170.8" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="149.4" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="60" y1="79.4" x2="1052" y2="79.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="82.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$80 R1</text>
<text x="1058" y="94.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="173.1" x2="1052" y2="173.1" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="167.1" font-size="11.5" fill="var(--support)" font-weight="600">$70 S1</text>
<text x="1058" y="179.1" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="301.4" x2="1052" y2="301.4" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="295.4" font-size="11.5" fill="var(--support)" font-weight="600">$56 S2</text>
<text x="1058" y="307.4" font-size="9.5" fill="var(--muted)">터치 3회</text>
<line x1="60" y1="337.9" x2="1052" y2="337.9" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="331.9" font-size="11.5" fill="var(--support)" font-weight="600">$52 S3</text>
<text x="1058" y="343.9" font-size="9.5" fill="var(--muted)">터치 4회</text>
<circle cx="1052.0" cy="164.3" r="3" fill="var(--ink)"/>
<text x="1046.0" y="156.3" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $71 (2026-08-21)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)를 뜻하며, 미래 지지/저항을 보장하지 않는다(§4 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $80 | 2 | 2026-05-18·2026-06-22 — 최근 5년 최고가($80.08)를 포함하는 구간, 아직 상단 저항이 한 차례만 형성 |
| **현재가** | **$70.60** (2026-08-21 종가) | — | R1과 S1 사이 |
| S1 | $70 | 2 | 2026-04-13·2026-06-01 |
| S2 | $56 | 3 | 2025-07-07·2025-08-18·2025-11-03 |
| S3 | $52 | 4 | 2024-12-16·2025-01-27·2025-03-03·2025-04-07 |

> 저항 레벨이 R1 하나뿐이고 지지 레벨이 3개인 것은 우연이 아니다 — 5년 내내 대체로 계단식 우상향한 종목이라, 과거 스윙 고점 대부분이 이후 주가에 뚫리며 "저항"이 아니라 "지지"로 성격이 바뀌었다(전형적인 상승 추세의 레벨 분포). 5년 조사 구간이 시작되는 2021년 8월경 주가가 이번 조사에서 확인한 최저치($23.53, 2021-08-16 주간 저가)에 가까웠다는 점도 이 구간이 상승장의 초입이었음을 보여준다.

---

## 3. 관측된 특이 구간 — 2024년 말~2026년 상반기 계단식 랠리

- S3($52, 2024-12~2025-04) → S2($56, 2025-07~2025-11) → S1($70, 2026-04~06) → R1($80, 2026-05~06)로 이어지는 스윙 레벨의 순서 자체가, 18개월에 걸쳐 지지선이 계속 위로 재형성되는 전형적인 계단식 상승 패턴을 보여준다.
- 이 구간은 `02_history.md`에서 확인한 Power Innovation(데이터센터向 전력) 신사업 부상·잇단 볼트온 M&A(Rimrock·Saber Midstream 등) 시기와 겹친다 — `06_valuation.md` §2에서도 같은 기간 PER·PBR 배수가 꾸준히 재평가(re-rating)돼온 것으로 확인된다.
- 2026-05~06 고점($80.08) 형성 이후 2026-08 현재($70.60)까지는 고점 대비 약 −12% 조정된 상태로, 아직 S1($70) 부근에서 지지 여부를 시험하는 국면으로 볼 수 있다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 262개 주, 2021-08-23~2026-08-21. 수집 시점: 2026-08-22. 원주가(과거 분할은 소급 반영, 배당은 미반영 — 5년간 배당 20회 지급)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py WMB --name "Williams Companies" --interval 1wk --close-on 2026-08-21` — 레벨 개수는 기본값(3) 그대로 사용, 위 §2 각주처럼 저항 1개·지지 3개로 비대칭 산출.
- **한계**:
    - 후행적(과거 데이터 기반) 지표다. 특정 가격이 지지·저항으로 "작동할 것"을 보장하지 않는다.
    - 거래량 프로파일, 이동평균, 추세선, 옵션 미결제약정 등 다른 기술적 지표는 포함하지 않았다 — 스윙 고점/저점 빈도만 반영한 단순 모델이다.
    - 윈도우(4주)·허용오차(±2.5%) 값을 바꾸면 레벨과 터치 횟수가 달라진다. 여기 쓰인 값은 262개 표본에서 스크립트에 고정된 파라미터이며, 최적화된 값이 아니다.
    - 5년 내내 강한 상승 추세였기 때문에 저항 레벨 표본이 1개뿐이다 — 하락 사이클에서의 저항대 정보가 이 표에는 담기지 않았다는 뜻이므로, 상단 저항을 "$80 하나"로 단정하지 말 것.
    - 조사 기간 중 자본구조 단절 M&A는 없었지만(위 상단 각주), 사업 구성(Power Innovation 등)은 점진적으로 바뀌어와 5년 전 형성된 저점(S3 이전 구간)이 지금과 같은 사업 믹스에서 나온 가격은 아니다.

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

- [Yahoo Finance — The Williams Companies (WMB)](https://finance.yahoo.com/quote/WMB/)
- [StockAnalysis — WMB 종가 이력](https://stockanalysis.com/stocks/wmb/history/)

---

*작성일: 2026-08-22*
