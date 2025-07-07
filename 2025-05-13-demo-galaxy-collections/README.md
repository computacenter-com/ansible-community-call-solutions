# Usage of roles from Galaxy collections

This demo shows how to use roles from Galaxy collections, in this example a role to automate the AAP with the `infra.controller_configuration` collection.

## How-to

Install requirements:

```console
ansible-galaxy collection install -r requirements.yml
```

Get a token for Automation Hub and add it to the `ansible.cfg`.

Now, run the playbook:

```console
ansible-playbook export-content.yml
```
