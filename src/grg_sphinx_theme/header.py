from sphinx.application import Sphinx

def add_navbar_functions(
    app: Sphinx, pagename: str, templatename: str, context, doctree
) -> None:
  """
  Add functions so Jinja template can create navbar details
  """
  def generate_navbar_links() -> str:
    """
    Generate different links for navbar_links configuration
    """

    # returns specific path for internal files
    def generate_url(link: dict) -> str:
      if "external" in link and link["external"]:
        return link["url"]
      return context["pathto"](link["url"])

    # returns the required class for external link
    def external_link(link: dict) -> str:
      if "external" in link and link["external"]:
        return """ nav-external"""
      return ""

    # constructs a basic link structure
    def generate_basic_link(link: dict) -> str:
      return f"""
          <li class="nav-item">
            <a class="nav-link{external_link(link)}" href="{generate_url(link)}">
              {link["name"]}
            </a>
          </li>
          """

    # constructs list of basic links
    def generate_sub_links(links: list) -> str:
      links_html = []
      for link in links:
        links_html.append(generate_basic_link(link))
      return "\n".join(links_html)
    
    # constructs section title element
    def generate_section_title(section: str) -> str:
      return f"""
          <li class="nav-item">
            <p class="nav-section-title nav-link">
              {section}
            </p>
          </li>
          """
    
    # constructs section wise links
    def generate_section_wise_links(links: list) -> str:
      links_html = []
      for link in links:
        links_html.append(generate_section_title(link["name"]))
        links_html.append(generate_sub_links(link["children"]))
      return "\n".join(links_html)
    
    links = context.get("theme_navbar_links")

    html_links = []

    for link in links:
      # If "url" is present: direct link
      if "url" in link:
        html_links.append(generate_basic_link(link))
      
      # If "children" is present: simple dropdown
      elif "children" in link:
        html_links.append(
          f"""
          <li class="nav-item dropdown">
                <button class="btn dropdown-toggle nav-item" type="button" data-bs-toggle="dropdown" aria-expanded="false" aria-controls="pst-header-nav-more-links">
                    {link["name"]}
                </button>
                <ul id="pst-header-nav-more-links" class="dropdown-menu">
                    {generate_sub_links(link["children"])}
                </ul>
            </li>
          """
        )

      # If "sections" is present: section wise dropdown
      elif "sections" in link:
        html_links.append(
          f"""
          <li class="nav-item dropdown">
                <button class="btn dropdown-toggle nav-item" type="button" data-bs-toggle="dropdown" aria-expanded="false" aria-controls="pst-header-nav-more-links">
                    {link["name"]}
                </button>
                <ul id="pst-header-nav-more-links" class="dropdown-menu">
                    {generate_section_wise_links(link["sections"])}
                </ul>
            </li>
          """
        )

    
    out = "\n".join(html_links)

    return out
  
  # Registering functions for context to access while building
  context["generate_navbar_links"] = generate_navbar_links

