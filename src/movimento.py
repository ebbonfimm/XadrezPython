from tipos import tCoordenada

class Movimento:

    
    def calcula_movimento_retilinio(self, coordenada: tCoordenada):

        movs_horizontal = [[i, coordenada[1]] for i in range(0, 8)]
        movs_vertical = [[coordenada[0], i] for i in range(0, 8)]
        
        movimentos = [*movs_vertical, *movs_horizontal]

        return movimentos
    

    def calcula_movimento_diagonal(self, coordenada: tCoordenada):
        movimentos = []

        limite_atual = 1
        limite_maximo = 7

        while limite_atual <= limite_maximo:
            superior_esquerda = [coordenada[0] - limite_atual, coordenada[1] - limite_atual]
            superior_direita =  [coordenada[0] + limite_atual, coordenada[1] - limite_atual]
            inferior_esquerda = [coordenada[0] - limite_atual, coordenada[1] + limite_atual]
            inferior_direita =  [coordenada[0] + limite_atual, coordenada[1] + limite_atual]

            movimentos_propagados = [superior_esquerda, superior_direita, inferior_esquerda, inferior_direita]
            
            [movimentos.append(mov) for mov in movimentos_propagados]

            limite_atual+=1

        return movimentos
