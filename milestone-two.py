import random

class Deck():
    def __init__(self):
        suites = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King", "Ace")
        self.fullDeck = []
        for suite in suites:
            for rank in ranks:
                self.fullDeck.append("%s of %s" % (rank, suite))

    def pick_card(self):
        card_index = random.randint(0, len(self.fullDeck)-1)  
        new_card = self.fullDeck[card_index] 
        del self.fullDeck[card_index]  
        return new_card

    def check_deck(self):
        print (len(self.fullDeck))



totalChips = input("How many chips do you have? ")
bet = input("What is your bet? ")

while(bet>totalChips):
    print("You can't bet more than you have. Try again.")
    bet = input("What is your bet? ")


d1 = Deck()
dealerCards = [d1.pick_card(), d1.pick_card()]
playerCards = [d1.pick_card(), d1.pick_card()]

print(f"Your hand is the {playerCards[0]} and the {playerCards[1]}")
print(f"The dealer has the {dealerCards[1]}")

d1.check_deck()
