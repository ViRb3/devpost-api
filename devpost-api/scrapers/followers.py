import requests
from scrapers import shared
from bs4 import BeautifulSoup

class Followers:
    soup = None

    def __init__(self, username):
        req = requests.get(f'{shared.base_url}{username}/followers')
        self.soup = BeautifulSoup(req.text, 'lxml')

    def get_followers(self) -> [str]:
        followers = self.soup.select('#follow-entries div a[href]')
        for follow in followers:
            yield shared.base_url + follow['href']
