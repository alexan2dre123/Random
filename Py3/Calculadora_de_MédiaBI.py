# Calculador de média usando Função e Lista
import os

notas = [0, 0, 0, 0]
asking = True
medsc = float(input('Qual é a média de sua escola ? '))




def medcal(notas):
    med_f = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
    if med_f >= medsc:
        return (f'Parabéns, você foi aprovado com {med_f} pontos')
    else:
        return (f'Infelizmente você foi reprovado com {med_f} pontos')


while asking:
    try:
        notas[0] = float(input('Coloque sua primeira nota: '))
        notas[1] = float(input('Coloque sua segunda nota: '))
        notas[2] = float(input('Coloque sua terceira nota: '))
        notas[3] = float(input('Coloque sua quarta nota: '))

        if notas[0] < 0 or notas[0] > 10 or notas[1] < 0 or notas[1] > 10 or notas[2] < 0 or notas[2] > 10 or notas[
            3] < 0 or notas[3] > 10:
            print('Sua nota está errada, tente novamente!')
            continue
    except:
        print('Você não digitou um número!')
        continue
    else:
        break


print(medcal(notas))
print(f'Suas notas separadas foram: {notas}')

os.system("pause")
