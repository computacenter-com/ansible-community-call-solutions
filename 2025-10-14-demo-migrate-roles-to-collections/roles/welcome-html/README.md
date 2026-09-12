# Ansible role: `welcome-html`

FIXME Add role description here.

<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

Main entry point for the welcome-html role.

This is the main entrypoint for the `welcome-html` role.

It is used to generate the welcome HTML page for the apache server.

The role is used as a demonstration during the Community Call

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description (abstract) |
|----------|------|----------|---------|------------------------|
| `attendee_list` | `list` | No | N/A | A list of usernames shown on the welcome page. |

### `attendee_list`<a id="variable-attendee_list"></a>

[*⇑ Back to ToC ⇑*](#toc)

A list of usernames shown on the welcome page.

- **Type**: `list`
- **Required**: No
- **List Elements**: `str`




<!-- ANSIBLE DOCSMITH MAIN END -->


## Dependencies<a id="dependencies"></a>

See `dependencies` in [`meta/main.yml`](./meta/main.yml).


## Compatibility<a id="compatibility"></a>

See `min_ansible_version` in [`meta/main.yml`](./meta/main.yml).


## Licensing, copyright<a id="licensing-copyright"></a>

<!--REUSE-IgnoreStart-->
Copyright (c) [FIXME YYYY Your Name]

[FIXME Adapt license:
This project is licensed under the GNU General Public License v3.0 or later
(SPDX-License-Identifier: `GPL-3.0-or-later`)].
<!--REUSE-IgnoreEnd-->


## Author information

This project was created and is maintained by [FIXME Your Name].

