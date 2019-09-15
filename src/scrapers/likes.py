import requests
from bs4 import BeautifulSoup

class Likes:
    soup = None

    def __init__(self, username):
        req = requests.get(f'https://devpost.com/{username}/likes')
        self.soup = BeautifulSoup(req.text, 'lxml')

    def get_likes(self) -> [str]:
        entries = self.soup.select('#software-entries .link-to-software[href]')
        entries = [x['href'] for x in entries]
        return entries
