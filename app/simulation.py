#!/usr/bin/env python3

from jass.base.const import JASS_SCHIEBER_2500
from jass.arena.arena import Arena
from jass.arena.trump_selection_players_strategy import TrumpPlayerStrategy
from jass.arena.play_game_nr_rounds_strategy import PlayNrRoundsStrategy
from jass.player.random_player_schieber import RandomPlayerSchieber

from kurtoid import Kurtoid

def main():
    arena = Arena(jass_type=JASS_SCHIEBER_2500,
                  trump_strategy=TrumpPlayerStrategy(),
                  play_game_strategy=PlayNrRoundsStrategy(4))

    opponent = RandomPlayerSchieber()
    kurtoid = Kurtoid()
    arena.set_players(kurtoid, opponent, kurtoid, opponent)

    arena.nr_games_to_play = 1000
    arena.play_all_games()

    kurtoid_wins = arena.nr_wins_team_0 
    opponent_wins = arena.nr_wins_team_1
    draws = arena.nr_draws
    total = kurtoid_wins + opponent_wins + draws

    print('Kurtoid Wins:  {:4d}  {:.1f}%'.format(kurtoid_wins, kurtoid_wins / total * 100))
    print('Opponent Wins: {:4d}  {:.1f}%'.format(opponent_wins, opponent_wins / total * 100))
    print('Draws:         {:4d}  {:.1f}%'.format(draws, draws / total * 100))


if __name__ == '__main__':
    main()
