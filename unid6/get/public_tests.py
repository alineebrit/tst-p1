import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global get_items
        undertest = __import__(module)
        get_items = getattr(undertest, 'get_items', None)

    def test_exemplo(self):
        valores = [18, 22, 73, 32, 19, 21, 43]
        indices2 = [3, 4, 8, 1]
        assert get_items(valores, indices2) == [32, 19, None, 22]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
