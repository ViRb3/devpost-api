import requests
from scrapers import shared
from bs4 import BeautifulSoup

class Following:
    soup = None

    def __init__(self, username):
        req = requests.get(f'{shared.base_url}{username}/following')
        self.soup = BeautifulSoup(req.text, 'html.parser')

    def get_following(self) -> [str]:
        following = self.soup.select('#follow-entries div a[href]')
        for follow in following:
            yield follow['href']
