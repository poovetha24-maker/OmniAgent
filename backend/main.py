from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "OmniAgent backend is running"}