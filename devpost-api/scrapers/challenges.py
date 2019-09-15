
import httpx
from scrapers import shared
from bs4 import BeautifulSoup

class Challenges:
    soup = None
    challenges = None

    def __init__(self, username):
        req = httpx.get(f'{shared.base_url}{username}/challenges')
        self.soup = BeautifulSoup(req.text, 'lxml')
        self.challenges = self.soup.select_one('.challenge-container')

    def get_hackathons(self) -> [str]:
        hackathons = self.challenges.select('div:has(.challenge-synopsis) a[href]')
        for hackathon in hackathons:
            yield hackathon['href'].rsplit('/', 1)[0]
