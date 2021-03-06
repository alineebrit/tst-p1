import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global organiza_por_media
        undertest = __import__(module)
        organiza_por_media = getattr(undertest, 'organiza_por_media', None)

    def test_exemplo(self):
        p1 = [1,2,4,1,3,4,56,7,7,4,3,67]
        assert organiza_por_media(p1) == [1,2,4,1,3,4,7,7,4,3,56,67]
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
