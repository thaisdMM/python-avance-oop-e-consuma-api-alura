from vehicle import Vehicle

# 6- Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo chamado tipo ao construtor, indicando se a moto é esportiva ou casual.


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, motorcycle_type: str):
        super().__init__(make, model)
        self.motorcycle_type = motorcycle_type

    # 7- Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
    def __str__(self):
        return f"{super().__str__()} | Motorcycle type: {self.motorcycle_type}"
