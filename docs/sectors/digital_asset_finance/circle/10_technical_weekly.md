# 기술적 분석 (주봉 캔들차트 · 다년 구조)

> 주봉으로 여러 사이클에 걸친 구조적 지지/저항을 본다. **Circle은 2025-06-05 상장이라 5년치가 없어 상장 이후 전체 기간(69주)을 대상으로 한다.** 최근 1년 흐름은 [기술적 분석 — 일봉·1년](./09_technical_daily.md)를 참고. **과거 가격 패턴에 대한 객관적 서술이며 매수/매도 신호나 목표가 예측이 아니다** — 적정주가 판단은 [밸류에이션 / 적정주가](./06_valuation.md), 투자 결론은 [투자 판단](./07_investment.md)에 있다.

::: warning 이 차트는 표본이 근본적으로 부족하다
상장 후 69주치뿐이고 그 안에서 주가가 $49.90~$159.47로 3.2배 움직여, **터치 2회 이상인 클러스터가 $138 하나밖에 검출되지 않았다.** 스크립트가 현재가 행에 붙이는 "기간 내 하단 지지 없음(신저가 구간)" 라벨은 **"검출된 레벨이 전부 현재가 위"라는 뜻이지 실제로 신저가라는 뜻이 아니다** — 상장 후 최저가는 $49.90으로 현재가보다 41% 아래다. 아래 표에서는 그 라벨을 쓰지 않고 실제 위치로 고쳐 적었다. **이 문서는 참고 자료로만 쓰고, 실질적인 레벨 판단은 [일봉 차트](./09_technical_daily.md)에 의존한다.**

:::
::: details 이 차트의 데이터 출처와 대조 결과
- **출처**: Yahoo Finance 주봉 OHLCV. [핵심 지표](./04_metrics.md)의 원자료 표와는 계보가 다르다.
- **대조 결과**: 마지막 주봉 종가 **$85.09**(2026-09-17)는 [일봉 차트](./09_technical_daily.md)·[밸류에이션 / 적정주가](./06_valuation.md)와 **일치**한다.

:::
---

## 1. 차트 — 상장 이후 전체 주봉 (2025-06-02 ~ 2026-09-17)

