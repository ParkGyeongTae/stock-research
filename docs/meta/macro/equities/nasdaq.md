# 나스닥종합지수

!!! note ""
    최근 5년간 나스닥종합지수(`^IXIC`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 특정 회사나 업종 하나에 좌우되지 않는 **시장 전체를 보여주는 벤치마크(비교 기준)**다. S&P 500보다 기술·성장주 비중이 높아서, 기술·성장주 성격이 강한 종목과 비교할 때 더 적합하다.

    **어떻게 쓰나**: 어떤 회사의 주가가 나스닥지수보다 유독 더 오르거나 내렸다면, 그 회사만의 특별한 이유(실적 등 펀더멘털) 때문인지, 아니면 성장주 전체의 밸류에이션 분위기(금리 변화에 대한 민감도) 때문인지 구분하는 첫 단서가 된다.

---

## 1. 차트 — 최근 5년 주봉

<div class="ixic-chart">
<style>
.ixic-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .ixic-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .ixic-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.ixic-chart svg { width:100%; height:auto; display:block; }
.ixic-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.ixic-chart .title { fill: var(--ink); font-weight:600; }
.ixic-chart .grid { stroke: var(--grid); stroke-width:1; }
.ixic-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="나스닥종합지수(^IXIC) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">나스닥종합지수 (^IXIC) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-21 · 마지막 종가 26,180.46 (2026-08-21) · 단위 지수</text>
<line x1="60" y1="610.4" x2="1052" y2="610.4" class="grid"/>
<text x="52" y="614.4" font-size="11" text-anchor="end" fill="var(--muted)">10,000.00</text>
<line x1="60" y1="532.3" x2="1052" y2="532.3" class="grid"/>
<text x="52" y="536.3" font-size="11" text-anchor="end" fill="var(--muted)">12,500.00</text>
<line x1="60" y1="454.2" x2="1052" y2="454.2" class="grid"/>
<text x="52" y="458.2" font-size="11" text-anchor="end" fill="var(--muted)">15,000.00</text>
<line x1="60" y1="376.1" x2="1052" y2="376.1" class="grid"/>
<text x="52" y="380.1" font-size="11" text-anchor="end" fill="var(--muted)">17,500.00</text>
<line x1="60" y1="298.1" x2="1052" y2="298.1" class="grid"/>
<text x="52" y="302.1" font-size="11" text-anchor="end" fill="var(--muted)">20,000.00</text>
<line x1="60" y1="220.0" x2="1052" y2="220.0" class="grid"/>
<text x="52" y="224.0" font-size="11" text-anchor="end" fill="var(--muted)">22,500.00</text>
<line x1="60" y1="141.9" x2="1052" y2="141.9" class="grid"/>
<text x="52" y="145.9" font-size="11" text-anchor="end" fill="var(--muted)">25,000.00</text>
<line x1="60" y1="63.8" x2="1052" y2="63.8" class="grid"/>
<text x="52" y="67.8" font-size="11" text-anchor="end" fill="var(--muted)">27,500.00</text>
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
<line x1="61.9" y1="449.7" x2="61.9" y2="461.2" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="450.2" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="65.7" y1="442.3" x2="65.7" y2="449.1" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="442.9" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="69.5" y1="441.6" x2="69.5" y2="450.7" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="442.5" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="73.3" y1="447.5" x2="73.3" y2="454.7" stroke="var(--down)" class="wick"/>
<rect x="72.08" y="447.6" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="77.0" y1="451.6" x2="77.0" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="75.86" y="452.7" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="80.8" y1="454.1" x2="80.8" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="455.7" width="2.35" height="12.1" fill="var(--down)"/>
<line x1="84.6" y1="461.8" x2="84.6" y2="479.8" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="467.4" width="2.35" height="2.7" fill="var(--up)"/>
<line x1="88.4" y1="457.2" x2="88.4" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="457.4" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="92.2" y1="447.3" x2="92.2" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="91.01" y="451.4" width="2.35" height="7.8" fill="var(--up)"/>
<line x1="96.0" y1="438.5" x2="96.0" y2="452.0" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="438.7" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="99.8" y1="421.3" x2="99.8" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="98.58" y="423.9" width="2.35" height="13.4" fill="var(--up)"/>
<line x1="103.5" y1="421.8" x2="103.5" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="423.1" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="107.3" y1="419.2" x2="107.3" y2="429.9" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="421.2" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="111.1" y1="416.4" x2="111.1" y2="440.0" stroke="var(--down)" class="wick"/>
<rect x="109.94" y="419.2" width="2.35" height="19.7" fill="var(--down)"/>
<line x1="114.9" y1="428.2" x2="114.9" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="113.73" y="431.7" width="2.35" height="19.8" fill="var(--down)"/>
<line x1="118.7" y1="429.4" x2="118.7" y2="456.4" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="434.5" width="2.35" height="16.0" fill="var(--up)"/>
<line x1="122.5" y1="434.3" x2="122.5" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="121.30" y="434.8" width="2.35" height="14.1" fill="var(--down)"/>
<line x1="126.3" y1="432.4" x2="126.3" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="125.09" y="433.8" width="2.35" height="22.5" fill="var(--up)"/>
<line x1="130.0" y1="426.1" x2="130.0" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="128.87" y="432.5" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="133.8" y1="427.6" x2="133.8" y2="458.0" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="431.3" width="2.35" height="24.9" fill="var(--down)"/>
<line x1="137.6" y1="444.3" x2="137.6" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="457.5" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="141.4" y1="462.3" x2="141.4" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="140.23" y="464.2" width="2.35" height="28.5" fill="var(--down)"/>
<line x1="145.2" y1="485.4" x2="145.2" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="492.6" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="149.0" y1="469.7" x2="149.0" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="482.4" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="152.8" y1="469.5" x2="152.8" y2="493.8" stroke="var(--down)" class="wick"/>
<rect x="151.59" y="481.7" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="156.5" y1="480.3" x2="156.5" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="155.38" y="492.7" width="2.35" height="6.9" fill="var(--down)"/>
<line x1="160.3" y1="494.9" x2="160.3" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="159.16" y="495.0" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="164.1" y1="490.5" x2="164.1" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="498.9" width="2.35" height="8.0" fill="var(--down)"/>
<line x1="167.9" y1="505.7" x2="167.9" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="506.4" width="2.35" height="15.1" fill="var(--down)"/>
<line x1="171.7" y1="488.6" x2="171.7" y2="530.6" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="488.8" width="2.35" height="34.3" fill="var(--up)"/>
<line x1="175.5" y1="478.6" x2="175.5" y2="495.4" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="480.2" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="179.3" y1="465.2" x2="179.3" y2="482.3" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="477.3" width="2.35" height="2.6" fill="var(--up)"/>
<line x1="183.1" y1="468.8" x2="183.1" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="475.9" width="2.35" height="18.5" fill="var(--down)"/>
<line x1="186.8" y1="495.3" x2="186.8" y2="506.8" stroke="var(--down)" class="wick"/>
<rect x="185.67" y="499.6" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="190.6" y1="494.5" x2="190.6" y2="522.1" stroke="var(--down)" class="wick"/>
<rect x="189.45" y="506.7" width="2.35" height="15.0" fill="var(--down)"/>
<line x1="194.4" y1="516.3" x2="194.4" y2="538.1" stroke="var(--down)" class="wick"/>
<rect x="193.24" y="524.5" width="2.35" height="12.9" fill="var(--down)"/>
<line x1="198.2" y1="517.2" x2="198.2" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="197.02" y="537.6" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="202.0" y1="548.2" x2="202.0" y2="575.8" stroke="var(--down)" class="wick"/>
<rect x="200.81" y="550.3" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="205.8" y1="548.3" x2="205.8" y2="578.0" stroke="var(--down)" class="wick"/>
<rect x="204.60" y="556.4" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="209.6" y1="543.8" x2="209.6" y2="576.3" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="543.8" width="2.35" height="23.0" fill="var(--up)"/>
<line x1="213.3" y1="537.9" x2="213.3" y2="551.0" stroke="var(--down)" class="wick"/>
<rect x="212.17" y="543.6" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="217.1" y1="540.3" x2="217.1" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="215.96" y="541.7" width="2.35" height="26.9" fill="var(--down)"/>
<line x1="220.9" y1="571.5" x2="220.9" y2="592.7" stroke="var(--down)" class="wick"/>
<rect x="219.74" y="579.6" width="2.35" height="5.9" fill="var(--down)"/>
<line x1="224.7" y1="560.0" x2="224.7" y2="581.1" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="560.2" width="2.35" height="19.8" fill="var(--up)"/>
<line x1="228.5" y1="558.0" x2="228.5" y2="583.8" stroke="var(--down)" class="wick"/>
<rect x="227.31" y="558.5" width="2.35" height="16.7" fill="var(--down)"/>
<line x1="232.3" y1="557.6" x2="232.3" y2="581.9" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="559.3" width="2.35" height="21.0" fill="var(--up)"/>
<line x1="236.1" y1="562.3" x2="236.1" y2="579.0" stroke="var(--down)" class="wick"/>
<rect x="234.89" y="562.8" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="239.8" y1="545.0" x2="239.8" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="553.1" width="2.35" height="8.5" fill="var(--up)"/>
<line x1="243.6" y1="534.6" x2="243.6" y2="562.5" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="535.7" width="2.35" height="17.3" fill="var(--up)"/>
<line x1="247.4" y1="524.9" x2="247.4" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="246.25" y="527.4" width="2.35" height="10.6" fill="var(--up)"/>
<line x1="251.2" y1="515.2" x2="251.2" y2="534.2" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="515.2" width="2.35" height="10.7" fill="var(--up)"/>
<line x1="255.0" y1="511.0" x2="255.0" y2="526.8" stroke="var(--down)" class="wick"/>
<rect x="253.82" y="516.8" width="2.35" height="9.1" fill="var(--down)"/>
<line x1="258.8" y1="527.4" x2="258.8" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="257.60" y="531.6" width="2.35" height="11.9" fill="var(--down)"/>
<line x1="262.6" y1="544.0" x2="262.6" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="261.39" y="547.3" width="2.35" height="12.2" fill="var(--down)"/>
<line x1="266.4" y1="543.8" x2="266.4" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="544.4" width="2.35" height="14.7" fill="var(--up)"/>
<line x1="270.1" y1="539.5" x2="270.1" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="268.96" y="542.5" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="273.9" y1="560.0" x2="273.9" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="272.75" y="568.6" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="277.7" y1="576.0" x2="277.7" y2="592.5" stroke="var(--down)" class="wick"/>
<rect x="276.54" y="584.4" width="2.35" height="8.1" fill="var(--down)"/>
<line x1="281.5" y1="572.0" x2="281.5" y2="592.3" stroke="var(--down)" class="wick"/>
<rect x="280.32" y="589.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="285.3" y1="586.4" x2="285.3" y2="607.6" stroke="var(--down)" class="wick"/>
<rect x="284.11" y="589.8" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="289.1" y1="580.0" x2="289.1" y2="593.4" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="583.5" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="292.9" y1="572.6" x2="292.9" y2="588.1" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="576.0" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="296.6" y1="574.3" x2="296.6" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="295.47" y="578.3" width="2.35" height="17.3" fill="var(--down)"/>
<line x1="300.4" y1="568.1" x2="300.4" y2="599.6" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="569.1" width="2.35" height="25.2" fill="var(--up)"/>
<line x1="304.2" y1="563.8" x2="304.2" y2="579.0" stroke="var(--down)" class="wick"/>
<rect x="303.04" y="571.8" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="308.0" y1="569.4" x2="308.0" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="572.1" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="311.8" y1="562.1" x2="311.8" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="564.7" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="315.6" y1="565.9" x2="315.6" y2="581.9" stroke="var(--down)" class="wick"/>
<rect x="314.40" y="567.3" width="2.35" height="11.8" fill="var(--down)"/>
<line x1="319.4" y1="561.3" x2="319.4" y2="590.3" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="578.7" width="2.35" height="9.7" fill="var(--down)"/>
<line x1="323.1" y1="586.8" x2="323.1" y2="600.6" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="588.3" width="2.35" height="6.5" fill="var(--down)"/>
<line x1="326.9" y1="594.7" x2="326.9" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="595.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="330.7" y1="591.2" x2="330.7" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="592.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="334.5" y1="576.5" x2="334.5" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="576.7" width="2.35" height="13.0" fill="var(--up)"/>
<line x1="338.3" y1="572.2" x2="338.3" y2="585.3" stroke="var(--up)" class="wick"/>
<rect x="337.12" y="574.8" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="342.1" y1="557.5" x2="342.1" y2="577.0" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="559.7" width="2.35" height="14.0" fill="var(--up)"/>
<line x1="345.9" y1="539.5" x2="345.9" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="547.7" width="2.35" height="15.4" fill="var(--up)"/>
<line x1="349.6" y1="543.2" x2="349.6" y2="559.5" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="550.9" width="2.35" height="5.8" fill="var(--down)"/>
<line x1="353.4" y1="545.7" x2="353.4" y2="558.1" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="554.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="357.2" y1="557.8" x2="357.2" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="356.05" y="559.2" width="2.35" height="7.7" fill="var(--down)"/>
<line x1="361.0" y1="557.3" x2="361.0" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="557.6" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="364.8" y1="553.3" x2="364.8" y2="576.2" stroke="var(--down)" class="wick"/>
<rect x="363.62" y="556.1" width="2.35" height="18.7" fill="var(--down)"/>
<line x1="368.6" y1="555.0" x2="368.6" y2="579.7" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="559.5" width="2.35" height="18.4" fill="var(--up)"/>
<line x1="372.4" y1="547.5" x2="372.4" y2="562.0" stroke="var(--up)" class="wick"/>
<rect x="371.19" y="553.4" width="2.35" height="6.5" fill="var(--up)"/>
<line x1="376.2" y1="540.8" x2="376.2" y2="559.3" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="541.0" width="2.35" height="11.0" fill="var(--up)"/>
<line x1="379.9" y1="540.9" x2="379.9" y2="551.1" stroke="var(--down)" class="wick"/>
<rect x="378.77" y="543.4" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="383.7" y1="541.5" x2="383.7" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="544.1" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="387.5" y1="540.3" x2="387.5" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="386.34" y="544.5" width="2.35" height="1.1" fill="var(--down)"/>
<line x1="391.3" y1="540.8" x2="391.3" y2="554.2" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="540.8" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="395.1" y1="539.6" x2="395.1" y2="550.2" stroke="var(--up)" class="wick"/>
<rect x="393.91" y="540.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="398.9" y1="536.5" x2="398.9" y2="542.5" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="539.0" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="402.7" y1="525.1" x2="402.7" y2="539.7" stroke="var(--up)" class="wick"/>
<rect x="401.48" y="527.4" width="2.35" height="11.1" fill="var(--up)"/>
<line x1="406.4" y1="516.6" x2="406.4" y2="534.9" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="517.4" width="2.35" height="9.7" fill="var(--up)"/>
<line x1="410.2" y1="508.7" x2="410.2" y2="520.1" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="509.2" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="414.0" y1="504.6" x2="414.0" y2="513.9" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="508.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="417.8" y1="489.7" x2="417.8" y2="507.2" stroke="var(--up)" class="wick"/>
<rect x="416.63" y="495.1" width="2.35" height="11.3" fill="var(--up)"/>
<line x1="421.6" y1="494.5" x2="421.6" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="496.6" width="2.35" height="4.7" fill="var(--down)"/>
<line x1="425.4" y1="491.2" x2="425.4" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="492.1" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="429.2" y1="490.3" x2="429.2" y2="499.0" stroke="var(--down)" class="wick"/>
<rect x="427.99" y="491.7" width="2.35" height="4.3" fill="var(--down)"/>
<line x1="432.9" y1="478.2" x2="432.9" y2="498.4" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="481.9" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="436.7" y1="471.5" x2="436.7" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="435.56" y="480.8" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="440.5" y1="474.2" x2="440.5" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="475.6" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="444.3" y1="473.9" x2="444.3" y2="489.2" stroke="var(--down)" class="wick"/>
<rect x="443.13" y="474.9" width="2.35" height="13.4" fill="var(--down)"/>
<line x1="448.1" y1="485.5" x2="448.1" y2="497.6" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="486.3" width="2.35" height="10.2" fill="var(--down)"/>
<line x1="451.9" y1="492.0" x2="451.9" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="450.70" y="498.0" width="2.35" height="9.6" fill="var(--down)"/>
<line x1="455.7" y1="490.6" x2="455.7" y2="506.5" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="498.2" width="2.35" height="7.6" fill="var(--up)"/>
<line x1="459.5" y1="480.8" x2="459.5" y2="497.1" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="484.5" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="463.2" y1="483.6" x2="463.2" y2="496.6" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="485.6" width="2.35" height="7.3" fill="var(--down)"/>
<line x1="467.0" y1="486.8" x2="467.0" y2="495.3" stroke="var(--down)" class="wick"/>
<rect x="465.85" y="489.1" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="470.8" y1="493.2" x2="470.8" y2="510.4" stroke="var(--down)" class="wick"/>
<rect x="469.64" y="495.8" width="2.35" height="14.3" fill="var(--down)"/>
<line x1="474.6" y1="504.7" x2="474.6" y2="517.8" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="509.8" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="478.4" y1="501.9" x2="478.4" y2="516.4" stroke="var(--up)" class="wick"/>
<rect x="477.21" y="503.2" width="2.35" height="6.7" fill="var(--up)"/>
<line x1="482.2" y1="494.4" x2="482.2" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="504.0" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="486.0" y1="497.9" x2="486.0" y2="517.4" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="502.5" width="2.35" height="14.7" fill="var(--down)"/>
<line x1="489.7" y1="511.4" x2="489.7" y2="530.9" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="518.8" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="493.5" y1="500.4" x2="493.5" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="501.7" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="497.3" y1="491.6" x2="497.3" y2="503.1" stroke="var(--up)" class="wick"/>
<rect x="496.14" y="491.8" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="501.1" y1="479.4" x2="501.1" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="499.93" y="481.5" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="504.9" y1="474.2" x2="504.9" y2="481.3" stroke="var(--up)" class="wick"/>
<rect x="503.71" y="477.6" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="508.7" y1="472.2" x2="508.7" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="475.9" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="512.5" y1="472.4" x2="512.5" y2="483.6" stroke="var(--up)" class="wick"/>
<rect x="511.28" y="472.8" width="2.35" height="7.3" fill="var(--up)"/>
<line x1="516.2" y1="458.7" x2="516.2" y2="475.3" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="460.0" width="2.35" height="14.8" fill="var(--up)"/>
<line x1="520.0" y1="452.1" x2="520.0" y2="461.2" stroke="var(--up)" class="wick"/>
<rect x="518.86" y="454.4" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="523.8" y1="449.5" x2="523.8" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="453.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="527.6" y1="457.7" x2="527.6" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="458.2" width="2.35" height="10.9" fill="var(--down)"/>
<line x1="531.4" y1="452.2" x2="531.4" y2="468.0" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="455.1" width="2.35" height="12.8" fill="var(--up)"/>
<line x1="535.2" y1="444.5" x2="535.2" y2="463.4" stroke="var(--up)" class="wick"/>
<rect x="534.00" y="444.5" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="539.0" y1="434.6" x2="539.0" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="537.79" y="440.0" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="542.7" y1="433.5" x2="542.7" y2="449.3" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="434.6" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="546.5" y1="422.8" x2="546.5" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="423.3" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="550.3" y1="420.5" x2="550.3" y2="437.0" stroke="var(--down)" class="wick"/>
<rect x="549.15" y="423.6" width="2.35" height="6.4" fill="var(--down)"/>
<line x1="554.1" y1="418.8" x2="554.1" y2="440.1" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="423.1" width="2.35" height="9.9" fill="var(--up)"/>
<line x1="557.9" y1="413.5" x2="557.9" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="414.4" width="2.35" height="8.1" fill="var(--up)"/>
<line x1="561.7" y1="408.9" x2="561.7" y2="427.3" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="414.7" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="565.5" y1="414.4" x2="565.5" y2="425.3" stroke="var(--down)" class="wick"/>
<rect x="564.29" y="421.3" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="569.3" y1="406.2" x2="569.3" y2="424.5" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="409.6" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="573.0" y1="408.1" x2="573.0" y2="414.3" stroke="var(--up)" class="wick"/>
<rect x="571.86" y="411.1" width="2.35" height="1.4" fill="var(--up)"/>
<line x1="576.8" y1="407.7" x2="576.8" y2="421.5" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="410.6" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="580.6" y1="408.5" x2="580.6" y2="420.1" stroke="var(--down)" class="wick"/>
<rect x="579.44" y="414.1" width="2.35" height="3.4" fill="var(--down)"/>
<line x1="584.4" y1="413.8" x2="584.4" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="583.22" y="414.4" width="2.35" height="31.1" fill="var(--down)"/>
<line x1="588.2" y1="423.6" x2="588.2" y2="445.9" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="425.2" width="2.35" height="16.6" fill="var(--up)"/>
<line x1="592.0" y1="416.6" x2="592.0" y2="436.8" stroke="var(--up)" class="wick"/>
<rect x="590.80" y="418.1" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="595.8" y1="409.3" x2="595.8" y2="416.8" stroke="var(--up)" class="wick"/>
<rect x="594.58" y="412.3" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="599.5" y1="398.1" x2="599.5" y2="412.5" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="401.6" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="603.3" y1="391.9" x2="603.3" y2="401.8" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="394.2" width="2.35" height="6.8" fill="var(--up)"/>
<line x1="607.1" y1="390.7" x2="607.1" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="605.94" y="392.1" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="610.9" y1="384.4" x2="610.9" y2="402.8" stroke="var(--up)" class="wick"/>
<rect x="609.73" y="387.6" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="614.7" y1="368.6" x2="614.7" y2="390.0" stroke="var(--up)" class="wick"/>
<rect x="613.51" y="370.2" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="618.5" y1="362.5" x2="618.5" y2="372.4" stroke="var(--down)" class="wick"/>
<rect x="617.30" y="370.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="622.3" y1="359.4" x2="622.3" y2="376.3" stroke="var(--up)" class="wick"/>
<rect x="621.09" y="368.9" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="626.0" y1="349.1" x2="626.0" y2="371.2" stroke="var(--up)" class="wick"/>
<rect x="624.87" y="349.5" width="2.35" height="18.1" fill="var(--up)"/>
<line x1="629.8" y1="339.6" x2="629.8" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="348.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="633.6" y1="340.5" x2="633.6" y2="370.2" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="345.3" width="2.35" height="23.7" fill="var(--down)"/>
<line x1="637.4" y1="356.5" x2="637.4" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="362.9" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="641.2" y1="367.0" x2="641.2" y2="404.8" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="377.9" width="2.35" height="20.9" fill="var(--down)"/>
<line x1="645.0" y1="398.3" x2="645.0" y2="432.1" stroke="var(--up)" class="wick"/>
<rect x="643.80" y="399.7" width="2.35" height="32.3" fill="var(--up)"/>
<line x1="648.8" y1="370.7" x2="648.8" y2="401.1" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="372.0" width="2.35" height="26.2" fill="var(--up)"/>
<line x1="652.5" y1="360.0" x2="652.5" y2="373.5" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="364.3" width="2.35" height="7.1" fill="var(--up)"/>
<line x1="656.3" y1="363.4" x2="656.3" y2="378.0" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="364.6" width="2.35" height="4.8" fill="var(--down)"/>
<line x1="660.1" y1="373.5" x2="660.1" y2="402.1" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="373.5" width="2.35" height="27.9" fill="var(--down)"/>
<line x1="663.9" y1="369.3" x2="663.9" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="662.73" y="370.4" width="2.35" height="26.5" fill="var(--up)"/>
<line x1="667.7" y1="357.4" x2="667.7" y2="376.7" stroke="var(--up)" class="wick"/>
<rect x="666.52" y="362.1" width="2.35" height="11.7" fill="var(--up)"/>
<line x1="671.5" y1="350.3" x2="671.5" y2="364.8" stroke="var(--up)" class="wick"/>
<rect x="670.31" y="356.8" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="675.3" y1="354.3" x2="675.3" y2="367.8" stroke="var(--up)" class="wick"/>
<rect x="674.09" y="356.2" width="2.35" height="2.1" fill="var(--up)"/>
<line x1="679.1" y1="348.8" x2="679.1" y2="363.6" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="349.8" width="2.35" height="8.2" fill="var(--up)"/>
<line x1="682.8" y1="342.9" x2="682.8" y2="353.8" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="345.2" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="686.6" y1="339.0" x2="686.6" y2="355.9" stroke="var(--up)" class="wick"/>
<rect x="685.45" y="344.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="690.4" y1="336.0" x2="690.4" y2="357.9" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="340.3" width="2.35" height="12.8" fill="var(--down)"/>
<line x1="694.2" y1="319.3" x2="694.2" y2="357.0" stroke="var(--up)" class="wick"/>
<rect x="693.02" y="320.3" width="2.35" height="33.3" fill="var(--up)"/>
<line x1="698.0" y1="317.9" x2="698.0" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="696.81" y="318.2" width="2.35" height="21.1" fill="var(--down)"/>
<line x1="701.8" y1="325.8" x2="701.8" y2="339.5" stroke="var(--up)" class="wick"/>
<rect x="700.60" y="329.2" width="2.35" height="8.9" fill="var(--up)"/>
<line x1="705.6" y1="321.6" x2="705.6" y2="331.2" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="322.5" width="2.35" height="2.4" fill="var(--up)"/>
<line x1="709.3" y1="302.3" x2="709.3" y2="321.3" stroke="var(--up)" class="wick"/>
<rect x="708.17" y="302.4" width="2.35" height="18.9" fill="var(--up)"/>
<line x1="713.1" y1="296.1" x2="713.1" y2="309.3" stroke="var(--up)" class="wick"/>
<rect x="711.96" y="300.3" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="716.9" y1="291.7" x2="716.9" y2="324.0" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="297.6" width="2.35" height="13.9" fill="var(--down)"/>
<line x1="720.7" y1="295.9" x2="720.7" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="306.7" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="724.5" y1="309.3" x2="724.5" y2="325.6" stroke="var(--up)" class="wick"/>
<rect x="723.31" y="309.9" width="2.35" height="5.0" fill="var(--up)"/>
<line x1="728.3" y1="297.8" x2="728.3" y2="328.7" stroke="var(--down)" class="wick"/>
<rect x="727.10" y="302.7" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="732.1" y1="307.1" x2="732.1" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="309.6" width="2.35" height="22.7" fill="var(--up)"/>
<line x1="735.8" y1="294.4" x2="735.8" y2="312.1" stroke="var(--up)" class="wick"/>
<rect x="734.67" y="299.5" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="739.6" y1="299.0" x2="739.6" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="309.7" width="2.35" height="12.3" fill="var(--up)"/>
<line x1="743.4" y1="302.3" x2="743.4" y2="324.9" stroke="var(--up)" class="wick"/>
<rect x="742.25" y="312.9" width="2.35" height="9.6" fill="var(--up)"/>
<line x1="747.2" y1="296.6" x2="747.2" y2="316.3" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="297.2" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="751.0" y1="294.6" x2="751.0" y2="313.3" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="295.2" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="754.8" y1="309.2" x2="754.8" y2="348.9" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="310.8" width="2.35" height="23.2" fill="var(--down)"/>
<line x1="758.6" y1="329.5" x2="758.6" y2="367.7" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="331.7" width="2.35" height="22.7" fill="var(--down)"/>
<line x1="762.4" y1="364.6" x2="762.4" y2="384.3" stroke="var(--down)" class="wick"/>
<rect x="761.18" y="365.5" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="766.1" y1="362.8" x2="766.1" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="764.96" y="367.3" width="2.35" height="1.9" fill="var(--up)"/>
<line x1="769.9" y1="351.7" x2="769.9" y2="382.9" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="359.1" width="2.35" height="22.6" fill="var(--down)"/>
<line x1="773.7" y1="369.4" x2="773.7" y2="436.2" stroke="var(--down)" class="wick"/>
<rect x="772.54" y="390.3" width="2.35" height="45.5" fill="var(--down)"/>
<line x1="777.5" y1="385.4" x2="777.5" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="776.32" y="400.4" width="2.35" height="54.5" fill="var(--up)"/>
<line x1="781.3" y1="387.5" x2="781.3" y2="420.9" stroke="var(--down)" class="wick"/>
<rect x="780.11" y="388.0" width="2.35" height="26.0" fill="var(--down)"/>
<line x1="785.1" y1="379.1" x2="785.1" y2="432.8" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="379.8" width="2.35" height="41.5" fill="var(--up)"/>
<line x1="788.9" y1="359.0" x2="788.9" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="787.68" y="361.2" width="2.35" height="18.3" fill="var(--up)"/>
<line x1="792.6" y1="357.5" x2="792.6" y2="376.0" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="362.7" width="2.35" height="3.5" fill="var(--up)"/>
<line x1="796.4" y1="322.6" x2="796.4" y2="345.8" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="322.7" width="2.35" height="16.8" fill="var(--up)"/>
<line x1="800.2" y1="321.7" x2="800.2" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="331.2" width="2.35" height="6.3" fill="var(--down)"/>
<line x1="804.0" y1="317.1" x2="804.0" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="802.83" y="325.7" width="2.35" height="3.1" fill="var(--up)"/>
<line x1="807.8" y1="310.2" x2="807.8" y2="329.7" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="312.7" width="2.35" height="14.6" fill="var(--up)"/>
<line x1="811.6" y1="304.3" x2="811.6" y2="317.8" stroke="var(--down)" class="wick"/>
<rect x="810.40" y="311.4" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="815.4" y1="306.4" x2="815.4" y2="317.4" stroke="var(--down)" class="wick"/>
<rect x="814.19" y="312.1" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="819.1" y1="288.3" x2="819.1" y2="318.8" stroke="var(--up)" class="wick"/>
<rect x="817.97" y="289.5" width="2.35" height="26.4" fill="var(--up)"/>
<line x1="822.9" y1="278.5" x2="822.9" y2="294.8" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="279.3" width="2.35" height="7.5" fill="var(--up)"/>
<line x1="826.7" y1="277.6" x2="826.7" y2="288.0" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="279.8" width="2.35" height="3.0" fill="var(--up)"/>
<line x1="830.5" y1="267.4" x2="830.5" y2="282.7" stroke="var(--up)" class="wick"/>
<rect x="829.33" y="270.1" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="834.3" y1="261.8" x2="834.3" y2="274.6" stroke="var(--up)" class="wick"/>
<rect x="833.12" y="263.4" width="2.35" height="4.6" fill="var(--up)"/>
<line x1="838.1" y1="252.5" x2="838.1" y2="280.6" stroke="var(--down)" class="wick"/>
<rect x="836.90" y="261.3" width="2.35" height="16.4" fill="var(--down)"/>
<line x1="841.9" y1="252.3" x2="841.9" y2="272.0" stroke="var(--up)" class="wick"/>
<rect x="840.69" y="252.8" width="2.35" height="18.6" fill="var(--up)"/>
<line x1="845.6" y1="241.7" x2="845.6" y2="256.0" stroke="var(--up)" class="wick"/>
<rect x="844.48" y="247.4" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="849.4" y1="246.5" x2="849.4" y2="269.8" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="247.6" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="853.2" y1="243.6" x2="853.2" y2="254.7" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="252.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="857.0" y1="239.4" x2="857.0" y2="265.8" stroke="var(--up)" class="wick"/>
<rect x="855.83" y="244.9" width="2.35" height="19.2" fill="var(--up)"/>
<line x1="860.8" y1="229.9" x2="860.8" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="859.62" y="231.2" width="2.35" height="10.5" fill="var(--up)"/>
<line x1="864.6" y1="215.4" x2="864.6" y2="233.7" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="215.9" width="2.35" height="12.1" fill="var(--up)"/>
<line x1="868.4" y1="210.5" x2="868.4" y2="229.8" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="216.6" width="2.35" height="3.8" fill="var(--down)"/>
<line x1="872.2" y1="206.7" x2="872.2" y2="220.2" stroke="var(--up)" class="wick"/>
<rect x="870.98" y="211.2" width="2.35" height="5.5" fill="var(--up)"/>
<line x1="875.9" y1="200.6" x2="875.9" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="874.77" y="207.7" width="2.35" height="21.5" fill="var(--down)"/>
<line x1="879.7" y1="207.9" x2="879.7" y2="228.9" stroke="var(--up)" class="wick"/>
<rect x="878.55" y="214.4" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="883.5" y1="196.2" x2="883.5" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="882.34" y="198.0" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="887.3" y1="172.5" x2="887.3" y2="188.9" stroke="var(--up)" class="wick"/>
<rect x="886.12" y="181.7" width="2.35" height="5.9" fill="var(--up)"/>
<line x1="891.1" y1="173.8" x2="891.1" y2="218.0" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="174.6" width="2.35" height="29.6" fill="var(--down)"/>
<line x1="894.9" y1="186.6" x2="894.9" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="893.70" y="193.3" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="898.7" y1="199.8" x2="898.7" y2="238.8" stroke="var(--down)" class="wick"/>
<rect x="897.48" y="211.0" width="2.35" height="16.1" fill="var(--down)"/>
<line x1="902.4" y1="192.9" x2="902.4" y2="220.7" stroke="var(--up)" class="wick"/>
<rect x="901.27" y="192.9" width="2.35" height="27.6" fill="var(--up)"/>
<line x1="906.2" y1="183.1" x2="906.2" y2="200.9" stroke="var(--up)" class="wick"/>
<rect x="905.06" y="186.3" width="2.35" height="12.7" fill="var(--up)"/>
<line x1="910.0" y1="182.4" x2="910.0" y2="201.4" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="184.4" width="2.35" height="13.8" fill="var(--down)"/>
<line x1="913.8" y1="193.6" x2="913.8" y2="214.0" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="194.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="917.6" y1="183.6" x2="917.6" y2="193.0" stroke="var(--up)" class="wick"/>
<rect x="916.41" y="185.8" width="2.35" height="4.5" fill="var(--up)"/>
<line x1="921.4" y1="186.1" x2="921.4" y2="200.6" stroke="var(--down)" class="wick"/>
<rect x="920.20" y="191.4" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="925.2" y1="181.8" x2="925.2" y2="194.0" stroke="var(--up)" class="wick"/>
<rect x="923.99" y="183.4" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="928.9" y1="179.0" x2="928.9" y2="194.8" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="186.3" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="932.7" y1="185.3" x2="932.7" y2="207.0" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="188.7" width="2.35" height="11.2" fill="var(--up)"/>
<line x1="936.5" y1="173.5" x2="936.5" y2="197.1" stroke="var(--down)" class="wick"/>
<rect x="935.35" y="187.8" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="940.3" y1="182.8" x2="940.3" y2="221.2" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="192.8" width="2.35" height="10.6" fill="var(--down)"/>
<line x1="944.1" y1="194.3" x2="944.1" y2="223.0" stroke="var(--down)" class="wick"/>
<rect x="942.92" y="205.8" width="2.35" height="12.7" fill="var(--down)"/>
<line x1="947.9" y1="206.0" x2="947.9" y2="227.6" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="207.9" width="2.35" height="15.3" fill="var(--up)"/>
<line x1="951.7" y1="199.1" x2="951.7" y2="219.1" stroke="var(--down)" class="wick"/>
<rect x="950.49" y="209.3" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="955.5" y1="207.7" x2="955.5" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="954.28" y="223.5" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="959.2" y1="207.3" x2="959.2" y2="233.7" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="229.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="963.0" y1="217.8" x2="963.0" y2="250.5" stroke="var(--down)" class="wick"/>
<rect x="961.85" y="225.0" width="2.35" height="21.6" fill="var(--down)"/>
<line x1="966.8" y1="229.7" x2="966.8" y2="269.6" stroke="var(--down)" class="wick"/>
<rect x="965.64" y="235.7" width="2.35" height="32.7" fill="var(--down)"/>
<line x1="970.6" y1="236.1" x2="970.6" y2="276.5" stroke="var(--up)" class="wick"/>
<rect x="969.42" y="239.4" width="2.35" height="24.5" fill="var(--up)"/>
<line x1="974.4" y1="204.0" x2="974.4" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="207.4" width="2.35" height="30.1" fill="var(--up)"/>
<line x1="978.2" y1="156.9" x2="978.2" y2="210.7" stroke="var(--up)" class="wick"/>
<rect x="976.99" y="158.5" width="2.35" height="50.6" fill="var(--up)"/>
<line x1="982.0" y1="146.4" x2="982.0" y2="166.9" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="147.0" width="2.35" height="13.1" fill="var(--up)"/>
<line x1="985.7" y1="134.9" x2="985.7" y2="157.8" stroke="var(--up)" class="wick"/>
<rect x="984.57" y="138.3" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="989.5" y1="102.9" x2="989.5" y2="144.6" stroke="var(--up)" class="wick"/>
<rect x="988.35" y="102.9" width="2.35" height="35.4" fill="var(--up)"/>
<line x1="993.3" y1="88.6" x2="993.3" y2="118.8" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="103.6" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="997.1" y1="94.9" x2="997.1" y2="120.0" stroke="var(--up)" class="wick"/>
<rect x="995.93" y="99.9" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="1000.9" y1="76.5" x2="1000.9" y2="94.4" stroke="var(--up)" class="wick"/>
<rect x="999.71" y="80.3" width="2.35" height="11.9" fill="var(--up)"/>
<line x1="1004.7" y1="73.5" x2="1004.7" y2="121.6" stroke="var(--down)" class="wick"/>
<rect x="1003.50" y="80.9" width="2.35" height="38.8" fill="var(--down)"/>
<line x1="1008.5" y1="102.5" x2="1008.5" y2="142.5" stroke="var(--down)" class="wick"/>
<rect x="1007.28" y="108.6" width="2.35" height="5.5" fill="var(--down)"/>
<line x1="1012.2" y1="86.0" x2="1012.2" y2="111.9" stroke="var(--up)" class="wick"/>
<rect x="1011.07" y="94.5" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="1016.0" y1="93.1" x2="1016.0" y2="141.4" stroke="var(--down)" class="wick"/>
<rect x="1014.86" y="95.6" width="2.35" height="37.0" fill="var(--down)"/>
<line x1="1019.8" y1="102.5" x2="1019.8" y2="132.8" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="115.9" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="1023.6" y1="101.2" x2="1023.6" y2="125.4" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="101.9" width="2.35" height="8.8" fill="var(--up)"/>
<line x1="1027.4" y1="100.8" x2="1027.4" y2="134.1" stroke="var(--down)" class="wick"/>
<rect x="1026.22" y="107.9" width="2.35" height="17.7" fill="var(--down)"/>
<line x1="1031.2" y1="114.4" x2="1031.2" y2="144.4" stroke="var(--down)" class="wick"/>
<rect x="1030.00" y="119.4" width="2.35" height="23.3" fill="var(--down)"/>
<line x1="1035.0" y1="127.5" x2="1035.0" y2="159.8" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="130.2" width="2.35" height="4.3" fill="var(--up)"/>
<line x1="1038.7" y1="87.6" x2="1038.7" y2="128.8" stroke="var(--up)" class="wick"/>
<rect x="1037.57" y="89.1" width="2.35" height="38.7" fill="var(--up)"/>
<line x1="1042.5" y1="83.3" x2="1042.5" y2="99.0" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="87.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="1046.3" y1="85.7" x2="1046.3" y2="109.9" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="86.2" width="2.35" height="18.9" fill="var(--down)"/>
<line x1="1050.1" y1="102.2" x2="1050.1" y2="109.1" stroke="var(--down)" class="wick"/>
<rect x="1048.93" y="104.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="60" y1="151.2" x2="1052" y2="151.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="145.2" font-size="11.5" fill="var(--support)" font-weight="600">24,702.86 S1</text>
<text x="1058" y="157.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="530.8" x2="1052" y2="530.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="524.8" font-size="11.5" fill="var(--support)" font-weight="600">12,549.60 S2</text>
<text x="1058" y="536.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="605.8" x2="1052" y2="605.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="599.8" font-size="11.5" fill="var(--support)" font-weight="600">10,148.15 S3</text>
<text x="1058" y="611.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="105.0" r="3" fill="var(--ink)"/>
<text x="1046.0" y="97.0" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 26,180.46 (2026-08-21)</text>
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

## 2. 해석

- **상승**: 성장주에 대한 위험선호가 커졌거나, 금리가 내려가서(할인율 완화) 미래 이익의 현재가치가 커질 것이라는 기대와 자주 함께 나타난다.
- **하락**: 성장주의 밸류에이션이 다시 낮게 매겨지는 압력(할인율 상승), 혹은 위험을 피하려는 심리와 자주 함께 나타난다.
- **왜 금리에 민감한가**: 성장주는 회사 가치의 상당 부분이 먼 미래에 벌어들일 현금흐름에 있다. 금리(할인율)가 오르면 먼 미래의 돈일수록 지금 가치로 환산했을 때 더 많이 깎인다. 그래서 같은 폭의 금리 변화라도, 이미 자리 잡은 성숙한 기업보다 성장주의 밸류에이션이 훨씬 크게 흔들린다([거시경제 개념 정리](../../concepts/macroeconomics.md) 참고).
- 금리에 대한 민감도가 크기 때문에, 어떤 회사의 주가가 나스닥지수보다 더 오르거나 덜 올랐을 때 그 차이가 "금리가 할인율을 거쳐 밸류에이션에 준 영향" 때문인지 "그 회사만의 이슈" 때문인지 구분해서 봐야 한다.

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
