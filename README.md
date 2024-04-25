# API de Validação de CPF, CNPJ e CEP

Esta é uma API construída com FastAPI que permite validar CPF, CNPJ e CEP.

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd seu-repositorio
    ```

3. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Inicie o servidor da API:

    ```bash
    uvicorn main:app --reload
    ```

2. Faça uma requisição para validar um CPF:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"cpf": "12345678900"}' http://localhost:8000/validate/cpf
    ```

    A resposta será um JSON indicando se o CPF é válido ou não.

3. Faça uma requisição para validar um CNPJ:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"cnpj": "12345678000199"}' http://localhost:8000/validate/cnpj
    ```

    A resposta será um JSON indicando se o CNPJ é válido ou não.

4. Faça uma requisição para validar um CEP:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"cep": "12345678"}' http://localhost:8000/validate/cep
    ```

    A resposta será um JSON contendo informações sobre o CEP, como logradouro, bairro, cidade e estado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).