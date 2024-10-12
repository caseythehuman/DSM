# src/preprocessing.py

import spacy

def preprocess_text(file_path, batch_size=100):
    nlp = spacy.load('en_core_web_sm')
    sentences = []

    def text_generator(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()

    texts = text_generator(file_path)
    for docs in nlp.pipe(texts, batch_size=batch_size):
        sentences.extend([sent.text.strip() for sent in docs.sents])

    return sentences