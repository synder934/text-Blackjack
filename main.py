import os
from time import sleep
from classes import *

def makeDeck(): return [Card(v, s) for v in 'A23456789XJQK' for s in 'CDHS']


def findWinner(dealer: Dealer, player: Player):
    # BLACKJACK CASES
    if player.score() == 21 and len(player.hand) == 2:
        winner = player.name
        reason = 'BLACKJACK'
    elif player.score() == dealer.score():
        winner = 'no one wins :('
        reason = 'push!'
    elif dealer.score() == 21 and len(dealer.hand) == 2:
        winner = dealer.name
        reason = 'BLACKJACK'

    # BUST CASES
    elif player.score() == 'BUST':
        winner = dealer.name
        reason = f'{player.name} went Bust'
    elif dealer.score() == 'BUST':
        winner = player.name
        reason = f'{dealer.name} went Bust'

    # COMPARE CASES
    elif player.score() > dealer.score():
        winner = player.name
        reason = f'with {player.score()}'
    else:
        winner = dealer.name
        reason = f'with {dealer.score()}'
    return (winner, reason)


def gameLoop():
    while True:
        player = Player()
        dealer = Dealer()
        info = 'dealing!'
        def output(): os.system('CLS'); return f'''
        ------------------------------
        {info}
        ------------------------------
            dealer: {' '.join([x.face() for x in dealer.hand])}
                    {dealer.score(True)}

            you:    {' '.join([x.face() for x in player.hand])}
                    {player.score()}
        ------------------------------
           {'| h = hit || s = stand |' if player.active else ''}
        ------------------------------
        '''

        deck = makeDeck()
        
        for p, h in [(player, False), (dealer, True), (player, False), (dealer, False)]:
            p.hit(deck, h)
            print(output())
            sleep(0.5)

        for p in [player, dealer]:
            info = f"{p.name}'s turn!"
            p.active = True
            p.show()
            print(output())
            sleep(0.5)
            while p.active: p.turn(deck); print(output()); sleep(1.5)

        winner, reason = findWinner(dealer, player)

        info = f"{winner} wins!, {reason}"
        print(output())
        print('replay? <y>', end='')
        if chr(ord(m.getch())) != 'y':
            break




if __name__ == '__main__':
    gameLoop()



