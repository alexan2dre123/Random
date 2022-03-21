import keyboard
from time import sleep

TECLA_A = 'a'
TECLA_S = 's'
TECLA_D = 'd'
TECLA_W = 'w'

ALTURA = 30
LARGURA = 60

class obj(object):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
    def movePlayer(self, tecla):
        if (tecla==TECLA_A):
            self.x -= 1
        elif (tecla==TECLA_S):
            self.y += 1
        elif (tecla==TECLA_D):
            self.x += 1
        elif (tecla==TECLA_W):
            self.y -= 1

def mapa(jogador, fruta):
    print("-"*((ALTURA*4)+2))
    for i in range(0,ALTURA):
        for j in range(0,LARGURA):
            if (j == 0):
                print("|", end = "")
            if (jogador.x == j and jogador.y == i):
                print(jogador.value, end = "")
            elif (fruta.x == j and fruta.y == i):
                print(fruta.value, end = "")
            else:
                print ("  " , end = "")
            if (j == LARGURA-1):
                print("|")

    print("-"*((ALTURA*4)+2))

def keyboard_setup(jogador, _ultimo_movimento):
    if (keyboard.is_pressed("d")):
        jogador.movePlayer("d")
        _ultimo_movimento = "d"
    elif (keyboard.is_pressed("s")):
        jogador.movePlayer("s")
        _ultimo_movimento = "s"
    elif (keyboard.is_pressed("a")):
        jogador.movePlayer("a")
        _ultimo_movimento = "a"
    elif (keyboard.is_pressed("w")):
        jogador.movePlayer("w")
        _ultimo_movimento = "w"
    elif (_ultimo_movimento=="d"):
        jogador.movePlayer("d")
    elif (_ultimo_movimento=="s"):
        jogador.movePlayer("s")
    elif (_ultimo_movimento=="a"):
        jogador.movePlayer("a")
    elif (_ultimo_movimento=="w"):
        jogador.movePlayer("w")
    else:
        pass
    return _ultimo_movimento
