from Chips import Chips
from Hand import Hand
from Deck import Deck

class Player():

    def __init__(self):
        
        self.chips = Chips()
        self.hand = Hand()


    def place_bet(self):

        while True:

            try:

                self.chips.bet = int(input('Please place your bet: '))
                if self.chips.bet > self.chips.total:
                    print(f'Please choose a value not higher than: {self.chips.total}')
                    raise ZeroDivisionError

            except ValueError:

                print("Please provide an integer!")

            except ZeroDivisionError:

                print("Insuficient funds!")

            else:

                print('Bet placed!\n')

                break


    def hit(self, deck, hand):

        self.hand.add_card(deck.deal())

    def hit_or_stand(self, deck, hand):
        
        
        try:

            hit_stand = input("Hit or Stand ?: ").capitalize().strip()
            if hit_stand != 'Hit' and hit_stand != 'Stand':
            
                raise EnvironmentError

            elif hit_stand == 'Hit':

                self.hit(deck, hand)
                return True
            
            else:

                print('Player stands!')
            
                return False


        except ValueError:

            print('Please enter Hit or Stand!')
        
        except EnvironmentError:

            print("Please enter Hit or Stand")

        