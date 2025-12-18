import requests
import json

# link da url - esse endereço chama endpoint
url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

# resposta da requisição - get para pegar os dados
response = requests.get(url)

# # 1-
# print(response)
# # output: <Response [200]> - status_code: 200 sucesso -

# 2-

if response.status_code == 200:
    # para salvar os dados json
    dados_json = response.json()

    # #2- print para ver se deu certo os dados_json
    # print(dados_json)

    # 3- criar um dicionário que tenha todos os dados do restaurante para ir separando os dados
    dados_restaurante = {}
    for item in dados_json:
        # armazenar o nome dos restaurante que no json é Company
        nome_do_restaurante = item["Company"]
        # se o nome nao estiver dentro de dados_restaurante
        if nome_do_restaurante not in dados_restaurante:
            # começa com a lista vazia e vai 'popular' com os dados
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append(
            {
                "item": item["Item"],
                "price": item["price"],
                "description": item["description"],
            }
        )

else:
    print(f"O erro foi {response.status_code}")

# # 3- print para testar se a logica de dados_restaurante esta funcionando
# print(dados_restaurante["McDonald’s"])


# 4- salvar os dados em arquivos
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f"{nome_do_restaurante}.json"

    # criando arquivo json
    with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo_restaurante:
        # OBS: # ensure_ascii=False para conseguir ficar mais visual quando as palavras tiverem acento
        json.dump(dados, arquivo_restaurante, indent=4, ensure_ascii=False)
