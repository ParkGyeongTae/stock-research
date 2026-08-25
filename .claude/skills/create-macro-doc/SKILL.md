---
name: create-macro-doc
description: 아직 `docs/meta/macro/`에 없는 거시지표(환율·금리·지수·원자재·디지털자산)를 "새로 만들어줘", "차트 추가해줘", "macro에 <지표> 추가해줘" 처럼 요청할 때 사용한다. `scripts/gen_technical_chart.py`로 캔들 SVG를 생성하고(사용법은 `chart-generation-guide.md`), 상승/하락 해석 절과 카테고리별 `.pages` 등록까지 `authoring-guide.md`의 규칙대로 채운다. 이미 있는 macro 문서를 최신 데이터로 재생성하는 작업에는 쓰지 않는다 — 그건 `improve-macro-doc` 대상.
---

# 거시지표 참고 문서 신규 작성

## 언제 쓰나

- 대상: `docs/meta/macro/{foreign_exchange,rates,bonds,equities,metals,energy,cryptocurrency}/`에 아직 없는 새 자산·지표
- 트리거 예시: "위안화 환율 macro 문서 만들어줘", "나스닥 100 차트 추가해줘", "이더리움 거시 참고 문서 새로 만들어줘"
- **대상 아님**:
  - 이미 있는 macro 문서를 최신 데이터로 재생성 → `improve-macro-doc`
  - 회사 자체의 `09_technical_daily.md`·`10_technical_weekly.md` → `create-company-doc`/`improve-company-doc` 대상(같은 스크립트를 쓰지만 회사 폴더 소관)
  - `docs/index.md`·`AGENTS.md` 자체 개선 → `review-master-docs`

## 왜 필요한가

이 폴더의 문서들은 전부 같은 골격(차트 → 해석 참고 → 관련 문서 → 참고 자료)을 스크립트 하나로 공유한다. 손으로 새로 쓰면 차트에 쓰인 스윙 탐지 파라미터가 슬쩍 달라지거나(회사 문서와 비교가 깨짐), 상승/하락 해석 절을 빠뜨리거나, `.pages` 등록을 잊어 내비게이션에서 조용히 빠지기 쉽다. 이 스킬은 신규 작성 흐름 전체를 한 번에 강제한다.

> macro 문서는 원래 3. 지지선 / 저항선 요약(지지/저항 레벨 표)·4. 방법론 · 한계·"갱신 방법"(재생성 커맨드)까지 문서마다 그대로 담았으나, 회사 문서(`09_technical_daily.md`·`10_technical_weekly.md`)와 달리 여기서는 "차트+방향성 해석 중심의 가벼운 참고 자료"로 스코프를 좁히기로 했다(2026-08-20 3. 지지선 / 저항선 요약·4. 방법론 · 한계 제거, 2026-08-21 갱신 커맨드도 문서에서 빼고 `chart-generation-guide.md`(당시엔 `authoring-guide.md` 안) "macro 문서 재현 파라미터" 표로 통합). 지지/저항 레벨 자체는 차트 SVG 안에 점선으로 이미 표시되므로 정보가 사라지는 건 아니고, 표·수치·재생성 커맨드를 문서마다 반복하지 않을 뿐이다.

## 절차

1. **카테고리 폴더 확정**
   `docs/meta/macro/{foreign_exchange,rates,bonds,equities,metals,energy,cryptocurrency}/` 중 성격이 맞는 곳을 고른다. 일곱 개 중 어디에도 안 맞는 완전히 새로운 자산군이면 새 카테고리 폴더를 만들고 `docs/meta/macro/.pages`의 `nav:`에 추가한다 — 이 경우만 필요하고, 기존 카테고리에 문서만 추가할 땐 불필요하다.

2. **티커·파라미터 확인**
   Yahoo Finance 티커를 WebSearch로 확인한다(추측 금지 — 환율·선물·지수는 `KRW=X`, `GC=F`, `^TNX`처럼 비직관적인 표기가 많다). 주가가 아닌 시계열이면 `--symbol`·`--symbol-pos`·`--unit-label`·`--adj-note`가 필요하다 — 문법은 `chart-generation-guide.md` "주가가 아닌 시계열에 쓰기" 참고. 같은 카테고리의 기존 자산이 `chart-generation-guide.md` "macro 문서 재현 파라미터" 표에 이미 있으면(예: 환율이면 `usd_krw.md` 행) 그 옵션 패턴을 참고하면 빠르다.

3. **파일명 결정**
   snake_case, 카테고리 폴더의 기존 파일명 관례를 따른다(`usd_krw.md`, `treasury_10y.md`, `sp500.md` 등 — 티커가 아니라 사람이 읽는 이름).

4. **차트는 스크립트로 생성**
   ```bash
   uv run python scripts/gen_technical_chart.py "<TICKER>" --name "<한글명>" --interval 1wk \
     --unit-label "<단위>" --adj-note "<조정 여부 각주>" --close-on <YYYY-MM-DD> --emit chart
   ```
   `--emit chart`로 캔들 SVG만 뽑아 1. 차트 — 최근 5년 주봉에 그대로 옮긴다(지지/저항 표·방법론 텍스트는 이 문서에 넣지 않으므로 `table`·`facts`·`dates`는 필요 없다).

