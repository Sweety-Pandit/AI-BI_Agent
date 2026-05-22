from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.health import router as health_router
from backend.routes.upload import router as upload_router
from backend.routes.analytics import router as analytics_router
from backend.routes.visualization import router as visualization_router
from backend.routes.chat import router as chat_router
from backend.routes.query import router as query_router
from backend.routes.rag import router as rag_router

app = FastAPI(title="AI Business Intelligence Agent", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(analytics_router)
app.include_router(visualization_router)
app.include_router(chat_router)
app.include_router(query_router)
app.include_router(rag_router)


@app.get("/")
async def root():
    return {
        "message": "AI BI Agent Running Successfully"
    }