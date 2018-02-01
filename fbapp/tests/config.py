import os
SECRET_KEY = 'votre_nouvelle_cle_secrete'

# Remplacez par l'id de l'app TEST que vous avez créée précédemment.
FB_APP_ID = 1556018984483068

basedir = os.path.abspath(os.path.dirname(__file__))

# Nouvelle base de données pour les tests.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app_test.db')

# Active le debogueur
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10
SERVER_NAME = 'localhost:8943'

# Facebook test user
FB_USER_NAME = "Open Graph Test User"
FB_USER_PW = "passer"
FB_USER_EMAIL = "open_zaplzsq_user@tfbnw.net"
FB_USER_ID = 100018814390853
FB_USER_GENDER = 'female'