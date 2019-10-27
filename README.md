# kurtoid

Jass-Bot für das Modul DL4G (einem Entlebucher Grossmeister im Jassen nachempfunden)

## Build, Run, and Deploy

Run locally:

    $ cd app
    $ gunicorn -b 0.0.0.0:5000 main:app

Build using a Docker container:

    $ username="[EnterpriseLab User Name]" password="[EnterpriseLab Password]" ./build.sh

The two environment variables `username` and `password` (GitLab credentials) are used as build arguments.

Run the Docker container:

    $ ./run.sh

Test the application:

    $ curl localhost:5000/canary

Publish to Heroku:

    $ heroku login
    $ username="[EnterpriseLab User Name]" password="[EnterpriseLab Password]" ./deploy.sh

## Run Tournaments

1. Create a new Tournament on the [Jass Server](https://jass-server.abiz.ch/tournaments)
2. Register players with their `PLAYER_NAME`as defined in `main.py` (`app.add_player(PLAYER_NAME, ...)`). The URL must be of the form `http://kurtoid.herokuapp.com/PLAYER_NAME`
3. Start the Tournament
4. Check the logs using `heroku logs -a kurtoid --tail`
