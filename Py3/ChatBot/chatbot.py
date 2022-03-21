from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

kronus = ChatBot('Kronus')
playing = True


conversa = ['Oi', 'Olá', 'Tudo bem ?', 'Tudo ótimo', 'Quem ganhou as eleições ? ', 'UH É BOLSONARO, UH É BOLSONARO', 'Posso come sua esposa ?', 'Claro meu consagrado',
            'Você gosta de programar?', 'Sim, eu programo em Python', 'Qual é o seu nome ?', 'Meu nome é Kronus', 'Quem é você ?',
            'Sou uma IA criado pelo grande sábio Alexandre Beck', 'Vou muito bem e você ?', 'Estou ótimo']

kronus.set_trainer(ListTrainer)
kronus.train(conversa)

user1 = input('Coloque um nome: ')
while playing:
    pergunta = input(user1 + ': ')
    resposta = kronus.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Kronus: ', resposta)
    else:
        print('Kronus: Não sei do que você esta falando, meu consagrado!, continue conversando comigo para eu aprender')

    if pergunta == 'sair'.startswith('s'):
        break
