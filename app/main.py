from jass.player_service.player_service_app import PlayerServiceApp
from jass.player.random_player_schieber import RandomPlayerSchieber

from kurtoid import Kurtoid

def create_app():
    app = PlayerServiceApp('kurtoid_service')
    app.add_player('Kurt', Kurtoid())
    app.add_player('Hans', Kurtoid())
    app.add_player('Sepp', Kurtoid())
    app.add_player('Schorsch', Kurtoid())
    return app

app = create_app()

@app.route('/canary')
def canary():
    return 'ok\n'