<style>
.crcl-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
.dark .crcl-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.crcl-chart svg { width:100%; height:auto; display:block; }
.crcl-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.crcl-chart .title { fill: var(--ink); font-weight:600; }
.crcl-chart .grid { stroke: var(--grid); stroke-width:1; }
.crcl-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="crcl-chart">
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Circle(CRCL) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">Circle (CRCL) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2025-06-02 ~ 2026-09-17 · 마지막 종가 $85.09 (2026-09-17) · 단위 USD</text>
<line x1="60" y1="604.9" x2="1052" y2="604.9" class="grid"/>
<text x="52" y="608.9" font-size="11" text-anchor="end" fill="var(--muted)">50</text>
<line x1="60" y1="499.3" x2="1052" y2="499.3" class="grid"/>
<text x="52" y="503.3" font-size="11" text-anchor="end" fill="var(--muted)">100</text>
<line x1="60" y1="393.8" x2="1052" y2="393.8" class="grid"/>
<text x="52" y="397.8" font-size="11" text-anchor="end" fill="var(--muted)">150</text>
<line x1="60" y1="288.2" x2="1052" y2="288.2" class="grid"/>
<text x="52" y="292.2" font-size="11" text-anchor="end" fill="var(--muted)">200</text>
<line x1="60" y1="182.7" x2="1052" y2="182.7" class="grid"/>
<text x="52" y="186.7" font-size="11" text-anchor="end" fill="var(--muted)">250</text>
<line x1="60" y1="77.1" x2="1052" y2="77.1" class="grid"/>
<text x="52" y="81.1" font-size="11" text-anchor="end" fill="var(--muted)">300</text>
<line x1="67.2" y1="56.0" x2="67.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="67.2" y1="626.0" x2="67.2" y2="631.0" class="axis"/>
<text x="67.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="512.9" y1="56.0" x2="512.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="512.9" y1="626.0" x2="512.9" y2="631.0" class="axis"/>
<text x="512.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="67.2" y1="449.7" x2="67.2" y2="575.3" stroke="var(--up)" class="wick"/>
<rect x="64.19" y="483.1" width="6.00" height="81.7" fill="var(--up)"/>
<line x1="81.6" y1="417.9" x2="81.6" y2="496.1" stroke="var(--up)" class="wick"/>
<rect x="78.57" y="428.5" width="6.00" height="1.8" fill="var(--up)"/>
<line x1="95.9" y1="185.0" x2="95.9" y2="407.4" stroke="var(--up)" class="wick"/>
<rect x="92.94" y="203.2" width="6.00" height="195.8" fill="var(--up)"/>
<line x1="110.3" y1="79.2" x2="110.3" y2="339.7" stroke="var(--down)" class="wick"/>
<rect x="107.32" y="207.0" width="6.00" height="122.5" fill="var(--down)"/>
<line x1="124.7" y1="300.9" x2="124.7" y2="348.4" stroke="var(--up)" class="wick"/>
<rect x="121.70" y="311.9" width="6.00" height="14.8" fill="var(--up)"/>
<line x1="139.1" y1="255.3" x2="139.1" y2="325.2" stroke="var(--down)" class="wick"/>
<rect x="136.07" y="301.4" width="6.00" height="13.6" fill="var(--down)"/>
<line x1="153.4" y1="155.3" x2="153.4" y2="318.7" stroke="var(--up)" class="wick"/>
<rect x="150.45" y="238.0" width="6.00" height="72.9" fill="var(--up)"/>
<line x1="167.8" y1="220.9" x2="167.8" y2="314.6" stroke="var(--down)" class="wick"/>
<rect x="164.83" y="232.5" width="6.00" height="70.8" fill="var(--down)"/>
<line x1="182.2" y1="292.7" x2="182.2" y2="357.3" stroke="var(--down)" class="wick"/>
<rect x="179.20" y="294.6" width="6.00" height="61.0" fill="var(--down)"/>
<line x1="196.6" y1="347.1" x2="196.6" y2="395.9" stroke="var(--down)" class="wick"/>
<rect x="193.58" y="347.1" width="6.00" height="27.6" fill="var(--down)"/>
<line x1="211.0" y1="309.5" x2="211.0" y2="422.5" stroke="var(--down)" class="wick"/>
<rect x="207.96" y="370.5" width="6.00" height="24.8" fill="var(--down)"/>
<line x1="225.3" y1="394.9" x2="225.3" y2="437.9" stroke="var(--down)" class="wick"/>
<rect x="222.33" y="396.5" width="6.00" height="28.8" fill="var(--down)"/>
<line x1="239.7" y1="423.4" x2="239.7" y2="448.3" stroke="var(--down)" class="wick"/>
<rect x="236.71" y="426.8" width="6.00" height="5.0" fill="var(--down)"/>
<line x1="254.1" y1="432.4" x2="254.1" y2="482.4" stroke="var(--down)" class="wick"/>
<rect x="251.09" y="439.0" width="6.00" height="29.6" fill="var(--down)"/>
<line x1="268.5" y1="422.3" x2="268.5" y2="478.1" stroke="var(--up)" class="wick"/>
<rect x="265.46" y="445.9" width="6.00" height="23.9" fill="var(--up)"/>
<line x1="282.8" y1="398.6" x2="282.8" y2="446.4" stroke="var(--up)" class="wick"/>
<rect x="279.84" y="406.1" width="6.00" height="30.1" fill="var(--up)"/>
<line x1="297.2" y1="411.5" x2="297.2" y2="451.1" stroke="var(--down)" class="wick"/>
<rect x="294.22" y="415.1" width="6.00" height="27.2" fill="var(--down)"/>
<line x1="311.6" y1="380.1" x2="311.6" y2="441.1" stroke="var(--up)" class="wick"/>
<rect x="308.59" y="402.7" width="6.00" height="34.4" fill="var(--up)"/>
<line x1="326.0" y1="373.8" x2="326.0" y2="430.5" stroke="var(--down)" class="wick"/>
<rect x="322.97" y="385.3" width="6.00" height="44.5" fill="var(--down)"/>
<line x1="340.3" y1="412.0" x2="340.3" y2="450.6" stroke="var(--down)" class="wick"/>
<rect x="337.35" y="419.0" width="6.00" height="24.4" fill="var(--down)"/>
<line x1="354.7" y1="406.4" x2="354.7" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="351.72" y="410.6" width="6.00" height="25.9" fill="var(--up)"/>
<line x1="369.1" y1="399.2" x2="369.1" y2="451.9" stroke="var(--down)" class="wick"/>
<rect x="366.10" y="400.3" width="6.00" height="42.1" fill="var(--down)"/>
<line x1="383.5" y1="445.0" x2="383.5" y2="507.6" stroke="var(--down)" class="wick"/>
<rect x="380.48" y="445.0" width="6.00" height="47.7" fill="var(--down)"/>
<line x1="397.9" y1="477.1" x2="397.9" y2="538.6" stroke="var(--down)" class="wick"/>
<rect x="394.86" y="482.9" width="6.00" height="54.7" fill="var(--down)"/>
<line x1="412.2" y1="537.5" x2="412.2" y2="573.4" stroke="var(--down)" class="wick"/>
<rect x="409.23" y="537.8" width="6.00" height="22.1" fill="var(--down)"/>
<line x1="426.6" y1="538.4" x2="426.6" y2="566.8" stroke="var(--up)" class="wick"/>
<rect x="423.61" y="541.7" width="6.00" height="16.7" fill="var(--up)"/>
<line x1="441.0" y1="524.1" x2="441.0" y2="551.6" stroke="var(--up)" class="wick"/>
<rect x="437.99" y="529.7" width="6.00" height="17.2" fill="var(--up)"/>
<line x1="455.4" y1="517.7" x2="455.4" y2="538.7" stroke="var(--down)" class="wick"/>
<rect x="452.36" y="526.9" width="6.00" height="7.3" fill="var(--down)"/>
<line x1="469.7" y1="528.3" x2="469.7" y2="552.7" stroke="var(--up)" class="wick"/>
<rect x="466.74" y="528.6" width="6.00" height="4.8" fill="var(--up)"/>
<line x1="484.1" y1="517.9" x2="484.1" y2="542.2" stroke="var(--down)" class="wick"/>
<rect x="481.12" y="525.2" width="6.00" height="13.7" fill="var(--down)"/>
<line x1="498.5" y1="531.9" x2="498.5" y2="544.2" stroke="var(--up)" class="wick"/>
<rect x="495.49" y="534.2" width="6.00" height="8.9" fill="var(--up)"/>
<line x1="512.9" y1="524.5" x2="512.9" y2="544.0" stroke="var(--down)" class="wick"/>
<rect x="509.87" y="531.9" width="6.00" height="3.5" fill="var(--down)"/>
<line x1="527.2" y1="523.7" x2="527.2" y2="550.9" stroke="var(--down)" class="wick"/>
<rect x="524.25" y="539.1" width="6.00" height="5.3" fill="var(--down)"/>
<line x1="541.6" y1="546.9" x2="541.6" y2="562.9" stroke="var(--down)" class="wick"/>
<rect x="538.62" y="550.6" width="6.00" height="9.2" fill="var(--down)"/>
<line x1="556.0" y1="547.9" x2="556.0" y2="579.8" stroke="var(--down)" class="wick"/>
<rect x="553.00" y="562.6" width="6.00" height="12.8" fill="var(--down)"/>
<line x1="570.4" y1="579.8" x2="570.4" y2="605.1" stroke="var(--down)" class="wick"/>
<rect x="567.38" y="580.6" width="6.00" height="9.4" fill="var(--down)"/>
<line x1="584.8" y1="579.1" x2="584.8" y2="593.7" stroke="var(--up)" class="wick"/>
<rect x="581.75" y="583.7" width="6.00" height="7.8" fill="var(--up)"/>
<line x1="599.1" y1="572.2" x2="599.1" y2="590.1" stroke="var(--up)" class="wick"/>
<rect x="596.13" y="577.4" width="6.00" height="7.9" fill="var(--up)"/>
<line x1="613.5" y1="519.2" x2="613.5" y2="584.9" stroke="var(--up)" class="wick"/>
<rect x="610.51" y="534.3" width="6.00" height="45.1" fill="var(--up)"/>
<line x1="627.9" y1="478.0" x2="627.9" y2="541.1" stroke="var(--up)" class="wick"/>
<rect x="624.88" y="495.3" width="6.00" height="44.6" fill="var(--up)"/>
<line x1="642.3" y1="449.9" x2="642.3" y2="489.0" stroke="var(--up)" class="wick"/>
<rect x="639.26" y="466.9" width="6.00" height="21.5" fill="var(--up)"/>
<line x1="656.6" y1="422.0" x2="656.6" y2="457.6" stroke="var(--up)" class="wick"/>
<rect x="653.64" y="444.4" width="6.00" height="12.4" fill="var(--up)"/>
<line x1="671.0" y1="441.3" x2="671.0" y2="518.7" stroke="var(--down)" class="wick"/>
<rect x="668.01" y="448.3" width="6.00" height="64.4" fill="var(--down)"/>
<line x1="685.4" y1="500.5" x2="685.4" y2="532.5" stroke="var(--down)" class="wick"/>
<rect x="682.39" y="507.2" width="6.00" height="12.7" fill="var(--down)"/>
<line x1="699.8" y1="495.5" x2="699.8" y2="531.8" stroke="var(--down)" class="wick"/>
<rect x="696.77" y="513.9" width="6.00" height="10.7" fill="var(--down)"/>
<line x1="714.1" y1="475.7" x2="714.1" y2="528.3" stroke="var(--up)" class="wick"/>
<rect x="711.14" y="486.9" width="6.00" height="41.3" fill="var(--up)"/>
<line x1="728.5" y1="485.6" x2="728.5" y2="508.2" stroke="var(--down)" class="wick"/>
<rect x="725.52" y="494.1" width="6.00" height="6.0" fill="var(--down)"/>
<line x1="742.9" y1="499.3" x2="742.9" y2="520.7" stroke="var(--up)" class="wick"/>
<rect x="739.90" y="500.0" width="6.00" height="2.4" fill="var(--up)"/>
<line x1="757.3" y1="451.1" x2="757.3" y2="484.8" stroke="var(--up)" class="wick"/>
<rect x="754.28" y="470.5" width="6.00" height="13.8" fill="var(--up)"/>
<line x1="771.7" y1="414.9" x2="771.7" y2="488.0" stroke="var(--down)" class="wick"/>
<rect x="768.65" y="459.5" width="6.00" height="10.2" fill="var(--down)"/>
<line x1="786.0" y1="459.5" x2="786.0" y2="484.1" stroke="var(--up)" class="wick"/>
<rect x="783.03" y="471.6" width="6.00" height="2.2" fill="var(--up)"/>
<line x1="800.4" y1="468.8" x2="800.4" y2="504.2" stroke="var(--up)" class="wick"/>
<rect x="797.41" y="471.9" width="6.00" height="1.6" fill="var(--up)"/>
<line x1="814.8" y1="479.3" x2="814.8" y2="544.9" stroke="var(--down)" class="wick"/>
<rect x="811.78" y="480.9" width="6.00" height="60.0" fill="var(--down)"/>
<line x1="829.2" y1="526.0" x2="829.2" y2="546.6" stroke="var(--down)" class="wick"/>
<rect x="826.16" y="533.1" width="6.00" height="13.0" fill="var(--down)"/>
<line x1="843.5" y1="526.1" x2="843.5" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="840.54" y="535.5" width="6.00" height="5.6" fill="var(--down)"/>
<line x1="857.9" y1="531.3" x2="857.9" y2="568.2" stroke="var(--down)" class="wick"/>
<rect x="854.91" y="538.9" width="6.00" height="16.2" fill="var(--down)"/>
<line x1="872.3" y1="549.7" x2="872.3" y2="580.0" stroke="var(--down)" class="wick"/>
<rect x="869.29" y="551.7" width="6.00" height="22.3" fill="var(--down)"/>
<line x1="886.7" y1="556.6" x2="886.7" y2="580.3" stroke="var(--up)" class="wick"/>
<rect x="883.67" y="570.8" width="6.00" height="3.3" fill="var(--up)"/>
<line x1="901.0" y1="569.3" x2="901.0" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="898.04" y="574.4" width="6.00" height="8.4" fill="var(--down)"/>
<line x1="915.4" y1="557.0" x2="915.4" y2="583.9" stroke="var(--up)" class="wick"/>
<rect x="912.42" y="578.8" width="6.00" height="3.0" fill="var(--up)"/>
<line x1="929.8" y1="570.6" x2="929.8" y2="586.6" stroke="var(--down)" class="wick"/>
<rect x="926.80" y="576.1" width="6.00" height="2.2" fill="var(--down)"/>
<line x1="944.2" y1="566.0" x2="944.2" y2="588.3" stroke="var(--up)" class="wick"/>
<rect x="941.17" y="569.7" width="6.00" height="16.2" fill="var(--up)"/>
<line x1="958.6" y1="550.2" x2="958.6" y2="574.3" stroke="var(--up)" class="wick"/>
<rect x="955.55" y="559.3" width="6.00" height="9.4" fill="var(--up)"/>
<line x1="972.9" y1="514.2" x2="972.9" y2="561.1" stroke="var(--up)" class="wick"/>
<rect x="969.93" y="524.7" width="6.00" height="35.4" fill="var(--up)"/>
<line x1="987.3" y1="507.3" x2="987.3" y2="532.6" stroke="var(--down)" class="wick"/>
<rect x="984.30" y="520.6" width="6.00" height="5.9" fill="var(--down)"/>
<line x1="1001.7" y1="492.4" x2="1001.7" y2="529.2" stroke="var(--up)" class="wick"/>
<rect x="998.68" y="495.0" width="6.00" height="31.7" fill="var(--up)"/>
<line x1="1016.1" y1="497.6" x2="1016.1" y2="521.5" stroke="var(--down)" class="wick"/>
<rect x="1013.06" y="498.0" width="6.00" height="21.2" fill="var(--down)"/>
<line x1="1030.4" y1="504.1" x2="1030.4" y2="545.2" stroke="var(--down)" class="wick"/>
<rect x="1027.43" y="516.0" width="6.00" height="14.8" fill="var(--down)"/>
<line x1="1044.8" y1="529.0" x2="1044.8" y2="538.4" stroke="var(--up)" class="wick"/>
<rect x="1041.81" y="530.8" width="6.00" height="4.4" fill="var(--up)"/>
<line x1="60" y1="418.4" x2="1052" y2="418.4" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="421.9" font-size="11.5" fill="var(--resistance)" font-weight="600">$138 R1</text>
<text x="1058" y="433.9" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="530.8" r="3" fill="var(--ink)"/>
<text x="1046.0" y="522.8" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 $85 (2026-09-17)</text>
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

