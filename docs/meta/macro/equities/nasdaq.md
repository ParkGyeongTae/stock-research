# 나스닥종합지수 — 기술적 참고 (주봉 5년)

> 최근 5년 나스닥종합지수(`^IXIC`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 특정 회사·섹터에 종속되지 않는 **범용 시장 벤치마크**다 — [`sp500.md`](./sp500.md)보다 기술·성장주 비중이 높아, 이 레포가 주로 다루는 섹터(EDA·ATE·사이버보안·양자컴퓨팅·결제네트워크 등) 성격과 더 가까운 비교군이다.
>
> **어떻게 쓰나**: 개별 회사 주가가 나스닥 대비 초과 상승/하락하고 있다면, 그 회사 고유의 이슈(펀더멘털)인지 성장주 전체의 밸류에이션 국면(금리 민감도 등, [`concepts/macroeconomics.md`](../../concepts/macroeconomics.md) "금리가 주가에 닿는 두 개의 경로" 참고) 때문인지 구분하는 첫 단서가 된다.

---

## 1. 차트 — 최근 5년 주봉

<div class="ixic-chart">
<style>
.ixic-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .ixic-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-19 · 마지막 종가 26,331.09 (2026-08-19) · 단위 지수</text>
<line x1="60" y1="610.4" x2="1052" y2="610.4" class="grid"/>
<text x="52" y="614.4" font-size="11" text-anchor="end" fill="var(--muted)">10,000</text>
<line x1="60" y1="532.3" x2="1052" y2="532.3" class="grid"/>
<text x="52" y="536.3" font-size="11" text-anchor="end" fill="var(--muted)">12,500</text>
<line x1="60" y1="454.2" x2="1052" y2="454.2" class="grid"/>
<text x="52" y="458.2" font-size="11" text-anchor="end" fill="var(--muted)">15,000</text>
<line x1="60" y1="376.1" x2="1052" y2="376.1" class="grid"/>
<text x="52" y="380.1" font-size="11" text-anchor="end" fill="var(--muted)">17,500</text>
<line x1="60" y1="298.1" x2="1052" y2="298.1" class="grid"/>
<text x="52" y="302.1" font-size="11" text-anchor="end" fill="var(--muted)">20,000</text>
<line x1="60" y1="220.0" x2="1052" y2="220.0" class="grid"/>
<text x="52" y="224.0" font-size="11" text-anchor="end" fill="var(--muted)">22,500</text>
<line x1="60" y1="141.9" x2="1052" y2="141.9" class="grid"/>
<text x="52" y="145.9" font-size="11" text-anchor="end" fill="var(--muted)">25,000</text>
<line x1="60" y1="63.8" x2="1052" y2="63.8" class="grid"/>
<text x="52" y="67.8" font-size="11" text-anchor="end" fill="var(--muted)">27,500</text>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.3" y1="626.0" x2="137.3" y2="631.0" class="axis"/>
<text x="137.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="333.5" y1="626.0" x2="333.5" y2="631.0" class="axis"/>
<text x="333.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="529.6" y1="626.0" x2="529.6" y2="631.0" class="axis"/>
<text x="529.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="729.5" y1="626.0" x2="729.5" y2="631.0" class="axis"/>
<text x="729.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="925.6" y1="626.0" x2="925.6" y2="631.0" class="axis"/>
<text x="925.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="462.9" x2="61.9" y2="472.2" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="463.1" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="65.7" y1="449.7" x2="65.7" y2="461.2" stroke="var(--up)" class="wick"/>
<rect x="64.49" y="450.2" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="69.4" y1="442.3" x2="69.4" y2="449.1" stroke="var(--up)" class="wick"/>
<rect x="68.26" y="442.9" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="73.2" y1="441.6" x2="73.2" y2="450.7" stroke="var(--down)" class="wick"/>
<rect x="72.03" y="442.5" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="77.0" y1="447.5" x2="77.0" y2="454.7" stroke="var(--down)" class="wick"/>
<rect x="75.80" y="447.6" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="80.7" y1="451.6" x2="80.7" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="79.58" y="452.7" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="84.5" y1="454.1" x2="84.5" y2="475.3" stroke="var(--down)" class="wick"/>
<rect x="83.35" y="455.7" width="2.34" height="12.1" fill="var(--down)"/>
<line x1="88.3" y1="461.8" x2="88.3" y2="479.8" stroke="var(--up)" class="wick"/>
<rect x="87.12" y="467.4" width="2.34" height="2.7" fill="var(--up)"/>
<line x1="92.1" y1="457.2" x2="92.1" y2="471.7" stroke="var(--up)" class="wick"/>
<rect x="90.89" y="457.4" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="95.8" y1="447.3" x2="95.8" y2="459.4" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="451.4" width="2.34" height="7.8" fill="var(--up)"/>
<line x1="99.6" y1="438.5" x2="99.6" y2="452.0" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="438.7" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="103.4" y1="421.3" x2="103.4" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="423.9" width="2.34" height="13.4" fill="var(--up)"/>
<line x1="107.1" y1="421.8" x2="107.1" y2="437.2" stroke="var(--down)" class="wick"/>
<rect x="105.98" y="423.1" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="110.9" y1="419.2" x2="110.9" y2="429.9" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="421.2" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="114.7" y1="416.4" x2="114.7" y2="440.0" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="419.2" width="2.34" height="19.7" fill="var(--down)"/>
<line x1="118.5" y1="428.2" x2="118.5" y2="456.4" stroke="var(--down)" class="wick"/>
<rect x="117.29" y="431.7" width="2.34" height="19.8" fill="var(--down)"/>
<line x1="122.2" y1="429.4" x2="122.2" y2="456.4" stroke="var(--up)" class="wick"/>
<rect x="121.07" y="434.5" width="2.34" height="16.0" fill="var(--up)"/>
<line x1="126.0" y1="434.3" x2="126.0" y2="455.5" stroke="var(--down)" class="wick"/>
<rect x="124.84" y="434.8" width="2.34" height="14.1" fill="var(--down)"/>
<line x1="129.8" y1="432.4" x2="129.8" y2="458.6" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="433.8" width="2.34" height="22.5" fill="var(--up)"/>
<line x1="133.6" y1="426.1" x2="133.6" y2="434.1" stroke="var(--down)" class="wick"/>
<rect x="132.38" y="432.5" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="137.3" y1="427.6" x2="137.3" y2="458.0" stroke="var(--down)" class="wick"/>
<rect x="136.15" y="431.3" width="2.34" height="24.9" fill="var(--down)"/>
<line x1="141.1" y1="444.3" x2="141.1" y2="468.9" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="457.5" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="144.9" y1="462.3" x2="144.9" y2="492.8" stroke="var(--down)" class="wick"/>
<rect x="143.70" y="464.2" width="2.34" height="28.5" fill="var(--down)"/>
<line x1="148.6" y1="485.4" x2="148.6" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="147.47" y="492.6" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="152.4" y1="469.7" x2="152.4" y2="492.7" stroke="var(--up)" class="wick"/>
<rect x="151.24" y="482.4" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="156.2" y1="469.5" x2="156.2" y2="493.8" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="481.7" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="160.0" y1="480.3" x2="160.0" y2="502.1" stroke="var(--down)" class="wick"/>
<rect x="158.79" y="492.7" width="2.34" height="6.9" fill="var(--down)"/>
<line x1="163.7" y1="494.9" x2="163.7" y2="529.6" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="495.0" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="167.5" y1="490.5" x2="167.5" y2="509.7" stroke="var(--down)" class="wick"/>
<rect x="166.33" y="498.9" width="2.34" height="8.0" fill="var(--down)"/>
<line x1="171.3" y1="505.7" x2="171.3" y2="527.0" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="506.4" width="2.34" height="15.1" fill="var(--down)"/>
<line x1="175.0" y1="488.6" x2="175.0" y2="530.6" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="488.8" width="2.34" height="34.3" fill="var(--up)"/>
<line x1="178.8" y1="478.6" x2="178.8" y2="495.4" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="480.2" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="182.6" y1="465.2" x2="182.6" y2="482.3" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="477.3" width="2.34" height="2.6" fill="var(--up)"/>
<line x1="186.4" y1="468.8" x2="186.4" y2="495.2" stroke="var(--down)" class="wick"/>
<rect x="185.19" y="475.9" width="2.34" height="18.5" fill="var(--down)"/>
<line x1="190.1" y1="495.3" x2="190.1" y2="506.8" stroke="var(--down)" class="wick"/>
<rect x="188.96" y="499.6" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="193.9" y1="494.5" x2="193.9" y2="522.1" stroke="var(--down)" class="wick"/>
<rect x="192.73" y="506.7" width="2.34" height="15.0" fill="var(--down)"/>
<line x1="197.7" y1="516.3" x2="197.7" y2="538.1" stroke="var(--down)" class="wick"/>
<rect x="196.50" y="524.5" width="2.34" height="12.9" fill="var(--down)"/>
<line x1="201.4" y1="517.2" x2="201.4" y2="548.2" stroke="var(--down)" class="wick"/>
<rect x="200.28" y="537.6" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="205.2" y1="548.2" x2="205.2" y2="575.8" stroke="var(--down)" class="wick"/>
<rect x="204.05" y="550.3" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="209.0" y1="548.3" x2="209.0" y2="578.0" stroke="var(--down)" class="wick"/>
<rect x="207.82" y="556.4" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="212.8" y1="543.8" x2="212.8" y2="576.3" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="543.8" width="2.34" height="23.0" fill="var(--up)"/>
<line x1="216.5" y1="537.9" x2="216.5" y2="551.0" stroke="var(--down)" class="wick"/>
<rect x="215.36" y="543.6" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="220.3" y1="540.3" x2="220.3" y2="568.9" stroke="var(--down)" class="wick"/>
<rect x="219.13" y="541.7" width="2.34" height="26.9" fill="var(--down)"/>
<line x1="224.1" y1="571.5" x2="224.1" y2="592.7" stroke="var(--down)" class="wick"/>
<rect x="222.91" y="579.6" width="2.34" height="5.9" fill="var(--down)"/>
<line x1="227.8" y1="560.0" x2="227.8" y2="581.1" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="560.2" width="2.34" height="19.8" fill="var(--up)"/>
<line x1="231.6" y1="558.0" x2="231.6" y2="583.8" stroke="var(--down)" class="wick"/>
<rect x="230.45" y="558.5" width="2.34" height="16.7" fill="var(--down)"/>
<line x1="235.4" y1="557.6" x2="235.4" y2="581.9" stroke="var(--up)" class="wick"/>
<rect x="234.22" y="559.3" width="2.34" height="21.0" fill="var(--up)"/>
<line x1="239.2" y1="562.3" x2="239.2" y2="579.0" stroke="var(--down)" class="wick"/>
<rect x="237.99" y="562.8" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="242.9" y1="545.0" x2="242.9" y2="569.1" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="553.1" width="2.34" height="8.5" fill="var(--up)"/>
<line x1="246.7" y1="534.6" x2="246.7" y2="562.5" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="535.7" width="2.34" height="17.3" fill="var(--up)"/>
<line x1="250.5" y1="524.9" x2="250.5" y2="539.8" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="527.4" width="2.34" height="10.6" fill="var(--up)"/>
<line x1="254.3" y1="515.2" x2="254.3" y2="534.2" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="515.2" width="2.34" height="10.7" fill="var(--up)"/>
<line x1="258.0" y1="511.0" x2="258.0" y2="526.8" stroke="var(--down)" class="wick"/>
<rect x="256.85" y="516.8" width="2.34" height="9.1" fill="var(--down)"/>
<line x1="261.8" y1="527.4" x2="261.8" y2="543.5" stroke="var(--down)" class="wick"/>
<rect x="260.63" y="531.6" width="2.34" height="11.9" fill="var(--down)"/>
<line x1="265.6" y1="544.0" x2="265.6" y2="562.1" stroke="var(--down)" class="wick"/>
<rect x="264.40" y="547.3" width="2.34" height="12.2" fill="var(--down)"/>
<line x1="269.3" y1="543.8" x2="269.3" y2="564.4" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="544.4" width="2.34" height="14.7" fill="var(--up)"/>
<line x1="273.1" y1="539.5" x2="273.1" y2="569.3" stroke="var(--down)" class="wick"/>
<rect x="271.94" y="542.5" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="276.9" y1="560.0" x2="276.9" y2="587.5" stroke="var(--down)" class="wick"/>
<rect x="275.71" y="568.6" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="280.7" y1="576.0" x2="280.7" y2="592.5" stroke="var(--down)" class="wick"/>
<rect x="279.48" y="584.4" width="2.34" height="8.1" fill="var(--down)"/>
<line x1="284.4" y1="572.0" x2="284.4" y2="592.3" stroke="var(--down)" class="wick"/>
<rect x="283.26" y="589.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="288.2" y1="586.4" x2="288.2" y2="607.6" stroke="var(--down)" class="wick"/>
<rect x="287.03" y="589.8" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="292.0" y1="580.0" x2="292.0" y2="593.4" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="583.5" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="295.7" y1="572.6" x2="295.7" y2="588.1" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="576.0" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="299.5" y1="574.3" x2="299.5" y2="602.2" stroke="var(--down)" class="wick"/>
<rect x="298.34" y="578.3" width="2.34" height="17.3" fill="var(--down)"/>
<line x1="303.3" y1="568.1" x2="303.3" y2="599.6" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="569.1" width="2.34" height="25.2" fill="var(--up)"/>
<line x1="307.1" y1="563.8" x2="307.1" y2="579.0" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="571.8" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="310.8" y1="569.4" x2="310.8" y2="579.9" stroke="var(--up)" class="wick"/>
<rect x="309.66" y="572.1" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="314.6" y1="562.1" x2="314.6" y2="580.9" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="564.7" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="318.4" y1="565.9" x2="318.4" y2="581.9" stroke="var(--down)" class="wick"/>
<rect x="317.20" y="567.3" width="2.34" height="11.8" fill="var(--down)"/>
<line x1="322.1" y1="561.3" x2="322.1" y2="590.3" stroke="var(--down)" class="wick"/>
<rect x="320.98" y="578.7" width="2.34" height="9.7" fill="var(--down)"/>
<line x1="325.9" y1="586.8" x2="325.9" y2="600.6" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="588.3" width="2.34" height="6.5" fill="var(--down)"/>
<line x1="329.7" y1="594.7" x2="329.7" y2="603.9" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="595.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="333.5" y1="591.2" x2="333.5" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="592.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="337.2" y1="576.5" x2="337.2" y2="592.0" stroke="var(--up)" class="wick"/>
<rect x="336.06" y="576.7" width="2.34" height="13.0" fill="var(--up)"/>
<line x1="341.0" y1="572.2" x2="341.0" y2="585.3" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="574.8" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="344.8" y1="557.5" x2="344.8" y2="577.0" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="559.7" width="2.34" height="14.0" fill="var(--up)"/>
<line x1="348.5" y1="539.5" x2="348.5" y2="567.0" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="547.7" width="2.34" height="15.4" fill="var(--up)"/>
<line x1="352.3" y1="543.2" x2="352.3" y2="559.5" stroke="var(--down)" class="wick"/>
<rect x="351.15" y="550.9" width="2.34" height="5.8" fill="var(--down)"/>
<line x1="356.1" y1="545.7" x2="356.1" y2="558.1" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="554.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="359.9" y1="557.8" x2="359.9" y2="568.7" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="559.2" width="2.34" height="7.7" fill="var(--down)"/>
<line x1="363.6" y1="557.3" x2="363.6" y2="570.6" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="557.6" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="367.4" y1="553.3" x2="367.4" y2="576.2" stroke="var(--down)" class="wick"/>
<rect x="366.24" y="556.1" width="2.34" height="18.7" fill="var(--down)"/>
<line x1="371.2" y1="555.0" x2="371.2" y2="579.7" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="559.5" width="2.34" height="18.4" fill="var(--up)"/>
<line x1="375.0" y1="547.5" x2="375.0" y2="562.0" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="553.4" width="2.34" height="6.5" fill="var(--up)"/>
<line x1="378.7" y1="540.8" x2="378.7" y2="559.3" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="541.0" width="2.34" height="11.0" fill="var(--up)"/>
<line x1="382.5" y1="540.9" x2="382.5" y2="551.1" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="543.4" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="386.3" y1="541.5" x2="386.3" y2="550.5" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="544.1" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="390.0" y1="540.3" x2="390.0" y2="548.3" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="544.5" width="2.34" height="1.1" fill="var(--down)"/>
<line x1="393.8" y1="540.8" x2="393.8" y2="554.2" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="540.8" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="397.6" y1="539.6" x2="397.6" y2="550.2" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="540.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="401.4" y1="536.5" x2="401.4" y2="542.5" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="539.0" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="405.1" y1="525.1" x2="405.1" y2="539.7" stroke="var(--up)" class="wick"/>
<rect x="403.96" y="527.4" width="2.34" height="11.1" fill="var(--up)"/>
<line x1="408.9" y1="516.6" x2="408.9" y2="534.9" stroke="var(--up)" class="wick"/>
<rect x="407.73" y="517.4" width="2.34" height="9.7" fill="var(--up)"/>
<line x1="412.7" y1="508.7" x2="412.7" y2="520.1" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="509.2" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="416.4" y1="504.6" x2="416.4" y2="513.9" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="508.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="420.2" y1="489.7" x2="420.2" y2="507.2" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="495.1" width="2.34" height="11.3" fill="var(--up)"/>
<line x1="424.0" y1="494.5" x2="424.0" y2="502.9" stroke="var(--down)" class="wick"/>
<rect x="422.82" y="496.6" width="2.34" height="4.7" fill="var(--down)"/>
<line x1="427.8" y1="491.2" x2="427.8" y2="506.2" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="492.1" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="431.5" y1="490.3" x2="431.5" y2="499.0" stroke="var(--down)" class="wick"/>
<rect x="430.36" y="491.7" width="2.34" height="4.3" fill="var(--down)"/>
<line x1="435.3" y1="478.2" x2="435.3" y2="498.4" stroke="var(--up)" class="wick"/>
<rect x="434.13" y="481.9" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="439.1" y1="471.5" x2="439.1" y2="484.8" stroke="var(--down)" class="wick"/>
<rect x="437.90" y="480.8" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="442.8" y1="474.2" x2="442.8" y2="485.5" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="475.6" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="446.6" y1="473.9" x2="446.6" y2="489.2" stroke="var(--down)" class="wick"/>
<rect x="445.45" y="474.9" width="2.34" height="13.4" fill="var(--down)"/>
<line x1="450.4" y1="485.5" x2="450.4" y2="497.6" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="486.3" width="2.34" height="10.2" fill="var(--down)"/>
<line x1="454.2" y1="492.0" x2="454.2" y2="511.6" stroke="var(--down)" class="wick"/>
<rect x="452.99" y="498.0" width="2.34" height="9.6" fill="var(--down)"/>
<line x1="457.9" y1="490.6" x2="457.9" y2="506.5" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="498.2" width="2.34" height="7.6" fill="var(--up)"/>
<line x1="461.7" y1="480.8" x2="461.7" y2="497.1" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="484.5" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="465.5" y1="483.6" x2="465.5" y2="496.6" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="485.6" width="2.34" height="7.3" fill="var(--down)"/>
<line x1="469.2" y1="486.8" x2="469.2" y2="495.3" stroke="var(--down)" class="wick"/>
<rect x="468.08" y="489.1" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="473.0" y1="493.2" x2="473.0" y2="510.4" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="495.8" width="2.34" height="14.3" fill="var(--down)"/>
<line x1="476.8" y1="504.7" x2="476.8" y2="517.8" stroke="var(--up)" class="wick"/>
<rect x="475.62" y="509.8" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="480.6" y1="501.9" x2="480.6" y2="516.4" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="503.2" width="2.34" height="6.7" fill="var(--up)"/>
<line x1="484.3" y1="494.4" x2="484.3" y2="508.0" stroke="var(--up)" class="wick"/>
<rect x="483.17" y="504.0" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="488.1" y1="497.9" x2="488.1" y2="517.4" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="502.5" width="2.34" height="14.7" fill="var(--down)"/>
<line x1="491.9" y1="511.4" x2="491.9" y2="530.9" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="518.8" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="495.7" y1="500.4" x2="495.7" y2="526.3" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="501.7" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="499.4" y1="491.6" x2="499.4" y2="503.1" stroke="var(--up)" class="wick"/>
<rect x="498.25" y="491.8" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="503.2" y1="479.4" x2="503.2" y2="495.2" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="481.5" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="507.0" y1="474.2" x2="507.0" y2="481.3" stroke="var(--up)" class="wick"/>
<rect x="505.80" y="477.6" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="510.7" y1="472.2" x2="510.7" y2="481.5" stroke="var(--up)" class="wick"/>
<rect x="509.57" y="475.9" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="514.5" y1="472.4" x2="514.5" y2="483.6" stroke="var(--up)" class="wick"/>
<rect x="513.34" y="472.8" width="2.34" height="7.3" fill="var(--up)"/>
<line x1="518.3" y1="458.7" x2="518.3" y2="475.3" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="460.0" width="2.34" height="14.8" fill="var(--up)"/>
<line x1="522.1" y1="452.1" x2="522.1" y2="461.2" stroke="var(--up)" class="wick"/>
<rect x="520.88" y="454.4" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="525.8" y1="449.5" x2="525.8" y2="455.6" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="453.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="529.6" y1="457.7" x2="529.6" y2="470.5" stroke="var(--down)" class="wick"/>
<rect x="528.43" y="458.2" width="2.34" height="10.9" fill="var(--down)"/>
<line x1="533.4" y1="452.2" x2="533.4" y2="468.0" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="455.1" width="2.34" height="12.8" fill="var(--up)"/>
<line x1="537.1" y1="444.5" x2="537.1" y2="463.4" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="444.5" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="540.9" y1="434.6" x2="540.9" y2="443.8" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="440.0" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="544.7" y1="433.5" x2="544.7" y2="449.3" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="434.6" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="548.5" y1="422.8" x2="548.5" y2="439.5" stroke="var(--up)" class="wick"/>
<rect x="547.29" y="423.3" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="552.2" y1="420.5" x2="552.2" y2="437.0" stroke="var(--down)" class="wick"/>
<rect x="551.06" y="423.6" width="2.34" height="6.4" fill="var(--down)"/>
<line x1="556.0" y1="418.8" x2="556.0" y2="440.1" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="423.1" width="2.34" height="9.9" fill="var(--up)"/>
<line x1="559.8" y1="413.5" x2="559.8" y2="425.3" stroke="var(--up)" class="wick"/>
<rect x="558.60" y="414.4" width="2.34" height="8.1" fill="var(--up)"/>
<line x1="563.5" y1="408.9" x2="563.5" y2="427.3" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="414.7" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="567.3" y1="414.4" x2="567.3" y2="425.3" stroke="var(--down)" class="wick"/>
<rect x="566.15" y="421.3" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="571.1" y1="406.2" x2="571.1" y2="424.5" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="409.6" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="574.9" y1="408.1" x2="574.9" y2="414.3" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="411.1" width="2.34" height="1.4" fill="var(--up)"/>
<line x1="578.6" y1="407.7" x2="578.6" y2="421.5" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="410.6" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="582.4" y1="408.5" x2="582.4" y2="420.1" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="414.1" width="2.34" height="3.4" fill="var(--down)"/>
<line x1="586.2" y1="413.8" x2="586.2" y2="447.3" stroke="var(--down)" class="wick"/>
<rect x="585.01" y="414.4" width="2.34" height="31.1" fill="var(--down)"/>
<line x1="589.9" y1="423.6" x2="589.9" y2="445.9" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="425.2" width="2.34" height="16.6" fill="var(--up)"/>
<line x1="593.7" y1="416.6" x2="593.7" y2="436.8" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="418.1" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="597.5" y1="409.3" x2="597.5" y2="416.8" stroke="var(--up)" class="wick"/>
<rect x="596.32" y="412.3" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="601.3" y1="398.1" x2="601.3" y2="412.5" stroke="var(--up)" class="wick"/>
<rect x="600.09" y="401.6" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="605.0" y1="391.9" x2="605.0" y2="401.8" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="394.2" width="2.34" height="6.8" fill="var(--up)"/>
<line x1="608.8" y1="390.7" x2="608.8" y2="409.1" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="392.1" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="612.6" y1="384.4" x2="612.6" y2="402.8" stroke="var(--up)" class="wick"/>
<rect x="611.41" y="387.6" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="616.3" y1="368.6" x2="616.3" y2="390.0" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="370.2" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="620.1" y1="362.5" x2="620.1" y2="372.4" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="370.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="623.9" y1="359.4" x2="623.9" y2="376.3" stroke="var(--up)" class="wick"/>
<rect x="622.72" y="368.9" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="627.7" y1="349.1" x2="627.7" y2="371.2" stroke="var(--up)" class="wick"/>
<rect x="626.50" y="349.5" width="2.34" height="18.1" fill="var(--up)"/>
<line x1="631.4" y1="339.6" x2="631.4" y2="353.1" stroke="var(--up)" class="wick"/>
<rect x="630.27" y="348.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="635.2" y1="340.5" x2="635.2" y2="370.2" stroke="var(--down)" class="wick"/>
<rect x="634.04" y="345.3" width="2.34" height="23.7" fill="var(--down)"/>
<line x1="639.0" y1="356.5" x2="639.0" y2="390.7" stroke="var(--down)" class="wick"/>
<rect x="637.81" y="362.9" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="642.8" y1="367.0" x2="642.8" y2="404.8" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="377.9" width="2.34" height="20.9" fill="var(--down)"/>
<line x1="646.5" y1="398.3" x2="646.5" y2="432.1" stroke="var(--up)" class="wick"/>
<rect x="645.36" y="399.7" width="2.34" height="32.3" fill="var(--up)"/>
<line x1="650.3" y1="370.7" x2="650.3" y2="401.1" stroke="var(--up)" class="wick"/>
<rect x="649.13" y="372.0" width="2.34" height="26.2" fill="var(--up)"/>
<line x1="654.1" y1="360.0" x2="654.1" y2="373.5" stroke="var(--up)" class="wick"/>
<rect x="652.90" y="364.3" width="2.34" height="7.1" fill="var(--up)"/>
<line x1="657.8" y1="363.4" x2="657.8" y2="378.0" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="364.6" width="2.34" height="4.8" fill="var(--down)"/>
<line x1="661.6" y1="373.5" x2="661.6" y2="402.1" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="373.5" width="2.34" height="27.9" fill="var(--down)"/>
<line x1="665.4" y1="369.3" x2="665.4" y2="400.1" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="370.4" width="2.34" height="26.5" fill="var(--up)"/>
<line x1="669.2" y1="357.4" x2="669.2" y2="376.7" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="362.1" width="2.34" height="11.7" fill="var(--up)"/>
<line x1="672.9" y1="350.3" x2="672.9" y2="364.8" stroke="var(--up)" class="wick"/>
<rect x="671.76" y="356.8" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="676.7" y1="354.3" x2="676.7" y2="367.8" stroke="var(--up)" class="wick"/>
<rect x="675.53" y="356.2" width="2.34" height="2.1" fill="var(--up)"/>
<line x1="680.5" y1="348.8" x2="680.5" y2="363.6" stroke="var(--up)" class="wick"/>
<rect x="679.30" y="349.8" width="2.34" height="8.2" fill="var(--up)"/>
<line x1="684.2" y1="342.9" x2="684.2" y2="353.8" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="345.2" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="688.0" y1="339.0" x2="688.0" y2="355.9" stroke="var(--up)" class="wick"/>
<rect x="686.85" y="344.3" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="691.8" y1="336.0" x2="691.8" y2="357.9" stroke="var(--down)" class="wick"/>
<rect x="690.62" y="340.3" width="2.34" height="12.8" fill="var(--down)"/>
<line x1="695.6" y1="319.3" x2="695.6" y2="357.0" stroke="var(--up)" class="wick"/>
<rect x="694.39" y="320.3" width="2.34" height="33.3" fill="var(--up)"/>
<line x1="699.3" y1="317.9" x2="699.3" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="318.2" width="2.34" height="21.1" fill="var(--down)"/>
<line x1="703.1" y1="325.8" x2="703.1" y2="339.5" stroke="var(--up)" class="wick"/>
<rect x="701.93" y="329.2" width="2.34" height="8.9" fill="var(--up)"/>
<line x1="706.9" y1="321.6" x2="706.9" y2="331.2" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="322.5" width="2.34" height="2.4" fill="var(--up)"/>
<line x1="710.6" y1="302.3" x2="710.6" y2="321.3" stroke="var(--up)" class="wick"/>
<rect x="709.48" y="302.4" width="2.34" height="18.9" fill="var(--up)"/>
<line x1="714.4" y1="296.1" x2="714.4" y2="309.3" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="300.3" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="718.2" y1="291.7" x2="718.2" y2="324.0" stroke="var(--down)" class="wick"/>
<rect x="717.02" y="297.6" width="2.34" height="13.9" fill="var(--down)"/>
<line x1="722.0" y1="295.9" x2="722.0" y2="313.5" stroke="var(--up)" class="wick"/>
<rect x="720.79" y="306.7" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="725.7" y1="309.3" x2="725.7" y2="325.6" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="309.9" width="2.34" height="5.0" fill="var(--up)"/>
<line x1="729.5" y1="297.8" x2="729.5" y2="328.7" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="302.7" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="733.3" y1="307.1" x2="733.3" y2="334.5" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="309.6" width="2.34" height="22.7" fill="var(--up)"/>
<line x1="737.0" y1="294.4" x2="737.0" y2="312.1" stroke="var(--up)" class="wick"/>
<rect x="735.88" y="299.5" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="740.8" y1="299.0" x2="740.8" y2="322.9" stroke="var(--up)" class="wick"/>
<rect x="739.65" y="309.7" width="2.34" height="12.3" fill="var(--up)"/>
<line x1="744.6" y1="302.3" x2="744.6" y2="324.9" stroke="var(--up)" class="wick"/>
<rect x="743.42" y="312.9" width="2.34" height="9.6" fill="var(--up)"/>
<line x1="748.4" y1="296.6" x2="748.4" y2="316.3" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="297.2" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="752.1" y1="294.6" x2="752.1" y2="313.3" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="295.2" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="755.9" y1="309.2" x2="755.9" y2="348.9" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="310.8" width="2.34" height="23.2" fill="var(--down)"/>
<line x1="759.7" y1="329.5" x2="759.7" y2="367.7" stroke="var(--down)" class="wick"/>
<rect x="758.51" y="331.7" width="2.34" height="22.7" fill="var(--down)"/>
<line x1="763.5" y1="364.6" x2="763.5" y2="384.3" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="365.5" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="767.2" y1="362.8" x2="767.2" y2="378.3" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="367.3" width="2.34" height="1.9" fill="var(--up)"/>
<line x1="771.0" y1="351.7" x2="771.0" y2="382.9" stroke="var(--down)" class="wick"/>
<rect x="769.83" y="359.1" width="2.34" height="22.6" fill="var(--down)"/>
<line x1="774.8" y1="369.4" x2="774.8" y2="436.2" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="390.3" width="2.34" height="45.5" fill="var(--down)"/>
<line x1="778.5" y1="385.4" x2="778.5" y2="461.0" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="400.4" width="2.34" height="54.5" fill="var(--up)"/>
<line x1="782.3" y1="387.5" x2="782.3" y2="420.9" stroke="var(--down)" class="wick"/>
<rect x="781.14" y="388.0" width="2.34" height="26.0" fill="var(--down)"/>
<line x1="786.1" y1="379.1" x2="786.1" y2="432.8" stroke="var(--up)" class="wick"/>
<rect x="784.91" y="379.8" width="2.34" height="41.5" fill="var(--up)"/>
<line x1="789.9" y1="359.0" x2="789.9" y2="393.0" stroke="var(--up)" class="wick"/>
<rect x="788.69" y="361.2" width="2.34" height="18.3" fill="var(--up)"/>
<line x1="793.6" y1="357.5" x2="793.6" y2="376.0" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="362.7" width="2.34" height="3.5" fill="var(--up)"/>
<line x1="797.4" y1="322.6" x2="797.4" y2="345.8" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="322.7" width="2.34" height="16.8" fill="var(--up)"/>
<line x1="801.2" y1="321.7" x2="801.2" y2="341.8" stroke="var(--down)" class="wick"/>
<rect x="800.00" y="331.2" width="2.34" height="6.3" fill="var(--down)"/>
<line x1="804.9" y1="317.1" x2="804.9" y2="334.0" stroke="var(--up)" class="wick"/>
<rect x="803.77" y="325.7" width="2.34" height="3.1" fill="var(--up)"/>
<line x1="808.7" y1="310.2" x2="808.7" y2="329.7" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="312.7" width="2.34" height="14.6" fill="var(--up)"/>
<line x1="812.5" y1="304.3" x2="812.5" y2="317.8" stroke="var(--down)" class="wick"/>
<rect x="811.32" y="311.4" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="816.3" y1="306.4" x2="816.3" y2="317.4" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="312.1" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="820.0" y1="288.3" x2="820.0" y2="318.8" stroke="var(--up)" class="wick"/>
<rect x="818.86" y="289.5" width="2.34" height="26.4" fill="var(--up)"/>
<line x1="823.8" y1="278.5" x2="823.8" y2="294.8" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="279.3" width="2.34" height="7.5" fill="var(--up)"/>
<line x1="827.6" y1="277.6" x2="827.6" y2="288.0" stroke="var(--up)" class="wick"/>
<rect x="826.40" y="279.8" width="2.34" height="3.0" fill="var(--up)"/>
<line x1="831.3" y1="267.4" x2="831.3" y2="282.7" stroke="var(--up)" class="wick"/>
<rect x="830.18" y="270.1" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="835.1" y1="261.8" x2="835.1" y2="274.6" stroke="var(--up)" class="wick"/>
<rect x="833.95" y="263.4" width="2.34" height="4.6" fill="var(--up)"/>
<line x1="838.9" y1="252.5" x2="838.9" y2="280.6" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="261.3" width="2.34" height="16.4" fill="var(--down)"/>
<line x1="842.7" y1="252.3" x2="842.7" y2="272.0" stroke="var(--up)" class="wick"/>
<rect x="841.49" y="252.8" width="2.34" height="18.6" fill="var(--up)"/>
<line x1="846.4" y1="241.7" x2="846.4" y2="256.0" stroke="var(--up)" class="wick"/>
<rect x="845.26" y="247.4" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="850.2" y1="246.5" x2="850.2" y2="269.8" stroke="var(--down)" class="wick"/>
<rect x="849.04" y="247.6" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="854.0" y1="243.6" x2="854.0" y2="254.7" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="252.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="857.7" y1="239.4" x2="857.7" y2="265.8" stroke="var(--up)" class="wick"/>
<rect x="856.58" y="244.9" width="2.34" height="19.2" fill="var(--up)"/>
<line x1="861.5" y1="229.9" x2="861.5" y2="244.0" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="231.2" width="2.34" height="10.5" fill="var(--up)"/>
<line x1="865.3" y1="215.4" x2="865.3" y2="233.7" stroke="var(--up)" class="wick"/>
<rect x="864.12" y="215.9" width="2.34" height="12.1" fill="var(--up)"/>
<line x1="869.1" y1="210.5" x2="869.1" y2="229.8" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="216.6" width="2.34" height="3.8" fill="var(--down)"/>
<line x1="872.8" y1="206.7" x2="872.8" y2="220.2" stroke="var(--up)" class="wick"/>
<rect x="871.67" y="211.2" width="2.34" height="5.5" fill="var(--up)"/>
<line x1="876.6" y1="200.6" x2="876.6" y2="229.6" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="207.7" width="2.34" height="21.5" fill="var(--down)"/>
<line x1="880.4" y1="207.9" x2="880.4" y2="228.9" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="214.4" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="884.2" y1="196.2" x2="884.2" y2="219.5" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="198.0" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="887.9" y1="172.5" x2="887.9" y2="188.9" stroke="var(--up)" class="wick"/>
<rect x="886.75" y="181.7" width="2.34" height="5.9" fill="var(--up)"/>
<line x1="891.7" y1="173.8" x2="891.7" y2="218.0" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="174.6" width="2.34" height="29.6" fill="var(--down)"/>
<line x1="895.5" y1="186.6" x2="895.5" y2="221.9" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="193.3" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="899.2" y1="199.8" x2="899.2" y2="238.8" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="211.0" width="2.34" height="16.1" fill="var(--down)"/>
<line x1="903.0" y1="192.9" x2="903.0" y2="220.7" stroke="var(--up)" class="wick"/>
<rect x="901.84" y="192.9" width="2.34" height="27.6" fill="var(--up)"/>
<line x1="906.8" y1="183.1" x2="906.8" y2="200.9" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="186.3" width="2.34" height="12.7" fill="var(--up)"/>
<line x1="910.6" y1="182.4" x2="910.6" y2="201.4" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="184.4" width="2.34" height="13.8" fill="var(--down)"/>
<line x1="914.3" y1="193.6" x2="914.3" y2="214.0" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="194.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="918.1" y1="183.6" x2="918.1" y2="193.0" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="185.8" width="2.34" height="4.5" fill="var(--up)"/>
<line x1="921.9" y1="186.1" x2="921.9" y2="200.6" stroke="var(--down)" class="wick"/>
<rect x="920.70" y="191.4" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="925.6" y1="181.8" x2="925.6" y2="194.0" stroke="var(--up)" class="wick"/>
<rect x="924.47" y="183.4" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="929.4" y1="179.0" x2="929.4" y2="194.8" stroke="var(--down)" class="wick"/>
<rect x="928.25" y="186.3" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="933.2" y1="185.3" x2="933.2" y2="207.0" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="188.7" width="2.34" height="11.2" fill="var(--up)"/>
<line x1="937.0" y1="173.5" x2="937.0" y2="197.1" stroke="var(--down)" class="wick"/>
<rect x="935.79" y="187.8" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="940.7" y1="182.8" x2="940.7" y2="221.2" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="192.8" width="2.34" height="10.6" fill="var(--down)"/>
<line x1="944.5" y1="194.3" x2="944.5" y2="223.0" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="205.8" width="2.34" height="12.7" fill="var(--down)"/>
<line x1="948.3" y1="206.0" x2="948.3" y2="227.6" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="207.9" width="2.34" height="15.3" fill="var(--up)"/>
<line x1="952.0" y1="199.1" x2="952.0" y2="219.1" stroke="var(--down)" class="wick"/>
<rect x="950.88" y="209.3" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="955.8" y1="207.7" x2="955.8" y2="231.7" stroke="var(--up)" class="wick"/>
<rect x="954.65" y="223.5" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="959.6" y1="207.3" x2="959.6" y2="233.7" stroke="var(--down)" class="wick"/>
<rect x="958.42" y="229.8" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="963.4" y1="217.8" x2="963.4" y2="250.5" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="225.0" width="2.34" height="21.6" fill="var(--down)"/>
<line x1="967.1" y1="229.7" x2="967.1" y2="269.6" stroke="var(--down)" class="wick"/>
<rect x="965.96" y="235.7" width="2.34" height="32.7" fill="var(--down)"/>
<line x1="970.9" y1="236.1" x2="970.9" y2="276.5" stroke="var(--up)" class="wick"/>
<rect x="969.74" y="239.4" width="2.34" height="24.5" fill="var(--up)"/>
<line x1="974.7" y1="204.0" x2="974.7" y2="247.7" stroke="var(--up)" class="wick"/>
<rect x="973.51" y="207.4" width="2.34" height="30.1" fill="var(--up)"/>
<line x1="978.4" y1="156.9" x2="978.4" y2="210.7" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="158.5" width="2.34" height="50.6" fill="var(--up)"/>
<line x1="982.2" y1="146.4" x2="982.2" y2="166.9" stroke="var(--up)" class="wick"/>
<rect x="981.05" y="147.0" width="2.34" height="13.1" fill="var(--up)"/>
<line x1="986.0" y1="134.9" x2="986.0" y2="157.8" stroke="var(--up)" class="wick"/>
<rect x="984.82" y="138.3" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="989.8" y1="102.9" x2="989.8" y2="144.6" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="102.9" width="2.34" height="35.4" fill="var(--up)"/>
<line x1="993.5" y1="88.6" x2="993.5" y2="118.8" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="103.6" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="997.3" y1="94.9" x2="997.3" y2="120.0" stroke="var(--up)" class="wick"/>
<rect x="996.14" y="99.9" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="1001.1" y1="76.5" x2="1001.1" y2="94.4" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="80.3" width="2.34" height="11.9" fill="var(--up)"/>
<line x1="1004.9" y1="73.5" x2="1004.9" y2="121.6" stroke="var(--down)" class="wick"/>
<rect x="1003.68" y="80.9" width="2.34" height="38.8" fill="var(--down)"/>
<line x1="1008.6" y1="102.5" x2="1008.6" y2="142.5" stroke="var(--down)" class="wick"/>
<rect x="1007.45" y="108.6" width="2.34" height="5.5" fill="var(--down)"/>
<line x1="1012.4" y1="86.0" x2="1012.4" y2="111.9" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="94.5" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="1016.2" y1="93.1" x2="1016.2" y2="141.4" stroke="var(--down)" class="wick"/>
<rect x="1015.00" y="95.6" width="2.34" height="37.0" fill="var(--down)"/>
<line x1="1019.9" y1="102.5" x2="1019.9" y2="132.8" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="115.9" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="1023.7" y1="101.2" x2="1023.7" y2="125.4" stroke="var(--up)" class="wick"/>
<rect x="1022.54" y="101.9" width="2.34" height="8.8" fill="var(--up)"/>
<line x1="1027.5" y1="100.8" x2="1027.5" y2="134.1" stroke="var(--down)" class="wick"/>
<rect x="1026.31" y="107.9" width="2.34" height="17.7" fill="var(--down)"/>
<line x1="1031.3" y1="114.4" x2="1031.3" y2="144.4" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="119.4" width="2.34" height="23.3" fill="var(--down)"/>
<line x1="1035.0" y1="127.5" x2="1035.0" y2="159.8" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="130.2" width="2.34" height="4.3" fill="var(--up)"/>
<line x1="1038.8" y1="87.6" x2="1038.8" y2="128.8" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="89.1" width="2.34" height="38.7" fill="var(--up)"/>
<line x1="1042.6" y1="83.3" x2="1042.6" y2="99.0" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="87.9" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="1046.3" y1="85.7" x2="1046.3" y2="104.9" stroke="var(--down)" class="wick"/>
<rect x="1045.17" y="86.2" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="1050.1" y1="96.4" x2="1050.1" y2="104.9" stroke="var(--down)" class="wick"/>
<rect x="1048.94" y="98.4" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="60" y1="151.2" x2="1052" y2="151.2" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="145.2" font-size="11.5" fill="var(--support)" font-weight="600">24,703 S1</text>
<text x="1058" y="157.2" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="530.8" x2="1052" y2="530.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="524.8" font-size="11.5" fill="var(--support)" font-weight="600">12,550 S2</text>
<text x="1058" y="536.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<line x1="60" y1="605.8" x2="1052" y2="605.8" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="599.8" font-size="11.5" fill="var(--support)" font-weight="600">10,148 S3</text>
<text x="1058" y="611.8" font-size="9.5" fill="var(--muted)">터치 2회</text>
<circle cx="1052.0" cy="100.3" r="3" fill="var(--ink)"/>
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

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **상승**: 성장주 위험선호 확대, 금리 하락(할인율 완화) 기대와 자주 동행한다.
- **하락**: 성장주 밸류에이션 리레이팅(할인율 상승) 압력, 위험회피 심리와 자주 동행한다.
- 금리 민감도가 커서, 개별 회사 주가의 초과/열위를 볼 때 [`concepts/macroeconomics.md`](../../concepts/macroeconomics.md) "금리가 주가에 닿는 두 개의 경로"를 함께 봐야 회사 고유 이슈와 시장 전체 금리 국면을 구분할 수 있다.

---

## 관련 문서

- [S&P 500](./sp500.md) — 시장 전체 대표값에 더 가까운 짝 지표
- [거시경제 개념 정리](../../concepts/macroeconomics.md) — 금리가 성장주 밸류에이션에 더 크게 작용하는 이유
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — Nasdaq Composite (^IXIC)](https://finance.yahoo.com/quote/%5EIXIC/)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
