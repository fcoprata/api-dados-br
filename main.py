from modelos.cpf import Cpf
from modelos.gerador_cpf import Gerador_cpf
from fastapi import FastAPI

app = FastAPI()


@app.get('/api/is_valid/{cpf}')
def validate_cpf(cpf):
    validador_cpf = Cpf(cpf)
    return validador_cpf.cpf_valid(cpf)


@app.get("/api/mascara/{cpf}")
def mascara(cpf):
    validador_cpf = Cpf(cpf)
    return validador_cpf.mascara(cpf)


@app.get('/api/generate-cpf/')
def generate_cpf():
    gerador = Gerador_cpf()
    return gerador.gerador_cpf()
