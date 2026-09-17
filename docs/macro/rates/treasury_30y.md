# 미국 30년물 국채금리

::: info
만기 30년 미 국채의 상수만기(constant maturity) 수익률이다(FRED `DGS30`). [2년물](./treasury_2y.md)·[10년물](./treasury_10y.md)과 함께 보면 수익률곡선에서 가장 만기가 긴 구간까지 채워서 볼 수 있다.

:::
---

## 1. 차트 — 최근 5년 일간

<style>
.fred-dgs30 {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-dgs30:#1baf7a;
}
.dark .fred-dgs30 { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-dgs30:#199e70; }
.fred-dgs30 svg { width:100%; height:auto; display:block; }
.fred-dgs30 text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-dgs30 .title { fill: var(--ink); font-weight:600; }
.fred-dgs30 .grid { stroke: var(--grid); stroke-width:1; }
.fred-dgs30 .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-dgs30">
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="미국 30년물 국채금리, 최근 5년 일간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 30년물 국채금리 (상수만기) (최근 5년 일간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-09-15 · 단위: % · 출처: FRED DGS30</text>
<line x1="60" y1="523.0" x2="1052" y2="523.0" class="grid"/>
<text x="52" y="527.0" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="395.5" x2="1052" y2="395.5" class="grid"/>
<text x="52" y="399.5" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="268.1" x2="1052" y2="268.1" class="grid"/>
<text x="52" y="272.1" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="140.7" x2="1052" y2="140.7" class="grid"/>
<text x="52" y="144.7" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
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
<polyline points="60.0,533.2 60.5,535.7 61.1,530.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="63.2,524.3 63.8,529.3 64.3,535.7 64.9,530.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="66.5,534.4 67.0,542.1 67.5,539.5 68.1,538.3 68.6,534.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="70.2,542.1 70.8,540.8 71.3,543.4 71.9,533.2 72.4,524.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="74.0,524.3 74.6,514.1 75.1,511.5 75.6,512.8 76.2,517.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="77.8,516.6 78.3,510.2 78.9,512.8 79.4,506.4 79.9,502.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="82.1,510.2 82.6,516.6 83.2,520.4 83.7,516.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="85.3,521.7 85.9,511.5 86.4,507.7 87.0,506.4 87.5,512.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="89.1,511.5 89.7,516.6 90.2,529.3 90.7,528.1 91.3,531.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="92.9,525.5 93.4,528.1 94.0,523.0 94.5,528.1 95.0,539.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="96.7,537.0 97.2,544.6 97.7,533.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="98.8" cy="529.3" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="100.4,521.7 101.0,520.4 101.5,523.0 102.1,526.8 102.6,534.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="104.2,525.5 104.7,520.4 105.3,528.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="106.4" cy="544.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="108.0,539.5 108.5,551.0 109.1,552.3 109.6,553.6 110.1,562.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="111.8,554.8 112.3,548.5 112.8,539.5 113.4,539.5 113.9,538.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="115.5,547.2 116.1,545.9 116.6,540.8 117.1,539.5 117.7,545.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="119.3,542.1 119.8,537.0 120.4,540.8 120.9,534.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="123.1,538.3 123.6,535.7 124.2,528.1 124.7,531.9 125.2,535.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="126.9,521.7 127.4,514.1 127.9,511.5 128.5,511.5 129.0,509.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="130.6,509.0 131.2,512.8 131.7,512.8 132.2,516.6 132.8,507.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="134.9,500.0 135.5,505.1 136.0,505.1 136.6,514.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="138.2,510.2 138.7,507.7 139.3,502.6 139.8,511.5 140.3,514.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="141.9,509.0 142.5,507.7 143.0,509.0 143.6,505.1 144.1,493.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="145.7,494.9 146.3,491.1 146.8,491.1 147.3,484.7 147.9,492.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="149.5,486.0 150.0,475.8 150.6,479.6 151.1,483.5 151.7,492.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="153.8,492.4 154.3,486.0 154.9,487.3 155.4,486.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="157.0,501.3 157.6,509.0 158.1,492.4 158.7,492.4 159.2,502.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="160.8,498.8 161.4,492.4 161.9,486.0 162.4,474.6 163.0,477.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="164.6,463.1 165.1,460.5 165.7,464.4 166.2,459.3 166.7,469.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="168.4,452.9 168.9,446.5 169.4,456.7 170.0,458.0 170.5,446.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="172.1,450.3 172.7,455.4 173.2,461.8 173.8,466.9 174.3,466.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="175.9,461.8 176.5,450.3 177.0,442.7 177.5,435.0 178.1,426.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="179.7,415.9 180.2,418.5 180.8,419.8 181.3,405.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="183.5,401.9 184.0,394.3 184.5,408.3 185.1,403.2 185.6,401.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="187.2,410.8 187.8,413.4 188.3,407.0 188.9,405.7 189.4,400.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="191.0,386.6 191.5,391.7 192.1,394.3 192.6,376.4 193.2,366.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="194.8,371.3 195.3,380.2 195.9,389.2 196.4,395.5 196.9,382.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="198.6,384.1 199.1,373.9 199.6,386.6 200.2,389.2 200.7,396.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="202.3,385.3 202.9,398.1 203.4,399.4 203.9,396.8 204.5,399.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="206.6,386.6 207.2,384.1 207.7,384.1 208.3,381.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="209.9,371.3 210.4,379.0 211.0,372.6 211.5,372.6 212.0,370.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="213.7,342.0 214.2,338.2 214.7,345.8 215.3,350.9 215.8,357.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="218.0,345.8 218.5,363.7 219.0,368.8 219.6,362.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="221.2,356.0 221.7,357.3 222.3,367.5 222.8,377.7 223.4,381.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="225.5,389.2 226.1,377.7 226.6,370.1 227.1,361.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="228.7,372.6 229.3,379.0 229.8,385.3 230.4,381.5 230.9,382.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="232.5,377.7 233.1,373.9 233.6,373.9 234.1,385.3 234.7,395.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="236.3,390.4 236.8,391.7 237.4,391.7 237.9,393.0 238.5,395.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="240.1,405.7 240.6,395.5 241.1,400.6 241.7,399.4 242.2,387.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="243.8,395.5 244.4,394.3 244.9,390.4 245.5,376.4 246.0,380.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="247.6,382.8 248.2,381.5 248.7,376.4 249.2,377.7 249.8,367.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="251.4,365.0 251.9,362.4 252.5,354.8 253.0,363.7 253.5,368.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="255.2,363.7 255.7,366.2 256.2,361.1 256.8,348.4 257.3,350.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="259.5,333.1 260.0,342.0 260.6,338.2 261.1,335.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="262.7,328.0 263.3,330.5 263.8,335.6 264.3,334.4 264.9,329.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="266.5,329.3 267.0,320.4 267.6,331.8 268.1,312.7 268.6,317.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="270.3,303.8 270.8,284.7 271.3,306.3 271.9,305.1 272.4,294.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="274.0,302.5 274.6,306.3 275.1,296.1 275.7,292.3 276.2,285.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="278.3,278.3 278.9,280.8 279.4,271.9 280.0,269.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="281.6,263.0 282.1,263.0 282.7,249.0 283.2,237.5 283.7,226.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="285.4,217.1 285.9,235.0 286.4,243.9 287.0,252.8 287.5,249.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="289.1,240.1 289.7,250.3 290.2,249.0 290.7,245.2 291.3,233.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="292.9,224.8 293.4,232.4 294.0,228.6 294.5,264.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="296.7,259.2 297.2,270.7 297.8,287.2 298.3,282.1 298.8,278.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="300.5,279.6 301.0,289.8 301.5,301.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="302.6" cy="301.2" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="304.2,301.2 304.8,292.3 305.3,293.6 305.8,314.0 306.4,324.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="308.0,316.5 308.5,329.3 309.1,342.0 309.6,339.5 310.2,324.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="311.8,322.9 312.3,328.0 312.9,329.3 313.4,334.4 313.9,328.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="315.5,316.5 316.1,301.2 316.6,301.2 317.2,302.5 317.7,291.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="319.9,277.0 320.4,270.7 320.9,278.3 321.5,271.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="323.6,283.4 324.2,292.3 324.7,296.1 325.3,310.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="326.9,311.4 327.4,301.2 327.9,310.2 328.5,324.2 329.0,317.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="331.2,314.0 331.7,326.7 332.3,322.9 332.8,311.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="334.4,307.6 335.0,316.5 335.5,316.5 336.0,316.5 336.6,314.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="338.2,311.4 338.7,312.7 339.3,325.5 339.8,325.5 340.3,315.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="342.0,310.2 342.5,303.8 343.0,306.3 343.6,300.0 344.1,289.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="345.7,294.9 346.3,292.3 346.8,287.2 347.4,278.3 347.9,283.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="350.1,270.7 350.6,275.8 351.1,283.4 351.7,277.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="353.3,277.0 353.8,277.0 354.4,271.9 354.9,264.3 355.4,280.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="357.1,278.3 357.6,283.4 358.1,283.4 358.7,283.4 359.2,306.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="360.8,306.3 361.4,297.4 361.9,306.3 362.5,305.1 363.0,319.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="364.6,312.7 365.1,302.5 365.7,308.9 366.2,311.4 366.8,314.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="368.4,297.4 368.9,297.4 369.5,296.1 370.0,301.2 370.5,310.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="372.2,314.0 372.7,319.1 373.2,324.2 373.8,326.7 374.3,317.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="375.9,316.5 376.5,316.5 377.0,314.0 377.5,307.6 378.1,301.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="379.7,292.3 380.2,294.9 380.8,294.9 381.3,300.0 381.9,296.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="383.5,302.5 384.0,312.7 384.6,306.3 385.1,298.7 385.6,310.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="387.3,288.5 387.8,303.8 388.3,306.3 388.9,302.5 389.4,298.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="391.0,288.5 391.6,287.2 392.1,293.6 392.6,302.5 393.2,296.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="394.8,288.5 395.3,284.7 395.9,283.4 396.4,279.6 397.0,274.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="398.6,271.9 399.1,273.2 399.7,271.9 400.2,266.8 400.7,273.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="402.9,280.8 403.4,287.2 404.0,288.5 404.5,283.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="406.1,282.1 406.7,284.7 407.2,274.5 407.7,282.1 408.3,282.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="409.9,284.7 410.4,275.8 411.0,280.8 411.5,287.2 412.1,285.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="414.2,289.8 414.7,292.3 415.3,283.4 415.8,291.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="417.4,289.8 418.0,288.5 418.5,292.3 419.1,278.3 419.6,287.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="421.2" cy="284.7" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="422.3,274.5 422.8,266.8 423.4,261.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="425.0,261.7 425.5,264.3 426.1,273.2 426.6,280.8 427.1,277.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="428.8,275.8 429.3,279.6 429.8,288.5 430.4,279.6 430.9,279.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="432.5,278.3 433.1,274.5 433.6,275.8 434.2,260.5 434.7,264.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="436.3,265.6 436.9,254.1 437.4,246.4 437.9,227.3 438.5,241.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="440.1,233.7 440.6,242.6 441.2,245.2 441.7,237.5 442.2,233.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="443.9,231.1 444.4,227.3 444.9,219.7 445.5,215.9 446.0,219.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="447.6,210.8 448.2,214.6 448.7,233.7 449.3,229.9 449.8,229.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="451.4,231.1 451.9,238.8 452.5,238.8 453.0,242.6 453.6,231.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="455.7,219.7 456.3,221.0 456.8,222.2 457.3,226.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="459.0,221.0 459.5,223.5 460.0,224.8 460.6,218.4 461.1,214.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="462.7,217.1 463.3,213.3 463.8,217.1 464.3,196.7 464.9,200.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="466.5,182.7 467.0,178.9 467.6,175.1 468.1,177.6 468.7,175.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="470.3,164.9 470.8,147.0 471.4,157.2 471.9,154.7 472.4,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="474.6,159.8 475.1,175.1 475.7,158.5 476.2,168.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="477.8,157.2 478.4,148.3 478.9,140.7 479.4,126.7 480.0,129.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="481.6,139.4 482.1,145.8 482.7,129.2 483.2,139.4 483.8,136.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="485.4,135.6 485.9,135.6 486.5,145.8 487.0,163.6 487.5,170.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="489.1,161.1 489.7,172.5 490.2,186.5 490.8,170.0 491.3,175.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="492.9,172.5 493.5,190.4 494.0,181.4 494.5,187.8 495.1,192.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="496.7,195.5 497.2,195.5 497.8,198.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="498.9" cy="191.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="500.5,200.6 501.0,201.8 501.5,212.0 502.1,199.3 502.6,217.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="504.2,213.3 504.8,229.9 505.3,240.1 505.9,236.2 506.4,228.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="508.0,227.3 508.6,229.9 509.1,243.9 509.6,264.3 510.2,268.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="511.8,261.7 512.3,264.3 512.9,270.7 513.4,264.3 513.9,261.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="516.1,263.0 516.6,274.5 517.2,270.7 517.7,264.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="519.9,257.9 520.4,261.7 521.0,251.5 521.5,241.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="523.1,246.4 523.7,245.2 524.2,242.6 524.7,245.2 525.3,242.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="527.4,229.9 528.0,228.6 528.5,221.0 529.0,222.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="530.7,227.3 531.2,219.7 531.7,215.9 532.3,219.7 532.8,219.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="534.4,228.6 535.0,232.4 535.5,240.1 536.1,255.4 536.6,240.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="538.2,223.5 538.7,231.1 539.3,228.6 539.8,222.2 540.4,221.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="542.0,221.0 542.5,209.5 543.1,210.8 543.6,214.6 544.1,210.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="546.3,212.0 546.8,205.7 547.4,208.2 547.9,221.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="549.5,217.1 550.1,212.0 550.6,217.1 551.1,219.7 551.7,226.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="553.3,222.2 553.8,233.7 554.4,237.5 554.9,236.2 555.5,235.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="557.1,235.0 557.6,228.6 558.2,223.5 558.7,212.0 559.2,213.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="560.9,209.5 561.4,212.0 561.9,210.8 562.5,212.0 563.0,218.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="564.6,214.6 565.2,217.1 565.7,222.2 566.2,224.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="568.4,208.2 568.9,203.1 569.5,203.1 570.0,208.2 570.6,199.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="572.2,198.0 572.7,204.4 573.3,186.5 573.8,185.3 574.3,190.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="575.9,173.8 576.5,170.0 577.0,177.6 577.6,173.8 578.1,176.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="579.7,176.4 580.3,175.1 580.8,168.7 581.3,163.6 581.9,168.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="583.5,172.5 584.0,167.4 584.6,173.8 585.1,176.4 585.7,184.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="587.3,186.5 587.8,190.4 588.3,186.5 588.9,191.6 589.4,186.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="591.0,187.8 591.6,192.9 592.1,201.8 592.7,201.8 593.2,196.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="594.8,194.2 595.4,198.0 595.9,198.0 596.4,194.2 597.0,195.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="599.1,184.0 599.7,173.8 600.2,180.2 600.7,185.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="602.4,198.0 602.9,206.9 603.4,212.0 604.0,213.3 604.5,198.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="606.1,192.9 606.7,200.6 607.2,208.2 607.8,217.1 608.3,224.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="609.9,217.1 610.5,222.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="611.5,218.4 612.1,218.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="613.7,219.7 614.2,222.2 614.8,210.8 615.3,213.3 615.8,203.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="617.5,186.5 618.0,191.6 618.5,200.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="619.6" cy="208.2" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="621.2,209.5 621.8,205.7 622.3,208.2 622.9,215.9 623.4,218.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="625.0,209.5 625.5,219.7 626.1,221.0 626.6,215.9 627.2,210.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="628.8,206.9 629.3,206.9 629.9,199.3 630.4,204.4 630.9,210.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="632.6,214.6 633.1,217.1 633.6,223.5 634.2,233.7 634.7,254.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="636.3,260.5 636.9,245.2 637.4,235.0 637.9,232.4 638.5,238.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="640.1,243.9 640.6,247.7 641.2,252.8 641.7,245.2 642.3,249.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="643.9,254.1 644.4,259.2 645.0,260.5 645.5,251.5 646.0,255.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="647.7,254.1 648.2,251.5 648.7,251.5 649.3,249.0 649.8,242.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="652.0,251.5 652.5,260.5 653.0,265.6 653.6,264.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="655.2,268.1 655.7,271.9 656.3,273.2 656.8,268.1 657.4,270.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="659.0,275.8 659.5,273.2 660.1,264.3 660.6,260.5 661.1,259.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="662.7,256.6 663.3,256.6 663.8,250.3 664.4,252.8 664.9,255.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="666.5,250.3 667.1,257.9 667.6,250.3 668.1,245.2 668.7,235.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="670.3,229.9 670.8,227.3 671.4,224.8 671.9,219.7 672.5,218.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="674.6,227.3 675.1,229.9 675.7,218.4 676.2,219.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="677.8,205.7 678.4,205.7 678.9,203.1 679.5,208.2 680.0,203.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="681.6,200.6 682.2,201.8 682.7,205.7 683.2,208.2 683.8,195.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="685.4,204.4 685.9,212.0 686.5,191.6 687.0,201.8 687.5,208.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="689.7,194.2 690.2,187.8 690.8,194.2 691.3,191.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="692.9,190.4 693.5,195.5 694.0,192.9 694.6,190.4 695.1,191.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="696.7,210.8 697.3,206.9 697.8,212.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="698.9" cy="222.2" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="700.5,222.2 701.0,217.1 701.6,223.5 702.1,226.1 702.6,224.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="704.3,218.4 704.8,215.9 705.3,206.9 705.9,198.0 706.4,190.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="708.0,191.6 708.6,192.9 709.1,185.3 709.7,173.8 710.2,176.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="711.8,168.7 712.3,171.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="713.4,171.3 714.0,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="715.6,170.0 716.1,168.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="717.2,167.4 717.7,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="719.4,159.8 719.9,152.1 720.4,152.1 721.0,150.9 721.5,145.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="723.1,144.5 723.7,143.2 724.2,156.0 724.7,161.1 725.3,161.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="727.4,166.2 728.0,163.6 728.5,157.2 729.1,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="730.7,171.3 731.2,168.7 731.8,167.4 732.3,171.3 732.8,162.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="734.5,170.0 735.0,172.5 735.5,186.5 736.1,185.3 736.6,180.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="738.2,177.6 738.8,172.5 739.3,162.3 739.8,176.4 740.4,180.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="742.5,170.0 743.1,171.3 743.6,173.8 744.2,182.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="745.8,184.0 746.3,198.0 746.9,203.1 747.4,196.7 747.9,203.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="749.5,210.8 750.1,200.6 750.6,195.5 751.2,194.2 751.7,189.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="753.3,199.3 753.9,192.9 754.4,187.8 754.9,192.9 755.5,189.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="757.1,191.6 757.6,194.2 758.2,196.7 758.7,198.0 759.3,192.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="760.9,184.0 761.4,185.3 761.9,180.2 762.5,175.1 763.0,186.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="764.6,192.9 765.2,201.8 765.7,199.3 766.3,205.7 766.8,215.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="768.4,194.2 769.0,177.6 769.5,176.4 770.0,158.5 770.6,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="772.2,166.2 772.7,167.4 773.3,173.8 773.8,166.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="776.0,152.1 776.5,156.0 777.0,162.3 777.6,170.0 778.1,173.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="779.7,180.2 780.3,186.5 780.8,184.0 781.4,173.8 781.9,167.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="783.5,162.3 784.1,164.9 784.6,170.0 785.1,162.3 785.7,162.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="787.3,154.7 787.8,148.3 788.4,144.5 788.9,152.1 789.4,154.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="791.1,150.9 791.6,145.8 792.1,130.5 792.7,134.3 793.2,135.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="795.4,148.3 795.9,144.5 796.5,150.9 797.0,150.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="798.6,141.9 799.1,143.2 799.7,154.7 800.2,156.0 800.8,144.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="802.4,147.0 802.9,149.6 803.5,152.1 804.0,161.1 804.5,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="806.2,145.8 806.7,156.0 807.2,156.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="808.3" cy="154.7" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="809.9,157.2 810.5,162.3 811.0,162.3 811.5,164.9 812.1,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="813.7,168.7 814.2,168.7 814.8,163.6 815.3,158.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="817.5,150.9 818.0,148.3 818.6,157.2 819.1,158.5 819.6,145.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="821.3,144.5 821.8,139.4 822.3,139.4 822.9,139.4 823.4,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="825.0,148.3 825.6,153.4 826.1,147.0 826.6,145.8 827.2,150.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="828.8,145.8 829.3,158.5 829.9,154.7 830.4,154.7 831.0,164.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="832.6,166.2 833.1,168.7 833.7,164.9 834.2,164.9 834.7,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="836.3,161.1 836.9,156.0 837.4,162.3 838.0,156.0 838.5,150.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="840.1,148.3 840.7,153.4 841.2,154.7 841.7,150.9 842.3,156.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="843.9,154.7 844.4,153.4 845.0,152.1 845.5,156.0 846.1,150.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="848.2,144.5 848.7,153.4 849.3,158.5 849.8,168.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="851.4,180.2 852.0,176.4 852.5,180.2 853.1,185.3 853.6,181.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="855.2,184.0 855.8,185.3 856.3,184.0 856.8,176.4 857.4,172.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="859.0,170.0 859.5,175.1 860.1,171.3 860.6,172.5 861.1,170.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="862.8,177.6 863.3,175.1 863.8,176.4 864.4,180.2 864.9,177.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="866.5,171.3 867.1,175.1 867.6,176.4 868.2,176.4 868.7,187.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="870.9,189.1 871.4,186.5 871.9,194.2 872.5,191.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="874.1,194.2 874.6,198.0 875.2,199.3 875.7,194.2 876.2,192.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="877.9,195.5 878.4,198.0 878.9,190.4 879.5,185.3 880.0,182.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="881.6,180.2 882.2,182.7 882.7,173.8 883.3,180.2 883.8,178.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="885.4" cy="177.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="886.5,182.7 887.0,178.9 887.6,173.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="889.2,175.1 889.7,173.8 890.3,172.5 890.8,175.1 891.3,177.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="893.0,181.4 893.5,182.7 894.0,186.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="895.1" cy="182.7" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="896.7,173.8 897.3,173.8 897.8,175.1 898.3,171.3 898.9,167.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="900.5,164.9 901.0,166.2 901.6,168.7 902.1,167.4 902.7,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="904.3,161.1 904.8,163.6 905.4,162.3 905.9,166.2 906.4,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="908.1,161.1 908.6,162.3 909.1,167.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="910.2" cy="164.9" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="911.8,166.2 912.4,164.9 912.9,161.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="914.0" cy="158.5" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="915.6,159.8 916.1,158.5 916.7,163.6 917.2,159.8 917.8,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="919.4,162.3 919.9,162.3 920.5,167.4 921.0,167.4 921.5,162.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="923.7,152.1 924.2,157.2 924.8,161.1 925.3,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="926.9,166.2 927.5,162.3 928.0,159.8 928.5,159.8 929.1,157.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="930.7,153.4 931.2,153.4 931.8,152.1 932.3,159.8 932.9,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="934.5,159.8 935.0,168.7 935.5,163.6 936.1,176.4 936.6,180.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="938.8,181.4 939.3,177.6 939.9,178.9 940.4,176.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="942.0,178.9 942.6,178.9 943.1,178.9 943.6,182.7 944.2,186.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="945.8,178.9 946.3,178.9 946.9,176.4 947.4,173.8 947.9,170.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="949.6,176.4 950.1,168.7 950.6,158.5 951.2,156.0 951.7,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="953.3,158.5 953.9,159.8 954.4,156.0 955.0,162.3 955.5,145.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="957.1,152.1 957.7,148.3 958.2,154.7 958.7,149.6 959.3,143.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="960.9,152.1 961.4,156.0 962.0,152.1 962.5,156.0 963.0,152.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="964.7,154.7 965.2,153.4 965.7,154.7 966.3,153.4 966.8,152.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="968.4,153.4 969.0,157.2 969.5,154.7 970.1,149.6 970.6,156.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="972.2,156.0 972.7,154.7 973.3,153.4 973.8,150.9 974.4,152.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="976.0,148.3 976.5,148.3 977.1,143.2 977.6,143.2 978.1,144.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="979.8,138.1 980.3,143.2 980.8,148.3 981.4,144.5 981.9,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="983.5,143.2 984.1,136.8 984.6,136.8 985.1,138.1 985.7,125.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="987.3,122.8 987.8,117.7 988.4,126.7 988.9,127.9 989.5,131.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="991.6,136.8 992.2,139.4 992.7,143.2 993.2,141.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="994.9,141.9 995.4,144.5 995.9,141.9 996.5,144.5 997.0,139.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="998.6,136.8 999.2,139.4 999.7,136.8 1000.2,147.0 1000.8,144.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1002.4,144.5 1002.9,149.6 1003.5,149.6 1004.0,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1006.2,147.0 1006.7,148.3 1007.3,158.5 1007.8,158.5 1008.3,157.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1009.9,158.5 1010.5,152.1 1011.0,144.5 1011.6,143.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1013.7,141.9 1014.3,134.3 1014.8,133.0 1015.3,134.3 1015.9,133.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1017.5,127.9 1018.0,130.5 1018.6,130.5 1019.1,129.2 1019.7,133.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1021.3,126.7 1021.8,124.1 1022.3,121.6 1022.9,119.0 1023.4,120.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1025.0,125.4 1025.6,129.2 1026.1,115.2 1026.7,113.9 1027.2,106.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1028.8,111.4 1029.4,117.7 1029.9,119.0 1030.4,112.6 1031.0,116.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1032.6,108.8 1033.1,110.1 1033.7,110.1 1034.2,113.9 1034.7,108.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1036.4,101.2 1036.9,105.0 1037.4,116.5 1038.0,111.4 1038.5,106.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1040.1,111.4 1040.7,119.0 1041.2,117.7 1041.8,116.5 1042.3,112.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1043.9,108.8 1044.5,106.3 1045.0,106.3 1045.5,108.8 1046.1,110.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1048.2,108.8 1048.8,105.0 1049.3,93.5 1049.8,96.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1051.5,97.3 1052.0,94.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<text x="1058" y="98.8" font-size="11.5" font-weight="700" fill="var(--s-dgs30)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 30년물 국채금리 5.36%</text>
</svg>
</div>

---

## 2. 해석

- **상승**: 장기 재정건전성 우려나 장기 인플레이션 기대가 커졌다는 신호로 흔히 해석한다 — 단기물과 달리 당장의 연준 결정보다 먼 미래에 대한 기대에 더 민감하다.
- **하락**: 장기 성장·인플레이션 기대가 둔화되거나 안전자산 수요가 커졌다는 신호로 흔히 해석한다.
- **왜 이런 신호로 읽히나**: 30년물 수익률은 "앞으로 30년간 평균 단기금리가 어떻게 움직일지에 대한 기대"보다 **기간 프리미엄**(만기가 길어질수록 투자자가 추가로 요구하는 보상) 비중이 더 크다. 그래서 당장의 통화정책보다는 장기 국채 발행량(재정 전망), 장기 성장·인플레이션 기대에 더 민감하게 움직인다. 연기금·보험사처럼 오랫동안 갚아야 할 부채를 가진 기관들이 구조적으로 사들이는 수요도 가격에 영향을 준다.
- **밸류에이션 할인율의 표준 근거로는 쓰지 않는다** — 표준은 [10년물](./treasury_10y.md)이다. 이 문서는 수익률곡선의 모양을 보기 위한 보조 자료다.

---

*작성일: 2026-09-18*
