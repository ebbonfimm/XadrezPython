from tipos import tCoordenada
from movimento import Movimento

class Peca:

    movimento = Movimento()

    def __init__(self, id, pos_x, pos_y, icone):
        self.id = id  # Formato NOME-COR-NUMERO
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.coordenada = [pos_x, pos_y]  # Representa a coordenada atual da Peca
        self.cor = self.__define_cor()
        self.icone = icone
        self.removida = False
        self.casa_inicial = True

    
    def exibe_detalhe(self) -> str:
        """Usado de forma pontual. Ao ser chamado, serve para visualizar rapidamente a posição atual da peça.

        Returns:
            str: String no formato: (x: {self.pos_x}) - (y: {self.pos_y})
        """
        return f"(x: {self.pos_x}) - (y: {self.pos_y})"
    

    def __define_cor(self) -> int:
        """Usado no construtor, serve para definir o código da cor da peça baseado no ID.

        Returns:
            int: Retorna 0 para peças Brancas e 1 para peças Pretas.
        """
        return 0 if self.id[1] == "B" else 1


    def calcula_movimento(self, movimentos: list) -> list[list[int, int]]:
        """Recebe a lista de todas as posições calculadas pelas peças, copia somente os movimentos válidos para uma segunda lista.

        Args:
            movimentos (list): Lista de movimentos possíveis, calculados previamente pelas classes especializadas.

        Returns:
            list[list[int, int]]: Lista contendo 1 ou mais listas de duas posições. Somente as posições válidas são devolvidas. Formato: [x, y].
        """
        movimentos_possíveis = []

        for possibilidade_movimento in movimentos:
            if self.__movimento_eh_valido(possibilidade_movimento):
                movimentos_possíveis.append(possibilidade_movimento)

        return movimentos_possíveis


    def mover_peca(self, x: int, y: int) -> list[int, int]:
        """Atribui as novas posições para a peça e define self.casa_inicial como False.

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
    

    def __movimento_eh_valido(self, par_ordenado: list[int, int]) -> bool:
        """Valida se determinado movimento é válido ou não baseado em 3 regras.
        - A coordenada de x não pode estar fora do conjunto [0, 1, 2, 3, 4, 5, 6, 7].
        - A coordenada de y não pode estar fora do conjunto [0, 1, 2, 3, 4, 5, 6, 7].
        - O par_ordenado não pode ser igual ao par ordenado formado pela posição atual da peça.

        Args:
            par_ordenado (list[int, int]): Lista contendo o par [x, y] gerado pela peça. Será usado para avaliar se é possível ou não.

        Returns:
            bool: True para posições válidas.
        """

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


    def calcula_movimento(self, casas_ocupadas: list) -> list[list[int, int]]:
        """Regra de movimento do Peão:
        - Não pode retroagir
        - Se a peça, naquele momento, estiver na casa inicial, o Peão pode andar 1 ou 2 casas
        - Caso contrário, apenas 1
        - A depender da cor do Peão, vai avançar para direções diferentes

        Returns:
            list[list[int, int]]: Movimentos gerados pela regra de movimentação da peça. PODE CONTER MOVIMENTOS INVÁLIDOS. (Vetor com 1 ou 2 posições calculadas)
        """

        movimentos = []

        iterador = range(1, 3)

        # Primeiro movimento
        if self.casa_inicial:
            if self.cor == 0:  # Caso a cor seja branca, a peça só pode avançar no tabuleiro "para cima".
                for i in iterador:
                    movimentos.append([self.pos_x, self.pos_y-i])
            else:
                for i in iterador:
                    movimentos.append([self.pos_x, self.pos_y+i])
        
        # Movimentos Seguintes
        else:
            if self.cor == 0:  # Caso a cor seja branca, a peça só pode avançar no tabuleiro "para cima".
                movimentos.append([self.pos_x, self.pos_y-1])
            else:
                movimentos.append([self.pos_x, self.pos_y+1])

        # Removendo Posições ocupadas.
        for casa in [*casas_ocupadas[0], *casas_ocupadas[1]]:
            
            # Verifica se tem uma peça imediamente a frente
            if casa in [[self.pos_x, self.pos_y + 1], [self.pos_x, self.pos_y - 1]]:
                movimentos = []
            
            # No primeiro movimento, caso calcule um movimento que já tem uma peça
            # Aqui é retirado este caso
            elif casa in movimentos:
                movimentos.remove(casa)


        return super().calcula_movimento(movimentos)


class Cavalo(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


    def calcula_movimento(self, casas_ocupadas: list) -> list[list[int, int]]:
        """Regra de movimento do Cavalo
        Observação: Por ser a regra mais complexa das peças, vou considerar um certo grau de entendimento do processo de desenho da regra para descrever.
        
        - Calcular os 4 limites: Considerando o movimento em "L" do cavalo, os limites são, a partir da casa atual da peça, as 4 casas que ficam a 2 casas de distância (Horizontal e Verticalmente).
        - Com os limites calculados, é preciso verificar se o limite "E" é um limite do X ou Y.
            - Caso seja do X, é preciso apenas criar as duas novas coordenadas deslocando X uma para cima e uma para baixo
            - Caso seja do Y, é preciso apenas criar as duas novas coordenadas deslocando Y uma para cima e uma para baixo
        - Esse processo é realizado para cada limite e considerando que o limite "E" só pode cair em uma das duas regras acima, são criadas 2 possíveis coordenadas para cada. Sendo assim, são geradas 8 posições (2 por limite, que são 4, resultando em 8).

        Returns:
            list[list[int, int]]: Movimentos gerados pela regra de movimentação da peça. PODE CONTER MOVIMENTOS INVÁLIDOS. (Vetor com 8 posições calculadas)
        """

        movimentos = []

        # Captura os limites dos eixos
        limites_eixo_x =  [[self.pos_x, self.pos_y-2], [self.pos_x, self.pos_y+2]]
        limites_eixo_y =  [[self.pos_x-2, self.pos_y], [self.pos_x+2, self.pos_y]]

        # Lista com todos os limites
        limites = [*limites_eixo_x, *limites_eixo_y]

        for i in limites:
            if i[0] == self.pos_x:
                movimentos.append([i[0]-1, i[1]])
                movimentos.append([i[0]+1, i[1]])
        
            else:
                movimentos.append([i[0], i[1]-1])
                movimentos.append([i[0], i[1]+1])

        # Removendo Posições ocupadas.
        for casa in casas_ocupadas[self.cor]:
            if casa in movimentos:
                movimentos.remove(casa)
            
        return super().calcula_movimento(movimentos)


class Bispo(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


    def calcula_movimento(self) -> list[list[int, int]]:
        """Regra de movimento do Bispo:

        ### Premissas:
        - Desconsiderando os limites do tabuleiro e a princípio sendo um tabuleiro "infinito", qualquer movimento do bispo deve levar em conta uma adição e/ou subtração do índice x e y.
        - Considerando um bispo alocado em uma casa C, pode ter no máximo 7 possibilidades de movimento para a diagonal em questão (Exemplo: Bispo em alguma extremidade absoluta do tabuleiro).

        ### Regra
        - Considerando a casa atual, limite_atual = 1 e limite_máximo = 7, são levadas em consideração os seguintes cálculos:
            - Diagonal Superior Esquerda = x - limite_atual & y - limite_atual
            - Diagonal Superior Direita = x + limite_atual & y - limite_atual
            - Diagonal Inferior Esquerda = x - limite_atual & y + limite_atual
            - Diagonal Inferior Direita = x + limite_atual & y + limite_atual
        - Para cada iteração do código, o limite atual é incrementado em 1 até que fique igual ao limite máximo

        Returns:
            list[list[int, int]]: Movimentos gerados pela regra de movimentação da peça. PODE CONTER MOVIMENTOS INVÁLIDOS. (Vetor com um número variado de posições calculadas)
        """

        movimentos = self.movimento.calcula_movimento_diagonal(self.coordenada)

        return super().calcula_movimento(movimentos)


class Dama(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)


    def calcula_movimento(self):
        """Regra de movimento da Dama
        - União da regra do Bispo com a Regra da Torre
        - Resulta em um vetor com todas as possibilidades Retilíneas + todas as possibilidades na Diagonal.

        Returns:
            list[list[int, int]]: Movimentos gerados pela regra de movimentação da peça. PODE CONTER MOVIMENTOS INVÁLIDOS. (Vetor com um número variado de posições calculadas)
        """

        movimentos = []

        movimento_retilinio = self.movimento.calcula_movimento_retilinio(self.coordenada)
        movimento_diagonal = self.movimento.calcula_movimento_diagonal(self.coordenada)

        movimentos = [*movimento_retilinio, *movimento_diagonal]

        return super().calcula_movimento(movimentos)


class Rei(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)

    
    def calcula_movimento(self, casas_ocupadas: list) -> list[list[int, int]]:
        """Regra de movimento do Rei
        - O rei pode andar 1 casa para qualquer direção
        - Sendo assim, é gerada uma matriz 3 x 3 com todas as casas ao redor do Rei. É feita uma iteração com complexidade O(n²) para gerar as 9 posições.

        Returns:
            list[list[int, int]]: Movimentos gerados pela regra de movimentação da peça. PODE CONTER MOVIMENTOS INVÁLIDOS. (Vetor com 9 posições calculadas)
        """

        movimentos = []

        for x in range(self.pos_x - 1, self.pos_x + 2):
            for y in range(self.pos_y - 1, self.pos_y + 2):

                movimentos.append([x, y])

        # Removendo Posições ocupadas.
        for casa in casas_ocupadas[self.cor]:
            if casa in movimentos:
                movimentos.remove(casa)

        return super().calcula_movimento(movimentos)


class Torre(Peca):
    def __init__(self, id, pos_x, pos_y, icone):
        super().__init__(id, pos_x, pos_y, icone)

     
    def calcula_movimento(self, casas_ocupadas: list[tCoordenada]) -> list[list[int, int]]:
        """Regras de movimento da Torre
        - A torre pode caminhar em movimento retilínio.
        - Sendo assim, são gerados 2 vetores com 8 posições, sendo elas:
            - Movimento Vertical: X congelado (no self.pos_x atual) + Todas as possibilidades de Y (de 0 até 8)
            - Movimento Horizontal: Y congelado (no self.pos_y atual) + Todas as possibilidades de X (de 0 até 8)

        Returns:
            list[list[int, int]]: Movimentos gerados pela regra de movimentação da peça. PODE CONTER MOVIMENTOS INVÁLIDOS. (Vetor com 16 posições calculadas)
        """

        # movimentos = self.movimento.calcula_movimento_retilinio(self.coordenada)

        movs_horizontal = [[i, self.pos_y] for i in range(0, 8)]
        movs_vertical = [[self.pos_x, i] for i in range(0, 8)]
        
        movimentos = [*movs_vertical, *movs_horizontal]

        return super().calcula_movimento(movimentos)
    

    