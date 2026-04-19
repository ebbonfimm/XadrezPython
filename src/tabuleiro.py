from casa import Casa

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[Casa(column, row) for column in range(0,8)] for row in range(0,8)]


    def procura_casa(self, coordenada: list[int, int]) -> Casa:
        """Função usada para retornar para o jogo, a casa que seja usada para ocupar ou ser desocupada.

        Args:
            coordenada list[int]: Uma lista contendo 2 elementos, sendo o de índice 0 = posição X e o de índice 1 = posição Y

        Returns:
            _type_: Retorna um objeto do tipo Casa na posição passada para o método
        """
        x = coordenada[0]
        y = coordenada[1]
        return self.tabuleiro[y][x]
    
    
    def calcula_casas_ocupadas(self):
        casas = []
        for x in self.tabuleiro:
            for y in x:
                if not y.livre: casas.append(y)

        return casas
        



    def __str__(self):
        return [[casa.__str__() for casa in row] for row in self.tabuleiro]