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
        rnd_copy = ParallelUniverse.from_player_round(rnd)
        our_trick_index = np.where(rnd.current_trick == -1)[0][0]

        depth = min(8 - rnd.nr_tricks, 3)
        best_card, _ = self.find_best_card(rnd_copy, our_trick_index, depth)
        return best_card


    def find_best_card(self, rnd: ParallelUniverse, our_trick_index: int, depth: int) -> int:
        valid_cards = rnd.get_valid_cards()
        valid_card_indices = np.where(valid_cards == 1)[0]

        unplayed_indices = np.where(rnd.trick == -1)[0]
        unplayed_indices = unplayed_indices[unplayed_indices != our_trick_index]

        best_result = np.iinfo(np.int32).min
        best_card = -1

        for card_index in valid_card_indices:
            # our move
            rnd.trick[our_trick_index] = card_index

            # remove our used card
            hand = np.copy(rnd.our_hand)
            hand[card_index] = 0

            # their moves
            others_card_indices = self.extract_others_card_indices(rnd.tricks, rnd.our_hand)
            others_choices = np.random.choice(others_card_indices, unplayed_indices.size, replace=False)
            rnd.trick[unplayed_indices] = others_choices

            # remove their used cards
            others_card_indices = np.setdiff1d(others_card_indices, others_choices)

            result, winner = self.simulate_trick(rnd, our_trick_index)
            our_next_trick_index = (4 - winner) % 4
            if depth > 0:
                trick = np.full(4, -1)
                player = rnd.player # TODO: seems to be constant over the entire round
                rnd_copy = ParallelUniverse(rnd.tricks, others_card_indices, hand, rnd.rule, rnd.trump, trick, player)
                _, game_result = self.find_best_card(rnd_copy, our_next_trick_index, depth-1)
                result += game_result
            if result > best_result:
                best_result = result
                best_card = card_index

        return (best_card, result)


    def simulate_trick(self, rnd, our_trick_index):
        round_result = rnd.rule.calc_points(rnd.trick, rnd.nr_tricks == 8, rnd.trump)
        first_player = (4 - our_trick_index) % 4
        round_winner = rnd.rule.calc_winner(rnd.trick, first_player, rnd.trump)

        if round_winner % 2 != rnd.player % 2:
            # invert score if other team made the trick
            round_result *= -1

        return (round_result, round_winner)


    def extract_others_card_indices(self, tricks, our_hand):
        cards_played = tricks.flatten()
        cards_played = cards_played[cards_played != -1]

        cards_unplayed = np.ones(36, dtype=np.int32)
        cards_unplayed[cards_played] = 0

        others_cards = cards_unplayed - our_hand
        return np.where(others_cards == 1)[0]
