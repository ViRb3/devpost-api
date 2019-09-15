base_url = 'https://devpost.com/'

def is_error_page(source) -> bool:
    return source.select_one('html.error-404') != None

def is_restricted_page(source) -> bool:
    return source.select_one('#user-login') != None