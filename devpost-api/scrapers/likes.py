import requests
from scrapers import shared
from bs4 import BeautifulSoup

class Likes:
    soup = None

    def __init__(self, username):
        req = requests.get(f'{shared.base_url}{username}/likes')
        self.soup = BeautifulSoup(req.text, 'lxml')

    def get_likes(self) -> [str]:
        entries = self.soup.select('#software-entries .link-to-software[href]')
        for entry in entries:
            yield entry['href']
