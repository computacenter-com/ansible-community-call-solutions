# Demo - Secret masking and other new features

Prepare demo environment:

```bash
ansible-playbook demo-environment.yml
```

Install requirements:

```bash
ansible-galaxy collection install -r requirements.yml
```

Create [account in Demo Netbox](https://demo.netbox.dev/plugins/demo/login/).

Activate Python VE depending on required Ansible version:

```bash
source ve-ansible-2.22/bin/activate
```

```bash
source ve-ansible-2.20/bin/activate
```

Run playbooks, depending on used Ansible version.

## Additional information

[Netbox Token Documentation](https://netboxlabs.com/docs/netbox/models/users/token/)
