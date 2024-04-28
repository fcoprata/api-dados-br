import requests


class Cep:
    @staticmethod
    def busca_Cep(cep: str):
        cep = cep.replace("-", "")
        url = f"https://viacep.com.br/ws/{cep}/json/"
        json_cep = requests.get(url)
        return json_cep
