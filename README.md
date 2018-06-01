# telegram bot base project with django

This is a code base for a telegram bot that uses [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
for telegram bot api wrapping and [django models](https://docs.djangoproject.com/en/2.0/topics/db/) as it's database managing system(ORM)
# configuring the bot before use

first open `private_conf.py` and set your api token and proxy if you are using one.

the underlying proxy system uses `HTTP` and `HTTPS` proxies. 
if you are using a `Socks5` proxy install `PySocks` module first.

# instaling dependencies

install dependencies for this project by running:

`pip install -r requirements.txt`

# running the bot

`python manage.py startbot`