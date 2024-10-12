# src/preprocessing.py

import spacy

def preprocess_text(file_path):
    nlp = spacy.load('en_core_web_sm')
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    doc = nlp(text)
    
    sentences = [sent.text.strip() for sent in doc.sents]
    return sentences