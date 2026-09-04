# 스킬 작성 가이드

이 문서는 Anthropic의 [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)를 한국어로 정리한 것입니다. `.claude/skills/` 아래의 스킬(`SKILL.md`·`reference/`)을 만들거나 고칠 때 따르는 규칙이자, 저장소 주인이 "에이전트에게 지시를 어떻게 써야 잘 먹히는가"를 익히려고 읽는 학습 문서이기도 합니다.

---

## 핵심 원칙

### 1. 간결함이 전부다

**컨텍스트 윈도우는 공용 자원입니다.** 스킬은 시스템 프롬프트·대화 기록·다른 스킬의 메타데이터·사용자의 실제 요청과 같은 공간을 나눠 씁니다.

모든 토큰이 즉시 비용이 되는 건 아닙니다. 시작 시점에 미리 올라가는 건 **모든 스킬의 메타데이터(`name`·`description`)뿐**이고, `SKILL.md` 본문은 그 스킬이 관련 있다고 판단됐을 때, 나머지 파일은 실제로 필요할 때 읽힙니다. 그래도 `SKILL.md`의 간결함은 여전히 중요합니다 — 한 번 로드되면 그 안의 모든 토큰이 대화 기록·다른 컨텍스트와 자리를 다투기 때문입니다.

**기본 전제: Claude는 이미 똑똑하다.** Claude가 갖고 있지 않은 맥락만 추가하고, 문장마다 따져보세요.

- "이 설명이 정말 필요한가?"
- "Claude가 이미 아는 내용이라고 가정해도 되나?"
- "이 문단이 토큰값을 하나?"

**좋은 예 (약 50토큰):**

````markdown
## PDF 텍스트 추출

pdfplumber를 쓴다:

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
````

**나쁜 예 (약 150토큰):**

```markdown
## PDF 텍스트 추출

PDF(Portable Document Format)는 텍스트·이미지 등을 담는 흔한 파일 형식입니다.
PDF에서 텍스트를 뽑으려면 라이브러리가 필요합니다. PDF 처리 라이브러리는 여러 가지가
있지만 pdfplumber가 쓰기 쉽고 대부분의 경우를 잘 처리해서 추천합니다.
먼저 pip으로 설치해야 하고, 그다음 아래 코드를 쓰면 됩니다...
```

간결한 쪽은 "PDF가 무엇인지", "라이브러리가 어떻게 동작하는지"를 Claude가 이미 안다고 가정합니다.

### 2. 자유도를 작업에 맞춰 정한다

작업이 **얼마나 깨지기 쉬운지, 얼마나 상황마다 달라지는지**에 맞춰 지시의 구체성을 정합니다.

| 자유도 | 형태 | 쓰는 상황 |
| --- | --- | --- |
| **높음** | 서술형 지침 | 여러 접근이 모두 유효하고, 판단이 맥락에 달렸고, 휴리스틱이 방향만 잡아주면 될 때 |
| **중간** | 의사코드 · 파라미터가 있는 스크립트 | 선호하는 패턴이 있지만 변형이 허용되고, 설정에 따라 동작이 달라질 때 |
| **낮음** | 정확한 스크립트, 파라미터 거의 없음 | 작업이 깨지기 쉽고, 일관성이 중요하고, 정해진 순서를 반드시 지켜야 할 때 |

**높은 자유도 예시:**

```markdown
## 코드 리뷰 절차

1. 코드 구조와 구성을 분석한다
2. 잠재적 버그·엣지 케이스를 확인한다
3. 가독성·유지보수성 개선을 제안한다
4. 프로젝트 관례를 따르는지 확인한다
```

**낮은 자유도 예시:**

````markdown
## DB 마이그레이션

정확히 이 스크립트를 실행한다:

```bash
python scripts/migrate.py --verify --backup
```

명령을 수정하거나 플래그를 추가하지 말 것.
````

**비유:** Claude를 길을 걷는 로봇이라고 생각하세요.