각 레벨은 "전후 4주 내 최고/최저인 스윙 포인트"를 가격 기준 ±2.5% 이내로 묶은 클러스터다. 터치 횟수는 그 클러스터에 포함된 스윙 포인트 개수(강도 근사치)이며, 미래 지지/저항을 보장하지 않는다(4. 방법론 · 한계 참고).

| 레벨 | 가격 | 터치 횟수 | 비고 |
|------|------|-----------|------|
| R1 | $138 | 2 | 2026-03-16·2026-05-11 — 2026년 상반기 고점대. 현재가의 1.6배 |
| **현재가** | **$85.09** (2026-09-17 종가) | — | R1보다 38% 아래. **아래쪽에 검출된 지지가 없는 것은 신저가여서가 아니라 표본이 69주뿐이라 클러스터가 만들어지지 않았기 때문**이다(위 경고 블록 참고). 상장 후 최저가는 $49.90 |

**이 표에서 읽을 수 있는 것은 사실상 없다.** 레벨이 하나뿐이고 그마저 현재가에서 38% 떨어져 있어 근시일 판단에 쓸 수 없다. [일봉 차트](./09_technical_daily.md)의 S1($85)·R1~R2($88~$91)가 실질적인 참고 레벨이다.

---

## 3. 관측된 특이 구간 — 상장 이후 세 국면

