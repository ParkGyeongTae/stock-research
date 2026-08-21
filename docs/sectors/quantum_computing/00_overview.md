# Quantum Computing (양자컴퓨팅)

> 양자역학 원리를 이용해 특정 문제(최적화·화학 시뮬레이션·암호 등)를 고전 컴퓨터보다 빠르게 풀 잠재력을 지닌 컴퓨팅 방식으로, 아직 상용화 초기 단계라 매출 규모는 작지만 성장률과 밸류에이션 기대치가 모두 극단적으로 높은 산업이다.

> ⚠️ 이 문서는 **산업 전체를 설명하는 맥락용 문서**다. 특정 회사의 재무 수치·투자 판단은 담지 않는다 — 회사별 사실·투자 판단은 각 회사 문서(`04_metrics.md`·`07_investment.md`)를 따른다. 이 문서와 회사 문서 내용이 겹치면 이 문서 쪽을 줄인다.
>
> ⚠️ 시장 규모(TAM)·CAGR 같은 숫자는 리서치 기관·정의(포함 범위)마다 다르다. 출처를 반드시 병기하고, 출처마다 값이 갈리면 하나로 단정하지 말고 범위로 남길 것.
>
> ⚠️ 개념 정리는 시점에 무관한 영구 참고용이라 "현재" 서술을 넣지 않지만, 이 문서는 **특정 시점의 산업 스냅샷**이라 시점 서술이 들어갈 수 있는 문서다. 그만큼 내용이 시간이 지나면 낡으므로 갱신할 때 `*작성일*`을 놓치지 말 것.

- **섹터명**: Quantum Computing (양자컴퓨팅)
- **밸류체인 위치**: 업스트림 — 양자컴퓨터 하드웨어·소프트웨어 개발사가 클라우드 플랫폼을 통해 최종 고객(기업·정부)에게 컴퓨팅 자원을 제공하는 신흥 컴퓨팅 인프라 계층
- **커버리지 기업**: (각 회사 폴더로 링크)
  - [IonQ](./ionq/01_overview.md)
- **인접 섹터**: 이 저장소에서 아직 클라우드 인프라·반도체(초전도/트랩드 이온 칩 제조) 섹터는 별도로 커버하지 않음

---

## 1. 한 줄 요약

양자컴퓨팅은 큐비트(qubit)라는 양자역학적 단위를 이용해 특정 유형의 문제를 고전 컴퓨터보다 빠르게 계산할 잠재력을 가진 신흥 컴퓨팅 산업이다. 아직 "결함허용양자컴퓨팅(fault-tolerant quantum computing)" 수준의 상용화는 이르지 못했지만, 매출은 낮은 기저에서 빠르게 성장 중이고 국가·대형 기술기업이 모두 투자를 확대하고 있다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| **양자 하드웨어/소프트웨어 개발 (이 섹터)** | 큐비트 하드웨어(트랩드 이온·초전도·중성원자·광자 등 방식별) 설계·제조, 제어 소프트웨어 개발 | IonQ·Quantinuum(비상장)·Rigetti·IBM·Google 등 | 극저온·정밀 제어 등 첨단 물리학 기술력, 오랜 R&D 축적, 자본 집약도 |
| 클라우드 배포/유통 (다운스트림 채널) | 양자컴퓨팅 자원을 클라우드로 제공 | AWS Braket·Azure Quantum·Google Cloud Marketplace | 하이퍼스케일러의 플랫폼 지배력 — 순수 양자컴퓨팅 기업 입장에서는 유통 채널이자 동시에 잠재적 경쟁자 |
| 최종 고객 | 최적화·화학 시뮬레이션·암호 연구 등에 활용 | 정부·국책연구소, 제약·화학·금융 기업 R&D 부서 | — |

이 산업의 특징은 **경쟁하는 큐비트 기술 방식이 여럿 공존하며 아직 승자가 가려지지 않았다**는 점이다 — 초전도(IBM·Google), 트랩드 이온(IonQ·Quantinuum), 중성원자, 광자 등 방식마다 장단점(정확도·확장성·상온 동작 여부)이 달라 표준화가 이뤄지지 않았다. 또한 IBM·Google·Microsoft 등 대형 기술기업이 자체 하드웨어 개발과 동시에 클라우드 유통 채널까지 쥐고 있어, 순수 양자컴퓨팅 상장기업에는 유통 의존이 "역(逆)해자"로 작용할 수 있다.

> 개별 회사의 진입장벽이 구체적으로 무엇인지는 각 회사 `07_investment.md`에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

---

## 3. 시장 규모 / 성장 동력

