"""
GRG Sphinx Theme
"""
from pathlib import Path
from . import header

__version__ = "0.1.0"
"""grg-sphinx-theme version"""

def get_html_theme_path():
    """Return list of HTML theme paths."""
    parent = Path(__file__).parent.resolve()
    theme_path = parent / "theme" / "grg_sphinx_theme"
    return theme_path

def setup(app):
    """Setup the Sphinx application for grg-sphinx-theme"""
    app.add_html_theme('grg_sphinx_theme', get_html_theme_path())
    app.connect("html-page-context", header.add_navbar_functions)