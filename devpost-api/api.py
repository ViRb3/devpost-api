from scrapers.challenges import *
from scrapers.followers import *
from scrapers.following import *
from scrapers.likes import *
from scrapers.profiles import *

from scrapers.projects import *

def get_project(project_name):
    result = {}

    project = Projects(project_name)
    if project.is_error_page():
        return 'not found', 404
    if project.is_restricted_page():
        return 'restricted', 401
    result['title'] = project.get_title()
    result['heading'] = project.get_heading()
    result['text'] = project.get_text()
    result['built-with'] = project.get_built_with()
    result['submissions'] = project.get_submissions()
    result['members'] = list(project.get_members())

    return result

def get_user(username):
    result = {}

    profile = Profile(username)
    if profile.is_error_page():
        return 'not found', 404
    if profile.is_restricted_page():
        return 'restricted', 401
    result['names'] = profile.get_names()
    result['bio'] = profile.get_bio()
    result['profile_img_url'] = profile.get_profile_img_url()
    result['links'] = profile.get_links()
    result['skills'] = profile.get_skills()
    result['interests'] = profile.get_interests()
    result['software_entries'] = profile.get_software_entries()

    followers = Followers(username)
    result['followers'] = followers.get_followers()

    following = Following(username)
    result['following'] = following.get_following()

    likes = Likes(username)
    result['likes'] = likes.get_likes()

    return result