- **2025.06~2025.12 — 상장 직후 급등과 되돌림**: 공모가 $31에서 출발해 상장 첫 분기에 세 자릿수로 뛰었다가 되밀렸다. 이 구간의 가격 분산이 워낙 커 스윙 클러스터가 형성되지 않았다.
- **2026.01~2026.06 — 고점권과 붕괴**: 상반기 $138 부근을 두 차례 시험한 뒤(위 R1), **2026-06-30 경쟁 컨소시엄 OUSD 출범**으로 사상 최고가 대비 약 70% 급락했다([최근 뉴스 / 이슈](./08_news.md)). 같은 시기 FTSE Russell 성장주 지수 제외가 겹쳤다.
- **2026.07~2026.09 — 신사업 기대 반등과 9월 급락**: 7월 저점($49.90~$58 구간)에서 OCC 신탁은행 인가·IBM 특허 인수·Arc 메인넷 일정 확정으로 9월 초 $103까지 올랐다가, 9/15~9/16 CLARITY Act 부결·연준 인상으로 $80.45까지 되밀린 뒤 $85.09에서 주를 마쳤다. **본업(준비자산 이자수익)이 아니라 제도·신사업 뉴스가 가격을 만든 구간**이라는 점이 세 국면 모두에 공통된다.

---

