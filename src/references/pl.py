import textwrap

def gb() -> None:
    """
    Polars groupby with one or more keys and common aggregations.
    """
    snippet = textwrap.dedent("""\
    df = your_polars_dataframe
    col = ["col1"]          # or ["col1", "col2", ...]
    value_col = "value_col"

    out = (
        df
        .groupby(col)
        .agg([
            pl.count().alias("n"),
            pl.col(value_col).mean().alias("mean_value"),
            pl.col(value_col).sum().alias("sum_value"),
        ])
    )
    """)
    print(snippet)
