import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
variacao_bubble = getattr(undertest, 'variacao_bubble', None)

class PublicTests(unittest.TestCase):

    def test_exemplo_1(self):
        vetor = [6, 9, 2, 3, 1, 4]
        assert variacao_bubble(vetor, 0, 6) == 2
        assert vetor == [4, 1, 2, 3, 9, 6]
       
    def test_exemplo_2(self):
        vetor = [8, 6, 9, 2, 3, 1, 4, 0, 7, 4]
        assert variacao_bubble(vetor, 1, 7) == 2
        assert vetor == [8, 4, 1, 2, 3, 9, 6, 0, 7, 4]
       

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
