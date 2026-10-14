"""Project Polaris - Application entry point."""

import streamlit as st
import pandas as pd

from ui import (
    configure_page,
    display_header,
    upload_csv,
    display_overview,
    display_data_quality,
    display_exploration,
    display_semantic_profile,
    display_dataset_context,
    display_report_section,
    display_provider_status,
)


@st.cache_data
def load_dataframe(file_content: bytes) -> pd.DataFrame | None:
    """Read uploaded file content with automatic delimiter detection."""
    import csv
    from io import BytesIO

    text = file_content.decode("utf-8", errors="replace")
    try:
        dialect = csv.Sniffer().sniff(text[:8192], delimiters=",;\t|")
        delimiter = dialect.delimiter
    except csv.Error:
        first_line = text.split("\n", 1)[0]
        candidates = [(",", first_line.count(",")), (";", first_line.count(";")), ("\t", first_line.count("\t")), ("|", first_line.count("|"))]
        best = max(candidates, key=lambda x: x[1])
        if best[1] > 0:
            delimiter = best[0]
        else:
            return None
    return pd.read_csv(BytesIO(file_content), sep=delimiter)


def main():
    """Application entry point."""
    configure_page()
    display_header()
    uploaded_file = upload_csv()
    if uploaded_file is not None:
        df = load_dataframe(uploaded_file.getvalue())
        if df is None:
            st.error("Não foi possível detectar o delimitador do arquivo CSV. Verifique se o arquivo está formatado corretamente.")
            return
        display_overview(uploaded_file, df)
        display_data_quality(df)
        display_exploration(df)
        display_semantic_profile(df)
        display_dataset_context(df)
        st.divider()
        display_report_section(uploaded_file, df)
    display_provider_status()


if __name__ == "__main__":
    main()
