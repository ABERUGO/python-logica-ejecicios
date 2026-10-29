import unittest
from palindromo import es_palindromo
from palabra_invertida import invertir_palabra # (Ajusta esto si tu función se llama diferente)

class TestEjerciciosLogica(unittest.TestCase):

    def test_palindromo_correcto(self):
        self.assertTrue(es_palindromo("reconocer"))

    def test_palindromo_incorrecto(self):
        self.assertFalse(es_palindromo("hola"))

    def test_palindromo_con_mayusculas(self):
        self.assertTrue(es_palindromo("Neuquen"))

if __name__ == '__main__':
    unittest.main()
