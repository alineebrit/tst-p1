import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
letras_alternadas = getattr(undertest, 'letras_alternadas', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
       assert letras_alternadas('casa') == 'cs'

   def test_basico1(self):
       assert letras_alternadas('exemplo') == 'eepo'

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
