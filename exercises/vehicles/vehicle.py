# 1- Crie uma Classe Pai (Veiculo):
# 2- Construa o Método Especial str:
# 3 Crie uma Classe Filha (Carro)
# 5 - Implemente o Método Especial str na Classe Filha:
# 6- Crie uma Classe Filha (Moto):
# 7- Implemente o Método Especial str na Classe Filha (Moto):
# 8- Crie um Arquivo Main (main.py):
# 9- Importe e Instancie Objetos: No arquivo main.py
# 11- Exiba as Informações:

# 1- Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, marca e modelo.


class Vehicle:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        # 2- A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
        self._started = False

    # 2- Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada com a marca, modelo e o estado de ligado/desligado do veículo.
    def __str__(self):
        start = "on" if self._started else "off"
        return f"Make: {self.make} | Model: {self.model} | Vehicle is: {start}"
