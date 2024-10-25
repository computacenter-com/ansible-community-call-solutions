# Ansible Policy-as-Code demo

The content in this folder can be used to demo the *Ansible Policy-as-Code* [prototype implementation](https://github.com/ansible/ansible-policy) (Q4 2024), expect frequent changes to the project.

## How-to

After cloning the project, change into the correct folder:

```console
cd 2024-11-08-demo-policy-as-code
```

Prepare your control node for the demo:

```console
ansible-playbook prepare-demo.yml
```

This will install *OpenPolicy* Agent and *ansible-policy*. Activate the Python VE:

```console
source demo-ve/bin/activate
```

Change into the demo folder:

```console
cd aces-demo
```

Run *ansible-policy*:

```console
ansible-policy -p . --policy-dir policies
```
