import logging
import random

import numpy as np

from jass.base.const import *
from jass.base.player_round import PlayerRound
from jass.player.player import Player
from jass.base.rule_schieber import RuleSchieber

class Kurtoid(Player):

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._rule = RuleSchieber()

    def select_trump(self, rnd: PlayerRound) -> int:
        trump = 0
        max_number_in_color = 0
        for c in range(4):
            number_in_color = (rnd.hand * color_masks[c]).sum()
            if number_in_color > max_number_in_color:
                max_number_in_color = number_in_color
                trump = c
        return trump

    def play_card(self, rnd: PlayerRound) -> int:
        cards_played = rnd.tricks.flatten()
        cards_played = cards_played[cards_played != -1]
        cards_unplayed = np.ones(36, dtype=np.int32)
        cards_unplayed[cards_played] = 0
        others_cards = cards_unplayed - rnd.hand
        others_indices = np.where(others_cards == 1)[0]

        valid_cards = rnd.get_valid_cards()
        our_trick_index = np.where(rnd.current_trick == -1)[0][0]
        valid_card_indices = np.where(valid_cards == 1)[0]
        if valid_card_indices.size == 1:
            return valid_card_indices[0]
        best_result = -9999 # TODO: use some constant
        best_card = -1
        for card_index in valid_card_indices:
            current_trick = rnd.current_trick
            current_trick[our_trick_index] = card_index
            cards_missing = 3 - our_trick_index
            # TODO: do this for different permutations
            others_choices = np.random.choice(others_indices, cards_missing, replace=False)
            np.put(current_trick, range(our_trick_index+1,4), others_choices)
            round_result = rnd.rule.calc_points(current_trick, rnd.nr_tricks == 7, rnd.trump)
            round_winner = rnd.rule.calc_winner(current_trick, rnd.trick_first_player[rnd.nr_tricks], rnd.trump)
            if round_winner % 2 == rnd.player % 2:
                # we win, nothing to do
                pass
            else:
                # they win, count result as a negative
                round_result = -round_result
            if round_result > best_result:
                best_result = round_result
                best_card = card_index
        return best_card

        #card = np.random.choice(np.flatnonzero(valid_cards))
        #self._logger.debug('Played card: {}'.format(card_strings[card]))
        #return card
