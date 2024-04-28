from fastapi import FastAPI
import uvicorn
from models.cpf import Cpf
from models.cnpj import Cnpj
from models.gerador_cpf import Gerador_cpf
from models.gerador_cnpj import Gerador_CNPJ
from models.cep import Cep

app = FastAPI()


@app.get('/api/cpf/is_valid/{cpf}')
def validate_cpf(cpf: str) -> str:
    """
    Validates a CPF (Cadastro de Pessoas Físicas) number.

    Args:
        cpf (str): The CPF number to be validated.

    Returns:
        bool: True if the CPF is valid, False otherwise.
    """
    if cpf is None:
        return "Passe um CPF"
    validador_cpf = Cpf(cpf)
    return validador_cpf.cpf_valid(cpf)


@app.get('/api/cnpj/is_valid/{cnpj}')
def validate_cnpj(cnpj: str) -> str:
    """
    Validates a CNPJ (Cadastro Nacional da Pessoa Jurídica) number.

    Args:
        cnpj (str): The CNPJ number to be validated.

    Returns:
        bool: True if the CNPJ is valid, False otherwise.
    """
    if cnpj is None:
        return "Passe um CNPJ"
    validador_cnpj = Cnpj(cnpj)
    return validador_cnpj.cnpj_valid(cnpj)


@app.get("/api/cpf/mascara/{cpf}")
def mascara_cpf(cpf: str) -> str:
    """
    Applies a mask to the given CPF (Cadastro de Pessoas Físicas) number.

    Args:
        cpf (str): The CPF number to apply the mask to.

    Returns:
        str: The CPF number with the mask applied.
    """
    validador_cpf = Cpf(cpf)
    return validador_cpf.mascara(cpf)


@app.get("/api/cnpj/mascara/{cnpj}")
def mascara_cnpj(cnpj):
    """
    Applies a mask to the given CNPJ number.

    Args:
        cnpj (str): The CNPJ number to be masked.

    Returns:
        str: The masked CNPJ number.
    """
    validador_cnpj = Cnpj(cnpj)
    return validador_cnpj.mascara(cnpj)


@app.get('/api/cpf/generate/')
def generate_cpf():
    """
    Generates a random CPF (Cadastro de Pessoas Físicas) number.

    Returns:
        str: A randomly generated CPF number.
    """
    gerador = Gerador_cpf()
    return gerador.gerador_cpf()


@app.get('/api/cnpj/generate/')
def generate_cnpj():
    """
    Generates a random CNPJ (Cadastro Nacional da Pessoa Jurídica) number.

    Returns:
        str: A randomly generated CNPJ number.
    """
    gerador = Gerador_CNPJ()
    return gerador.gerador_CNPJ()


@app.get('/api/cpf/generate/{quantidade}')
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


@app.get('/api/cnpj/generate/{quantidade}')
def generate_cnpjs(quantidade: int):
    """
    Generate a list of CNPJs.

    Args:
        quantidade (int): The number of CNPJs to generate.

    Returns:
        list: A list of generated CNPJs.
    """
    gerador = Gerador_CNPJ()
    return gerador.gerador_CNPJs(quantidade)


@app.get('/api/busca_cep/{cep}')
def buscador_cep(cep: str):
    buscar_cep = Cep()
    return buscar_cep.busca_Cep(cep)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
