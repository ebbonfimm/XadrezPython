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


    def calcula_movimento(self):
        movimentos_possíveis = []

        if self.casa_inicial:
            if self.pos_y < 4:  # Significa que são as peças pretas
                for i in range(1, 3):
                    movimentos_possíveis.append([self.pos_x, self.pos_y+i])

            elif self.pos_y >= 4:
                for i in range(1, 3):
                    movimentos_possíveis.append([self.pos_x, self.pos_y-i])

        else:
            if self.pos_y < 4:  # Significa que são as peças pretas
                movimentos_possíveis.append([self.pos_x, self.pos_y+1])

            elif self.pos_y >= 4:
                movimentos_possíveis.append([self.pos_x, self.pos_y-1])

        return movimentos_possíveis



    def __str__(self):
        return f"{id}"
    
