import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
remove_divisores_k = getattr(undertest, 'remove_divisores_k', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = [8, 1, 2, 2, 13, 4, 19]
        remove_divisores_k(l1, 4, 2)
        assert l1 == [8, 1, 2, 13, 19]


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
