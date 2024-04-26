from validate_docbr import CNPJ


class Cnpj:

    validador = CNPJ()

    def __init__(self, documento: str):
        if self.cnpj_valid(documento):
            self.documento = documento
        else:
            raise TypeError('CNPJ invalid')

    def cnpj_valid(self, documento: str):
        """
        Validates the CNPJ number.

        Args:
            documento (str): The CNPJ number to be validated.

        Returns:
            str: "Valid" if the CNPJ number is valid, "Invalid" otherwise.
        """
        if len(documento) == 11:
            return "Valid" if self.validador.validate(documento) else "Invalid"

    def mascara(self, documento: str) -> str:
        """
        Applies a mask to the CNPJ number.

        Args:
            documento (str): The CNPJ number to apply the mask to.

        Returns:
            str: The CNPJ number with the mask applied.
        """
        return f"{self.validador.mask(documento)}"
