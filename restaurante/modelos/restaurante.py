from modelos.avaliacao import Avaliacao


class Restaurante:
    """Representa um restaurante e suas características."""

    # atributo de classe
    restaurantes = []

    # construtor
    def __init__(self, nome: str, categoria: str):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        # atributo protegido
        self._ativo = False
        # para usar a classe avalição na pasta modelos
        self._avaliacao = []
        # toda vez que cria um objeto restaurante adiciona à lista
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f"{self._nome} | {self._categoria}"

    # não precisa de instanciar a classe para acessar esses métodos
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        # colocou entre chaves para manter a formatação :<25
        print(
            f"{'Nome do restaurante':<25} | {'Categoria':<25} | {'Avaliação':<25} | {'Status'}"
        )
        for restaurante in Restaurante.restaurantes:
            print(
                f"{restaurante._nome:<25} | {restaurante._categoria:<25} | {restaurante.media_avaliacoes:<25} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return "☑" if self._ativo else "☐"

    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avalicao(self, cliente: str, nota: float):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            # objeto da classe Avalicao em modelos
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    # 10- fez o metodo e depois transformou em property para ser capaz de ler esse metodo
    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return "-"
        # ternário - pega todas as notas de _avalicao e soma todas as notas
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        # usou o round para arrendondar e pegar só uma casa com 1
        media = round(soma_das_notas / quantidade_notas, 1)
        return media

    def adicionar_bebida_no_cardapio(self, bebida):
        self._cardapio.append(bebida)

    def adicionar_prato_no_cardapio(self, prato):
        self._cardapio.append(prato)
