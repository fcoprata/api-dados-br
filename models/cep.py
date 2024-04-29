import requests


class Cep:
    """
    This class provides methods to search for CEP (Brazilian postal code)
    information.

    Methods:
        busca_Cep(cep: str) -> dict:
            Retrieves the CEP information from the ViaCEP API.

    Usage:
        cep = Cep()
        cep_info = cep.busca_Cep("12345-678")
        print(cep_info)
    """

    @staticmethod
    def busca_Cep(cep: str):
        """
        Retrieves the CEP information from the ViaCEP API.

        Args:
            cep (str): The CEP to search for.

        Returns:
            dict: A dictionary containing the CEP information.

        Raises:
            ValueError: If the CEP format is invalid.

        Example:
            cep = Cep()
            cep_info = cep.busca_Cep("12345-678")
            print(cep_info)
        """
        cep = cep.replace("-", "")
        if cep.isdigit() or len(cep) == 8:
            raise ValueError("Invalid CEP format")

        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        json_cep = response.json()
        return json_cep
