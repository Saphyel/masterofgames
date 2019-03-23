import os


class Config:
    def __init__(self):
        self.base_url = 'https://api.steampowered.com/'
        self.key = os.environ.get('SECRET_KEY', 'XXXXXXX')
