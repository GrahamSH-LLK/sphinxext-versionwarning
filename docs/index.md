# sphinx-version-warning

`sphinxext-versionwarning` is a Sphinx extension that shows a customizable warning banner at the top of versioned documentation hosted on Read the Docs. By default, it compares the version being viewed with the highest active version whose slug can be interpreted as [SemVer](https://semver.org/).

## Why use this extension?

Read the Docs [provides a version warning](https://docs.readthedocs.io/page/versions.html#version-warning). This extension lets you customize the banner's message, style, and position. The default settings behave similarly to the built-in warning.

## How it works

When a page is visited, the extension listens for version information from the [Read the Docs Addons API](https://docs.readthedocs.com/platform/stable/addons.html#custom-event-integration). It loads the banner configuration generated during the Sphinx build and compares the current version against active versions. If the current semantic version is older than the highest active semantic version, it inserts a warning at the top of the configured page container.

Version selection can prefer Read the Docs' `stable` version. Custom messages can replace version comparison for specific slugs.

## Contents

- [Installation](installation.md)
- [Configuration](configuration.md)
- [Who is using it?](who-is-using-it.md)
- [Get involved](get-involved.md)
- [Releasing](releasing.md)
- [Changelog](../CHANGELOG.md)