- **양옆이 낭떠러지인 좁은 다리** — 안전한 길이 하나뿐입니다. 구체적인 가드레일과 정확한 지시를 주세요(낮은 자유도). 예: 순서를 반드시 지켜야 하는 DB 마이그레이션.
- **장애물 없는 벌판** — 성공에 이르는 길이 여럿입니다. 방향만 주고 나머지는 맡기세요(높은 자유도). 예: 맥락이 최선의 접근을 결정하는 코드 리뷰.

### 3. 실제로 쓸 모든 모델에서 테스트한다

스킬은 모델에 얹히는 추가물이라, 효과는 기반 모델에 따라 달라집니다. 쓸 예정인 모델 전부에서 시험해 보세요.

- **Haiku**(빠르고 저렴) — 지침이 충분히 상세한가?
- **Sonnet**(균형) — 지침이 명확하고 효율적인가?
- **Opus**(강한 추론) — 설명이 과하지 않은가?

Opus에서 완벽한 스킬이 Haiku에서는 설명이 더 필요할 수 있습니다. 여러 모델에서 쓸 거라면 모두에서 무난하게 동작하는 수준을 목표로 하세요.

---

## 스킬 구조

### YAML frontmatter 규칙

`SKILL.md`의 frontmatter는 두 필드를 요구합니다.

**`name`**

- 최대 64자
- 소문자·숫자·하이픈만 사용
- XML 태그 불가
- 예약어(`anthropic`, `claude`) 사용 불가

**`description`**

- 비어 있으면 안 됨
- 최대 1,024자
- XML 태그 불가
- **무엇을 하는지 + 언제 쓰는지**를 모두 담을 것

### 이름 짓기

**동명사형(verb + -ing)**을 권장합니다 — 그 스킬이 제공하는 활동·능력을 그대로 드러내기 때문입니다.

- **좋음(동명사):** `processing-pdfs`, `analyzing-spreadsheets`, `managing-databases`, `testing-code`, `writing-documentation`
- **허용:** 명사구(`pdf-processing`, `spreadsheet-analysis`), 행위형(`process-pdfs`, `analyze-spreadsheets`)
- **피할 것:** 모호한 이름(`helper`, `utils`, `tools`), 지나치게 일반적인 이름(`documents`, `data`, `files`), 예약어(`claude-tools`), **스킬 모음 안에서 규칙이 제각각인 것**

### `description` 쓰기 — 스킬 선택을 좌우하는 한 줄

Claude는 100개가 넘을 수도 있는 스킬 중에서 **`description`만 보고** 어느 것을 쓸지 고릅니다. 나머지 `SKILL.md`는 고르고 난 뒤의 구현 지침입니다.

**항상 3인칭으로 씁니다.** `description`은 시스템 프롬프트에 주입되므로 시점이 섞이면 스킬 탐색이 어긋납니다.

- ✅ "Processes Excel files and generates reports"
- ❌ "I can help you process Excel files"
- ❌ "You can use this to process Excel files"

> 한국어로 쓸 때도 같은 취지입니다 — "제가 도와드립니다" 같은 화자 시점 대신 **스킬이 하는 일과 발동 조건**을 서술합니다.

**구체적으로, 핵심 용어를 포함해서** 씁니다.

```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

```yaml
description: Analyze Excel spreadsheets, create pivot tables, generate charts. Use when analyzing Excel files, spreadsheets, tabular data, or .xlsx files.
```

```yaml
description: Generate descriptive commit messages by analyzing git diffs. Use when the user asks for help writing commit messages or reviewing staged changes.
```

이런 건 피합니다: `Helps with documents` / `Processes data` / `Does stuff with files`.

### 점진적 공개(progressive disclosure)

`SKILL.md`는 **목차 역할**을 하고, 상세한 자료는 필요할 때 읽히는 별도 파일로 내립니다.

- `SKILL.md` 본문은 **500줄 이내**로 유지
- 한계에 가까워지면 내용을 별도 파일로 분리
- 디렉터리 예시:

```
pdf/
├── SKILL.md        # 주 지침 (트리거될 때 로드)
├── FORMS.md        # 폼 작성 가이드 (필요할 때만)
├── reference.md    # API 레퍼런스 (필요할 때만)
├── examples.md     # 사용 예시 (필요할 때만)
└── scripts/
    ├── analyze_form.py   # 실행되는 스크립트 (로드되지 않음)
    ├── fill_form.py
    └── validate.py
