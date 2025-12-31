# LogSense AI — Intelligent Log Analysis System

LogSense AI is an AI-powered backend service that analyzes application logs to detect severity, summarize incidents, and extract key error patterns.
It is designed to simulate real-world production monitoring and incident analysis.

## Features
✅ Severity classification (INFO / WARNING / ERROR)
✅ Incident summarization using transformer models
✅ Keyword extraction from logs
✅ Batch log processing
✅ FastAPI backend
✅ Clean, modular architecture
✅ Production-ready API design

## API

POST /analyze
```json
{
  "logs": [
    "ERROR Database connection failed",
    "WARNING Retry attempt 2",
    "ERROR Timeout while calling payment service."
  ]
}

{
  "severity_breakdown": {
    "INFO": 0,
    "WARNING": 1,
    "ERROR": 2
  },
  "incident_summary": "The system experienced database connection failures and timeouts while attempting to process requests.",
  "top_keywords": ["error", "database", "timeout", "connection", "service"]
}

---

## 3. Folder cleanup (THIS MATTERS)

Final structure:
backend/
├── main.py
├── model.py
├── service/
│   ├── severity.py
│   ├── summarization.py
│   ├── keywords.py
│   └── analysis.py
├── requirements.txt
└── README.md

---

## 4. requirements.txt (clean & minimal)

```txt
fastapi
uvicorn
transformers
torch
nltk
pydantic
nltk
pydantic
