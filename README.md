# API de Validação de CPF, CNPJ e CEP

![API Dados Br]('https://github.com/fcoprata/api-dados-br/blob/development/assets/Api%20dados%20Br.jpg')

Esta é uma API construída com FastAPI que permite validar CPF, CNPJ e CEP.

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/fcoprata/api-dados-br
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd api-dados-br
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

4. Faça uma requisição para validar um CEP 🚧:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"cep": "12345678"}' http://localhost:8000/validate/cep
    ```

    A resposta será um JSON contendo informações sobre o CEP, como logradouro, bairro, cidade e estado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.


## TODO
- Implementar CNPJ e CEP

## License

```
The MIT License (MIT)

Copyright (c) 2024 Francisco Prata Cavalcante Neto

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```