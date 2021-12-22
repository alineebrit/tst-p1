import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
insere_nome = getattr(undertest, 'insere_nome', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
     duplas = ['joel', 'juliano', 'cesar', 'auri', 'zito']
     assert insere_nome('gil', duplas, 'juliano') == None
     assert duplas == ['joel','gil','juliano','cesar','auri','zito']
     assert insere_nome('marta', duplas, 'vera') == None
     assert duplas == ['joel', 'gil', 'juliano', 'cesar', 'auri', 'zito', 'marta']
   
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
