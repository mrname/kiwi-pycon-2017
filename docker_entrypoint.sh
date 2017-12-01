#!/bin/bash

# NOTE - this sleep is a stupid hack to keep our demo simple. The point is
# that we need the database server to be up and running before we do our
# database migrations. There are better ways to do this!
# https://docs.docker.com/compose/startup-order/
sleep 5

python manage.py collectstatic --noinput
python manage.py migrate --noinput

python manage.py runserver 0.0.0.0:8000
