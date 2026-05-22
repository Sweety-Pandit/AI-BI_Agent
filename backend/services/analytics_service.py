import pandas as pd
import numpy as np


def basic_statistics(df: pd.DataFrame):

    numeric_df = df.select_dtypes(include=["number"])
    stats = {
        "mean": numeric_df.mean().to_dict(),
        "median": numeric_df.median().to_dict(),
        "std": numeric_df.std().to_dict(),
        "min": numeric_df.min().to_dict(),
        "max": numeric_df.max().to_dict()
    }

    return stats


def missing_value_analysis(df: pd.DataFrame):
    missing = df.isnull().sum()
    missing_percent = ((missing / len(df)) * 100).round(2)

    return {
        "missing_count": missing.to_dict(),
        "missing_percentage": missing_percent.to_dict()
    }


def correlation_analysis(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        return {}

    correlation_matrix = numeric_df.corr()
    return correlation_matrix.round(2).to_dict()


def dataset_overview(df: pd.DataFrame):

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "duplicate_rows": int(df.duplicated().sum()),
        "memory_usage_mb": round(
            df.memory_usage(deep=True).sum() / (1024 * 1024),
            2
        )
    }