# 주식 리서치 노트

개인 투자자가 **실제 투자 판단**을 위해 작성·갱신하는 주식 리서치 아카이브입니다. [VitePress](https://vitepress.dev/)로 빌드해 GitHub Pages로 배포합니다.

**🔗 사이트: https://parkgyeongtae.github.io/stock-research/**

## 구성

- `docs/sectors/` — 섹터별·회사별 리서치 문서. 회사마다 같은 파일 구성을 써서 회사 간 비교가 되도록 했습니다
- `docs/glossary.md`·`docs/concepts/`·`docs/macro/` — 용어집·개념 정리·거시지표 차트. 특정 회사·섹터에 종속되지 않는 참고 문서입니다
- `docs/authoring/` — 이 저장소의 문서를 만드는 규칙과 AI 활용 참고 자료 (아래 참고)
- `scripts/` — 차트 생성기와 SEC XBRL 재무 수치 추출기. 각 스크립트 상단 docstring이 사용법의 마스터입니다
- `.claude/skills/` — 문서를 만들거나 다시 만드는 절차를 코드화한 Claude Code 스킬
- `.github/workflows/deploy.yml` — `main`에 푸시하면 빌드 결과를 GitHub Pages로 자동 배포

폴더 구조와 파일별 역할의 상세는 [`authoring-guide.md`](./docs/authoring/authoring-guide.md)에만 적습니다 — 여기서 같은 내용을 되풀이하면 한쪽만 낡습니다.

## 규칙은 어디에 있나

- [`AGENTS.md`](./AGENTS.md) — **AI 에이전트 작업 지침이자 저장소의 중심 문서.** 어떤 규칙이 어느 파일에 사는지를 정리한 "단일 출처 지도"가 여기 있습니다 (`CLAUDE.md`는 이 파일의 심볼릭 링크)
- [`authoring-guide.md`](./docs/authoring/authoring-guide.md) — 폴더 구조·작성 규칙의 마스터
- [`chart-generation-guide.md`](./docs/authoring/chart-generation-guide.md) — 차트 생성 절차의 마스터
- [`skill-authoring-guide.md`](./docs/authoring/skill-authoring-guide.md) — 스킬 작성 규칙
- [`claude-code-guide.md`](./docs/authoring/claude-code-guide.md) · [`codex-guide.md`](./docs/authoring/codex-guide.md) — 외부 공식 문서의 한국어 정리 *(참고용, 이 저장소의 규칙은 아님)*

`AGENTS.md`만 저장소 루트에 있고 나머지는 `docs/authoring/`에 두어 사이트와 함께 발행합니다 — 어떤 규칙으로 이 문서들이 만들어졌는지 사이트에서 바로 읽기 위해서입니다.

## 로컬에서 실행

사이트는 Node, 스크립트는 파이썬([uv](https://docs.astral.sh/uv/))으로 돌립니다. 외부 파이썬 의존성은 없습니다(표준 라이브러리만 사용).

```bash
npm install
npm run dev           # http://localhost:5173/stock-research/ 에서 미리보기
npm run build         # 배포와 동일하게 정적 사이트 빌드 (docs/.vitepress/dist/)
```

```bash
uv run python scripts/gen_technical_chart.py --help
uv run python scripts/fetch_sec_facts.py --help
```
