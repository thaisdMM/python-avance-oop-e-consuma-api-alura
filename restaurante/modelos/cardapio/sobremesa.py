from modelos.cardapio.item_cardapio import ItemCardapio


# 1- Crie uma classe chamada Sobremesa que herda de ItemCardapio,
class Sobremesa(ItemCardapio):
    # 2- adicione atributos específicos como tipo, tamanho e descricao à classe Sobremesa.
    def __init__(
        self, nome: str, preco: float, tipo: str, tamanho: str, descricao: str
    ):
        super().__init__(nome, preco)
        # 3- Ajuste a inicialização da classe para incluir esses novos atributos, possibilitando a criação de um novo item ao cardápio do restaurante.
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    # 4- Atualize o método __str__ conforme necessário para refletir essas mudanças.

    def __str__(self):
        return self._nome

    # 5- Certifique-se de que a classe Sobremesa mantenha a herança do método aplicar_desconto de ItemCardapio.
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.15
