import os


class Config(object):
    YERR = 'YERR'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key-for-devs'
