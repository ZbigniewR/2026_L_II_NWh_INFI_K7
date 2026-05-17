import unittest
from hello_world import app
from hello_world.formater import SUPPORTED

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        # Używamy .decode('utf-8'), aby ładnie zamienić bajty na zwykły tekst
        s = rv.data.decode('utf-8')
        # Dodajemy spację po przecinku ', ', aby pasowało do kodu aplikacji
        self.assertTrue(', '.join(SUPPORTED) in s)

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        # Usuwamy wewnętrzne spacje i dodajemy \n na końcu stringa bajtowego
        self.assertEqual(b'{"imie":"Zbigniew","mgs":"Hello World!"}\n', rv.data)