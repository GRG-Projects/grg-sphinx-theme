import os
import json
import sys
from urllib.request import Request, urlopen
from sphinx.application import Sphinx
from sphinx.util import logger

GH_TOKEN = os.environ.get('GH_TOKEN', '')

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

def fetch_basic_stats(github_project:str, github_repo:str, contributors:list):
    """Fetch the basic stats."""

    desired_keys = [
        'stargazers_count',
        'forks_count',
    ]
    url = 'https://api.github.com/repos/{0}/{1}'.format(github_project, github_repo)
    r_json = get_json_from_url(url)
    basic_stats = dict((k, r_json[k]) for k in desired_keys if k in r_json)

    basic_stats.update({"contributors": len(contributors)})
    total_contributions = 0
    for contributor in contributors:
        total_contributions += contributor["contributions"]
    basic_stats.update({"total_contributions": total_contributions})

    return basic_stats

def login_to_fullname(contributors:list, contributors_details:list):
    """Updates the login from github to fullname of the contributor."""
    for contributor in contributors:
        for contributor_detail in contributors_details:
            if contributor["login"].lower() == contributor_detail["login"].lower():
                contributor["login"] = contributor_detail["fullname"]
                if "priority" in contributor_detail:
                    contributor["priority"] = contributor_detail["priority"]
        if "priority" not in contributor:
            contributor["priority"] = 100000000000

    return sorted(contributors, key=lambda x: x["priority"])

def get_teams(github_project:str, github_teams:list, contributors_details:list = None):
    """Fetch team details from github."""
    teams_data = []
    for team in github_teams:
        # Check Response Reference in github Apis
        url = "https://api.github.com/orgs/{0}/teams/{1}/members".format(github_project, team["value"])
        members = get_json_from_url(url)
        if members:
            if contributors_details:
                members = login_to_fullname(members, contributors_details)
            team_data = {
                "name": team["label"],
                "members": members
            }
            teams_data.append(team_data)
        else:
            logger.warning("Unable to fetch team data for team: {0}. Check your API key or the name of the team!".format(team))
    return teams_data

def get_contributors(github_project:str, github_repo:str, contributors_details:list = None):
    """Fetch list of contributors from github."""

    url = "https://api.github.com/repos/{0}/{1}/contributors?per_page=500".format(github_project, github_repo)
    contributors = get_json_from_url(url)
    if contributors_details:
        contributors = login_to_fullname(contributors, contributors_details)
    return contributors


def add_team_details(
    app: Sphinx
) -> None:
    """Add team deatils in the context"""

    # Fetching theme configurations
    theme_conf = app.config.html_theme_options
    # Registering functions for context to access while building
    context = app.config.html_context

    if "github_project" not in theme_conf or "github_repo" not in theme_conf:
        return

    if not theme_conf["github_project"] or not theme_conf["github_repo"]:
        return

    # Setting values in context for usage while building
    context["contributors"] = get_contributors(theme_conf["github_project"], theme_conf["github_repo"], theme_conf.get("contributors_details"))


    context["team_stats"] = fetch_basic_stats(theme_conf["github_project"], theme_conf["github_repo"], context["contributors"])

    if "github_teams" in theme_conf:
        context["teams_data"] = get_teams(theme_conf["github_project"], theme_conf["github_teams"], theme_conf.get("contributors_details"))






