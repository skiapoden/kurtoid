import logging

import numpy as np

from jass.base.const import *
from jass.base.player_round import PlayerRound
from jass.player.player import Player
from jass.base.rule_schieber import RuleSchieber

from kurtutils import extract_others_card_indices, calculate_round_outcome_winner

class Carloid(Player):

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
        others_indices = extract_others_card_indices(rnd)

        our_trick_index = np.where(rnd.current_trick == -1)[0][0]
        valid_cards = rnd.get_valid_cards()
        valid_card_indices = np.where(valid_cards == 1)[0]
        if valid_card_indices.size == 1:
            return valid_card_indices[0]

        best_result = np.iinfo(np.int32).min
        best_card = -1
        for card_index in valid_card_indices:
            simulated_trick = rnd.current_trick

            # put our card
            simulated_trick[our_trick_index] = card_index

            # simulate others cards
            cards_missing = MAX_PLAYER - our_trick_index
            others_choices = np.random.choice(others_indices, cards_missing, replace=False)
            np.put(simulated_trick, range(our_trick_index+1, MAX_PLAYER+1), others_choices)

            (round_result, _) = calculate_round_outcome_winner(rnd, simulated_trick)
            if round_result > best_result:
                best_result = round_result
                best_card = card_index

        return best_card
