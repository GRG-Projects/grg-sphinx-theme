import os
import json
import sys
from urllib.request import Request, urlopen
from sphinx.application import Sphinx

GH_TOKEN = os.environ.get('GH_TOKEN', '')
CONTRIBUTORS_FILE = 'contributors.json'

def fetch_url(url):
    """
    Notes
    -----
    This was pointed out as a Security issue in bandit.
    please look at issue #355,
    we fixed it, but the bandit warning might remain,
    need to suppress it manually (just ignore it)
    """
    req = Request(url)
    if GH_TOKEN:
        req.add_header('Authorization', 'token {0}'.format(GH_TOKEN))
    try:
        print('fetching %s' % url, file=sys.stderr)
        # url = Request(url,
        #               headers={'Accept': 'application/vnd.github.v3+json',
        #                        'User-agent': 'Defined'})
        if not url.lower().startswith('http'):
            msg = 'Please make sure you use http/https connection'
            raise ValueError(msg)
        f = urlopen(req)
    except Exception as e:
        print(e)
        print('return Empty data', file=sys.stderr)
        return {}

    return f

def get_json_from_url(url):
    """Fetch and read url."""
    f = fetch_url(url)
    return json.load(f) if f else {}

def fetch_basic_stats(project='dipy/dipy'):
    """Fetch the basic stats.

    Returns
    -------
    basic_stats : dict
        A dictionary containing basic statistics. For example:
        {   'subscribers': 41,
            'forks': 142,
            'forks_url': 'https://github.com/fury-gl/fury/network'
            'watchers': 94,
            'open_issues': 154,
            'stars': 94,
            'stars_url': 'https://github.com/fury-gl/fury/stargazers'
        }

    """
    desired_keys = [
        'stargazers_count',
        'stargazers_url',
        'watchers_count',
        'watchers_url',
        'forks_count',
        'forks_url',
        'open_issues',
        'issues_url',
        'subscribers_count',
        'subscribers_url',
    ]
    url = 'https://api.github.com/repos/{0}'.format(project)
    r_json = get_json_from_url(url)
    basic_stats = dict((k, r_json[k]) for k in desired_keys if k in r_json)
    return basic_stats

def get_teams(github_project:str, github_teams:list):
    teams_data = []
    for team in github_teams:
        url = "https://api.github.com/orgs/{0}/teams/{1}/members".format(github_project, team["value"])
        team_data = {
            "name": team["label"],
            "members": get_json_from_url(url)
        }
        teams_data.append(team_data)
    return teams_data

def get_contributors(github_project:str, github_repo:str):
    url = "https://api.github.com/repos/{0}/{1}/contributors?per_page=500".format(github_project, github_repo)
    return get_json_from_url(url)


def add_team_details(
    app: Sphinx
) -> None:
    """Add team deatils in the context"""
    
    # Fetching theme configurations
    theme_conf = app.config.html_theme_options
    # Registering functions for context to access while building
    context = app.config.html_context

    # Setting values in context for usage while building
    context["team_stats"] = fetch_basic_stats()
    context["contributors"] = get_contributors(theme_conf["github_project"], theme_conf["github_repo"])

    if theme_conf["github_teams"]:
        context["teams_data"] = get_teams(theme_conf["github_project"], theme_conf["github_teams"])
        
    