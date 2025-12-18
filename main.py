from fastapi import FastAPI, Query
import requests

# FastAPI é um framework orientado a APIs (JSON)
# O FastAPI foi projetado desde a base para construir APIs HTTP modernas, e o formato padrão de comunicação de uma API é JSON.
# Em Python, o tipo de dado que representa naturalmente um JSON é o dicionário
# Para rodar a rota: uvicorn main:app --reload

# app: objeto de FastAPI
app = FastAPI()


# 1- Criando a primeira rota Hello World
#  servidor rodando localmente na nossa máquina
@app.get("/api/hello")
def hello_world():
    """
    Endpoint que exibe a mensagem tradicional mais usada no mundo da programação: 'Hello World'
    """
    # por isso que o retorno é um dict: formato padrão de comunicação de uma API é JSON
    return {"Hello": "World"}


# 2- Criando rota para os Restaurantes:
# /api/restaurantes/ - esse / depois do restaurantes é para dizer que terá outra informação ali, que vem da Query
# > exemplo: para acessar a rota de um dos restaurantes:
# http://127.0.0.1:8000/api/restaurantes/?restaurante=KFC
@app.get("/api/restaurantes/")
# parametro: restaurante -> para exibir informações específicas de um restaurante
# Query(especifico do fastapi) com o valor default None
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para ver os cardápios dos restaurantes.
    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        # se não não é passado um restaurante vai retornar todos os restaurantes do dados_json
        if restaurante is None:
            return {"Dados": dados_json}

        # aqui restaurante é passado
        dados_restaurante = []
        for item in dados_json:
            if item["Company"] == restaurante:
                dados_restaurante.append(
                    {
                        "item": item["Item"],
                        "price": item["price"],
                        "description": item["description"],
                    }
                )

        return {"Restaurate": restaurante, "Cardápio:": dados_restaurante}

    else:
        return {"Erro": f"{response.status_code} - {response.text}"}


# no html se colocar docs(http://127.0.0.1:8000/docs) da para ver informações sobre as rotas - formato Swagger
