# src/relationship_extraction.py

import spacy

def extract_relationships(sentences):
    nlp = spacy.load('en_core_web_sm')
    relationships = []
    for sentence in sentences:
        doc = nlp(sentence)
        entities = [ent.text for ent in doc.ents]
        for token in doc:
            # Simple pattern matching for demonstration purposes
            if token.dep_ == 'nsubj' and token.head.pos_ == 'VERB':
                subject = token.text
                verb = token.head.lemma_
                obj = ''
                for child in token.head.children:
                    if child.dep_ == 'dobj':
                        obj = child.text
                if obj:
                    relationships.append((subject, verb, obj))
    return relationships