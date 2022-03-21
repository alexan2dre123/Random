from Lib.functions import *
import random
import os

jogador = obj(1, 1, 'o ')
fruta = obj(random.randint(0,LARGURA-1),random.randint(0,ALTURA-1), '* ')
_ultimo_movimento = 'd'

os.system("mode con:cols=125 lines=35")

while (True):
    if jogador.x == fruta.x and jogador.y == fruta.y:
        fruta.x = random.randint(0,LARGURA-1)
        fruta.y = random.randint(0,ALTURA-1)
    mapa(jogador, fruta)
    _ultimo_movimento = keyboard_setup(jogador, _ultimo_movimento)
    sleep(0.2)
    os.system('cls')
