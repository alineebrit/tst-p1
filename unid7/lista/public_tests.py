import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
lista_so_com_oposto = getattr(undertest, 'lista_so_com_oposto', None)

class PublicTests(unittest.TestCase):

   def test_do_enunciado(self):
       lista1 = [1, 2, 1, 3, 4, -1, -3, 5]
       assert lista_so_com_oposto(lista1) == None
       assert lista1 == [1, 1, 3, -1, -3]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
