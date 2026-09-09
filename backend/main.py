from fastapi import FastAPI

from backend.app.api.chat import router as chat_router
from backend.app.api.health import router as health_router

app = FastAPI(title="OmniAgent API")


app.include_router(chat_router)
app.include_router(health_router)