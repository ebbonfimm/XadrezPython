from tabuleiro import Tabuleiro
from peca import Peca, Peao, Torre, Rei, Dama, Cavalo, Bispo
from dados import mapeamento_posicao_inicial_pecas, mapeamento_icone_pecas

import os


def clear_cmd():
    os.system('cls')


def inicializa_pecas(
        mapeamento_posicao_inicial: dict[list[int, int]], 
        mapeamento_icones: dict[list[str, str]]
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
    for id in mapeamento_posicao_inicial.keys():  # Possui as 32 peças do tabuleiro para serem iteradas

        # Lógica para capturar o ícone adequado para a peça, a depender da sua cor
        indice_icone = [id[0] == x[0] for x in mapeamento_icones].index(True)
        icone = mapeamento_icones[list(mapeamento_icones.keys())[indice_icone]]

        tipo_da_peca = id[0]
        dados_objeto = [id, mapeamento_posicao_inicial[id][1], mapeamento_posicao_inicial[id][0], icone[0 if id[1] == "P" else 1]]

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


def imprime_tabuleiro(tab: Tabuleiro) -> None:
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

    # Quebra a linha e adiciona a borda superior do tabuleiro para começar a imprimir as linhas.
    print("\n  ┌" + "═"*17 + "┐")
    # Itera por cada uma das linhas do tabuleiro.
    for row in tab.tabuleiro:
        # Imprime o índice de cada linha e adiciona um " │ " no final antes de imprimir as casas daquela linha.
        print(linhas[contador], end=" ║ ")
        # Imprime cada casa da linha que está sendo iterada, dando um espaço entre cada casa.
        [print(casa, end=" ") for casa in row]
        # Ao final de cada linha, é impresso um "│ " (Não tem um espaço antes, pois na impressão anterior, o último termo já tem um espaço no final).
        print("║ ")
        # Aumenta uma undiade no contador, para que cada linha tenha impresso o seu número correto.
        contador+=1
    # Depois de imprimir a última linha do tabuleiro, é adicionado uma borda.
    print("  └" + "═"*17, end="┘\n")
    # Adição de 4 espaços para o número das colunas fica visualmente coerente ao tabuleiro.
    print(" "*4, end="")
    # Impressão dos números das colunas.
    [print(x, end=" ") for x in range(0, 8)]
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

    tab = Tabuleiro()

    # Cria as peças, retornando uma lista com todas elas (Lista de objetos do tipo Peca).
    pecas_criadas = inicializa_pecas(mapeamento_posicao_inicial=mapeamento_posicao_inicial_pecas, mapeamento_icones=mapeamento_icone_pecas)

    # # Posiciona as peças na coordenada inicial, retornando um tabuleiro preenchido.
    _tab = preenche_tabuleiro(tab, pecas_criadas)

    imprime_tabuleiro(_tab)

    #######################################################################################

    for i in range(0,1000):
        # Testando funcionalidade de escolher qual peça quero mexer.
        par_coord = captura_coordenada("Informe a posição da peça que deseja mexer:")

        casa = _tab.procura_casa((par_coord[0], par_coord[1]))
        if not casa.livre:  # Se não está livre, então tem peça

            peca = casa.peca  # Tenho agora a peça que eu selecionei
            print(peca)

            lista_possibilidades = peca.calcula_movimento()

            contador = 1
            for i in lista_possibilidades:
                print(f"{contador} - {i}")
                contador+=1

            opt = int(input("Opção >> "))

            #Thiago
            while opt > len(lista_possibilidades):
                print("Selecione outra peça !!!") 
                opt = int(input("Opção >> "))
            #fim

            peca.mover_peca(lista_possibilidades[opt-1][0], lista_possibilidades[opt-1][1])

            casa.desocupar_casa()

            nova_casa = _tab.procura_casa((lista_possibilidades[opt-1][0], lista_possibilidades[opt-1][1]))
            nova_casa.ocupar_casa(peca)

            clear_cmd()

            imprime_tabuleiro(_tab)
    