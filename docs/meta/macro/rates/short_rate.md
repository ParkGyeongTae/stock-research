# 13주 단기금리 (US 3M T-Bill) (주봉 5년)

!!! note ""
    최근 5년 미 국채 13주(3개월) 할인율(`^IRX`) 주봉 흐름을 지지선·저항선과 함께 정리한 참고 자료. 특정 회사 문서가 아니라 **여러 회사 문서에서 공통으로 인용하는 거시 참고 차트**다 — 사실상 연준 기준금리의 시장 프록시라, 10년물 국채금리와 함께 봐서 **장단기 금리차(수익률곡선)** 국면을 확인할 때 인용한다.

    **왜 10년물과 따로 두는가**: 수익률곡선 이론에 따르면 단기물(이 문서)은 **정책금리 기대**를, 장기물(10년물)은 **장기 성장·물가 기대**를 주로 반영한다 — 같은 "국채금리"라도 반영하는 정보가 다르다. 두 문서의 최신 종가를 직접 빼면(장기 − 단기) 대략적인 장단기 스프레드를 볼 수 있다(이 스크립트는 스프레드를 자동 계산하지 않는다).

    ⚠️ **정의 확인 필요**: Yahoo Finance의 `^IRX`는 13주 국채의 **할인율(discount yield)** 기준으로 표시된다. FRED의 `DGS3MO` 등 다른 소스는 **채권등가수익률(bond-equivalent yield, BEY)** 기준일 수 있어 두 값이 소수점 이하에서 갈릴 수 있다 — 정밀 비교가 필요한 계산(예: DCF 무위험이자율)에는 이 문서의 값을 그대로 쓰지 말고 출처별 정의를 다시 확인할 것.

---

## 1. 차트 — 최근 5년 주봉

