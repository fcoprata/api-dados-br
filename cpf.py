from validate_docbr import CPF


class Cpf:
    validador = CPF()

    def __init__(self, documento: str):
        if self.cpf_valid(documento):
            self.documento = documento
        else:
            raise TypeError("CPF invalid")

    def __str__(self) -> str:
        return f"{self.validador.mask(self.documento)} - {self.cpf_valid(self.documento)}"

    def cpf_valid(self, documento: str):
        if len(documento) == 11:
            return "Valid" if self.validador.validate(documento) else "Invalid"
