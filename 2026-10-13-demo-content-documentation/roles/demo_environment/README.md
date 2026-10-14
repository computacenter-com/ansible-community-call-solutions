# demo_environment role<a id="toc"></a>

Create and manage a set of Podman containers for an Ansible demo environment.

<!-- ANSIBLE DOCSMITH TOC-FULL START -->
- [demo\_environment role](#demo_environment-role)
  - [Requirements](#requirements)
  - [Role variables](#role-variables)
    - [`managed_nodes_state`](#managed_nodes_state)
    - [`managed_nodes_stop_signal`](#managed_nodes_stop_signal)
    - [`container_labels_dict`](#container_labels_dict)
    - [`managed_nodes_list`](#managed_nodes_list)
      - [`managed_nodes_list['name']`](#managed_nodes_listname)
      - [`managed_nodes_list['hostname']`](#managed_nodes_listhostname)
      - [`managed_nodes_list['image']`](#managed_nodes_listimage)
    - [`managed_nodes_domain`](#managed_nodes_domain)
    - [`container_registry_username`](#container_registry_username)
    - [`container_registry_password`](#container_registry_password)
  - [Example Playbook](#example-playbook)
  - [Authors](#authors)
<!-- ANSIBLE DOCSMITH TOC-FULL END -->

## Requirements<a id="requirements"></a>

The `podman` Container runtime must be available, as well as the `containers.podman` Ansible collection.

```bash
ansible-galaxy collection install containers.podman
```

<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable                        | Type   | Required | Default            | Description (abstract)                                                                                                |
| ------------------------------- | ------ | -------- | ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `managed_nodes_state`           | `str`  | No       | `"started"`        | State of the managed nodes, either started, stopped or deleted                                                        |
| `managed_nodes_stop_signal`     | `int`  | No       | `15`               | Stop signal to use for the managed nodes, requires a numeric value, for example: SIGQUIT - 3 SIGKILL - 9 SIGTERM - 15 |
| `container_labels_dict`         | `dict` | No       | `{'role': 'demo'}` | Labels to apply to the containers, must be provided as key-value pairs                                                |
| `managed_nodes_list`            | `list` | Yes      | N/A                | List of managed nodes for the demo environment                                                                        |
| `managed_nodes_domain`          | `str`  | No       | N/A                | Domain to append to the hostname of the managed nodes, if not provided the hostname will be used as is                |
| `container_registry_username`   | `str`  | No       | N/A                | Username for the container registry, if authentication is required                                                    |
| `container_registry_password` 🔒 | `str`  | No       | N/A                | Password for the container registry, if authentication is required                                                    |

### `managed_nodes_state`<a id="variable-managed_nodes_state"></a>

[*⇑ Back to ToC ⇑*](#toc)

State of the managed nodes, either started, stopped or deleted

- **Type**: `str`
- **Required**: No
- **Default**: `"started"`
- **Choices**: `started`, `stopped`, `absent`

### `managed_nodes_stop_signal`<a id="variable-managed_nodes_stop_signal"></a>

[*⇑ Back to ToC ⇑*](#toc)

Stop signal to use for the managed nodes, requires a numeric value, for example:
SIGQUIT - 3
SIGKILL - 9
SIGTERM - 15

- **Type**: `int`
- **Required**: No
- **Default**: `15`

### `container_labels_dict`<a id="variable-container_labels_dict"></a>

[*⇑ Back to ToC ⇑*](#toc)

Labels to apply to the containers, must be provided as key-value pairs

- **Type**: `dict`
- **Required**: No
- **Default**: `{'role': 'demo'}`

### `managed_nodes_list`<a id="variable-managed_nodes_list"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of managed nodes for the demo environment

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `dict`

#### `managed_nodes_list['name']`<a id="variable-managed_nodes_list-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Name of the managed node

- **Type**: `str`
- **Required**: No

#### `managed_nodes_list['hostname']`<a id="variable-managed_nodes_list-sub-hostname"></a>

[*⇑ Back to ToC ⇑*](#toc)

Hostname of the managed node

- **Type**: `str`
- **Required**: No

#### `managed_nodes_list['image']`<a id="variable-managed_nodes_list-sub-image"></a>

[*⇑ Back to ToC ⇑*](#toc)

Podman image to use for the managed node

- **Type**: `str`
- **Required**: Yes

### `managed_nodes_domain`<a id="variable-managed_nodes_domain"></a>

[*⇑ Back to ToC ⇑*](#toc)

Domain to append to the hostname of the managed nodes, if not provided the hostname will be used as is

- **Type**: `str`
- **Required**: No

### `container_registry_username`<a id="variable-container_registry_username"></a>

[*⇑ Back to ToC ⇑*](#toc)

Username for the container registry, if authentication is required

- **Type**: `str`
- **Required**: No

### `container_registry_password`<a id="variable-container_registry_password"></a>

[*⇑ Back to ToC ⇑*](#toc)

Password for the container registry, if authentication is required

- **Type**: `str`
- **Required**: No
- **Sensitive**: Yes (`no_log`, values are masked in logs)

<!-- ANSIBLE DOCSMITH MAIN END -->

## Example Playbook<a id="example-playbook"></a>

Use the role in a playbook like this (after running plays/roles from dependencies section):

```yaml
- name: Create demo environment
  hosts: localhost
  gather_facts: false
  roles:
    - demo_environment
```

## Authors<a id="authors"></a>

Tim Grützmacher - <tim.gruetzmacher@computacenter.com>

Readme mostly created by [ansible-docsmith](https://github.com/foundata/ansible-docsmith).
