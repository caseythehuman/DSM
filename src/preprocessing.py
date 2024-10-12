# src/preprocessing.py

import re
import spacy

def clean_line(line):
    # Remove ICD codes (e.g., F44.4, R15.9)
    line = re.sub(r'\b[A-Z][A-Z]?[0-9]+(\.[0-9]+)?\b', '', line)
    # Remove numerical codes and references (e.g., (405), 8:, 9:)
    line = re.sub(r'\b\d+:\b', '', line)
    line = re.sub(r'\(\d+\)', '', line)
    # Remove notes starting with 'Note:'
    line = re.sub(r'^Note:', '', line)
    # Remove extra whitespace
    line = re.sub(r'\s+', ' ', line)
    return line.strip()

def preprocess_text(file_path, batch_size=100):
    nlp = spacy.load('en_core_web_sm')
    sentences = []

    def text_generator(file_path):
        buffer = ''
        buffer_size = 10000  # Adjust based on your memory capacity
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Clean the line
                line = clean_line(line)
                if line:
                    buffer += ' ' + line  # Replace newlines with spaces
                # Yield buffer when it reaches a certain size
                if len(buffer) >= buffer_size:
                    buffer = re.sub(r'\s+', ' ', buffer)
                    yield buffer.strip()
                    buffer = ''
            # Yield any remaining text in the buffer
            if buffer:
                buffer = re.sub(r'\s+', ' ', buffer)
                yield buffer.strip()

    texts = text_generator(file_path)
    for doc in nlp.pipe(texts, batch_size=batch_size):
        sentences.extend([sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 0])

    return sentences
