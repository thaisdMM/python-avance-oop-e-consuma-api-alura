from modelos.cardapio.item_cardapio import ItemCardapio

# HERANÇA: Bebida herda de ItemCardapio
class Bebida(ItemCardapio):
    def __init__(self, nome: str, preco: float, tamanho: str):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome