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
        others_indices = self.extract_others_card_indices(rnd)

        valid_cards = rnd.get_valid_cards()
        our_trick_index = np.where(rnd.current_trick == -1)[0][0]
        valid_card_indices = np.where(valid_cards == 1)[0]
        if valid_card_indices.size == 1:
            return valid_card_indices[0]

        best_result = np.iinfo(np.int32).min
        best_card = -1
        for card_index in valid_card_indices:
            current_trick = rnd.current_trick

            # put our card
            current_trick[our_trick_index] = card_index

            # simulate others cards
            cards_missing = MAX_PLAYER - our_trick_index
            others_choices = np.random.choice(others_indices, cards_missing, replace=False)
            np.put(current_trick, range(our_trick_index+1, MAX_PLAYER+1), others_choices)

            round_result = self.calculate_outcome(rnd, current_trick)
            if round_result > best_result:
                best_result = round_result
                best_card = card_index

        return best_card


    def extract_others_card_indices(self, rnd: PlayerRound):
        cards_played = rnd.tricks.flatten()
        cards_played = cards_played[cards_played != -1]

        cards_unplayed = np.ones(36, dtype=np.int32)
        cards_unplayed[cards_played] = 0

        others_cards = cards_unplayed - rnd.hand
        return np.where(others_cards == 1)[0]


    def calculate_outcome(self, rnd: PlayerRound, simulated_trick):
        round_result = rnd.rule.calc_points(simulated_trick, rnd.nr_tricks == 7, rnd.trump)
        round_winner = rnd.rule.calc_winner(simulated_trick, rnd.trick_first_player[rnd.nr_tricks], rnd.trump)

        if round_winner % 2 != rnd.player % 2:
            # invert score if other team made the trick
            round_result *= -1

        return round_result
