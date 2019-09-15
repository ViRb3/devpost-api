import requests
from bs4 import BeautifulSoup

class Projects:
    soup = None

    def __init__(self, project_name):
        req = requests.get('https://devpost.com/software/' + project_name)
        self.soup = BeautifulSoup(req.text, "lxml")

    def get_text(self) -> [str]:
        entries = self.soup.select('#app-details-left > div')[1]
        return entries.text.strip()

    def get_title(self) -> str:
        return self.soup.select_one('#app-title').text

    def get_heading(self) -> str:
        return self.soup.select_one('div:has(> #app-title) > p').text.strip()

    def get_built_with(self) -> [str]:
        items = self.soup.select('#built-with li')
        items = [x.text for x in items]
        return items

    def get_members(self) -> [(str, str)]:
        members = self.soup.select('#app-team ul li')
        for member in members:
            url = member.select_one('div figure > a[href]')['href']
            description = member.select_one('div > p')
            description = '' if description == None else description.text
            yield (url, description)

    def get_submissions(self) -> [str]:
        subs = self.soup.select('#submissions ul li figure a[href]')
        subs = [x['href'] for x in subs]
        return subs
