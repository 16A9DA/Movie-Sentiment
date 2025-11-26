import re
import contractions
import unicodedata
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import unittest

lemm = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = contractions.fix(text)

    text  = re.sub(r"\d+", " ", text)
    text = re.sub(r"[@,$,&,/]", " ", text)
    text = re.sub(r"[<.*?>]", " ", text)
    text = re.sub(r"\s+", " ", text)
    words = word_tokenize(text)
    words = [lemm.lemmatize(w) for w in words]

    text = " ".join(words)

    text = unicodedata.normalize("NFKD", text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])

    return text


class TestCleanText(unittest.TestCase):

    def test_lowercase(self):
        self.assertEqual(clean_text("HELLO"), "hello")

    def test_contraction(self):
        result = clean_text("don't")
        self.assertIn("do", result)
        self.assertIn("not", result)

    def test_numbers_removed(self):
        self.assertEqual(clean_text("movie123"), "movie")

    def test_symbols_removed(self):
        self.assertEqual(clean_text("hi@you&me"), "hi you me")

    def test_slashes_removed(self):
        self.assertEqual(clean_text("good/bad"), "good bad")

    def test_spacing(self):
        self.assertEqual(clean_text("hello      world"), "hello world")


if __name__ == "__main__":
    unittest.main()