# src/fuzzy_search.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process, fuzz

def vector_search(query, data, limit=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(data + [query])
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    related_docs_indices = cosine_similarities.argsort()[-limit:][::-1]
    results = [(data[i], cosine_similarities[i]) for i in related_docs_indices if cosine_similarities[i] > 0]
    return results

def fuzzy_search(query, data, limit=5):
    # Preprocess the data
    data_processed = [entry.lower() for entry in data]
    query = query.lower()
    # Perform fuzzy search using RapidFuzz
    results = process.extract(query, data_processed, scorer=fuzz.token_sort_ratio, limit=limit)
    # Map back to the original sentences
    results_with_sentences = [(data[idx], score, idx) for (match, score, idx) in results]
    return results_with_sentences
