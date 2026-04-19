from peca import Peca


class Casa:
    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.coordenada = [pos_x, pos_y]
        self.livre = True
        self.peca: None | Peca = None
        self.cor = self.define_codigo_cor()


    def define_codigo_cor(self) -> int:
        """Função Interna, usada dentro do construtor para dizer qual é a cor da casa no tabuleiro.
           ### Considere:
            - 0 -> Casa Branca
            - 1 -> Casa Preta
            ### Regra:
            - Quando a divisão inteiro para as duas coordendas são iguais, então a casa é Preta.
            Caso contrário, ela é Branca.

        Returns:
            int: 0 e 1
        """
        result = 1
        if (self.pos_x % 2 == 0 and self.pos_y % 2 == 0) or (self.pos_x % 2 == 1 and self.pos_y % 2 == 1):
            result = 0
        return result
    

    def define_cor(self) -> str:
        """Função que define uma cor para a casa a partir do que foi definido pelo método define_codigo_cor().

        Returns:
            string: Retorna '■' para casas Brancas ou '□' para casas Pretas.
        """
        return '■' if self.cor == 0 else '□'
    

    def ocupar_casa(self, peca: Peca) -> bool:
        """Aloca uma peça (que é passada por parâmetro) na casa em questão.

        Args:
            peca (Peca ou Qualquer Especialização): Objeto do tipo peça que será alocado na casa

        Returns:
            bool: Retorna o atributo self.livre
        """
        self.livre = False
        self.peca = peca

        return self.livre
    

    def desocupar_casa(self) -> bool:
        """Remove a peça da casa em questão e define self.livre como True, pois não há mais peça naquela posição.

        Returns:
            bool: Retorna o atributo self.livre
        """
        self.peca = None
        self.livre = True

        return self.livre
    

    def exibe_descricao(self) -> str:
        """Exibe uma descrição detalhada da situação atual da casa em questão.

        Returns:
            str: Texto contendo a situação, Coordenada e peça
        """
        return f"Coordenada: ({self.pos_x}, {self.pos_y}) | {"Livre" if self.livre else "Ocupada"} | Peça: {self.peca.icone if self.peca else None}"


    def __str__(self):
        return f"{self.peca.icone if self.peca != None else self.define_cor()}"