#5 one's
#4 of every other card (2's, 3's, 4's, 5's, 7's, 8's, 10's, 11's, 12's,)
#4 Sorry cards

#DRAWING A 13 = SORRY CARD  
import random
class Deck:

    #List holding initial unshuffled deck
    cards = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 7, 7, 7, 7, 8, 8, 8, 8, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
    #emtpy list for shuffled cards
    shuffledDeck = []

    #pick random card in cards list and add it to the shuffledDeck list length of cards times
    #return: nothing
    def shuffleDeck(self):
        for i in range(0, len(Deck.cards)):
            randomIndex = random.randint(0, len(Deck.cards) - 1)
            shuffledCard = Deck.cards[randomIndex]
            self.shuffledDeck.insert(i, shuffledCard)

    #draw a card from the top of the shuffledDeck list
    #return: string representation of drawn card
    def drawCard(self):
        #check if all cards have been drawn
        if len(self.shuffledDeck) == 0:
            self.shuffleDeck()

        drawnCard = Deck.shuffledDeck[0]
        #delete drawn card from shuffledDeck list
        del Deck.shuffledDeck[0]

        return int(drawnCard)