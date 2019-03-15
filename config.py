import os


class Config:
    def __init__(self):
        self.base_url = 'http://api.steampowered.com/',
        self.key = os.environ.get('SECRET_KEY')
