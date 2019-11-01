#!/usr/bin/env python3

import sys

from jass.base.const import JASS_SCHIEBER_2500
from jass.arena.arena import Arena
from jass.arena.trump_selection_players_strategy import TrumpPlayerStrategy
from jass.arena.play_game_nr_rounds_strategy import PlayNrRoundsStrategy
from jass.player.random_player_schieber import RandomPlayerSchieber

from kurtoid import Kurtoid
from donat_trump import DonatTrump

def main(n_games):
    arena = Arena(jass_type=JASS_SCHIEBER_2500,
                  trump_strategy=TrumpPlayerStrategy(),
                  play_game_strategy=PlayNrRoundsStrategy(4))

    randy = RandomPlayerSchieber()
    donat = DonatTrump()
    kurtoid = Kurtoid()
    arena.set_players(kurtoid, randy, donat, randy)

    arena.nr_games_to_play = n_games
    arena.play_all_games()

    kurtoid_wins = arena.nr_wins_team_0 
    opponent_wins = arena.nr_wins_team_1
    draws = arena.nr_draws
    total = kurtoid_wins + opponent_wins + draws

    print('Our Team  {:4d} {:5.1f}%'.format(kurtoid_wins, kurtoid_wins / total * 100))
    print('Opponents {:4d} {:5.1f}%'.format(opponent_wins, opponent_wins / total * 100))
    print('Draws     {:4d} {:5.1f}%'.format(draws, draws / total * 100))


if __name__ == '__main__':
    n_games = 1000
    if len(sys.argv) > 1:
        n_games = int(sys.argv[1])
    main(n_games)
