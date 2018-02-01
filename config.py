import os

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"

if os.environ.get('DATABASE_URL') is None:
	basedir = os.path.abspath(os.path.dirname(__file__))
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	FB_APP_ID = 1556018984483068
else:
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	FB_APP_ID = 833751096807156