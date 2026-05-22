import pandas as pd


def clean_column_names(df: pd.DataFrame):

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df