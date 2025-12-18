import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    cotacao = float(data["USDBRL"]["bid"])
    mensagem = f"UU$ 1 dólar corresponde a R$ {cotacao:.2f}"
    print(mensagem)
else:
    print(f"A requisição falhou com o código de status {response.status_code}")
