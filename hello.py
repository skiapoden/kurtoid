import os

from flask import Flask

from jass.player.random_player_schieber import RandomPlayerSchieber

app = Flask(__name__)

@app.route('/')
def hello_kurtoid():
    kurtoid = RandomPlayerSchieber
    return 'Hallo, ich bin Kurtoid! Ich habe folgende Methoden: {}\n'.format(dir(kurtoid))

if __name__ == '__main__':
    port = '5000'
    if 'PORT' in os.environ:
        port = os.environ['PORT']
    app.run(host='0.0.0.0', port=port)
