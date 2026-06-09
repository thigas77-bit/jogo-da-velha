import random as rd


def exibir_tabuleiro(tabuleiro):
    """Desenha o estado atual do tabuleiro"""
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")


def validar_jogada(tabuleiro, posicao):
    """Retorna True se a posição está vazia e dentro do intervalo (1-9)"""
    if 1 <= posicao <= 9:
        return tabuleiro[posicao - 1] == " "
    return False


def verificar_vitoria(tabuleiro, jogador):
    """Retorna True se o jogador (X ou O) formou três em linha"""
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combinacao in combinacoes:
        if all(tabuleiro[i] == jogador for i in combinacao):
            return True
    return False


def verificar_empate(tabuleiro):
    """Retorna True se não há casas vazias"""
    return " " not in tabuleiro


def jogada_humano(tabuleiro, jogador, nome):
    """Lê e processa a jogada do humano, chamando as validações"""
    while True:
        try:
            posicao = int(input(f"\n{nome} ({jogador}), escolha uma posição de 1 a 9:\n"))
            if validar_jogada(tabuleiro, posicao):
                tabuleiro[posicao - 1] = jogador
                break
            elif 1 <= posicao <= 9:
                print("Posição ocupada!")
            else:
                print("Digite um número de 1 a 9")
        except ValueError:
            print("Entrada inválida! Digite um número de 1 a 9.")


def jogada_computador(tabuleiro, jogador):
    """Implementa a IA com lógica de prioridade decrescente"""
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    # 1. Vitória imediata
    for combinacao in combinacoes:
        valores = [tabuleiro[i] for i in combinacao]
        if valores.count("O") == 2 and valores.count(" ") == 1:
            posicao = combinacao[valores.index(" ")]
            tabuleiro[posicao] = "O"
            print(f'A IA🤖 escolheu a posição {posicao + 1}\n')
            return

    # 2. Bloqueio
    for combinacao in combinacoes:
        valores = [tabuleiro[i] for i in combinacao]
        if valores.count("X") == 2 and valores.count(" ") == 1:
            posicao = combinacao[valores.index(" ")]
            tabuleiro[posicao] = "O"
            print(f'A IA🤖 escolheu a posição {posicao + 1}\n')
            return

    # 3. Centro
    if tabuleiro[4] == " ":
        tabuleiro[4] = "O"
        print('A IA🤖 escolheu a posição 5\n')
        return

    # 4. Canto vazio
    cantos = [i for i in [0, 2, 6, 8] if tabuleiro[i] == " "]
    if cantos:
        posicao = rd.choice(cantos)
        tabuleiro[posicao] = "O"
        print(f'A IA🤖 escolheu a posição {posicao + 1}\n')
        return

    # 5. Qualquer posição vazia restante
    vazias = [i for i in range(9) if tabuleiro[i] == " "]
    posicao = rd.choice(vazias)
    tabuleiro[posicao] = "O"
    print(f'A IA🤖 escolheu a posição {posicao + 1}\n')


def menu_principal():
    """Exibe as opções de modo de jogo e retorna a escolha do usuário"""
    print('     -----SEJA BEM-VINDO!-----\n')
    print('Você jogará o MELHOR jogo da velha🤯🤯\n')

    nome_usuario = input('Digite o nome do usuário:\n')
    print(f'\n{nome_usuario}, escolha um modo de jogo:')
    print('1. Jogar com um amigo😃😃\n2. Jogar contra a I.A🤖\n')

    while True:
        try:
            modo = int(input('Escolha a opção de jogo:\n'))
            if modo in [1, 2]:
                break
            else:
                print("Digite 1 ou 2.")
        except ValueError:
            print("Entrada inválida! Digite 1 ou 2.")

    if modo == 1:
        jogador1 = input('Nome do jogador 1:\n')
        jogador2 = input('Nome do jogador 2:\n')
    else:
        jogador1 = input('Nome do jogador 1:\n')
        jogador2 = 'I.A🤖'

    return modo, jogador1, jogador2


def iniciar():
    """Função principal de fluxo do jogo"""
    modo, jogador1, jogador2 = menu_principal()

    tabuleiro = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]

    jogador_atual = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)

        if jogador_atual == "X":
            jogada_humano(tabuleiro, 'X', jogador1)

            if verificar_vitoria(tabuleiro, 'X'):
                exibir_tabuleiro(tabuleiro)
                print(f'🏆 {jogador1} venceu!')
                break

            if verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print('🤝 O jogo terminou em empate!')
                break

            jogador_atual = 'O'

        else:
            if jogador2 == 'I.A🤖':
                jogada_computador(tabuleiro, 'O')
            else:
                jogada_humano(tabuleiro, 'O', jogador2)

            if verificar_vitoria(tabuleiro, 'O'):
                exibir_tabuleiro(tabuleiro)
                print(f'🏆 {jogador2} venceu!')
                break

            if verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print('🤝 O jogo terminou em empate!')
                break

            jogador_atual = 'X'


iniciar()
