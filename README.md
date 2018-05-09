
# Welcome to MacPorts webapp.

The Idea is to create a final web app displaying these things about a particular port (eg: <https://macports.org/port/python27> ) :

- Port Information

All the port information will stored in port table .

- Build History/Summary

All the history as far as available will be stored.

- Installation Statistics

If a user volunteers for Statistics.
Updated Statistics version will give wonderful insights.

- Results of Livecheck

- Git Log / Commit History

- Links to track tickets for that port 

- Binary Package status

- Links for Pull Request (Optional)


This project is currently active on : <https://macports.herokuapp.com/port/>


# Setup in Local Envirnoment

### Install python
```
python3 --version
sudo apt-get install python3.6
```
### Install *pipenv*
`pip install --user pipenv`

### Install *postgresql*
```
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
pip3 install psycopg2
```
### Install *gunicorn* (Needed for heroku deployment)
`pip3 install gunicorn`

Run these
```
git clone https://github.com/macports/macports-webapp.git
cd macports-webapp
```

### Open settings ('macports/settings.py') and change the Database according to your database

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'macports',
        'USER': 'postgres',
        'PASSWORD': 'qwerty',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### Now run these commands
```
pip --three
pipenv install
pipenv shell
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```
open the ip provided. And add `/port` at the end of the ip.

`http://127.0.0.1:8000/port`




# Deploying to Heroku

```
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open```
