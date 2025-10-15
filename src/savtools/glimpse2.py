import polars as pl

def glimpse2(df: pl.DataFrame, n: int = 5, width: int = 60) -> None:
    """Adds a null column to the already existing polars.DataFrame.glimpse function"""
    print(f"Rows: {df.height}  Columns: {df.width}")

    names  = df.columns
    dtypes = [str(t) for t in df.dtypes]
    nulls  = dict(zip(df.columns, df.null_count().row(0)))

    # align names
    name_w = max((len(nm) for nm in names), default=1)

    # precompute and align "nulls: x (y%)"
    null_info_map = {
        nm: f"nulls: {nulls[nm]} ({(nulls[nm] / df.height * 100) if df.height else 0.0:.1f}%)"
        for nm in names
    }
    null_w = max((len(s) for s in null_info_map.values()), default=1)

    # precompute and align dtype block "<dtype>"
    dtype_blocks = [f"<{dt}>" for dt in dtypes]
    dtype_w = max((len(s) for s in dtype_blocks), default=1)

    for name, dt in zip(names, dtypes):
        vals = str(df[name].head(n).to_list())
        if len(vals) > width:
            vals = vals[: width - 3] + "..."
        null_info = null_info_map[name]
        dtype_block = f"<{dt}>"

        # name | nulls | dtype (aligned) | values
        print(f"$ {name:<{name_w}}  {null_info:<{null_w}}  {dtype_block:<{dtype_w}}  {vals}")


pl.DataFrame.glimpse2 = glimpse2
