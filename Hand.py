from Card import Card

class Hand():

    values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, Card):
        
        self.cards.append(Card)
        if Card.rank == 'Ace':
            self.aces = self.aces + 1      
        else: 
            self.value = self.value + Hand.values[Card.rank]
                
        

    def adjust_for_ace(self):
        
        for card in self.cards:

            if card.rank == 'Ace':
            
                while True:

                    try:

                        ace_value = int(input('Choose a value for the ace (1 or 11): \n'))

                        if ace_value != 11 and ace_value != 1:
                            raise EnvironmentError


                    except ValueError:

                        print('Please enter an integer!\n')
                    
                    except EnvironmentError:

                        print ("Please enter 1 or 11!\n")

                    else:

                        print(f'Value of the Ace : {ace_value}\n')
                        self.value =self.value + ace_value
                        self.aces = self.aces - 1
                        return True


    def gameon_dealers_hand_value(self, Card):
        # RETURNS CARD VALUE
        # FUNCTION USED TO CALCULATE DEALERS HAND VALUE WHILE GAME IS STILL ON
        # DEALERS IS GOING TO BE WITH ONE HIDDEN CARD
        
        return  Hand.values[Card.rank]
                