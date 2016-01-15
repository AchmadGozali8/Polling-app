'''configuration'''
import os

DEBUG = True
APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR,os.pardir))

SQLALCHMEY_DATABASE_URI='sqlite:///' + PROJECT_ROOT+'apps.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False