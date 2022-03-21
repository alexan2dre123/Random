import random

suits= ('Corações', 'Diamantes', 'Espadas', 'Trevos')
ranks= ('Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Coringa', 'Rainha', 'Rei', 'Ace')
values= {'Dois':2, 'Três':3, 'Quatro':4, 'Cinco':5, 'Seis':6, 'Sete':7, 'Oito':8, 'Nove':9, 'Dez':10, 'Coringa':10, 'Rainha':10, 'Rei':10, 'Ace':11}

playing = True

#Classes

class Card():
	def __init__(self, suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + ' de ' + self.suit

class Deck(object):
	def __init__(self):
		self.deck= [] #Começa como uma list vazia
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank)) #Construir cartas e adicionar a lista criada
	
	def __str__(self):
		deck_comp = '' #Começa como uma String Vazia
		for card in self.deck:
			deck_comp += '\n ' + card.__str__()
		return 'O baralho tem: ' + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1 
	
	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1
			
class Chips():
	def __init__(self):
		self.total = 100
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

# Functions

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input('Quantas fichas você quer apostar? '))
		except ValueError:
			print('Desculpe, mas o número deve ser um inteiro')
		else:
			if chips.bet > chips.total:
				print("Desculpe você não pode exceder ", chips.total)
			else:
				break

def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing

	while True:
		x = input("Você gostaria de adicionar mais uma carta ou esperar? Adicionar ou Esperar?  ")
		if x[0].lower() == 'a':
			hit(deck,hand)

		elif x[0].lower() == 'e':
			print('Jogador resolveu esperar, Oponente jogará agora!')
			playing = False
		else:
			print('Desculpe, tente novamente. ')
			continue
		break
def show_some(player,dealer):
	print("\nMão do Oponente: ")
	print(" <Carta Oculta>")
	print('', dealer.cards[1])
	print("\nMão do Jogador: ", *player.cards, sep= '\n ')

def show_all(player,dealer):
	print("\nMão do Oponente:", *dealer.cards, sep='\n ')
	print("Mão do Oponente: ",dealer.value)
	print("\nMão do Jogador:", *player.cards, sep='\n ')
	print("Mão do Jogador: ",player.value)
	
def player_busts(player,dealer,chips):
    print("Jogador Excedeu 21!!!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Jogador Ganhou a partida!!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Oponente Excedeu 21!!!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Oponente Ganhou!!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Jogador e Oponente impataram!!!")

 #Game

while True:
    print('Bem vindo ao 21, tente chegar a 21 ou proximo sem exceder\nOponente aposta até chegar a 17. Aces conta como 1 ou 11')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
    	hit_or_stand(deck,player_hand)
    	show_some(player_hand, dealer_hand)

    	if player_hand.value > 21:
    		player_busts(player_hand,dealer_hand,player_chips)
    		break
    if player_hand.value <= 21:
    	while dealer_hand.value<17:
    		hit(deck, dealer_hand)
    		show_all(player_hand,dealer_hand)

    	if dealer_hand.value > 21:
    		dealer_busts(player_hand,dealer_hand,player_chips)
    	elif dealer_hand.value > player_hand.value:
    		dealer_wins(player_hand, dealer_hand, player_chips)
    	elif dealer_hand.value < player_hand.value:
    		player_wins(player_hand,dealer_hand,player_chips)
    	else:
    		push(player_hand, dealer_hand)

    print("\nFichas do Jogador: ", player_chips.total)

    new_game = input('Gostaria de jogar novamente? responda sim ou não')

    if new_game[0].lower() == 's':
    	playing = True
    	continue
    else:
    	print("Obrigado por jogar!!")
    	break

