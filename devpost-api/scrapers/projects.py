import requests
from scrapers import shared
from bs4 import BeautifulSoup

class Projects:
    soup = None

    def __init__(self, project_name):
        req = requests.get(f'{shared.base_url}software/{project_name}')
        self.soup = BeautifulSoup(req.text, 'html.parser')

    def is_error_page(self) -> bool:
        return shared.is_error_page(self.soup)

    def is_restricted_page(self) -> bool:
        return shared.is_restricted_page(self.soup)

    def get_text(self) -> [str]:
        entries = self.soup.select('#app-details-left > div')
        if len(entries) < 2:
            return []
        entries = entries[1]
        return entries.text.strip()

    def get_title(self) -> str:
        title = self.soup.select_one('#app-title')
        if title == None:
            return ''
        return title.text

    def get_heading(self) -> str:
        heading = self.soup.select_one('div:has(> #app-title) > p')
        if heading == None:
            return ''
        return heading.text.strip()

    def get_built_with(self) -> [str]:
        items = self.soup.select('#built-with li')
        for item in items:
            yield item.text

    def get_members(self) -> [(str, str)]:
        members = self.soup.select('#app-team ul li')
        for member in members:
            url = member.select_one('div figure > a[href]')
            if url == None:
                continue
            url = url['href']
            description = member.select_one('div > p')
            description = '' if description == None else description.text
            yield {'url': url, 'description': description}

    def get_submissions(self) -> [str]:
        subs = self.soup.select('#submissions ul li figure a[href]')
        for sub in subs:
            yield sub['href']
