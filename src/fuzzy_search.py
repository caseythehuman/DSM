# src/fuzzy_search.py

from rapidfuzz import process

def fuzzy_search(query, data, limit=5):
    results = process.extract(query, data, limit=limit)
    return results