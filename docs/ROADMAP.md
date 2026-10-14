# Project Polaris — Roadmap

> Status snapshot generated 2026-10-13. See `PROJECT_HANDOFF.md` for evidence and detail.

## Completed (confirmed in code)

- CSV upload with automatic delimiter detection and cached loading.
- Data-quality summary, missing values, duplicates, memory usage.
- Basic and advanced descriptive statistics with Brazilian number/currency formatting.
- Name- and content-based semantic detection and analytical roles.
- Structure detection: keys, booleans, constants, cardinality.
- Context/domain inference with confidence and evidence.
- NPS/CSAT/CES methodology detection and dimensional business analysis.
- Privacy sanitization for LLM context and UI display.
- OpenRouter provider abstraction, mock/deterministic fallback.
- Deterministic report composition, session caching, Markdown export.
- Numbered Streamlit UI hierarchy.

## In progress / partial

- Generic analysis works for typical business datasets but is shallow for coordinate-, boolean-, and code-heavy datasets.
- Generic LLM output can echo deterministic tables because it lacks a dedicated interpretation request.

## Prioritized future work

1. Add a committed pytest suite for routing, semantic roles, fixtures, privacy, and prompt contracts.
2. Add a generic interpretation request without changing the satisfaction-specific prompt contract.
3. Surface coordinate/boolean roles and detected domain in generic reports.
4. Include computed quality summaries and categorical top-five values in generic prompts.
5. Gate debug prints behind a debug flag.
6. Improve detection of numeric-coded categorical fields; consider optional data-dictionary ingestion.
7. Consider PDF export, multi-file analysis, charts, and additional methodologies/providers.

**Dependencies:** items 3–5 build on item 2. Item 1 should precede changes to the shared semantic layer.
