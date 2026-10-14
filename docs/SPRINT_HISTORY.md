# Project Polaris — Sprint History

> Chronological summary reconstructed from development history and code markers. Sprint ordering is reliable; calendar dates are unknown. See `PROJECT_HANDOFF.md` for detail.

| Sprint | Focus | Status |
|---|---|---|
| 1 | MVP: Streamlit CSV upload and file summary | Done |
| 2 | Dataset overview: columns, dtypes, missing values, duplicates | Done (from history) |
| 3 | Overview reorganization and data-quality sections | Done (from history) |
| 4 | Brazilian Portuguese UI | Done |
| 5 | Descriptive statistics | Done |
| 6–8 | Semantic profiling: name rules, refactor, content-based detection | Done |
| 9 / 9.1 | Modularization and separation of computation from rendering | Done |
| 10 | Deterministic insight engine | Implemented; later removed from main UI/LLM prompt |
| 11–12 | Domain/context inference and structural detection | Done |
| 13–15 | LLM abstraction, Markdown export, OpenRouter integration and fallback | Done |
| 15.x | OpenAI SDK/httpx dependency compatibility fix | Done |
| 16 / 16.1 / 16.2 | Advanced statistics, caching, relevance tuning | Done |
| 17 | Privacy by Design / LGPD-oriented sanitization | Done |
| 18–20 | NPS analysis, LLM guardrails, dimensional analysis | Done |
| 21 | UI hierarchy and explainability refinement | Done |
| 22 | NPS/CSAT/CES methodology detection and analyzers | Done |
| 23 / 23.1 | Semantic roles and identifier/coordinate classification fixes | Done |
| 24 | Generic analysis and Brazilian formatting | Done |
| 25 / 25.1 | LLM prompt audit and contract fixes | Done |
| 26 / 26.1 | Semantic role fixes for booleans, admin codes, coordinates | Done |
| 26.2 | Geographic report audit | Audit only; no production code change |

## Historical fixtures recorded

- NPS score: **-7.2**
- CSAT satisfied count: **338**
- CES low-effort count: **245**
- Geographic fixture role expectations: `state_code` as dimension, `capital` as boolean, `lat`/`long` as coordinates, `city_code` as identifier.

## Gaps

No persisted sprint log, issue tracker, changelog, or Git history was available in the project folder. Sprint dates are unknown; the exact scope of Sprints 2 and 3 could not be independently confirmed. Treat historical fixture values as recorded history, not as an automated test suite.
