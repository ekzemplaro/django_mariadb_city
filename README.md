# django_mariadb_city

git clone https://github.com/ekzemplaro/django_mariadb_city


mysql> create database django_city;
mysql> grant all on django_city.* to django@localhost;

$ python3 manage.py migrate

cd data
./go_restore.sh
