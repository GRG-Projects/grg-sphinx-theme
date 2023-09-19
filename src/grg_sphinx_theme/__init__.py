"""
GRG Sphinx Theme
"""
from pathlib import Path
from . import header, team

try:
    from ._version import version as __version__
except ImportError:
    pass

def get_html_theme_path():
    """Return list of HTML theme paths."""
    parent = Path(__file__).parent.resolve()
    theme_path = parent / "theme" / "grg_sphinx_theme"
    return theme_path

def setup(app):
    """Setup the Sphinx application for grg-sphinx-theme"""
    app.add_html_theme('grg_sphinx_theme', get_html_theme_path())
    app.connect("html-page-context", header.add_navbar_functions)
    app.connect("builder-inited", team.add_team_details)