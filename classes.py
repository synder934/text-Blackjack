
from random import choice
import msvcrt as m

class Card():
    def __init__(self, value, suit) -> None:
        self.value = value
        self.suit = suit
        self.hidden = False
        self.face = self.__face
        self.score = self.__score

    def __face(self):
        return ''.join([self.value, self.suit]) if not self.hidden else '##'

    def __score(self):
        try: return int(self.value)
        except:
            return 1 if self.value == 'A' else 10



class Player():
    def __init__(self) -> None:
        self.name = 'Player'
        self.hand = []
        self.active = False
        self.score = self.__score
    
    def __score(self, hidden = False):
        if hidden:
            val = sum([x.score() for x in self.hand if not x.hidden])
            if val <= 11 and len([x for x in self.hand if x.value == 'A' and not x.hidden]) > 0:
                val+=10
        
        else:
            val = sum([x.score() for x in self.hand])
            if val <= 11 and len([x for x in self.hand if x.value == 'A']) > 0:
                val+=10

        return val if val <= 21 else 'BUST'


    def hit(self, deck: list[Card], hidden = False):
        card = choice(deck)
        card.hidden = hidden
        deck.remove(card)
        self.hand.append(card)

    def stand(self):
        self.active = False

    def turn(self, deck):
        if self.score() == 'BUST' or self.score() == 21: self.stand(); return
        entry = chr(ord(m.getch()))
        print(entry)
        if entry == 'h':
            self.hit(deck)
        elif entry == 's':
            self.stand()

    def show(self):
        for x in self.hand:
            x.hidden = False

class Dealer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Dealer'

    def turn(self, deck):
        if self.score() == 'BUST': self.stand(); return
        if self.score() < 17:
            self.hit(deck)
        else:
            self.stand()


    