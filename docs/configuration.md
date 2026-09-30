# Configuration

Set these values in your Sphinx `conf.py` to control the banner.

## Version selection

By default, the extension compares active version slugs from the Read the Docs Addons API that can be interpreted as semantic versions. Slugs such as `latest` and `stable` are excluded from this comparison. Use `versionwarning_messages` to show a custom banner for those slugs.

| Setting | Description | Default |
| --- | --- | --- |
| `versionwarning_stable_as_highest` | Prefer the active Read the Docs `stable` version as the warning target. If it is unavailable, use the highest active semantic version. | `False` |
| `versionwarning_project_version` | Slug of the current documentation version. | `READTHEDOCS_VERSION` environment variable |
| `versionwarning_project_slug` | Read the Docs project slug. | `READTHEDOCS_PROJECT` environment variable |

## Banner customization

| Setting | Description | Default |
| --- | --- | --- |
| `versionwarning_admonition_type` | Banner admonition type: `warning`, `admonition`, `tip`, or `note`. | `'warning'` |
| `versionwarning_banner_title` | Banner title. | `'Warning'` |
| `versionwarning_default_message` | Default banner message. | `'You are not reading the most up to date version of this documentation. {newest} is the newest version.'` |
| `versionwarning_messages` | Mapping of version slugs to custom messages, shown without comparing active versions. | `{}` |
| `versionwarning_message_placeholder` | Text replaced by the version number link in the message. | `'newest'` |
| `versionwarning_banner_html` | HTML template for the banner (shown below). | See below |
| `versionwarning_banner_id_div` | ID of the injected banner `<div>`. | `'version-warning-banner'` |
| `versionwarning_body_selector` | CSS selector for the page container. The banner is inserted as its first child. | `'div.body'` |

The default `versionwarning_banner_html` is:

```html
<div id="{id_div}" class="admonition {admonition_type}">
  <p class="first admonition-title">{banner_title}</p>
  <p class="last">
    {message}
  </p>
</div>
```
