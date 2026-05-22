from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import pandas as pd
import os
from backend.services.query_service import analyze_business_query
from backend.services.llm_service import generate_ai_insights
router = APIRouter(prefix="/query", tags=["Business Query"])

UPLOAD_DIR = "data/uploads"

class QueryRequest(BaseModel):
    question: str


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

@router.post("/")
async def ask_business_question(request: QueryRequest):

    latest_file = get_latest_csv()
    if not latest_file:
        raise HTTPException(status_code=404, detail="No dataset uploaded")

    df = pd.read_csv(latest_file)
    analysis_result = analyze_business_query(df, request.question)

    prompt = f"""
    User Question:{request.question}
    Dataset Analysis:{analysis_result}
    Generate a business-focused analytical response.
    """
    
    ai_response = generate_ai_insights(prompt)
    return {
        "question": request.question,
        "analysis": analysis_result,
        "ai_response": ai_response
    }