```

**패턴 1 — 개요 + 참조 링크**

````markdown
---
name: pdf-processing
description: Extracts text and tables from PDF files, fills forms, and merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---

# PDF Processing

## Quick start

pdfplumber로 텍스트 추출:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Advanced features

**Form filling**: [FORMS.md](FORMS.md)
**API reference**: [REFERENCE.md](REFERENCE.md)
**Examples**: [EXAMPLES.md](EXAMPLES.md)
````

**패턴 2 — 도메인별 분리**

여러 도메인을 다루는 스킬은 도메인별로 파일을 나눠 **관련 없는 맥락이 딸려 들어오지 않게** 합니다. 매출 지표를 물었을 때 재무 스키마만 읽고 마케팅·영업 데이터는 건드리지 않게 되는 식입니다.

```
bigquery-skill/
├── SKILL.md            # 개요와 길잡이
└── reference/
    ├── finance.md      # 매출·빌링 지표
    ├── sales.md        # 파이프라인·기회
    ├── product.md      # API 사용량·기능
    └── marketing.md    # 캠페인·어트리뷰션
```

**패턴 3 — 조건부 상세**

기본 내용만 본문에 두고, 특수한 경우만 링크로 내립니다.

```markdown
# DOCX Processing

## 문서 생성

새 문서는 docx-js를 쓴다. [DOCX-JS.md](DOCX-JS.md) 참고.

## 문서 편집

간단한 편집은 XML을 직접 수정한다.

**변경 이력(tracked changes)이 필요하면**: [REDLINING.md](REDLINING.md)
**OOXML 세부 사항**: [OOXML.md](OOXML.md)
```

### 참조는 한 단계까지만

참조 파일이 또 다른 파일을 참조하면, Claude는 그 파일을 `head -100` 같은 방식으로 **일부만 훑고 지나갈 수 있습니다.** 그러면 정보가 반쪽만 들어옵니다.

**모든 참조 파일은 `SKILL.md`에서 직접 링크되게 두세요.**

- ❌ `SKILL.md` → `advanced.md` → `details.md` (진짜 내용은 여기)
- ✅ `SKILL.md` → `advanced.md` / `reference.md` / `examples.md` (전부 한 단계)

### 100줄 넘는 참조 파일에는 목차를 단다

부분적으로만 읽히더라도 어떤 내용이 있는지 전체 범위가 보이게 하려는 것입니다.

```markdown
# API Reference

## Contents
- 인증과 초기 설정
- 핵심 메서드 (create, read, update, delete)
- 고급 기능 (배치 작업, 웹훅)
- 에러 처리 패턴
- 코드 예시

## 인증과 초기 설정
...
```

---

## 워크플로와 피드백 루프

### 복잡한 작업은 워크플로로 쪼갠다

단계를 명확한 순서로 나누고, 특히 복잡하면 **Claude가 응답에 복사해 체크해 나갈 체크리스트**를 제공합니다.

````markdown
## 리서치 종합 워크플로

이 체크리스트를 복사해 진행 상황을 표시할 것:

```
Research Progress:
- [ ] 1단계: 모든 원자료 읽기
- [ ] 2단계: 핵심 주제 식별
- [ ] 3단계: 주장 교차 검증
- [ ] 4단계: 구조화된 요약 작성
- [ ] 5단계: 인용 검증
```

**1단계: 모든 원자료 읽기**
`sources/` 폴더의 각 문서를 검토하고 주요 논지와 근거를 적는다.

...

**5단계: 인용 검증**
모든 주장이 올바른 출처를 가리키는지 확인한다. 인용이 불완전하면 3단계로 돌아간다.
````

코드가 없는 분석 작업에도 그대로 통합니다. 단계가 명확하면 Claude가 검증 단계를 건너뛰지 않습니다.

### 피드백 루프를 넣는다

**검증기 실행 → 오류 수정 → 반복.** 이 패턴 하나로 결과 품질이 크게 올라갑니다.

**코드 없는 예 — 스타일 가이드 준수**

```markdown
## 콘텐츠 검토 절차

