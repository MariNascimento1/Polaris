# Project Polaris — Development Handoff

Generated: 2026-10-13.

## Purpose

Polaris is a Python/Streamlit data-profiling and dataset-understanding application. It analyzes an uploaded CSV deterministically first, then can optionally use an LLM to generate an executive narrative from structured findings. Intended use cases include NPS, CSAT, CES, and generic business datasets.

## Current scope

Single-file CSV analysis, quality and statistical profiling, semantic roles, context/domain inference, satisfaction methodology detection, dimensional business analysis, privacy sanitization, optional OpenRouter integration with fallback, and Markdown export. No database, authentication, multi-file analysis, or charts are included.

## Architecture

- `app.py`: entry point and CSV loading.
- `ui.py`: Streamlit rendering.
- `quality.py`, `statistics.py`, `structure_engine.py`: deterministic profiling.
- `semantic_rules.py`, `semantic_engine.py`: semantic types and analytical roles.
- `domain_rules.py`, `context_engine.py`: domain inference.
- `metric_detection.py`, `descriptive_analysis_engine.py`: NPS/CSAT/CES and generic analysis.
- `privacy_engine.py`: sanitization for UI and LLM context.
- `llm_engine.py`: provider abstraction, OpenRouter integration, prompt construction, fallback.
- `export_engine.py`: Markdown export.
- `insight_engine.py`: deterministic insights (retained but not prominent in the UI).

## Confirmed capabilities recorded by the handoff

CSV delimiter detection; data-quality metrics; numeric/categorical statistics; semantic detection by name and content; analytical role classification; structure and domain inference; NPS/CSAT/CES detection and dimensional analysis; privacy-oriented sanitization; OpenRouter provider abstraction with mock/deterministic fallback; cached report composition; Markdown download; Brazilian number formatting.

## Known limitations

- Generic reports are shallow for coordinate/boolean/code-heavy datasets.
- The generic LLM path lacks a dedicated interpretation request and may echo tables.
- The system prompt is satisfaction-centric.
- Numeric-coded categorical columns without name hints and year-like columns can be misclassified.
- Debug print traces remain in the LLM engine.
- There is no committed automated test suite.
- Live OpenRouter behavior was not verified in the handoff.

## Recorded historical fixtures (not a committed test suite)

- NPS score: -7.2.
- CSAT satisfied count: 338.
- CES low-effort count: 245.
- Privacy and prompt-contract checks were reportedly run in temporary scripts that were later deleted.

## Setup

Requires Python 3.10+.

```bash
python -m venv .venv
```

Activate the environment (Windows: `.venv\Scripts\activate`; macOS/Linux: `source .venv/bin/activate`), then:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Optional OpenRouter configuration: copy `.env.example` to `.env` and set `OPENROUTER_API_KEY`. Never commit `.env` or publish real keys.

## Recommended continuation order

1. Add a pytest suite for routing, metrics, roles, privacy, and prompt contracts.
2. Improve generic LLM interpretation without changing satisfaction behavior.
3. Surface coordinate/boolean roles and inferred domain in generic reports.
4. Include quality summaries and top categorical values in generic reports.
5. Gate debug output behind a flag.
6. Improve numeric-coded categorical detection in a separate, tested change.

## Historical limitations

No persisted sprint log, issue tracker, changelog, or Git history was available in the original project folder. Sprint ordering was reconstructed from conversation history and code comments. Dates are unknown, and the exact scope of Sprints 2–3 could not be independently confirmed. Treat the recorded fixtures as historical claims until tests are restored and rerun.
