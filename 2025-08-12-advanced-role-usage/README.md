# Usage advanced role feature

This demo shows how to use some advanced features with roles, utilizing the `meta` folder.  
Most of the stuff is documented here: [Ansible Docs - Roles](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#role-argument-validation)

## How-to

Install requirements:

```console
ansible-galaxy collection install -r requirements.yml
```

A script is prepared to export the required variables for ACI connection, use the following command:

```console
. export-aci-credentials.sh
```

Ensure the environment variables are exported correctly:

```console
env | grep ACI
```

## Demo commands:

### Show role info

```console
ansible-galaxy role info apic --offline
```

Parameter `offline` is necessary as the role is not in galaxy.ansible.com

For a *online* role (in Galaxy), show the following:

```console
ansible-galaxy role info geerlinguy.nginx
```

### Run only specific tasks from a role

Use this playbook:

```yaml
- name: ACI automation with Ansible for Workshop
  hosts: apic
  gather_facts: false
  tasks:
    - name: Run only tenant creation from APIC role
      ansible.builtin.import_role:
        name: apic
        tasks_from: tenant
```

### Run role multiple times

If role is specified multiple times, it will only run once by default.

The key-value `allow_duplicates: true` is ncessary in `meta/main.yml`.

> Comment some task files in `tasks/main.yml` for faster runtime.
