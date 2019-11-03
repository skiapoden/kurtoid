from jass.player_service.player_service_app import PlayerServiceApp
from jass.player.random_player_schieber import RandomPlayerSchieber

from kurtoid import Kurtoid
from donat_trump import DonatTrump
from permutoid import Permutoid
from carloid import Carloid

def create_app():
    app = PlayerServiceApp('kurtoid_service')

    app.add_player('Kurt', Kurtoid())
    app.add_player('Maurin', DonatTrump())
    app.add_player('Randy', RandomPlayerSchieber())
    app.add_player('Permi', Permutoid())
    for depth in range(4):
        app.add_player('Carlo{:d}'.format(depth), Carloid(depth))

    return app

app = create_app()

@app.route('/canary')
def canary():
    return 'ok\n'
