import logging

import numpy as np

from jass.base.const import *
from jass.base.player_round import PlayerRound
from jass.player.player import Player
from jass.base.rule_schieber import RuleSchieber

from kurtutils import extract_others_card_indices, calculate_round_outcome
from rule_based_trump import get_trumps, get_boeck

class Trumpruloid(Player):

    PUSH_THRESHOLD = 5 # average calculated strength

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._rule = RuleSchieber()

    def select_trump(self, rnd: PlayerRound) -> int:
        trumps = get_trumps(rnd.hand)
        boeck = get_boeck(rnd.hand)

        score = {}
        for option in trumps.keys():
            score[option] = trumps[option] + boeck[option]
        sorted_score = sorted(score.items(), key=lambda kv: kv[1])
        sorted_score.reverse()

        if rnd.forehand is None and sorted_score[0][1] < self.PUSH_THRESHOLD:
            return PUSH # gschobe (if forehand and bad score)

        trump = sorted_score[0][0]
        return trump

    def play_card(self, rnd: PlayerRound) -> int:
        others_indices = extract_others_card_indices(rnd)

        valid_cards = rnd.get_valid_cards()
        our_trick_index = np.where(rnd.current_trick == -1)[0][0]
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

            round_result = calculate_round_outcome(rnd, simulated_trick)
            if round_result > best_result:
                best_result = round_result
                best_card = card_index

        return best_card
