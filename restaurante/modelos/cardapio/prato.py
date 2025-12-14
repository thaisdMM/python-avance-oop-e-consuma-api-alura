from modelos.cardapio.item_cardapio import ItemCardapio

# 1. HERANÇA: Prato herda de ItemCardapio
class Prato(ItemCardapio):
    def __init__(self, nome: str, preco: float, descricao: str):
        # super acessando informacao da classe base(mãe)
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome