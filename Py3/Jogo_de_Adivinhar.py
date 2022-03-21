import random
import os

num = random.randint(1,100)

print('Seja bem vindo ao jogo de adivinhação \nEstou pensando em um número de 1 a 100 \nse seu palpite estiver mais de 10 números distantes você receberá a mensagem "GELADO!"')
print('agora, se seu número estiver até 10 ou menos, você rebeceberá a mensagem QUENTE! \ne se estiver mais longe que antes, receberá a mensagem GELANDO!')
print('se estiver mais perto receberá a mensagem ESQUENTANDO! \nVAMOS JOGAR!! SE DIVIRTA :)')
print('\n')

guesses = [0]

while True:
    guess = int(input('Estou pensando em um número de 1 a 100. Em qual número estou pensando ?'))
    if guess < 1 or guess > 100:
        print('Atenção, você deve escolher um número entre 1 e 100: ')
        continue


    if guess == num:
        print(f'\nParabéns você acertou o número em {len(guesses)} tentativas!')
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('ESQUENTANDO!')
        else:
            print('GELANDO!')

    else:
        if abs(num-guess) <= 10:
            print('QUENTE!')

        else:
            print('GELADO!')


os.system("pause")