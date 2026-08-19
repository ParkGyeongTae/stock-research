# 원자력 부품·연료 제조

> 원자로 압력용기·증기발생기·핵연료 등 원자력 발전·추진의 핵심 부품을 정밀 제작하는 산업. 국방(해군 원자력 추진)과 상업용 원전 양쪽에 공급하는 소수 과점 업체가 주축이라 하나의 섹터로 묶어 커버한다.

> ⚠️ 이 문서는 **산업 전체를 설명하는 맥락용 문서**다. 특정 회사의 재무 수치·투자 판단은 담지 않는다 — 회사별 사실·투자 판단은 각 회사 문서(`04_metrics.md`·`07_investment.md`)를 따른다. 이 문서와 회사 문서 내용이 겹치면 이 문서 쪽을 줄인다.
>
> ⚠️ 시장 규모(TAM)·CAGR 같은 숫자는 리서치 기관·정의(포함 범위)마다 다르다. 출처를 반드시 병기하고, 출처마다 값이 갈리면 하나로 단정하지 말고 범위로 남길 것.
>
> ⚠️ `concepts/`는 시점에 무관한 영구 참고용이라 "현재" 서술을 넣지 않지만, 이 문서는 **특정 시점의 산업 스냅샷**이라 시점 서술이 들어갈 수 있는 문서다. 그만큼 내용이 시간이 지나면 낡으므로 갱신할 때 `*작성일*`을 놓치지 말 것.

- **섹터명**: 원자력 부품·연료 제조 (Nuclear Components & Fuel Manufacturing)
- **밸류체인 위치**: 업스트림(우라늄 농축)~미드스트림 제조(상업 생산·상업화 이전 단계 포함) — 우라늄 농축부터 원자로·핵연료 완제품 정밀 가공까지 걸쳐 있으며, 커버리지 기업별로 위치가 다르다(BWXT는 상업 생산 중인 미드스트림 제조, Centrus는 업스트림 농축, NuScale은 미드스트림 원자로 제조 중에서도 아직 상업화 이전 단계)
- **커버리지 기업**:
  - [BWX Technologies](./bwx_technologies/01_overview.md)
  - [Centrus Energy](./centrus_energy/01_overview.md)
  - [NuScale Power](./nuscale_power/01_overview.md)
- **인접 섹터**: 아직 없음 (이 섹터가 저장소 내 첫 원자력 관련 섹터)

---

## 1. 한 줄 요약

원자력 부품·연료 제조업은 원자로 압력용기·증기발생기·핵연료봉 등 원자력 발전·추진의 핵심 부품을 규제 인증 아래 정밀 제작하는 산업으로, 고객이 미 해군(잠수함·항공모함 원자로)과 상업용 원전 유틸리티로 나뉜다. 수십 년에 걸친 인증·설비·숙련인력 장벽 때문에 소수 업체가 사실상 독과점하며, 최근 AI 데이터센터발 전력수요 증가로 원전·SMR(소형모듈원자로) 신규 수요가 재조명되면서 다시 주목받고 있다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| 업스트림: 우라늄 채굴·전환·농축 | 천연 우라늄을 채굴해 핵연료용으로 전환·농축(U3O8 → UF6 → 농축 우라늄) | 우라늄 광산업체, 국영·민간 농축업체 (Cameco, Centrus Energy, Rosatom 등) | 자원 매장지 접근권, 방사성물질 취급 라이선스, 대규모 자본 |
| 미드스트림: 원자로·핵연료 정밀 제조 (**이 섹터**) | 농축 우라늄·특수합금을 원자로 압력용기·증기발생기·핵연료봉·정밀 부품으로 가공. 해군 원자로는 설계~제조~연료 장전까지 일괄 수행 | 방산 겸업 정밀제조업체(BWXT), 대형 중공업체(Framatome, Rolls-Royce, KEPCO 계열) | NRC(원자력규제위원회)·해군 인증, 수십 년 축적된 용접·야금 기술, 장기 단독/복수 소싱 계약, 국가안보 심사(ITAR 등) |
| 다운스트림: 발전·운영·서비스 | 원전 건설·운영, 정비·연료교체, 사용후핵연료 관리 | 전력 유틸리티(Constellation Energy, Duke Energy 등), EPC 업체 | 대규모 자본, 원전 건설·운영 인허가, 지역 독점 규제 |

> 개별 회사의 진입장벽(브랜드/전환비용/네트워크 효과/규모의 경제)이 구체적으로 무엇인지는 각 회사 `07_investment.md`에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

업스트림 중에서도 **우라늄 농축** 단계는 특히 소수 과점 구조다. 글로벌 상업용 원전 농축 서비스 시장은 연간 약 5,000만 SWU(분리작업단위) 규모로 추정되며, Rosatom/TENEX(러시아, 약 2,700만 SWU/년)·Urenco(영·네덜란드·독일 컨소시엄, 약 1,700만 SWU/년)·CNEIC(중국, 약 1,100만 SWU/년)·Orano(프랑스) 4개사가 95% 이상을 과점한다(World Nuclear Association 2025년 데이터, Centrus Energy Corp. 10-K FY2025 "Competition and Foreign Trade" 절 인용). Centrus Energy는 이 중 미국이 자국 기술·자본으로 소유한 유일한 사업자라는 지정학적 위치를 갖는데, 러시아산 우라늄 수입을 제한하는 러시아 정지협정(RSA)·Import Ban Act가 이 위치의 가치를 직접 뒷받침한다 — 다만 이는 정책이 바뀌면 가치도 되돌아갈 수 있다는 뜻이기도 하다.

