# grg-sphinx-theme

A Sphinx theme for GRG projects and its affiliated packages.

## Usage

**install**

```
pip install grg-sphinx-theme
```

To start using the theme you need to set the theme in `conf.py` 

```python
html_theme = "grg_sphinx_theme"
```

To set different navbar-links update the html_theme_options 

```
html_theme_options = {
...
  "navbar_center": ["components/navbar-links.html"],
  "navbar_links": [
     {
        "url": "#",
        "name": "Home",
     },
     {
        "name": "Community",
        "children": [
          {
            "url": "https://www.geeksforgeeks.org/python-ways-to-concatenate-two-lists/",
            "name": "GeeksForGeeks",
            "external": True
          }
        ]
     },
     {
        "name": "Multiple",
        "sections": [
            {
              "name": "First",
              "children": [
                  {
                    "name": "First-Hello",
                    "url": "",
                    "external": True
                  },
                  {
                    "name": "First-How",
                    "url": ""
                  }
              ]
            },
            {
              "name": "Second",
              "children": [
                  {
                    "name": "Second-Hello",
                    "url": ""
                  },
                  {
                    "name": "Second-How",
                    "url": "",
                    "external": True
                  }
              ]
            }
        ]
     }
  ]
...
}
```

## Contributing Guidelines

For contribution we are required to have to maintain the same coding standard and formatting. We recommend using VSCode as an editor and use prettier extension on the VSCode.

For more steps, you can read our [Contributing guidelines](CONTRIBUTING.md)
