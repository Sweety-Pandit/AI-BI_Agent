import pandas as pd

def analyze_business_query(df: pd.DataFrame, query: str):

    query = query.lower()
    response = {}

    # Sales Analysis
    if "sales" in query:

        numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

        if numeric_columns:

            sales_column = numeric_columns[0]
            response["sales_summary"] = {
                "total_sales": float(df[sales_column].sum()),
                "average_sales": float(df[sales_column].mean()),
                "max_sales": float(df[sales_column].max()),
                "min_sales": float(df[sales_column].min())
            }

    # Profit Analysis
    if "profit" in query:

        profit_columns = [
            col for col in df.columns
            if "profit" in col.lower()
        ]

        if profit_columns:

            profit_col = profit_columns[0]

            response["profit_analysis"] = {
                "total_profit": float(df[profit_col].sum()),
                "average_profit": float(df[profit_col].mean())
            }

    # Region Analysis
    if "region" in query:
        region_columns = [
            col for col in df.columns
            if "region" in col.lower()
        ]

        if region_columns:

            region_col = region_columns[0]
            response["region_distribution"] = (
                df[region_col]
                .value_counts()
                .to_dict()
            )

    return response