from tabuleiro import Tabuleiro
from casa import Casa
from peca import Peca, Peao, Torre, Rei, Dama, Cavalo, Bispo
from dados import mapeamento_posicao_inicial_pecas, mapeamento_icone_pecas, teste_mapeamento_posicao_inicial_pecas
from cores import coresterminal as ct

import os


def clear_cmd():
    os.system('cls')


def print_colorir_tabuleiro(casa: Casa, lista_movimentos: list) -> None:

    result = casa.__str__()

    # Valida se casa faz parte da lista de movimentos
    if casa.coordenada in lista_movimentos:
        result = ct.AZUL + result + ct.FINAL

    # Sobreescreve a cor, caso tenha uma peça
    if not casa.livre:  # Se não está livre, logo, tem uma peça
        result = ct.VERDE + result + ct.FINAL

    print(result, end=" ")


def print_casa_colorida(casa: Casa, lista_movimentos):

    result = casa.__str__()

    print(ct.AZUL + result + ct.FINAL if casa.peca != None and casa.coordenada in lista_movimentos else casa, end=" ")



def inicializa_pecas(
        depara_posicao_inicial: dict[list[int, int]],
        depara_icones: dict[list[str, str]]
    ) -> list[Peca]:
    """_summary_
    Função responsável por criar todas as 32 peças necessárias para a partida iniciar. Leva em consideração um mapeamento manual feito previamente, com a posição inicial de cada peça e seus respectivos ícones.

    Args:
        mapeamento_posicao_inicial (dict[list[int, int]]): Um dicionário contendo o ID de cada peça respeitamento o padrão NOME-COR-NUMERO e suas respectivas posições iniciais.
        mapeamento_icones (dict[list[str, str]]): Dicionário contendo o par de ícones na cor Branca e Preta para cada peça.

    Returns:
        list[Peca]: Uma lista contendo todas as 32 peças adequadamente criadas.
    """
    
    # Lista vazia para que posteriormente seja preenchida com as peças criadas.
    lista_pecas_criadas = []

    # Percorre todo o conjunto do mapeamento da posição inicial de cada uma das peças (que foi criado previamente e de forma manual)
    for id in depara_posicao_inicial.keys():  # Possui as 32 peças do tabuleiro para serem iteradas

        # Lógica para capturar o ícone adequado para a peça, a depender da sua cor
        indice_icone = [id[0] == x[0] for x in depara_icones].index(True)
        icone = depara_icones[list(depara_icones.keys())[indice_icone]]

        tipo_da_peca = id[0]
        dados_objeto = [id, depara_posicao_inicial[id][0], depara_posicao_inicial[id][1], icone[0 if id[1] == "P" else 1]]

        # Define qual é a classe que deverá ser utilizada, dependendo da nomenclatura da peça.
        if tipo_da_peca == "T": obj_peca = Torre(*dados_objeto)
        elif tipo_da_peca == "P": obj_peca = Peao(*dados_objeto)
        elif tipo_da_peca == "D": obj_peca = Dama(*dados_objeto)
        elif tipo_da_peca == "R": obj_peca = Rei(*dados_objeto)
        elif tipo_da_peca == "C": obj_peca = Cavalo(*dados_objeto)
        elif tipo_da_peca == "B": obj_peca = Bispo(*dados_objeto)

        # Cria todos os objetos de Peça e preenche a lista
        lista_pecas_criadas.append(obj_peca)

    return lista_pecas_criadas


def imprime_tabuleiro(tab: Tabuleiro, colorir = False, lista_movimentos = []) -> None:
    """Imprime o tabuleiro em um formato ornamentado. Esse método será utilizado durante toda a partida para exibir o tabuleiro com seu estado atual.

    A impressão contém:
    - Coordenadas de apoio do lado de fora do tabuleiro
    - Borda formatada
    - Casas do Xadrez

    Args:
        tab (Tabuleiro): Objeto da Classe Tabuleiro
    """
    contador: int = 0
    linhas: list[int] = range(0, 8)
    # Adição de 4 espaços para o número das colunas fica visualmente coerente ao tabuleiro.
    print(" "*4, end="")
    # Impressão dos números das colunas.
    [print(x, end=" ") for x in range(0, 8)]
    # Quebra a linha e adiciona a borda superior do tabuleiro para começar a imprimir as linhas.
    print("\n  ┌" + "═"*17 + "┐")
    # Itera por cada uma das linhas do tabuleiro.
    for row in tab.tabuleiro:
        # Imprime o índice de cada linha e adiciona um " │ " no final antes de imprimir as casas daquela linha.
        print(linhas[contador], end=" ║ ")

        # Coloração da Casa:
        if colorir:
            [print_colorir_tabuleiro(casa, lista_movimentos) for casa in row]
        else:
            [print(casa, end=" ") for casa in row]

        
        # Ao final de cada linha, é impresso um "│ " (Não tem um espaço antes, pois na impressão anterior, o último termo já tem um espaço no final).
        print("║ ")
        # Aumenta uma undiade no contador, para que cada linha tenha impresso o seu número correto.
        contador+=1
    # Depois de imprimir a última linha do tabuleiro, é adicionado uma borda.
    print("  └" + "═"*17, end="┘\n")
    # Quebra a linha ao final de todas as impressões
    print()


