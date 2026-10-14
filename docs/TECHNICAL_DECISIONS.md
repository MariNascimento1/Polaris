# Project Polaris — Technical Decisions

This document summarizes the principal decisions recorded during development. Sprint dates were not recoverable.

## 1. Deterministic-first, AI-second

Quantitative facts are computed in Python. The LLM is intended to interpret structured findings, not calculate metrics from raw CSV data. This improves reproducibility and reduces hallucination risk, but limits the narrative to facts produced by the deterministic layer.

## 2. Semantic roles as a shared source of truth

A column's storage dtype does not necessarily describe its analytical role. The role layer distinguishes metrics, dimensions, identifiers, classifications, coordinates, booleans, and sensitive fields. Changes to this shared layer can affect all analysis paths and should be test-first.

## 3. Name-driven coordinate detection

Coordinate detection requires geographic intent in the column name because numeric value ranges alone produce false positives. The trade-off is that coordinates with non-standard names may be missed.

## 4. Conservative methodology detection

NPS/CSAT/CES detection combines column-name evidence with scale compatibility. Scale alone should not force a classification; “unknown” is preferred over a confidently wrong methodology.

## 5. Deterministic report is authoritative

For satisfaction datasets, deterministic report sections remain intact; an LLM executive summary is additive. This preserves a useful report if the provider is unavailable or returns invalid output, though some content may be repeated.

## 6. Generic LLM path is a known gap

The generic path lacks a dedicated interpretation instruction, and the system prompt is satisfaction-centric. Generic reports can therefore echo tables rather than interpret them. The fix remains pending.

## 7. Shared privacy sanitization

A single privacy layer sanitizes structured context before LLM use and masks sensitive values in the UI. This reduces drift between presentation and model input, but makes that module important to test.

## 8. Report caching

Reports are cached in Streamlit session state with version-based invalidation to reduce repeated latency and token spend. The report version must be updated when report logic changes.

## 9. Brazilian formatting

Numbers use Brazilian separators, and monetary values are prefixed with R$ for the intended Brazilian audience.

## 10. Separation of computation and rendering

Computation modules are intended to remain independent of Streamlit, with UI rendering concentrated in `ui.py`. This supports isolated testing and reuse.
