# 미국 물가지표 3종 비교

::: info
[CPI](./cpi.md)·[Core CPI](./core_cpi.md)·[Core PCE](./core_pce.md)의 전년동월비를 한 차트에 겹쳐, 셋이 어떻게 벌어지고 좁혀지는지 보기 위한 자료다. 통화·금속 비교 문서와 달리 **지수화하지 않는다** — 셋 다 이미 같은 단위(%)라 원값을 그대로 겹쳐야 수준과 격차가 왜곡 없이 보인다.
:::

---

## 1. 차트 — 최근 5년 월간, 원값(%) 그대로 겹침

<style>
.fred-cpiaucsl-cpilfesl-pcepilfe {
  --bg:#fcfcfb; --grid:#e1e0d9; --axis:#c3c2b7; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781; --base:#898781; --rec:#898781; --s-cpiaucsl:#2a78d6; --s-cpilfesl:#eb6834; --s-pcepilfe:#1baf7a;
}
.dark .fred-cpiaucsl-cpilfesl-pcepilfe { --bg:#1a1a19; --grid:#2c2c2a; --axis:#383835; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781; --base:#898781; --rec:#c3c2b7; --s-cpiaucsl:#3987e5; --s-cpilfesl:#d95926; --s-pcepilfe:#199e70; }
.fred-cpiaucsl-cpilfesl-pcepilfe svg { width:100%; height:auto; display:block; }
.fred-cpiaucsl-cpilfesl-pcepilfe text { font-family: system-ui,-apple-system,"Segoe UI",sans-serif; }
.fred-cpiaucsl-cpilfesl-pcepilfe .title { fill: var(--ink); font-weight:600; }
.fred-cpiaucsl-cpilfesl-pcepilfe .grid { stroke: var(--grid); stroke-width:1; }
.fred-cpiaucsl-cpilfesl-pcepilfe .axis { stroke: var(--axis); stroke-width:1; }
</style>

<div class="fred-cpiaucsl-cpilfesl-pcepilfe">
<svg viewBox="0 0 1200 700" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CPI·Core CPI·Core PCE, 최근 5년 월간, 단위 % 선 차트">
<rect x="0" y="0" width="1200" height="700" fill="var(--bg)"/>
<text x="60" y="26" class="title" font-size="18">미국 물가지표 3종 비교 (전년동월비) (최근 5년 월간)</text>
<text x="60" y="44" font-size="12.5" fill="var(--ink2)">2021-09-01 ~ 2026-08-01 · 단위: % · 출처: FRED CPIAUCSL · FRED CPILFESL · FRED PCEPILFE</text>
<line x1="60" y1="562.5" x2="1052" y2="562.5" class="grid"/>
<text x="52" y="566.5" font-size="11" text-anchor="end" fill="var(--muted)">2.0</text>
<line x1="60" y1="428.1" x2="1052" y2="428.1" class="grid"/>
<text x="52" y="432.1" font-size="11" text-anchor="end" fill="var(--muted)">4.0</text>
<line x1="60" y1="293.7" x2="1052" y2="293.7" class="grid"/>
<text x="52" y="297.7" font-size="11" text-anchor="end" fill="var(--muted)">6.0</text>
<line x1="60" y1="159.3" x2="1052" y2="159.3" class="grid"/>
<text x="52" y="163.3" font-size="11" text-anchor="end" fill="var(--muted)">8.0</text>
<line x1="127.4" y1="56" x2="127.4" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="127.4" y1="600" x2="127.4" y2="605" class="axis"/>
<text x="127.4" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2022</text>
<line x1="329.1" y1="56" x2="329.1" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="329.1" y1="600" x2="329.1" y2="605" class="axis"/>
<text x="329.1" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2023</text>
<line x1="530.9" y1="56" x2="530.9" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="530.9" y1="600" x2="530.9" y2="605" class="axis"/>
<text x="530.9" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2024</text>
<line x1="733.1" y1="56" x2="733.1" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="733.1" y1="600" x2="733.1" y2="605" class="axis"/>
<text x="733.1" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2025</text>
<line x1="934.8" y1="56" x2="934.8" y2="600" stroke="var(--axis)" stroke-width="1" stroke-dasharray="2,4" opacity="0.5"/>
<line x1="934.8" y1="600" x2="934.8" y2="605" class="axis"/>
<text x="934.8" y="618" font-size="10.5" text-anchor="middle" fill="var(--muted)">2026</text>
<line x1="60" y1="600" x2="1052" y2="600" class="axis"/>
<line x1="60" y1="56" x2="60" y2="600" class="axis"/>
<line x1="60" y1="562.5" x2="1052" y2="562.5" stroke="var(--base)" stroke-width="1.2" stroke-dasharray="5,3" opacity="0.85"/>
<text x="66" y="557.5" font-size="10.5" fill="var(--muted)">연준 물가목표 2%</text>
<polyline points="60.0,337.3 76.6,277.9 93.7,233.1 110.3,214.8 127.4,189.0 144.6,163.5 160.0,120.9 177.2,143.8 193.7,123.2 210.9,93.5 227.5,128.2 244.6,144.4 261.7,146.4 278.3,175.5 295.4,218.3 312.0,266.5 329.1,271.7 346.3,296.5 361.7,366.4 378.9,364.3 395.5,419.2 412.6,490.5 429.2,476.0 446.3,446.7 463.4,449.1 480.0,478.4 497.1,486.3 513.7,474.1 530.9,489.4 548.0,484.7 564.0,462.6 581.1,471.0 597.7,478.9 614.9,497.3 631.4,499.2 648.6,521.7 665.7,533.8 682.3,523.6 699.4,514.1 716.0,504.0 733.1,495.9 750.3,508.6 765.7,536.8 782.9,540.6 799.4,537.1 816.6,516.8 833.2,512.6 850.3,499.4 867.4,493.8" fill="none" stroke="var(--s-cpiaucsl)" stroke-width="2"/>
<polyline points="901.1,515.7 917.7,518.6 934.8,536.2 952.0,533.3 967.4,476.1 984.6,442.9 1001.2,416.9 1018.3,464.1 1034.9,474.9 1052.0,471.6" fill="none" stroke="var(--s-cpiaucsl)" stroke-width="2"/>
<polyline points="60.0,427.9 76.6,388.4 93.7,362.7 110.3,328.0 127.4,290.1 144.6,263.1 160.0,261.3 177.2,283.0 193.7,292.0 210.9,300.0 227.5,300.4 244.6,274.5 261.7,251.8 278.3,273.9 295.4,295.7 312.0,314.8 329.1,324.7 346.3,327.4 361.7,322.8 378.9,326.3 395.5,338.2 412.6,370.7 429.2,381.0 446.3,401.3 463.4,419.4 480.0,426.3 497.1,426.9 513.7,433.8 530.9,437.6 548.0,444.1 564.0,440.4 581.1,453.2 597.7,468.8 614.9,477.5 631.4,479.8 648.6,476.1 665.7,476.3 682.3,475.2 699.4,476.1 716.0,481.0 733.1,476.3 750.3,486.0 765.7,508.1 782.9,510.3 799.4,511.0 816.6,501.3 833.2,491.6 850.3,487.8 867.4,493.9" fill="none" stroke="var(--s-cpilfesl)" stroke-width="2"/>
<polyline points="901.1,522.2 917.7,519.0 934.8,528.1 952.0,530.7 967.4,522.0 984.6,512.5 1001.2,507.2 1018.3,524.5 1034.9,531.1 1052.0,532.5" fill="none" stroke="var(--s-cpilfesl)" stroke-width="2"/>
<polyline points="60.0,427.2 76.6,398.8 93.7,368.2 110.3,346.5 127.4,336.8 144.6,320.4 160.0,321.0 177.2,337.7 193.7,348.5 210.9,339.7 227.5,353.7 244.6,336.5 261.7,320.2 278.3,330.0 295.4,346.9 312.0,363.1 329.1,365.1 346.3,370.6 361.7,375.5 378.9,375.0 395.5,378.9 412.6,402.3 429.2,408.0 446.3,439.6 463.4,449.1 480.0,463.4 497.1,475.8 513.7,487.7 530.9,484.6 548.0,491.3 564.0,487.1 581.1,494.8 597.7,510.7 614.9,511.9 631.4,508.3 648.6,503.8 665.7,506.1 682.3,496.2 699.4,496.6 716.0,496.1 733.1,510.1 750.3,497.4 765.7,517.4 782.9,521.2 799.4,509.8 816.6,508.2 833.2,504.5 850.3,501.2 867.4,507.0 884.0,511.8 901.1,506.8 917.7,497.2 934.8,488.3 952.0,492.0 967.4,478.2 984.6,473.1 1001.2,464.1 1018.3,472.2 1034.9,472.2" fill="none" stroke="var(--s-pcepilfe)" stroke-width="2"/>
<text x="1058" y="475.6" font-size="11.5" font-weight="700" fill="var(--s-cpiaucsl)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">CPI 3.4%</text>
<text x="1058" y="491.6" font-size="11.5" font-weight="700" fill="var(--s-pcepilfe)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">Core PCE 3.3%</text>
<text x="1058" y="536.5" font-size="11.5" font-weight="700" fill="var(--s-cpilfesl)" paint-order="stroke" stroke="var(--bg)" stroke-width="3">Core CPI 2.4%</text>
</svg>
</div>

### 5년간 변화 요약

| 지표 | 시작 | 현재 | 변화 | 기간 최고 | 기간 최저 |
|------|------|------|------|-----------|-----------|
| CPI | 5.4% (2021-09-01) | 3.4% (2026-08-01) | -2.0 | 9.0% (2022-06-01) | 2.3% (2025-04-01) |
| Core CPI | 4.0% (2021-09-01) | 2.4% (2026-08-01) | -1.6 | 6.6% (2022-09-01) | 2.4% (2026-08-01) |
| Core PCE | 4.0% (2021-09-01) | 3.3% (2026-07-01) | -0.7 | 5.6% (2022-09-01) | 2.6% (2025-04-01) |

---

## 2. 해석 참고 — 이 차트를 읽는 법

이 절은 특정 구간의 결과가 아니라 **차트와 표를 어떤 순서로 읽는지**만 정리한다.

- **세 선이 함께 위로**: 물가 압력이 특정 품목이 아니라 전반에 걸쳐 있다는 신호로 흔히 해석한다.
- **세 선이 함께 아래로**: 기조적 디스인플레이션 국면으로 흔히 해석한다.
- **CPI와 Core CPI의 간격 = 에너지·식품의 기여도**: CPI가 Core CPI 위로 벌어지면 유가·식료품이 물가를 밀어 올리는 국면, 아래로 내려가면 그 둘이 물가를 끌어내리는 국면으로 읽는다.
- **Core CPI와 Core PCE의 간격 = 만드는 방식의 차이**: 둘 다 "에너지·식품 제외"인데 숫자가 다른 이유는 바스켓 가중치와 포함 범위가 다르기 때문이다(상세는 [Core PCE](./core_pce.md)). 그래서 이 간격은 대체로 한 방향으로 유지되며, 정책 판단의 기준은 연준이 목표를 매기는 Core PCE 쪽이다.
- **셋 다 기저효과를 공유한다**: 모두 전년동월비라, 작년 같은 달이 특이했다면 세 선이 동시에 같은 방향으로 움직인다 — 올해 물가의 변화가 아니라 비교 대상의 성질이다.
- **선의 길이가 다를 수 있다**: Core PCE는 나머지 둘보다 발표가 한 달가량 늦어 차트 오른쪽 끝이 짧게 끝난다. 발표가 취소된 달은 결측으로 남아 선이 끊긴다 — 스크립트 오류가 아니다.
- **차트의 회색 음영과 점선**: 음영은 NBER이 사후에 판정한 침체 국면, 가로 점선은 연준의 물가목표 2%다. 목표선은 정책 판단의 기준점이지 도달해야 하는 상한선이 아니다.

---

*작성일: 2026-09-18*
