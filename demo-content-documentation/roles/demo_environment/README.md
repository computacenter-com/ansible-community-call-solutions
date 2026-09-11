# demo_environment role

Ansible role to create a number of Podman demo instances.

<!-- ANSIBLE DOCSMITH TOC-FULL START -->
<!-- ANSIBLE DOCSMITH TOC-FULL END -->

## Requirements

The `podman` Container runtime must be available, as well as the `containers.podman` Ansible collection.

<!-- ANSIBLE DOCSMITH MAIN START -->
<!-- ANSIBLE DOCSMITH MAIN END -->

## Example Playbook

Use the role in a playbook like this (after running plays/roles from dependencies section):

```yaml
- name: Create demo environment
  hosts: localhost
  gather_facts: false
  roles:
    - role: demo_environment
```

## Authors

Tim Grützmacher - <tim.gruetzmacher@computacenter.com>