---

## 3. 시장 규모 / 성장 동력

- **시장 규모(TAM)**: 글로벌 원자력 발전 시장 규모는 약 $37.46B(2025년 기준, Research Nester). 이 수치는 발전 시장 전체를 포함하며 원자로·연료 "제조" 단계만의 시장 규모를 별도로 집계한 자료는 확인하지 못함 — 확인 필요
- **성장률(CAGR)**: 약 3.3%(2026~2035년, Research Nester). SMR(소형모듈원자로) 부문은 별도로 훨씬 가파른 성장이 전망됨 — 아래 참고
- **핵심 성장 동력**:
  1. **AI 데이터센터발 전력수요 증가와 SMR 재조명** — IEA는 SMR 투자가 현재 연간 $5B 수준에서 2030년 $25B 이상으로, 2050년까지 누적 $670B 규모로 늘어날 것으로 전망한다(IEA, "The Path to a New Era for Nuclear Energy"). IAEA는 고성장 시나리오에서 2050년 글로벌 원전 설비용량이 2024년의 2.6배(992GW)까지 늘어날 것으로 본다(저성장 시나리오는 561GW, IAEA 발표 기준).
  2. **미 해군 원자력 추진 함정 증산 및 국방예산 확대** — 컬럼비아급 전략핵잠수함·버지니아급 공격원잠 건조 물량이 늘면서 해군 원자로·핵연료 수요가 다년 계약으로 뒷받침됨(국방수권법(NDAA) 예산 배정에 연동).
  3. **노후 원전 교체 및 신규 원전 인허가 확대 기조** — 각국 정부의 탄소중립 정책과 에너지 안보 논의 속에 원전 신규 건설·수명연장 인허가가 늘어나는 추세.

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| 국방예산 의존 | 매출의 상당 부분이 정부(해군) 계약에서 나오는 업체가 많아 국방예산 삭감·정부 셧다운에 민감 | 미 국방수권법(NDAA) 예산안 통과 여부, 연방정부 셧다운 뉴스 |
| 규제·인허가 지연 | NRC 등 규제기관의 신규 원자로·SMR 설계 인증이 지연되면 프로젝트 착공·매출 인식이 밀림 | NRC 설계 인증 심사 일정, 규제 변경 발표 |
| 대형 프로젝트 실행 리스크 | 원자로 건설은 공기 지연·원가 초과가 잦은 산업(예: Vogtle 3·4호기 사례) — 고정가 계약 비중이 높은 업체는 원가 초과를 그대로 떠안을 수 있음 | 진행 중인 대형 프로젝트의 공정률·원가 초과 공시 |
| 공급망·숙련인력 부족 | 특수 용접·야금 숙련인력과 니켈합금 등 특수 원자재 공급이 제한적 | 숙련인력 수급 관련 업계 뉴스, 특수강·니켈합금 가격 추이 |

> 개별 회사의 Bull/Bear Case는 각 회사 `07_investment.md`에서 다룬다. 여기서는 섹터 전체가 함께 노출되는 리스크만 남긴다.

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- 미 국방수권법(NDAA) 예산안, 특히 해군 조선 계정 중 컬럼비아급·버지니아급 잠수함 건조 예산 배정
- NRC의 신규 원자로·SMR 설계 인증(Design Certification) 진행 상황
- 우라늄 현물가격(U3O8)·농축 서비스(SWU) 가격 추이
- 빅테크의 원자력 전력구매계약(PPA) 체결 뉴스(예: 데이터센터향 원전·SMR 계약)

---

## 관련 문서

- [BWX Technologies 개요](./bwx_technologies/01_overview.md)
- [Centrus Energy 개요](./centrus_energy/01_overview.md)
- [NuScale Power 개요](./nuscale_power/01_overview.md)

---

## 참고 자료

- [Nuclear Power Market Size, Share & Growth Forecast to 2035 — Research Nester](https://www.researchnester.com/reports/nuclear-power-market/7450)
- [The Path to a New Era for Nuclear Energy: Outlook for nuclear investment — IEA](https://www.iea.org/reports/the-path-to-a-new-era-for-nuclear-energy/outlook-for-nuclear-investment)
- [IAEA Raises Nuclear Power Projections for Fifth Consecutive Year — IAEA](https://www.iaea.org/newscenter/pressreleases/iaea-raises-nuclear-power-projections-for-fifth-consecutive-year)
- [BWX Technologies, Inc. — Form 10-K FY2025 (SEC EDGAR)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001486957&type=10-K)
- Centrus Energy Corp. — Form 10-K FY2025, "Competition and Foreign Trade" 절(World Nuclear Association 2025년 데이터 인용, SEC EDGAR CIK 0001065059)

---

*작성일: 2026-08-17 (최종 수정일: 2026-08-19)*
