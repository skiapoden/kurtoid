#!/usr/bin/env python3

import unittest

import numpy as np

from jass.base.rule_schieber import RuleSchieber

from parallel_universe import ParallelUniverse

class ParallelUniverseTest(unittest.TestCase):

    def test_calculate_nr_tricks(self):
        tricks = np.full([9, 4], -1, dtype=np.int32)
        others_cards = np.full(36, 0, dtype=np.int32)
        our_hand = np.full(36, 0, dtype=np.int32)
        rule = RuleSchieber()
        trump = 0
        trick = np.full(4, -1, dtype=np.int32)

        universe = ParallelUniverse(tricks, others_cards, our_hand, rule, trump, trick)
        print(tricks, others_cards, our_hand, rule, trump, trick)

if __name__ == '__main__':
    unittest.main()
