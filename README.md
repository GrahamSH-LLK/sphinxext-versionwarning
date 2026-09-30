# sphinxext-versionwarning

[![PyPI version](https://img.shields.io/pypi/v/sphinxext-versionwarning.svg)](https://pypi.org/project/sphinxext-versionwarning/) [![License](https://img.shields.io/github/license/grahamsh-llk/sphinx-version-warning.svg)](LICENSE)

`sphinxext-versionwarning` is a Sphinx extension that shows a customizable warning banner at the top of versioned documentation hosted on Read the Docs. It uses Read the Docs Addons data to compare the version being viewed with the highest active semantic version.

## Installation

```sh
pip install sphinxext-versionwarning
```

To install the current version directly from GitHub:

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

The Read the Docs Addons API must also be enabled for the site. See [installation](docs/installation.md) for the required meta tag and complete setup.

By default, the warning links to the highest active version whose slug can be interpreted as [SemVer](https://semver.org/). Set `versionwarning_stable_as_highest = True` in `conf.py` to prefer Read the Docs' `stable` version instead.

## Documentation

Read the [documentation](docs/index.md) in this repository.
