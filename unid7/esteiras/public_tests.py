import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
filas_de_atendimento = getattr(undertest, 'distribui_materia_prima', None)

class PublicTests(unittest.TestCase):

    def test_exemplo1(self):
        fila_unica = [ 'A', 'A', 'B', 'C', 'C']
        assert filas_de_atendimento(fila_unica, 3) == [['A','C'],['A', 'C'], ['B']]        

    def test_exemplo2(self):
        fila_unica = ['A', 'A', 'B', 'C']
        assert filas_de_atendimento(fila_unica, 2) == [['A','B'],['A', 'C']]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