1. STYLE_GUIDE.md에 따라 초안을 쓴다
2. 체크리스트와 대조한다
   - 용어 일관성
   - 예시가 표준 형식을 따르는지
   - 필수 절이 모두 있는지
3. 문제가 있으면
   - 각 문제를 해당 절과 함께 적는다
   - 내용을 고친다
   - 체크리스트를 다시 확인한다
4. 모든 요건을 만족했을 때만 다음으로 넘어간다
5. 최종본을 저장한다
```

여기서 "검증기"는 스크립트가 아니라 `STYLE_GUIDE.md`이고, 대조 작업은 Claude가 읽고 비교하며 수행합니다.

**코드 있는 예 — 문서 편집**

```markdown
1. `word/document.xml`을 수정한다
2. **즉시 검증**: `python ooxml/scripts/validate.py unpacked_dir/`
3. 검증 실패 시: 에러 메시지를 확인 → XML 수정 → 재검증
4. **검증을 통과했을 때만** 다음으로 진행
5. 재패킹: `python ooxml/scripts/pack.py unpacked_dir/ output.docx`
6. 산출 문서를 확인한다
```

---

## 콘텐츠 지침

### 시점에 의존하는 정보를 넣지 않는다

**나쁜 예** (언젠가 틀린 말이 됨):

```markdown
2025년 8월 이전이면 구 API를, 이후면 신 API를 쓴다.
```

**좋은 예** ("옛 패턴" 절로 분리):

```markdown
## 현재 방식

v2 엔드포인트를 쓴다: `api.example.com/v2/messages`

## 옛 패턴

<details>
<summary>레거시 v1 API (2025-08 지원 종료)</summary>

v1은 `api.example.com/v1/messages`를 썼다. 더 이상 지원되지 않는다.
</details>
```

이렇게 하면 본문을 어지럽히지 않으면서 과거 맥락을 남길 수 있습니다.

### 용어를 하나로 고정한다

한 스킬 안에서 같은 대상은 항상 같은 말로 부릅니다.

- ✅ 항상 "API endpoint", 항상 "field", 항상 "extract"
- ❌ "API endpoint"·"URL"·"API route"·"path"를 섞어 쓰기 / "extract"·"pull"·"get"·"retrieve" 섞어 쓰기

---

## 자주 쓰는 패턴

### 템플릿 패턴

출력 형식을 템플릿으로 주되, **엄격함의 수준을 목적에 맞춥니다.**

- **엄격해야 할 때**(API 응답·데이터 포맷): "ALWAYS use this exact template structure"라고 못 박습니다.
- **유연해도 될 때:** "기본 형식이며 분석에 맞게 판단해서 조정할 것"이라고 명시합니다.

### 예시 패턴

출력 품질이 "본 적 있는 예"에 달린 작업은 **입력/출력 쌍**을 그대로 보여줍니다. 일반 프롬프팅과 같습니다.

````markdown
## 커밋 메시지 형식

**예시 1**
입력: JWT 토큰 기반 사용자 인증 추가
출력:
```
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
```

**예시 2**
입력: 리포트에서 날짜가 잘못 표시되던 버그 수정
출력:
```
fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation
```
````

설명을 늘어놓는 것보다 예시 두세 개가 원하는 문체와 상세도를 훨씬 정확하게 전달합니다.

### 조건부 분기 패턴

판단이 갈리는 지점을 명시적으로 표시합니다.

```markdown
1. 수정 유형을 판단한다
   **새로 만드는가?** → 아래 "생성 워크플로"
   **기존 것을 고치는가?** → 아래 "편집 워크플로"
