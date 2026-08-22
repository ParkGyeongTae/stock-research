# Automated Test Equipment (ATE, 반도체 테스트 장비)

> 제조된 반도체 칩이 규격대로 동작하는지 검사하는 장비 산업으로, 반도체 자체의 생산량·공정 복잡도 사이클에 직접 연동되는 후공정(back-end) 장비 시장이다.

> ⚠️ 이 문서는 **산업 전체를 설명하는 맥락용 문서**다. 특정 회사의 재무 수치·투자 판단은 담지 않는다 — 회사별 사실·투자 판단은 각 회사 문서(핵심 지표·투자 판단)를 따른다. 이 문서와 회사 문서 내용이 겹치면 이 문서 쪽을 줄인다.
>
> ⚠️ 시장 규모(TAM)·CAGR 같은 숫자는 리서치 기관·정의(포함 범위)마다 다르다. 출처를 반드시 병기하고, 출처마다 값이 갈리면 하나로 단정하지 말고 범위로 남길 것.
>
> ⚠️ 개념 정리는 시점에 무관한 영구 참고용이라 "현재" 서술을 넣지 않지만, 이 문서는 **특정 시점의 산업 스냅샷**이라 시점 서술이 들어갈 수 있는 문서다. 그만큼 내용이 시간이 지나면 낡으므로 갱신할 때 `*작성일*`을 놓치지 말 것.

- **섹터명**: Automated Test Equipment (반도체 테스트 장비)
- **밸류체인 위치**: 다운스트림(후공정) — 웨이퍼 제조(파운드리) 이후, 패키징·조립 전후 단계에서 칩의 정상 동작 여부를 검사하는 장비 공급
- **커버리지 기업**: (각 회사 폴더로 링크)
  - [Teradyne](./teradyne/01_overview.md)
- **인접 섹터**: `electronic_design_automation`(EDA, 밸류체인상 업스트림 — 설계 단계) — 이 저장소에서 아직 반도체 파운드리·OSAT(패키징·조립 전문 위탁업체) 섹터는 별도로 커버하지 않음

---

## 1. 한 줄 요약

ATE는 웨이퍼·완성 칩이 사양대로 동작하는지 검사해 불량품을 걸러내고 성능 등급(binning)을 매기는 장비를 만드는 산업이다. 반도체 자체가 팔리려면 반드시 거쳐야 하는 공정이라 반도체 생산량·복잡도 사이클에 직접 연동되며, 최근에는 AI 반도체의 테스트 시간·복잡도 증가가 새로운 성장 동력으로 부상하고 있다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

ATE는 반도체 제조 공정의 후공정(back-end) 단계에 위치해, 웨이퍼 테스트(다이싱 전)와 최종 테스트(패키징 후) 두 시점에서 쓰인다.

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| 칩 설계 (업스트림) | 반도체 설계·검증 (`electronic_design_automation` 섹터 참고) | 팹리스·IDM | EDA 도구·설계 IP |
| 웨이퍼 제조 (업스트림) | 설계된 칩을 실제로 제조 | TSMC·Samsung Foundry·Intel Foundry, 메모리 IDM(Samsung·SK Hynix·Micron) | 막대한 자본 지출, 공정 미세화 기술력 |
| **ATE (이 섹터)** | 웨이퍼·완성 칩의 정상 동작 여부 검사, 성능 등급 분류(binning) | Teradyne·Advantest (사실상 듀오폴리) | 고객(반도체 회사·OSAT)의 신뢰성 검증 사이클이 길어 전환비용이 높음, 최신 공정·패키징 기술 대응력 |
| 패키징·조립 (다운스트림) | 테스트를 통과한 칩의 패키징·조립 | ASE·Amkor 등 OSAT | 장비 투자, 수율 관리 노하우 |
| 최종 수요 | 완성된 칩이 탑재되는 최종 제품 | AI 데이터센터·모바일·자동차·산업용 등 | — |

이 섹터의 커버리지 기업(Teradyne)은 반도체 테스트(SoC·메모리) 사업을 핵심으로 하되, 협동로봇(Robotics) 등 반도체 사이클과 무관한 사업으로 다각화를 병행하고 있다 — 이는 회사 고유의 전략이라 회사 문서에서 다룬다.

> 개별 회사의 진입장벽이 구체적으로 무엇인지는 각 회사 투자 판단에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

---

## 3. 시장 규모 / 성장 동력

