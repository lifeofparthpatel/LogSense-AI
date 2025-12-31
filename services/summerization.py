import logging
from transformers import pipeline

logging.info("Loading summerization model...")

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_logs(text):
    return summarizer(text, max_length=80, min_length=30, do_sample=False)[0]['summary_text']

