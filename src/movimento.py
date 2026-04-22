from peca import Peca

class Movimento:
    def calcula_movimento_retilinio(self, peca: Peca):
        movs_horizontal = [[i, peca.pos_y] for i in range(0, 8)]
        movs_vertical = [[peca.pos_x, i] for i in range(0, 8)]
        
        movimentos = [*movs_vertical, *movs_horizontal]

        return movimentos

    def calcula_movimento_diagonal(self, peca: Peca):
        movimentos = []

        limite_atual = 1
        limite_maximo = 7

        while limite_atual <= limite_maximo:
            superior_esquerda = [peca.pos_x - limite_atual, peca.pos_y - limite_atual]
            superior_direita = [peca.pos_x + limite_atual, peca.pos_y - limite_atual]
            inferior_esquerda = [peca.pos_x - limite_atual, peca.pos_y + limite_atual]
            inferior_direita = [peca.pos_x + limite_atual, peca.pos_y + limite_atual]

            movimentos_propagados = [superior_esquerda, superior_direita, inferior_esquerda, inferior_direita]
            
            [movimentos.append(mov) for mov in movimentos_propagados]

            limite_atual+=1

        return movimentos