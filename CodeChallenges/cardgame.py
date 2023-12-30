SUITES = "♠ ♡ ♢ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

import random
from typing import List, Tuple, Dict


Card = Tuple[str,str]
Deck = List[Card]

def create_card_deck(shuffle=False) -> Deck:
    '''Create adeck of card'''
    
    deck = [(s,c) for c in RANKS for s in SUITES]

    if shuffle:
        random.shuffle(deck)
    return deck


    

def deal_hands(deck)-> Tuple[Deck,Deck, Deck,Deck]:
    '''distribute the cards across 4 players'''
    return (deck[0::4],  deck[1::4], deck[2::4],  deck[3::4])



def play()->None:
    '''play with cards the play'''
    
    deck = create_card_deck(shuffle=True)

    names = 'P1 P2 P3 P4'.split()

    hands = { n:h for n,h in zip(names,deal_hands(deck))}

    #randomly play cards by each player until empty
    


 
    for name, cards in hands.items():
            card_str = ' '.join(f'{s}{r}' for s, r in cards)
            print(f'{name} {card_str}')

    throws = dict()


    # number of throws 
    # pick a random card from each of the four buckets and remove the card from the bucket
    #make a throw out of it
    
     
    throwcount = 0

    names = list(hands.keys())
    num_of_throws =4
 
    while throwcount < num_of_throws:
    
        throw = list()
        for name in names:
           
            throw.append(get_random_card_from_player(hands[name]))

        throws[throwcount] = throw
        del throw 


        for name, cards in hands.items():
            card_str = ' '.join(f'{s}{r}' for s, r in cards)
            print(f'{name} {card_str}')
        
        throwcount+=1
        
    
    print(throws) 



def get_random_card_from_player(deck:List)->Card:
    
    card = random.choice(deck)
    deck.remove(card)
    return card


     



    
    



if __name__ == '__main__':
     play()




 
