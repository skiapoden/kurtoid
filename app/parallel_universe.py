from math import ceil

import numpy as np

from jass.base.player_round import PlayerRound

from kurtutils import extract_others_card_indices

class ParallelUniverse:

    def from_player_round(rnd: PlayerRound):
        others_cards = extract_others_card_indices(rnd)
        tricks = np.copy(rnd.tricks)
        our_hand = np.copy(rnd.hand)
        rule = rnd.rule
        trick = np.copy(rnd.current_trick)
        player = rnd.player

        instance = ParallelUniverse(tricks, others_cards, our_hand, rule, rnd.trump, trick, player)
        return instance


    def __init__(self, tricks, others_cards, our_hand, rule, trump, trick, player):
        self.tricks = tricks
        self.others_cards = others_cards
        self.our_hand = our_hand
        self.rule = rule
        self.trump = trump
        self.trick = trick
        self.player = player


    @property
    def nr_tricks(self):
        # first unplayed card index is number of played cards
        cards_played = np.where(self.tricks == -1)[0][0]
        return ceil(cards_played / 4)


    def get_valid_cards(self):
        cards_in_trick = np.where(self.tricks == -1)[0][0]
        return self.rule.get_valid_cards(self.our_hand, self.trick, cards_in_trick, self.trump)
