import requests
from scrapers import shared
from bs4 import BeautifulSoup

class Profile:
    soup: BeautifulSoup = None

    def __init__(self, username):
        req = requests.get(f'{shared.base_url}{username}')
        self.soup = BeautifulSoup(req.text, 'lxml')

    def is_error_page(self) -> bool:
        return shared.is_error_page(self.soup)
        
    def is_restricted_page(self) -> bool:
        return shared.is_restricted_page(self.soup)

    def get_profile_img_url(self) -> str:
        profile_img = self.soup.select_one('#portfolio-user-photo img[src]')
        if profile_img == None:
            return ''
        return profile_img['src']

    def get_names(self) -> (str, str):
        user_name = self.soup.select_one('#portfolio-user-name')
        name, username = '', ''
        for item in user_name:
            if isinstance(item, str):
                name += item
            else:
                username = item.text
        # strip parentheses
        if len(username) > 3:
            username = username[1:-1]
        return {'fullname': name.strip(), 'username': username}

    def get_bio(self) -> str:
        bio = self.soup.select_one('#portfolio-user-bio')
        if bio == None:
            return ''
        return bio.text.strip()

    def _get_links_location(self, links) -> str:
        location = links.select_one('li:has(.ss-location)')
        if location == None:
            return location
        return location.text.strip()

    def _get_links_website(self, links) -> str:
        website = links.select_one('li:has(.ss-link) a[href]')
        if website == None:
            return website
        return website['href']

    def _get_links_github(self, links) -> str:
        github = links.select_one('li:has(.ss-octocat) a[href]')
        if github == None:
            return github
        return github['href']

    def get_links(self) -> (str, str, str):
        links = self.soup.select_one('#portfolio-user-links')
        if links == None:
            return {'location':'', 'website':'', 'github':''}
        location = self._get_links_location(links)
        website = self._get_links_website(links)
        github = self._get_links_github(links)
        return {'location': location, 'website': website, 'github': github}

    def _get_user_info_table_items(self, i: int) -> [str]:
        lists = self.soup.select('#portfolio-user-info div:has(div > span > strong) ul')
        if len(lists)-1 < i:
            return []
        items = lists[i].select('li span')
        for item in items:
            yield item.text.strip()

    def get_skills(self) -> [str]:
        return self._get_user_info_table_items(1)

    def get_interests(self) -> [str]:
        return self._get_user_info_table_items(2)

    def get_software_entries(self) -> [str]:
        entries = self.soup.select('#software-entries .link-to-software[href]')
        for entry in entries:
            yield entry['href']