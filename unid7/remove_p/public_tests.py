import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global remove_palavras_com_maiusculas
        undertest = __import__(module)
        remove_palavras_com_maiusculas = getattr(undertest, 'remove_palavras_com_maiusculas', None)

    def test_exemplo(self):
        lista1 = ['arara', 'Tv', 'baCia']
        assert remove_palavras_com_maiusculas(lista1) == None
        assert lista1 == ['arara']

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
