import logging

import numpy as np

from jass.base.const import *
from jass.base.player_round import PlayerRound
from jass.player.player import Player
from jass.base.rule_schieber import RuleSchieber

from parallel_universe import ParallelUniverse
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
        valid_cards = rnd.get_valid_cards()
        valid_card_indices = np.where(valid_cards == 1)[0]
        best_result = np.iinfo(np.int32).min
        best_card = -1
        for card_index in valid_card_indices:
            rnd_copy = ParallelUniverse.from_player_round(rnd)
            round_result = self.simulate_round(card_index, rnd_copy)
            if round_result > best_result:
                best_result = round_result
                best_card = card_index
        return best_card


    def simulate_round(self, our_card: int, rnd: ParallelUniverse) -> int:
        this_trick = self.simulate_trick(our_card, rnd)
        if rnd.nr_tricks <= 8: # TODO: adapt depth as needed
            return this_trick
        else:
            # TODO simulate for every valid card (loop)
            valid_cards = rnd.get_valid_cards()
            valid_card_indices = np.where(valid_cards == 1)[0]
            best_outcome = np.iinfo(np.int32).min
            best_card = -1
            for card_index in valid_card_indices:
                # TODO: manipulate rnd as needed, maybe create a copy
                outcome = this_trick + self.simulate_round(card_index, rnd)
                if outcome > best_outcome:
                    best_outcome = outcome
                    best_card = card_index
            return best_outcome


    def simulate_trick(self, our_card, rnd):
        # FIXME: dummy implementation
        # who won? this player begins the next round
        return 0

# others_indices = extract_others_card_indices(rnd)

# our_trick_index = np.where(rnd.current_trick == -1)[0][0]
# valid_cards = rnd.get_valid_cards()
# valid_card_indices = np.where(valid_cards == 1)[0]
# if valid_card_indices.size == 1:
    # return valid_card_indices[0]

# simulated_trick = rnd.current_trick

# put our card
# simulated_trick[our_trick_index] = card_index

# simulate others cards
# cards_missing = MAX_PLAYER - our_trick_index
# others_choices = np.random.choice(others_indices, cards_missing, replace=False)
# np.put(simulated_trick, range(our_trick_index+1, MAX_PLAYER+1), others_choices)
