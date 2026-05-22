import plotly.express as px
import pandas as pd


def generate_histogram(df: pd.DataFrame, column: str):
    fig = px.histogram(df, x=column, title=f"Distribution of {column}")

    return fig.to_json()


def generate_scatter_plot(df: pd.DataFrame, x_column: str, y_column: str):

    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{x_column} vs {y_column}"
    )

    return fig.to_json()