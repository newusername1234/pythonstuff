import random

ranks = {
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
    'ace': 11
}

suits = ('hearts', 'diamonds', 'spades', 'clubs')

class Deck:

    def __init__(self):
        self.all_cards = []        
        for suit in suits:
            for key, value in ranks.items():
                card_to_append = Card(key, suit, value)
                self.all_cards.append(card_to_append)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f"Deck has {len(self.all_cards)} cards"


class Card:

    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Player:

    def __init__(self, name='Dealer'):
        self.name = name
        self.chips = 100
        self.hand = []
        self.total = 0
        self.bet = 0

    def bet(self,amount):
        self.bet = amount

    def add_chips(self,winnings):
        self.chips += winnings

    def lose_chips(self,loss):
        self.chips -= loss

    def get_card(self, card):
        self.hand.append(card)
        if card.rank == 'ace' and self.total + 11 > 21:
            self.total += 1
        else:
            self.total += card.value

new_deck = Deck()
new_deck.shuffle()

name = input("Please enter your name\n")
print('\n'*100)

player = Player(name)
dealer = Player()

while True:
    dealer_stands = False
    player_stands = False
    game_over = False

    bet = int(input(f'{player.name} has {player.chips} chips.\nHow many to bet?\n'))
    print('\n'*100)

    player.get_card(new_deck.deal())
    player.get_card(new_deck.deal())
    dealer.get_card(new_deck.deal())
    dealer.get_card(new_deck.deal())

    print(f"{player.name} has:\n")
    for card in player.hand:
        print(card)
    print(f'Total: {player.total}\n')

    print(f"Dealer has:\n")
    for card in dealer.hand:
        print(card)
    print(f'Total: {dealer.total}\n')

    while not dealer_stands:
        if dealer.total < 17:
            dealer.get_card(new_deck.deal())
            print(f'Dealer drew {dealer.hand[-1]}\n')
            print(f'Dealer total: {dealer.total}\n')
        if dealer.total > 21:
            print("Dealer bust!")
            print(f"{player.name} won {bet} chips")
            player.add_chips(bet)
            game_over = True
            break
        if dealer.total == 21:
            print("Dealer wins with 21")
            player.lose_chips(bet)
            game_over = True
            break
        if dealer.total >= 17:
            print(f"Dealer stands on {dealer.total}")
            dealer_stands = True

    while player.total < 21 and not player_stands and not game_over:
        print(f"Total: {player.total}")
        choice = input(f"{player.name} has {player.total}. Hit or stand? ").lower()

        if choice == 'hit':
            player.get_card(new_deck.deal())
            print(player.hand[-1])
        elif choice == 'stand':
            break
        else:
            print("invalid choice")


    if player.total > 21:
        print('You bust!')
        player.lose_chips(bet)
    elif player.total > dealer.total:
        print(f'{player.name} wins with {player.total} over {dealer.total}')
        player.add_chips(bet)
    elif player.total == dealer.total:
        print('Dealer wins the tie')    
        player.lose_chips(bet)
    else:
        print(f'Dealer wins with {dealer.total} over {player.total}')
        player.lose_chips(bet)

    player.hand, player.total = [], 0
    dealer.hand, dealer.total = [], 0
    


