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

        Raises a ValueError if the CEP format is invalid.
        The CEP format should be in the format "XXXXX-XXX",
        where X represents a digit.
        The function makes a GET request to the ViaCEP API
        using the provided CEP.
        If the request is successful (status code 200),
        it returns a dictionary containing the CEP information.
        If the CEP is not found, it returns the string "CEP not found".
        If the request fails,it raises a ValueError with the message
        "Failed to retrieve CEP information".
        """
        cep = cep.replace("-", "")
        if not cep.isdigit() or len(cep) != 8:
            raise ValueError("Formato invalido do CEP")

        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            json_cep = response.json()
            if "error" in json_cep and json_cep["error"]:
                return "CEP não encontrado"
            return json_cep
        else:
            raise ValueError("Failed to retrieve CEP information")