def preenche_tabuleiro(tabuleiro: Tabuleiro ,pecas: list[Peca]) -> Tabuleiro:
    
    for peca in pecas_criadas:
        casa = tabuleiro.procura_casa(peca.coordenada)
        casa.ocupar_casa(peca)

    return tabuleiro


def captura_coordenada(texto: str) -> list[int, int]:
    """Método para capturar a coordenada X e Y vindo do usuário.

    Args:
        texto (str): Texto que aparece na interação com o usuário.

    Returns:
        list[int, int]: [posicao x, posicao y]
    """
    print(texto)
    x = int(input("X >> "))
    y = int(input("Y >> "))

    return [x, y]
    

if __name__ == "__main__":

    # =======================================
    # LIMPEZA DA TELA
    # =======================================
    clear_cmd()

    # Inicializa um Tabuleiro Vazio
    tab = Tabuleiro()

    # =============================================================================================
    # INICIALIZA DAS PEÇAS DO XADREZ
    # Cria as peças, retornando uma lista com todas elas (Lista de objetos do tipo Peca).
    # =============================================================================================
    PECAS_TESTE = True

    if PECAS_TESTE:
        # =============================================================================================
        # Cria as peças com os dados de TESTE
        # =============================================================================================
        pecas_criadas = inicializa_pecas(depara_posicao_inicial=teste_mapeamento_posicao_inicial_pecas, depara_icones=mapeamento_icone_pecas)
    else:
        # =============================================================================================
        # Cria as peças com a posição REAL
        # =============================================================================================
        pecas_criadas = inicializa_pecas(depara_posicao_inicial=mapeamento_posicao_inicial_pecas, depara_icones=mapeamento_icone_pecas)

    # =============================================================================================
    # PREENCHIMENTO DO TABULEIRO
    # Posiciona as peças na coordenada inicial, retornando um tabuleiro preenchido.
    # =============================================================================================
    _tab = preenche_tabuleiro(tab, pecas_criadas)

    # =============================================================================================
    # ITERAÇÃO DA PARTIDA
    # =============================================================================================
    for i in range(0,1000):
        
        clear_cmd()

        # Imprime Inicialmente
        imprime_tabuleiro(_tab, colorir=True)

        # Testando casas ocupadas:
        obj_casas_ocupadas = _tab.calcula_casas_ocupadas()
        coordenada_casas_ocupadas = [casa.coordenada for casa in obj_casas_ocupadas]

        # =============================================================================================
        # MOVIMENTAÇÃO DAS PEÇAS
        # =============================================================================================
        # Jogador seleciona a peça que deseja mover
        par_coord = captura_coordenada("Informe a posição da peça que deseja mexer:")

        # Procura a casa que o jogador informou e verifica se há uma peça
        casa = _tab.procura_casa((par_coord[0], par_coord[1]))
        if not casa.livre:  # Se não está livre, então tem peça

            # Peça Selecionada
            peca = casa.peca
            # Calcula as possibilidades de movimento
            lista_possibilidades = peca.calcula_movimento(coordenada_casas_ocupadas)

            # =======================================
            # LIMPEZA DA TELA
            # =======================================
            # clear_cmd()
            imprime_tabuleiro(_tab, colorir=True, lista_movimentos=lista_possibilidades)

            # Imprime as possibilidades calculadas pelas peças
            # Recebe a opção de movimento do jogador
            contador = 1
            for i in lista_possibilidades:
                print(f"{contador} - {i}")
                contador+=1
            opt = int(input("Opção >> "))

            # Efetivamente move a peça
            peca.mover_peca(lista_possibilidades[opt-1][0], lista_possibilidades[opt-1][1])
            casa.desocupar_casa()
            nova_casa = _tab.procura_casa((lista_possibilidades[opt-1][0], lista_possibilidades[opt-1][1]))
            nova_casa.ocupar_casa(peca)

            # =======================================
            # LIMPEZA DA TELA
            # =======================================
            clear_cmd()
        else:
            # Utilizo o método input para o código ficar parado esperando a interação do usuário.
            input(f"Peça não encontrada na posição: {par_coord} >> ")
            pass
    