import unittest
import sys

module = sys.argv[-1].split(".py")[0]


class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global alocacao_aulas
        undertest = __import__(module)
        alocacao_aulas = getattr(undertest, 'alocacao_aulas', None)

    def test_example(self):
        alunos = [("Maria", 3), ("João", 5), ("Carlos", 1), ("Pedro", 9), ("Ângela", 7)]
        assert alocacao_aulas(alunos) == [["Maria", "Carlos"],["João"],["Pedro", "Ângela"]]
        assert alunos == [("Maria", 3), ("João", 5), ("Carlos", 1), ("Pedro", 9), ("Ângela", 7)]

    def test_exemplo2(self):
        alunos = [("Maria", 3), ("João", 10)]
        assert alocacao_aulas(alunos) == [["Maria"],[],["João"]]
        assert alunos == [("Maria", 3), ("João", 10)]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
