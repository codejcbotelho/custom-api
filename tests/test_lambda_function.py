import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_custom_warning_web(self):
        event = {
            'httpMethod': 'GET',
            'path': '/custom-warning',
            'pathParameters': {
                'param': 'web'
            }
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertIsInstance(response['body'], str)
        body = response['body']
        data = json.loads(body)
        self.assertIsInstance(data['list'], list)

    def test_custom_warning_app(self):
        event = {
            'httpMethod': 'GET',
            'path': '/custom-warning',
            'pathParameters': {
                'param': 'app'
            }
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertIsInstance(response['body'], str)
        body = response['body']
        data = json.loads(body)
        self.assertIsInstance(data['list'], list)

    def test_custom_warning_invalid_param(self):
        event = {
            'httpMethod': 'GET',
            'path': '/custom-warning',
            'pathParameters': {
                'param': 'invalid'
            }
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 400)
        self.assertIsInstance(response['body'], str)
        body = response['body']
        data = json.loads(body)
        self.assertEqual(data['error'], 'Invalid parameter')

    def test_brands_no_filter(self):
        event = {
            'httpMethod': 'GET',
            'path': '/brands',
            'queryStringParameters': None
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertIsInstance(response['body'], str)
        body = response['body']
        data = json.loads(body)
        self.assertIsInstance(data['list'], list)

    def test_brands_with_filter(self):
        event = {
            'httpMethod': 'GET',
            'path': '/brands',
            'queryStringParameters': {
                'brand': 'mastercard'
            }
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 200)
        self.assertIsInstance(response['body'], str)
        body = response['body']
        data = json.loads(body)
        self.assertIsInstance(data['list'], list)

    def test_invalid_path(self):
        event = {
            'httpMethod': 'GET',
            'path': '/invalid-path'
        }
        response = lambda_handler(event, None)
        self.assertEqual(response['statusCode'], 404)
        self.assertIsInstance(response['body'], str)
        body = response['body']
        data = json.loads(body)
        self.assertEqual(data['error'], 'Resource not found')
