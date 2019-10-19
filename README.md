# kurtoid

Jass-Bot für das Modul DL4G (einem Entlebucher Grossmeister im Jassen nachempfunden)

## Instructions

Run locally:

    $ python hello.py

Build using a Docker container:

    $ username="[EnterpriseLab User Name]" password="[EnterpriseLab Password]" ./build.sh

The two environment variables `username` and `password` (GitLab credentials) are used as build arguments.

Run the Docker container:

    $ ./run.sh

Test the application:

    $ curl localhost:5000

Publish to Heroku:

    $ username="[EnterpriseLab User Name]" password="[EnterpriseLab Password]" ./deploy.sh
