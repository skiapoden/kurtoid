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
        possible_trump = trump_ints.copy()
        if rnd.forehand is None:
            possible_trump.append(PUSH)
        self._logger.debug('Selected trump: {}'.format(possible_trump))
        return random.choice(possible_trump)

    def play_card(self, rnd: PlayerRound) -> int:
        valid_cards = rnd.get_valid_cards()
        card = np.random.choice(np.flatnonzero(valid_cards))
        self._logger.debug('Played card: {}'.format(card_strings[card]))
        return card
