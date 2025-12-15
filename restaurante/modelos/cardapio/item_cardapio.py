# Usando classe abstrata
from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    # ABSTRAÇÃO: a classe mãe não precisa saber como vai ser implementado
    # molde para classes filhas - obrigatória implementação
    @abstractmethod
    def aplicar_desconto(self):
        pass
