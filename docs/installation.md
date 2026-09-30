# Installation

Install from PyPI:

```sh
pip install sphinxext-versionwarning
```

Or install from GitHub:

```sh
pip install git+https://github.com/GrahamSH-LLK/sphinx-version-warning.git@main
```

Add the extension to your Sphinx `conf.py`:

```python
extensions = [
    # ... other extensions here
    'versionwarning.extension',
]
```

## Enable the Read the Docs Addons API

The extension receives active-version information from the Read the Docs Addons API. Add this meta tag to every HTML page:

```html
<meta name="readthedocs-addons-api-version" content="1" />
```

One way to do this in Sphinx is to create `_templates/layout.html` with:

```jinja
{% extends "!layout.html" %}

{% block extrahead %}
  {{ super() }}
  <meta name="readthedocs-addons-api-version" content="1" />
{% endblock %}
```

Then configure the template directory in `conf.py`:

```python
templates_path = ['_templates']
```

Build your documentation on Read the Docs. When an older semantic version is visited, the banner points to the equivalent page in the highest active semantic version. See [configuration](configuration.md) to customize version selection and banner messages.
