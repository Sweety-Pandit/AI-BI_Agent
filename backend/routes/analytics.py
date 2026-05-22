from fastapi import APIRouter, HTTPException
import pandas as pd
import os
from backend.services.analytics_service import basic_statistics, missing_value_analysis, correlation_analysis, dataset_overview

router = APIRouter(prefix="/analytics", tags=["Analytics"])

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


@router.get("/summary")
async def analytics_summary():

    latest_file = get_latest_csv()
    if not latest_file:
        raise HTTPException(status_code=404, detail="No dataset uploaded")

    df = pd.read_csv(latest_file)
    return {
        "overview": dataset_overview(df),
        "statistics": basic_statistics(df),
        "missing_values": missing_value_analysis(df),
        "correlation": correlation_analysis(df)
    }
