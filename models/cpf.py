from validate_docbr import CPF


class Cpf:
    """
    Represents a CPF (Cadastro de Pessoas Físicas) number.

    Attributes:
        documento (str): The CPF number.

    Methods:
        __init__(self, documento: str):
            Initializes a new instance of the Cpf class.
        __str__(self) -> str:
            Returns a string representation of the CPF number.
        cpf_valid(self, documento: str): Validates the CPF number.
        mascara(self, documento: str) -> str: Applies a mask to the CPF number.

    """

    validador = CPF()

    def __init__(self, documento: str):
        if self.cpf_valid(documento):
            self.documento = documento
        else:
            raise TypeError("CPF invalid")

    def cpf_valid(self, documento: str):
        """
        Validates the CPF number.

        Args:
            documento (str): The CPF number to be validated.

        Returns:
            str: "Valid" if the CPF number is valid, "Invalid" otherwise.
        """
        if len(documento) == 11:
            return "Valid" if self.validador.validate(documento) else "Invalid"

    def mascara(self, documento: str) -> str:
        """
        Applies a mask to the CPF number.

        Args:
            documento (str): The CPF number to apply the mask to.

        Returns:
            str: The CPF number with the mask applied.
        """
        return f"{self.validador.mask(documento)}"
