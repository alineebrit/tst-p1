import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
verifica_esteira = getattr(undertest, 'verifica_esteira', None)

class PublicTests(unittest.TestCase):

    def test_example(self):
        esteira = [2, 1, 3, 4]
        componentes = [2, 4]
        assert verifica_esteira(esteira, componentes)
        assert esteira == [2, 1, 3, 4]
        assert componentes == [2, 4]

        esteira = [1, 3, 4]
        componentes = [4, 1, 3]
        assert not verifica_esteira(esteira, componentes)
        assert esteira == [1, 3, 4]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
