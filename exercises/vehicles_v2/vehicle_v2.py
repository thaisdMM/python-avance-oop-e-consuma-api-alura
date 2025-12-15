from abc import ABC, abstractmethod


# 1- Crie uma classe chamada Veiculo...
class Vehicle(ABC):
    # 3- No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    # 2- ...com um método abstrato chamado ligar.
    @abstractmethod
    def start(self):
        pass
