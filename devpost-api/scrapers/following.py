import requests
from bs4 import BeautifulSoup

base_url = 'https://devpost.com'

class Following:
    soup = None

    def __init__(self, username):
        req = requests.get(f'https://devpost.com/{username}/following')
        self.soup = BeautifulSoup(req.text, 'lxml')

    def get_following(self) -> [str]:
        following = self.soup.select('#follow-entries div a[href]')
        following = [base_url + x['href'] for x in following]
        return following
