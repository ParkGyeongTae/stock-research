# 미국 30년물 국채금리

::: info
만기 30년 미 국채의 상수만기 수익률이다(FRED `DGS30`). [2년물](./treasury_2y.md)·[10년물](./treasury_10y.md)과 함께 보면 수익률곡선에서 가장 만기가 긴 구간까지 채워서 볼 수 있다.
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
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-09-16 · 단위: % · 출처: FRED DGS30</text>
<line x1="60" y1="523.0" x2="1052" y2="523.0" class="grid"/>
<text x="52" y="527.0" font-size="11" text-anchor="end" fill="var(--muted)">2.00</text>
<line x1="60" y1="395.5" x2="1052" y2="395.5" class="grid"/>
<text x="52" y="399.5" font-size="11" text-anchor="end" fill="var(--muted)">3.00</text>
<line x1="60" y1="268.1" x2="1052" y2="268.1" class="grid"/>
<text x="52" y="272.1" font-size="11" text-anchor="end" fill="var(--muted)">4.00</text>
<line x1="60" y1="140.7" x2="1052" y2="140.7" class="grid"/>
<text x="52" y="144.7" font-size="11" text-anchor="end" fill="var(--muted)">5.00</text>
<line x1="125.7" y1="56" x2="125.7" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="125.7" y1="600" x2="125.7" y2="605" class="axis"/>
<text x="125.7" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="322.4" y1="56" x2="322.4" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="322.4" y1="600" x2="322.4" y2="605" class="axis"/>
<text x="322.4" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="519.1" y1="56" x2="519.1" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="519.1" y1="600" x2="519.1" y2="605" class="axis"/>
<text x="519.1" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="716.3" y1="56" x2="716.3" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="716.3" y1="600" x2="716.3" y2="605" class="axis"/>
<text x="716.3" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="913.0" y1="56" x2="913.0" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="913.0" y1="600" x2="913.0" y2="605" class="axis"/>
<text x="913.0" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="600" x2="1052" y2="600" class="axis"/>
<line x1="60" y1="56" x2="60" y2="600" class="axis"/>
<polyline points="60.0,533.2 60.5,535.7 61.1,530.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="63.2,524.3 63.8,529.3 64.3,535.7 64.8,530.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="66.5,534.4 67.0,542.1 67.5,539.5 68.1,538.3 68.6,534.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="70.2,542.1 70.8,540.8 71.3,543.4 71.9,533.2 72.4,524.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="74.0,524.3 74.5,514.1 75.1,511.5 75.6,512.8 76.2,517.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="77.8,516.6 78.3,510.2 78.9,512.8 79.4,506.4 79.9,502.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="82.1,510.2 82.6,516.6 83.2,520.4 83.7,516.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="85.3,521.7 85.9,511.5 86.4,507.7 86.9,506.4 87.5,512.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="89.1,511.5 89.6,516.6 90.2,529.3 90.7,528.1 91.3,531.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="92.9,525.5 93.4,528.1 93.9,523.0 94.5,528.1 95.0,539.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="96.6,537.0 97.2,544.6 97.7,533.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="98.8" cy="529.3" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="100.4,521.7 101.0,520.4 101.5,523.0 102.0,526.8 102.6,534.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="104.2,525.5 104.7,520.4 105.3,528.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="106.3" cy="544.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="108.0,539.5 108.5,551.0 109.0,552.3 109.6,553.6 110.1,562.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="111.7,554.8 112.3,548.5 112.8,539.5 113.3,539.5 113.9,538.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="115.5,547.2 116.0,545.9 116.6,540.8 117.1,539.5 117.7,545.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="119.3,542.1 119.8,537.0 120.3,540.8 120.9,534.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="123.0,538.3 123.6,535.7 124.1,528.1 124.7,531.9 125.2,535.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="126.8,521.7 127.4,514.1 127.9,511.5 128.4,511.5 129.0,509.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="130.6,509.0 131.1,512.8 131.7,512.8 132.2,516.6 132.7,507.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="134.9,500.0 135.4,505.1 136.0,505.1 136.5,514.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="138.1,510.2 138.7,507.7 139.2,502.6 139.7,511.5 140.3,514.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="141.9,509.0 142.4,507.7 143.0,509.0 143.5,505.1 144.1,493.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="145.7,494.9 146.2,491.1 146.8,491.1 147.3,484.7 147.8,492.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="149.4,486.0 150.0,475.8 150.5,479.6 151.1,483.5 151.6,492.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="153.8,492.4 154.3,486.0 154.8,487.3 155.4,486.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="157.0,501.3 157.5,509.0 158.1,492.4 158.6,492.4 159.1,502.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="160.8,498.8 161.3,492.4 161.8,486.0 162.4,474.6 162.9,477.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="164.5,463.1 165.1,460.5 165.6,464.4 166.2,459.3 166.7,469.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="168.3,452.9 168.8,446.5 169.4,456.7 169.9,458.0 170.5,446.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="172.1,450.3 172.6,455.4 173.2,461.8 173.7,466.9 174.2,466.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="175.9,461.8 176.4,450.3 176.9,442.7 177.5,435.0 178.0,426.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="179.6,415.9 180.2,418.5 180.7,419.8 181.2,405.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="183.4,401.9 183.9,394.3 184.5,408.3 185.0,403.2 185.5,401.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="187.2,410.8 187.7,413.4 188.2,407.0 188.8,405.7 189.3,400.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="190.9,386.6 191.5,391.7 192.0,394.3 192.6,376.4 193.1,366.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="194.7,371.3 195.2,380.2 195.8,389.2 196.3,395.5 196.9,382.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="198.5,384.1 199.0,373.9 199.6,386.6 200.1,389.2 200.6,396.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="202.3,385.3 202.8,398.1 203.3,399.4 203.9,396.8 204.4,399.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="206.6,386.6 207.1,384.1 207.6,384.1 208.2,381.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="209.8,371.3 210.3,379.0 210.9,372.6 211.4,372.6 212.0,370.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="213.6,342.0 214.1,338.2 214.6,345.8 215.2,350.9 215.7,357.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="217.9,345.8 218.4,363.7 219.0,368.8 219.5,362.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="221.1,356.0 221.7,357.3 222.2,367.5 222.7,377.7 223.3,381.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="225.4,389.2 226.0,377.7 226.5,370.1 227.0,361.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="228.7,372.6 229.2,379.0 229.7,385.3 230.3,381.5 230.8,382.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="232.4,377.7 233.0,373.9 233.5,373.9 234.0,385.3 234.6,395.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="236.2,390.4 236.7,391.7 237.3,391.7 237.8,393.0 238.4,395.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="240.0,405.7 240.5,395.5 241.0,400.6 241.6,399.4 242.1,387.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="243.7,395.5 244.3,394.3 244.8,390.4 245.4,376.4 245.9,380.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="247.5,382.8 248.1,381.5 248.6,376.4 249.1,377.7 249.7,367.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="251.3,365.0 251.8,362.4 252.4,354.8 252.9,363.7 253.4,368.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="255.1,363.7 255.6,366.2 256.1,361.1 256.7,348.4 257.2,350.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="259.4,333.1 259.9,342.0 260.4,338.2 261.0,335.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="262.6,328.0 263.1,330.5 263.7,335.6 264.2,334.4 264.8,329.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="266.4,329.3 266.9,320.4 267.5,331.8 268.0,312.7 268.5,317.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="270.1,303.8 270.7,284.7 271.2,306.3 271.8,305.1 272.3,294.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="273.9,302.5 274.5,306.3 275.0,296.1 275.5,292.3 276.1,285.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="278.2,278.3 278.8,280.8 279.3,271.9 279.8,269.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="281.5,263.0 282.0,263.0 282.5,249.0 283.1,237.5 283.6,226.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="285.2,217.1 285.8,235.0 286.3,243.9 286.9,252.8 287.4,249.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="289.0,240.1 289.5,250.3 290.1,249.0 290.6,245.2 291.2,233.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="292.8,224.8 293.3,232.4 293.9,228.6 294.4,264.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="296.5,259.2 297.1,270.7 297.6,287.2 298.2,282.1 298.7,278.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="300.3,279.6 300.9,289.8 301.4,301.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="302.5" cy="301.2" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="304.1,301.2 304.6,292.3 305.2,293.6 305.7,314.0 306.2,324.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="307.9,316.5 308.4,329.3 308.9,342.0 309.5,339.5 310.0,324.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="311.6,322.9 312.2,328.0 312.7,329.3 313.3,334.4 313.8,328.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="315.4,316.5 315.9,301.2 316.5,301.2 317.0,302.5 317.6,291.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="319.7,277.0 320.3,270.7 320.8,278.3 321.3,271.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="323.5,283.4 324.0,292.3 324.6,296.1 325.1,310.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="326.7,311.4 327.3,301.2 327.8,310.2 328.3,324.2 328.9,317.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="331.0,314.0 331.6,326.7 332.1,322.9 332.7,311.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="334.3,307.6 334.8,316.5 335.3,316.5 335.9,316.5 336.4,314.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="338.0,311.4 338.6,312.7 339.1,325.5 339.7,325.5 340.2,315.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="341.8,310.2 342.4,303.8 342.9,306.3 343.4,300.0 344.0,289.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="345.6,294.9 346.1,292.3 346.7,287.2 347.2,278.3 347.7,283.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="349.9,270.7 350.4,275.8 351.0,283.4 351.5,277.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="353.1,277.0 353.7,277.0 354.2,271.9 354.7,264.3 355.3,280.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="356.9,278.3 357.4,283.4 358.0,283.4 358.5,283.4 359.1,306.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="360.7,306.3 361.2,297.4 361.7,306.3 362.3,305.1 362.8,319.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="364.4,312.7 365.0,302.5 365.5,308.9 366.1,311.4 366.6,314.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="368.2,297.4 368.8,297.4 369.3,296.1 369.8,301.2 370.4,310.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="372.0,314.0 372.5,319.1 373.1,324.2 373.6,326.7 374.1,317.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="375.8,316.5 376.3,316.5 376.8,314.0 377.4,307.6 377.9,301.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="379.5,292.3 380.1,294.9 380.6,294.9 381.1,300.0 381.7,296.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="383.3,302.5 383.8,312.7 384.4,306.3 384.9,298.7 385.5,310.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="387.1,288.5 387.6,303.8 388.2,306.3 388.7,302.5 389.2,298.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="390.8,288.5 391.4,287.2 391.9,293.6 392.5,302.5 393.0,296.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="394.6,288.5 395.2,284.7 395.7,283.4 396.2,279.6 396.8,274.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="398.4,271.9 398.9,273.2 399.5,271.9 400.0,266.8 400.5,273.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="402.7,280.8 403.2,287.2 403.8,288.5 404.3,283.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="405.9,282.1 406.5,284.7 407.0,274.5 407.6,282.1 408.1,282.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="409.7,284.7 410.2,275.8 410.8,280.8 411.3,287.2 411.9,285.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="414.0,289.8 414.6,292.3 415.1,283.4 415.6,291.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="417.2,289.8 417.8,288.5 418.3,292.3 418.9,278.3 419.4,287.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="421.0" cy="284.7" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="422.1,274.5 422.6,266.8 423.2,261.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="424.8,261.7 425.3,264.3 425.9,273.2 426.4,280.8 426.9,277.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="428.6,275.8 429.1,279.6 429.6,288.5 430.2,279.6 430.7,279.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="432.3,278.3 432.9,274.5 433.4,275.8 434.0,260.5 434.5,264.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="436.1,265.6 436.6,254.1 437.2,246.4 437.7,227.3 438.3,241.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="439.9,233.7 440.4,242.6 441.0,245.2 441.5,237.5 442.0,233.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="443.7,231.1 444.2,227.3 444.7,219.7 445.3,215.9 445.8,219.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="447.4,210.8 448.0,214.6 448.5,233.7 449.0,229.9 449.6,229.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="451.2,231.1 451.7,238.8 452.3,238.8 452.8,242.6 453.4,231.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="455.5,219.7 456.0,221.0 456.6,222.2 457.1,226.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="458.7,221.0 459.3,223.5 459.8,224.8 460.4,218.4 460.9,214.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="462.5,217.1 463.1,213.3 463.6,217.1 464.1,196.7 464.7,200.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="466.3,182.7 466.8,178.9 467.4,175.1 467.9,177.6 468.4,175.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="470.1,164.9 470.6,147.0 471.1,157.2 471.7,154.7 472.2,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="474.4,159.8 474.9,175.1 475.4,158.5 476.0,168.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="477.6,157.2 478.1,148.3 478.7,140.7 479.2,126.7 479.8,129.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="481.4,139.4 481.9,145.8 482.4,129.2 483.0,139.4 483.5,136.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="485.1,135.6 485.7,135.6 486.2,145.8 486.8,163.6 487.3,170.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="488.9,161.1 489.5,172.5 490.0,186.5 490.5,170.0 491.1,175.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="492.7,172.5 493.2,190.4 493.8,181.4 494.3,187.8 494.8,192.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="496.5,195.5 497.0,195.5 497.5,198.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="498.6" cy="191.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="500.2,200.6 500.8,201.8 501.3,212.0 501.8,199.3 502.4,217.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="504.0,213.3 504.5,229.9 505.1,240.1 505.6,236.2 506.2,228.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="507.8,227.3 508.3,229.9 508.9,243.9 509.4,264.3 509.9,268.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="511.5,261.7 512.1,264.3 512.6,270.7 513.2,264.3 513.7,261.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="515.9,263.0 516.4,274.5 516.9,270.7 517.5,264.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="519.6,257.9 520.2,261.7 520.7,251.5 521.2,241.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="522.9,246.4 523.4,245.2 523.9,242.6 524.5,245.2 525.0,242.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="527.2,229.9 527.7,228.6 528.2,221.0 528.8,222.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="530.4,227.3 530.9,219.7 531.5,215.9 532.0,219.7 532.6,219.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="534.2,228.6 534.7,232.4 535.3,240.1 535.8,255.4 536.3,240.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="537.9,223.5 538.5,231.1 539.0,228.6 539.6,222.2 540.1,221.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="541.7,221.0 542.3,209.5 542.8,210.8 543.3,214.6 543.9,210.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="546.0,212.0 546.6,205.7 547.1,208.2 547.6,221.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="549.3,217.1 549.8,212.0 550.3,217.1 550.9,219.7 551.4,226.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="553.0,222.2 553.6,233.7 554.1,237.5 554.7,236.2 555.2,235.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="556.8,235.0 557.3,228.6 557.9,223.5 558.4,212.0 559.0,213.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="560.6,209.5 561.1,212.0 561.7,210.8 562.2,212.0 562.7,218.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="564.4,214.6 564.9,217.1 565.4,222.2 566.0,224.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="568.1,208.2 568.7,203.1 569.2,203.1 569.7,208.2 570.3,199.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="571.9,198.0 572.4,204.4 573.0,186.5 573.5,185.3 574.1,190.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="575.7,173.8 576.2,170.0 576.7,177.6 577.3,173.8 577.8,176.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="579.4,176.4 580.0,175.1 580.5,168.7 581.1,163.6 581.6,168.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="583.2,172.5 583.8,167.4 584.3,173.8 584.8,176.4 585.4,184.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="587.0,186.5 587.5,190.4 588.1,186.5 588.6,191.6 589.1,186.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="590.8,187.8 591.3,192.9 591.8,201.8 592.4,201.8 592.9,196.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="594.5,194.2 595.1,198.0 595.6,198.0 596.1,194.2 596.7,195.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="598.8,184.0 599.4,173.8 599.9,180.2 600.5,185.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="602.1,198.0 602.6,206.9 603.1,212.0 603.7,213.3 604.2,198.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="605.8,192.9 606.4,200.6 606.9,208.2 607.5,217.1 608.0,224.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="609.6,217.1 610.2,222.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="611.2,218.4 611.8,218.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="613.4,219.7 613.9,222.2 614.5,210.8 615.0,213.3 615.5,203.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="617.2,186.5 617.7,191.6 618.2,200.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="619.3" cy="208.2" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="620.9,209.5 621.5,205.7 622.0,208.2 622.5,215.9 623.1,218.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="624.7,209.5 625.2,219.7 625.8,221.0 626.3,215.9 626.9,210.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="628.5,206.9 629.0,206.9 629.6,199.3 630.1,204.4 630.6,210.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="632.2,214.6 632.8,217.1 633.3,223.5 633.9,233.7 634.4,254.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="636.0,260.5 636.6,245.2 637.1,235.0 637.6,232.4 638.2,238.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="639.8,243.9 640.3,247.7 640.9,252.8 641.4,245.2 641.9,249.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="643.6,254.1 644.1,259.2 644.6,260.5 645.2,251.5 645.7,255.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="647.3,254.1 647.9,251.5 648.4,251.5 648.9,249.0 649.5,242.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="651.6,251.5 652.2,260.5 652.7,265.6 653.3,264.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="654.9,268.1 655.4,271.9 656.0,273.2 656.5,268.1 657.0,270.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="658.6,275.8 659.2,273.2 659.7,264.3 660.3,260.5 660.8,259.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="662.4,256.6 663.0,256.6 663.5,250.3 664.0,252.8 664.6,255.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="666.2,250.3 666.7,257.9 667.3,250.3 667.8,245.2 668.3,235.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="670.0,229.9 670.5,227.3 671.0,224.8 671.6,219.7 672.1,218.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="674.3,227.3 674.8,229.9 675.4,218.4 675.9,219.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="677.5,205.7 678.0,205.7 678.6,203.1 679.1,208.2 679.7,203.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="681.3,200.6 681.8,201.8 682.4,205.7 682.9,208.2 683.4,195.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="685.1,204.4 685.6,212.0 686.1,191.6 686.7,201.8 687.2,208.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="689.4,194.2 689.9,187.8 690.4,194.2 691.0,191.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="692.6,190.4 693.1,195.5 693.7,192.9 694.2,190.4 694.8,191.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="696.4,210.8 696.9,206.9 697.4,212.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="698.5" cy="222.2" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="700.1,222.2 700.7,217.1 701.2,223.5 701.8,226.1 702.3,224.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="703.9,218.4 704.4,215.9 705.0,206.9 705.5,198.0 706.1,190.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="707.7,191.6 708.2,192.9 708.8,185.3 709.3,173.8 709.8,176.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="711.5,168.7 712.0,171.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="713.1,171.3 713.6,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="715.2,170.0 715.8,168.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="716.8,167.4 717.4,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="719.0,159.8 719.5,152.1 720.1,152.1 720.6,150.9 721.2,145.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="722.8,144.5 723.3,143.2 723.8,156.0 724.4,161.1 724.9,161.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="727.1,166.2 727.6,163.6 728.2,157.2 728.7,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="730.3,171.3 730.9,168.7 731.4,167.4 731.9,171.3 732.5,162.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="734.1,170.0 734.6,172.5 735.2,186.5 735.7,185.3 736.2,180.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="737.9,177.6 738.4,172.5 738.9,162.3 739.5,176.4 740.0,180.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="742.2,170.0 742.7,171.3 743.2,173.8 743.8,182.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="745.4,184.0 745.9,198.0 746.5,203.1 747.0,196.7 747.6,203.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="749.2,210.8 749.7,200.6 750.3,195.5 750.8,194.2 751.3,189.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="752.9,199.3 753.5,192.9 754.0,187.8 754.6,192.9 755.1,189.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="756.7,191.6 757.3,194.2 757.8,196.7 758.3,198.0 758.9,192.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="760.5,184.0 761.0,185.3 761.6,180.2 762.1,175.1 762.6,186.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="764.3,192.9 764.8,201.8 765.3,199.3 765.9,205.7 766.4,215.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="768.0,194.2 768.6,177.6 769.1,176.4 769.6,158.5 770.2,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="771.8,166.2 772.3,167.4 772.9,173.8 773.4,166.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="775.6,152.1 776.1,156.0 776.7,162.3 777.2,170.0 777.7,173.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="779.3,180.2 779.9,186.5 780.4,184.0 781.0,173.8 781.5,167.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="783.1,162.3 783.7,164.9 784.2,170.0 784.7,162.3 785.3,162.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="786.9,154.7 787.4,148.3 788.0,144.5 788.5,152.1 789.0,154.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="790.7,150.9 791.2,145.8 791.7,130.5 792.3,134.3 792.8,135.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="795.0,148.3 795.5,144.5 796.1,150.9 796.6,150.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="798.2,141.9 798.7,143.2 799.3,154.7 799.8,156.0 800.4,144.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="802.0,147.0 802.5,149.6 803.1,152.1 803.6,161.1 804.1,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="805.8,145.8 806.3,156.0 806.8,156.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="807.9" cy="154.7" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="809.5,157.2 810.1,162.3 810.6,162.3 811.1,164.9 811.7,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="813.3,168.7 813.8,168.7 814.4,163.6 814.9,158.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="817.1,150.9 817.6,148.3 818.1,157.2 818.7,158.5 819.2,145.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="820.8,144.5 821.4,139.4 821.9,139.4 822.5,139.4 823.0,140.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="824.6,148.3 825.1,153.4 825.7,147.0 826.2,145.8 826.8,150.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="828.4,145.8 828.9,158.5 829.5,154.7 830.0,154.7 830.5,164.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="832.2,166.2 832.7,168.7 833.2,164.9 833.8,164.9 834.3,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="835.9,161.1 836.5,156.0 837.0,162.3 837.5,156.0 838.1,150.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="839.7,148.3 840.2,153.4 840.8,154.7 841.3,150.9 841.9,156.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="843.5,154.7 844.0,153.4 844.5,152.1 845.1,156.0 845.6,150.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="847.8,144.5 848.3,153.4 848.9,158.5 849.4,168.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="851.0,180.2 851.6,176.4 852.1,180.2 852.6,185.3 853.2,181.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="854.8,184.0 855.3,185.3 855.9,184.0 856.4,176.4 856.9,172.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="858.6,170.0 859.1,175.1 859.6,171.3 860.2,172.5 860.7,170.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="862.3,177.6 862.9,175.1 863.4,176.4 863.9,180.2 864.5,177.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="866.1,171.3 866.6,175.1 867.2,176.4 867.7,176.4 868.3,187.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="870.4,189.1 871.0,186.5 871.5,194.2 872.0,191.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="873.6,194.2 874.2,198.0 874.7,199.3 875.3,194.2 875.8,192.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="877.4,195.5 878.0,198.0 878.5,190.4 879.0,185.3 879.6,182.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="881.2,180.2 881.7,182.7 882.3,173.8 882.8,180.2 883.3,178.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="885.0" cy="177.6" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="886.0,182.7 886.6,178.9 887.1,173.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="888.7,175.1 889.3,173.8 889.8,172.5 890.3,175.1 890.9,177.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="892.5,181.4 893.0,182.7 893.6,186.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="894.7" cy="182.7" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="896.3,173.8 896.8,173.8 897.4,175.1 897.9,171.3 898.4,167.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="900.0,164.9 900.6,166.2 901.1,168.7 901.7,167.4 902.2,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="903.8,161.1 904.4,163.6 904.9,162.3 905.4,166.2 906.0,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="907.6,161.1 908.1,162.3 908.7,167.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="909.7" cy="164.9" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="911.4,166.2 911.9,164.9 912.4,161.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<circle cx="913.5" cy="158.5" r="2.4" fill="var(--s-dgs30)"/>
<polyline points="915.1,159.8 915.7,158.5 916.2,163.6 916.8,159.8 917.3,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="918.9,162.3 919.4,162.3 920.0,167.4 920.5,167.4 921.1,162.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="923.2,152.1 923.8,157.2 924.3,161.1 924.8,163.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="926.5,166.2 927.0,162.3 927.5,159.8 928.1,159.8 928.6,157.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="930.2,153.4 930.8,153.4 931.3,152.1 931.8,159.8 932.4,159.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="934.0,159.8 934.5,168.7 935.1,163.6 935.6,176.4 936.1,180.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="938.3,181.4 938.8,177.6 939.4,178.9 939.9,176.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="941.5,178.9 942.1,178.9 942.6,178.9 943.2,182.7 943.7,186.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="945.3,178.9 945.8,178.9 946.4,176.4 946.9,173.8 947.5,170.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="949.1,176.4 949.6,168.7 950.2,158.5 950.7,156.0 951.2,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="952.9,158.5 953.4,159.8 953.9,156.0 954.5,162.3 955.0,145.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="956.6,152.1 957.2,148.3 957.7,154.7 958.2,149.6 958.8,143.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="960.4,152.1 960.9,156.0 961.5,152.1 962.0,156.0 962.6,152.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="964.2,154.7 964.7,153.4 965.2,154.7 965.8,153.4 966.3,152.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="967.9,153.4 968.5,157.2 969.0,154.7 969.6,149.6 970.1,156.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="971.7,156.0 972.3,154.7 972.8,153.4 973.3,150.9 973.9,152.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="975.5,148.3 976.0,148.3 976.6,143.2 977.1,143.2 977.6,144.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="979.3,138.1 979.8,143.2 980.3,148.3 980.9,144.5 981.4,147.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="983.0,143.2 983.6,136.8 984.1,136.8 984.6,138.1 985.2,125.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="986.8,122.8 987.3,117.7 987.9,126.7 988.4,127.9 989.0,131.7" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="991.1,136.8 991.7,139.4 992.2,143.2 992.7,141.9" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="994.3,141.9 994.9,144.5 995.4,141.9 996.0,144.5 996.5,139.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="998.1,136.8 998.7,139.4 999.2,136.8 999.7,147.0 1000.3,144.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1001.9,144.5 1002.4,149.6 1003.0,149.6 1003.5,153.4" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1005.7,147.0 1006.2,148.3 1006.7,158.5 1007.3,158.5 1007.8,157.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1009.4,158.5 1010.0,152.1 1010.5,144.5 1011.0,143.2" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1013.2,141.9 1013.7,134.3 1014.3,133.0 1014.8,134.3 1015.4,133.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1017.0,127.9 1017.5,130.5 1018.1,130.5 1018.6,129.2 1019.1,133.0" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1020.7,126.7 1021.3,124.1 1021.8,121.6 1022.4,119.0 1022.9,120.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1024.5,125.4 1025.1,129.2 1025.6,115.2 1026.1,113.9 1026.7,106.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1028.3,111.4 1028.8,117.7 1029.4,119.0 1029.9,112.6 1030.4,116.5" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1032.1,108.8 1032.6,110.1 1033.1,110.1 1033.7,113.9 1034.2,108.8" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1035.8,101.2 1036.4,105.0 1036.9,116.5 1037.5,111.4 1038.0,106.3" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1039.6,111.4 1040.1,119.0 1040.7,117.7 1041.2,116.5 1041.8,112.6" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1043.4,108.8 1043.9,106.3 1044.5,106.3 1045.0,108.8 1045.5,110.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1047.7,108.8 1048.2,105.0 1048.8,93.5 1049.3,96.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<polyline points="1050.9,97.3 1051.5,94.8 1052.0,96.1" fill="none" stroke="var(--s-dgs30)" stroke-width="2"/>
<text x="1058" y="100.1" font-size="11.5" font-weight="700" fill="var(--s-dgs30)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">미국 30년물 국채금리 5.35%</text>
</svg>
</div>

