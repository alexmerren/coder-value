import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
THREADS_PER_PAGE = 2
CSRF_ENABLED = True
# I'm not sure that we need both of these...
# CSRF_SESSION_KEY - Use a secure, unique, and absolutely secret key for signing the data.
# SECRET_KEY - Secret key for signing cookies
CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"


