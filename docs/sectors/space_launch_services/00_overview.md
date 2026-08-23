# Space Launch Services (우주 발사 서비스)

> 위성·화물을 궤도에 올리는 발사체 산업으로, 재사용 로켓 기술로 발사 비용이 구조적으로 낮아지면서 위성 인터넷·국방·상업 우주 시장 전반의 성장을 뒷받침하는 인프라 산업이다.

- **섹터명**: Space Launch Services (우주 발사 서비스)
- **밸류체인 위치**: 미드스트림 — 위성·화물 제조사(업스트림)와 최종 궤도 서비스 운영사(다운스트림, 위성 인터넷·통신·지구관측 등) 사이에서 궤도까지 물리적으로 올려주는 발사 서비스를 제공
- **커버리지 기업**: (각 회사 폴더로 링크)
  - [Rocket Lab](./rocket_lab/01_overview.md)
  - [SpaceX](./spacex/01_overview.md)
- **인접 섹터**: `unmanned_aerial_systems`(방산·항공 — 국방 발사 계약이라는 공통 고객군을 일부 공유) — 이 저장소에서 위성 제조·위성통신 운영 섹터는 아직 별도로 커버하지 않음

---

## 1. 한 줄 요약

우주 발사 서비스는 위성·화물을 지구 궤도에 올리는 로켓 발사 사업이다. 재사용 로켓 기술이 발사 단가를 구조적으로 낮추면서, 저궤도 위성 인터넷 구축·국방 위성 수요 증가와 맞물려 빠르게 성장하는 산업이다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| 위성·페이로드 제조 (업스트림) | 발사할 위성·화물 제작 | 위성 제조사, 정부·국방 기관 | 기술력, 인증 |
| **발사체/발사 서비스 (이 섹터)** | 위성·화물을 로켓으로 궤도에 투입 | SpaceX·Rocket Lab·ULA·Blue Origin 등 | 막대한 초기 개발비, 재사용 기술, 발사 실적(신뢰성) 트랙레코드, 각국 발사 인허가 |
| 궤도 운영/최종 서비스 (다운스트림) | 위성을 이용한 통신·인터넷·지구관측 등 서비스 제공 | Starlink(SpaceX 자체 운영), 통신사, 정부기관 | 위성 운용 노하우, 지상 인프라, 주파수 확보 |

발사체는 소형(수백 kg급)·중형·대형(초대형 포함) 등 탑재 중량별로 시장이 나뉘며, 이 섹터의 커버리지 기업은 소형 발사 선두주자(Rocket Lab)와 압도적 1위 사업자(SpaceX, 궤도 발사 질량 기준 약 87%)로 체급이 다르다. 최근에는 재사용 로켓 기술이 업계 표준이 되면서 발사 단가가 구조적으로 낮아지는 추세이며, SpaceX는 위성 인터넷(Starlink) 등 다운스트림 사업까지 수직계열화한 것이 특징이다.

> 개별 회사의 진입장벽이 구체적으로 무엇인지는 각 회사 투자 판단에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

---

## 3. 시장 규모 / 성장 동력

- **시장 규모(TAM)**: 리서치 기관마다 정의(발사 서비스만 vs 위성 산업 전체 포함 여부)가 크게 달라 $6.6B~32B(2026년 기준)까지 넓은 범위로 추정된다 — Research and Markets $31.84B(2026), Grand View Research $25.3B(2026), The Business Research Company 약 $13.85B(2026), Fortune Business Insights $6.57B(2026, 좁은 정의로 추정). 범위가 넓으므로 단일 값으로 단정하지 않는다.
- **성장률(CAGR)**: 기관별로 8.7%~16.9% 범위(2026년 기준 향후 4~9년 전망). 대체로 15%대의 높은 성장률을 제시하는 기관이 많다.
- **핵심 성장 동력**:
  1. **재사용 로켓에 의한 발사 단가 구조적 하락** — 발사 비용이 낮아지면서 이전에는 경제성이 없던 위성 사업(대규모 저궤도 콘스텔레이션 등)이 가능해지는 선순환.
  2. **저궤도 위성 인터넷 콘스텔레이션 구축 수요** — Starlink·Amazon Kuiper·OneWeb 등 대규모 위성군 배치가 반복적 발사 수요를 만들어냄.
  3. **국방·안보 위성 수요 증가** — 각국 정부의 우주 안보 예산 확대(미 우주군 NSSL 프로그램 등)가 안정적인 정부 발사 계약 수요를 뒷받침.

