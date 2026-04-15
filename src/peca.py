class Peca:
    def __init__(self, id, pos_x, pos_y, icone):
        self.id = id  # Formato NOME-COR-NUMERO
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.coordenada = (pos_x, pos_y)  # Representa a coordenada atual da Peca
        self.cor = self.define_cor()
        self.icone = icone
        self.removida = False
        self.casa_inicial = True

    
    def exibe_detalhe(self):
        return f"(x: {self.pos_x}) - (y: {self.pos_y})"
    

    def define_cor(self):
        return 0 if self.id[1] == "B" else 1


    def calcula_movimento(self, movimentos: list):
        movimentos_possíveis = []

        [movimentos_possíveis.append(mov) for mov in movimentos]

        return movimentos_possíveis


    def mover_peca(self, x: int, y: int) -> list[int, int]:
        """_summary_

        Args:
            x (int): Nova posição X no tabuleiro
            y (int): Nova posição Y no tabuleiro

        Returns:
            list[int, int]: Posição Atual, após mover a peça.
        """
        self.pos_x = x
        self.pos_y = y

        self.casa_inicial = False

        return [x, y]


    def __str__(self):
        return f"{self.id}"
    

class Peao(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


class Cavalo(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


class Bispo(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


class Dama(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


class Rei(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


class Torre(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)

     
    def calcula_movimento(self):

        movs_horizontal = [[i, self.pos_y] for i in range(0, 8)]
        movs_vertical = [[self.pos_x, i] for i in range(0, 8)]
        
        movimentos = [*movs_vertical, *movs_horizontal]

        return super().calcula_movimento(movimentos)
    



    