---

## 2. 해석 참고 — 상승/하락이 의미하는 것

- **한 줄로**: 당장의 연준보다 **먼 미래의 재정·물가**에 대한 시장의 요구 보상이 실리는 금리다.
- **오르면**: 장기 재정건전성 우려나 장기 인플레이션 기대가 커졌다는 신호로 흔히 해석한다.
- **내리면**: 장기 성장·물가 기대가 둔화됐거나 안전자산 수요가 커졌다는 신호로 흔히 해석한다.
- **왜 통화정책보다 재정에 민감한가**: 30년물 수익률은 "앞으로 30년간의 평균 단기금리 기대"보다 **기간 프리미엄**(장기간 묶어 두는 대가) 비중이 크다. 그래서 장기 국채 발행량(재정 전망)과 장기 물가 기대가 더 크게 작용한다. 연기금·보험사처럼 만기가 긴 부채를 가진 기관의 구조적 매수 수요도 가격에 영향을 준다.
- **할인율의 표준 근거로 쓰지 않는다**: 표준은 [10년물](./treasury_10y.md)이다. 이 문서는 수익률곡선의 모양을 보기 위한 보조 자료다.
- **상수만기(constant maturity)라는 표기**: 실제로 만기가 정확히 그 기간인 채권 하나의 값이 아니라, 거래되는 여러 국채의 수익률곡선에서 그 만기 지점을 읽어 낸 값이다. 시간이 지나도 만기가 줄지 않는 일정한 잣대를 유지하기 위한 방식이다.
- **차트의 회색 음영**: NBER이 사후에 판정한 미국의 침체 국면이다. 실시간 신호가 아니라 나중에 붙는 라벨이다.

---

*작성일: 2026-09-18*
