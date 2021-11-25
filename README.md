# django_mariadb_city

	Nov/25/2021

git clone https://github.com/ekzemplaro/django_mariadb_city


sudo pip3 install django-environ


mysql> create database django_city;
mysql> grant all on django_city.* to django@localhost;

cd proj01
python3 manage.py migrate

cd data
./go_restore.sh

cd proj01
python3 manage.py runserver

http://127.0.0.1:8000/city/

