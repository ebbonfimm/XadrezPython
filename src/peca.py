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

        for possibilidade_movimento in movimentos:
            if self.__movimento_eh_valido(possibilidade_movimento):
                movimentos_possíveis.append(possibilidade_movimento)

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
    

    def __movimento_eh_valido(self, par_ordenado: list[int, int]):

        lista_posicoes_validas = range(0, 8)

        result = True
        if par_ordenado[0] not in lista_posicoes_validas or \
            par_ordenado[1] not in lista_posicoes_validas or \
            par_ordenado == [self.pos_x, self.pos_y]:  
            # Caso o par ordenado recebido seja a própria posição atual 

                result = False

        return result


    def __str__(self):
        return f"{self.id}"
    

class Peao(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


    def calcula_movimento(self):

        movimentos = []

        if self.casa_inicial:
            iterador = range(1, 3)
            
            if self.cor == 0:  # Caso a cor seja branca, a peça só pode avançar no tabuleiro "para cima".
                for i in iterador:
                    movimentos.append([self.pos_x, self.pos_y-i])
            else:
                for i in iterador:
                    movimentos.append([self.pos_x, self.pos_y+i])
        
        else:
            if self.cor == 0:
                movimentos.append([self.pos_x, self.pos_y-1])
            else:
                movimentos.append([self.pos_x, self.pos_y+1])

        return super().calcula_movimento(movimentos)


class Cavalo(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


class Bispo(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


    def calcula_movimento(self,):

        movimentos = []

        limite_atual = 1
        limite_maximo = 7

        while limite_atual <= limite_maximo:
            superior_esquerda = [self.pos_x - limite_atual, self.pos_y - limite_atual]
            superior_direita = [self.pos_x + limite_atual, self.pos_y - limite_atual]
            inferior_esquerda = [self.pos_x - limite_atual, self.pos_y + limite_atual]
            inferior_direita = [self.pos_x + limite_atual, self.pos_y + limite_atual]

            movimentos_propagados = [superior_esquerda, superior_direita, inferior_esquerda, inferior_direita]
            
            [movimentos.append(mov) for mov in movimentos_propagados]

            limite_atual+=1

        return super().calcula_movimento(movimentos)


class Dama(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


class Rei(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)

    
    def calcula_movimento(self):

        movimentos = []

        for x in range(self.pos_x - 1, self.pos_x + 2):
            for y in range(self.pos_y - 1, self.pos_y + 2):

                movimentos.append([x, y])

        return super().calcula_movimento(movimentos)


class Torre(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)

     
    def calcula_movimento(self):

        movs_horizontal = [[i, self.pos_y] for i in range(0, 8)]
        movs_vertical = [[self.pos_x, i] for i in range(0, 8)]
        
        movimentos = [*movs_vertical, *movs_horizontal]

        return super().calcula_movimento(movimentos)
    



    