```

워크플로가 커지거나 단계가 많아지면 **별도 파일로 내리고, 작업에 맞는 파일을 읽으라고 지시**하세요.

---

## 평가와 반복

### 평가(evaluation)를 먼저 만든다

**긴 문서를 쓰기 전에 평가부터 만듭니다.** 그래야 상상 속 문제가 아니라 실제 문제를 푸는 스킬이 됩니다.

1. **격차 파악** — 스킬 없이 대표적인 작업을 시켜 보고, 실패하거나 맥락이 빠진 지점을 기록한다
2. **평가 작성** — 그 격차를 겨냥한 시나리오 3개를 만든다
3. **베이스라인 측정** — 스킬 없는 상태의 성능을 기록한다
4. **최소한의 지침 작성** — 격차를 메우고 평가를 통과할 만큼만 쓴다
5. **반복** — 평가를 돌려 베이스라인과 비교하고 다듬는다

평가 구조 예시:

```json
{
  "skills": ["pdf-processing"],
  "query": "Extract all text from this PDF file and save it to output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "적절한 PDF 처리 라이브러리·CLI 도구로 파일을 읽는다",
    "모든 페이지의 텍스트를 빠짐없이 추출한다",
    "추출 결과를 읽기 좋은 형태로 output.txt에 저장한다"
  ]
}
```

> 이 평가를 돌려주는 기본 제공 도구는 아직 없습니다 — 각자 실행 방식을 만들어 씁니다. 그래도 평가는 스킬 효과를 재는 유일한 기준선입니다.

### Claude와 함께 반복해서 개발한다

가장 효과적인 방식은 **Claude A**(스킬을 같이 설계·수정하는 인스턴스)와 **Claude B**(그 스킬을 실제로 써서 일하는 새 인스턴스)를 나누는 것입니다.

**새 스킬 만들기**

1. **스킬 없이 한 번 해본다** — 평소처럼 프롬프트로 작업하면서, 내가 **반복해서 제공하는 맥락**이 무엇인지 관찰한다
2. **재사용 가능한 패턴을 추린다** — 다음에도 필요할 맥락(테이블 이름, 필드 정의, "테스트 계정은 항상 제외" 같은 규칙)을 정리한다
3. **Claude A에게 스킬로 만들어 달라고 한다** — Claude는 스킬 형식을 이미 알고 있어서, 별도의 "스킬 작성용 스킬" 없이도 올바른 frontmatter와 본문을 만들어 냅니다
4. **간결성 검토** — 불필요한 설명을 지운다("win rate가 뭔지 설명하는 부분 빼줘. Claude는 이미 알아")
5. **정보 구조 개선** — "테이블 스키마는 별도 참조 파일로 빼줘. 나중에 테이블이 더 늘 것 같아"
6. **비슷한 작업에서 테스트** — 스킬을 로드한 새 인스턴스(Claude B)로 실제 작업을 시켜 본다
7. **관찰 결과로 반복** — "Claude가 이 스킬을 쓸 때 4분기 날짜 필터를 빠뜨렸어. 날짜 필터 절을 넣을까?"

**기존 스킬 개선하기**도 같은 구조입니다. 실제 업무에서 Claude B에게 시키고 → 어디서 헤매는지 관찰하고 → Claude A에게 현재 `SKILL.md`와 관찰 내용을 주며 개선을 요청합니다. Claude A는 규칙을 더 눈에 띄는 위치로 옮기거나, "always" 대신 "MUST" 같은 강한 표현을 쓰거나, 워크플로 구조를 바꾸는 식으로 제안합니다.

**왜 이게 통하는가:** Claude A는 에이전트에게 필요한 정보가 무엇인지 알고, 사람은 도메인 지식을 대며, Claude B는 실제 사용에서 격차를 드러냅니다 — 추측이 아니라 관찰된 행동으로 스킬이 개선됩니다.

### Claude가 스킬을 어떻게 돌아다니는지 관찰한다

- **예상 밖의 탐색 경로** — 생각지 못한 순서로 파일을 읽는다면 구조가 직관적이지 않다는 신호
- **놓친 연결** — 중요한 파일 참조를 따라가지 않는다면 링크가 더 눈에 띄어야 한다는 뜻
- **특정 파일에만 과의존** — 같은 파일을 매번 읽는다면 그 내용은 `SKILL.md` 본문에 있어야 할지 모른다
- **아예 안 읽히는 파일** — 불필요하거나, 본문에서 신호가 약한 것

`name`과 `description`은 특히 중요합니다 — 스킬 발동 여부가 이 둘로 결정됩니다.

---

## 피해야 할 안티패턴

### Windows 스타일 경로

파일 경로는 항상 슬래시(`/`)로 씁니다.

- ✅ `scripts/helper.py`, `reference/guide.md`
- ❌ `scripts\helper.py`, `reference\guide.md`

### 선택지를 너무 많이 주는 것

- ❌ "pypdf를 쓰거나, pdfplumber를 쓰거나, PyMuPDF를 쓰거나, pdf2image를 쓰거나..."
- ✅ **기본값 하나 + 탈출구:** "텍스트 추출은 pdfplumber를 쓴다. 스캔된 PDF로 OCR이 필요하면 pdf2image + pytesseract를 쓴다."

### 도구가 설치돼 있다고 가정하는 것

- ❌ "PDF 라이브러리로 파일을 처리한다"
- ✅ "필요 패키지 설치: `pip install pypdf` — 그다음 아래처럼 쓴다"

---

## 고급: 실행 가능한 코드가 포함된 스킬

마크다운 지침만 있는 스킬이라면 이 절은 건너뛰어도 됩니다.

### 미루지 말고 해결한다 (Solve, don't defer)

스크립트는 오류 상황을 **스스로 처리**해야 합니다. Claude에게 떠넘기지 마세요.

```python
def process_file(path):
    """파일을 처리하고, 없으면 만들어서 진행한다."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {path} not found, creating default")
        with open(path, "w") as f:
            f.write("")
        return ""
    except PermissionError:
        print(f"Cannot access {path}, using default")
        return ""
```

설정값도 근거를 남깁니다 — 이른바 "부두 상수(voodoo constants)"를 두지 않습니다(Ousterhout's law). **작성자도 모르는 값을 Claude가 어떻게 정하겠습니까?**

```python
# HTTP 요청은 보통 30초 안에 끝난다
# 느린 연결을 감안해 여유를 둔 값
REQUEST_TIMEOUT = 30

# 재시도 3회는 신뢰성과 속도의 절충
# 일시적 실패는 대개 두 번째 시도에서 해소된다
MAX_RETRIES = 3
```

❌ `TIMEOUT = 47  # 왜 47?` / `RETRIES = 5  # 왜 5?`

### 유틸리티 스크립트를 미리 만들어 둔다

Claude가 그때그때 코드를 쓸 수 있더라도, 미리 만든 스크립트가 낫습니다.

- 생성 코드보다 **신뢰성**이 높다
- **토큰 절약** — 코드를 컨텍스트에 넣을 필요가 없다
- **시간 절약** — 코드 생성 과정이 없다
- **일관성** — 쓸 때마다 같은 결과

**실행할 것인지 읽을 것인지 명시하세요.**

- 실행(대부분): "필드를 뽑으려면 `analyze_form.py`를 실행한다"
- 참조용 읽기(복잡한 로직): "필드 추출 알고리즘은 `analyze_form.py`를 참고한다"

### 시각적 분석을 활용한다

입력을 이미지로 렌더링할 수 있으면, 그 이미지를 Claude가 직접 보게 하세요(예: PDF → 이미지 변환 후 폼 필드 위치·유형 파악). 레이아웃·구조 분석에 유효합니다.

### 검증 가능한 중간 산출물을 만든다

복잡하고 열린 작업에서는 **계획 → 검증 → 실행(plan-validate-execute)** 패턴이 오류를 일찍 잡습니다.

예를 들어 스프레드시트를 근거로 PDF 폼 50개 필드를 갱신한다면, 없는 필드를 참조하거나 값이 충돌하거나 필수 항목을 빠뜨릴 수 있습니다. 중간에 `changes.json` 같은 **계획 파일**을 만들고 스크립트로 검증한 뒤 적용하면 됩니다: 분석 → **계획 파일 작성** → **계획 검증** → 실행 → 확인.

- **오류를 일찍 잡는다** — 변경이 적용되기 전에 문제를 발견
- **기계 검증이 가능하다** — 스크립트가 객관적으로 확인
- **되돌리기 쉽다** — 원본을 건드리지 않고 계획만 고쳐 반복
- **디버깅이 쉽다** — 에러 메시지가 문제 지점을 정확히 가리킨다

배치 작업·파괴적 변경·복잡한 검증 규칙·실수 비용이 큰 작업에 씁니다. 검증 스크립트의 에러 메시지는 **수다스럽게** 만드세요: "Field 'signature_date' not found. Available fields: customer_name, order_total, signature_date_signed".

### 패키지 의존성

스킬은 코드 실행 환경에서 돌아가며 플랫폼별 제약이 있습니다.

- **claude.ai** — npm·PyPI 설치, GitHub 저장소 가져오기 가능
- **Claude API** — 네트워크 접근 없음, 런타임 패키지 설치 없음

필요한 패키지는 `SKILL.md`에 명시하고, 실행 환경에서 실제로 쓸 수 있는지 확인하세요.

### 런타임 환경이 작성 방식에 미치는 영향

1. **메타데이터는 미리 로드** — 모든 스킬의 `name`·`description`이 시작 시 시스템 프롬프트에 들어간다
2. **파일은 필요할 때 읽힘** — `SKILL.md`와 나머지 파일은 필요한 시점에 파일시스템에서 읽는다
3. **스크립트는 실행만 됨** — 내용이 컨텍스트에 올라가지 않고 **출력만** 토큰을 쓴다
4. **큰 파일에 컨텍스트 페널티가 없다** — 참조 문서·데이터는 실제로 읽히기 전까지 토큰을 쓰지 않는다

따라서:

- **경로 표기가 중요하다** — `reference/guide.md` (역슬래시 금지)
- **파일명을 내용이 드러나게** — `doc2.md` ❌ / `form_validation_rules.md` ✅
- **탐색하기 좋게 구성** — `reference/finance.md`·`reference/sales.md` ✅ / `docs/file1.md` ❌
- **자료는 넉넉히 번들해도 된다** — 완전한 API 문서·풍부한 예시·큰 데이터셋 모두 읽히기 전엔 공짜
- **결정적 작업은 스크립트로** — Claude에게 검증 코드를 생성시키기보다 `validate_form.py`를 써 둔다
- **실행/참조 의도를 명시**하고, **실제 요청으로 탐색 경로를 시험**한다

### MCP 도구는 정규화된 이름으로

`서버이름:도구이름` 형식으로 씁니다.

```markdown
Use the BigQuery:bigquery_schema tool to retrieve table schemas.
Use the GitHub:create_issue tool to create issues.
```

서버 접두어가 없으면, 특히 MCP 서버가 여러 개일 때 도구를 못 찾을 수 있습니다.

---

## 발행 전 체크리스트

**기본 품질**

- [ ] `description`이 구체적이고 핵심 용어를 포함한다
- [ ] `description`에 **무엇을 하는지 + 언제 쓰는지**가 모두 있다
- [ ] `SKILL.md` 본문이 500줄 미만이다
- [ ] 상세 내용은 별도 파일로 분리돼 있다(필요한 경우)
- [ ] 시점에 의존하는 정보가 없다(있다면 "옛 패턴" 절에 있다)
- [ ] 용어가 일관된다
- [ ] 예시가 추상적이지 않고 구체적이다
- [ ] 파일 참조가 한 단계 깊이다
- [ ] 점진적 공개를 적절히 썼다
- [ ] 워크플로의 단계가 명확하다

**코드·스크립트**

- [ ] 스크립트가 문제를 미루지 않고 해결한다
- [ ] 오류 처리가 명시적이고 도움이 된다
- [ ] "부두 상수"가 없다(모든 값에 근거가 있다)
- [ ] 필요한 패키지를 명시했고 사용 가능한지 확인했다
- [ ] 스크립트에 사용법 설명이 있다
- [ ] Windows 스타일 경로가 없다
- [ ] 중요한 작업에 검증 단계가 있다
- [ ] 품질이 중요한 작업에 피드백 루프가 있다

**테스트**

- [ ] 평가 시나리오를 최소 3개 만들었다
- [ ] Haiku·Sonnet·Opus에서 테스트했다
- [ ] 실제 사용 시나리오로 테스트했다
- [ ] (해당되면) 팀 피드백을 반영했다

---

*작성일: 2026-09-04*