- **시장 규모(TAM)**: 리서치 기관별로 $1.8~5.6B(2026년 기준)로 편차가 크다 — Grand View Research $1.9B(2026), Fortune Business Insights $1.82B(2026), FactMR $2.0B(2026), Research and Markets $5.59B(2026), The Business Research Company $5.09B(2026). 정의(순수 하드웨어만 vs 소프트웨어·서비스 포함 여부)가 갈려 단일 값으로 단정하지 않는다. 절대 규모 자체가 다른 커버리지 섹터 대비 아직 작다는 점에 유의.
- **성장률(CAGR)**: 기관 대부분이 22~37%(2026년 기준 향후 7~14년 전망)라는 매우 높은 성장률을 제시 — 다만 절대 규모가 작은 초기 시장 특유의 기저효과(base effect)를 감안해서 읽어야 한다.
- **핵심 성장 동력**:
  1. **국가 차원의 양자 기술 투자 경쟁** — 미국(National Quantum Initiative), 중국, EU 등이 국가 안보·산업 경쟁력 차원에서 양자컴퓨팅 R&D에 대규모 예산을 투입.
  2. **엔터프라이즈 파일럿 프로그램 확대** — 제약·화학·금융 등 산업에서 최적화·시뮬레이션 문제에 양자컴퓨팅을 시범 적용하는 사례가 늘어나는 초기 상업화 단계.
  3. **큐비트 정확도·큐비트 수 개선** — 하드웨어 성능이 개선될수록 실용적 문제 해결 가능성이 커져 상업화 시점이 앞당겨질 것이라는 기대.

Sources: [Quantum Computing Market — Grand View Research](https://www.grandviewresearch.com/industry-analysis/quantum-computing-market) · [Quantum Computing Market — Fortune Business Insights](https://www.fortunebusinessinsights.com/quantum-computing-market-104855) · [Quantum Computing Market — Research and Markets](https://www.researchandmarkets.com/reports/5470718/quantum-computing-market-global-forecast-2026) · [Quantum Computing Market — FactMR](https://www.factmr.com/report/quantum-computing-market)

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| 기술 표준 미확정 | 여러 큐비트 방식이 경쟁 중이며 어느 방식이 상용화 단계에서 우위를 점할지 아직 불확실 — 특정 방식에 베팅한 기업이 기술 경쟁에서 밀리면 사업 자체가 흔들릴 수 있음 | 각 방식별 큐비트 수·정확도(fidelity) 개선 속도, 학계·업계의 방식별 우위 평가 변화 |
| 상용화 시점 지연 리스크 | "결함허용양자컴퓨팅" 등 실질적 상업 가치를 낼 수 있는 수준의 상용화 목표 시점(업계 통상 2030년 전후로 거론)이 계속 후퇴할 가능성 | 주요 기업의 로드맵 발표·목표연도 수정 여부 |
| 클라우드 유통 의존(역해자) | AWS·Azure·Google 등 하이퍼스케일러가 유통 채널이자 동시에 자체 양자컴퓨팅 개발 경쟁자 — 이들이 자사 기술을 우선 노출시키면 순수 양자컴퓨팅 기업의 채널 접근성이 축소될 수 있음 | 하이퍼스케일러의 자체 양자칩 로드맵·클라우드 마켓플레이스 정책 변화 |
| 정부 예산 의존도 | 초기 매출의 상당 부분이 정부·국책 연구 예산에서 나오는 경우가 많아, 예산 축소 시 매출에 직접 영향 | 각국 양자 기술 관련 예산안·국가전략 발표 |
| 산업 전반의 자본시장 민감도 | 아직 대부분 기업이 적자 상태라, 금리·리스크 선호도 변화에 따라 밸류에이션 변동성이 큼 | 금리 환경, 고성장·고밸류 기술주 전반의 시장 심리 |

> 개별 회사의 Bull/Bear Case는 각 회사 `07_investment.md`에서 다룬다. 여기서는 섹터 전체가 함께 노출되는 리스크만 남긴다.

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- **각국 양자 기술 국가전략·예산 발표** (미국 National Quantum Initiative 재승인, 중국·EU 투자 계획 등)
- **하이퍼스케일러(AWS·Microsoft·Google)의 자체 양자칩 로드맵·마일스톤 발표** — 유통 채널이자 잠재 경쟁자의 움직임
- **큐비트 수·정확도(fidelity) 개선 마일스톤 발표** — 기술 경쟁 구도 변화 신호
- **엔터프라이즈 파일럿 프로그램·상용 계약 발표** — 초기 상업화 진행 상황

---

## 관련 문서

- [IonQ 개요](./ionq/01_overview.md)

---

## 참고 자료

- [Quantum Computing Market Size & Share Report, 2026-2033 — Grand View Research](https://www.grandviewresearch.com/industry-analysis/quantum-computing-market)
- [Quantum Computing Market Size, Share — Fortune Business Insights](https://www.fortunebusinessinsights.com/quantum-computing-market-104855)
- [Quantum Computing Market - Global Forecast 2026-2032 — Research and Markets](https://www.researchandmarkets.com/reports/5470718/quantum-computing-market-global-forecast-2026)
- [Quantum Computing Market — FactMR](https://www.factmr.com/report/quantum-computing-market)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-21)*
