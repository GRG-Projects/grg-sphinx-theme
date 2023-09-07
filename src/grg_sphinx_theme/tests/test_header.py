import re
import pytest

from grg_sphinx_theme.header import (
    generate_url, external_link_classes,generate_basic_link,
    generate_sub_links, generate_section_title, external_link_classes,
    generate_url)


# Sample data for testing
sample_link = {"external": False, "url": "internal_file.txt", "name": "Internal Link"}
sample_links = [
    {"external": False, "url": "link1.txt", "name": "Link 1"},
    {"external": True, "url": "link2.txt", "name": "Link 2"},
    ]
sample_section = "Section Title"

def strip_whitespace(html_string):
    # Use a regular expression to replace multiple whitespace characters with a single space
    return re.sub(r'\s+', ' ', html_string).strip()

# Test cases for generate_url function
def test_generate_url_internal_link():
    link = {"external": False, "url": "internal_file.txt"}
    context = {"pathto": lambda x: f"/path/to/{x}"}
    result = generate_url(link, context)
    assert result == "/path/to/internal_file.txt"

def test_generate_url_external_link():
    link = {"external": True, "url": "external_file.txt"}
    context = {}
    result = generate_url(link, context)
    assert result == "external_file.txt"

# Test cases for external_link_classes function
def test_external_link_classes_internal_link():
    link = {"external": False, "url": "internal_file.txt"}
    result = external_link_classes(link)
    assert result == ""

def test_external_link_classes_external_link():
    link = {"external": True, "url": "external_file.txt"}
    result = external_link_classes(link)
    assert result == "nav-external"

# Additional test case for generate_url with missing "pathto" in context
def test_generate_url_missing_pathto():
    link = {"external": False, "url": "internal_file.txt"}
    context = {}
    with pytest.raises(KeyError):
        generate_url(link, context)

def test_generate_basic_link_external_link():
    context = {"pathto": lambda x: f"{x}"}
    external_link = {"external": True, "url": "internal_file.txt", "name": "Internal Link"}
    result = generate_basic_link(external_link, context)
    expected_result = """
      <li class="nav-item">
        <a class="nav-link nav-external" href="internal_file.txt">
          Internal Link
        </a>
      </li>
      """
    assert strip_whitespace(result) == strip_whitespace(expected_result)

# Test cases for generate_section_title function
def test_generate_section_title():
    result = generate_section_title(sample_section)
    expected_result = """
      <li class="nav-item">
        <p class="nav-section-title nav-link">
          Section Title
        </p>
      </li>
      """
    assert strip_whitespace(result) == strip_whitespace(expected_result)

# Test cases for generate_basic_link function
def test_generate_basic_link_internal_link():
    context = {"pathto": lambda x: f"/path/to/{x}"}
    result = generate_basic_link(sample_link, context)
    expected_result = """
      <li class="nav-item">
        <a class="nav-link " href="/path/to/internal_file.txt">
          Internal Link
        </a>
      </li>"""
    assert strip_whitespace(result) == strip_whitespace(expected_result)

def test_generate_basic_link_missing_pathto_in_context():
    context = {}  # Missing "pathto" function in context
    with pytest.raises(KeyError):
        generate_basic_link(sample_link, context)

def test_generate_basic_link_missing_url_in_link():
    invalid_link = {"external": False, "name": "Invalid Link"}  # Missing "url" key
    context = {"pathto": lambda x: f"/path/to/{x}"}
    with pytest.raises(KeyError):
        generate_basic_link(invalid_link, context)

# Test cases for generate_sub_links function
def test_generate_sub_links():
    context = {"pathto": lambda x: f"/path/to/{x}"}
    result = generate_sub_links(sample_links, context)
    expected_result = """
      <li class="nav-item">
        <a class="nav-link " href="/path/to/link1.txt">
          Link 1
        </a>
      </li>

      <li class="nav-item">
        <a class="nav-link nav-external" href="link2.txt">
          Link 2
        </a>
      </li>
    """
    assert result.strip() == expected_result.strip()

def test_generate_sub_links_empty_list():
    empty_links = []
    context = {"pathto": lambda x: f"/path/to/{x}"}
    result = generate_sub_links(empty_links, context)
    assert result == ""

# Test cases for generate_section_title function
def test_generate_section_title():
    result = generate_section_title(sample_section)
    expected_result = """
      <li class="nav-item">
        <p class="nav-section-title nav-link">
          Section Title
        </p>
      </li>
      """
    assert strip_whitespace(result) == strip_whitespace(expected_result)

def test_generate_section_title_empty_section():
    empty_section = ""
    result = generate_section_title(empty_section)
    expected_result = """
    <li class="nav-item">
    <p class="nav-section-title nav-link">

    </p>
    </li>"""
    assert strip_whitespace(result) == strip_whitespace(expected_result)
