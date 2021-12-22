import unittest
import sys

module = sys.argv[-1].split(".py")[0]

class PublicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global ultimo_nome, fmt_citacao
        undertest = __import__(module)
        ultimo_nome = getattr(undertest, 'ultimo_nome', None)
        fmt_citacao = getattr(undertest, 'fmt_citacao', None)

    def test_exemplo(self):
        autores = [
            'Machado de Assis',
            'João Cabral de Melo Neto',
            'Graciliano Ramos',
            'Guimarães Rosa'
        ]
        assert ultimo_nome(autores[0]) == 'Assis'
        assert ultimo_nome(autores[1]) == 'Neto'
        assert ultimo_nome(autores[2]) == 'Ramos'
        assert ultimo_nome(autores[3]) == 'Rosa'


    def test_exemplo_2(self):
        autores = [
            'Machado de Assis',
            'João Cabral de Melo Neto',
            'Graciliano Ramos',
            'Guimarães Rosa'
        ]
        citacoes = fmt_citacao(autores)
        assert citacoes == [
            'Assis, M.',
            'Neto, J.',
            'Ramos, G.',
            'Rosa, G.'
        ] 


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
