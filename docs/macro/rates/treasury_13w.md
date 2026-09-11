# 미국 13주물 국채금리

::: info
최근 5년간 미국 13주(3개월) 단기국채 할인율(`^IRX`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 사실상 연준(미국 중앙은행) 기준금리를 시장 가격으로 보여주는 지표라서, 10년물 국채금리와 함께 보면서 **장단기 금리차(수익률곡선)** 국면을 확인할 때 자주 인용한다.

**왜 10년물과 따로 다루나**: 수익률곡선 이론에 따르면, 만기가 짧은 이 문서의 금리는 주로 **앞으로 정책금리가 어떻게 바뀔지에 대한 기대**를 반영하고, 만기가 긴 10년물 금리는 주로 **장기적인 성장·물가 기대**를 반영한다. 둘 다 "국채금리"라는 이름은 같아도 담고 있는 정보가 다른 셈이다. 두 문서의 가장 최근 값을 직접 빼면(10년물 − 13주물) 대략적인 장단기 스프레드를 계산해 볼 수 있다(이 문서 자체가 스프레드를 자동으로 계산해 주지는 않는다).

⚠️ **정의를 다시 확인해야 한다**: Yahoo Finance의 `^IRX`는 13주 국채의 **할인율(discount yield)** 기준으로 표시된다. 반면 FRED의 `DGS3MO` 같은 다른 출처는 **채권등가수익률(bond-equivalent yield, BEY)** 기준일 수 있어서, 두 값이 소수점 단위에서 서로 다를 수 있다 — DCF 무위험이자율 계산처럼 정밀한 비교가 필요할 때는 이 문서의 값을 그대로 쓰지 말고, 출처마다 어떤 기준으로 계산했는지 다시 확인해야 한다.

:::
---

## 1. 차트 — 최근 5년 주봉

<div class="irx-chart">
<style>
.irx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .dark .irx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
.dark .irx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.irx-chart svg { width:100%; height:auto; display:block; }
.irx-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.irx-chart .title { fill: var(--ink); font-weight:600; }
.irx-chart .grid { stroke: var(--grid); stroke-width:1; }
.irx-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미 국채 13주물 금리(^IRX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미 국채 13주물 금리 (^IRX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-06 ~ 2026-09-10 · 마지막 종가 3.85% (2026-09-10) · 단위 %</text>
<line x1="60" y1="606.3" x2="1052" y2="606.3" class="grid"/>
<text x="52" y="610.3" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="508.1" x2="1052" y2="508.1" class="grid"/>
<text x="52" y="512.1" font-size="11" text-anchor="end" fill="var(--muted)">1.00</text>
<line x1="60" y1="409.8" x2="1052" y2="409.8" class="grid"/>
<text x="52" y="413.8" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="311.5" x2="1052" y2="311.5" class="grid"/>
<text x="52" y="315.5" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="213.2" x2="1052" y2="213.2" class="grid"/>
<text x="52" y="217.2" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="115.0" x2="1052" y2="115.0" class="grid"/>
<text x="52" y="119.0" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
<line x1="61.9" y1="56.0" x2="61.9" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="126.0" y1="56.0" x2="126.0" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="126.0" y1="626.0" x2="126.0" y2="631.0" class="axis"/>
<text x="126.0" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="322.1" y1="56.0" x2="322.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="322.1" y1="626.0" x2="322.1" y2="631.0" class="axis"/>
<text x="322.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="518.3" y1="56.0" x2="518.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="518.3" y1="626.0" x2="518.3" y2="631.0" class="axis"/>
<text x="518.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="718.2" y1="56.0" x2="718.2" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="718.2" y1="626.0" x2="718.2" y2="631.0" class="axis"/>
<text x="718.2" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="914.3" y1="56.0" x2="914.3" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="914.3" y1="626.0" x2="914.3" y2="631.0" class="axis"/>
<text x="914.3" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="602.6" x2="61.9" y2="602.9" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="602.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="602.6" x2="65.7" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="64.49" y="602.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="69.4" y1="602.9" x2="69.4" y2="604.9" stroke="var(--down)" class="wick"/>
<rect x="68.26" y="603.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="73.2" y1="602.9" x2="73.2" y2="604.4" stroke="var(--up)" class="wick"/>
<rect x="72.03" y="603.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="77.0" y1="601.9" x2="77.0" y2="603.6" stroke="var(--up)" class="wick"/>
<rect x="75.80" y="602.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="80.7" y1="601.9" x2="80.7" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="79.58" y="602.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="84.5" y1="601.4" x2="84.5" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="83.35" y="601.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="88.3" y1="601.4" x2="88.3" y2="602.1" stroke="var(--down)" class="wick"/>
<rect x="87.12" y="601.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="92.1" y1="601.6" x2="92.1" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="90.89" y="601.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="95.8" y1="601.9" x2="95.8" y2="602.9" stroke="var(--up)" class="wick"/>
<rect x="94.66" y="602.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="99.6" y1="601.9" x2="99.6" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="98.44" y="601.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="103.4" y1="601.1" x2="103.4" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="102.21" y="602.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="107.1" y1="601.4" x2="107.1" y2="603.4" stroke="var(--up)" class="wick"/>
<rect x="105.98" y="602.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="110.9" y1="600.4" x2="110.9" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="109.75" y="601.4" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="114.7" y1="600.9" x2="114.7" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="113.52" y="601.9" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="118.5" y1="599.5" x2="118.5" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="117.29" y="600.6" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="122.2" y1="600.0" x2="122.2" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="121.07" y="600.2" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="126.0" y1="597.2" x2="126.0" y2="601.4" stroke="var(--up)" class="wick"/>
<rect x="124.84" y="597.7" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="129.8" y1="594.7" x2="129.8" y2="597.7" stroke="var(--up)" class="wick"/>
<rect x="128.61" y="594.7" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="133.6" y1="589.6" x2="133.6" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="132.38" y="590.8" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="137.3" y1="587.4" x2="137.3" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="136.15" y="589.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="141.1" y1="583.9" x2="141.1" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="139.93" y="584.4" width="2.34" height="4.4" fill="var(--up)"/>
<line x1="144.9" y1="568.7" x2="144.9" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="143.70" y="573.1" width="2.34" height="11.6" fill="var(--up)"/>
<line x1="148.6" y1="565.1" x2="148.6" y2="576.1" stroke="var(--down)" class="wick"/>
<rect x="147.47" y="571.5" width="2.34" height="3.6" fill="var(--down)"/>
<line x1="152.4" y1="570.5" x2="152.4" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="151.24" y="574.9" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="156.2" y1="572.4" x2="156.2" y2="579.5" stroke="var(--down)" class="wick"/>
<rect x="155.01" y="575.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="160.0" y1="569.5" x2="160.0" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="158.79" y="570.5" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="163.7" y1="560.6" x2="163.7" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="162.56" y="568.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="167.5" y1="552.8" x2="167.5" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="166.33" y="555.2" width="2.34" height="13.8" fill="var(--up)"/>
<line x1="171.3" y1="547.6" x2="171.3" y2="558.4" stroke="var(--down)" class="wick"/>
<rect x="170.10" y="554.9" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="175.0" y1="540.0" x2="175.0" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="173.87" y="540.7" width="2.34" height="16.5" fill="var(--up)"/>
<line x1="178.8" y1="530.9" x2="178.8" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="177.64" y="532.8" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="182.6" y1="523.3" x2="182.6" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="181.42" y="529.7" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="186.4" y1="520.8" x2="186.4" y2="530.7" stroke="var(--up)" class="wick"/>
<rect x="185.19" y="526.9" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="190.1" y1="514.9" x2="190.1" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="188.96" y="526.3" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="193.9" y1="511.7" x2="193.9" y2="530.4" stroke="var(--up)" class="wick"/>
<rect x="192.73" y="513.7" width="2.34" height="13.3" fill="var(--up)"/>
<line x1="197.7" y1="503.8" x2="197.7" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="196.50" y="510.2" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="201.4" y1="503.4" x2="201.4" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="200.28" y="505.6" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="205.2" y1="494.3" x2="205.2" y2="506.8" stroke="var(--up)" class="wick"/>
<rect x="204.05" y="494.8" width="2.34" height="9.5" fill="var(--up)"/>
<line x1="209.0" y1="479.8" x2="209.0" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="207.82" y="479.8" width="2.34" height="15.7" fill="var(--up)"/>
<line x1="212.8" y1="432.9" x2="212.8" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="211.59" y="457.9" width="2.34" height="17.2" fill="var(--up)"/>
<line x1="216.5" y1="448.1" x2="216.5" y2="463.4" stroke="var(--up)" class="wick"/>
<rect x="215.36" y="449.3" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="220.3" y1="434.6" x2="220.3" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="219.13" y="448.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="224.1" y1="422.8" x2="224.1" y2="448.8" stroke="var(--up)" class="wick"/>
<rect x="222.91" y="425.2" width="2.34" height="22.6" fill="var(--up)"/>
<line x1="227.8" y1="374.1" x2="227.8" y2="425.2" stroke="var(--up)" class="wick"/>
<rect x="226.68" y="386.2" width="2.34" height="38.0" fill="var(--up)"/>
<line x1="231.6" y1="365.6" x2="231.6" y2="385.4" stroke="var(--up)" class="wick"/>
<rect x="230.45" y="374.9" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="235.4" y1="362.1" x2="235.4" y2="397.5" stroke="var(--down)" class="wick"/>
<rect x="234.22" y="371.5" width="2.34" height="9.0" fill="var(--down)"/>
<line x1="239.2" y1="363.6" x2="239.2" y2="383.9" stroke="var(--up)" class="wick"/>
<rect x="237.99" y="369.5" width="2.34" height="11.8" fill="var(--up)"/>
<line x1="242.9" y1="353.0" x2="242.9" y2="368.0" stroke="var(--up)" class="wick"/>
<rect x="241.77" y="360.7" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="246.7" y1="348.1" x2="246.7" y2="366.1" stroke="var(--up)" class="wick"/>
<rect x="245.54" y="352.8" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="250.5" y1="335.6" x2="250.5" y2="352.3" stroke="var(--up)" class="wick"/>
<rect x="249.31" y="335.6" width="2.34" height="16.7" fill="var(--up)"/>
<line x1="254.3" y1="321.0" x2="254.3" y2="336.1" stroke="var(--up)" class="wick"/>
<rect x="253.08" y="329.2" width="2.34" height="6.9" fill="var(--up)"/>
<line x1="258.0" y1="314.2" x2="258.0" y2="329.4" stroke="var(--up)" class="wick"/>
<rect x="256.85" y="314.7" width="2.34" height="14.2" fill="var(--up)"/>
<line x1="261.8" y1="290.6" x2="261.8" y2="317.1" stroke="var(--up)" class="wick"/>
<rect x="260.63" y="304.6" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="265.6" y1="285.7" x2="265.6" y2="309.7" stroke="var(--up)" class="wick"/>
<rect x="264.40" y="300.9" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="269.3" y1="285.5" x2="269.3" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="268.17" y="293.8" width="2.34" height="6.6" fill="var(--up)"/>
<line x1="273.1" y1="280.1" x2="273.1" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="271.94" y="282.7" width="2.34" height="12.6" fill="var(--up)"/>
<line x1="276.9" y1="248.6" x2="276.9" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="275.71" y="249.8" width="2.34" height="33.7" fill="var(--up)"/>
<line x1="280.7" y1="222.1" x2="280.7" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="279.48" y="224.5" width="2.34" height="28.0" fill="var(--up)"/>
<line x1="284.4" y1="215.7" x2="284.4" y2="227.0" stroke="var(--up)" class="wick"/>
<rect x="283.26" y="216.2" width="2.34" height="8.6" fill="var(--up)"/>
<line x1="288.2" y1="207.5" x2="288.2" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="287.03" y="212.0" width="2.34" height="6.2" fill="var(--up)"/>
<line x1="292.0" y1="203.9" x2="292.0" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="290.80" y="207.0" width="2.34" height="5.2" fill="var(--up)"/>
<line x1="295.7" y1="199.7" x2="295.7" y2="208.3" stroke="var(--up)" class="wick"/>
<rect x="294.57" y="200.0" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="299.5" y1="192.1" x2="299.5" y2="205.1" stroke="var(--up)" class="wick"/>
<rect x="298.34" y="196.0" width="2.34" height="5.1" fill="var(--up)"/>
<line x1="303.3" y1="185.7" x2="303.3" y2="199.2" stroke="var(--up)" class="wick"/>
<rect x="302.12" y="192.8" width="2.34" height="3.2" fill="var(--up)"/>
<line x1="307.1" y1="188.7" x2="307.1" y2="202.9" stroke="var(--down)" class="wick"/>
<rect x="305.89" y="195.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="310.8" y1="184.7" x2="310.8" y2="200.2" stroke="var(--down)" class="wick"/>
<rect x="309.66" y="196.0" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="314.6" y1="188.2" x2="314.6" y2="198.7" stroke="var(--up)" class="wick"/>
<rect x="313.43" y="194.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="318.4" y1="179.5" x2="318.4" y2="198.2" stroke="var(--up)" class="wick"/>
<rect x="317.20" y="187.7" width="2.34" height="6.1" fill="var(--up)"/>
<line x1="322.1" y1="162.1" x2="322.1" y2="191.1" stroke="var(--up)" class="wick"/>
<rect x="320.98" y="164.8" width="2.34" height="22.9" fill="var(--up)"/>
<line x1="325.9" y1="156.2" x2="325.9" y2="169.2" stroke="var(--down)" class="wick"/>
<rect x="324.75" y="165.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="329.7" y1="158.9" x2="329.7" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="328.52" y="160.4" width="2.34" height="4.7" fill="var(--up)"/>
<line x1="333.5" y1="156.4" x2="333.5" y2="162.1" stroke="var(--up)" class="wick"/>
<rect x="332.29" y="159.4" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="337.2" y1="156.2" x2="337.2" y2="168.5" stroke="var(--down)" class="wick"/>
<rect x="336.06" y="159.7" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="341.0" y1="150.0" x2="341.0" y2="164.1" stroke="var(--up)" class="wick"/>
<rect x="339.83" y="150.8" width="2.34" height="10.0" fill="var(--up)"/>
<line x1="344.8" y1="145.4" x2="344.8" y2="151.0" stroke="var(--up)" class="wick"/>
<rect x="343.61" y="146.4" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="348.5" y1="143.5" x2="348.5" y2="146.4" stroke="var(--up)" class="wick"/>
<rect x="347.38" y="144.2" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="352.3" y1="141.0" x2="352.3" y2="149.6" stroke="var(--up)" class="wick"/>
<rect x="351.15" y="142.7" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="356.1" y1="126.5" x2="356.1" y2="144.4" stroke="var(--up)" class="wick"/>
<rect x="354.92" y="134.3" width="2.34" height="8.4" fill="var(--up)"/>
<line x1="359.9" y1="136.1" x2="359.9" y2="188.9" stroke="var(--down)" class="wick"/>
<rect x="358.69" y="170.2" width="2.34" height="14.2" fill="var(--down)"/>
<line x1="363.6" y1="146.6" x2="363.6" y2="187.9" stroke="var(--up)" class="wick"/>
<rect x="362.47" y="163.8" width="2.34" height="24.1" fill="var(--up)"/>
<line x1="367.4" y1="147.9" x2="367.4" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="366.24" y="155.7" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="371.2" y1="138.6" x2="371.2" y2="158.2" stroke="var(--up)" class="wick"/>
<rect x="370.01" y="143.5" width="2.34" height="9.0" fill="var(--up)"/>
<line x1="375.0" y1="123.8" x2="375.0" y2="149.4" stroke="var(--up)" class="wick"/>
<rect x="373.78" y="124.5" width="2.34" height="15.2" fill="var(--up)"/>
<line x1="378.7" y1="111.0" x2="378.7" y2="125.8" stroke="var(--up)" class="wick"/>
<rect x="377.55" y="119.9" width="2.34" height="5.6" fill="var(--up)"/>
<line x1="382.5" y1="110.5" x2="382.5" y2="130.4" stroke="var(--down)" class="wick"/>
<rect x="381.33" y="120.4" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="386.3" y1="101.2" x2="386.3" y2="128.7" stroke="var(--up)" class="wick"/>
<rect x="385.10" y="107.1" width="2.34" height="14.9" fill="var(--up)"/>
<line x1="390.0" y1="102.2" x2="390.0" y2="115.5" stroke="var(--down)" class="wick"/>
<rect x="388.87" y="106.1" width="2.34" height="6.1" fill="var(--down)"/>
<line x1="393.8" y1="102.7" x2="393.8" y2="124.8" stroke="var(--up)" class="wick"/>
<rect x="392.64" y="106.6" width="2.34" height="4.9" fill="var(--up)"/>
<line x1="397.6" y1="93.3" x2="397.6" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="396.41" y="103.7" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="401.4" y1="87.9" x2="401.4" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="400.18" y="93.8" width="2.34" height="10.3" fill="var(--up)"/>
<line x1="405.1" y1="95.0" x2="405.1" y2="106.6" stroke="var(--down)" class="wick"/>
<rect x="403.96" y="95.3" width="2.34" height="10.3" fill="var(--down)"/>
<line x1="408.9" y1="102.2" x2="408.9" y2="115.0" stroke="var(--down)" class="wick"/>
<rect x="407.73" y="105.3" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="412.7" y1="101.2" x2="412.7" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="411.50" y="101.4" width="2.34" height="7.2" fill="var(--up)"/>
<line x1="416.4" y1="96.8" x2="416.4" y2="101.9" stroke="var(--up)" class="wick"/>
<rect x="415.27" y="99.9" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="420.2" y1="93.3" x2="420.2" y2="102.4" stroke="var(--up)" class="wick"/>
<rect x="419.04" y="94.0" width="2.34" height="7.4" fill="var(--up)"/>
<line x1="424.0" y1="90.4" x2="424.0" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="422.82" y="93.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="427.8" y1="90.4" x2="427.8" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="426.59" y="90.6" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="431.5" y1="87.6" x2="431.5" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="430.36" y="89.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="435.3" y1="87.9" x2="435.3" y2="93.5" stroke="var(--down)" class="wick"/>
<rect x="434.13" y="89.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="439.1" y1="87.0" x2="439.1" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="437.90" y="88.9" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="442.8" y1="87.0" x2="442.8" y2="88.9" stroke="var(--up)" class="wick"/>
<rect x="441.67" y="87.6" width="2.34" height="1.3" fill="var(--up)"/>
<line x1="446.6" y1="84.0" x2="446.6" y2="88.4" stroke="var(--up)" class="wick"/>
<rect x="445.45" y="84.0" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="450.4" y1="81.6" x2="450.4" y2="93.3" stroke="var(--down)" class="wick"/>
<rect x="449.22" y="83.5" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="454.2" y1="84.5" x2="454.2" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="452.99" y="86.2" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="457.9" y1="84.0" x2="457.9" y2="88.6" stroke="var(--up)" class="wick"/>
<rect x="456.76" y="85.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="461.7" y1="83.5" x2="461.7" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="460.53" y="85.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="465.5" y1="82.2" x2="465.5" y2="86.7" stroke="var(--down)" class="wick"/>
<rect x="464.31" y="84.2" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="469.2" y1="80.8" x2="469.2" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="468.08" y="80.8" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="473.0" y1="80.8" x2="473.0" y2="95.3" stroke="var(--down)" class="wick"/>
<rect x="471.85" y="80.8" width="2.34" height="2.0" fill="var(--down)"/>
<line x1="476.8" y1="81.6" x2="476.8" y2="86.2" stroke="var(--down)" class="wick"/>
<rect x="475.62" y="82.5" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="480.6" y1="84.0" x2="480.6" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="479.39" y="85.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="484.3" y1="83.2" x2="484.3" y2="92.4" stroke="var(--down)" class="wick"/>
<rect x="483.17" y="85.0" width="2.34" height="5.1" fill="var(--down)"/>
<line x1="488.1" y1="87.6" x2="488.1" y2="90.9" stroke="var(--down)" class="wick"/>
<rect x="486.94" y="89.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="491.9" y1="87.4" x2="491.9" y2="92.9" stroke="var(--down)" class="wick"/>
<rect x="490.71" y="90.6" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="495.7" y1="88.4" x2="495.7" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="494.48" y="90.1" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="499.4" y1="88.4" x2="499.4" y2="94.8" stroke="var(--down)" class="wick"/>
<rect x="498.25" y="89.6" width="2.34" height="4.2" fill="var(--down)"/>
<line x1="503.2" y1="90.9" x2="503.2" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="502.02" y="92.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="507.0" y1="89.4" x2="507.0" y2="96.0" stroke="var(--down)" class="wick"/>
<rect x="505.80" y="91.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="510.7" y1="91.1" x2="510.7" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="509.57" y="93.3" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="514.5" y1="91.9" x2="514.5" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="513.34" y="94.3" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="518.3" y1="91.9" x2="518.3" y2="97.0" stroke="var(--up)" class="wick"/>
<rect x="517.11" y="93.3" width="2.34" height="3.6" fill="var(--up)"/>
<line x1="522.1" y1="91.9" x2="522.1" y2="96.3" stroke="var(--down)" class="wick"/>
<rect x="520.88" y="92.6" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="525.8" y1="92.9" x2="525.8" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="524.66" y="94.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="529.6" y1="94.0" x2="529.6" y2="96.5" stroke="var(--up)" class="wick"/>
<rect x="528.43" y="95.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="533.4" y1="93.3" x2="533.4" y2="101.7" stroke="var(--up)" class="wick"/>
<rect x="532.20" y="94.3" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="537.1" y1="92.6" x2="537.1" y2="94.8" stroke="var(--up)" class="wick"/>
<rect x="535.97" y="93.3" width="2.34" height="1.2" fill="var(--up)"/>
<line x1="540.9" y1="90.9" x2="540.9" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="539.74" y="93.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="544.7" y1="91.4" x2="544.7" y2="94.0" stroke="var(--up)" class="wick"/>
<rect x="543.52" y="91.4" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="548.5" y1="90.1" x2="548.5" y2="93.8" stroke="var(--down)" class="wick"/>
<rect x="547.29" y="91.1" width="2.34" height="2.8" fill="var(--down)"/>
<line x1="552.2" y1="92.1" x2="552.2" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="551.06" y="92.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="556.0" y1="90.9" x2="556.0" y2="92.6" stroke="var(--up)" class="wick"/>
<rect x="554.83" y="91.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="559.8" y1="91.1" x2="559.8" y2="97.5" stroke="var(--down)" class="wick"/>
<rect x="558.60" y="91.6" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="563.5" y1="93.0" x2="563.5" y2="96.0" stroke="var(--down)" class="wick"/>
<rect x="562.37" y="93.5" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="567.3" y1="92.6" x2="567.3" y2="96.0" stroke="var(--up)" class="wick"/>
<rect x="566.15" y="93.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="571.1" y1="90.9" x2="571.1" y2="98.8" stroke="var(--up)" class="wick"/>
<rect x="569.92" y="92.4" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="574.9" y1="90.6" x2="574.9" y2="92.1" stroke="var(--up)" class="wick"/>
<rect x="573.69" y="90.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="578.6" y1="89.9" x2="578.6" y2="91.6" stroke="var(--down)" class="wick"/>
<rect x="577.46" y="90.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="582.4" y1="89.9" x2="582.4" y2="94.5" stroke="var(--down)" class="wick"/>
<rect x="581.23" y="91.1" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="586.2" y1="90.9" x2="586.2" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="585.01" y="91.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="589.9" y1="90.9" x2="589.9" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="588.78" y="91.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="593.7" y1="90.6" x2="593.7" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="592.55" y="90.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="597.5" y1="90.4" x2="597.5" y2="91.1" stroke="var(--down)" class="wick"/>
<rect x="596.32" y="90.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="601.3" y1="90.9" x2="601.3" y2="92.6" stroke="var(--down)" class="wick"/>
<rect x="600.09" y="90.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="605.0" y1="90.9" x2="605.0" y2="92.1" stroke="var(--up)" class="wick"/>
<rect x="603.86" y="91.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="608.8" y1="90.9" x2="608.8" y2="94.0" stroke="var(--down)" class="wick"/>
<rect x="607.64" y="91.7" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="612.6" y1="92.2" x2="612.6" y2="94.5" stroke="var(--down)" class="wick"/>
<rect x="611.41" y="93.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="616.3" y1="92.2" x2="616.3" y2="100.2" stroke="var(--up)" class="wick"/>
<rect x="615.18" y="92.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="620.1" y1="92.6" x2="620.1" y2="96.5" stroke="var(--down)" class="wick"/>
<rect x="618.95" y="92.6" width="2.34" height="2.9" fill="var(--down)"/>
<line x1="623.9" y1="95.5" x2="623.9" y2="96.8" stroke="var(--down)" class="wick"/>
<rect x="622.72" y="95.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="627.7" y1="96.0" x2="627.7" y2="101.4" stroke="var(--down)" class="wick"/>
<rect x="626.50" y="96.0" width="2.34" height="3.7" fill="var(--down)"/>
<line x1="631.4" y1="99.7" x2="631.4" y2="114.0" stroke="var(--down)" class="wick"/>
<rect x="630.27" y="99.7" width="2.34" height="12.3" fill="var(--down)"/>
<line x1="635.2" y1="106.6" x2="635.2" y2="123.8" stroke="var(--up)" class="wick"/>
<rect x="634.04" y="107.6" width="2.34" height="12.5" fill="var(--up)"/>
<line x1="639.0" y1="106.8" x2="639.0" y2="117.6" stroke="var(--up)" class="wick"/>
<rect x="637.81" y="107.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="642.8" y1="107.6" x2="642.8" y2="119.4" stroke="var(--down)" class="wick"/>
<rect x="641.58" y="107.8" width="2.34" height="7.2" fill="var(--down)"/>
<line x1="646.5" y1="114.2" x2="646.5" y2="120.1" stroke="var(--down)" class="wick"/>
<rect x="645.36" y="115.0" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="650.3" y1="117.6" x2="650.3" y2="132.7" stroke="var(--down)" class="wick"/>
<rect x="649.13" y="118.4" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="654.1" y1="122.3" x2="654.1" y2="138.6" stroke="var(--down)" class="wick"/>
<rect x="652.90" y="123.3" width="2.34" height="14.9" fill="var(--down)"/>
<line x1="657.8" y1="139.5" x2="657.8" y2="159.9" stroke="var(--down)" class="wick"/>
<rect x="656.67" y="142.2" width="2.34" height="17.5" fill="var(--down)"/>
<line x1="661.6" y1="159.4" x2="661.6" y2="168.2" stroke="var(--down)" class="wick"/>
<rect x="660.44" y="159.7" width="2.34" height="6.2" fill="var(--down)"/>
<line x1="665.4" y1="163.3" x2="665.4" y2="170.0" stroke="var(--up)" class="wick"/>
<rect x="664.21" y="163.6" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="669.2" y1="160.7" x2="669.2" y2="165.1" stroke="var(--up)" class="wick"/>
<rect x="667.99" y="162.6" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="672.9" y1="161.9" x2="672.9" y2="164.3" stroke="var(--down)" class="wick"/>
<rect x="671.76" y="162.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="676.7" y1="162.3" x2="676.7" y2="166.3" stroke="var(--down)" class="wick"/>
<rect x="675.53" y="162.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="680.5" y1="163.3" x2="680.5" y2="174.6" stroke="var(--down)" class="wick"/>
<rect x="679.30" y="163.8" width="2.34" height="10.1" fill="var(--down)"/>
<line x1="684.2" y1="170.5" x2="684.2" y2="175.4" stroke="var(--up)" class="wick"/>
<rect x="683.07" y="171.7" width="2.34" height="2.8" fill="var(--up)"/>
<line x1="688.0" y1="171.5" x2="688.0" y2="176.1" stroke="var(--down)" class="wick"/>
<rect x="686.85" y="172.5" width="2.34" height="2.2" fill="var(--down)"/>
<line x1="691.8" y1="172.0" x2="691.8" y2="174.6" stroke="var(--up)" class="wick"/>
<rect x="690.62" y="172.5" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="695.6" y1="172.7" x2="695.6" y2="177.1" stroke="var(--down)" class="wick"/>
<rect x="694.39" y="172.7" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="699.3" y1="174.2" x2="699.3" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="698.16" y="176.4" width="2.34" height="7.9" fill="var(--down)"/>
<line x1="703.1" y1="184.0" x2="703.1" y2="191.8" stroke="var(--down)" class="wick"/>
<rect x="701.93" y="184.7" width="2.34" height="7.1" fill="var(--down)"/>
<line x1="706.9" y1="189.4" x2="706.9" y2="192.3" stroke="var(--up)" class="wick"/>
<rect x="705.71" y="192.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="710.6" y1="191.1" x2="710.6" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="709.48" y="191.8" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="714.4" y1="191.8" x2="714.4" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="713.25" y="194.3" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="718.2" y1="192.3" x2="718.2" y2="195.1" stroke="var(--up)" class="wick"/>
<rect x="717.02" y="192.3" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="722.0" y1="191.3" x2="722.0" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="720.79" y="191.8" width="2.34" height="2.5" fill="var(--down)"/>
<line x1="725.7" y1="192.1" x2="725.7" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="724.56" y="193.1" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="729.5" y1="193.6" x2="729.5" y2="196.2" stroke="var(--down)" class="wick"/>
<rect x="728.34" y="193.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="733.3" y1="190.8" x2="733.3" y2="194.8" stroke="var(--up)" class="wick"/>
<rect x="732.11" y="190.8" width="2.34" height="3.9" fill="var(--up)"/>
<line x1="737.0" y1="190.1" x2="737.0" y2="193.3" stroke="var(--down)" class="wick"/>
<rect x="735.88" y="191.1" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="740.8" y1="191.3" x2="740.8" y2="193.9" stroke="var(--down)" class="wick"/>
<rect x="739.65" y="192.3" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="744.6" y1="193.3" x2="744.6" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="743.42" y="193.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="748.4" y1="192.8" x2="748.4" y2="195.6" stroke="var(--up)" class="wick"/>
<rect x="747.20" y="193.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="752.1" y1="192.8" x2="752.1" y2="195.1" stroke="var(--down)" class="wick"/>
<rect x="750.97" y="194.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="755.9" y1="193.6" x2="755.9" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="754.74" y="194.8" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="759.7" y1="194.3" x2="759.7" y2="196.0" stroke="var(--up)" class="wick"/>
<rect x="758.51" y="194.8" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="763.5" y1="193.1" x2="763.5" y2="203.9" stroke="var(--down)" class="wick"/>
<rect x="762.28" y="195.4" width="2.34" height="2.7" fill="var(--down)"/>
<line x1="767.2" y1="189.4" x2="767.2" y2="201.6" stroke="var(--up)" class="wick"/>
<rect x="766.06" y="192.3" width="2.34" height="9.1" fill="var(--up)"/>
<line x1="771.0" y1="192.1" x2="771.0" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="769.83" y="193.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="774.8" y1="191.8" x2="774.8" y2="194.6" stroke="var(--down)" class="wick"/>
<rect x="773.60" y="193.1" width="2.34" height="1.2" fill="var(--down)"/>
<line x1="778.5" y1="192.6" x2="778.5" y2="196.5" stroke="var(--up)" class="wick"/>
<rect x="777.37" y="192.8" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="782.3" y1="191.8" x2="782.3" y2="197.2" stroke="var(--up)" class="wick"/>
<rect x="781.14" y="192.1" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="786.1" y1="184.7" x2="786.1" y2="190.1" stroke="var(--down)" class="wick"/>
<rect x="784.91" y="188.4" width="2.34" height="1.6" fill="var(--down)"/>
<line x1="789.9" y1="187.4" x2="789.9" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="788.69" y="189.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="793.6" y1="190.0" x2="793.6" y2="193.6" stroke="var(--up)" class="wick"/>
<rect x="792.46" y="190.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="797.4" y1="189.2" x2="797.4" y2="191.1" stroke="var(--up)" class="wick"/>
<rect x="796.23" y="190.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="801.2" y1="183.3" x2="801.2" y2="190.4" stroke="var(--up)" class="wick"/>
<rect x="800.00" y="189.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="804.9" y1="188.9" x2="804.9" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="803.77" y="188.9" width="2.34" height="5.2" fill="var(--down)"/>
<line x1="808.7" y1="192.8" x2="808.7" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="807.55" y="193.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="812.5" y1="189.7" x2="812.5" y2="195.4" stroke="var(--up)" class="wick"/>
<rect x="811.32" y="189.7" width="2.34" height="5.4" fill="var(--up)"/>
<line x1="816.3" y1="188.7" x2="816.3" y2="190.4" stroke="var(--down)" class="wick"/>
<rect x="815.09" y="189.2" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="820.0" y1="189.4" x2="820.0" y2="192.1" stroke="var(--down)" class="wick"/>
<rect x="818.86" y="190.4" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="823.8" y1="189.2" x2="823.8" y2="191.8" stroke="var(--up)" class="wick"/>
<rect x="822.63" y="189.2" width="2.34" height="1.7" fill="var(--up)"/>
<line x1="827.6" y1="188.7" x2="827.6" y2="199.0" stroke="var(--down)" class="wick"/>
<rect x="826.40" y="189.4" width="2.34" height="6.0" fill="var(--down)"/>
<line x1="831.3" y1="195.7" x2="831.3" y2="201.0" stroke="var(--down)" class="wick"/>
<rect x="830.18" y="195.7" width="2.34" height="4.4" fill="var(--down)"/>
<line x1="835.1" y1="198.8" x2="835.1" y2="204.4" stroke="var(--down)" class="wick"/>
<rect x="833.95" y="200.0" width="2.34" height="2.3" fill="var(--down)"/>
<line x1="838.9" y1="200.2" x2="838.9" y2="205.6" stroke="var(--down)" class="wick"/>
<rect x="837.72" y="202.7" width="2.34" height="1.9" fill="var(--down)"/>
<line x1="842.7" y1="203.1" x2="842.7" y2="209.3" stroke="var(--down)" class="wick"/>
<rect x="841.49" y="203.6" width="2.34" height="5.4" fill="var(--down)"/>
<line x1="846.4" y1="208.8" x2="846.4" y2="223.3" stroke="var(--down)" class="wick"/>
<rect x="845.26" y="209.0" width="2.34" height="13.1" fill="var(--down)"/>
<line x1="850.2" y1="218.8" x2="850.2" y2="223.3" stroke="var(--up)" class="wick"/>
<rect x="849.04" y="220.3" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="854.0" y1="220.1" x2="854.0" y2="233.1" stroke="var(--down)" class="wick"/>
<rect x="852.81" y="220.6" width="2.34" height="4.6" fill="var(--down)"/>
<line x1="857.7" y1="223.3" x2="857.7" y2="229.0" stroke="var(--down)" class="wick"/>
<rect x="856.58" y="225.7" width="2.34" height="1.3" fill="var(--down)"/>
<line x1="861.5" y1="226.5" x2="861.5" y2="229.5" stroke="var(--up)" class="wick"/>
<rect x="860.35" y="227.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="865.3" y1="227.0" x2="865.3" y2="229.2" stroke="var(--down)" class="wick"/>
<rect x="864.12" y="227.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="869.1" y1="226.7" x2="869.1" y2="230.6" stroke="var(--down)" class="wick"/>
<rect x="867.90" y="227.7" width="2.34" height="2.1" fill="var(--down)"/>
<line x1="872.8" y1="230.4" x2="872.8" y2="238.5" stroke="var(--down)" class="wick"/>
<rect x="871.67" y="230.9" width="2.34" height="5.6" fill="var(--down)"/>
<line x1="876.6" y1="234.1" x2="876.6" y2="242.7" stroke="var(--down)" class="wick"/>
<rect x="875.44" y="237.8" width="2.34" height="3.1" fill="var(--down)"/>
<line x1="880.4" y1="232.9" x2="880.4" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="879.21" y="237.1" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="884.2" y1="233.2" x2="884.2" y2="236.0" stroke="var(--up)" class="wick"/>
<rect x="882.98" y="234.1" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="887.9" y1="234.4" x2="887.9" y2="239.1" stroke="var(--down)" class="wick"/>
<rect x="886.75" y="234.9" width="2.34" height="3.9" fill="var(--down)"/>
<line x1="891.7" y1="237.1" x2="891.7" y2="244.2" stroke="var(--down)" class="wick"/>
<rect x="890.53" y="239.8" width="2.34" height="3.2" fill="var(--down)"/>
<line x1="895.5" y1="240.5" x2="895.5" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="894.30" y="242.7" width="2.34" height="9.5" fill="var(--down)"/>
<line x1="899.2" y1="248.8" x2="899.2" y2="259.9" stroke="var(--down)" class="wick"/>
<rect x="898.07" y="250.6" width="2.34" height="9.3" fill="var(--down)"/>
<line x1="903.0" y1="256.8" x2="903.0" y2="261.1" stroke="var(--down)" class="wick"/>
<rect x="901.84" y="259.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="906.8" y1="256.2" x2="906.8" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="905.61" y="258.2" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="910.6" y1="257.0" x2="910.6" y2="259.4" stroke="var(--down)" class="wick"/>
<rect x="909.39" y="258.9" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="914.3" y1="259.1" x2="914.3" y2="261.7" stroke="var(--down)" class="wick"/>
<rect x="913.16" y="259.4" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="918.1" y1="255.7" x2="918.1" y2="260.9" stroke="var(--up)" class="wick"/>
<rect x="916.93" y="256.8" width="2.34" height="4.1" fill="var(--up)"/>
<line x1="921.9" y1="253.5" x2="921.9" y2="257.8" stroke="var(--up)" class="wick"/>
<rect x="920.70" y="254.3" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="925.6" y1="252.7" x2="925.6" y2="257.8" stroke="var(--down)" class="wick"/>
<rect x="924.47" y="254.7" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="929.4" y1="252.7" x2="929.4" y2="255.5" stroke="var(--up)" class="wick"/>
<rect x="928.25" y="253.5" width="2.34" height="2.0" fill="var(--up)"/>
<line x1="933.2" y1="251.9" x2="933.2" y2="254.3" stroke="var(--up)" class="wick"/>
<rect x="932.02" y="253.2" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="937.0" y1="252.1" x2="937.0" y2="253.7" stroke="var(--up)" class="wick"/>
<rect x="935.79" y="253.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="940.7" y1="253.0" x2="940.7" y2="254.7" stroke="var(--down)" class="wick"/>
<rect x="939.56" y="253.0" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="944.5" y1="252.1" x2="944.5" y2="255.7" stroke="var(--down)" class="wick"/>
<rect x="943.33" y="254.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="948.3" y1="251.9" x2="948.3" y2="254.7" stroke="var(--up)" class="wick"/>
<rect x="947.10" y="252.3" width="2.34" height="2.3" fill="var(--up)"/>
<line x1="952.0" y1="250.1" x2="952.0" y2="252.7" stroke="var(--up)" class="wick"/>
<rect x="950.88" y="250.8" width="2.34" height="1.8" fill="var(--up)"/>
<line x1="955.8" y1="249.6" x2="955.8" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="954.65" y="251.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="959.6" y1="251.4" x2="959.6" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="958.42" y="251.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="963.4" y1="249.6" x2="963.4" y2="254.0" stroke="var(--down)" class="wick"/>
<rect x="962.19" y="251.6" width="2.34" height="1.7" fill="var(--down)"/>
<line x1="967.1" y1="250.8" x2="967.1" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="965.96" y="252.6" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="970.9" y1="252.1" x2="970.9" y2="254.0" stroke="var(--down)" class="wick"/>
<rect x="969.74" y="252.6" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="974.7" y1="253.2" x2="974.7" y2="255.5" stroke="var(--down)" class="wick"/>
<rect x="973.51" y="253.5" width="2.34" height="1.5" fill="var(--down)"/>
<line x1="978.4" y1="252.3" x2="978.4" y2="254.7" stroke="var(--up)" class="wick"/>
<rect x="977.28" y="253.0" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="982.2" y1="251.6" x2="982.2" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="981.05" y="253.0" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="986.0" y1="253.5" x2="986.0" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="984.82" y="253.5" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="989.8" y1="253.5" x2="989.8" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="988.59" y="253.7" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="993.5" y1="249.6" x2="993.5" y2="253.5" stroke="var(--up)" class="wick"/>
<rect x="992.37" y="250.1" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="997.3" y1="249.1" x2="997.3" y2="251.1" stroke="var(--down)" class="wick"/>
<rect x="996.14" y="250.3" width="2.34" height="1.0" fill="var(--down)"/>
<line x1="1001.1" y1="246.4" x2="1001.1" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="999.91" y="246.9" width="2.34" height="4.2" fill="var(--up)"/>
<line x1="1004.9" y1="243.2" x2="1004.9" y2="246.9" stroke="var(--up)" class="wick"/>
<rect x="1003.68" y="246.4" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1008.6" y1="238.8" x2="1008.6" y2="247.9" stroke="var(--up)" class="wick"/>
<rect x="1007.45" y="245.9" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1012.4" y1="240.0" x2="1012.4" y2="246.7" stroke="var(--up)" class="wick"/>
<rect x="1011.23" y="243.2" width="2.34" height="3.4" fill="var(--up)"/>
<line x1="1016.2" y1="237.8" x2="1016.2" y2="245.5" stroke="var(--up)" class="wick"/>
<rect x="1015.00" y="242.0" width="2.34" height="1.0" fill="var(--up)"/>
<line x1="1019.9" y1="232.4" x2="1019.9" y2="242.4" stroke="var(--up)" class="wick"/>
<rect x="1018.77" y="232.4" width="2.34" height="9.8" fill="var(--up)"/>
<line x1="1023.7" y1="230.9" x2="1023.7" y2="247.9" stroke="var(--down)" class="wick"/>
<rect x="1022.54" y="232.9" width="2.34" height="11.6" fill="var(--down)"/>
<line x1="1027.5" y1="239.3" x2="1027.5" y2="243.9" stroke="var(--up)" class="wick"/>
<rect x="1026.31" y="241.7" width="2.34" height="2.2" fill="var(--up)"/>
<line x1="1031.3" y1="239.8" x2="1031.3" y2="243.4" stroke="var(--down)" class="wick"/>
<rect x="1030.09" y="241.3" width="2.34" height="1.8" fill="var(--down)"/>
<line x1="1035.0" y1="241.0" x2="1035.0" y2="243.2" stroke="var(--up)" class="wick"/>
<rect x="1033.86" y="241.7" width="2.34" height="1.5" fill="var(--up)"/>
<line x1="1038.8" y1="239.3" x2="1038.8" y2="246.7" stroke="var(--up)" class="wick"/>
<rect x="1037.63" y="239.8" width="2.34" height="2.5" fill="var(--up)"/>
<line x1="1042.6" y1="235.1" x2="1042.6" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="1041.40" y="237.1" width="2.34" height="2.9" fill="var(--up)"/>
<line x1="1046.3" y1="228.2" x2="1046.3" y2="236.8" stroke="var(--up)" class="wick"/>
<rect x="1045.17" y="228.5" width="2.34" height="7.9" fill="var(--up)"/>
<line x1="1050.1" y1="228.2" x2="1050.1" y2="232.6" stroke="var(--up)" class="wick"/>
<rect x="1048.94" y="228.5" width="2.34" height="3.7" fill="var(--up)"/>
<line x1="60" y1="187.9" x2="1052" y2="187.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="191.4" font-size="11.5" fill="var(--resistance)" font-weight="600">4.26% R1</text>
<text x="1058" y="203.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="85.8" x2="1052" y2="85.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="89.3" font-size="11.5" fill="var(--resistance)" font-weight="600">5.30% R2</text>
<text x="1058" y="101.3" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="258.3" x2="1052" y2="258.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="252.3" font-size="11.5" fill="var(--support)" font-weight="600">3.54% S1</text>
<text x="1058" y="264.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="228.5" r="3" fill="var(--ink)"/>
<text x="1046.0" y="220.5" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 3.85% (2026-09-10)</text>
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

- **상승**: 연준이 정책금리를 올렸거나 올릴 것으로 기대된다는 신호로 흔히 해석한다 — 사실상 기준금리를 시장 가격으로 보여주는 지표다.
- **하락**: 연준이 정책금리를 내렸거나 내릴 것으로 기대된다는 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 연준이 실제로 직접 정하는 것은 하루짜리(익일물) 기준금리(연방기금금리)다. 13주짜리 국채는 만기가 워낙 짧아서, 그 금리에는 "만기가 길어질수록 추가로 요구하는 보상(기간 프리미엄)"이 거의 섞이지 않고 "앞으로 몇 달 안에 금리가 어떻게 바뀔지에 대한 기대"만 거의 그대로 담긴다. 그래서 앞으로 3개월간 시장이 예상하는 금리 인상·인하 확률을 가장 직접적으로 보여준다.
- 이 금리 하나만 보는 것보다, 10년물 국채금리와의 차이(장단기 금리차)를 함께 보는 경우가 더 많다.

---

*작성일: 2026-09-11*
