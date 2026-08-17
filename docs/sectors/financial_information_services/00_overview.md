# Financial Information & Analytics (금융 정보·분석 서비스)

> 기업 재무·시장가격·원자재 가격 같은 원천 데이터를 신용등급·지수(벤치마크)·분석 플랫폼으로 가공해 자산운용사·은행·발행기업·규제당국에 유통하는 산업으로, 규제가 만든 진입장벽(NRSRO 지정 등)과 전환비용(워크플로 내재화)에 힘입어 소수 사업자가 과점하는 구조다.

> ⚠️ 이 문서는 **산업 전체를 설명하는 맥락용 문서**다. 특정 회사의 재무 수치·투자 판단은 담지 않는다 — 회사별 사실·투자 판단은 각 회사 문서(`04_metrics.md`·`07_investment.md`)를 따른다. 이 문서와 회사 문서 내용이 겹치면 이 문서 쪽을 줄인다.
>
> ⚠️ 시장 규모(TAM)·CAGR 같은 숫자는 리서치 기관·정의(포함 범위)마다 다르다. 출처를 반드시 병기하고, 출처마다 값이 갈리면 하나로 단정하지 말고 범위로 남길 것.
>
> ⚠️ `concepts/`는 시점에 무관한 영구 참고용이라 "현재" 서술을 넣지 않지만, 이 문서는 **특정 시점의 산업 스냅샷**이라 시점 서술이 들어갈 수 있는 문서다. 그만큼 내용이 시간이 지나면 낡으므로 갱신할 때 `*작성일*`을 놓치지 말 것.

- **섹터명**: Financial Information & Analytics (금융 정보·분석 서비스)
- **밸류체인 위치**: 미드스트림 — 증권거래소·규제 공시 등에서 나오는 원천 데이터(업스트림)를 신용등급·지수·분석 플랫폼으로 가공해 자산운용사·은행·발행기업(다운스트림)에 유통하는 계층
- **커버리지 기업**: (각 회사 폴더로 링크)
  - [S&P Global](./sp_global/01_overview.md)
- **인접 섹터**: 이 저장소에서 아직 별도로 커버하지 않음(신용평가 대상이 되는 발행기업 자체, 자산운용사, 은행·보험사 등은 별도 섹터로 분리 가능하나 현재 커버리지 없음)

---

## 1. 한 줄 요약

금융 정보·분석 산업은 원천 금융/시장 데이터를 신용등급·지수(벤치마크)·리서치 분석 상품으로 가공해 부가가치를 만드는 사업이다. 신용평가는 채권 발행기업이 자본시장에 접근하기 위해 사실상 필수로 거쳐야 하는 관문이고, 지수 사업은 패시브 투자 성장의 직접 수혜를 받는 구조라 두 사업 모두 규제가 뒷받침하는 높은 진입장벽 위에서 안정적인 현금흐름을 낸다.

---

## 2. 산업 구조 — 돈이 어떻게 도는가

