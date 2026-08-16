# Unmanned Aerial Systems (UAS, 무인체계)

> 조종사 없이 운용되는 군용 항공기·자폭 드론(loitering munition) 등을 만드는 방산 하위 산업으로, 우크라이나 전쟁 이후 "저비용 대량생산(affordable mass)" 전략이 각국 국방 예산의 우선순위로 떠오르며 구조적 성장기에 있다.

> ⚠️ 이 문서는 **산업 전체를 설명하는 맥락용 문서**다. 특정 회사의 재무 수치·투자 판단은 담지 않는다 — 회사별 사실·투자 판단은 각 회사 문서(`04_metrics.md`·`07_investment.md`)를 따른다. 이 문서와 회사 문서 내용이 겹치면 이 문서 쪽을 줄인다.
>
> ⚠️ 시장 규모(TAM)·CAGR 같은 숫자는 리서치 기관·정의(포함 범위)마다 다르다. 출처를 반드시 병기하고, 출처마다 값이 갈리면 하나로 단정하지 말고 범위로 남길 것.
>
> ⚠️ `concepts/`는 시점에 무관한 영구 참고용이라 "현재" 서술을 넣지 않지만, 이 문서는 **특정 시점의 산업 스냅샷**이라 시점 서술이 들어갈 수 있는 문서다. 그만큼 내용이 시간이 지나면 낡으므로 갱신할 때 `*작성일*`을 놓치지 말 것.

- **섹터명**: Unmanned Aerial Systems (무인체계, 군용 무인기)
- **밸류체인 위치**: 미드스트림~다운스트림 — 센서·통신·추진 등 부품(업스트림)을 통합해 완제 플랫폼(무인기·자폭 드론 등)을 만들고, 정부(주로 국방부) 프로그램에 직접 공급하는 방산 완제품 사업자
- **커버리지 기업**: (각 회사 폴더로 링크)
  - [AeroVironment](./aerovironment/01_overview.md)
  - [Kratos Defense & Security Solutions](./kratos/01_overview.md)
- **인접 섹터**: `space_launch_services`(우주 발사 — 일부 국방 고객군 공유) — 이 저장소에서 대형 방산 프라임(Lockheed Martin·General Dynamics 등)·위성 방산 섹터는 아직 별도로 커버하지 않음

---

## 1. 한 줄 요약

UAS 산업은 정찰·타격·표적기 등으로 쓰이는 군용 무인항공기를 개발·생산하는 방산 하위 산업이다. 미군을 비롯한 주요국 국방부가 유인 전투기 대비 저렴한 "소모성(attritable)" 무인체계를 대량 조달하는 방향으로 전략을 전환하면서, 관련 예산과 프로그램이 빠르게 늘고 있다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| 부품(업스트림) | 센서·통신장비·추진체·항전장비 등 | 방산 부품 공급사 | 군사 규격 인증 |
| **플랫폼 개발·생산 (이 섹터)** | 무인기·자폭 드론·표적기 등 완제 플랫폼 설계·제조 | AeroVironment·Kratos·General Atomics·Anduril 등 | 국방부 프로그램 선정(program of record) 트랙레코드, 보안 인가(security clearance), 개발·인증에 드는 장기간·고비용 |
| 정부 조달/프로그램 (다운스트림) | 프로그램 선정, 예산 배정, 조달 계약 체결 | 미 국방부(각 군종), 동맹국 국방부(FMS 경로) | — |
| 최종 사용자 | 실전 운용 | 각국 군, 방위산업 협력국 | — |

이 섹터의 커버리지 기업은 모두 플랫폼 개발·생산 단계에 있으며, 국방부 프로그램 선정 여부가 매출의 핵심 변수다. 최근 미 국방부의 CCA(Collaborative Combat Aircraft) 등 대형 프로그램에서 신흥 방산 스타트업(Anduril 등)과 전통 방산 대기업(General Atomics 등)이 함께 경쟁하는 구도가 형성되며 업계 재편이 진행 중이다.

> 개별 회사의 진입장벽이 구체적으로 무엇인지는 각 회사 `07_investment.md`에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

---

## 3. 시장 규모 / 성장 동력

