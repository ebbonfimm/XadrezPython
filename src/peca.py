class Peca:
    def __init__(self, id, pos_x, pos_y, icone):
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.coordenada = (pos_x, pos_y)  # Representa a coordenada atual da Peca
        self.cor = 1
        self.icone = icone
        self.removida = False
        self.casa_inicial = True

    
    def exibe_detalhe(self):
        return f"(x: {self.pos_x}) - (y: {self.pos_y})"


    def __str__(self):
        return f"{id}"