Sources: [Space Launch Services Market — Research and Markets](https://www.researchandmarkets.com/reports/6012027/space-launch-services-market-global-forecast) · [Space Launch Services Market Size Report — Grand View Research](https://www.grandviewresearch.com/industry-analysis/space-launch-services-market-report) · [Space Launch Services Market Report 2026 — Research and Markets](https://www.researchandmarkets.com/reports/5782706/space-launch-services-market-report) · [Space Launch Services Market — Fortune Business Insights](https://www.fortunebusinessinsights.com/industry-reports/space-launch-services-market-101931)

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| 발사 실패/기술적 이상 리스크 | 로켓 발사는 본질적으로 고위험 기술 활동이며, 실패나 이상 발생 시 다음 발사까지 장기간 지상 대기(grounding)로 이어질 수 있음 — 매출·고객 신뢰에 직접 타격 | 발사 성공률 추이, 규제기관(FAA 등)의 조사·지상 대기 명령 여부 |
| 정부·국방 계약 의존도 | 국방 발사(NSSL 등)는 안정적 매출원이지만 정부 예산·정책 변화에 좌우됨 | 미 우주군 등 국방 예산안, NSSL Phase 발주 일정 |
| 발사 단가 경쟁 심화 | 재사용 기술이 업계 표준화되면서 경쟁사 간 가격 경쟁이 격화될 수 있음 — 원가 우위가 없는 후발주자는 마진 압박 | 경쟁사 발사 단가·빈도 공개 자료 |
| 규제·발사 인허가 | 각국 발사장 인허가, 궤도상 잔해(space debris) 규제 강화 가능성 | FAA 등 발사 인허가 기관의 정책 변화, 궤도 혼잡도 관련 국제 규제 논의 |
| 경기 민감도 | 상업 위성 발주는 자본시장 상황(금리·자금조달 여건)에 영향받지만, 국방 계약 비중이 크면 경기 방어적 성격이 강해짐 — 회사별 정부/상업 매출 비중에 따라 편차가 큼 | 상업 위성 스타트업들의 자금조달 동향 |

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- **미 우주군 NSSL(National Security Space Launch) 프로그램 발주 현황** — 대형 안정적 매출원의 배분 상황
- **주요 위성 콘스텔레이션(Starlink·Kuiper·OneWeb 등)의 배치 일정·규제 기한(FCC 배치 의무 등)** — 반복적 발사 수요의 선행지표
- **경쟁사 신규 발사체 개발·시험 발사 일정** (Blue Origin New Glenn, Rocket Lab Neutron 등) — 시장 구도 변화 신호
- **발사 빈도(연간 발사 횟수) 공개 통계** — 각사·업계 전체의 처리 능력(capacity) 추이

---

## 관련 문서

- [Rocket Lab 개요](./rocket_lab/01_overview.md)
- [SpaceX 개요](./spacex/01_overview.md)

---

## 참고 자료

- [Space Launch Services Market - Global Forecast 2026-2032 — Research and Markets](https://www.researchandmarkets.com/reports/6012027/space-launch-services-market-global-forecast)
- [Space Launch Services Market Size Report, 2024-2030 — Grand View Research](https://www.grandviewresearch.com/industry-analysis/space-launch-services-market-report)
- [Space Launch Services Market Report 2026 — Research and Markets](https://www.researchandmarkets.com/reports/5782706/space-launch-services-market-report)
- [Space Launch Services Market Size, Share, Growth Report 2034 — Fortune Business Insights](https://www.fortunebusinessinsights.com/industry-reports/space-launch-services-market-101931)

---

*작성일: 2026-08-16 (최종 수정일: 2026-08-23)*
