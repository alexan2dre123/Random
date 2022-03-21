import random

#Função para mostrar a "Interface"
def display_board(board):
    print('\n' * 100)
    print(board[7]+' |',board[8]+' |',board[9])
    print('---------')
    print(board[4]+' |',board[5]+' |',board[6])
    print('---------')
    print(board[1]+' |',board[2]+' |',board[3])



# Função para escolha entre X ou O do primeiro jogador
def player_input1():
    marker = ''
    # Favor Escolher um tipo de marcador
    while marker != 'X' and marker != 'O': # Loop While: Faz o jogador escolhe entre X ou O, enquanto não escolher corretamente o loop continua
        marker = input('Queridissimo Deputado, Escolha X ou O: ').upper() # Vai ser armazenado na variavel marker a escolha do jogador, o método upper é para caso o jogador coloca letra minúscula.
    player1 = marker

    if player1 == 'X': # If statement: Aqui caso o Player 1 escolher X o jogador automaticamente vai ser O.
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2) # Retorna as escolhas de ambos os jogadores!



#Função para colocar o marcador
def place_marker(board,marker,position): # Pega o tabuleiro, o marcador e a posição
    board[position] = marker # Aqui simplismente ta dizendo q a posição escolhida no tabuleiro(board[position]) é igual ao marcador



#Função pra checar se um jogador ganhou
def win_check(board,mark): #Simplismente vai retornar se é True ou False as posiçòes diagonal e horizontais de acordo com as regras do jogo
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark))

# Escolhe randomicamente quem jogará primeiro
def choose_first():
    if random.randint(0,1) == 0: # Pega 0 ou 1 randomicamente.
        return 'DEPUTADO 2'      # Caso for 0 o número o jogador 2 jogará primeiro.
    else:
        return 'DEPUTADO 1'      # Se não o jogador 1 é que joga'ra primeiro.

def space_check(board, position):# Checar se o espaço no tabuleiro ja não está marcado.
    return board[position] == ' '

def full_board_check(board):     # Checar se o tabuleiro está completamente marcado.
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):        # Escolha da posição do jogador.
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position= int(input(f'Escolha uma posição {turn}: '))
    return position


def replay():                    # Replay da partida, pergunta se o jogador continuar a jogar ou não.
    return input('Você quer jogar de novo ? Sim ou Não ? ').lower().startswith('s')

#Mensagens de apresentação
print('Jogo da Velha')
print('Os espaços do jogo estão enumerados de 1-9 da esquerda pra direita, de baixo para cima.')
print('DICA: USE O TECLADO NUMÉRICO COMO TABULEIRO(NUMERAÇÃO DA DIREITA)')
print('HAVE FUN!!!!!!! ')

# Algoritmo Principal
while True:
    theboard = [' '] * 10
    player1_marker, player2_marker = player_input1()
    turn = choose_first()
    print(turn + ' vai primeiro!')

    play_game = input('Você está preparado para jogar? Sim ou Não')
    if play_game.lower()[0] == 's':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'DEPUTADO 1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)

            if win_check(theboard, player1_marker):
                display_board(theboard)
                print('Parabéns deputado 1, você ganhou a partida')
                game_on = False

            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('O jogo empatou')
                    break
                else:
                    turn = 'DEPUTADO 2'

        else:
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print('Parabéns deputado 2, você ganhou a partida')
                game_on = False

            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('O jogo empatou')
                    break
                else:
                    turn = 'DEPUTADO 1'

    if not replay():
        break