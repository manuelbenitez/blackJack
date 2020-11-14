import random
from Deck import Deck
from Card import Card
from Hand import Hand
from Chips import Chips
from Player import Player
from Dealer import Dealer



def show_some(dealer):
    '''SHOWS ALL THE CARDS OF THE DEALER EXCEPT THE FIRST ONE'''
   
    print('Dealers cards!')
    print('[***]')

    dealers_hand_value = 0
    for i in range(1, len(dealer.hand.cards)):
        print(f"[{dealer.hand.cards[i]}]")
        dealers_hand_value = dealer.hand.gameon_dealers_hand_value(dealer.hand.cards[i])
        
    
    print(f'Dealers Hand Value: {dealers_hand_value}\n')


    
def show_all(player):
    ''' SHOWS ALL THE CARDS OF THE DEALER AND THE PLAYER'''
    if isinstance(player, Player):

        print('Players cards!')
        for card in player.hand.cards:
            print(f'[{card}]')
        while player.hand.aces > 0:
            player.hand.adjust_for_ace()
        print('\n')
        print(f"Players Hand Value: {player.hand.value}\n")

    else:

        print('Dealers cards!')
        for card in dealer.hand.cards:
            print(f'[{card}]')

        print('\n')
        print(f'Dealers Hand Value: {dealer.hand.value}')

    
def player_busts(player, dealer):
    
        print('PLAYER BUSTS!\n')
        show_all(player)
        player.chips.lose_bet()
        return False

def player_wins(player, dealer):
    
        print('PLAYER WINS!!!\n')
        show_all(player)
        show_all(dealer)
        player.chips.win_bet()
        return False


def dealer_busts(player, dealer):
        
        print('DEALER BUSTS!\n')
        show_all(dealer)
        show_all(player)
        player.chips.win_bet()
        return False
    
def dealer_wins(player, dealer):
    
        print('DEALER WINS!!!\n')
        show_all(dealer)
        show_all(player)
        player.chips.lose_bet()
        return False
    
def push(player, dealer):
    
    print('TIE\n')
    show_all(player)
    show_all(dealer)
    return False

# 
# 
# 
#                   START OF THE GAME
# 
# 
# 
# 

# CREATES PLAYER AND DEALER
player = Player()
dealer = Dealer()
playing = True

print("WELCOME TO BLACK JACK 21")
print(f'The inicial amount of chips is: {player.chips.total}')

while True:

    
    # Print an opening statement
    print("NEW MATCH!\n\n")
    
    # Create & shuffle the deck, deal two cards to each player

    deck = Deck()
    deck.shuffle()


    # Prompt the Player for their bet


    for i in range(2):
        player.hand.add_card(deck.deal())
        dealer.hand.add_card(deck.deal())

    # Prompt the Player for their bet

    player.place_bet()

    # Show cards (but keep one dealer card hidden)


    
    show_all(player)
    
    show_some(dealer)

    while True:
        # WHILE PLAYER KEEPS HITING
        while playing:  # recall this variable from our hit_or_stand function
            
            # Prompt for Player to Hit or Stand
            playing = player.hit_or_stand(deck, player.hand)
            
            # Show cards (but keep one dealer card hidden)
            
            show_all(player)
            
            show_some(dealer)
            
            
            # If player's hand exceeds 21, run player_busts() and break out of loop

            if player.hand.value >21:
                
                player_busts(player, dealer)
                playing = False
            
            

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        show_all(dealer)
        if player.hand.value > 21:
            break

            # HIT THE DEALER UNTIL IR REACHES 17
        while dealer.hand.value <17:
            dealer.hand.add_card(deck.deal())


        # DIFFERENT WINNING SCENARIOS
        if dealer.hand.value >21:

            dealer_busts(player, dealer)
            break

        elif dealer.hand.value == player.hand.value:

            push(player, dealer)
            break

        elif player.hand.value == 21:

            player_wins(player,dealer)
            break

        elif dealer.hand.value > player.hand.value:

            dealer_wins(player, dealer)
            break
    
        elif dealer.hand.value < player.hand.value:

            player_wins(player, dealer)
            break

            
        
    
    # Inform Player of their chips total 
    print(f"Player's total chips : {player.chips.total}")
    
    
    if player.chips.total == 0:
        print('You run out of chips')
        break
    
    else:
        # Ask to play again
        playagain = input("Want to play again? [Y/N]").upper()

        if playagain == 'N':
            break
        else:
            player.hand = Hand()
            dealer.hand = Hand()
            player.hand.value=0
            dealer.hand.value=0
            playing = True

    