| 밸류체인 단계 | 하는 일 | 대표 플레이어 유형 | 이 단계의 진입장벽 |
|----------------|---------|----------------------|----------------------|
| 원천 데이터 (업스트림) | 기업 재무제표·시장가격·소유구조·원자재 가격 등 원천 데이터 생성·공시 | 증권거래소, 규제 공시 시스템(SEC EDGAR 등), 1차 데이터 벤더 | 낮음 — 공개 데이터 원천 자체는 접근이 제한적이지 않음 |
| **가공·분석 (이 섹터)** | 원천 데이터를 신용등급·지수·벤치마크·리서치/분석 플랫폼으로 가공 | 신용평가사(예: S&P Global Ratings, Moody's), 지수 사업자(예: S&P Dow Jones Indices, MSCI, FTSE Russell), 데이터·분석 플랫폼(예: S&P Global Market Intelligence, FactSet) | 규제 지정(NRSRO 등)에 따른 진입 제한, 브랜드 신뢰(수십 년간 쌓인 등급·지수의 시장 표준 지위), 전환비용(투자 워크플로·펀드 상품 설계에 내재화), 네트워크 효과(벤치마크로 널리 쓰일수록 더 많은 자금이 추종) |
| 유통·최종 수요 (다운스트림) | 등급·지수·분석 상품을 실제로 소비 | 자산운용사(패시브 펀드가 지수를 추종), 은행·보험사(규제자본 산정에 등급 활용), 발행기업(채권 발행 시 등급 필요), 규제당국 | — |

> 개별 회사의 진입장벽(브랜드/전환비용/네트워크 효과/규모의 경제)이 구체적으로 무엇인지는 각 회사 `07_investment.md`에서 다룬다. 여기서는 산업 단계별 장벽의 일반적 성격만 서술.

---

## 3. 시장 규모 / 성장 동력

- **신용평가(Credit Rating) 시장**: 약 $7.77B(2026E) → $13.07B(2035E), CAGR 6.1%(Market Research Future). 신용평가 외 개인·기업 신용조회를 포함하는 더 넓은 정의의 "Credit Agency" 시장은 $12.89B(2025) → $20.88B(2035), CAGR 4.94%로 다르게 집계되기도 한다 — 후자는 소비자 신용조회(credit bureau) 매출까지 포함해 정의 자체가 다르므로 직접 비교하지 않는다.
- **금융 데이터·분석(Financial Data & Analytics) 시장**: 리서치 기관마다 정의(포함 범위)가 크게 갈려 $16~18B(2025~2026, 좁은 정의)부터 $67B(2025, 넓은 정의) 이상까지 편차가 크다. 회사 매출과 비교할 때는 반드시 어느 정의를 쓴 추정치인지 확인한 뒤 인용할 것 — 단일 숫자로 단정하지 않는다.
- **지수(Index/Benchmark) 라이선싱 시장**: 2023년 기준 지수 산업 매출 약 $6.5B, 영업이익률 60~70%대로 추정(Oxford Law Blogs 인용). S&P 500 한 지수에만 $4T 이상의 자금이 추종하는 등, 소수 벤치마크에 대규모 자금이 집중되는 구조.
- **참고 지표 — 글로벌 회사채 발행 규모**: 2025년 글로벌 회사채·신디케이트론 합산 발행액이 약 $13.7T(회사채 $6.8T + 신디케이트론 $7T)로 사상 최대치를 기록. 이는 산업 TAM이 아니라 신용평가 부문 매출의 물량 기반(volume base)을 보여주는 참고 지표.
- **핵심 성장 동력**:
  1. **글로벌 채권 발행 잔액의 구조적 증가** — 신흥국 자본시장 발달, 회사채 시장 확대로 등급이 필요한 발행 물량 자체가 장기적으로 늘어남.
  2. **패시브 투자로의 자금 이동 지속** — ETF·인덱스펀드로의 자금 유입이 이어지는 한, 자산 기준(asset-based) 라이선싱 수수료를 받는 지수 사업자 매출이 함께 성장.
  3. **규제상 데이터·리스크 분석 수요 확대** — 은행 자본규제, ESG 공시 의무화 등 규제 요구가 늘수록 분석 데이터 상품 수요도 함께 증가.
  4. **사모시장(Private Markets) 데이터 서비스 신규 수요** — 전통적으로 데이터가 부족했던 사모대출·사모주식 영역에 데이터·분석 상품을 새로 파는 기회.

Sources: [Credit Agency Market Size — Market Research Future](https://www.marketresearchfuture.com/reports/credit-agency-market-24072) · [Financial Analytics Market — Fortune Business Insights](https://www.fortunebusinessinsights.com/financial-analytics-market-107948) · [Can you take me higher? — Oxford Law Blogs](https://blogs.law.ox.ac.uk/oblb/blog-post/2024/06/can-you-take-me-higher-how-big-three-benefit-dominance-index-providers) · [Corporate Debt Market Outlook — OECD Global Debt Report 2026](https://www.oecd.org/en/publications/global-debt-report-2026_e9d80efd-en/full-report/corporate-debt-market-outlook-in-a-transforming-world_cf86a220.html)

---

## 4. 구조적 리스크 / 경기 민감도

| 리스크 유형 | 내용 | 관찰 가능한 신호 |
|--------------|------|----------------------|
| 채권 발행량의 경기·금리 민감도 | 신용평가 부문 매출 상당 부분이 신규 채권 발행 시 부과되는 거래 수수료(transaction fee)라, 금리 상승기·경기 침체기에 발행이 위축되면 매출도 함께 둔화 | 글로벌 회사채·하이일드 발행량, 신용스프레드, 정책금리 사이클 |
| 규제 지정에 의존하는 진입장벽의 정치적 리스크 | NRSRO 지정(미국), EU Benchmark Regulation 같은 규제가 소수 사업자의 과점 구조를 사실상 뒷받침하는데, 규제 완화·반독점 조치가 나오면 장벽 자체가 흔들릴 수 있음 | SEC·EU의 신용평가/벤치마크 규제 개정 동향, 반독점 조사·소송 |
| 사모신용시장 성장에 따른 탈중개화 | 사모대출(private credit)의 상당수가 공개 신용등급 없이 이루어지며, 이 시장이 커질수록 전통 신용평가 사업의 상대적 커버리지가 축소될 수 있음 | 사모신용시장(Private Credit) AUM 증가율, 무등급(unrated) 발행 비중 |
| 패시브 투자 둔화·자체 지수화(self-indexing) 리스크 | 지수 라이선싱 매출은 벤치마크에 연동된 자산(AUM) 규모에 좌우되므로, 패시브 자금 유입이 꺾이거나 대형 자산운용사가 라이선스 비용을 피해 자체 지수로 전환하면 매출 기반이 흔들림 | ETF·인덱스펀드 순유입 추이, 대형 운용사의 자체 지수 채택 사례 |
| 데이터·라이선싱 수수료에 대한 규제·반독점 압력 | 지수·데이터 라이선싱 요금이 패시브 펀드 보수 인하를 막는다는 지적이 반복되며, 공정·비차별 라이선싱 요구(MiFIR 등) 강화 가능성이 매출 성장률을 제약할 수 있음 | EU/미국 반독점 당국의 데이터·지수 라이선싱 조사, 관련 입법 동향 |

> 개별 회사의 Bull/Bear Case는 각 회사 `07_investment.md`에서 다룬다. 여기서는 섹터 전체가 함께 노출되는 리스크만 남긴다.

---

## 5. 이 섹터를 볼 때 체크하는 지표 / 신호

- **글로벌 회사채·하이일드 발행량 및 신용스프레드** — 신용평가 부문 매출의 직접 선행지표
- **ETF·인덱스펀드 순자산·순유입(AUM flow)** — 지수 라이선싱 매출의 직접 선행지표
- **정책금리·장기금리 사이클** — 채권 발행 유인에 직접 영향을 미쳐 신용평가 부문 물량을 좌우
- **사모신용시장(Private Credit) AUM 성장률과 무등급 발행 비중** — 탈중개화 리스크의 진행 정도를 보여주는 신호
- **주요국 신용평가·벤치마크 규제 입법 동향(미국 SEC, EU BMR/MiFIR)** — 이 산업의 진입장벽이 유지되는지 여부를 가르는 핵심 변수

---

## 관련 문서

- [S&P Global 개요](./sp_global/01_overview.md)

---

## 참고 자료

- [Credit Agency Market Size, Share and Industry Trends 2035 — Market Research Future](https://www.marketresearchfuture.com/reports/credit-agency-market-24072)
- [Financial Analytics Market Size, Share | Trends Report — Fortune Business Insights](https://www.fortunebusinessinsights.com/financial-analytics-market-107948)
- [Can you take me higher? How the Big Three benefit from the dominance of index providers — Oxford Law Blogs](https://blogs.law.ox.ac.uk/oblb/blog-post/2024/06/can-you-take-me-higher-how-big-three-benefit-dominance-index-providers)
- [Corporate debt market outlook in a transforming world: Global Debt Report 2026 — OECD](https://www.oecd.org/en/publications/global-debt-report-2026_e9d80efd-en/full-report/corporate-debt-market-outlook-in-a-transforming-world_cf86a220.html)
- [Why Is the Oligopoly in the Credit-Rating Market So Tenacious? — International Banker](https://internationalbanker.com/finance/why-is-the-oligopoly-in-the-credit-rating-market-so-tenacious/)
- [Report on Vulnerabilities in Private Credit (2026-05-06) — Financial Stability Board](https://www.fsb.org/uploads/P060526.pdf)

---

*작성일: 2026-08-17*
