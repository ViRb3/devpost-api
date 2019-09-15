import requests
from bs4 import BeautifulSoup

class Challenges:
    soup = None
    challenges = None

    def __init__(self, username):
        req = requests.get(f'https://devpost.com/{username}/challenges')
        self.soup = BeautifulSoup(req.text, 'lxml')
        self.challenges = self.soup.select_one('.challenge-container')

    def get_hackathons(self) -> [str]:
        hackathons = self.challenges.select('div:has(.challenge-synopsis) a[href]')
        hackathons = [x['href'].rsplit('/', 1)[0] for x in hackathons]
        return hackathons
