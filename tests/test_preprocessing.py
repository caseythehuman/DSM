# tests/test_preprocessing.py

import unittest
from src.preprocessing import preprocess_text

class TestPreprocessing(unittest.TestCase):
    def test_preprocess_text(self):
        sentences = preprocess_text('data/diagnosis_characteristics.txt')
        self.assertIsInstance(sentences, list)
        self.assertGreater(len(sentences), 0)

if __name__ == '__main__':
    unittest.main()
