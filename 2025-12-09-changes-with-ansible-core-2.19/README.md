
# Changes with ansible-core 2.19+

This demo shows changes with newer Ansible (-Core) versions, especially with pre-and post release of 2.19 for example differences in templates and conditionals.

## Demo environment

> This is only necessary if you want to run the playbooks for demo purposes.

Create a demo environment by running the `demo-environment.yml` playbook:

```console
ansible-playbook demo-environment.yml
```

Activate Python VEs in separate terminal windows:

```console
source ve-ansible-2.20/bin/activate
```

After the demo, delete the demo environment again:

```console
ansible-playbook demo-environment.yml -e delete=true
```


