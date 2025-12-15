from vehicle_v2 import Vehicle


# 4-  Crie uma nova classe chamada Carro que herda da classe Veiculo.
class Car(Vehicle):
    # 5- No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
    def __init__(self, make: str, model: str, color: str):
        super().__init__(make, model)
        self.color = color

    def start(self):
        return f"The car {self.model} is on!"

    # Create method str to show the the instance in app.py
    def __str__(self):
        return f"Make: {self.make} | Model: {self.model} | Color: {self.color}\n {self.start()}"
