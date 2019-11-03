#!/usr/bin/env python3

import unittest

import numpy as np

from jass.base.const import *

from rule_based_trump import get_trumps, get_boeck

class RuleBasedTrumpTest(unittest.TestCase):

    def test_trumps(self):
        hand = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],  # Diamonds/Schellen (Ass)
                         [1, 1, 0, 0, 0, 0, 0, 0, 0],  # Hearts/Rosen (Ass, König)
                         [1, 0, 1, 1, 0, 0, 0, 0, 0],  # Spades/Schilten (Ass, Ober, Puur)
                         [1, 0, 0, 1, 0, 1, 0, 0, 0]]) # Clubs/Eicheln (Ass, Puur, Näll)
        flat_hand = hand.flatten()

        trumps = get_trumps(flat_hand)
        self.assertEqual(trumps[DIAMONDS], 1)
        self.assertEqual(trumps[HEARTS], 2)
        self.assertEqual(trumps[SPADES], 3)
        self.assertEqual(trumps[CLUBS], 3)


    def test_boeck_high(self):
        hand = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],  # Diamonds/Schellen (Ass)
                         [1, 1, 0, 0, 0, 0, 0, 0, 0],  # Hearts/Rosen (Ass, König)
                         [1, 0, 1, 1, 0, 0, 0, 0, 0],  # Spades/Schilten (Ass, Ober, Puur)
                         [1, 0, 0, 1, 0, 1, 0, 0, 0]]) # Clubs/Eicheln (Ass, Puur, Näll)
        flat_hand = hand.flatten()

        boeck = get_boeck(flat_hand)
        self.assertEqual(boeck[DIAMONDS], 0)
        self.assertEqual(boeck[HEARTS], 0)
        self.assertEqual(boeck[SPADES], 1) # Puur
        self.assertEqual(boeck[CLUBS], 3) # Puur, Näll, Ass
        self.assertEqual(boeck[OBE_ABE], 5) # 4*Ass + König
        self.assertEqual(boeck[UNE_UFE], 0)


    def test_boeck_low(self):
        hand = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 1],  # Diamonds/Schellen (Ass)
                         [0, 0, 0, 0, 0, 0, 0, 1, 1],  # Hearts/Rosen (Ass, König)
                         [0, 0, 0, 0, 0, 0, 1, 1, 1],  # Spades/Schilten (Ass, Ober, Puur)
                         [0, 0, 0, 0, 0, 1, 0, 1, 1]]) # Clubs/Eicheln (Ass, Puur, Näll)
        flat_hand = hand.flatten()

        boeck = get_boeck(flat_hand)
        self.assertEqual(boeck[DIAMONDS], 0)
        self.assertEqual(boeck[HEARTS], 0)
        self.assertEqual(boeck[SPADES], 0)
        self.assertEqual(boeck[CLUBS], 0)
        self.assertEqual(boeck[OBE_ABE], 0)
        self.assertEqual(boeck[UNE_UFE], 8)


if __name__ == '__main__':
    unittest.main()
