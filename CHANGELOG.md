# Changelog

## 1.1.2 (2018-11-03)

- Load JSON file on all pages properly ([#20](https://github.com/humitos/sphinx-version-warning/pull/20)).

## 1.1.1 (2018-10-31)

- Fix calling `coerce` by `semver.coerce`.

## 1.1.0 (2018-10-31)

- Support semver prefixed with `v`, like `v2.0.5` ([#16](https://github.com/humitos/sphinx-version-warning/pull/16)).

## 1.0.2 (2018-10-22)

- Fix a mistake when releasing.

## 1.0.1 (2018-10-22)

- Fix compatibility between Sphinx 1.7 and Sphinx 1.8.

## 1.0.0 (2018-10-21)

- Remove ability to add the warning banner statically.
- Make the banner more customizable (all configs are included in the generated JSON file and available from JavaScript).
- Rename `versionwarning_default_admonition_type` to `versionwarning_admonition_type`.
- Rename `versionwarning_body_default_selector` to `versionwarning_body_selector`.
- Remove `versionwarning_body_extra_selector`.
- Refactor to avoid potential circular imports.
- Filter Read the Docs versions by `active=True` when retrieving versions.

## 0.2.0 (2018-07-30)

- Use `READTHEDOCS_PROJECT` and `READTHEDOCS_VERSION` environment variables.
- Remove unused `versionwarning_enabled` config.
- Parse `versionwarning_messages` as reStructuredText ([#7](https://github.com/humitos/sphinx-version-warning/pull/7)).

## 0.1.0 (2018-07-29)

- Make banner more configurable with `api_url`, `banner_html`, `banner_id_div`, `body_default_selector`, and `body_extra_selector` ([#6](https://github.com/humitos/sphinx-version-warning/pull/6)).
- Add compatibility with Sphinx 1.7.x.

## 0.0.1 (2018-07-27)

- Initial release.
