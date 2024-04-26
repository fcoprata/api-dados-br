from validate_docbr import CPF


class Gerador_cpf:
    @staticmethod
    def gerador_cpf(mask=True):
        gerador = CPF()
        return gerador.generate(mask)

    @staticmethod
    def gerador_cpfs(quantidade: int, mask=True):
        gerador = CPF()
        lista_cpfs = gerador.generate_list(quantidade, mask)
        dicionario = {f'cpf {i+1}': cpf for i, cpf in enumerate(lista_cpfs)}
        return dicionario
