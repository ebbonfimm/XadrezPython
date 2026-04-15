class Jogador:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def __str__(self):
        return f"{self.nome} - Cor: {self.cor}"