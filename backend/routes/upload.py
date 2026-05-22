from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.data_service import save_uploaded_file, load_dataset, generate_dataset_summary

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/csv")
async def upload_csv(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    file_path = await save_uploaded_file(file)
    df = load_dataset(file_path)
    summary = generate_dataset_summary(df)

    return {
        "filename": file.filename,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "summary": summary
    }