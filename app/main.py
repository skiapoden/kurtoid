from jass.player_service.player_service_app import PlayerServiceApp
from jass.player.random_player_schieber import RandomPlayerSchieber

from kurtoid import Kurtoid
from donat_trump import DonatTrump

def create_app():
    app = PlayerServiceApp('kurtoid_service')
    app.add_player('Kurt', Kurtoid())
    app.add_player('Maurin', DonatTrump())
    app.add_player('Randy', RandomPlayerSchieber())
    return app

app = create_app()

@app.route('/canary')
def canary():
    return 'ok\n'
