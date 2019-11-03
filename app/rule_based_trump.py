import numpy as np

from jass.base.const import *

def get_trumps(hand: np.array):
    trumps = {
            DIAMONDS: 0,
            HEARTS: 0,
            SPADES: 0,
            CLUBS: 0,
            OBE_ABE: 0,
            UNE_UFE: 0,
        }

    offsets = {DIAMONDS: 0, HEARTS: 9, SPADES: 18, CLUBS: 27}
    for color, offset in offsets.items():
        color_cards = hand[offset:offset+9]
        trumps[color] = np.where(color_cards == 1)[0].size

    return trumps 

def get_boeck(hand: np.array):
    boeck = {
            DIAMONDS: 0,
            HEARTS: 0,
            SPADES: 0,
            CLUBS: 0,
            OBE_ABE: 0,
            UNE_UFE: 0,
        }

    color_bock_seq = [3, 5, 0, 1, 2, 4, 6, 7, 8] # Puur, Näll, Ass, König, Ober, Banner, 9, 8, 7, 6
    obe_abe_bock_seq = [i for i in range(9)]
    une_ufe_bock_seq = [i for i in range(9)]
    une_ufe_bock_seq.reverse()

    offsets = {DIAMONDS: 0, HEARTS: 9, SPADES: 18, CLUBS: 27}
    for color, offset in offsets.items():
        color_cards = hand[offset:offset+9]
        n_boeck = 0
        for i in color_bock_seq:
            if color_cards[i] == 1:
                n_boeck += 1
            else:
                boeck[color] = n_boeck
                break

        for i in obe_abe_bock_seq:
            if color_cards[i] == 1:
                boeck[OBE_ABE] += 1
            else:
                break

        for i in une_ufe_bock_seq:
            if color_cards[i] == 1:
                boeck[UNE_UFE] += 1
            else:
                break
        
    return boeck
