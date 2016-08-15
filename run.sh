#!/bin/bash

mkdir -p cached/en
for lang in cs ct de es fr it jp kr pt ru;
do
  mkdir -p cached/$lang
  mkdir -p cached/links/$lang
done

. ./env.sh $1
python ./manage.py migrate
python ./manage.py runserver 0.0.0.0:8000

