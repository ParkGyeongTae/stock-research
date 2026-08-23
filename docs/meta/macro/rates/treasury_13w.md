# 미국 13주물 국채금리

!!! note ""
    최근 5년간 미국 13주(3개월) 단기국채 할인율(`^IRX`)의 주간 흐름을 지지선·저항선과 함께 정리한 참고 자료다. 사실상 연준(미국 중앙은행) 기준금리를 시장 가격으로 보여주는 지표라서, 10년물 국채금리와 함께 보면서 **장단기 금리차(수익률곡선)** 국면을 확인할 때 자주 인용한다.

    **왜 10년물과 따로 다루나**: 수익률곡선 이론에 따르면, 만기가 짧은 이 문서의 금리는 주로 **앞으로 정책금리가 어떻게 바뀔지에 대한 기대**를 반영하고, 만기가 긴 10년물 금리는 주로 **장기적인 성장·물가 기대**를 반영한다. 둘 다 "국채금리"라는 이름은 같아도 담고 있는 정보가 다른 셈이다. 두 문서의 가장 최근 값을 직접 빼면(10년물 − 13주물) 대략적인 장단기 스프레드를 계산해 볼 수 있다(이 문서 자체가 스프레드를 자동으로 계산해 주지는 않는다).

    ⚠️ **정의를 다시 확인해야 한다**: Yahoo Finance의 `^IRX`는 13주 국채의 **할인율(discount yield)** 기준으로 표시된다. 반면 FRED의 `DGS3MO` 같은 다른 출처는 **채권등가수익률(bond-equivalent yield, BEY)** 기준일 수 있어서, 두 값이 소수점 단위에서 서로 다를 수 있다 — DCF 무위험이자율 계산처럼 정밀한 비교가 필요할 때는 이 문서의 값을 그대로 쓰지 말고, 출처마다 어떤 기준으로 계산했는지 다시 확인해야 한다.

---

## 1. 차트 — 최근 5년 주봉

