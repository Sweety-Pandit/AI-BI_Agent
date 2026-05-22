import os
import uuid
import pandas as pd
import aiofiles

from fastapi import UploadFile


UPLOAD_DIR = "data/uploads"


async def save_uploaded_file(file: UploadFile):

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)
    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    return file_path


def load_dataset(file_path: str):
    df = pd.read_csv(file_path)

    return df


def generate_dataset_summary(df: pd.DataFrame):

    summary = {
        "column_names": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.astype(str).to_dict(),
        "sample_data": df.head(5).to_dict(orient="records")
    }

    return summary