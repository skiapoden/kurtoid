#!/bin/sh

heroku container:login
heroku container:push --arg username="${username}",password="${password}" -a kurtoid web
heroku container:release -a kurtoid web
heroku ps:scale web=1 -a kurtoid
curl https://kurtoid.herokuapp.com/
