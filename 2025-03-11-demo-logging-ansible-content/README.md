# Logging Ansible content

This demo shows how log Ansible runs wit local log files and with ARA.

## How-to

Install ARA:

```console
ansible-playbook prepare-ara.yml
```

Create demo environment:

```console
ansible-playbook create-workshop-environment.yml
```

Run demo playbook and observe local log files or in ARA:

```console
ansible-playbook playbook.yml
```
