# Project Polaris

> **Understand data before asking AI to explain it.**

Polaris is a Python and Streamlit application for deterministic data profiling and dataset understanding. It analyzes an uploaded CSV locally, builds structured findings, and can optionally use an LLM to produce an executive narrative from those findings.

## Features

- CSV upload with automatic delimiter detection (comma, semicolon, tab, or pipe)
- Data-quality summary: duplicate rows, completeness, missing values, and memory usage
- Descriptive statistics for numeric and categorical columns, including advanced summaries
- Semantic profiling based on column names and sampled values
- Analytical column roles: metrics, dimensions, identifiers, classifications, sensitive fields, coordinates, and booleans
- Dataset structure and domain inference
- Customer-satisfaction methodology detection for NPS, CSAT, and CES
- Methodology-specific business analysis with dimensional breakdowns
- Privacy-oriented sanitization of sensitive values before LLM use and in UI display
- Optional OpenRouter LLM integration with a deterministic/mock fallback
- Downloadable Markdown report
- Brazilian number and currency formatting

## How it works

1. Upload a CSV file.
2. Polaris profiles data quality, structure, semantic types, and likely analytical roles.
3. It detects whether the dataset fits NPS, CSAT, CES, or a generic analysis path.
4. Deterministic Python logic calculates the reported facts.
5. If requested and configured, an LLM may add an executive narrative based on the structured analysis.
6. Export the report as Markdown.

The deterministic analysis is the source of quantitative facts; the LLM is intended to interpret those facts, not calculate metrics from raw data.

## Tech stack

- Python 3.10+
- Streamlit
- Pandas and NumPy
- OpenAI Python SDK configured to use OpenRouter
- python-dotenv

## Run locally

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Optional LLM configuration

Polaris can run without an API key using its deterministic fallback. To enable OpenRouter:

1. Copy `.env.example` to `.env`.
2. Add your own key as `OPENROUTER_API_KEY=...`.
3. Restart the application.

**Never commit `.env` or publish API keys.** The repository intentionally contains only a sanitized `.env.example`.

## Project structure

| File | Responsibility |
|---|---|
| `app.py` | App entry point and CSV loading |
| `ui.py` | Streamlit interface |
| `quality.py` | Data-quality computations |
| `statistics.py` | Descriptive statistics |
| `semantic_rules.py` | Name/content detection rules |
| `semantic_engine.py` | Semantic types and analytical roles |
| `structure_engine.py` | Structural characteristics |
| `domain_rules.py` / `context_engine.py` | Domain inference |
| `metric_detection.py` | NPS/CSAT/CES detection |
| `descriptive_analysis_engine.py` | Methodology-specific and generic analysis |
| `privacy_engine.py` | Sensitive-value sanitization |
| `insight_engine.py` | Deterministic observations |
| `llm_engine.py` | LLM provider abstraction and report composition |
| `export_engine.py` | Markdown export |

## Current limitations

- Generic reports can be shallow for datasets dominated by coordinates, booleans, or coded categories.
- The generic LLM path needs a dedicated interpretation instruction to avoid echoing deterministic tables.
- There is no committed automated test suite yet.
- Live OpenRouter output quality has not been verified as part of this handoff.

See [the roadmap](docs/ROADMAP.md), [sprint history](docs/SPRINT_HISTORY.md), [technical decisions](docs/TECHNICAL_DECISIONS.md), and [the development handoff](docs/PROJECT_HANDOFF.md) for details.

## License

MIT. See [LICENSE](LICENSE).
