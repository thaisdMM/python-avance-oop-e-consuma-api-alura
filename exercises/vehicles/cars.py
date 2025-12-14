from vehicle import Vehicle

# 3 Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo.


class Car(Vehicle):
    # 4 - No construtor da classe Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
    def __init__(self, make: str, model: str, doors: int):
        super().__init__(make, model)
        self.doors = doors

    # 5 - Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.
    def __str__(self):
        return f"{super().__str__()} | doors: {self.doors}"
