import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_BASE_DIR = os.path.join(APP_ROOT, 'data/')

DATA_BASE_DIR = '/home/atli/Projects/LOBE/data/'
TOKEN_DIR = os.path.join(DATA_BASE_DIR, 'tokens/')
RECORD_DIR = os.path.join(DATA_BASE_DIR, 'records/')
TOKEN_PAGINATION = 500
RECORDING_PAGINATION = 20
COLLECTION_PAGINATION = 20

SECRET_KEY = 'CHANGE_THIS'
SECURITY_PASSWORD_SALT = 'SOME_SALT'

SECURITY_LOGIN_URL = '/lobe/login'
SECURITY_LOGOUT_URL = '/lobe/logout'


RECAPTCHA_PUBLIC_KEY = '6Lcan7IUAAAAACXrZazA4OeWJ2ZAC1DdxgNK8wUX'
RECAPTCHA_PRIVATE_KEY = '6Lcan7IUAAAAANSmBbECrHlpz5EzSqNVX4uDiwH4'
RECAPTCHA_USE_SSL = False
RECAPTCHA_DATA_ATTRS = {'theme':'dark'}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/lobe_dev'

DEBUG = True