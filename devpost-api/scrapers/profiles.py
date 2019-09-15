import requests
from scrapers import shared
from bs4 import BeautifulSoup

class Profile:
    soup = None

    def __init__(self, username):
        req = requests.get('https://devpost.com/' + username)
        self.soup = BeautifulSoup(req.text, 'lxml')

    def is_error_page(self) -> bool:
        return shared.is_error_page(self.soup)
        
    def is_restricted_page(self) -> bool:
        return shared.is_restricted_page(self.soup)

    def get_profile_img_url(self) -> str:
        profile_img = self.soup.select_one('#portfolio-user-photo img[src]')
        return profile_img['src']

    def get_names(self) -> (str, str):
        user_name = self.soup.select_one('#portfolio-user-name')
        name, username = '', ''
        for item in user_name:
            if isinstance(item, str):
                name += item
            else:
                username = item.text
        return (name.strip(), username[1:-1])

    def get_bio(self) -> str:
        return self.soup.find(id='portfolio-user-bio').text.strip()

    def get_links(self) -> (str, str, str):
        links = self.soup.find(id='portfolio-user-links')
        location = links.select_one('li:has(.ss-location)').text.strip()
        website = links.select_one('li:has(.ss-link) a[href]')['href']
        github = links.select_one('li:has(.ss-octocat) a[href]')['href']
        return (location, website, github)

    def _get_user_info_table_items(self, i: int) -> [str]:
        lists = self.soup.select('#portfolio-user-info div:has(div > span > strong) ul')
        items = lists[i].select('li span')
        items = [x.text.strip() for x in items]
        return items

    def get_skills(self) -> [str]:
        return self._get_user_info_table_items(1)

    def get_interests(self) -> [str]:
        return self._get_user_info_table_items(2)

    def get_software_entries(self) -> [str]:
        entries = self.soup.select('#software-entries .link-to-software[href]')
        entries = [x['href'] for x in entries]
        return entries