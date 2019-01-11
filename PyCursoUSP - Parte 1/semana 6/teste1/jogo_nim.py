"""
Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente,
retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.
"""

def usuario_escolhe_jogada(n, m):
    """(int, int) -> (int)
    Escolha do usuário (com mensagem de erro para caso o valor escolhido seja inválido)
    """
    m_inicial = m
    m = int(input('Quantas peças você vai tirar? '))
    while m > m_inicial or m <= 0:
        print('Oops! Jogada inválida! Tente de novo.')
        m = int(input('Quantas peças você vai tirar? '))
    n -= m
    return n, m


def computador_escolhe_jogada(n, m):
    """(int, int) -> (int)
    Escolha do computador: aplicando a estratégia para vencer sempre
    """
    m_inicial = m
    m = 0
    while (n - m) % (m_inicial + 1) != 0:
        m += 1
    n -= m
    return n, m
