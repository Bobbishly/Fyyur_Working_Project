import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/fyyur'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/fyyur_legit'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost:5432/fyyur_legit2'
SQLALCHEMY_TRACK_MODIFICATIONS = False
