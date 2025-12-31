from concurrent.futures import ThreadPoolExecutor
from services.summerization import summarize_logs
from services.keywords import extract_keywords
from services.serverity import classify_serverity

executor = ThreadPoolExecutor(max_workers=3)

def analyze_logs_pipeline(logs: list[str]):
    combined_text = " ".join(logs)

    classify_serverity_future = executor.submit(classify_serverity, logs)
    summary_future = executor.submit(summarize_logs, combined_text)
    keywords_future = executor.submit(extract_keywords, combined_text)

    return {
        "serverity": classify_serverity_future.result(),
        "summary": summary_future.result(),
        "keywords": keywords_future.result()
    }
