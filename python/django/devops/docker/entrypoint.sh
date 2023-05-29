#!/usr/bin/env bash

./manage.py makemigrations logbook
./manage.py migrate
./manage.py loaddata tags
./manage.py runserver