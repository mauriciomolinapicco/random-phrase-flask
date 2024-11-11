import unittest
from app import app  
import json

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_frase(self):
        response = self.app.get('/frase')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        
        self.assertIn('frase', data)
        self.assertIn(data['frase'], [
            "esto es una frase v1",
            "esto es una frase v2",
            "esto es una frase v3",
            "esto es una frase v4",
            "esto es una frase v5"
        ])

    def test_suma(self):
        response = self.app.get('/suma?a=3&b=5')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)
        self.assertEqual(data['result'], 8)

    def test_suma_v2(self):
        response = self.app.get('/suma?a=3')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)
        self.assertEqual(data['result'], 3)

    def test_suma_param_invalido(self):
        response = self.app.get('/suma?a=abc&b=5')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data['error'], "Los parámetros deben ser números")

if __name__ == '__main__':
    unittest.main()