- **시장 규모(TAM)**: ATE 한정 기준 리서치 기관별로 $6.6~9.4B(2026년 기준)로 추정치가 갈린다 — 360iResearch $9.43B(2026), Persistence Market Research $8.2B(2026), Intel Market Research $7.56B(2026), IndustryResearch.biz 약 $6.6B(2026). "반도체 테스트 장비" 전체(웨이퍼 프로버 등 포함)로 정의를 넓히면 Mordor Intelligence $16.04B(2026)까지 커진다 — 정의 범위 차이가 크므로 단일 값으로 단정하지 않는다.
- **성장률(CAGR)**: 기관별로 4.6%~7.8% 범위(2026년 기준 향후 6~9년 전망).
- **핵심 성장 동력**:
  1. **AI 반도체 테스트 복잡도 증가** — AI 칩(GPU·가속기·HBM 메모리)은 트랜지스터 밀도·핀 수·전력 밀도가 높아 테스트 시간·장비당 처리 용량 요구가 커짐. 칩 판매 수량이 늘지 않아도 칩 1개당 테스트 비용·시간이 늘어나는 구조.
  2. **첨단 패키징 전환** — 칩렛(chiplet)·2.5D/3D 패키징 확산으로 개별 다이뿐 아니라 패키징 이후 시스템 레벨 테스트 수요가 새로 생김.
  3. **메모리(특히 HBM) 테스트 수요** — AI 서버용 고대역폭 메모리(HBM) 생산 확대가 메모리 테스트 장비 수요를 견인.

Sources: [Semiconductor Automated Test Equipment Market — 360iResearch](https://www.360iresearch.com/library/intelligence/semiconductor-automated-test-equipment) · [Semiconductor Test Equipment Market — Persistence Market Research](https://www.persistencemarketresearch.com/market-research/semiconductor-test-equipment-market.asp) · [Automated Test Equipment Market Outlook — Intel Market Research](https://www.intelmarketresearch.com/automated-test-equipment-market-47367) · [Semiconductor Test Equipment Market — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/semiconductor-test-equipment-market)

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| 반도체 업/다운사이클 | ATE는 반도체 생산량에 직접 연동되는 자본재 산업이라 EDA보다 경기 민감도가 훨씬 높음 — 메모리 가격 하락기·반도체 재고 조정기에는 장비 발주가 크게 줄어듦 | 메모리(DRAM·NAND) 현물가격, 주요 IDM·파운드리의 capex 가이던스, SEMI 반도체 장비 매출(billings) 지표 |
| 지정학 규제 | 첨단 반도체 장비의 대중국 수출통제가 이미 시행 중이며(미 상무부 BIS), 반도체 장비 전반에 걸린 리스크. ATE도 예외가 아님 | BIS 수출관리규정(EAR) 개정, 미·중 반도체 장비 관련 협상 동향 |
| 고객 집중도 | 매출이 소수의 대형 반도체 제조사·메모리 IDM·OSAT에 집중 — 이들의 capex 축소가 섹터 전체 수요에 직접 영향 | 주요 고객사(삼성·SK하이닉스·Micron·TSMC 등)의 반도체 부문 capex 가이던스 |
| 기술 전환 리스크 | 첨단 패키징·차세대 인터페이스로의 전환이 빠르게 진행 중이라, 신기술 대응이 늦은 사업자는 점유율을 잃을 수 있음 | 신규 패키징 규격(HBM4 등) 대응 제품 발표, 경쟁사 대비 신기술 채택 속도 |

> 개별 회사의 Bull/Bear Case는 각 회사 투자 판단에서 다룬다. 여기서는 섹터 전체가 함께 노출되는 리스크만 남긴다.

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- **SEMI 반도체 장비 매출(billings) 통계** — 전 세계 반도체 장비 산업의 월간/분기 매출 지표, ATE 수요의 선행지표
- **DRAM·NAND 현물가격 추이** — 메모리 가격 사이클은 메모리 IDM의 capex·테스트 장비 발주와 강하게 연동
- **주요 파운드리·IDM의 capex 가이던스** — TSMC·Samsung·Intel·Micron·SK하이닉스의 연간 투자 계획 발표
- **AI 가속기(GPU 등) 출하량·생산 계획** — AI 칩 생산 확대는 첨단 테스트 장비 수요와 직결

---

## 관련 문서

- [Teradyne 개요](./teradyne/01_overview.md)

---

## 참고 자료

- [Semiconductor Automated Test Equipment Market Size 2026-2032 — 360iResearch](https://www.360iresearch.com/library/intelligence/semiconductor-automated-test-equipment)
- [Semiconductor Test Equipment Market Forecast 2026-2033 — Persistence Market Research](https://www.persistencemarketresearch.com/market-research/semiconductor-test-equipment-market.asp)
- [Automated Test Equipment Market Outlook 2026-2034 — Intel Market Research](https://www.intelmarketresearch.com/automated-test-equipment-market-47367)
- [Semiconductor Test Equipment Market Size & Growth to 2031 — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/semiconductor-test-equipment-market)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-21)*
