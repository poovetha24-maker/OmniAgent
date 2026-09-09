from fastapi import FastAPI

from backend.memory.routes import router as memory_router

app = FastAPI()

# Memory API routes
app.include_router(memory_router)


@app.get("/health")
def health_check():
    return {"status": "OmniAgent backend is running"}