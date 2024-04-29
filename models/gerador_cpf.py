from validate_docbr import CPF


class Gerador_cpf:
    """
    A class for generating CPF (Cadastro de Pessoas Físicas) numbers.

    Methods:
        gerador_cpf(mask=True):
            Generates a random CPF number.
        gerador_cpfs(quantidade: int, mask=True):
            Generates a dictionary of random CPF numbers.

    """

    @staticmethod
    def gerador_cpf(mask=True):
        """
        Generates a random CPF (Cadastro de Pessoas Físicas) number.

        Args:
            mask (bool, optional):
            Specifies whether to include the CPF mask (format: XXX.XXX.XXX-XX).
                       Defaults to True.

        Returns:
            str: The generated CPF number.

        """
        gerador = CPF()
        return gerador.generate(mask)

    @staticmethod
    def gerador_cpfs(quantidade: int, mask=True):
        """
        Generates a dictionary of random CPF numbers.

        Args:
            quantidade (int): The number of CPF numbers to generate.
            mask (bool, optional):
            Specifies whether to include the CPF mask (format: XXX.XXX.XXX-XX).
                Defaults to True.

        Returns:
            dict: A dictionary containing the generated CPF numbers as values,
            with keys in the format 'cpf i',
                  where i is the index of the CPF number in the list.

        """
        gerador = CPF()
        if quantidade > 10:
            return "Máximo é 10 números de CPF"
        lista_cpfs = gerador.generate_list(quantidade, mask)
        dicionario = {f'cpf {i+1}': cpf for i, cpf in enumerate(lista_cpfs)}
        return dicionario
