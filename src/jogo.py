from tabuleiro import Tabuleiro
from peca import Peca
from dados import mapeamento_posicao_inicial_pecas, mapeamento_icone_pecas

tab = Tabuleiro()

def recebe_nova_posicao() -> list[int, int]:
    pos_x = int(input("Novo X >> "))
    pos_y = int(input("Novo Y >> "))

    return [pos_x, pos_y]


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
        indice_icone = [id[0] == x[0] for x in mapeamento_icone_pecas].index(True)
        icone = mapeamento_icone_pecas[list(mapeamento_icone_pecas.keys())[indice_icone]]

        # Cria todos os objetos de Peça e preenche a lista
        lista_pecas_criadas.append(
            Peca(id
                 , mapeamento_posicao_inicial[id][1]
                 , mapeamento_posicao_inicial[id][0]
                 , icone[0 if id[1] == "P" else 1]  # Verifica, pelo ID, qual é a cor. Assim decide qual é o ícone correto.
                )
            )
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


if __name__ == "__main__":

    # Cria as peças, retornando uma lista com todas elas (Lista de objetos do tipo Peca).
    pecas_criadas = inicializa_pecas(mapeamento_posicao_inicial=mapeamento_posicao_inicial_pecas, mapeamento_icones=mapeamento_icone_pecas)

    # Posiciona as peças na coordenada inicial, retornando um tabuleiro preenchido.
    _tab = preenche_tabuleiro(tab, pecas_criadas)

    imprime_tabuleiro(_tab)


    #######################################################################################

    # Testando funcionalidade de escolher qual peça quero mexer.
    print("\nQual peça deseja mexer? ")
    coord_x = int(input("Digite X >> "))
    coord_y = int(input("Digite Y >> "))

    casa = _tab.procura_casa((coord_x, coord_y))
    if not casa.livre:  # Se não está livre, então tem peça
        print(casa.exibe_descricao())

        peca = casa.peca  # Tenho agora a peça que eu selecionei
        casa.desocupar_casa()

        nova_pos = recebe_nova_posicao()
        peca.pos_x = nova_pos[0]
        peca.pos_y = nova_pos[1]

        _tab.procura_casa((peca.pos_x, peca.pos_y)).ocupar_casa(peca)

    print("Casa Vazia!")

    imprime_tabuleiro(tab)