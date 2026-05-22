from fastapi import APIRouter, HTTPException
import pandas as pd
import os

from backend.services.visualization_service import generate_histogram, generate_scatter_plot

router = APIRouter(prefix="/visualization", tags=["Visualization"])
UPLOAD_DIR = "data/uploads"


def get_latest_csv():

    files = [
        os.path.join(UPLOAD_DIR, file)
        for file in os.listdir(UPLOAD_DIR)
        if file.endswith(".csv")
    ]

    if not files:
        return None

    latest_file = max(files, key=os.path.getctime)
    return latest_file


@router.get("/histogram/{column}")
async def histogram(column: str):

    latest_file = get_latest_csv()

    if not latest_file:
        raise HTTPException(
            status_code=404,
            detail="No dataset uploaded"
        )

    df = pd.read_csv(latest_file)

    if column not in df.columns:
        raise HTTPException(status_code=400, detail="Column not found")

    return {
        "chart": generate_histogram(df, column)
    }


@router.get("/scatter")
async def scatter_plot(x_column: str, y_column: str):

    latest_file = get_latest_csv()

    if not latest_file:
        raise HTTPException(status_code=404, detail="No dataset uploaded")

    df = pd.read_csv(latest_file)
    return {
        "chart": generate_scatter_plot(
            df,
            x_column,
            y_column
        )
    }