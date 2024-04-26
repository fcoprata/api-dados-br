from validate_docbr import CPF


class Gerador_cpf:
    @staticmethod
    def gerador_cpf(mask=True):
        gerador = CPF()
        return gerador.generate(mask)
