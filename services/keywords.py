import logging
from collections import Counter
import nltk
from nltk.corpus import stopwords

logging.info("Loading keywords model...")

nltk.download("stopwords")

def extract_keywords(text: str):
    words = text.lower().split()
    words = [w for w in words if w.isalpha()]
    words = [w for w in words if w not in stopwords.words("english")]
    return [w for w, _ in Counter(words).most_common(5)]
