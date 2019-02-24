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

class Bets():
    def __init__(self, total):
        self.total = total
    
    def set_bet(self):
        self.bet = input("What is your bet? ")
    
    def new_total(self):
        self.total -= self.bet


def find_sums(playerCards):
    cardSum = 0
    for card in playerCards:
        if not card.find("Jack") or not card.find("King") or not card.find("Queen") or not card.find("Ace"):
            if not card.find("Ace"):
                cardSum += 11
            else:
                cardSum += 10
        else:
            value = int(card[0])
            if value == 1:
                value = 10
            cardSum += value
    
    if cardSum > 21:
        cardSum - 10

    return cardSum

def dealerRevealCards():
    dealerSum = find_sums(dealerCards)
    print(f"The dealer has the {dealerCards[0]} and the {dealerCards[1]} for a total of {dealerSum}")
    if dealerSum <=21:
        if (21 - dealerSum) < (21-playerSum):
            print("The dealer wins!")
        else:
            print("You win!")
    else:
        print("You win!")


def check_sum(playerSum):
    if playerSum > 21:
        print("It's a bust!")
        return False
    elif playerSum < 21:
        flag = False
        while not flag:
            hit = input("Would you like to hit? (Type Y or N) ")
            if hit == "Y":
                flag = True
                playerCards.append(d1.pick_card())
                print(f"You got the {playerCards[-1]}")
                return True
            elif hit == "N":
                flag = True
                dealerRevealCards()
                return False
            else:
                print("Not valid response. Try again.")
    else:
        print("You got 21!")
        return False


totalChips = input("How many chips do you have? ")
betting = Bets(totalChips)
betting.set_bet()

while(betting.bet>totalChips):
    print("You can't bet more than you have. Try again.")
    bet = input("What is your bet? ")


d1 = Deck()
cardSum = 0

dealerCards = [d1.pick_card(), d1.pick_card()]
playerCards = [d1.pick_card(), d1.pick_card()]


print(f"The dealer has the {dealerCards[1]}")
print(f"Your hand is the {playerCards[0]} and the {playerCards[1]}")

game = True

while (game):
    playerSum = find_sums(playerCards)
    game = check_sum(playerSum)