<div class="irx-chart">
<style>
.irx-chart {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --up:#0ca30c; --down:#d03b3b; --support:#2a78d6; --resistance:#eb6834; --ref:#898781;
}
@media (prefers-color-scheme: dark) {
  .irx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
}
[data-md-color-scheme="slate"] .irx-chart { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --up:#0ca30c; --down:#e66767; --support:#3987e5; --resistance:#d95926; --ref:#898781; }
.irx-chart svg { width:100%; height:auto; display:block; }
.irx-chart text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.irx-chart .title { fill: var(--ink); font-weight:600; }
.irx-chart .grid { stroke: var(--grid); stroke-width:1; }
.irx-chart .axis { stroke: var(--axis); stroke-width:1; }
</style>
<svg viewBox="0 0 1200 680" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="13주 단기금리(^IRX) 최근 5년 주봉 캔들차트, 지지선과 저항선 포함">
<rect x="0" y="0" width="1200" height="680" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">13주 단기금리 (^IRX) — 최근 5년 주봉</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-08-16 ~ 2026-08-17 · 마지막 종가 3.70% (2026-08-17) · 단위 %</text>
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
<line x1="61.9" y1="626.0" x2="61.9" y2="631.0" class="axis"/>
<text x="61.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2021</text>
<line x1="137.6" y1="626.0" x2="137.6" y2="631.0" class="axis"/>
<text x="137.6" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="334.5" y1="626.0" x2="334.5" y2="631.0" class="axis"/>
<text x="334.5" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="531.4" y1="626.0" x2="531.4" y2="631.0" class="axis"/>
<text x="531.4" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="732.1" y1="626.0" x2="732.1" y2="631.0" class="axis"/>
<text x="732.1" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="928.9" y1="626.0" x2="928.9" y2="631.0" class="axis"/>
<text x="928.9" y="644.0" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="626.0" x2="1052" y2="626.0" class="axis"/>
<line x1="60" y1="56.0" x2="60" y2="626.0" class="axis"/>
<line x1="61.9" y1="600.9" x2="61.9" y2="602.4" stroke="var(--down)" class="wick"/>
<rect x="60.72" y="600.9" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="65.7" y1="601.4" x2="65.7" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="64.51" y="602.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="69.5" y1="601.9" x2="69.5" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="68.29" y="601.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="73.3" y1="602.4" x2="73.3" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="72.08" y="602.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="77.0" y1="602.6" x2="77.0" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="75.86" y="602.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="80.8" y1="602.9" x2="80.8" y2="604.9" stroke="var(--down)" class="wick"/>
<rect x="79.65" y="603.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="84.6" y1="602.9" x2="84.6" y2="604.4" stroke="var(--up)" class="wick"/>
<rect x="83.44" y="603.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="88.4" y1="601.9" x2="88.4" y2="603.6" stroke="var(--up)" class="wick"/>
<rect x="87.22" y="602.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="92.2" y1="601.9" x2="92.2" y2="602.6" stroke="var(--down)" class="wick"/>
<rect x="91.01" y="602.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="96.0" y1="601.4" x2="96.0" y2="602.1" stroke="var(--up)" class="wick"/>
<rect x="94.80" y="601.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="99.8" y1="601.4" x2="99.8" y2="602.1" stroke="var(--down)" class="wick"/>
<rect x="98.58" y="601.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="103.5" y1="601.6" x2="103.5" y2="602.9" stroke="var(--down)" class="wick"/>
<rect x="102.37" y="601.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="107.3" y1="601.9" x2="107.3" y2="602.9" stroke="var(--up)" class="wick"/>
<rect x="106.15" y="602.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="111.1" y1="601.9" x2="111.1" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="109.94" y="601.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="114.9" y1="601.1" x2="114.9" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="113.73" y="602.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="118.7" y1="601.4" x2="118.7" y2="603.4" stroke="var(--up)" class="wick"/>
<rect x="117.51" y="602.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="122.5" y1="600.4" x2="122.5" y2="602.6" stroke="var(--up)" class="wick"/>
<rect x="121.30" y="601.4" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="126.3" y1="600.9" x2="126.3" y2="603.6" stroke="var(--down)" class="wick"/>
<rect x="125.09" y="601.9" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="130.0" y1="599.5" x2="130.0" y2="603.1" stroke="var(--up)" class="wick"/>
<rect x="128.87" y="600.6" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="133.8" y1="600.0" x2="133.8" y2="604.4" stroke="var(--down)" class="wick"/>
<rect x="132.66" y="600.2" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="137.6" y1="597.2" x2="137.6" y2="601.4" stroke="var(--up)" class="wick"/>
<rect x="136.44" y="597.7" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="141.4" y1="594.7" x2="141.4" y2="597.7" stroke="var(--up)" class="wick"/>
<rect x="140.23" y="594.7" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="145.2" y1="589.6" x2="145.2" y2="594.3" stroke="var(--up)" class="wick"/>
<rect x="144.02" y="590.8" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="149.0" y1="587.4" x2="149.0" y2="591.1" stroke="var(--up)" class="wick"/>
<rect x="147.80" y="589.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="152.8" y1="583.9" x2="152.8" y2="589.6" stroke="var(--up)" class="wick"/>
<rect x="151.59" y="584.4" width="2.35" height="4.4" fill="var(--up)"/>
<line x1="156.5" y1="568.7" x2="156.5" y2="586.7" stroke="var(--up)" class="wick"/>
<rect x="155.38" y="573.1" width="2.35" height="11.6" fill="var(--up)"/>
<line x1="160.3" y1="565.1" x2="160.3" y2="576.1" stroke="var(--down)" class="wick"/>
<rect x="159.16" y="571.5" width="2.35" height="3.6" fill="var(--down)"/>
<line x1="164.1" y1="570.5" x2="164.1" y2="580.3" stroke="var(--down)" class="wick"/>
<rect x="162.95" y="574.9" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="167.9" y1="572.4" x2="167.9" y2="579.5" stroke="var(--down)" class="wick"/>
<rect x="166.73" y="575.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="171.7" y1="569.5" x2="171.7" y2="577.4" stroke="var(--up)" class="wick"/>
<rect x="170.52" y="570.5" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="175.5" y1="560.6" x2="175.5" y2="571.7" stroke="var(--up)" class="wick"/>
<rect x="174.31" y="568.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="179.3" y1="552.8" x2="179.3" y2="569.0" stroke="var(--up)" class="wick"/>
<rect x="178.09" y="555.2" width="2.35" height="13.8" fill="var(--up)"/>
<line x1="183.1" y1="547.6" x2="183.1" y2="558.4" stroke="var(--down)" class="wick"/>
<rect x="181.88" y="554.9" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="186.8" y1="540.0" x2="186.8" y2="557.2" stroke="var(--up)" class="wick"/>
<rect x="185.67" y="540.7" width="2.35" height="16.5" fill="var(--up)"/>
<line x1="190.6" y1="530.9" x2="190.6" y2="540.2" stroke="var(--up)" class="wick"/>
<rect x="189.45" y="532.8" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="194.4" y1="523.3" x2="194.4" y2="534.6" stroke="var(--up)" class="wick"/>
<rect x="193.24" y="529.7" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="198.2" y1="520.8" x2="198.2" y2="530.7" stroke="var(--up)" class="wick"/>
<rect x="197.02" y="526.9" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="202.0" y1="514.9" x2="202.0" y2="531.7" stroke="var(--up)" class="wick"/>
<rect x="200.81" y="526.3" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="205.8" y1="511.7" x2="205.8" y2="530.4" stroke="var(--up)" class="wick"/>
<rect x="204.60" y="513.7" width="2.35" height="13.3" fill="var(--up)"/>
<line x1="209.6" y1="503.8" x2="209.6" y2="513.7" stroke="var(--up)" class="wick"/>
<rect x="208.38" y="510.2" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="213.3" y1="503.4" x2="213.3" y2="510.2" stroke="var(--up)" class="wick"/>
<rect x="212.17" y="505.6" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="217.1" y1="494.3" x2="217.1" y2="506.8" stroke="var(--up)" class="wick"/>
<rect x="215.96" y="494.8" width="2.35" height="9.5" fill="var(--up)"/>
<line x1="220.9" y1="479.8" x2="220.9" y2="495.5" stroke="var(--up)" class="wick"/>
<rect x="219.74" y="479.8" width="2.35" height="15.7" fill="var(--up)"/>
<line x1="224.7" y1="432.9" x2="224.7" y2="475.1" stroke="var(--up)" class="wick"/>
<rect x="223.53" y="457.9" width="2.35" height="17.2" fill="var(--up)"/>
<line x1="228.5" y1="448.1" x2="228.5" y2="463.4" stroke="var(--up)" class="wick"/>
<rect x="227.31" y="449.3" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="232.3" y1="434.6" x2="232.3" y2="451.8" stroke="var(--up)" class="wick"/>
<rect x="231.10" y="448.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="236.1" y1="422.8" x2="236.1" y2="448.8" stroke="var(--up)" class="wick"/>
<rect x="234.89" y="425.2" width="2.35" height="22.6" fill="var(--up)"/>
<line x1="239.8" y1="374.1" x2="239.8" y2="425.2" stroke="var(--up)" class="wick"/>
<rect x="238.67" y="386.2" width="2.35" height="38.0" fill="var(--up)"/>
<line x1="243.6" y1="365.6" x2="243.6" y2="385.4" stroke="var(--up)" class="wick"/>
<rect x="242.46" y="374.9" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="247.4" y1="362.1" x2="247.4" y2="397.5" stroke="var(--down)" class="wick"/>
<rect x="246.25" y="371.5" width="2.35" height="9.0" fill="var(--down)"/>
<line x1="251.2" y1="363.6" x2="251.2" y2="383.9" stroke="var(--up)" class="wick"/>
<rect x="250.03" y="369.5" width="2.35" height="11.8" fill="var(--up)"/>
<line x1="255.0" y1="353.0" x2="255.0" y2="368.0" stroke="var(--up)" class="wick"/>
<rect x="253.82" y="360.7" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="258.8" y1="348.1" x2="258.8" y2="366.1" stroke="var(--up)" class="wick"/>
<rect x="257.60" y="352.8" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="262.6" y1="335.6" x2="262.6" y2="352.3" stroke="var(--up)" class="wick"/>
<rect x="261.39" y="335.6" width="2.35" height="16.7" fill="var(--up)"/>
<line x1="266.4" y1="321.0" x2="266.4" y2="336.1" stroke="var(--up)" class="wick"/>
<rect x="265.18" y="329.2" width="2.35" height="6.9" fill="var(--up)"/>
<line x1="270.1" y1="314.2" x2="270.1" y2="329.4" stroke="var(--up)" class="wick"/>
<rect x="268.96" y="314.7" width="2.35" height="14.2" fill="var(--up)"/>
<line x1="273.9" y1="290.6" x2="273.9" y2="317.1" stroke="var(--up)" class="wick"/>
<rect x="272.75" y="304.6" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="277.7" y1="285.7" x2="277.7" y2="309.7" stroke="var(--up)" class="wick"/>
<rect x="276.54" y="300.9" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="281.5" y1="285.5" x2="281.5" y2="301.9" stroke="var(--up)" class="wick"/>
<rect x="280.32" y="293.8" width="2.35" height="6.6" fill="var(--up)"/>
<line x1="285.3" y1="280.1" x2="285.3" y2="297.8" stroke="var(--up)" class="wick"/>
<rect x="284.11" y="282.7" width="2.35" height="12.6" fill="var(--up)"/>
<line x1="289.1" y1="248.6" x2="289.1" y2="283.7" stroke="var(--up)" class="wick"/>
<rect x="287.89" y="249.8" width="2.35" height="33.7" fill="var(--up)"/>
<line x1="292.9" y1="222.1" x2="292.9" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="291.68" y="224.5" width="2.35" height="28.0" fill="var(--up)"/>
<line x1="296.6" y1="215.7" x2="296.6" y2="227.0" stroke="var(--up)" class="wick"/>
<rect x="295.47" y="216.2" width="2.35" height="8.6" fill="var(--up)"/>
<line x1="300.4" y1="207.5" x2="300.4" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="299.25" y="212.0" width="2.35" height="6.2" fill="var(--up)"/>
<line x1="304.2" y1="203.9" x2="304.2" y2="218.4" stroke="var(--up)" class="wick"/>
<rect x="303.04" y="207.0" width="2.35" height="5.2" fill="var(--up)"/>
<line x1="308.0" y1="199.7" x2="308.0" y2="208.3" stroke="var(--up)" class="wick"/>
<rect x="306.83" y="200.0" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="311.8" y1="192.1" x2="311.8" y2="205.1" stroke="var(--up)" class="wick"/>
<rect x="310.61" y="196.0" width="2.35" height="5.1" fill="var(--up)"/>
<line x1="315.6" y1="185.7" x2="315.6" y2="199.2" stroke="var(--up)" class="wick"/>
<rect x="314.40" y="192.8" width="2.35" height="3.2" fill="var(--up)"/>
<line x1="319.4" y1="188.7" x2="319.4" y2="202.9" stroke="var(--down)" class="wick"/>
<rect x="318.19" y="195.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="323.1" y1="184.7" x2="323.1" y2="200.2" stroke="var(--down)" class="wick"/>
<rect x="321.97" y="196.0" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="326.9" y1="188.2" x2="326.9" y2="198.7" stroke="var(--up)" class="wick"/>
<rect x="325.76" y="194.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="330.7" y1="179.5" x2="330.7" y2="198.2" stroke="var(--up)" class="wick"/>
<rect x="329.54" y="187.7" width="2.35" height="6.1" fill="var(--up)"/>
<line x1="334.5" y1="162.1" x2="334.5" y2="191.1" stroke="var(--up)" class="wick"/>
<rect x="333.33" y="164.8" width="2.35" height="22.9" fill="var(--up)"/>
<line x1="338.3" y1="156.2" x2="338.3" y2="169.2" stroke="var(--down)" class="wick"/>
<rect x="337.12" y="165.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="342.1" y1="158.9" x2="342.1" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="340.90" y="160.4" width="2.35" height="4.7" fill="var(--up)"/>
<line x1="345.9" y1="156.4" x2="345.9" y2="162.1" stroke="var(--up)" class="wick"/>
<rect x="344.69" y="159.4" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="349.6" y1="156.2" x2="349.6" y2="168.5" stroke="var(--down)" class="wick"/>
<rect x="348.48" y="159.7" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="353.4" y1="150.0" x2="353.4" y2="164.1" stroke="var(--up)" class="wick"/>
<rect x="352.26" y="150.8" width="2.35" height="10.0" fill="var(--up)"/>
<line x1="357.2" y1="145.4" x2="357.2" y2="151.0" stroke="var(--up)" class="wick"/>
<rect x="356.05" y="146.4" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="361.0" y1="143.5" x2="361.0" y2="146.4" stroke="var(--up)" class="wick"/>
<rect x="359.83" y="144.2" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="364.8" y1="141.0" x2="364.8" y2="149.6" stroke="var(--up)" class="wick"/>
<rect x="363.62" y="142.7" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="368.6" y1="126.5" x2="368.6" y2="144.4" stroke="var(--up)" class="wick"/>
<rect x="367.41" y="134.3" width="2.35" height="8.4" fill="var(--up)"/>
<line x1="372.4" y1="136.1" x2="372.4" y2="188.9" stroke="var(--down)" class="wick"/>
<rect x="371.19" y="170.2" width="2.35" height="14.2" fill="var(--down)"/>
<line x1="376.2" y1="146.6" x2="376.2" y2="187.9" stroke="var(--up)" class="wick"/>
<rect x="374.98" y="163.8" width="2.35" height="24.1" fill="var(--up)"/>
<line x1="379.9" y1="147.9" x2="379.9" y2="173.9" stroke="var(--up)" class="wick"/>
<rect x="378.77" y="155.7" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="383.7" y1="138.6" x2="383.7" y2="158.2" stroke="var(--up)" class="wick"/>
<rect x="382.55" y="143.5" width="2.35" height="9.0" fill="var(--up)"/>
<line x1="387.5" y1="123.8" x2="387.5" y2="149.4" stroke="var(--up)" class="wick"/>
<rect x="386.34" y="124.5" width="2.35" height="15.2" fill="var(--up)"/>
<line x1="391.3" y1="111.0" x2="391.3" y2="125.8" stroke="var(--up)" class="wick"/>
<rect x="390.12" y="119.9" width="2.35" height="5.6" fill="var(--up)"/>
<line x1="395.1" y1="110.5" x2="395.1" y2="130.4" stroke="var(--down)" class="wick"/>
<rect x="393.91" y="120.4" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="398.9" y1="101.2" x2="398.9" y2="128.7" stroke="var(--up)" class="wick"/>
<rect x="397.70" y="107.1" width="2.35" height="14.9" fill="var(--up)"/>
<line x1="402.7" y1="102.2" x2="402.7" y2="115.5" stroke="var(--down)" class="wick"/>
<rect x="401.48" y="106.1" width="2.35" height="6.1" fill="var(--down)"/>
<line x1="406.4" y1="102.7" x2="406.4" y2="124.8" stroke="var(--up)" class="wick"/>
<rect x="405.27" y="106.6" width="2.35" height="4.9" fill="var(--up)"/>
<line x1="410.2" y1="93.3" x2="410.2" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="409.06" y="103.7" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="414.0" y1="87.9" x2="414.0" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="412.84" y="93.8" width="2.35" height="10.3" fill="var(--up)"/>
<line x1="417.8" y1="95.0" x2="417.8" y2="106.6" stroke="var(--down)" class="wick"/>
<rect x="416.63" y="95.3" width="2.35" height="10.3" fill="var(--down)"/>
<line x1="421.6" y1="102.2" x2="421.6" y2="115.0" stroke="var(--down)" class="wick"/>
<rect x="420.41" y="105.3" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="425.4" y1="101.2" x2="425.4" y2="115.0" stroke="var(--up)" class="wick"/>
<rect x="424.20" y="101.4" width="2.35" height="7.2" fill="var(--up)"/>
<line x1="429.2" y1="96.8" x2="429.2" y2="101.9" stroke="var(--up)" class="wick"/>
<rect x="427.99" y="99.9" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="432.9" y1="93.3" x2="432.9" y2="102.4" stroke="var(--up)" class="wick"/>
<rect x="431.77" y="94.0" width="2.35" height="7.4" fill="var(--up)"/>
<line x1="436.7" y1="90.4" x2="436.7" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="435.56" y="93.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="440.5" y1="90.4" x2="440.5" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="439.35" y="90.6" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="444.3" y1="87.6" x2="444.3" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="443.13" y="89.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="448.1" y1="87.9" x2="448.1" y2="93.5" stroke="var(--down)" class="wick"/>
<rect x="446.92" y="89.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="451.9" y1="87.0" x2="451.9" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="450.70" y="88.9" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="455.7" y1="87.0" x2="455.7" y2="88.9" stroke="var(--up)" class="wick"/>
<rect x="454.49" y="87.6" width="2.35" height="1.3" fill="var(--up)"/>
<line x1="459.5" y1="84.0" x2="459.5" y2="88.4" stroke="var(--up)" class="wick"/>
<rect x="458.28" y="84.0" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="463.2" y1="81.6" x2="463.2" y2="93.3" stroke="var(--down)" class="wick"/>
<rect x="462.06" y="83.5" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="467.0" y1="84.5" x2="467.0" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="465.85" y="86.2" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="470.8" y1="84.0" x2="470.8" y2="88.6" stroke="var(--up)" class="wick"/>
<rect x="469.64" y="85.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="474.6" y1="83.5" x2="474.6" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="473.42" y="85.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="478.4" y1="82.2" x2="478.4" y2="86.7" stroke="var(--down)" class="wick"/>
<rect x="477.21" y="84.2" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="482.2" y1="80.8" x2="482.2" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="480.99" y="80.8" width="2.35" height="3.7" fill="var(--up)"/>
<line x1="486.0" y1="80.8" x2="486.0" y2="95.3" stroke="var(--down)" class="wick"/>
<rect x="484.78" y="80.8" width="2.35" height="2.0" fill="var(--down)"/>
<line x1="489.7" y1="81.6" x2="489.7" y2="86.2" stroke="var(--down)" class="wick"/>
<rect x="488.57" y="82.5" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="493.5" y1="84.0" x2="493.5" y2="95.3" stroke="var(--up)" class="wick"/>
<rect x="492.35" y="85.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="497.3" y1="83.2" x2="497.3" y2="92.4" stroke="var(--down)" class="wick"/>
<rect x="496.14" y="85.0" width="2.35" height="5.1" fill="var(--down)"/>
<line x1="501.1" y1="87.6" x2="501.1" y2="90.9" stroke="var(--down)" class="wick"/>
<rect x="499.93" y="89.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="504.9" y1="87.4" x2="504.9" y2="92.9" stroke="var(--down)" class="wick"/>
<rect x="503.71" y="90.6" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="508.7" y1="88.4" x2="508.7" y2="105.1" stroke="var(--up)" class="wick"/>
<rect x="507.50" y="90.1" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="512.5" y1="88.4" x2="512.5" y2="94.8" stroke="var(--down)" class="wick"/>
<rect x="511.28" y="89.6" width="2.35" height="4.2" fill="var(--down)"/>
<line x1="516.2" y1="90.9" x2="516.2" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="515.07" y="92.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="520.0" y1="89.4" x2="520.0" y2="96.0" stroke="var(--down)" class="wick"/>
<rect x="518.86" y="91.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="523.8" y1="91.1" x2="523.8" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="522.64" y="93.3" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="527.6" y1="91.9" x2="527.6" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="526.43" y="94.3" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="531.4" y1="91.9" x2="531.4" y2="97.0" stroke="var(--up)" class="wick"/>
<rect x="530.22" y="93.3" width="2.35" height="3.6" fill="var(--up)"/>
<line x1="535.2" y1="91.9" x2="535.2" y2="96.3" stroke="var(--down)" class="wick"/>
<rect x="534.00" y="92.6" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="539.0" y1="92.9" x2="539.0" y2="105.1" stroke="var(--down)" class="wick"/>
<rect x="537.79" y="94.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="542.7" y1="94.0" x2="542.7" y2="96.5" stroke="var(--up)" class="wick"/>
<rect x="541.57" y="95.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="546.5" y1="93.3" x2="546.5" y2="101.7" stroke="var(--up)" class="wick"/>
<rect x="545.36" y="94.3" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="550.3" y1="92.6" x2="550.3" y2="94.8" stroke="var(--up)" class="wick"/>
<rect x="549.15" y="93.3" width="2.35" height="1.2" fill="var(--up)"/>
<line x1="554.1" y1="90.9" x2="554.1" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="552.93" y="93.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="557.9" y1="91.4" x2="557.9" y2="94.0" stroke="var(--up)" class="wick"/>
<rect x="556.72" y="91.4" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="561.7" y1="90.1" x2="561.7" y2="93.8" stroke="var(--down)" class="wick"/>
<rect x="560.51" y="91.1" width="2.35" height="2.8" fill="var(--down)"/>
<line x1="565.5" y1="92.1" x2="565.5" y2="94.5" stroke="var(--up)" class="wick"/>
<rect x="564.29" y="92.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="569.3" y1="90.9" x2="569.3" y2="92.6" stroke="var(--up)" class="wick"/>
<rect x="568.08" y="91.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="573.0" y1="91.1" x2="573.0" y2="97.5" stroke="var(--down)" class="wick"/>
<rect x="571.86" y="91.6" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="576.8" y1="93.0" x2="576.8" y2="96.0" stroke="var(--down)" class="wick"/>
<rect x="575.65" y="93.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="580.6" y1="92.6" x2="580.6" y2="96.0" stroke="var(--up)" class="wick"/>
<rect x="579.44" y="93.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="584.4" y1="90.9" x2="584.4" y2="98.8" stroke="var(--up)" class="wick"/>
<rect x="583.22" y="92.4" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="588.2" y1="90.6" x2="588.2" y2="92.1" stroke="var(--up)" class="wick"/>
<rect x="587.01" y="90.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="592.0" y1="89.9" x2="592.0" y2="91.6" stroke="var(--down)" class="wick"/>
<rect x="590.80" y="90.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="595.8" y1="89.9" x2="595.8" y2="94.5" stroke="var(--down)" class="wick"/>
<rect x="594.58" y="91.1" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="599.5" y1="90.9" x2="599.5" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="598.37" y="91.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="603.3" y1="90.9" x2="603.3" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="602.15" y="91.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="607.1" y1="90.6" x2="607.1" y2="91.9" stroke="var(--up)" class="wick"/>
<rect x="605.94" y="90.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="610.9" y1="90.4" x2="610.9" y2="91.1" stroke="var(--down)" class="wick"/>
<rect x="609.73" y="90.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="614.7" y1="90.9" x2="614.7" y2="92.6" stroke="var(--down)" class="wick"/>
<rect x="613.51" y="90.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="618.5" y1="90.9" x2="618.5" y2="92.1" stroke="var(--up)" class="wick"/>
<rect x="617.30" y="91.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="622.3" y1="90.9" x2="622.3" y2="94.0" stroke="var(--down)" class="wick"/>
<rect x="621.09" y="91.7" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="626.0" y1="92.2" x2="626.0" y2="94.5" stroke="var(--down)" class="wick"/>
<rect x="624.87" y="93.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="629.8" y1="92.2" x2="629.8" y2="100.2" stroke="var(--up)" class="wick"/>
<rect x="628.66" y="92.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="633.6" y1="92.6" x2="633.6" y2="96.5" stroke="var(--down)" class="wick"/>
<rect x="632.44" y="92.6" width="2.35" height="2.9" fill="var(--down)"/>
<line x1="637.4" y1="95.5" x2="637.4" y2="96.8" stroke="var(--down)" class="wick"/>
<rect x="636.23" y="95.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="641.2" y1="96.0" x2="641.2" y2="101.4" stroke="var(--down)" class="wick"/>
<rect x="640.02" y="96.0" width="2.35" height="3.7" fill="var(--down)"/>
<line x1="645.0" y1="99.7" x2="645.0" y2="114.0" stroke="var(--down)" class="wick"/>
<rect x="643.80" y="99.7" width="2.35" height="12.3" fill="var(--down)"/>
<line x1="648.8" y1="106.6" x2="648.8" y2="123.8" stroke="var(--up)" class="wick"/>
<rect x="647.59" y="107.6" width="2.35" height="12.5" fill="var(--up)"/>
<line x1="652.5" y1="106.8" x2="652.5" y2="117.6" stroke="var(--up)" class="wick"/>
<rect x="651.38" y="107.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="656.3" y1="107.6" x2="656.3" y2="119.4" stroke="var(--down)" class="wick"/>
<rect x="655.16" y="107.8" width="2.35" height="7.2" fill="var(--down)"/>
<line x1="660.1" y1="114.2" x2="660.1" y2="120.1" stroke="var(--down)" class="wick"/>
<rect x="658.95" y="115.0" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="663.9" y1="117.6" x2="663.9" y2="132.7" stroke="var(--down)" class="wick"/>
<rect x="662.73" y="118.4" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="667.7" y1="122.3" x2="667.7" y2="138.6" stroke="var(--down)" class="wick"/>
<rect x="666.52" y="123.3" width="2.35" height="14.9" fill="var(--down)"/>
<line x1="671.5" y1="139.5" x2="671.5" y2="159.9" stroke="var(--down)" class="wick"/>
<rect x="670.31" y="142.2" width="2.35" height="17.5" fill="var(--down)"/>
<line x1="675.3" y1="159.4" x2="675.3" y2="168.2" stroke="var(--down)" class="wick"/>
<rect x="674.09" y="159.7" width="2.35" height="6.2" fill="var(--down)"/>
<line x1="679.1" y1="163.3" x2="679.1" y2="170.0" stroke="var(--up)" class="wick"/>
<rect x="677.88" y="163.6" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="682.8" y1="160.7" x2="682.8" y2="165.1" stroke="var(--up)" class="wick"/>
<rect x="681.67" y="162.6" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="686.6" y1="161.9" x2="686.6" y2="164.3" stroke="var(--down)" class="wick"/>
<rect x="685.45" y="162.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="690.4" y1="162.3" x2="690.4" y2="166.3" stroke="var(--down)" class="wick"/>
<rect x="689.24" y="162.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="694.2" y1="163.3" x2="694.2" y2="174.6" stroke="var(--down)" class="wick"/>
<rect x="693.02" y="163.8" width="2.35" height="10.1" fill="var(--down)"/>
<line x1="698.0" y1="170.5" x2="698.0" y2="175.4" stroke="var(--up)" class="wick"/>
<rect x="696.81" y="171.7" width="2.35" height="2.8" fill="var(--up)"/>
<line x1="701.8" y1="171.5" x2="701.8" y2="176.1" stroke="var(--down)" class="wick"/>
<rect x="700.60" y="172.5" width="2.35" height="2.2" fill="var(--down)"/>
<line x1="705.6" y1="172.0" x2="705.6" y2="174.6" stroke="var(--up)" class="wick"/>
<rect x="704.38" y="172.5" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="709.3" y1="172.7" x2="709.3" y2="177.1" stroke="var(--down)" class="wick"/>
<rect x="708.17" y="172.7" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="713.1" y1="174.2" x2="713.1" y2="184.2" stroke="var(--down)" class="wick"/>
<rect x="711.96" y="176.4" width="2.35" height="7.9" fill="var(--down)"/>
<line x1="716.9" y1="184.0" x2="716.9" y2="191.8" stroke="var(--down)" class="wick"/>
<rect x="715.74" y="184.7" width="2.35" height="7.1" fill="var(--down)"/>
<line x1="720.7" y1="189.4" x2="720.7" y2="192.3" stroke="var(--up)" class="wick"/>
<rect x="719.53" y="192.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="724.5" y1="191.1" x2="724.5" y2="198.5" stroke="var(--down)" class="wick"/>
<rect x="723.31" y="191.8" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="728.3" y1="191.8" x2="728.3" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="727.10" y="194.3" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="732.1" y1="192.3" x2="732.1" y2="195.1" stroke="var(--up)" class="wick"/>
<rect x="730.89" y="192.3" width="2.35" height="2.5" fill="var(--up)"/>
<line x1="735.8" y1="191.3" x2="735.8" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="734.67" y="191.8" width="2.35" height="2.5" fill="var(--down)"/>
<line x1="739.6" y1="192.1" x2="739.6" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="738.46" y="193.1" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="743.4" y1="193.6" x2="743.4" y2="196.2" stroke="var(--down)" class="wick"/>
<rect x="742.25" y="193.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="747.2" y1="190.8" x2="747.2" y2="194.8" stroke="var(--up)" class="wick"/>
<rect x="746.03" y="190.8" width="2.35" height="3.9" fill="var(--up)"/>
<line x1="751.0" y1="190.1" x2="751.0" y2="193.3" stroke="var(--down)" class="wick"/>
<rect x="749.82" y="191.1" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="754.8" y1="191.3" x2="754.8" y2="193.9" stroke="var(--down)" class="wick"/>
<rect x="753.60" y="192.3" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="758.6" y1="193.3" x2="758.6" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="757.39" y="193.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="762.4" y1="192.8" x2="762.4" y2="195.6" stroke="var(--up)" class="wick"/>
<rect x="761.18" y="193.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="766.1" y1="192.8" x2="766.1" y2="195.1" stroke="var(--down)" class="wick"/>
<rect x="764.96" y="194.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="769.9" y1="193.6" x2="769.9" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="768.75" y="194.8" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="773.7" y1="194.3" x2="773.7" y2="196.0" stroke="var(--up)" class="wick"/>
<rect x="772.54" y="194.8" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="777.5" y1="193.1" x2="777.5" y2="203.9" stroke="var(--down)" class="wick"/>
<rect x="776.32" y="195.4" width="2.35" height="2.7" fill="var(--down)"/>
<line x1="781.3" y1="189.4" x2="781.3" y2="201.6" stroke="var(--up)" class="wick"/>
<rect x="780.11" y="192.3" width="2.35" height="9.1" fill="var(--up)"/>
<line x1="785.1" y1="192.1" x2="785.1" y2="194.6" stroke="var(--up)" class="wick"/>
<rect x="783.89" y="193.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="788.9" y1="191.8" x2="788.9" y2="194.6" stroke="var(--down)" class="wick"/>
<rect x="787.68" y="193.1" width="2.35" height="1.2" fill="var(--down)"/>
<line x1="792.6" y1="192.6" x2="792.6" y2="196.5" stroke="var(--up)" class="wick"/>
<rect x="791.47" y="192.8" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="796.4" y1="191.8" x2="796.4" y2="197.2" stroke="var(--up)" class="wick"/>
<rect x="795.25" y="192.1" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="800.2" y1="184.7" x2="800.2" y2="190.1" stroke="var(--down)" class="wick"/>
<rect x="799.04" y="188.4" width="2.35" height="1.6" fill="var(--down)"/>
<line x1="804.0" y1="187.4" x2="804.0" y2="191.1" stroke="var(--down)" class="wick"/>
<rect x="802.83" y="189.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="807.8" y1="190.0" x2="807.8" y2="193.6" stroke="var(--up)" class="wick"/>
<rect x="806.61" y="190.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="811.6" y1="189.2" x2="811.6" y2="191.1" stroke="var(--up)" class="wick"/>
<rect x="810.40" y="190.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="815.4" y1="183.3" x2="815.4" y2="190.4" stroke="var(--up)" class="wick"/>
<rect x="814.19" y="189.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="819.1" y1="188.9" x2="819.1" y2="195.6" stroke="var(--down)" class="wick"/>
<rect x="817.97" y="188.9" width="2.35" height="5.2" fill="var(--down)"/>
<line x1="822.9" y1="192.8" x2="822.9" y2="198.0" stroke="var(--up)" class="wick"/>
<rect x="821.76" y="193.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="826.7" y1="189.7" x2="826.7" y2="195.4" stroke="var(--up)" class="wick"/>
<rect x="825.54" y="189.7" width="2.35" height="5.4" fill="var(--up)"/>
<line x1="830.5" y1="188.7" x2="830.5" y2="190.4" stroke="var(--down)" class="wick"/>
<rect x="829.33" y="189.2" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="834.3" y1="189.4" x2="834.3" y2="192.1" stroke="var(--down)" class="wick"/>
<rect x="833.12" y="190.4" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="838.1" y1="189.2" x2="838.1" y2="191.8" stroke="var(--up)" class="wick"/>
<rect x="836.90" y="189.2" width="2.35" height="1.7" fill="var(--up)"/>
<line x1="841.9" y1="188.7" x2="841.9" y2="199.0" stroke="var(--down)" class="wick"/>
<rect x="840.69" y="189.4" width="2.35" height="6.0" fill="var(--down)"/>
<line x1="845.6" y1="195.7" x2="845.6" y2="201.0" stroke="var(--down)" class="wick"/>
<rect x="844.48" y="195.7" width="2.35" height="4.4" fill="var(--down)"/>
<line x1="849.4" y1="198.8" x2="849.4" y2="204.4" stroke="var(--down)" class="wick"/>
<rect x="848.26" y="200.0" width="2.35" height="2.3" fill="var(--down)"/>
<line x1="853.2" y1="200.2" x2="853.2" y2="205.6" stroke="var(--down)" class="wick"/>
<rect x="852.05" y="202.7" width="2.35" height="1.9" fill="var(--down)"/>
<line x1="857.0" y1="203.1" x2="857.0" y2="209.3" stroke="var(--down)" class="wick"/>
<rect x="855.83" y="203.6" width="2.35" height="5.4" fill="var(--down)"/>
<line x1="860.8" y1="208.8" x2="860.8" y2="223.3" stroke="var(--down)" class="wick"/>
<rect x="859.62" y="209.0" width="2.35" height="13.1" fill="var(--down)"/>
<line x1="864.6" y1="218.8" x2="864.6" y2="223.3" stroke="var(--up)" class="wick"/>
<rect x="863.41" y="220.3" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="868.4" y1="220.1" x2="868.4" y2="233.1" stroke="var(--down)" class="wick"/>
<rect x="867.19" y="220.6" width="2.35" height="4.6" fill="var(--down)"/>
<line x1="872.2" y1="223.3" x2="872.2" y2="229.0" stroke="var(--down)" class="wick"/>
<rect x="870.98" y="225.7" width="2.35" height="1.3" fill="var(--down)"/>
<line x1="875.9" y1="226.5" x2="875.9" y2="229.5" stroke="var(--up)" class="wick"/>
<rect x="874.77" y="227.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="879.7" y1="227.0" x2="879.7" y2="229.2" stroke="var(--down)" class="wick"/>
<rect x="878.55" y="227.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="883.5" y1="226.7" x2="883.5" y2="230.6" stroke="var(--down)" class="wick"/>
<rect x="882.34" y="227.7" width="2.35" height="2.1" fill="var(--down)"/>
<line x1="887.3" y1="230.4" x2="887.3" y2="238.5" stroke="var(--down)" class="wick"/>
<rect x="886.12" y="230.9" width="2.35" height="5.6" fill="var(--down)"/>
<line x1="891.1" y1="234.1" x2="891.1" y2="242.7" stroke="var(--down)" class="wick"/>
<rect x="889.91" y="237.8" width="2.35" height="3.1" fill="var(--down)"/>
<line x1="894.9" y1="232.9" x2="894.9" y2="240.0" stroke="var(--up)" class="wick"/>
<rect x="893.70" y="237.1" width="2.35" height="2.9" fill="var(--up)"/>
<line x1="898.7" y1="233.2" x2="898.7" y2="236.0" stroke="var(--up)" class="wick"/>
<rect x="897.48" y="234.1" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="902.4" y1="234.4" x2="902.4" y2="239.1" stroke="var(--down)" class="wick"/>
<rect x="901.27" y="234.9" width="2.35" height="3.9" fill="var(--down)"/>
<line x1="906.2" y1="237.1" x2="906.2" y2="244.2" stroke="var(--down)" class="wick"/>
<rect x="905.06" y="239.8" width="2.35" height="3.2" fill="var(--down)"/>
<line x1="910.0" y1="240.5" x2="910.0" y2="253.2" stroke="var(--down)" class="wick"/>
<rect x="908.84" y="242.7" width="2.35" height="9.5" fill="var(--down)"/>
<line x1="913.8" y1="248.8" x2="913.8" y2="259.9" stroke="var(--down)" class="wick"/>
<rect x="912.63" y="250.6" width="2.35" height="9.3" fill="var(--down)"/>
<line x1="917.6" y1="256.8" x2="917.6" y2="261.1" stroke="var(--down)" class="wick"/>
<rect x="916.41" y="259.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="921.4" y1="256.2" x2="921.4" y2="260.4" stroke="var(--up)" class="wick"/>
<rect x="920.20" y="258.2" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="925.2" y1="257.0" x2="925.2" y2="259.4" stroke="var(--down)" class="wick"/>
<rect x="923.99" y="258.9" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="928.9" y1="259.1" x2="928.9" y2="261.7" stroke="var(--down)" class="wick"/>
<rect x="927.77" y="259.4" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="932.7" y1="255.7" x2="932.7" y2="260.9" stroke="var(--up)" class="wick"/>
<rect x="931.56" y="256.8" width="2.35" height="4.1" fill="var(--up)"/>
<line x1="936.5" y1="253.5" x2="936.5" y2="257.8" stroke="var(--up)" class="wick"/>
<rect x="935.35" y="254.3" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="940.3" y1="252.7" x2="940.3" y2="257.8" stroke="var(--down)" class="wick"/>
<rect x="939.13" y="254.7" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="944.1" y1="252.7" x2="944.1" y2="255.5" stroke="var(--up)" class="wick"/>
<rect x="942.92" y="253.5" width="2.35" height="2.0" fill="var(--up)"/>
<line x1="947.9" y1="251.9" x2="947.9" y2="254.3" stroke="var(--up)" class="wick"/>
<rect x="946.70" y="253.2" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="951.7" y1="252.1" x2="951.7" y2="253.7" stroke="var(--up)" class="wick"/>
<rect x="950.49" y="253.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="955.5" y1="253.0" x2="955.5" y2="254.7" stroke="var(--down)" class="wick"/>
<rect x="954.28" y="253.0" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="959.2" y1="252.1" x2="959.2" y2="255.7" stroke="var(--down)" class="wick"/>
<rect x="958.06" y="254.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="963.0" y1="251.9" x2="963.0" y2="254.7" stroke="var(--up)" class="wick"/>
<rect x="961.85" y="252.3" width="2.35" height="2.3" fill="var(--up)"/>
<line x1="966.8" y1="250.1" x2="966.8" y2="252.7" stroke="var(--up)" class="wick"/>
<rect x="965.64" y="250.8" width="2.35" height="1.8" fill="var(--up)"/>
<line x1="970.6" y1="249.6" x2="970.6" y2="252.1" stroke="var(--down)" class="wick"/>
<rect x="969.42" y="251.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="974.4" y1="251.4" x2="974.4" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="973.21" y="251.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="978.2" y1="249.6" x2="978.2" y2="254.0" stroke="var(--down)" class="wick"/>
<rect x="976.99" y="251.6" width="2.35" height="1.7" fill="var(--down)"/>
<line x1="982.0" y1="250.8" x2="982.0" y2="253.0" stroke="var(--up)" class="wick"/>
<rect x="980.78" y="252.6" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="985.7" y1="252.1" x2="985.7" y2="254.0" stroke="var(--down)" class="wick"/>
<rect x="984.57" y="252.6" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="989.5" y1="253.2" x2="989.5" y2="255.5" stroke="var(--down)" class="wick"/>
<rect x="988.35" y="253.5" width="2.35" height="1.5" fill="var(--down)"/>
<line x1="993.3" y1="252.3" x2="993.3" y2="254.7" stroke="var(--up)" class="wick"/>
<rect x="992.14" y="253.0" width="2.35" height="1.5" fill="var(--up)"/>
<line x1="997.1" y1="251.6" x2="997.1" y2="253.7" stroke="var(--down)" class="wick"/>
<rect x="995.93" y="253.0" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1000.9" y1="253.5" x2="1000.9" y2="257.5" stroke="var(--down)" class="wick"/>
<rect x="999.71" y="253.5" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1004.7" y1="253.5" x2="1004.7" y2="254.5" stroke="var(--up)" class="wick"/>
<rect x="1003.50" y="253.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1008.5" y1="249.6" x2="1008.5" y2="253.5" stroke="var(--up)" class="wick"/>
<rect x="1007.28" y="250.1" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="1012.2" y1="249.1" x2="1012.2" y2="251.1" stroke="var(--down)" class="wick"/>
<rect x="1011.07" y="250.3" width="2.35" height="1.0" fill="var(--down)"/>
<line x1="1016.0" y1="246.4" x2="1016.0" y2="251.4" stroke="var(--up)" class="wick"/>
<rect x="1014.86" y="246.9" width="2.35" height="4.2" fill="var(--up)"/>
<line x1="1019.8" y1="243.2" x2="1019.8" y2="246.9" stroke="var(--up)" class="wick"/>
<rect x="1018.64" y="246.4" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1023.6" y1="238.8" x2="1023.6" y2="247.9" stroke="var(--up)" class="wick"/>
<rect x="1022.43" y="245.9" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1027.4" y1="240.0" x2="1027.4" y2="246.7" stroke="var(--up)" class="wick"/>
<rect x="1026.22" y="243.2" width="2.35" height="3.4" fill="var(--up)"/>
<line x1="1031.2" y1="237.8" x2="1031.2" y2="245.5" stroke="var(--up)" class="wick"/>
<rect x="1030.00" y="242.0" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="1035.0" y1="232.4" x2="1035.0" y2="242.4" stroke="var(--up)" class="wick"/>
<rect x="1033.79" y="232.4" width="2.35" height="9.8" fill="var(--up)"/>
<line x1="1038.7" y1="230.9" x2="1038.7" y2="247.9" stroke="var(--down)" class="wick"/>
<rect x="1037.57" y="232.9" width="2.35" height="11.6" fill="var(--down)"/>
<line x1="1042.5" y1="239.3" x2="1042.5" y2="243.9" stroke="var(--up)" class="wick"/>
<rect x="1041.36" y="241.7" width="2.35" height="2.2" fill="var(--up)"/>
<line x1="1046.3" y1="239.8" x2="1046.3" y2="243.4" stroke="var(--down)" class="wick"/>
<rect x="1045.15" y="241.3" width="2.35" height="1.8" fill="var(--down)"/>
<line x1="1050.1" y1="241.4" x2="1050.1" y2="243.2" stroke="var(--up)" class="wick"/>
<rect x="1048.93" y="242.7" width="2.35" height="1.0" fill="var(--up)"/>
<line x1="60" y1="187.9" x2="1052" y2="187.9" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="191.4" font-size="11.5" fill="var(--resistance)" font-weight="600">4.26% R1</text>
<text x="1058" y="203.4" font-size="9.5" fill="var(--muted)">터치 4회</text>
<line x1="60" y1="85.8" x2="1052" y2="85.8" stroke="var(--resistance)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="89.3" font-size="11.5" fill="var(--resistance)" font-weight="600">5.30% R2</text>
<text x="1058" y="101.3" font-size="9.5" fill="var(--muted)">터치 7회</text>
<line x1="60" y1="258.3" x2="1052" y2="258.3" stroke="var(--support)" stroke-width="1.4" stroke-dasharray="6,4"/>
<text x="1058" y="252.3" font-size="11.5" fill="var(--support)" font-weight="600">3.54% S1</text>
<text x="1058" y="264.3" font-size="9.5" fill="var(--muted)">터치 3회</text>
<circle cx="1052.0" cy="242.7" r="3" fill="var(--ink)"/>
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

- **상승**: 연준의 정책금리 인상(또는 인상 기대) 신호로 흔히 해석된다 — 사실상 기준금리의 시장 프록시다.
- **하락**: 연준의 정책금리 인하(또는 인하 기대) 신호로 흔히 해석된다.
- 10년물 국채금리와의 스프레드(장단기 금리차)가 단독 수준보다 더 자주 인용된다.

---

## 관련 문서

- [미국 5년물 국채금리](./treasury_5y.md)
- [미국 10년물 국채금리](./treasury_10y.md) — 장단기 스프레드의 짝 지표
- [미국 30년물 국채금리](./treasury_30y.md)
- [거시경제 개념 정리](../../concepts/macroeconomics.md) — "연준과 금리 결정"·"수익률곡선" 절
- [밸류에이션 개념 정리](../../concepts/valuation.md) — 무위험이자율이 Ke·WACC로 들어가는 지점
- [용어집 — 9. 거시경제](../../glossary.md#macro)

---

## 참고 자료

- [Yahoo Finance — 13 Week Treasury Bill (^IRX)](https://finance.yahoo.com/quote/%5EIRX/)
- [미 재무부 금리 (원출처)](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics)

---

*작성일: 2026-08-20 (최종 수정일: 2026-08-21)*
