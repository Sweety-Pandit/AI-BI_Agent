from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.rag_service import create_vector_store, retrieve_context

from backend.services.llm_service import generate_ai_insights

router = APIRouter(prefix="/rag", tags=["RAG"])


@router.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):

    content = await file.read()
    text = content.decode("utf-8")
    chunks = create_vector_store(text)

    return {
        "message": "Document indexed successfully",
        "chunks_created": chunks
    }


@router.get("/query")
async def rag_query(question: str):
    context = retrieve_context(question)

    if not context:
        raise HTTPException(
            status_code=404,
            detail="No context available"
        )

    prompt = f"""
    Answer the question using the provided context.
    CONTEXT:{context}
    QUESTION:{question}
    Generate a business-focused response.
    """

    response = generate_ai_insights(prompt)

    return {
        "question": question,
        "context": context,
        "response": response
    }