<div class="irx-chart">
<style>
.irx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  body:not([data-md-color-scheme="default"]) .irx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .irx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.irx-chart svg { width:100%; height:auto; display:block; }
.irx-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.irx-chart .title { fill: var(--ink); font-weight:600; }
.irx-chart .grid { stroke: var(--grid); stroke-width:1; }
.irx-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미 국채 13주물 금리(^IRX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미 국채 13주물 금리 (^IRX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-23 ~ 2026-08-17 · 마지막 종가 3.71% (2026-08-17) · 단위 %</text>
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
<line x1="134.1" y1="56.0" x2="134.1" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="134.1" y1="626.0" x2="134.1" y2="631.0" class="axis"/>
<text x="134.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="331.8" y1="56.0" x2="331.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="331.8" y1="626.0" x2="331.8" y2="631.0" class="axis"/>
<text x="331.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="529.4" y1="56.0" x2="529.4" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="529.4" y1="626.0" x2="529.4" y2="631.0" class="axis"/>
<text x="529.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="730.8" y1="56.0" x2="730.8" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="730.8" y1="626.0" x2="730.8" y2="631.0" class="axis"/>
<text x="730.8" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="928.5" y1="56.0" x2="928.5" y2="626.0" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="928.5" y1="626.0" x2="928.5" y2="631.0" class="axis"/>
<text x="928.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="601.4" x2="61.9" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="60.72" y="602.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="65.7" y1="601.9" x2="65.7" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="64.52" y="601.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="69.5" y1="602.4" x2="69.5" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="68.32" y="602.6" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="73.3" y1="602.6" x2="73.3" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="72.12" y="602.6" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="77.1" y1="602.9" x2="77.1" y2="604.9" stroke="var(--down)" class="wick"/>
<rect x="75.93" y="603.4" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="80.9" y1="602.9" x2="80.9" y2="604.4" stroke="var(--up)" class="wick"/>
<rect x="79.73" y="603.6" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="84.7" y1="601.9" x2="84.7" y2="603.6" stroke="var(--up)" class="wick"/>
<rect x="83.53" y="602.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="88.5" y1="601.9" x2="88.5" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="87.33" y="602.4" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="92.3" y1="601.4" x2="92.3" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="91.13" y="601.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="96.1" y1="601.4" x2="96.1" y2="602.1" stroke="var(--down)" class="wick"/>
<rect x="94.93" y="601.4" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="99.9" y1="601.6" x2="99.9" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="98.73" y="601.6" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="103.7" y1="601.9" x2="103.7" y2="602.9" stroke="var(--up)" class="wick"/>
<rect x="102.53" y="602.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="107.5" y1="601.9" x2="107.5" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="106.33" y="601.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="111.3" y1="601.1" x2="111.3" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="110.13" y="602.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="115.1" y1="601.4" x2="115.1" y2="603.4" stroke="var(--up)" class="wick"/>
<rect x="113.93" y="602.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="118.9" y1="600.4" x2="118.9" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="117.73" y="601.4" width="2.36" height="1.2" fill="var(--up)"/>
<line x1="122.7" y1="600.9" x2="122.7" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="121.53" y="601.9" width="2.36" height="1.5" fill="var(--down)"/>
<line x1="126.5" y1="599.5" x2="126.5" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="125.34" y="600.6" width="2.36" height="2.3" fill="var(--up)"/>
<line x1="130.3" y1="600.0" x2="130.3" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="129.14" y="600.2" width="2.36" height="2.9" fill="var(--down)"/>
<line x1="134.1" y1="597.2" x2="134.1" y2="601.4" stroke="var(--up)" class="wick"/>
<rect x="132.94" y="597.7" width="2.36" height="3.7" fill="var(--up)"/>
<line x1="137.9" y1="594.7" x2="137.9" y2="597.7" stroke="var(--up)" class="wick"/>
<rect x="136.74" y="594.7" width="2.36" height="2.9" fill="var(--up)"/>
<line x1="141.7" y1="589.6" x2="141.7" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="140.54" y="590.8" width="2.36" height="3.4" fill="var(--up)"/>
<line x1="145.5" y1="587.4" x2="145.5" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="144.34" y="589.3" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="149.3" y1="583.9" x2="149.3" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="148.14" y="584.4" width="2.36" height="4.4" fill="var(--up)"/>
<line x1="153.1" y1="568.7" x2="153.1" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="151.94" y="573.1" width="2.36" height="11.6" fill="var(--up)"/>
<line x1="156.9" y1="565.1" x2="156.9" y2="576.1" stroke="var(--down)" class="wick"/>
<rect x="155.74" y="571.5" width="2.36" height="3.6" fill="var(--down)"/>
<line x1="160.7" y1="570.5" x2="160.7" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="159.54" y="574.9" width="2.36" height="2.2" fill="var(--down)"/>
<line x1="164.5" y1="572.4" x2="164.5" y2="579.5" stroke="var(--down)" class="wick"/>
<rect x="163.34" y="575.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="168.3" y1="569.5" x2="168.3" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="167.14" y="570.5" width="2.36" height="4.9" fill="var(--up)"/>
<line x1="172.1" y1="560.6" x2="172.1" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="170.94" y="568.7" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="175.9" y1="552.8" x2="175.9" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="174.75" y="555.2" width="2.36" height="13.8" fill="var(--up)"/>
<line x1="179.7" y1="547.6" x2="179.7" y2="558.4" stroke="var(--down)" class="wick"/>
<rect x="178.55" y="554.9" width="2.36" height="2.3" fill="var(--down)"/>
<line x1="183.5" y1="540.0" x2="183.5" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="182.35" y="540.7" width="2.36" height="16.5" fill="var(--up)"/>
<line x1="187.3" y1="530.9" x2="187.3" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="186.15" y="532.8" width="2.36" height="7.2" fill="var(--up)"/>
<line x1="191.1" y1="523.3" x2="191.1" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="189.95" y="529.7" width="2.36" height="2.9" fill="var(--up)"/>
<line x1="194.9" y1="520.8" x2="194.9" y2="530.7" stroke="var(--up)" class="wick"/>
<rect x="193.75" y="526.9" width="2.36" height="1.3" fill="var(--up)"/>
<line x1="198.7" y1="514.9" x2="198.7" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="197.55" y="526.3" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="202.5" y1="511.7" x2="202.5" y2="530.4" stroke="var(--up)" class="wick"/>
<rect x="201.35" y="513.7" width="2.36" height="13.3" fill="var(--up)"/>
<line x1="206.3" y1="503.8" x2="206.3" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="205.15" y="510.2" width="2.36" height="3.4" fill="var(--up)"/>
<line x1="210.1" y1="503.4" x2="210.1" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="208.95" y="505.6" width="2.36" height="3.9" fill="var(--up)"/>
<line x1="213.9" y1="494.3" x2="213.9" y2="506.8" stroke="var(--up)" class="wick"/>
<rect x="212.75" y="494.8" width="2.36" height="9.5" fill="var(--up)"/>
<line x1="217.7" y1="479.8" x2="217.7" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="216.55" y="479.8" width="2.36" height="15.7" fill="var(--up)"/>
<line x1="221.5" y1="432.9" x2="221.5" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="220.35" y="457.9" width="2.36" height="17.2" fill="var(--up)"/>
<line x1="225.3" y1="448.1" x2="225.3" y2="463.4" stroke="var(--up)" class="wick"/>
<rect x="224.16" y="449.3" width="2.36" height="5.4" fill="var(--up)"/>
<line x1="229.1" y1="434.6" x2="229.1" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="227.96" y="448.8" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="232.9" y1="422.8" x2="232.9" y2="448.8" stroke="var(--up)" class="wick"/>
<rect x="231.76" y="425.2" width="2.36" height="22.6" fill="var(--up)"/>
<line x1="236.7" y1="374.1" x2="236.7" y2="425.2" stroke="var(--up)" class="wick"/>
<rect x="235.56" y="386.2" width="2.36" height="38.0" fill="var(--up)"/>
<line x1="240.5" y1="365.6" x2="240.5" y2="385.4" stroke="var(--up)" class="wick"/>
<rect x="239.36" y="374.9" width="2.36" height="10.0" fill="var(--up)"/>
<line x1="244.3" y1="362.1" x2="244.3" y2="397.5" stroke="var(--down)" class="wick"/>
<rect x="243.16" y="371.5" width="2.36" height="9.0" fill="var(--down)"/>
<line x1="248.1" y1="363.6" x2="248.1" y2="383.9" stroke="var(--up)" class="wick"/>
<rect x="246.96" y="369.5" width="2.36" height="11.8" fill="var(--up)"/>
<line x1="251.9" y1="353.0" x2="251.9" y2="368.0" stroke="var(--up)" class="wick"/>
<rect x="250.76" y="360.7" width="2.36" height="6.6" fill="var(--up)"/>
<line x1="255.7" y1="348.1" x2="255.7" y2="366.1" stroke="var(--up)" class="wick"/>
<rect x="254.56" y="352.8" width="2.36" height="9.0" fill="var(--up)"/>
<line x1="259.5" y1="335.6" x2="259.5" y2="352.3" stroke="var(--up)" class="wick"/>
<rect x="258.36" y="335.6" width="2.36" height="16.7" fill="var(--up)"/>
<line x1="263.3" y1="321.0" x2="263.3" y2="336.1" stroke="var(--up)" class="wick"/>
<rect x="262.16" y="329.2" width="2.36" height="6.9" fill="var(--up)"/>
<line x1="267.1" y1="314.2" x2="267.1" y2="329.4" stroke="var(--up)" class="wick"/>
<rect x="265.96" y="314.7" width="2.36" height="14.2" fill="var(--up)"/>
<line x1="270.9" y1="290.6" x2="270.9" y2="317.1" stroke="var(--up)" class="wick"/>
<rect x="269.76" y="304.6" width="2.36" height="12.5" fill="var(--up)"/>
<line x1="274.7" y1="285.7" x2="274.7" y2="309.7" stroke="var(--up)" class="wick"/>
<rect x="273.57" y="300.9" width="2.36" height="3.7" fill="var(--up)"/>
<line x1="278.5" y1="285.5" x2="278.5" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="277.37" y="293.8" width="2.36" height="6.6" fill="var(--up)"/>
<line x1="282.3" y1="280.1" x2="282.3" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="281.17" y="282.7" width="2.36" height="12.6" fill="var(--up)"/>
<line x1="286.1" y1="248.6" x2="286.1" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="284.97" y="249.8" width="2.36" height="33.7" fill="var(--up)"/>
<line x1="289.9" y1="222.1" x2="289.9" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="288.77" y="224.5" width="2.36" height="28.0" fill="var(--up)"/>
<line x1="293.7" y1="215.7" x2="293.7" y2="227.0" stroke="var(--up)" class="wick"/>
<rect x="292.57" y="216.2" width="2.36" height="8.6" fill="var(--up)"/>
<line x1="297.5" y1="207.5" x2="297.5" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="296.37" y="212.0" width="2.36" height="6.2" fill="var(--up)"/>
<line x1="301.3" y1="203.9" x2="301.3" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="300.17" y="207.0" width="2.36" height="5.2" fill="var(--up)"/>
<line x1="305.1" y1="199.7" x2="305.1" y2="208.3" stroke="var(--up)" class="wick"/>
<rect x="303.97" y="200.0" width="2.36" height="5.6" fill="var(--up)"/>
<line x1="309.0" y1="192.1" x2="309.0" y2="205.1" stroke="var(--up)" class="wick"/>
<rect x="307.77" y="196.0" width="2.36" height="5.1" fill="var(--up)"/>
<line x1="312.8" y1="185.7" x2="312.8" y2="199.2" stroke="var(--up)" class="wick"/>
<rect x="311.57" y="192.8" width="2.36" height="3.2" fill="var(--up)"/>
<line x1="316.6" y1="188.7" x2="316.6" y2="202.9" stroke="var(--down)" class="wick"/>
<rect x="315.37" y="195.7" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="320.4" y1="184.7" x2="320.4" y2="200.2" stroke="var(--down)" class="wick"/>
<rect x="319.17" y="196.0" width="2.36" height="1.2" fill="var(--down)"/>
<line x1="324.2" y1="188.2" x2="324.2" y2="198.7" stroke="var(--up)" class="wick"/>
<rect x="322.98" y="194.3" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="328.0" y1="179.5" x2="328.0" y2="198.2" stroke="var(--up)" class="wick"/>
<rect x="326.78" y="187.7" width="2.36" height="6.1" fill="var(--up)"/>
<line x1="331.8" y1="162.1" x2="331.8" y2="191.1" stroke="var(--up)" class="wick"/>
<rect x="330.58" y="164.8" width="2.36" height="22.9" fill="var(--up)"/>
<line x1="335.6" y1="156.2" x2="335.6" y2="169.2" stroke="var(--down)" class="wick"/>
<rect x="334.38" y="165.1" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="339.4" y1="158.9" x2="339.4" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="338.18" y="160.4" width="2.36" height="4.7" fill="var(--up)"/>
<line x1="343.2" y1="156.4" x2="343.2" y2="162.1" stroke="var(--up)" class="wick"/>
<rect x="341.98" y="159.4" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="347.0" y1="156.2" x2="347.0" y2="168.5" stroke="var(--down)" class="wick"/>
<rect x="345.78" y="159.7" width="2.36" height="2.2" fill="var(--down)"/>
<line x1="350.8" y1="150.0" x2="350.8" y2="164.1" stroke="var(--up)" class="wick"/>
<rect x="349.58" y="150.8" width="2.36" height="10.0" fill="var(--up)"/>
<line x1="354.6" y1="145.4" x2="354.6" y2="151.0" stroke="var(--up)" class="wick"/>
<rect x="353.38" y="146.4" width="2.36" height="3.9" fill="var(--up)"/>
<line x1="358.4" y1="143.5" x2="358.4" y2="146.4" stroke="var(--up)" class="wick"/>
<rect x="357.18" y="144.2" width="2.36" height="2.3" fill="var(--up)"/>
<line x1="362.2" y1="141.0" x2="362.2" y2="149.6" stroke="var(--up)" class="wick"/>
<rect x="360.98" y="142.7" width="2.36" height="2.8" fill="var(--up)"/>
<line x1="366.0" y1="126.5" x2="366.0" y2="144.4" stroke="var(--up)" class="wick"/>
<rect x="364.78" y="134.3" width="2.36" height="8.4" fill="var(--up)"/>
<line x1="369.8" y1="136.1" x2="369.8" y2="188.9" stroke="var(--down)" class="wick"/>
<rect x="368.58" y="170.2" width="2.36" height="14.2" fill="var(--down)"/>
<line x1="373.6" y1="146.6" x2="373.6" y2="187.9" stroke="var(--up)" class="wick"/>
<rect x="372.38" y="163.8" width="2.36" height="24.1" fill="var(--up)"/>
<line x1="377.4" y1="147.9" x2="377.4" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="376.19" y="155.7" width="2.36" height="2.5" fill="var(--up)"/>
<line x1="381.2" y1="138.6" x2="381.2" y2="158.2" stroke="var(--up)" class="wick"/>
<rect x="379.99" y="143.5" width="2.36" height="9.0" fill="var(--up)"/>
<line x1="385.0" y1="123.8" x2="385.0" y2="149.4" stroke="var(--up)" class="wick"/>
<rect x="383.79" y="124.5" width="2.36" height="15.2" fill="var(--up)"/>
<line x1="388.8" y1="111.0" x2="388.8" y2="125.8" stroke="var(--up)" class="wick"/>
<rect x="387.59" y="119.9" width="2.36" height="5.6" fill="var(--up)"/>
<line x1="392.6" y1="110.5" x2="392.6" y2="130.4" stroke="var(--down)" class="wick"/>
<rect x="391.39" y="120.4" width="2.36" height="2.2" fill="var(--down)"/>
<line x1="396.4" y1="101.2" x2="396.4" y2="128.7" stroke="var(--up)" class="wick"/>
<rect x="395.19" y="107.1" width="2.36" height="14.9" fill="var(--up)"/>
<line x1="400.2" y1="102.2" x2="400.2" y2="115.5" stroke="var(--down)" class="wick"/>
<rect x="398.99" y="106.1" width="2.36" height="6.1" fill="var(--down)"/>
<line x1="404.0" y1="102.7" x2="404.0" y2="124.8" stroke="var(--up)" class="wick"/>
<rect x="402.79" y="106.6" width="2.36" height="4.9" fill="var(--up)"/>
<line x1="407.8" y1="93.3" x2="407.8" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="406.59" y="103.7" width="2.36" height="1.7" fill="var(--up)"/>
<line x1="411.6" y1="87.9" x2="411.6" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="410.39" y="93.8" width="2.36" height="10.3" fill="var(--up)"/>
<line x1="415.4" y1="95.0" x2="415.4" y2="106.6" stroke="var(--down)" class="wick"/>
<rect x="414.19" y="95.3" width="2.36" height="10.3" fill="var(--down)"/>
<line x1="419.2" y1="102.2" x2="419.2" y2="115.0" stroke="var(--down)" class="wick"/>
<rect x="417.99" y="105.3" width="2.36" height="3.2" fill="var(--down)"/>
<line x1="423.0" y1="101.2" x2="423.0" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="421.79" y="101.4" width="2.36" height="7.2" fill="var(--up)"/>
<line x1="426.8" y1="96.8" x2="426.8" y2="101.9" stroke="var(--up)" class="wick"/>
<rect x="425.60" y="99.9" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="430.6" y1="93.3" x2="430.6" y2="102.4" stroke="var(--up)" class="wick"/>
<rect x="429.40" y="94.0" width="2.36" height="7.4" fill="var(--up)"/>
<line x1="434.4" y1="90.4" x2="434.4" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="433.20" y="93.8" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="438.2" y1="90.4" x2="438.2" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="437.00" y="90.6" width="2.36" height="2.5" fill="var(--up)"/>
<line x1="442.0" y1="87.6" x2="442.0" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="440.80" y="89.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="445.8" y1="87.9" x2="445.8" y2="93.5" stroke="var(--down)" class="wick"/>
<rect x="444.60" y="89.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="449.6" y1="87.0" x2="449.6" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="448.40" y="88.9" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="453.4" y1="87.0" x2="453.4" y2="88.9" stroke="var(--up)" class="wick"/>
<rect x="452.20" y="87.6" width="2.36" height="1.3" fill="var(--up)"/>
<line x1="457.2" y1="84.0" x2="457.2" y2="88.4" stroke="var(--up)" class="wick"/>
<rect x="456.00" y="84.0" width="2.36" height="3.6" fill="var(--up)"/>
<line x1="461.0" y1="81.6" x2="461.0" y2="93.3" stroke="var(--down)" class="wick"/>
<rect x="459.80" y="83.5" width="2.36" height="5.1" fill="var(--down)"/>
<line x1="464.8" y1="84.5" x2="464.8" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="463.60" y="86.2" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="468.6" y1="84.0" x2="468.6" y2="88.6" stroke="var(--up)" class="wick"/>
<rect x="467.40" y="85.7" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="472.4" y1="83.5" x2="472.4" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="471.20" y="85.0" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="476.2" y1="82.2" x2="476.2" y2="86.7" stroke="var(--down)" class="wick"/>
<rect x="475.01" y="84.2" width="2.36" height="1.3" fill="var(--down)"/>
<line x1="480.0" y1="80.8" x2="480.0" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="478.81" y="80.8" width="2.36" height="3.7" fill="var(--up)"/>
<line x1="483.8" y1="80.8" x2="483.8" y2="95.3" stroke="var(--down)" class="wick"/>
<rect x="482.61" y="80.8" width="2.36" height="2.0" fill="var(--down)"/>
<line x1="487.6" y1="81.6" x2="487.6" y2="86.2" stroke="var(--down)" class="wick"/>
<rect x="486.41" y="82.5" width="2.36" height="2.9" fill="var(--down)"/>
<line x1="491.4" y1="84.0" x2="491.4" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="490.21" y="85.0" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="495.2" y1="83.2" x2="495.2" y2="92.4" stroke="var(--down)" class="wick"/>
<rect x="494.01" y="85.0" width="2.36" height="5.1" fill="var(--down)"/>
<line x1="499.0" y1="87.6" x2="499.0" y2="90.9" stroke="var(--down)" class="wick"/>
<rect x="497.81" y="89.6" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="502.8" y1="87.4" x2="502.8" y2="92.9" stroke="var(--down)" class="wick"/>
<rect x="501.61" y="90.6" width="2.36" height="1.5" fill="var(--down)"/>
<line x1="506.6" y1="88.4" x2="506.6" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="505.41" y="90.1" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="510.4" y1="88.4" x2="510.4" y2="94.8" stroke="var(--down)" class="wick"/>
<rect x="509.21" y="89.6" width="2.36" height="4.2" fill="var(--down)"/>
<line x1="514.2" y1="90.9" x2="514.2" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="513.01" y="92.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="518.0" y1="89.4" x2="518.0" y2="96.0" stroke="var(--down)" class="wick"/>
<rect x="516.81" y="91.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="521.8" y1="91.1" x2="521.8" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="520.61" y="93.3" width="2.36" height="1.2" fill="var(--down)"/>
<line x1="525.6" y1="91.9" x2="525.6" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="524.42" y="94.3" width="2.36" height="2.9" fill="var(--down)"/>
<line x1="529.4" y1="91.9" x2="529.4" y2="97.0" stroke="var(--up)" class="wick"/>
<rect x="528.22" y="93.3" width="2.36" height="3.6" fill="var(--up)"/>
<line x1="533.2" y1="91.9" x2="533.2" y2="96.3" stroke="var(--down)" class="wick"/>
<rect x="532.02" y="92.6" width="2.36" height="2.9" fill="var(--down)"/>
<line x1="537.0" y1="92.9" x2="537.0" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="535.82" y="94.5" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="540.8" y1="94.0" x2="540.8" y2="96.5" stroke="var(--up)" class="wick"/>
<rect x="539.62" y="95.3" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="544.6" y1="93.3" x2="544.6" y2="101.7" stroke="var(--up)" class="wick"/>
<rect x="543.42" y="94.3" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="548.4" y1="92.6" x2="548.4" y2="94.8" stroke="var(--up)" class="wick"/>
<rect x="547.22" y="93.3" width="2.36" height="1.2" fill="var(--up)"/>
<line x1="552.2" y1="90.9" x2="552.2" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="551.02" y="93.0" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="556.0" y1="91.4" x2="556.0" y2="94.0" stroke="var(--up)" class="wick"/>
<rect x="554.82" y="91.4" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="559.8" y1="90.1" x2="559.8" y2="93.8" stroke="var(--down)" class="wick"/>
<rect x="558.62" y="91.1" width="2.36" height="2.8" fill="var(--down)"/>
<line x1="563.6" y1="92.1" x2="563.6" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="562.42" y="92.6" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="567.4" y1="90.9" x2="567.4" y2="92.6" stroke="var(--up)" class="wick"/>
<rect x="566.22" y="91.6" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="571.2" y1="91.1" x2="571.2" y2="97.5" stroke="var(--down)" class="wick"/>
<rect x="570.02" y="91.6" width="2.36" height="1.8" fill="var(--down)"/>
<line x1="575.0" y1="93.0" x2="575.0" y2="96.0" stroke="var(--down)" class="wick"/>
<rect x="573.83" y="93.5" width="2.36" height="1.5" fill="var(--down)"/>
<line x1="578.8" y1="92.6" x2="578.8" y2="96.0" stroke="var(--up)" class="wick"/>
<rect x="577.63" y="93.8" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="582.6" y1="90.9" x2="582.6" y2="98.8" stroke="var(--up)" class="wick"/>
<rect x="581.43" y="92.4" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="586.4" y1="90.6" x2="586.4" y2="92.1" stroke="var(--up)" class="wick"/>
<rect x="585.23" y="90.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="590.2" y1="89.9" x2="590.2" y2="91.6" stroke="var(--down)" class="wick"/>
<rect x="589.03" y="90.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="594.0" y1="89.9" x2="594.0" y2="94.5" stroke="var(--down)" class="wick"/>
<rect x="592.83" y="91.1" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="597.8" y1="90.9" x2="597.8" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="596.63" y="91.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="601.6" y1="90.9" x2="601.6" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="600.43" y="91.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="605.4" y1="90.6" x2="605.4" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="604.23" y="90.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="609.2" y1="90.4" x2="609.2" y2="91.1" stroke="var(--down)" class="wick"/>
<rect x="608.03" y="90.6" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="613.0" y1="90.9" x2="613.0" y2="92.6" stroke="var(--down)" class="wick"/>
<rect x="611.83" y="90.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="616.8" y1="90.9" x2="616.8" y2="92.1" stroke="var(--up)" class="wick"/>
<rect x="615.63" y="91.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="620.6" y1="90.9" x2="620.6" y2="94.0" stroke="var(--down)" class="wick"/>
<rect x="619.43" y="91.7" width="2.36" height="2.2" fill="var(--down)"/>
<line x1="624.4" y1="92.2" x2="624.4" y2="94.5" stroke="var(--down)" class="wick"/>
<rect x="623.24" y="93.8" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="628.2" y1="92.2" x2="628.2" y2="100.2" stroke="var(--up)" class="wick"/>
<rect x="627.04" y="92.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="632.0" y1="92.6" x2="632.0" y2="96.5" stroke="var(--down)" class="wick"/>
<rect x="630.84" y="92.6" width="2.36" height="2.9" fill="var(--down)"/>
<line x1="635.8" y1="95.5" x2="635.8" y2="96.8" stroke="var(--down)" class="wick"/>
<rect x="634.64" y="95.8" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="639.6" y1="96.0" x2="639.6" y2="101.4" stroke="var(--down)" class="wick"/>
<rect x="638.44" y="96.0" width="2.36" height="3.7" fill="var(--down)"/>
<line x1="643.4" y1="99.7" x2="643.4" y2="114.0" stroke="var(--down)" class="wick"/>
<rect x="642.24" y="99.7" width="2.36" height="12.3" fill="var(--down)"/>
<line x1="647.2" y1="106.6" x2="647.2" y2="123.8" stroke="var(--up)" class="wick"/>
<rect x="646.04" y="107.6" width="2.36" height="12.5" fill="var(--up)"/>
<line x1="651.0" y1="106.8" x2="651.0" y2="117.6" stroke="var(--up)" class="wick"/>
<rect x="649.84" y="107.6" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="654.8" y1="107.6" x2="654.8" y2="119.4" stroke="var(--down)" class="wick"/>
<rect x="653.64" y="107.8" width="2.36" height="7.2" fill="var(--down)"/>
<line x1="658.6" y1="114.2" x2="658.6" y2="120.1" stroke="var(--down)" class="wick"/>
<rect x="657.44" y="115.0" width="2.36" height="3.1" fill="var(--down)"/>
<line x1="662.4" y1="117.6" x2="662.4" y2="132.7" stroke="var(--down)" class="wick"/>
<rect x="661.24" y="118.4" width="2.36" height="5.6" fill="var(--down)"/>
<line x1="666.2" y1="122.3" x2="666.2" y2="138.6" stroke="var(--down)" class="wick"/>
<rect x="665.04" y="123.3" width="2.36" height="14.9" fill="var(--down)"/>
<line x1="670.0" y1="139.5" x2="670.0" y2="159.9" stroke="var(--down)" class="wick"/>
<rect x="668.84" y="142.2" width="2.36" height="17.5" fill="var(--down)"/>
<line x1="673.8" y1="159.4" x2="673.8" y2="168.2" stroke="var(--down)" class="wick"/>
<rect x="672.65" y="159.7" width="2.36" height="6.2" fill="var(--down)"/>
<line x1="677.6" y1="163.3" x2="677.6" y2="170.0" stroke="var(--up)" class="wick"/>
<rect x="676.45" y="163.6" width="2.36" height="2.3" fill="var(--up)"/>
<line x1="681.4" y1="160.7" x2="681.4" y2="165.1" stroke="var(--up)" class="wick"/>
<rect x="680.25" y="162.6" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="685.2" y1="161.9" x2="685.2" y2="164.3" stroke="var(--down)" class="wick"/>
<rect x="684.05" y="162.3" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="689.0" y1="162.3" x2="689.0" y2="166.3" stroke="var(--down)" class="wick"/>
<rect x="687.85" y="162.8" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="692.8" y1="163.3" x2="692.8" y2="174.6" stroke="var(--down)" class="wick"/>
<rect x="691.65" y="163.8" width="2.36" height="10.1" fill="var(--down)"/>
<line x1="696.6" y1="170.5" x2="696.6" y2="175.4" stroke="var(--up)" class="wick"/>
<rect x="695.45" y="171.7" width="2.36" height="2.8" fill="var(--up)"/>
<line x1="700.4" y1="171.5" x2="700.4" y2="176.1" stroke="var(--down)" class="wick"/>
<rect x="699.25" y="172.5" width="2.36" height="2.2" fill="var(--down)"/>
<line x1="704.2" y1="172.0" x2="704.2" y2="174.6" stroke="var(--up)" class="wick"/>
<rect x="703.05" y="172.5" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="708.0" y1="172.7" x2="708.0" y2="177.1" stroke="var(--down)" class="wick"/>
<rect x="706.85" y="172.7" width="2.36" height="3.9" fill="var(--down)"/>
<line x1="711.8" y1="174.2" x2="711.8" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="710.65" y="176.4" width="2.36" height="7.9" fill="var(--down)"/>
<line x1="715.6" y1="184.0" x2="715.6" y2="191.8" stroke="var(--down)" class="wick"/>
<rect x="714.45" y="184.7" width="2.36" height="7.1" fill="var(--down)"/>
<line x1="719.4" y1="189.4" x2="719.4" y2="192.3" stroke="var(--up)" class="wick"/>
<rect x="718.25" y="192.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="723.2" y1="191.1" x2="723.2" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="722.06" y="191.8" width="2.36" height="3.9" fill="var(--down)"/>
<line x1="727.0" y1="191.8" x2="727.0" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="725.86" y="194.3" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="730.8" y1="192.3" x2="730.8" y2="195.1" stroke="var(--up)" class="wick"/>
<rect x="729.66" y="192.3" width="2.36" height="2.5" fill="var(--up)"/>
<line x1="734.6" y1="191.3" x2="734.6" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="733.46" y="191.8" width="2.36" height="2.5" fill="var(--down)"/>
<line x1="738.4" y1="192.1" x2="738.4" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="737.26" y="193.1" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="742.2" y1="193.6" x2="742.2" y2="196.2" stroke="var(--down)" class="wick"/>
<rect x="741.06" y="193.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="746.0" y1="190.8" x2="746.0" y2="194.8" stroke="var(--up)" class="wick"/>
<rect x="744.86" y="190.8" width="2.36" height="3.9" fill="var(--up)"/>
<line x1="749.8" y1="190.1" x2="749.8" y2="193.3" stroke="var(--down)" class="wick"/>
<rect x="748.66" y="191.1" width="2.36" height="1.2" fill="var(--down)"/>
<line x1="753.6" y1="191.3" x2="753.6" y2="193.9" stroke="var(--down)" class="wick"/>
<rect x="752.46" y="192.3" width="2.36" height="1.6" fill="var(--down)"/>
<line x1="757.4" y1="193.3" x2="757.4" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="756.26" y="193.6" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="761.2" y1="192.8" x2="761.2" y2="195.6" stroke="var(--up)" class="wick"/>
<rect x="760.06" y="193.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="765.0" y1="192.8" x2="765.0" y2="195.1" stroke="var(--down)" class="wick"/>
<rect x="763.86" y="194.3" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="768.8" y1="193.6" x2="768.8" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="767.66" y="194.8" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="772.6" y1="194.3" x2="772.6" y2="196.0" stroke="var(--up)" class="wick"/>
<rect x="771.47" y="194.8" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="776.4" y1="193.1" x2="776.4" y2="203.9" stroke="var(--down)" class="wick"/>
<rect x="775.27" y="195.4" width="2.36" height="2.7" fill="var(--down)"/>
<line x1="780.2" y1="189.4" x2="780.2" y2="201.6" stroke="var(--up)" class="wick"/>
<rect x="779.07" y="192.3" width="2.36" height="9.1" fill="var(--up)"/>
<line x1="784.0" y1="192.1" x2="784.0" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="782.87" y="193.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="787.8" y1="191.8" x2="787.8" y2="194.6" stroke="var(--down)" class="wick"/>
<rect x="786.67" y="193.1" width="2.36" height="1.2" fill="var(--down)"/>
<line x1="791.6" y1="192.6" x2="791.6" y2="196.5" stroke="var(--up)" class="wick"/>
<rect x="790.47" y="192.8" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="795.4" y1="191.8" x2="795.4" y2="197.2" stroke="var(--up)" class="wick"/>
<rect x="794.27" y="192.1" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="799.2" y1="184.7" x2="799.2" y2="190.1" stroke="var(--down)" class="wick"/>
<rect x="798.07" y="188.4" width="2.36" height="1.6" fill="var(--down)"/>
<line x1="803.0" y1="187.4" x2="803.0" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="801.87" y="189.7" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="806.9" y1="190.0" x2="806.9" y2="193.6" stroke="var(--up)" class="wick"/>
<rect x="805.67" y="190.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="810.7" y1="189.2" x2="810.7" y2="191.1" stroke="var(--up)" class="wick"/>
<rect x="809.47" y="190.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="814.5" y1="183.3" x2="814.5" y2="190.4" stroke="var(--up)" class="wick"/>
<rect x="813.27" y="189.7" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="818.3" y1="188.9" x2="818.3" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="817.07" y="188.9" width="2.36" height="5.2" fill="var(--down)"/>
<line x1="822.1" y1="192.8" x2="822.1" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="820.88" y="193.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="825.9" y1="189.7" x2="825.9" y2="195.4" stroke="var(--up)" class="wick"/>
<rect x="824.68" y="189.7" width="2.36" height="5.4" fill="var(--up)"/>
<line x1="829.7" y1="188.7" x2="829.7" y2="190.4" stroke="var(--down)" class="wick"/>
<rect x="828.48" y="189.2" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="833.5" y1="189.4" x2="833.5" y2="192.1" stroke="var(--down)" class="wick"/>
<rect x="832.28" y="190.4" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="837.3" y1="189.2" x2="837.3" y2="191.8" stroke="var(--up)" class="wick"/>
<rect x="836.08" y="189.2" width="2.36" height="1.7" fill="var(--up)"/>
<line x1="841.1" y1="188.7" x2="841.1" y2="199.0" stroke="var(--down)" class="wick"/>
<rect x="839.88" y="189.4" width="2.36" height="6.0" fill="var(--down)"/>
<line x1="844.9" y1="195.7" x2="844.9" y2="201.0" stroke="var(--down)" class="wick"/>
<rect x="843.68" y="195.7" width="2.36" height="4.4" fill="var(--down)"/>
<line x1="848.7" y1="198.8" x2="848.7" y2="204.4" stroke="var(--down)" class="wick"/>
<rect x="847.48" y="200.0" width="2.36" height="2.3" fill="var(--down)"/>
<line x1="852.5" y1="200.2" x2="852.5" y2="205.6" stroke="var(--down)" class="wick"/>
<rect x="851.28" y="202.7" width="2.36" height="1.9" fill="var(--down)"/>
<line x1="856.3" y1="203.1" x2="856.3" y2="209.3" stroke="var(--down)" class="wick"/>
<rect x="855.08" y="203.6" width="2.36" height="5.4" fill="var(--down)"/>
<line x1="860.1" y1="208.8" x2="860.1" y2="223.3" stroke="var(--down)" class="wick"/>
<rect x="858.88" y="209.0" width="2.36" height="13.1" fill="var(--down)"/>
<line x1="863.9" y1="218.8" x2="863.9" y2="223.3" stroke="var(--up)" class="wick"/>
<rect x="862.68" y="220.3" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="867.7" y1="220.1" x2="867.7" y2="233.1" stroke="var(--down)" class="wick"/>
<rect x="866.48" y="220.6" width="2.36" height="4.6" fill="var(--down)"/>
<line x1="871.5" y1="223.3" x2="871.5" y2="229.0" stroke="var(--down)" class="wick"/>
<rect x="870.29" y="225.7" width="2.36" height="1.3" fill="var(--down)"/>
<line x1="875.3" y1="226.5" x2="875.3" y2="229.5" stroke="var(--up)" class="wick"/>
<rect x="874.09" y="227.2" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="879.1" y1="227.0" x2="879.1" y2="229.2" stroke="var(--down)" class="wick"/>
<rect x="877.89" y="227.0" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="882.9" y1="226.7" x2="882.9" y2="230.6" stroke="var(--down)" class="wick"/>
<rect x="881.69" y="227.7" width="2.36" height="2.1" fill="var(--down)"/>
<line x1="886.7" y1="230.4" x2="886.7" y2="238.5" stroke="var(--down)" class="wick"/>
<rect x="885.49" y="230.9" width="2.36" height="5.6" fill="var(--down)"/>
<line x1="890.5" y1="234.1" x2="890.5" y2="242.7" stroke="var(--down)" class="wick"/>
<rect x="889.29" y="237.8" width="2.36" height="3.1" fill="var(--down)"/>
<line x1="894.3" y1="232.9" x2="894.3" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="893.09" y="237.1" width="2.36" height="2.9" fill="var(--up)"/>
<line x1="898.1" y1="233.2" x2="898.1" y2="236.0" stroke="var(--up)" class="wick"/>
<rect x="896.89" y="234.1" width="2.36" height="1.8" fill="var(--up)"/>
<line x1="901.9" y1="234.4" x2="901.9" y2="239.1" stroke="var(--down)" class="wick"/>
<rect x="900.69" y="234.9" width="2.36" height="3.9" fill="var(--down)"/>
<line x1="905.7" y1="237.1" x2="905.7" y2="244.2" stroke="var(--down)" class="wick"/>
<rect x="904.49" y="239.8" width="2.36" height="3.2" fill="var(--down)"/>
<line x1="909.5" y1="240.5" x2="909.5" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="908.29" y="242.7" width="2.36" height="9.5" fill="var(--down)"/>
<line x1="913.3" y1="248.8" x2="913.3" y2="259.9" stroke="var(--down)" class="wick"/>
<rect x="912.09" y="250.6" width="2.36" height="9.3" fill="var(--down)"/>
<line x1="917.1" y1="256.8" x2="917.1" y2="261.1" stroke="var(--down)" class="wick"/>
<rect x="915.89" y="259.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="920.9" y1="256.2" x2="920.9" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="919.70" y="258.2" width="2.36" height="2.3" fill="var(--up)"/>
<line x1="924.7" y1="257.0" x2="924.7" y2="259.4" stroke="var(--down)" class="wick"/>
<rect x="923.50" y="258.9" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="928.5" y1="259.1" x2="928.5" y2="261.7" stroke="var(--down)" class="wick"/>
<rect x="927.30" y="259.4" width="2.36" height="1.7" fill="var(--down)"/>
<line x1="932.3" y1="255.7" x2="932.3" y2="260.9" stroke="var(--up)" class="wick"/>
<rect x="931.10" y="256.8" width="2.36" height="4.1" fill="var(--up)"/>
<line x1="936.1" y1="253.5" x2="936.1" y2="257.8" stroke="var(--up)" class="wick"/>
<rect x="934.90" y="254.3" width="2.36" height="3.4" fill="var(--up)"/>
<line x1="939.9" y1="252.7" x2="939.9" y2="257.8" stroke="var(--down)" class="wick"/>
<rect x="938.70" y="254.7" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="943.7" y1="252.7" x2="943.7" y2="255.5" stroke="var(--up)" class="wick"/>
<rect x="942.50" y="253.5" width="2.36" height="2.0" fill="var(--up)"/>
<line x1="947.5" y1="251.9" x2="947.5" y2="254.3" stroke="var(--up)" class="wick"/>
<rect x="946.30" y="253.2" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="951.3" y1="252.1" x2="951.3" y2="253.7" stroke="var(--up)" class="wick"/>
<rect x="950.10" y="253.0" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="955.1" y1="253.0" x2="955.1" y2="254.7" stroke="var(--down)" class="wick"/>
<rect x="953.90" y="253.0" width="2.36" height="1.7" fill="var(--down)"/>
<line x1="958.9" y1="252.1" x2="958.9" y2="255.7" stroke="var(--down)" class="wick"/>
<rect x="957.70" y="254.5" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="962.7" y1="251.9" x2="962.7" y2="254.7" stroke="var(--up)" class="wick"/>
<rect x="961.50" y="252.3" width="2.36" height="2.3" fill="var(--up)"/>
<line x1="966.5" y1="250.1" x2="966.5" y2="252.7" stroke="var(--up)" class="wick"/>
<rect x="965.30" y="250.8" width="2.36" height="1.8" fill="var(--up)"/>
<line x1="970.3" y1="249.6" x2="970.3" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="969.11" y="251.6" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="974.1" y1="251.4" x2="974.1" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="972.91" y="251.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="977.9" y1="249.6" x2="977.9" y2="254.0" stroke="var(--down)" class="wick"/>
<rect x="976.71" y="251.6" width="2.36" height="1.7" fill="var(--down)"/>
<line x1="981.7" y1="250.8" x2="981.7" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="980.51" y="252.6" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="985.5" y1="252.1" x2="985.5" y2="254.0" stroke="var(--down)" class="wick"/>
<rect x="984.31" y="252.6" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="989.3" y1="253.2" x2="989.3" y2="255.5" stroke="var(--down)" class="wick"/>
<rect x="988.11" y="253.5" width="2.36" height="1.5" fill="var(--down)"/>
<line x1="993.1" y1="252.3" x2="993.1" y2="254.7" stroke="var(--up)" class="wick"/>
<rect x="991.91" y="253.0" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="996.9" y1="251.6" x2="996.9" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="995.71" y="253.0" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="1000.7" y1="253.5" x2="1000.7" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="999.51" y="253.5" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="1004.5" y1="253.5" x2="1004.5" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="1003.31" y="253.7" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="1008.3" y1="249.6" x2="1008.3" y2="253.5" stroke="var(--up)" class="wick"/>
<rect x="1007.11" y="250.1" width="2.36" height="3.4" fill="var(--up)"/>
<line x1="1012.1" y1="249.1" x2="1012.1" y2="251.1" stroke="var(--down)" class="wick"/>
<rect x="1010.91" y="250.3" width="2.36" height="1.0" fill="var(--down)"/>
<line x1="1015.9" y1="246.4" x2="1015.9" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="1014.71" y="246.9" width="2.36" height="4.2" fill="var(--up)"/>
<line x1="1019.7" y1="243.2" x2="1019.7" y2="246.9" stroke="var(--up)" class="wick"/>
<rect x="1018.52" y="246.4" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="1023.5" y1="238.8" x2="1023.5" y2="247.9" stroke="var(--up)" class="wick"/>
<rect x="1022.32" y="245.9" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="1027.3" y1="240.0" x2="1027.3" y2="246.7" stroke="var(--up)" class="wick"/>
<rect x="1026.12" y="243.2" width="2.36" height="3.4" fill="var(--up)"/>
<line x1="1031.1" y1="237.8" x2="1031.1" y2="245.5" stroke="var(--up)" class="wick"/>
<rect x="1029.92" y="242.0" width="2.36" height="1.0" fill="var(--up)"/>
<line x1="1034.9" y1="232.4" x2="1034.9" y2="242.4" stroke="var(--up)" class="wick"/>
<rect x="1033.72" y="232.4" width="2.36" height="9.8" fill="var(--up)"/>
<line x1="1038.7" y1="230.9" x2="1038.7" y2="247.9" stroke="var(--down)" class="wick"/>
<rect x="1037.52" y="232.9" width="2.36" height="11.6" fill="var(--down)"/>
<line x1="1042.5" y1="239.3" x2="1042.5" y2="243.9" stroke="var(--up)" class="wick"/>
<rect x="1041.32" y="241.7" width="2.36" height="2.2" fill="var(--up)"/>
<line x1="1046.3" y1="239.8" x2="1046.3" y2="243.4" stroke="var(--down)" class="wick"/>
<rect x="1045.12" y="241.3" width="2.36" height="1.8" fill="var(--down)"/>
<line x1="1050.1" y1="241.0" x2="1050.1" y2="243.2" stroke="var(--up)" class="wick"/>
<rect x="1048.92" y="241.7" width="2.36" height="1.5" fill="var(--up)"/>
<line x1="60" y1="187.9" x2="1052" y2="187.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="191.4" font-size="11.5" fill="var(--resistance)" font-weight="600">4.26% R1</text>
<text x="1058" y="203.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="85.8" x2="1052" y2="85.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="89.3" font-size="11.5" fill="var(--resistance)" font-weight="600">5.30% R2</text>
<text x="1058" y="101.3" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="258.3" x2="1052" y2="258.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="252.3" font-size="11.5" fill="var(--support)" font-weight="600">3.54% S1</text>
<text x="1058" y="264.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="241.7" r="3" fill="var(--ink)"/>
<text x="1046.0" y="233.7" font-size="11.5" text-anchor="end" fill="var(--ink)" font-weight="700" paint-order="stroke" stroke="var(--bg)" stroke-width="3">현재 3.71% (2026-08-17)</text>
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

## 관련 문서

- [미국 10년물 국채금리](./treasury_10y.md)
- [미국 30년물 국채금리](./treasury_30y.md)
- [미국 국채금리 3종 비교 (수익률곡선)](./comparison.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md)
- [밸류에이션 개념 정리](../../concepts/valuation.md)
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — 13 Week Treasury Bill (^IRX)](https://finance.yahoo.com/quote/%5EIRX/)
- [미 재무부 금리 (원출처)](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-23)*
