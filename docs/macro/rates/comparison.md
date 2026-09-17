# 미국 국채금리 3종 비교 (수익률곡선)

::: info
미국 2년물·10년물·30년물 상수만기 국채금리를 한 차트에 겹쳐, 시간에 따라 수익률곡선이 어떻게 움직였는지(가팔라졌는지·평평해졌는지·역전됐는지) 보기 위한 참고 자료다. [통화 3종 비교](../foreign_exchange/comparison.md)와 달리 **지수화하지 않는다** — 세 지표가 이미 같은 단위(%)이고, 금리는 제로금리 국면에서 0%에 가까워질 수 있어 그런 값을 기준(100)으로 나누면 지수가 크게 왜곡되기 때문이다. 만기별 상세 해석은 [2년물](./treasury_2y.md)·[10년물](./treasury_10y.md)·[30년물](./treasury_30y.md) 각 문서를 따로 참고할 것 — 이 문서는 그 셋을 대체하지 않는다.

:::
---

## 1. 차트 — 최근 5년 일간, 원값(%) 그대로 겹침

<style>
.fred-dgs2-dgs10-dgs30 {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-dgs2:#2a78d6; --s-dgs10:#eb6834; --s-dgs30:#1baf7a;
}
.dark .fred-dgs2-dgs10-dgs30 { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-dgs2:#3987e5; --s-dgs10:#d95926; --s-dgs30:#199e70; }
.fred-dgs2-dgs10-dgs30 svg { width:100%; height:auto; display:block; }
.fred-dgs2-dgs10-dgs30 text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-dgs2-dgs10-dgs30 .title { fill: var(--ink); font-weight:600; }
.fred-dgs2-dgs10-dgs30 .grid { stroke: var(--grid); stroke-width:1; }
.fred-dgs2-dgs10-dgs30 .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-dgs2-dgs10-dgs30">
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미국 2년물 국채금리·미국 10년물 국채금리·미국 30년물 국채금리, 최근 5년 일간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 국채금리 3종 비교 (상수만기) (최근 5년 일간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-09-15 · 단위: % · 출처: FRED DGS2 · FRED DGS10 · FRED DGS30</text>
<line x1="60" y1="580.6" x2="1052" y2="580.6" class="grid"/>
<text x="52" y="584.6" font-size="11" text-anchor="end" fill="var(--muted)">0.00</text>
<line x1="60" y1="489.9" x2="1052" y2="489.9" class="grid"/>
<text x="52" y="493.9" font-size="11" text-anchor="end" fill="var(--muted)">1.00</text>
<line x1="60" y1="399.2" x2="1052" y2="399.2" class="grid"/>
<text x="52" y="403.2" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="308.5" x2="1052" y2="308.5" class="grid"/>
<text x="52" y="312.5" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="217.8" x2="1052" y2="217.8" class="grid"/>
<text x="52" y="221.8" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="127.1" x2="1052" y2="127.1" class="grid"/>
<text x="52" y="131.1" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
<line x1="125.8" y1="56" x2="125.8" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="125.8" y1="600" x2="125.8" y2="605" class="axis"/>
<text x="125.8" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="322.6" y1="56" x2="322.6" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="322.6" y1="600" x2="322.6" y2="605" class="axis"/>
<text x="322.6" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="519.3" y1="56" x2="519.3" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="519.3" y1="600" x2="519.3" y2="605" class="axis"/>
<text x="519.3" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.7" y1="56" x2="716.7" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.7" y1="600" x2="716.7" y2="605" class="axis"/>
<text x="716.7" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.4" y1="56" x2="913.4" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.4" y1="600" x2="913.4" y2="605" class="axis"/>
<text x="913.4" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="600" x2="1052" y2="600" class="axis"/>
<line x1="60" y1="56" x2="60" y2="600" class="axis"/>
<polyline points="60.0,562.5 60.5,562.5 61.1,561.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="63.2,560.7 63.8,560.7 64.3,559.8 64.9,559.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="66.5,561.6 67.0,561.6 67.5,561.6 68.1,559.8 68.6,559.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="70.2,559.8 70.8,560.7 71.3,557.9 71.9,556.1 72.4,554.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="74.0,552.5 74.6,552.5 75.1,553.4 75.6,555.2 76.2,556.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="77.8,556.1 78.3,555.2 78.9,553.4 79.4,551.6 79.9,551.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="82.1,548.9 82.6,547.1 83.2,548.0 83.7,543.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="85.3,540.7 85.9,543.4 86.4,544.3 87.0,539.8 87.5,537.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="89.1,538.0 89.7,538.0 90.2,535.3 90.7,535.3 91.3,537.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="92.9,535.3 93.4,538.9 94.0,538.0 94.5,543.4 95.0,545.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="96.7,539.8 97.2,543.4 97.7,534.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="98.8" cy="532.5" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="100.4,532.5 101.0,531.6 101.5,533.5 102.1,533.5 102.6,533.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="104.2,523.5 104.7,526.2 105.3,522.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="106.4" cy="535.3" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="108.0,534.4 108.5,533.5 109.1,529.8 109.6,523.5 110.1,526.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="111.8,521.7 112.3,517.1 112.8,518.9 113.4,517.1 113.9,519.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="115.5,520.8 116.1,519.8 116.6,518.0 117.1,522.6 117.7,520.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="119.3,521.7 119.8,517.1 120.4,518.9 120.9,516.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="123.1,511.7 123.6,513.5 124.2,512.6 124.7,514.4 125.2,514.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="126.9,509.9 127.4,510.8 127.9,505.3 128.5,500.8 129.0,501.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="130.6,497.2 131.2,499.0 131.7,497.2 132.2,498.1 132.8,490.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="134.9,484.5 135.5,486.3 136.0,482.7 136.6,489.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="138.2,490.8 138.7,488.1 139.3,478.1 139.8,473.6 140.3,476.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="141.9,473.6 142.5,473.6 143.0,475.4 143.6,472.7 144.1,461.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="145.7,462.7 146.3,458.2 146.8,457.3 147.3,434.6 147.9,444.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="149.5,437.3 150.0,437.3 150.6,442.7 151.1,445.5 151.7,447.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="153.8,439.1 154.3,437.3 154.9,440.9 155.4,440.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="157.0,450.0 157.6,461.8 158.1,444.6 158.7,441.8 159.2,444.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="160.8,440.0 161.4,432.8 161.9,428.2 162.4,424.6 163.0,421.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="164.6,411.0 165.1,412.8 165.7,403.7 166.2,404.6 166.7,401.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="168.4,386.5 168.9,382.9 169.4,387.4 170.0,387.4 170.5,372.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="172.1,367.5 172.7,367.5 173.2,371.1 173.8,373.8 174.3,359.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="175.9,360.2 176.5,352.9 177.0,353.9 177.5,356.6 178.1,351.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="179.7,353.9 180.2,363.8 180.8,365.6 181.3,356.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="183.5,357.5 184.0,343.9 184.5,344.8 185.1,337.5 185.6,333.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="187.2,342.1 187.8,350.2 188.3,346.6 188.9,342.1 189.4,335.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="191.0,333.0 191.5,328.5 192.1,339.3 192.6,334.8 193.2,333.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="194.8,343.9 195.3,343.0 195.9,339.3 196.4,348.4 196.9,343.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="198.6,346.6 199.1,334.8 199.6,337.5 200.2,342.1 200.7,344.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="202.3,340.2 202.9,353.9 203.4,355.7 203.9,357.5 204.5,356.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="206.6,351.1 207.2,339.3 207.7,340.2 208.3,339.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="209.9,333.0 210.4,331.2 211.0,328.5 211.5,323.9 212.0,303.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="213.7,272.2 214.2,267.7 214.7,290.4 215.3,295.8 215.8,293.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="218.0,289.4 218.5,303.1 219.0,307.6 219.6,304.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="221.2,301.2 221.7,299.4 222.3,303.1 222.8,315.8 223.4,323.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="225.5,324.8 226.1,311.2 226.6,305.8 227.1,297.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="228.7,302.1 229.3,305.8 229.8,296.7 230.4,294.9 230.9,296.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="232.5,294.9 233.1,287.6 233.6,285.8 234.1,299.4 234.7,310.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="236.3,308.5 236.8,306.7 237.4,312.1 237.9,322.1 238.5,318.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="240.1,317.6 240.6,303.1 241.1,299.4 241.7,305.8 242.2,286.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="243.8,289.4 244.4,283.1 244.9,287.6 245.5,287.6 246.0,285.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="247.6,290.4 248.2,285.8 248.7,283.1 249.2,288.5 249.8,285.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="251.4,279.5 251.9,282.2 252.5,275.8 253.0,276.7 253.5,274.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="255.2,270.4 255.7,266.8 256.2,267.7 256.8,262.2 257.3,272.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="259.5,263.1 260.0,267.7 260.6,265.0 261.1,257.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="262.7,255.9 263.3,240.5 263.8,237.7 264.3,229.6 264.9,231.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="266.5,222.3 267.0,221.4 267.6,216.0 268.1,207.8 268.6,199.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="270.3,193.3 270.8,190.6 271.3,211.4 271.9,203.3 272.4,197.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="274.0,206.9 274.6,208.7 275.1,204.2 275.7,196.9 276.2,190.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="278.3,190.6 278.9,192.4 279.4,175.2 280.0,174.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="281.6,177.0 282.1,178.8 282.7,167.9 283.2,161.5 283.7,173.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="285.4,172.4 285.9,179.7 286.4,182.4 287.0,190.6 287.5,180.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="289.1,171.5 289.7,168.8 290.2,162.5 290.7,153.4 291.3,157.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="292.9,152.5 293.4,157.0 294.0,162.5 294.5,186.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="296.7,181.5 297.2,184.2 297.8,186.0 298.3,178.8 298.8,171.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="300.5,174.2 301.0,175.2 301.5,176.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="302.6" cy="179.7" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="304.2,176.1 304.8,174.2 305.3,183.3 305.8,195.1 306.4,192.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="308.0,180.6 308.5,186.9 309.1,194.2 309.6,189.7 310.2,187.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="311.8,182.4 312.3,197.8 312.9,196.9 313.4,196.9 313.9,202.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="315.5,195.1 316.1,195.1 316.6,198.7 317.2,196.0 317.7,189.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="319.9,188.8 320.4,189.7 320.9,186.9 321.5,180.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="323.6,181.5 324.2,185.1 324.7,177.0 325.3,196.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="326.9,200.6 327.4,196.0 327.9,199.6 328.5,206.9 329.0,197.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="331.2,201.5 331.7,212.3 332.3,209.6 332.8,205.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="334.4,198.7 335.0,206.9 335.5,207.8 336.0,202.4 336.6,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="338.2,195.1 338.7,198.7 339.3,209.6 339.8,209.6 340.3,190.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="342.0,177.9 342.5,175.2 343.0,177.0 343.6,174.2 344.1,172.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="345.7,170.6 346.3,163.4 346.8,161.5 347.4,161.5 347.9,163.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="350.1,157.0 350.6,157.9 351.1,157.9 351.7,147.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="353.3,147.0 353.8,144.3 354.4,137.1 354.9,137.1 355.4,139.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="357.1,137.1 357.6,127.1 358.1,122.5 358.7,136.2 359.2,163.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="360.8,215.1 361.4,199.6 361.9,224.1 362.5,205.1 363.0,235.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="364.6,225.0 365.1,202.4 365.7,221.4 366.2,239.6 366.8,239.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="368.4,223.2 368.9,216.0 369.5,210.5 370.0,208.7 370.5,212.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="372.2,220.5 372.7,232.3 373.2,236.8 373.8,234.1 374.3,220.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="375.9,217.8 376.5,215.1 377.0,222.3 377.5,221.4 378.1,210.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="379.7,201.5 380.2,200.6 380.8,196.0 381.3,205.1 381.9,202.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="383.5,206.9 384.0,230.5 384.6,226.9 385.1,211.4 385.6,214.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="387.3,205.1 387.8,220.5 388.3,227.8 388.9,240.5 389.4,225.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="391.0,217.8 391.6,216.9 392.1,226.9 392.6,227.8 393.2,219.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="394.8,218.7 395.3,212.3 395.9,206.9 396.4,196.0 397.0,192.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="398.6,191.5 399.1,194.2 399.7,189.7 400.2,172.4 400.7,168.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="402.9,176.1 403.4,181.5 404.0,187.9 404.5,172.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="406.1,176.1 406.7,171.5 407.2,167.0 407.7,170.6 408.3,164.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="409.9,167.9 410.4,157.0 411.0,150.7 411.5,161.5 412.1,154.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="414.2,156.1 414.7,156.1 415.3,147.9 415.8,153.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="417.4,158.8 418.0,150.7 418.5,153.4 419.1,138.9 419.6,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="421.2" cy="132.5" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="422.3,132.5 422.8,128.0 423.4,132.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="425.0,140.7 425.5,138.0 426.1,152.5 426.6,164.3 427.1,150.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="428.8,150.7 429.3,150.7 429.8,150.7 430.4,145.2 430.9,143.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="432.5,144.3 433.1,140.7 433.6,143.4 434.2,135.2 434.7,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="436.3,138.0 436.9,134.3 437.4,138.0 437.9,136.2 438.5,147.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="440.1,148.8 440.6,150.7 441.2,146.1 441.7,143.4 442.2,137.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="443.9,130.7 444.4,134.3 444.9,129.8 445.5,132.5 446.0,134.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="447.6,129.8 448.2,125.3 448.7,131.6 449.3,128.9 449.8,124.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="451.4,128.9 451.9,138.9 452.5,136.2 453.0,140.7 453.6,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="455.7,132.5 456.3,126.2 456.8,132.5 457.3,128.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="459.0,129.8 459.5,128.9 460.0,130.7 460.6,127.1 461.1,125.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="462.7,122.5 463.3,119.8 463.8,116.2 464.3,116.2 464.9,118.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="466.5,118.9 467.0,123.5 467.6,118.0 468.1,123.5 468.7,124.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="470.3,116.2 470.8,113.5 471.4,122.5 471.9,124.4 472.4,119.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="474.6,130.7 475.1,128.0 475.7,121.6 476.2,123.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="477.8,118.9 478.4,109.8 478.9,109.8 479.4,114.4 480.0,120.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="481.6,122.5 482.1,125.3 482.7,119.8 483.2,125.3 483.8,128.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="485.4,124.4 485.9,120.7 486.5,131.6 487.0,128.9 487.5,142.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="489.1,133.4 489.7,135.2 490.2,133.4 490.8,124.4 491.3,123.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="492.9,125.3 493.5,145.2 494.0,136.2 494.5,142.5 495.1,138.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="496.7,137.1 497.2,139.8 497.8,137.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="498.9" cy="134.3" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="500.5,141.6 501.0,151.6 501.5,159.7 502.1,151.6 502.6,167.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="504.2,159.7 504.8,166.1 505.3,163.4 505.9,165.2 506.4,153.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="508.0,153.4 508.6,151.6 509.1,176.1 509.6,184.2 510.2,177.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="511.8,178.8 512.3,180.6 512.9,186.9 513.4,187.9 513.9,189.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="516.1,194.2 516.6,199.6 517.2,194.2 517.7,196.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="519.9,187.9 520.4,187.9 521.0,183.3 521.5,181.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="523.1,185.1 523.7,185.1 524.2,184.2 524.7,194.2 525.3,205.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="527.4,197.8 528.0,186.9 528.5,186.9 529.0,182.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="530.7,184.2 531.2,189.7 531.7,186.9 532.3,192.4 532.8,186.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="534.4,191.5 535.0,185.1 535.5,193.3 536.1,199.6 536.6,185.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="538.2,176.1 538.7,182.4 539.3,180.6 539.8,176.1 540.4,174.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="542.0,176.1 542.5,159.7 543.1,167.0 543.6,167.0 544.1,159.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="546.3,164.3 546.8,159.7 547.4,155.2 547.9,157.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="549.5,155.2 550.1,154.3 550.6,159.7 551.1,159.7 551.7,168.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="553.3,162.5 553.8,168.8 554.4,167.9 554.9,172.4 555.5,174.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="557.1,171.5 557.6,165.2 558.2,162.5 558.7,156.1 559.2,152.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="560.9,151.6 561.4,156.1 561.9,164.3 562.5,161.5 563.0,164.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="564.6,168.8 565.2,167.0 565.7,168.8 566.2,164.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="568.4,152.5 568.9,154.3 569.5,156.1 570.0,158.8 570.6,151.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="572.2,147.0 572.7,150.7 573.3,129.8 573.8,133.4 574.3,138.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="575.9,133.4 576.5,129.8 577.0,133.4 577.6,128.9 578.1,129.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="579.7,129.8 580.3,139.8 580.8,137.1 581.3,130.7 581.9,130.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="583.5,129.8 584.0,123.5 584.6,130.7 585.1,138.9 585.7,144.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="587.3,143.4 587.8,143.4 588.3,141.6 588.9,145.2 589.4,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="591.0,140.7 591.6,144.3 592.1,151.6 592.7,147.0 593.2,142.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="594.8,143.4 595.4,143.4 595.9,139.8 596.4,135.2 597.0,133.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="599.1,132.5 599.7,130.7 600.2,134.3 600.7,137.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="602.4,143.4 602.9,147.9 603.4,152.5 604.0,152.5 604.5,138.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="606.1,138.9 606.7,144.3 607.2,149.8 607.8,156.1 608.3,157.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="609.9,149.8 610.5,155.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="611.5,154.3 612.1,154.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="613.7,153.4 614.2,158.8 614.8,153.4 615.3,154.3 615.8,153.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="617.5,147.9 618.0,150.7 618.5,153.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="619.6" cy="163.4" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="621.2,161.5 621.8,161.5 622.3,161.5 622.9,172.4 623.4,177.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="625.0,177.9 625.5,178.8 626.1,179.7 626.6,176.1 627.2,173.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="628.8,172.4 629.3,181.5 629.9,184.2 630.4,180.6 630.9,185.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="632.6,185.1 633.1,186.0 633.6,191.5 634.2,203.3 634.7,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="636.3,227.8 636.9,218.7 637.4,217.8 637.9,214.2 638.5,213.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="640.1,216.9 640.6,224.1 641.2,223.2 641.7,210.5 642.3,212.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="643.9,212.3 644.4,218.7 645.0,225.0 645.5,218.7 646.0,226.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="647.7,226.0 648.2,233.2 648.7,233.2 649.3,229.6 649.8,226.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="652.0,228.7 652.5,239.6 653.0,240.5 653.6,248.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="655.2,246.8 655.7,255.0 656.3,252.3 656.8,250.4 657.4,256.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="659.0,257.7 659.5,255.0 660.1,253.2 660.6,255.0 661.1,258.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="662.7,256.8 663.3,264.1 663.8,260.4 664.4,254.1 664.9,258.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="666.5,248.6 667.1,253.2 667.6,251.4 668.1,245.0 668.7,224.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="670.3,218.7 670.8,219.6 671.4,218.7 671.9,219.6 672.5,222.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="674.6,222.3 675.1,224.1 675.7,221.4 676.2,222.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="677.8,216.0 678.4,215.1 678.9,211.4 679.5,211.4 680.0,207.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="681.6,206.9 682.2,207.8 682.7,204.2 683.2,203.3 683.8,198.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="685.4,202.4 685.9,200.6 686.5,193.3 687.0,198.7 687.5,194.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="689.7,186.9 690.2,193.3 690.8,186.9 691.3,189.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="692.9,191.5 693.5,193.3 694.0,189.7 694.6,186.9 695.1,184.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="696.7,198.7 697.3,198.7 697.8,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="698.9" cy="206.0" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="700.5,202.4 701.0,202.4 701.6,206.0 702.1,204.2 702.6,208.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="704.3,206.0 704.8,204.2 705.3,204.2 705.9,201.5 706.4,195.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="708.0,195.1 708.6,195.1 709.1,186.0 709.7,188.8 710.2,190.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="711.8,190.6 712.3,191.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="713.4,190.6 714.0,189.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="715.6,196.0 716.1,195.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="717.2,195.1 717.7,192.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="719.4,192.4 719.9,190.6 720.4,192.4 721.0,193.3 721.5,181.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="723.1,181.5 723.7,184.2 724.2,193.3 724.7,196.9 725.3,193.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="727.4,191.5 728.0,191.5 728.5,191.5 729.1,193.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="730.7,202.4 731.2,200.6 731.8,198.7 732.3,201.5 732.8,197.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="734.5,194.2 735.0,198.7 735.5,202.4 736.1,198.7 736.6,191.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="738.2,192.4 738.8,191.5 739.3,185.1 739.8,189.7 740.4,194.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="742.5,191.5 743.1,192.4 743.6,192.4 744.2,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="745.8,206.0 746.3,211.4 746.9,213.3 747.4,211.4 747.9,218.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="749.5,221.4 750.1,221.4 750.6,218.7 751.2,221.4 751.7,218.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="753.3,227.8 753.9,223.2 754.4,216.9 754.9,223.2 755.5,216.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="757.1,212.3 757.6,214.2 758.2,218.7 758.7,222.3 759.3,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="760.9,214.2 761.4,221.4 761.9,219.6 762.5,220.5 763.0,227.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="764.6,227.8 765.2,229.6 765.7,226.0 766.3,244.1 766.8,246.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="768.4,242.3 769.0,244.1 769.5,226.0 770.0,232.3 770.6,221.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="772.2,232.3 772.7,232.3 773.3,238.7 773.8,235.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="776.0,240.5 776.5,239.6 777.0,235.0 777.6,238.7 778.1,241.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="779.7,247.7 780.3,249.5 780.8,254.1 781.4,245.0 781.9,233.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="783.5,233.2 784.1,237.7 784.6,237.7 785.1,226.9 785.7,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="787.3,219.6 787.8,216.0 788.4,213.3 788.9,221.4 789.4,219.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="791.1,220.5 791.6,220.5 792.1,217.8 792.7,217.8 793.2,217.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="795.4,225.0 795.9,221.4 796.5,225.0 797.0,227.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="798.6,223.2 799.1,221.4 799.7,229.6 800.2,225.0 800.8,214.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="802.4,216.9 802.9,216.9 803.5,223.2 804.0,226.9 804.5,221.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="806.2,220.5 806.7,223.2 807.2,223.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="808.3" cy="226.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="809.9,232.3 810.5,240.5 811.0,241.4 811.5,245.0 812.1,242.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="813.7,243.2 814.2,237.7 814.8,237.7 815.3,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="817.5,226.9 818.0,226.9 818.6,230.5 819.1,230.5 819.6,226.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="821.3,226.9 821.8,222.3 822.3,228.7 822.9,226.0 823.4,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="825.0,231.4 825.6,233.2 826.1,228.7 826.6,226.0 827.2,226.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="828.8,226.0 829.3,230.5 829.9,223.2 830.4,223.2 831.0,245.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="832.6,245.9 833.1,243.2 833.7,245.9 834.2,243.2 834.7,239.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="836.3,239.6 836.9,243.2 837.4,247.7 838.0,241.4 838.5,240.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="840.1,238.7 840.7,240.5 841.2,241.4 841.7,236.8 842.3,246.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="843.9,242.3 844.4,253.2 845.0,255.0 845.5,252.3 846.1,255.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="848.2,248.6 848.7,253.2 849.3,255.0 849.8,262.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="851.4,264.1 852.0,259.5 852.5,259.5 853.1,261.3 853.6,257.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="855.2,259.5 855.8,262.2 856.3,261.3 856.8,256.8 857.4,256.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="859.0,253.2 859.5,260.4 860.1,256.8 860.6,250.4 861.1,251.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="862.8,251.4 863.3,254.1 863.8,258.6 864.4,258.6 864.9,255.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="866.5,254.1 867.1,256.8 867.6,255.9 868.2,254.1 868.7,261.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="870.9,265.0 871.4,263.1 871.9,271.3 872.5,266.8" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="874.1,266.8 874.6,267.7 875.2,267.7 875.7,265.0 876.2,265.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="877.9,265.0 878.4,265.9 878.9,255.0 879.5,253.2 880.0,254.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="881.6,254.1 882.2,255.9 882.7,251.4 883.3,256.8 883.8,258.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="885.4" cy="255.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="886.5,257.7 887.0,255.9 887.6,252.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="889.2,254.1 889.7,255.9 890.3,255.9 890.8,258.6 891.3,262.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="893.0,266.8 893.5,269.5 894.0,267.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="895.1" cy="265.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="896.7,259.5 897.3,262.2 897.8,264.1 898.3,261.3 898.9,257.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="900.5,256.8 901.0,253.2 901.6,259.5 902.1,261.3 902.7,261.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="904.3,262.2 904.8,265.0 905.4,264.1 905.9,266.8 906.4,265.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="908.1,268.6 908.6,265.0 909.1,265.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="910.2" cy="266.8" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="911.8,267.7 912.4,267.7 912.9,265.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<circle cx="914.0" cy="265.9" r="2.4" fill="var(--s-dgs2)"/>
<polyline points="915.6,266.8 916.1,265.9 916.7,265.9 917.2,264.1 917.8,259.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="919.4,259.5 919.9,260.4 920.5,262.2 921.0,257.7 921.5,255.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="923.7,254.1 924.2,254.1 924.8,253.2 925.3,254.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="926.9,257.7 927.5,260.4 928.0,257.7 928.5,260.4 929.1,261.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="930.7,256.8 931.2,256.8 931.8,256.8 932.3,265.9 932.9,263.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="934.5,265.0 935.0,267.7 935.5,261.3 936.1,265.9 936.6,272.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="938.8,269.5 939.3,265.9 939.9,265.9 940.4,265.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="942.0,269.5 942.6,269.5 943.1,267.7 943.6,270.4 944.2,274.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="945.8,265.9 946.3,262.2 946.9,259.5 947.4,256.8 947.9,257.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="949.6,257.7 950.1,256.8 950.6,250.4 951.2,239.6 951.7,242.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="953.3,246.8 953.9,246.8 954.4,239.6 955.0,236.8 955.5,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="957.1,233.2 957.7,226.9 958.2,232.3 958.7,221.4 959.3,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="960.9,234.1 961.4,236.8 962.0,235.0 962.5,236.8 963.0,232.3" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="964.7,232.3 965.2,235.0 965.7,236.8 966.3,237.7 966.8,235.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="968.4,237.7 969.0,239.6 969.5,239.6 970.1,237.7 970.6,244.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="972.2,243.2 972.7,237.7 973.3,236.8 973.8,233.2 974.4,237.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="976.0,237.7 976.5,232.3 977.1,225.0 977.6,228.7 978.1,228.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="979.8,222.3 980.3,224.1 980.8,229.6 981.4,225.0 981.9,226.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="983.5,222.3 984.1,217.8 984.6,219.6 985.1,217.8 985.7,209.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="987.3,211.4 987.8,206.0 988.4,214.2 988.9,210.5 989.5,206.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="991.6,216.9 992.2,217.8 992.7,218.7 993.2,219.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="994.9,213.3 995.4,213.3 995.9,210.5 996.5,213.3 997.0,202.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="998.6,204.2 999.2,206.0 999.7,206.0 1000.2,213.3 1000.8,209.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1002.4,211.4 1002.9,213.3 1003.5,199.6 1004.0,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1006.2,196.0 1006.7,203.3 1007.3,207.8 1007.8,209.6 1008.3,211.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1009.9,208.7 1010.5,205.1 1011.0,202.4 1011.6,205.1" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1013.7,206.0 1014.3,200.6 1014.8,198.7 1015.3,203.3 1015.9,198.7" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1017.5,194.2 1018.0,201.5 1018.6,206.0 1019.1,203.3 1019.7,201.5" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1021.3,198.7 1021.8,194.2 1022.3,189.7 1022.9,184.2 1023.4,187.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1025.0,189.7 1025.6,194.2 1026.1,197.8 1026.7,196.9 1027.2,192.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1028.8,195.1 1029.4,199.6 1029.9,201.5 1030.4,195.1 1031.0,200.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1032.6,195.1 1033.1,197.8 1033.7,199.6 1034.2,204.2 1034.7,202.4" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1036.4,200.6 1036.9,200.6 1037.4,200.6 1038.0,200.6 1038.5,196.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1040.1,196.0 1040.7,202.4 1041.2,200.6 1041.8,199.6 1042.3,186.9" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1043.9,186.9 1044.5,182.4 1045.0,182.4 1045.5,186.9 1046.1,184.2" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1048.2,182.4 1048.8,178.8 1049.3,167.0 1049.8,160.6" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="1051.5,158.8 1052.0,157.0" fill="none" stroke="var(--s-dgs2)" stroke-width="2"/>
<polyline points="60.0,461.8 60.5,463.6 61.1,460.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="63.2,455.4 63.8,458.2 64.3,462.7 64.9,458.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="66.5,460.0 67.0,464.5 67.5,461.8 68.1,459.1 68.6,456.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="70.2,461.8 70.8,460.0 71.3,460.9 71.9,452.7 72.4,447.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="74.0,446.4 74.6,440.9 75.1,440.0 75.6,442.7 76.2,446.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="77.8,445.5 78.3,440.9 78.9,441.8 79.4,437.3 79.9,434.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="82.1,436.4 82.6,439.1 83.2,442.7 83.7,436.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="85.3,436.4 85.9,431.0 86.4,431.0 87.0,428.2 87.5,430.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="89.1,431.9 89.7,432.8 90.2,440.9 90.7,438.2 91.3,440.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="92.9,437.3 93.4,439.1 94.0,435.5 94.5,441.8 95.0,449.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="96.7,443.7 97.2,448.2 97.7,439.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="98.8" cy="437.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="100.4,432.8 101.0,432.8 101.5,435.5 102.1,436.4 102.6,440.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="104.2,432.8 104.7,429.1 105.3,431.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="106.4" cy="446.4" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="108.0,442.7 108.5,450.9 109.1,450.9 109.6,450.0 110.1,458.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="111.8,450.9 112.3,446.4 112.8,442.7 113.4,445.5 113.9,446.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="115.5,451.8 116.1,450.0 116.6,447.3 117.1,450.0 117.7,452.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="119.3,450.9 119.8,446.4 120.4,448.2 120.9,444.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="123.1,446.4 123.6,445.5 124.2,440.0 124.7,442.7 125.2,442.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="126.9,432.8 127.4,430.0 127.9,425.5 128.5,423.7 129.0,421.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="130.6,419.2 131.2,421.9 131.7,422.8 132.2,426.4 132.8,419.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="134.9,411.0 135.5,414.6 136.0,414.6 136.6,421.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="138.2,421.9 138.7,419.2 139.3,412.8 139.8,416.4 140.3,419.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="141.9,418.3 142.5,416.4 143.0,419.2 143.6,415.5 144.1,405.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="145.7,406.5 146.3,402.8 146.8,404.6 147.3,396.5 147.9,406.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="149.5,401.0 150.0,394.7 150.6,396.5 151.1,401.9 151.7,406.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="153.8,404.6 154.3,400.1 154.9,402.8 155.4,401.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="157.0,414.6 157.6,424.6 158.1,411.9 158.7,411.9 159.2,422.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="160.8,419.2 161.4,411.9 161.9,404.6 162.4,401.0 163.0,399.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="164.6,386.5 165.1,385.6 165.7,382.0 166.2,381.1 166.7,386.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="168.4,370.2 168.9,364.7 169.4,370.2 170.0,368.4 170.5,355.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="172.1,357.5 172.7,362.0 173.2,367.5 173.8,370.2 174.3,363.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="175.9,361.1 176.5,350.2 177.0,343.9 177.5,339.3 178.1,333.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="179.7,327.5 180.2,333.9 180.8,335.7 181.3,323.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="183.5,322.1 184.0,314.8 184.5,322.1 185.1,317.6 185.6,317.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="187.2,325.7 187.8,329.4 188.3,324.8 188.9,322.1 189.4,318.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="191.0,309.4 191.5,311.2 192.1,314.8 192.6,304.0 193.2,297.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="194.8,304.0 195.3,309.4 195.9,316.7 196.4,323.0 196.9,314.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="198.6,319.4 199.1,310.3 199.6,318.5 200.2,323.0 200.7,328.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="202.3,321.2 202.9,330.3 203.4,331.2 203.9,331.2 204.5,332.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="206.6,322.1 207.2,313.9 207.7,315.8 208.3,312.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="209.9,304.9 210.4,310.3 211.0,305.8 211.5,304.9 212.0,294.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="213.7,269.5 214.2,264.1 214.7,278.6 215.3,283.1 215.8,285.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="218.0,280.4 218.5,294.0 219.0,300.3 219.6,296.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="221.2,290.4 221.7,290.4 222.3,299.4 222.8,310.3 223.4,319.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="225.5,324.8 226.1,314.8 226.6,307.6 227.1,300.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="228.7,309.4 229.3,312.1 229.8,316.7 230.4,312.1 230.9,314.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="232.5,312.1 233.1,307.6 233.6,304.9 234.1,316.7 234.7,329.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="236.3,325.7 236.8,325.7 237.4,328.5 237.9,337.5 238.5,338.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="240.1,344.8 240.6,331.2 241.1,333.0 241.7,337.5 242.2,323.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="243.8,329.4 244.4,326.6 244.9,328.5 245.5,320.3 246.0,323.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="247.6,327.5 248.2,324.8 248.7,318.5 249.2,319.4 249.8,310.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="251.4,305.8 251.9,304.0 252.5,298.5 253.0,305.8 253.5,304.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="255.2,297.6 255.7,298.5 256.2,294.9 256.8,284.9 257.3,290.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="259.5,278.6 260.0,284.0 260.6,282.2 261.1,278.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="262.7,274.9 263.3,270.4 263.8,271.3 264.3,267.7 264.9,267.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="266.5,264.1 267.0,256.8 267.6,262.2 268.1,245.0 268.6,245.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="270.3,228.7 270.8,220.5 271.3,243.2 271.9,239.6 272.4,233.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="274.0,247.7 274.6,252.3 275.1,239.6 275.7,233.2 276.2,227.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="278.3,224.1 278.9,226.0 279.4,220.5 280.0,217.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="281.6,216.0 282.1,216.9 282.7,205.1 283.2,196.0 283.7,198.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="285.4,195.1 285.9,208.7 286.4,214.2 287.0,221.4 287.5,216.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="289.1,208.7 289.7,211.4 290.2,208.7 290.7,205.1 291.3,202.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="292.9,197.8 293.4,205.1 294.0,206.9 294.5,234.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="296.7,228.7 297.2,235.9 297.8,247.7 298.3,238.7 298.8,234.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="300.5,233.2 301.0,239.6 301.5,244.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="302.6" cy="246.8" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="304.2,245.9 304.8,240.5 305.3,246.8 305.8,260.4 306.4,262.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="308.0,254.1 308.5,262.2 309.1,270.4 309.6,265.0 310.2,256.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="311.8,253.2 312.3,262.2 312.9,264.1 313.4,268.6 313.9,265.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="315.5,256.8 316.1,245.9 316.6,246.8 317.2,247.7 317.7,240.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="319.9,232.3 320.4,228.7 320.9,233.2 321.5,228.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="323.6,236.8 324.2,245.9 324.7,244.1 325.3,258.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="326.9,260.4 327.4,253.2 327.9,259.5 328.5,269.5 329.0,264.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="331.2,260.4 331.7,274.9 332.3,273.1 332.8,265.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="334.4,261.3 335.0,266.8 335.5,266.8 336.0,264.1 336.6,261.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="338.2,258.6 338.7,261.3 339.3,273.1 339.8,272.2 340.3,260.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="342.0,251.4 342.5,247.7 343.0,251.4 343.6,247.7 344.1,241.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="345.7,243.2 346.3,238.7 346.8,235.0 347.4,230.5 347.9,234.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="350.1,222.3 350.6,224.1 351.1,228.7 351.7,222.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="353.3,225.0 353.8,225.0 354.4,216.9 354.9,210.5 355.4,220.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="357.1,219.6 357.6,220.5 358.1,219.6 358.7,224.1 359.2,245.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="360.8,258.6 361.4,250.4 361.9,262.2 362.5,257.7 363.0,273.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="364.6,265.9 365.1,255.0 365.7,265.0 366.2,274.0 366.8,274.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="368.4,260.4 368.9,258.6 369.5,256.8 370.0,258.6 370.5,265.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="372.2,269.5 372.7,276.7 373.2,281.3 373.8,281.3 374.3,273.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="375.9,271.3 376.5,269.5 377.0,271.3 377.5,267.7 378.1,261.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="379.7,254.1 380.2,255.9 380.8,254.1 381.3,259.5 381.9,256.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="383.5,261.3 384.0,272.2 384.6,269.5 385.1,260.4 385.6,268.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="387.3,255.0 387.8,268.6 388.3,274.0 388.9,274.9 389.4,268.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="391.0,261.3 391.6,260.4 392.1,269.5 392.6,273.1 393.2,266.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="394.8,263.1 395.3,259.5 395.9,256.8 396.4,249.5 397.0,245.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="398.6,243.2 399.1,245.0 399.7,242.3 400.2,233.2 400.7,235.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="402.9,245.9 403.4,250.4 404.0,253.2 404.5,245.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="406.1,245.9 406.7,245.0 407.2,236.8 407.7,242.3 408.3,240.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="409.9,242.3 410.4,232.3 411.0,233.2 411.5,243.2 412.1,238.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="414.2,241.4 414.7,243.2 415.3,235.9 415.8,241.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="417.4,243.2 418.0,238.7 418.5,244.1 419.1,231.4 419.6,235.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="421.2" cy="230.5" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="422.3,222.3 422.8,213.3 423.4,212.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="425.0,216.9 425.5,218.7 426.1,230.5 426.6,239.6 427.1,233.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="428.8,235.0 429.3,235.9 429.8,240.5 430.4,231.4 430.9,232.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="432.5,230.5 433.1,226.0 433.6,230.5 434.2,216.9 434.7,221.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="436.3,220.5 436.9,213.3 437.4,210.5 437.9,199.6 438.5,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="440.1,209.6 440.6,216.0 441.2,217.8 441.7,209.6 442.2,203.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="443.9,200.6 444.4,198.7 444.9,192.4 445.5,190.6 446.0,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="447.6,186.9 448.2,186.9 448.7,200.6 449.3,196.9 449.8,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="451.4,199.6 451.9,206.9 452.5,206.9 453.0,209.6 453.6,201.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="455.7,193.3 456.3,190.6 456.8,193.3 457.3,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="459.0,191.5 459.5,193.3 460.0,195.1 460.6,191.5 461.1,187.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="462.7,188.8 463.3,184.2 463.8,186.0 464.3,173.3 464.9,177.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="466.5,167.9 467.0,167.0 467.6,162.5 468.1,164.3 468.7,164.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="470.3,155.2 470.8,144.3 471.4,151.6 471.9,152.5 472.4,147.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="474.6,157.9 475.1,165.2 475.7,154.3 476.2,160.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="477.8,153.4 478.4,142.5 478.9,135.2 479.4,128.9 480.0,133.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="481.6,139.8 482.1,142.5 482.7,131.6 483.2,139.8 483.8,141.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="485.4,138.0 485.9,138.0 486.5,147.9 487.0,157.0 487.5,166.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="489.1,157.0 489.7,165.2 490.2,173.3 490.8,161.5 491.3,162.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="492.9,160.6 493.5,177.9 494.0,169.7 494.5,177.0 495.1,177.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="496.7,179.7 497.2,180.6 497.8,179.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="498.9" cy="175.2" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="500.5,182.4 501.0,186.9 501.5,193.3 502.1,184.2 502.6,197.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="504.2,192.4 504.8,201.5 505.3,206.9 505.9,205.1 506.4,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="508.0,196.9 508.6,199.6 509.1,214.2 509.6,225.0 510.2,226.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="511.8,222.3 512.3,224.1 512.9,230.5 513.4,227.8 513.9,226.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="516.1,227.8 516.6,236.8 517.2,232.3 517.7,228.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="519.9,222.3 520.4,226.0 521.0,218.7 521.5,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="523.1,216.9 523.7,216.0 524.2,214.2 524.7,219.6 525.3,221.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="527.4,211.4 528.0,208.7 528.5,205.1 529.0,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="530.7,207.8 531.2,205.1 531.7,201.5 532.3,205.1 532.8,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="534.4,210.5 535.0,212.3 535.5,218.7 536.1,229.6 536.6,215.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="538.2,202.4 538.7,209.6 539.3,209.6 539.8,204.2 540.4,202.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="542.0,202.4 542.5,189.7 543.1,193.3 543.6,196.0 544.1,190.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="546.3,193.3 546.8,188.8 547.4,187.9 547.9,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="549.5,192.4 550.1,189.7 550.6,193.3 551.1,195.1 551.7,200.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="553.3,197.8 553.8,206.0 554.4,207.8 554.9,209.6 555.5,209.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="557.1,208.7 557.6,203.3 558.2,200.6 558.7,191.5 559.2,189.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="560.9,186.9 561.4,190.6 561.9,193.3 562.5,193.3 563.0,197.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="564.6,195.1 565.2,196.0 565.7,199.6 566.2,199.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="568.4,187.9 568.9,185.1 569.5,185.1 570.0,189.7 570.6,182.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="572.2,179.7 572.7,185.1 573.3,167.9 573.8,167.0 574.3,172.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="575.9,160.6 576.5,157.0 577.0,164.3 577.6,159.7 578.1,161.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="579.7,161.5 580.3,162.5 580.8,158.8 581.3,154.3 581.9,157.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="583.5,160.6 584.0,155.2 584.6,160.6 585.1,165.2 585.7,172.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="587.3,173.3 587.8,175.2 588.3,174.2 588.9,177.0 589.4,172.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="591.0,174.2 591.6,177.0 592.1,185.1 592.7,183.3 593.2,179.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="594.8,177.9 595.4,180.6 595.9,178.8 596.4,175.2 597.0,176.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="599.1,168.8 599.7,162.5 600.2,167.9 600.7,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="602.4,180.6 602.9,187.9 603.4,191.5 604.0,192.4 604.5,178.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="606.1,175.2 606.7,182.4 607.2,189.7 607.8,196.0 608.3,199.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="609.9,192.4 610.5,197.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="611.5,195.1 612.1,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="613.7,195.1 614.2,196.9 614.8,188.8 615.3,191.5 615.8,185.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="617.5,174.2 618.0,178.8 618.5,185.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="619.6" cy="192.4" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="621.2,192.4 621.8,190.6 622.3,192.4 622.9,199.6 623.4,201.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="625.0,196.9 625.5,202.4 626.1,203.3 626.6,199.6 627.2,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="628.8,194.2 629.3,195.1 629.9,192.4 630.4,193.3 630.9,199.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="632.6,202.4 633.1,204.2 633.6,209.6 634.2,218.7 634.7,235.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="636.3,237.7 636.9,226.9 637.4,221.4 637.9,218.7 638.5,223.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="640.1,226.9 640.6,231.4 641.2,233.2 641.7,225.0 642.3,227.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="643.9,230.5 644.4,234.1 645.0,236.8 645.5,230.5 646.0,235.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="647.7,234.1 648.2,233.2 648.7,232.3 649.3,229.6 649.8,226.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="652.0,232.3 652.5,238.7 653.0,242.3 653.6,243.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="655.2,245.0 655.7,249.5 656.3,249.5 656.8,246.8 657.4,248.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="659.0,251.4 659.5,249.5 660.1,245.0 660.6,242.3 661.1,242.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="662.7,240.5 663.3,241.4 663.8,236.8 664.4,236.8 664.9,240.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="666.5,235.0 667.1,241.4 667.6,236.8 668.1,231.4 668.7,219.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="670.3,215.1 670.8,214.2 671.4,212.3 671.9,209.6 672.5,210.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="674.6,215.1 675.1,216.0 675.7,209.6 676.2,210.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="677.8,200.6 678.4,199.6 678.9,196.0 679.5,198.7 680.0,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="681.6,192.4 682.2,192.4 682.7,191.5 683.2,192.4 683.8,184.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="685.4,189.7 685.9,194.2 686.5,179.7 687.0,189.7 687.5,190.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="689.7,178.8 690.2,177.9 690.8,178.8 691.3,178.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="692.9,179.7 693.5,182.4 694.0,180.6 694.6,178.8 695.1,180.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="696.7,193.3 697.3,190.6 697.8,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="698.9" cy="201.5" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="700.5,200.6 701.0,196.9 701.6,200.6 702.1,202.4 702.6,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="704.3,199.6 704.8,197.8 705.3,194.2 705.9,188.8 706.4,181.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="708.0,182.4 708.6,181.5 709.1,172.4 709.7,166.1 710.2,170.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="711.8,164.3 712.3,164.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="713.4,165.2 714.0,161.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="715.6,167.9 716.1,165.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="717.2,166.1 717.7,163.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="719.4,161.5 719.9,157.0 720.4,157.0 721.0,156.1 721.5,147.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="723.1,146.1 723.7,147.0 724.2,157.9 724.7,162.5 725.3,162.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="727.4,166.1 728.0,163.4 728.5,158.8 729.1,160.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="730.7,169.7 731.2,167.9 731.8,167.9 732.3,170.6 732.8,165.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="734.5,168.8 735.0,170.6 735.5,178.8 736.1,177.0 736.6,173.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="738.2,171.5 738.8,168.8 739.3,161.5 739.8,170.6 740.4,175.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="742.5,167.9 743.1,169.7 743.6,172.4 744.2,179.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="745.8,181.5 746.3,190.6 746.9,195.1 747.4,191.5 747.9,196.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="749.5,203.3 750.1,197.8 750.6,192.4 751.2,191.5 751.7,188.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="753.3,197.8 753.9,192.4 754.4,188.8 754.9,193.3 755.5,189.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="757.1,189.7 757.6,191.5 758.2,195.1 758.7,196.0 759.3,195.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="760.9,186.9 761.4,189.7 761.9,186.0 762.5,183.3 763.0,193.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="764.6,196.9 765.2,202.4 765.7,199.6 766.3,212.3 766.8,216.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="768.4,204.2 769.0,194.2 769.5,186.9 770.0,181.5 770.6,174.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="772.2,183.3 772.7,186.0 773.3,191.5 773.8,186.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="776.0,179.7 776.5,180.6 777.0,181.5 777.6,188.8 778.1,191.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="779.7,196.9 780.3,200.6 780.8,202.4 781.4,195.1 781.9,187.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="783.5,185.1 784.1,190.6 784.6,194.2 785.1,184.2 785.7,184.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="787.3,177.0 787.8,173.3 788.4,169.7 788.9,177.0 789.4,178.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="791.1,176.1 791.6,174.2 792.1,165.2 792.7,168.8 793.2,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="795.4,178.8 795.9,175.2 796.5,178.8 797.0,180.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="798.6,176.1 799.1,176.1 799.7,184.2 800.2,181.5 800.8,171.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="802.4,173.3 802.9,175.2 803.5,180.6 804.0,185.1 804.5,180.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="806.2,176.1 806.7,182.4 807.2,183.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="808.3" cy="183.3" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="809.9,186.9 810.5,190.6 811.0,191.5 811.5,194.2 812.1,191.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="813.7,196.0 814.2,194.2 814.8,190.6 815.3,186.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="817.5,181.5 818.0,179.7 818.6,186.9 819.1,186.0 819.6,178.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="821.3,178.8 821.8,172.4 822.3,176.1 822.9,175.2 823.4,177.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="825.0,183.3 825.6,186.0 826.1,181.5 826.6,178.8 827.2,181.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="828.8,179.7 829.3,186.9 829.9,183.3 830.4,184.2 831.0,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="832.6,197.8 833.1,197.8 833.7,197.8 834.2,196.9 834.7,193.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="836.3,193.3 836.9,191.5 837.4,196.0 838.0,191.5 838.5,187.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="840.1,186.9 840.7,190.6 841.2,191.5 841.7,187.9 842.3,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="843.9,192.4 844.4,194.2 845.0,196.0 845.5,197.8 846.1,196.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="848.2,192.4 848.7,197.8 849.3,202.4 849.8,208.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="851.4,213.3 852.0,210.5 852.5,214.2 853.1,216.9 853.6,212.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="855.2,213.3 855.8,214.2 856.3,212.3 856.8,207.8 857.4,205.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="859.0,204.2 859.5,206.9 860.1,203.3 860.6,201.5 861.1,199.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="862.8,204.2 863.3,203.3 863.8,206.9 864.4,208.7 864.9,206.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="866.5,201.5 867.1,205.1 867.6,206.0 868.2,205.1 868.7,213.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="870.9,215.1 871.4,213.3 871.9,218.7 872.5,216.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="874.1,217.8 874.6,219.6 875.2,220.5 875.7,216.9 876.2,216.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="877.9,216.9 878.4,218.7 878.9,210.5 879.5,207.8 880.0,207.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="881.6,206.0 882.2,208.7 882.7,202.4 883.3,207.8 883.8,207.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="885.4" cy="206.0" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="886.5,210.5 887.0,207.8 887.6,205.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="889.2,206.0 889.7,206.9 890.3,206.0 890.8,208.7 891.3,212.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="893.0,214.2 893.5,216.9 894.0,217.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="895.1" cy="216.0" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="896.7,209.6 897.3,209.6 897.8,212.3 898.3,207.8 898.9,205.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="900.5,202.4 901.0,201.5 901.6,206.0 902.1,205.1 902.7,200.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="904.3,201.5 904.8,204.2 905.4,203.3 905.9,206.9 906.4,203.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="908.1,202.4 908.6,201.5 909.1,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="910.2" cy="205.1" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="911.8,206.9 912.4,205.1 912.9,201.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<circle cx="914.0" cy="200.6" r="2.4" fill="var(--s-dgs10)"/>
<polyline points="915.6,202.4 916.1,201.5 916.7,204.2 917.2,200.6 917.8,201.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="919.4,200.6 919.9,201.5 920.5,204.2 921.0,202.4 921.5,196.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="923.7,190.6 924.2,194.2 924.8,194.2 925.3,196.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="926.9,197.8 927.5,196.0 928.0,194.2 928.5,196.0 929.1,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="930.7,191.5 931.2,192.4 931.8,191.5 932.3,198.7 932.9,197.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="934.5,197.8 935.0,203.3 935.5,201.5 936.1,209.6 936.6,214.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="938.8,213.3 939.3,209.6 939.9,210.5 940.4,210.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="942.0,215.1 942.6,214.2 943.1,213.3 943.6,216.0 944.2,220.5" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="945.8,213.3 946.3,212.3 946.9,209.6 947.4,206.0 947.9,204.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="949.6,206.9 950.1,204.2 950.6,198.7 951.2,193.3 951.7,192.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="953.3,196.9 953.9,199.6 954.4,194.2 955.0,195.1 955.5,182.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="957.1,186.9 957.7,182.4 958.2,187.9 958.7,179.7 959.3,177.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="960.9,186.0 961.4,190.6 962.0,187.9 962.5,189.7 963.0,186.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="964.7,186.9 965.2,187.9 965.7,191.5 966.3,191.5 966.8,189.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="968.4,190.6 969.0,194.2 969.5,191.5 970.1,188.8 970.6,194.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="972.2,194.2 972.7,190.6 973.3,190.6 973.8,186.9 974.4,189.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="976.0,186.0 976.5,185.1 977.1,179.7 977.6,181.5 978.1,182.4" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="979.8,177.0 980.3,178.8 980.8,185.1 981.4,180.6 981.9,183.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="983.5,179.7 984.1,176.1 984.6,176.1 985.1,175.2 985.7,164.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="987.3,162.5 987.8,157.0 988.4,166.1 988.9,166.1 989.5,167.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="991.6,172.4 992.2,174.2 992.7,177.0 993.2,177.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="994.9,175.2 995.4,176.1 995.9,173.3 996.5,175.2 997.0,167.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="998.6,167.0 999.2,169.7 999.7,167.9 1000.2,177.0 1000.8,174.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1002.4,175.2 1002.9,178.8 1003.5,173.3 1004.0,176.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1006.2,171.5 1006.7,172.4 1007.3,180.6 1007.8,181.5 1008.3,183.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1009.9,183.3 1010.5,177.9 1011.0,174.2 1011.6,173.3" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1013.7,174.2 1014.3,167.9 1014.8,167.0 1015.3,168.8 1015.9,167.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1017.5,161.5 1018.0,165.2 1018.6,167.9 1019.1,166.1 1019.7,167.9" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1021.3,163.4 1021.8,160.6 1022.3,157.0 1022.9,153.4 1023.4,155.2" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1025.0,158.8 1025.6,162.5 1026.1,157.0 1026.7,156.1 1027.2,149.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1028.8,154.3 1029.4,160.6 1029.9,160.6 1030.4,155.2 1031.0,158.8" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1032.6,152.5 1033.1,154.3 1033.7,156.1 1034.2,160.6 1034.7,156.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1036.4,152.5 1036.9,153.4 1037.4,158.8 1038.0,155.2 1038.5,150.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1040.1,154.3 1040.7,159.7 1041.2,157.9 1041.8,157.0 1042.3,151.6" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1043.9,149.8 1044.5,146.1 1045.0,146.1 1045.5,147.9 1046.1,147.0" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1048.2,145.2 1048.8,142.5 1049.3,131.6 1049.8,130.7" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="1051.5,129.8 1052.0,127.1" fill="none" stroke="var(--s-dgs10)" stroke-width="2"/>
<polyline points="60.0,406.5 60.5,408.3 61.1,404.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="63.2,400.1 63.8,403.7 64.3,408.3 64.9,404.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="66.5,407.4 67.0,412.8 67.5,411.0 68.1,410.1 68.6,407.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="70.2,412.8 70.8,411.9 71.3,413.7 71.9,406.5 72.4,400.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="74.0,400.1 74.6,392.9 75.1,391.0 75.6,391.9 76.2,395.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="77.8,394.7 78.3,390.1 78.9,391.9 79.4,387.4 79.9,384.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="82.1,390.1 82.6,394.7 83.2,397.4 83.7,394.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="85.3,398.3 85.9,391.0 86.4,388.3 87.0,387.4 87.5,391.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="89.1,391.0 89.7,394.7 90.2,403.7 90.7,402.8 91.3,405.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="92.9,401.0 93.4,402.8 94.0,399.2 94.5,402.8 95.0,411.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="96.7,409.2 97.2,414.6 97.7,406.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="98.8" cy="403.7" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="100.4,398.3 101.0,397.4 101.5,399.2 102.1,401.9 102.6,407.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="104.2,401.0 104.7,397.4 105.3,402.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="106.4" cy="414.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="108.0,411.0 108.5,419.2 109.1,420.1 109.6,421.0 110.1,427.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="111.8,421.9 112.3,417.3 112.8,411.0 113.4,411.0 113.9,410.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="115.5,416.4 116.1,415.5 116.6,411.9 117.1,411.0 117.7,415.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="119.3,412.8 119.8,409.2 120.4,411.9 120.9,407.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="123.1,410.1 123.6,408.3 124.2,402.8 124.7,405.6 125.2,408.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="126.9,398.3 127.4,392.9 127.9,391.0 128.5,391.0 129.0,389.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="130.6,389.2 131.2,391.9 131.7,391.9 132.2,394.7 132.8,388.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="134.9,382.9 135.5,386.5 136.0,386.5 136.6,392.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="138.2,390.1 138.7,388.3 139.3,384.7 139.8,391.0 140.3,392.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="141.9,389.2 142.5,388.3 143.0,389.2 143.6,386.5 144.1,378.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="145.7,379.3 146.3,376.5 146.8,376.5 147.3,372.0 147.9,377.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="149.5,372.9 150.0,365.6 150.6,368.4 151.1,371.1 151.7,377.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="153.8,377.4 154.3,372.9 154.9,373.8 155.4,372.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="157.0,383.8 157.6,389.2 158.1,377.4 158.7,377.4 159.2,384.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="160.8,382.0 161.4,377.4 161.9,372.9 162.4,364.7 163.0,366.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="164.6,356.6 165.1,354.8 165.7,357.5 166.2,353.9 166.7,361.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="168.4,349.3 168.9,344.8 169.4,352.0 170.0,352.9 170.5,344.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="172.1,347.5 172.7,351.1 173.2,355.7 173.8,359.3 174.3,359.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="175.9,355.7 176.5,347.5 177.0,342.1 177.5,336.6 178.1,330.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="179.7,323.0 180.2,324.8 180.8,325.7 181.3,315.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="183.5,313.0 184.0,307.6 184.5,317.6 185.1,313.9 185.6,313.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="187.2,319.4 187.8,321.2 188.3,316.7 188.9,315.8 189.4,312.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="191.0,302.1 191.5,305.8 192.1,307.6 192.6,294.9 193.2,287.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="194.8,291.3 195.3,297.6 195.9,304.0 196.4,308.5 196.9,299.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="198.6,300.3 199.1,293.1 199.6,302.1 200.2,304.0 200.7,309.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="202.3,301.2 202.9,310.3 203.4,311.2 203.9,309.4 204.5,311.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="206.6,302.1 207.2,300.3 207.7,300.3 208.3,298.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="209.9,291.3 210.4,296.7 211.0,292.2 211.5,292.2 212.0,290.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="213.7,270.4 214.2,267.7 214.7,273.1 215.3,276.7 215.8,281.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="218.0,273.1 218.5,285.8 219.0,289.4 219.6,284.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="221.2,280.4 221.7,281.3 222.3,288.5 222.8,295.8 223.4,298.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="225.5,304.0 226.1,295.8 226.6,290.4 227.1,284.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="228.7,292.2 229.3,296.7 229.8,301.2 230.4,298.5 230.9,299.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="232.5,295.8 233.1,293.1 233.6,293.1 234.1,301.2 234.7,308.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="236.3,304.9 236.8,305.8 237.4,305.8 237.9,306.7 238.5,308.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="240.1,315.8 240.6,308.5 241.1,312.1 241.7,311.2 242.2,303.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="243.8,308.5 244.4,307.6 244.9,304.9 245.5,294.9 246.0,297.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="247.6,299.4 248.2,298.5 248.7,294.9 249.2,295.8 249.8,288.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="251.4,286.7 251.9,284.9 252.5,279.5 253.0,285.8 253.5,289.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="255.2,285.8 255.7,287.6 256.2,284.0 256.8,274.9 257.3,276.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="259.5,264.1 260.0,270.4 260.6,267.7 261.1,265.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="262.7,260.4 263.3,262.2 263.8,265.9 264.3,265.0 264.9,261.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="266.5,261.3 267.0,255.0 267.6,263.1 268.1,249.5 268.6,253.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="270.3,243.2 270.8,229.6 271.3,245.0 271.9,244.1 272.4,236.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="274.0,242.3 274.6,245.0 275.1,237.7 275.7,235.0 276.2,230.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="278.3,225.0 278.9,226.9 279.4,220.5 280.0,218.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="281.6,214.2 282.1,214.2 282.7,204.2 283.2,196.0 283.7,187.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="285.4,181.5 285.9,194.2 286.4,200.6 287.0,206.9 287.5,204.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="289.1,197.8 289.7,205.1 290.2,204.2 290.7,201.5 291.3,193.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="292.9,186.9 293.4,192.4 294.0,189.7 294.5,215.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="296.7,211.4 297.2,219.6 297.8,231.4 298.3,227.8 298.8,225.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="300.5,226.0 301.0,233.2 301.5,241.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="302.6" cy="241.4" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="304.2,241.4 304.8,235.0 305.3,235.9 305.8,250.4 306.4,257.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="308.0,252.3 308.5,261.3 309.1,270.4 309.6,268.6 310.2,257.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="311.8,256.8 312.3,260.4 312.9,261.3 313.4,265.0 313.9,260.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="315.5,252.3 316.1,241.4 316.6,241.4 317.2,242.3 317.7,234.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="319.9,224.1 320.4,219.6 320.9,225.0 321.5,220.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="323.6,228.7 324.2,235.0 324.7,237.7 325.3,247.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="326.9,248.6 327.4,241.4 327.9,247.7 328.5,257.7 329.0,253.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="331.2,250.4 331.7,259.5 332.3,256.8 332.8,248.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="334.4,245.9 335.0,252.3 335.5,252.3 336.0,252.3 336.6,250.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="338.2,248.6 338.7,249.5 339.3,258.6 339.8,258.6 340.3,251.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="342.0,247.7 342.5,243.2 343.0,245.0 343.6,240.5 344.1,233.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="345.7,236.8 346.3,235.0 346.8,231.4 347.4,225.0 347.9,228.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="350.1,219.6 350.6,223.2 351.1,228.7 351.7,224.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="353.3,224.1 353.8,224.1 354.4,220.5 354.9,215.1 355.4,226.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="357.1,225.0 357.6,228.7 358.1,228.7 358.7,228.7 359.2,245.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="360.8,245.0 361.4,238.7 361.9,245.0 362.5,244.1 363.0,254.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="364.6,249.5 365.1,242.3 365.7,246.8 366.2,248.6 366.8,250.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="368.4,238.7 368.9,238.7 369.5,237.7 370.0,241.4 370.5,247.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="372.2,250.4 372.7,254.1 373.2,257.7 373.8,259.5 374.3,253.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="375.9,252.3 376.5,252.3 377.0,250.4 377.5,245.9 378.1,241.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="379.7,235.0 380.2,236.8 380.8,236.8 381.3,240.5 381.9,237.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="383.5,242.3 384.0,249.5 384.6,245.0 385.1,239.6 385.6,247.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="387.3,232.3 387.8,243.2 388.3,245.0 388.9,242.3 389.4,239.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="391.0,232.3 391.6,231.4 392.1,235.9 392.6,242.3 393.2,237.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="394.8,232.3 395.3,229.6 395.9,228.7 396.4,226.0 397.0,222.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="398.6,220.5 399.1,221.4 399.7,220.5 400.2,216.9 400.7,221.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="402.9,226.9 403.4,231.4 404.0,232.3 404.5,228.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="406.1,227.8 406.7,229.6 407.2,222.3 407.7,227.8 408.3,227.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="409.9,229.6 410.4,223.2 411.0,226.9 411.5,231.4 412.1,230.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="414.2,233.2 414.7,235.0 415.3,228.7 415.8,234.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="417.4,233.2 418.0,232.3 418.5,235.0 419.1,225.0 419.6,231.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="421.2" cy="229.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="422.3,222.3 422.8,216.9 423.4,213.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="425.0,213.3 425.5,215.1 426.1,221.4 426.6,226.9 427.1,224.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="428.8,223.2 429.3,226.0 429.8,232.3 430.4,226.0 430.9,226.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="432.5,225.0 433.1,222.3 433.6,223.2 434.2,212.3 434.7,215.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="436.3,216.0 436.9,207.8 437.4,202.4 437.9,188.8 438.5,198.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="440.1,193.3 440.6,199.6 441.2,201.5 441.7,196.0 442.2,193.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="443.9,191.5 444.4,188.8 444.9,183.3 445.5,180.6 446.0,183.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="447.6,177.0 448.2,179.7 448.7,193.3 449.3,190.6 449.8,190.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="451.4,191.5 451.9,196.9 452.5,196.9 453.0,199.6 453.6,191.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="455.7,183.3 456.3,184.2 456.8,185.1 457.3,187.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="459.0,184.2 459.5,186.0 460.0,186.9 460.6,182.4 461.1,179.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="462.7,181.5 463.3,178.8 463.8,181.5 464.3,167.0 464.9,169.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="466.5,157.0 467.0,154.3 467.6,151.6 468.1,153.4 468.7,151.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="470.3,144.3 470.8,131.6 471.4,138.9 471.9,137.1 472.4,131.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="474.6,140.7 475.1,151.6 475.7,139.8 476.2,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="477.8,138.9 478.4,132.5 478.9,127.1 479.4,117.1 480.0,118.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="481.6,126.2 482.1,130.7 482.7,118.9 483.2,126.2 483.8,124.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="485.4,123.5 485.9,123.5 486.5,130.7 487.0,143.4 487.5,147.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="489.1,141.6 489.7,149.8 490.2,159.7 490.8,147.9 491.3,151.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="492.9,149.8 493.5,162.5 494.0,156.1 494.5,160.6 495.1,164.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="496.7,166.1 497.2,166.1 497.8,167.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="498.9" cy="163.4" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="500.5,169.7 501.0,170.6 501.5,177.9 502.1,168.8 502.6,181.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="504.2,178.8 504.8,190.6 505.3,197.8 505.9,195.1 506.4,189.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="508.0,188.8 508.6,190.6 509.1,200.6 509.6,215.1 510.2,217.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="511.8,213.3 512.3,215.1 512.9,219.6 513.4,215.1 513.9,213.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="516.1,214.2 516.6,222.3 517.2,219.6 517.7,215.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="519.9,210.5 520.4,213.3 521.0,206.0 521.5,198.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="523.1,202.4 523.7,201.5 524.2,199.6 524.7,201.5 525.3,199.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="527.4,190.6 528.0,189.7 528.5,184.2 529.0,185.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="530.7,188.8 531.2,183.3 531.7,180.6 532.3,183.3 532.8,183.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="534.4,189.7 535.0,192.4 535.5,197.8 536.1,208.7 536.6,197.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="538.2,186.0 538.7,191.5 539.3,189.7 539.8,185.1 540.4,184.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="542.0,184.2 542.5,176.1 543.1,177.0 543.6,179.7 544.1,177.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="546.3,177.9 546.8,173.3 547.4,175.2 547.9,184.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="549.5,181.5 550.1,177.9 550.6,181.5 551.1,183.3 551.7,187.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="553.3,185.1 553.8,193.3 554.4,196.0 554.9,195.1 555.5,194.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="557.1,194.2 557.6,189.7 558.2,186.0 558.7,177.9 559.2,178.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="560.9,176.1 561.4,177.9 561.9,177.0 562.5,177.9 563.0,182.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="564.6,179.7 565.2,181.5 565.7,185.1 566.2,186.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="568.4,175.2 568.9,171.5 569.5,171.5 570.0,175.2 570.6,168.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="572.2,167.9 572.7,172.4 573.3,159.7 573.8,158.8 574.3,162.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="575.9,150.7 576.5,147.9 577.0,153.4 577.6,150.7 578.1,152.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="579.7,152.5 580.3,151.6 580.8,147.0 581.3,143.4 581.9,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="583.5,149.8 584.0,146.1 584.6,150.7 585.1,152.5 585.7,157.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="587.3,159.7 587.8,162.5 588.3,159.7 588.9,163.4 589.4,159.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="591.0,160.6 591.6,164.3 592.1,170.6 592.7,170.6 593.2,167.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="594.8,165.2 595.4,167.9 595.9,167.9 596.4,165.2 597.0,166.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="599.1,157.9 599.7,150.7 600.2,155.2 600.7,158.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="602.4,167.9 602.9,174.2 603.4,177.9 604.0,178.8 604.5,167.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="606.1,164.3 606.7,169.7 607.2,175.2 607.8,181.5 608.3,186.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="609.9,181.5 610.5,185.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="611.5,182.4 612.1,182.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="613.7,183.3 614.2,185.1 614.8,177.0 615.3,178.8 615.8,171.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="617.5,159.7 618.0,163.4 618.5,169.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="619.6" cy="175.2" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="621.2,176.1 621.8,173.3 622.3,175.2 622.9,180.6 623.4,182.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="625.0,176.1 625.5,183.3 626.1,184.2 626.6,180.6 627.2,177.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="628.8,174.2 629.3,174.2 629.9,168.8 630.4,172.4 630.9,177.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="632.6,179.7 633.1,181.5 633.6,186.0 634.2,193.3 634.7,207.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="636.3,212.3 636.9,201.5 637.4,194.2 637.9,192.4 638.5,196.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="640.1,200.6 640.6,203.3 641.2,206.9 641.7,201.5 642.3,204.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="643.9,207.8 644.4,211.4 645.0,212.3 645.5,206.0 646.0,208.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="647.7,207.8 648.2,206.0 648.7,206.0 649.3,204.2 649.8,199.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="652.0,206.0 652.5,212.3 653.0,216.0 653.6,215.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="655.2,217.8 655.7,220.5 656.3,221.4 656.8,217.8 657.4,219.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="659.0,223.2 659.5,221.4 660.1,215.1 660.6,212.3 661.1,211.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="662.7,209.6 663.3,209.6 663.8,205.1 664.4,206.9 664.9,208.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="666.5,205.1 667.1,210.5 667.6,205.1 668.1,201.5 668.7,194.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="670.3,190.6 670.8,188.8 671.4,186.9 671.9,183.3 672.5,182.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="674.6,188.8 675.1,190.6 675.7,182.4 676.2,183.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="677.8,173.3 678.4,173.3 678.9,171.5 679.5,175.2 680.0,171.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="681.6,169.7 682.2,170.6 682.7,173.3 683.2,175.2 683.8,166.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="685.4,172.4 685.9,177.9 686.5,163.4 687.0,170.6 687.5,175.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="689.7,165.2 690.2,160.6 690.8,165.2 691.3,163.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="692.9,162.5 693.5,166.1 694.0,164.3 694.6,162.5 695.1,163.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="696.7,177.0 697.3,174.2 697.8,177.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="698.9" cy="185.1" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="700.5,185.1 701.0,181.5 701.6,186.0 702.1,187.9 702.6,186.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="704.3,182.4 704.8,180.6 705.3,174.2 705.9,167.9 706.4,162.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="708.0,163.4 708.6,164.3 709.1,158.8 709.7,150.7 710.2,152.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="711.8,147.0 712.3,148.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="713.4,148.8 714.0,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="715.6,147.9 716.1,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="717.2,146.1 717.7,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="719.4,140.7 719.9,135.2 720.4,135.2 721.0,134.3 721.5,130.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="723.1,129.8 723.7,128.9 724.2,138.0 724.7,141.6 725.3,141.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="727.4,145.2 728.0,143.4 728.5,138.9 729.1,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="730.7,148.8 731.2,147.0 731.8,146.1 732.3,148.8 732.8,142.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="734.5,147.9 735.0,149.8 735.5,159.7 736.1,158.8 736.6,155.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="738.2,153.4 738.8,149.8 739.3,142.5 739.8,152.5 740.4,155.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="742.5,147.9 743.1,148.8 743.6,150.7 744.2,157.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="745.8,157.9 746.3,167.9 746.9,171.5 747.4,167.0 747.9,171.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="749.5,177.0 750.1,169.7 750.6,166.1 751.2,165.2 751.7,161.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="753.3,168.8 753.9,164.3 754.4,160.6 754.9,164.3 755.5,161.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="757.1,163.4 757.6,165.2 758.2,167.0 758.7,167.9 759.3,164.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="760.9,157.9 761.4,158.8 761.9,155.2 762.5,151.6 763.0,159.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="764.6,164.3 765.2,170.6 765.7,168.8 766.3,173.3 766.8,180.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="768.4,165.2 769.0,153.4 769.5,152.5 770.0,139.8 770.6,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="772.2,145.2 772.7,146.1 773.3,150.7 773.8,145.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="776.0,135.2 776.5,138.0 777.0,142.5 777.6,147.9 778.1,150.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="779.7,155.2 780.3,159.7 780.8,157.9 781.4,150.7 781.9,146.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="783.5,142.5 784.1,144.3 784.6,147.9 785.1,142.5 785.7,142.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="787.3,137.1 787.8,132.5 788.4,129.8 788.9,135.2 789.4,137.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="791.1,134.3 791.6,130.7 792.1,119.8 792.7,122.5 793.2,123.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="795.4,132.5 795.9,129.8 796.5,134.3 797.0,134.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="798.6,128.0 799.1,128.9 799.7,137.1 800.2,138.0 800.8,129.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="802.4,131.6 802.9,133.4 803.5,135.2 804.0,141.6 804.5,136.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="806.2,130.7 806.7,138.0 807.2,138.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="808.3" cy="137.1" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="809.9,138.9 810.5,142.5 811.0,142.5 811.5,144.3 812.1,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="813.7,147.0 814.2,147.0 814.8,143.4 815.3,139.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="817.5,134.3 818.0,132.5 818.6,138.9 819.1,139.8 819.6,130.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="821.3,129.8 821.8,126.2 822.3,126.2 822.9,126.2 823.4,127.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="825.0,132.5 825.6,136.2 826.1,131.6 826.6,130.7 827.2,134.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="828.8,130.7 829.3,139.8 829.9,137.1 830.4,137.1 831.0,144.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="832.6,145.2 833.1,147.0 833.7,144.3 834.2,144.3 834.7,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="836.3,141.6 836.9,138.0 837.4,142.5 838.0,138.0 838.5,134.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="840.1,132.5 840.7,136.2 841.2,137.1 841.7,134.3 842.3,138.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="843.9,137.1 844.4,136.2 845.0,135.2 845.5,138.0 846.1,134.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="848.2,129.8 848.7,136.2 849.3,139.8 849.8,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="851.4,155.2 852.0,152.5 852.5,155.2 853.1,158.8 853.6,156.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="855.2,157.9 855.8,158.8 856.3,157.9 856.8,152.5 857.4,149.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="859.0,147.9 859.5,151.6 860.1,148.8 860.6,149.8 861.1,147.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="862.8,153.4 863.3,151.6 863.8,152.5 864.4,155.2 864.9,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="866.5,148.8 867.1,151.6 867.6,152.5 868.2,152.5 868.7,160.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="870.9,161.5 871.4,159.7 871.9,165.2 872.5,163.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="874.1,165.2 874.6,167.9 875.2,168.8 875.7,165.2 876.2,164.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="877.9,166.1 878.4,167.9 878.9,162.5 879.5,158.8 880.0,157.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="881.6,155.2 882.2,157.0 882.7,150.7 883.3,155.2 883.8,154.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="885.4" cy="153.4" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="886.5,157.0 887.0,154.3 887.6,150.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="889.2,151.6 889.7,150.7 890.3,149.8 890.8,151.6 891.3,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="893.0,156.1 893.5,157.0 894.0,159.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="895.1" cy="157.0" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="896.7,150.7 897.3,150.7 897.8,151.6 898.3,148.8 898.9,146.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="900.5,144.3 901.0,145.2 901.6,147.0 902.1,146.1 902.7,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="904.3,141.6 904.8,143.4 905.4,142.5 905.9,145.2 906.4,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="908.1,141.6 908.6,142.5 909.1,146.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="910.2" cy="144.3" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="911.8,145.2 912.4,144.3 912.9,141.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="914.0" cy="139.8" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="915.6,140.7 916.1,139.8 916.7,143.4 917.2,140.7 917.8,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="919.4,142.5 919.9,142.5 920.5,146.1 921.0,146.1 921.5,142.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="923.7,135.2 924.2,138.9 924.8,141.6 925.3,143.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="926.9,145.2 927.5,142.5 928.0,140.7 928.5,140.7 929.1,138.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="930.7,136.2 931.2,136.2 931.8,135.2 932.3,140.7 932.9,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="934.5,140.7 935.0,147.0 935.5,143.4 936.1,152.5 936.6,155.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="938.8,156.1 939.3,153.4 939.9,154.3 940.4,152.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="942.0,154.3 942.6,154.3 943.1,154.3 943.6,157.0 944.2,159.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="945.8,154.3 946.3,154.3 946.9,152.5 947.4,150.7 947.9,147.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="949.6,152.5 950.1,147.0 950.6,139.8 951.2,138.0 951.7,136.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="953.3,139.8 953.9,140.7 954.4,138.0 955.0,142.5 955.5,130.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="957.1,135.2 957.7,132.5 958.2,137.1 958.7,133.4 959.3,128.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="960.9,135.2 961.4,138.0 962.0,135.2 962.5,138.0 963.0,135.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="964.7,137.1 965.2,136.2 965.7,137.1 966.3,136.2 966.8,135.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="968.4,136.2 969.0,138.9 969.5,137.1 970.1,133.4 970.6,138.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="972.2,138.0 972.7,137.1 973.3,136.2 973.8,134.3 974.4,135.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="976.0,132.5 976.5,132.5 977.1,128.9 977.6,128.9 978.1,129.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="979.8,125.3 980.3,128.9 980.8,132.5 981.4,129.8 981.9,131.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="983.5,128.9 984.1,124.4 984.6,124.4 985.1,125.3 985.7,116.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="987.3,114.4 987.8,110.8 988.4,117.1 988.9,118.0 989.5,120.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="991.6,124.4 992.2,126.2 992.7,128.9 993.2,128.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="994.9,128.0 995.4,129.8 995.9,128.0 996.5,129.8 997.0,126.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="998.6,124.4 999.2,126.2 999.7,124.4 1000.2,131.6 1000.8,129.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1002.4,129.8 1002.9,133.4 1003.5,133.4 1004.0,136.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1006.2,131.6 1006.7,132.5 1007.3,139.8 1007.8,139.8 1008.3,138.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1009.9,139.8 1010.5,135.2 1011.0,129.8 1011.6,128.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1013.7,128.0 1014.3,122.5 1014.8,121.6 1015.3,122.5 1015.9,121.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1017.5,118.0 1018.0,119.8 1018.6,119.8 1019.1,118.9 1019.7,121.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1021.3,117.1 1021.8,115.3 1022.3,113.5 1022.9,111.7 1023.4,112.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1025.0,116.2 1025.6,118.9 1026.1,108.9 1026.7,108.0 1027.2,102.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1028.8,106.2 1029.4,110.8 1029.9,111.7 1030.4,107.1 1031.0,109.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1032.6,104.4 1033.1,105.3 1033.7,105.3 1034.2,108.0 1034.7,104.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1036.4,99.0 1036.9,101.7 1037.4,109.8 1038.0,106.2 1038.5,102.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1040.1,106.2 1040.7,111.7 1041.2,110.8 1041.8,109.8 1042.3,107.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1043.9,104.4 1044.5,102.6 1045.0,102.6 1045.5,104.4 1046.1,105.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1048.2,104.4 1048.8,101.7 1049.3,93.5 1049.8,95.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1051.5,96.2 1052.0,94.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<text x="1058" y="98.4" font-size="11.5" font-weight="700" fill="var(--s-dgs30)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 30년물 국채금리 5.36%</text>
<text x="1058" y="131.1" font-size="11.5" font-weight="700" fill="var(--s-dgs10)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 10년물 국채금리 5.00%</text>
<text x="1058" y="161.0" font-size="11.5" font-weight="700" fill="var(--s-dgs2)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 2년물 국채금리 4.67%</text>
</svg>
</div>

### 5년간 변화 요약

| 지표 | 시작 | 현재 | 변화 | 기간 최고 | 기간 최저 |
|------|------|------|------|-----------|-----------|
| 미국 2년물 국채금리 | 0.20% (2021-09-01) | 4.67% (2026-09-15) | +4.47 | 5.19% (2023-10-17) | 0.20% (2021-09-01) |
| 미국 10년물 국채금리 | 1.31% (2021-09-01) | 5.00% (2026-09-15) | +3.69 | 5.00% (2026-09-15) | 1.28% (2021-09-14) |
| 미국 30년물 국채금리 | 1.92% (2021-09-01) | 5.36% (2026-09-15) | +3.44 | 5.37% (2026-09-10) | 1.69% (2021-12-03) |

---

## 2. 해석

수치는 위 차트와 표에만 둔다 — 이 절은 그 표를 **어떻게 읽는지**만 정리한다.

- **먼저 볼 것**: 세 만기의 변화(%p) 방향과 크기 순서. 셋이 비슷한 폭으로 움직였다면(평행 이동) 금리 수준 전체가 재조정된 것이고, 만기별로 크기가 갈렸다면 수익률곡선의 **모양**(가팔라짐·평평해짐)이 바뀐 것이다.
- **수익률곡선의 기울기 = 10년물 − 2년물**: 표의 두 "현재" 값을 빼면 장단기 스프레드(흔히 2s10s로 부른다)가 나온다. 양수면 정상(장기 > 단기), 음수면 **역전(inversion)**이다. 장단기 금리 역전은 역사적으로 경기침체의 선행지표로 자주 인용되는 신호이고, 역전이 풀려 다시 양수로 돌아서는 시점 또한 별개의 관전 포인트로 다뤄진다 — 차트에서 두 선이 교차하는 구간을 함께 확인한다.
- **만기별로 담고 있는 정보가 다르다**: 2년물은 앞으로 몇 차례 FOMC의 정책금리 경로 기대를, 10년물은 장기 성장·물가 기대를, 30년물은 거기에 기간 프리미엄(장기 국채 발행량·재정 전망)까지 반영한다. 단기물만 크게 움직인 구간은 통화정책이, 장기물만 크게 움직인 구간은 재정·인플레이션 기대가 주도했다고 읽는다.
- **30년물 − 10년물 = 장기 구간의 기간 프리미엄**: 이 스프레드가 시작 시점과 크게 다르지 않다면 장기 구간의 프리미엄이 안정적으로 유지됐다는 뜻이고, 벌어졌다면 시장이 먼 미래의 재정·물가 위험에 대해 더 큰 보상을 요구하기 시작했다는 신호로 읽는다.

---

*작성일: 2026-09-18*
