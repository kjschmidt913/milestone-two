import random

class Deck():
    def __init__(self):
        suites = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King", "Ace")
        self.fullDeck = []
        for suite in suites:
            for rank in ranks:
                self.fullDeck.append("%s of %s" % (rank, suite))

    def pick_item(self):
        card_key = random.randint(0, len(self.fullDeck)-1)  
        new_card = self.fullDeck[card_key] 
        del self.fullDeck[card_key]  
        return new_card

    def missing_card(self):
        print (self.fullDeck)

d1 = Deck()
card1 = d1.pick_item()

print(d1.fullDeck)

