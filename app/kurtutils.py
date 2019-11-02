import numpy as np

from jass.base.player_round import PlayerRound

def extract_others_card_indices(rnd: PlayerRound):
    cards_played = rnd.tricks.flatten()
    cards_played = cards_played[cards_played != -1]

    cards_unplayed = np.ones(36, dtype=np.int32)
    cards_unplayed[cards_played] = 0

    others_cards = cards_unplayed - rnd.hand
    return np.where(others_cards == 1)[0]


def calculate_round_outcome(rnd: PlayerRound, simulated_trick):
    return calculate_round_outcome_winner(rnd, simulated_trick)[0]

def calculate_round_outcome_winner(rnd: PlayerRound, simulated_trick):
    round_result = rnd.rule.calc_points(simulated_trick, rnd.nr_tricks == 8, rnd.trump)
    round_winner = rnd.rule.calc_winner(simulated_trick, rnd.trick_first_player[rnd.nr_tricks], rnd.trump)

    if round_winner % 2 != rnd.player % 2:
        # invert score if other team made the trick
        round_result *= -1

    return (round_result, round_winner)
