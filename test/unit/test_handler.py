import unittest
from src.handler import lambda_handler

class TestLambdaHandler(unittest.TestCase):
    def test_lambda_handler(self):
        result = lambda_handler({}, None)
        self.assertEqual(result['statusCode'], 200)