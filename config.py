__strict__ = True

import os


class Config:
    DEBUG = os.environ.get('DEBUG', False) == '1'
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'this-really-needs-to-be-changed')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
