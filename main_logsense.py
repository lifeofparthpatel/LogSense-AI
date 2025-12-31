import logging
from fastapi import FastAPI
from model import LogRequest
from services.analysis import analyze_logs_pipeline

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(request: LogRequest):
    logging.info(f"Received {len(request.logs)} logs")
    result = analyze_logs_pipeline(request.logs)
    logging.info("Analysis completed")
    return result
