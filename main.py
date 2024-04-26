from modelos.cpf import Cpf
from modelos.gerador_cpf import Gerador_cpf
from fastapi import FastAPI

app = FastAPI()


@app.get('/api/is_valid/{cpf}')
def validate_cpf(cpf):
    """
    Validates a CPF (Cadastro de Pessoas Físicas) number.

    Args:
        cpf (str): The CPF number to be validated.

    Returns:
        bool: True if the CPF is valid, False otherwise.
    """
    validador_cpf = Cpf(cpf)
    return validador_cpf.cpf_valid(cpf)


@app.get("/api/mascara/{cpf}")
def mascara(cpf):
    """
    Applies a mask to the given CPF (Cadastro de Pessoas Físicas) number.

    Args:
        cpf (str): The CPF number to apply the mask to.

    Returns:
        str: The CPF number with the mask applied.
    """
    validador_cpf = Cpf(cpf)
    return validador_cpf.mascara(cpf)


@app.get('/api/generate-cpf/')
def generate_cpf():
    """
    Generates a random CPF (Cadastro de Pessoas Físicas) number.

    Returns:
        str: A randomly generated CPF number.
    """
    gerador = Gerador_cpf()
    return gerador.gerador_cpf()


@app.get('/api/generate-cpfs/{quantidade}')
def generate_cpfs(quantidade: int):
    """
    Generate a given number of CPFs (Brazilian identification numbers).

    Args:
        quantidade (int): The number of CPFs to generate.

    Returns:
        list: A list of generated CPFs.

    """
    gerador = Gerador_cpf()
    return gerador.gerador_cpfs(quantidade)
