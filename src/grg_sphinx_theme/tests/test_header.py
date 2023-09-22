import re
import pytest

from grg_sphinx_theme.header import (generate_basic_link,
    generate_sub_links, generate_section_title, add_navbar_functions)


# Sample data for testing
sample_link = {"external": False, "url": "internal_file.txt", "name": "Internal Link"}
sample_links = [
    {"external": False, "url": "link1.txt", "name": "Link 1"},
    {"external": True, "url": "link2.txt", "name": "Link 2"},
    ]
sample_section = "Section Title"
sphinx_context = {
    "theme_navbar_links": [
        {"name": "Link 1", "url": "/link1"},
        {"name": "Dropdown 1", "children": [{"name": "Sublink 1", "url": "/sublink1"}, {"name": "Sublink 2", "url": "/sublink2"}]},
        {"name": "Dropdown 2", "sections": [{"name": "Section 1", "links": [{"name": "Subsection 1", "url": "/subsection1"}, {"name": "Subsection 2", "url": "/subsection2"}]}]}
    ]
}

def strip_whitespace(html_string):
    # Use a regular expression to replace multiple whitespace characters with a single space
    return re.sub(r'\s+', ' ', html_string).strip()

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

# TODO: test to update and check for correct html output
# # Test cases for generate_navbar_links function
# def test_generate_navbar_links_with_direct_links():
#     expected_result = """
#       <li class="nav-item">
#         <a class="nav-link " href="/link1">
#           Link 1
#         </a>
#       </li>
#       """
#     sphinx_context["pathto"] = lambda x: f"/path/to/{x}"
#     add_navbar_functions(None, '', '', sphinx_context, None)
#     result = sphinx_context["generate_navbar_links"]()
#     assert strip_whitespace(result) == strip_whitespace(expected_result)

# def test_generate_navbar_links_with_dropdown_links():
#     expected_result = """
#       <li class="nav-item dropdown">
#         <button class="btn dropdown-toggle nav-item" type="button" data-bs-toggle="dropdown" aria-expanded="false" aria-controls="pst-header-nav-more-links">
#           Dropdown 1
#         </button>
#         <ul id="pst-header-nav-more-links" class="dropdown-menu">
#           <li class="nav-item">
#             <a class="nav-link " href="/sublink1">
#               Sublink 1
#             </a>
#           </li>
#           <li class="nav-item">
#             <a class="nav-link " href="/sublink2">
#               Sublink 2
#             </a>
#           </li>
#         </ul>
#       </li>
#       """
#     result = add_navbar_functions(None, '', '', sphinx_context, None)()
#     assert strip_whitespace(result) == strip_whitespace(expected_result)

# def test_generate_navbar_links_with_section_links():
#     expected_result = """
#       <li class="nav-item dropdown">
#         <button class="btn dropdown-toggle nav-item" type="button" data-bs-toggle="dropdown" aria-expanded="false" aria-controls="pst-header-nav-more-links">
#           Dropdown 2
#         </button>
#         <ul id="pst-header-nav-more-links" class="dropdown-menu">
#           <li class="nav-item dropdown">
#             <button class="btn dropdown-toggle nav-item" type="button" data-bs-toggle="dropdown" aria-expanded="false" aria-controls="pst-header-nav-more-links">
#               Section 1
#             </button>
#             <ul id="pst-header-nav-more-links" class="dropdown-menu">
#               <li class="nav-item">
#                 <a class="nav-link " href="/subsection1">
#                   Subsection 1
#                 </a>
#               </li>
#               <li class="nav-item">
#                 <a class="nav-link " href="/subsection2">
#                   Subsection 2
#                 </a>
#               </li>
#             </ul>
#           </li>
#         </ul>
#       </li>
#       """
#     result = add_navbar_functions(None, '', '', sphinx_context, None)()
#     assert strip_whitespace(result) == strip_whitespace(expected_result)
