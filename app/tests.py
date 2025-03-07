import unittest
from app.main import app


class SentimentTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_positive_sentiment(self):
        response = self.app.post('/predict', json={"text": "I love this!"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["sentiment"], "positive")

    def test_negative_sentiment(self):
        response = self.app.post('/predict', json={"text": "I hate this!"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["sentiment"], "negative")

    def test_empty_text(self):
        response = self.app.post('/predict', json={"text": ""})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