## 4. 방법론 · 한계

- **데이터**: Yahoo Finance 주봉 OHLCV(주간 시가/고가/저가/종가/거래량, 주 마지막 거래일 기준), 69개 주, 2025-06-02~2026-09-17. 수집 시점: 2026-09-18. 원주가(과거 분할은 소급 반영, 배당은 미반영)
- **스윙 포인트 탐지**: 각 주의 고가/저가가 전후 4주(총 9주 창) 내 최고/최저값과 같으면 스윙 고점/저점으로 분류.
- **클러스터링**: 스윙 포인트를 가격 오름차순으로 정렬한 뒤, 이미 만든 클러스터 중심과 ±2.5% 이내면 같은 클러스터로 합산하고 중심을 재계산. 터치 2회 이상만 표시.
- **생성**: `scripts/gen_technical_chart.py CRCL --name Circle --interval 1wk --close-on 2026-09-17` (옵션 기본값 그대로. 기간은 5년을 지정했으나 상장이 2025-06이라 실제로는 69주만 존재한다)
- **한계**: 후행 지표이며 특정 가격의 지지·저항 작동을 보장하지 않는다. 거래량 프로파일·이동평균·추세선 등은 포함하지 않은 단순 모델이고, 윈도우·허용오차 값을 바꾸면 레벨과 터치 횟수가 달라진다(최적화된 값이 아니다).
    - **표본 부족이 이 문서의 결정적 한계다.** 69주는 전후 4주 창을 쓰는 스윙 탐지에 충분하지 않고, 그 안에서 주가가 3.2배 움직여 ±2.5% 허용오차로 묶이는 스윙이 거의 없다. `--levels`를 올려도 해결되지 않는다 — 제약은 개수 상한이 아니라 **터치 2회 이상 조건**이기 때문이다. 이 파라미터는 회사 간 비교를 위해 고정돼 있으므로 바꾸지 않았다.
    - **상장 1년 3개월 종목에 "다년 구조"라는 개념이 성립하지 않는다.** 이 문서는 형식상 필수라 만들었을 뿐이며, 실제 레벨 판단은 [일봉 차트](./09_technical_daily.md)를 쓴다.
    - 해당 기간에 주식분할·병합은 없었다. IPO 시 우선주의 Class A 전환은 자본구조 재편이지 분할이 아니므로 소급조정이 필요 없다([핵심 지표](./04_metrics.md) 상단 참고).

---

*작성일: 2026-09-18*