- **시장 규모(TAM)**: 리서치 기관별로 "군용 드론" 정의 범위 차이로 $20~54B(2026년 기준)까지 넓게 추정된다 — 대체로 $20~35B 구간에 다수 기관이 몰려 있고($22.49B, $20.7B, $27.20B, $34.85B 등), 넓은 정의(민군 겸용 UAV 포함)를 쓰는 기관은 $54.2B까지 추정. 단일 값으로 단정하지 않는다.
- **성장률(CAGR)**: 대부분 기관이 7~14% 구간(2026년 기준 향후 5~9년 전망)을 제시하며, 일부 좁은 정의의 기관은 25%대의 높은 CAGR을 제시하기도 한다 — 후자는 이상치(outlier)로 보고 범위 하단·중간값에 무게를 둘 것.
- **핵심 성장 동력**:
  1. **"저비용 대량생산(affordable mass)" 전략으로의 전환** — 우크라이나 전쟁에서 저가 소모성 무인기의 실전 효과가 입증되며, 미 국방부를 비롯한 각국이 고가 유인 플랫폼 대신 저비용 무인체계를 대량 조달하는 방향으로 전략을 바꾸는 중.
  2. **국방 예산 확대** — 지정학적 긴장 고조로 미국·NATO 회원국·인도태평양 동맹국의 국방 예산이 전반적으로 증가 추세.
  3. **자율화·AI 결합** — 무인기에 AI 기반 자율 임무 수행 능력을 결합하는 차세대 프로그램(CCA 등)이 새로운 수요를 창출.

Sources: [Military Drone Market — Fortune Business Insights](https://www.fortunebusinessinsights.com/military-drone-market-102181) · [Military Drones Market — GMInsights](https://www.gminsights.com/industry-analysis/military-drone-market) · [Military Drone Market — Grand View Research](https://www.grandviewresearch.com/industry-analysis/military-drone-market-report) · [Military Drones Market — MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/military-drone-market-221577711.html)

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| 정부 예산·프로그램 의존도 | 매출 대부분이 정부(주로 미 국방부) 예산에서 나와, 국방 예산안 통과 지연(정부 셧다운 등)이나 특정 프로그램 취소·축소에 직접 영향받음 | 미 국방수권법(NDAA)·세출예산안(appropriations) 통과 일정, 개별 프로그램 예산 배정 현황 |
| 프로그램 선정 리스크 | 대형 국방 프로그램은 소수 승자만 선정되는 경쟁 입찰 구조라, 선정에서 탈락하면 그 분야 매출 기회 자체가 사라짐 (예: CCA Increment 1 선정) | 주요 프로그램 RFP·선정 발표 일정 |
| 수출 통제·FMS 승인 | 해외 판매(Foreign Military Sales)는 미 국무부·의회 승인이 필요해 지정학적 상황에 따라 지연·거부될 수 있음 | 국무부 FMS 승인 공고, 의회 무기 수출 심사 동향 |
| 기술 변화(대드론 방어 고도화) | 대드론 방어(counter-UAS) 기술이 발전하면 기존 무인기 플랫폼의 실전 효과가 떨어져 차세대 설계로의 전환 압력이 생김 | 경쟁국·적성국의 대드론 방어체계 배치 동향 |

> 개별 회사의 Bull/Bear Case는 각 회사 `07_investment.md`에서 다룬다. 여기서는 섹터 전체가 함께 노출되는 리스크만 남긴다.

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- **미 국방수권법(NDAA)·국방 세출예산안** — 무인체계 관련 예산 배정 규모·항목
- **주요 프로그램 발주·선정 일정** — CCA(Collaborative Combat Aircraft) 등 차세대 프로그램의 Increment별 진행 상황
- **실전 분쟁에서의 무인기 운용 사례** — 우크라이나 전쟁 등에서 드러나는 전술적 효과가 조달 우선순위에 영향
- **FMS(대외군사판매) 승인 공고** — 해외 매출 파이프라인의 선행지표

---

## 관련 문서

- [AeroVironment 개요](./aerovironment/01_overview.md)
- [Kratos Defense & Security Solutions 개요](./kratos/01_overview.md)

---

## 참고 자료

- [Military Drone Market Size, Share, Trends — Fortune Business Insights](https://www.fortunebusinessinsights.com/military-drone-market-102181)
- [Military Drones Market Size, Share & Growth Report — GMInsights](https://www.gminsights.com/industry-analysis/military-drone-market)
- [Military Drone Market Size And Growth Report — Grand View Research](https://www.grandviewresearch.com/industry-analysis/military-drone-market-report)
- [Military Drones Market — MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/military-drone-market-221577711.html)

---

*작성일: 2026-08-16*
