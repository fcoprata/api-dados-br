from validate_docbr import CNPJ


class Gerador_CNPJ:
    """
    A class for generating CNPJ numbers.

    Methods:
    - gerador_CNPJ: Generates a single CNPJ number.
    - gerador_cNPCNPJs: Generates a dictionary of multiple CNPJ numbers.

    """

    @staticmethod
    def gerador_CNPJ(mask=True):
        """
        Generates a single CNPJ number.

        Parameters:
        - mask (bool):
        Whether to include formatting mask in the generated CNPJ number.
        Default is True.

        Returns:
        - str: The generated CNPJ number.

        """
        gerador = CNPJ()
        return gerador.generate(mask)

    @staticmethod
    def gerador_CNPJs(quantidade: int, mask=True):
        """
        Generates a dictionary of multiple CNPJ numbers.

        Parameters:
        - quantidade (int): The number of CNPJ numbers to generate.
        - mask (bool):
        Whether to include formatting mask in the generated CNPJ numbers.
        Default is True.

        Returns:
        - dict:
        A dictionary where the keys are the CNPJ numbers' indices and
        the values are the CNPJ numbers.

        """
        gerador = CNPJ()
        if quantidade > 10:
            return "Máximo é 10 números de CNPJ"
        lista_CNPJ = gerador.generate_list(quantidade, mask)
        dicionario = {f'CNPJ {i+1}': CNPJ for i, CNPJ in enumerate(lista_CNPJ)}
        return dicionario
