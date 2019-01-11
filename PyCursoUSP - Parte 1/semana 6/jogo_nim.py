def computador_escolhe_jogada(n, m):
    """     
    o compuador vai retirar n peças de acordo com a estratégia de ganhar sempre
    """
    computadorRetira = 1
    while computadorRetira != m:
        if (n - computadorRetira) % (m + 1) == 0:
            return computadorRetira
        else:
            computadorRetira += 1
    n -= computadorRetira

    return computadorRetira


def usuario_escolhe_jogada(n, m):
    """     
    o usuário faz sua escolha e caso a jogada seja inválida, recebe um aviso
    """
    while 1:
        print()
        usuarioRetira = int(input('Quantas peças você vai tirar? '))
        if usuarioRetira > m or usuarioRetira < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            break

    return usuarioRetira


def partida():
    """
    a partida inicia com o computador ou o usuário segundo o critério de que o computado vencerá sempre
    """
    
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    # condição de início do jogo segundo a estratégia do computador ganhar sempre
    # aqui está o segredo: o computador que decida quem começa. Por isso ganha sempre
    if n % (m + 1) == 0:
        print()
        print('Voce começa!')

        while n != 0:
            usuarioRetira = usuario_escolhe_jogada(n, m)
            n -= usuarioRetira
            if usuarioRetira == 1:
                print()
                print('Você tirou uma peça')
            elif usuarioRetira == 0:
                break
            else:
                print()
                print('Você tirou', usuarioRetira, 'peças')
            # mensagem de quantas peças sobraram
            if n == 1:
                print()
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n == 0:
                break
            else:
                print()
                print('Agora restam', n, 'peças no tabuleiro.')

            computadorRetira = computador_escolhe_jogada(n, m)
            n -= computadorRetira
            # mensagem de quantas peças são retiradas
            if computadorRetira == 1:
                print()
                print('O computador tirou uma peça')
            elif computadorRetira == 0:
                break
            else:
                print()
                print('O computador tirou', computadorRetira, 'peças')
            # mensagem de quantas peças sobraram
            if n == 1:
                print()
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n == 0:
                break
            else:
                print()
                print('Agora restam', n, 'peças no tabuleiro.')
    else:
        print()
        print('Computador começa!')

        while n != 0:
            computadorRetira = computador_escolhe_jogada(n, m)
            n -= computadorRetira
            # mensagem de quantas peças são retiradas
            if computadorRetira == 1:
                print()
                print('O computador tirou uma peça')
            elif computadorRetira == 0:
                break
            else:
                print()
                print('O computador tirou', computadorRetira, 'peças')
            # mensagem de quantas peças sobraram
            if n == 1:
                print()
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n == 0:
                break
            else:
                print()
                print('Agora restam', n, 'peças no tabuleiro.')
                
            usuarioRetira = usuario_escolhe_jogada(n, m)
            n -= usuarioRetira
            if usuarioRetira == 1:
                print()
                print('Você tirou uma peça')
            elif usuarioRetira == 0:
                break
            else:
                print()
                print('Você tirou', usuarioRetira, 'peças')
            # mensagem de quantas peças sobraram
            if n == 1:
                print()
                print('Agora resta apenas uma peça no tabuleiro.')
            elif n == 0:
                break
            else:
                print()
                print('Agora restam', n, 'peças no tabuleiro.')
    print()
    print('Fim do jogo! O computador ganhou!')


def campeonato():
    """ função que executa 3 partidas. O computador ganha sempre """
    rodada = 1
    while rodada < 4:
        print()
        print('**** Rodada ', rodada, ' ****')
        partida()
        rodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')


# Inicialização do jogo
print('Bem-vindo ao jogo do NIM! Escolha:')
print()

escolhaPartida = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato '))

# executa uma partida isoladamente
if escolhaPartida == 1:
    partida()
# executa a função campeonato que por sua vez executa 3 partidas
else:
    print('Voce escolheu um campeonato!')
    print()
    campeonato()