5. **문서 골격 채우기** — 기존 정리된 문서(예: `commodities/gold.md`)를 구조 기준으로 삼는다:
   - 제목 + intro 블록쿼트 1문장: 이 지표가 무엇의 프록시인지, 관련 문서와의 관계만 간결히 적는다. **아래 세 가지는 넣지 않는다** — 커버리지 연관성 경고, "객관적 서술이며 투자 판단이 아니다" 면책, 스크립트 공유 각주. 이 셋은 이미 전체 macro 문서에서 제거된 보일러플레이트이고, 마지막 것의 근거(회사 문서와 같은 스크립트를 쓰지만 `meta/`에 두는 이유)는 `authoring-guide.md` "📁 폴더 구조·명명 규칙"이 마스터라 각 문서에서 반복할 필요가 없다.
   - `## 1. 차트 — 최근 5년 주봉`
   - `## 2. 해석 참고 — 상승/하락이 의미하는 것` — **스크립트가 만들지 않는다. 사람이 직접 쓴다.** "**상승**: …", "**하락**: …" 두 불릿 + 해석이 갈리거나 다른 요인이 섞이는 경우의 한계를 짚는 불릿 하나(3번째 불릿). `commodities/*.md` 5개가 참고 예시다. 일반적·교과서적인 경제적 해석만 적고, 지금 이 시점의 가격 전망이나 투자 판단은 적지 않는다.
   - ⚠️ **intro 블록쿼트와 이 절에는 시점 종속 서술을 넣지 않는다** — 수치·날짜·순위·기간은 스크립트가 만드는 차트(와 비교 문서의 요약 표)에만 두고, 사람이 쓰는 산문은 재생성해도 고칠 필요가 없어야 한다. 금지 표현 목록과 조건부 서술로 바꾸는 예시는 `chart-generation-guide.md` "macro 문서의 산문은 시점에 종속되지 않게 씁니다"가 마스터다.
   - **`## 갱신 방법`은 넣지 않는다** — 재생성 커맨드(티커·옵션·조정 각주)는 문서에 남기지 않고 `chart-generation-guide.md` "macro 문서 재현 파라미터" 표에만 행으로 추가한다(6번 참고).
   - `## 관련 문서` — 같은 카테고리의 관련 자산(예: 은 문서는 금 문서를 링크), `docs/meta/concepts/macroeconomics.md`, `docs/meta/glossary.md` 앵커.
   - `## 참고 자료` — Yahoo Finance 등 데이터 출처 링크.
   - 문서 최하단 `*작성일: YYYY-MM-DD*` — 오늘 날짜는 세션 컨텍스트 `# currentDate` → `date +%Y-%m-%d` → 확인 불가 시 사용자에게 확인. 이후 수정 시 라벨·형식은 저장소 확정 규칙("최종 수정일:" — 날짜만, 무엇을 고쳤는지는 서술하지 않음)을 따른다.

6. **`chart-generation-guide.md` "macro 문서 재현 파라미터" 표에 행 추가**
   2번에서 확정한 티커·옵션·조정 각주를 표에 새 행으로 넣는다. 각주가 기존 코드(FUT/IDX/FX/ETF/YLD/DISC 등) 중 하나와 같은 문구면 그 코드를 재사용하고, 다르면 새 코드를 만들어 위 범례에도 추가한다.

7. **`.pages` 등록**
   해당 카테고리의 `.pages`(예: `docs/meta/macro/foreign_exchange/.pages`) `nav:`에 파일명을 추가한다. 빠뜨려도 빌드는 성공하지만 내비게이션에서 문서가 조용히 사라진다. 카테고리 폴더에 `.pages`가 아예 없으면(현재는 7개 카테고리 모두 갖추고 있으므로, 새 카테고리를 만든 경우에만 해당) 새로 만든다.

8. **다른 문서에서 인용할 곳이 있는지 확인**
   이 지표를 언급할 만한 기존 회사·섹터 문서가 있으면(예: 원자력 섹터 회사 문서에서 우라늄 가격 문서를 인용) 링크를 추가할지 사용자에게 확인한다 — 자동으로 끼워 넣지 않는다.

9. **마무리 체크리스트**
   - `uv run mkdocs build`로 깨진 링크(`unrecognized relative link`) 없는지 확인
   - `.pages` 등록 재확인
   - `chart-generation-guide.md` 표에 새 행이 실제로 들어갔는지, 문서 자체에는 재생성 커맨드가 없는지 확인
   - 2. 해석 참고 — 상승/하락이 의미하는 것이 전망이 아니라 일반적 해석으로 쓰였는지 재확인
   - 문서 최하단 작성일 표기 확인

## 하지 않는 것

- 특정 시점의 가격 전망이나 투자 판단 서술 — `AGENTS.md` "투자 권유가 아니다" 원칙
- 스윙 탐지·클러스터링 파라미터를 문서마다 다르게(직접 계산) 만드는 것 — 회사 문서(`09_technical_daily.md`·`10_technical_weekly.md`)와 비교 가능성이 깨진다
- 커밋·푸시 — `AGENTS.md` 커밋 정책대로 사용자가 명시적으로 요청할 때만

## 참고

- 폴더 구조·역할은 `authoring-guide.md`("📁 폴더 구조·명명 규칙"), 생성 커맨드 문법은 `chart-generation-guide.md`("주가가 아닌 시계열에 쓰기")가 마스터다 — 이 스킬은 신규 작성이라는 한 흐름 안에서 그 규칙들을 순서대로 적용할 뿐, 새 기준을 만들지 않는다.
