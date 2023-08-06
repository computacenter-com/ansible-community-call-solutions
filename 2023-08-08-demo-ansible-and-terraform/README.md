# Ansible vs./and Terraform

## Prepare demo environment

Install necessary requirements:

```console
ansible-galaxy install -r requirements.yml
```

Install Terraform, you need to provide your sudo password:

```console
ansible-playbook prepare-demo.yml --ask-become-pass
```

## Playbook for infrastructure provisioning

Run the `provisioning.yml` playbook:

```console
ansible-playbook provisioning.yml
```

Terraform will deploy two (systemd-enabled) Docker containers and will add these hosts to an Ansible inventory group `test_group`, as well as define some Ansible inventory variables. Take a look at `resource "ansible_group" ...` or `resource "ansible_host" ...` in the `main.tf` for additional information.

## Playbook for infrastructure configuration

The `inventory.yml` use the Terraform *statefile* as a dynamic inventory source, the playbook `configuration.yml` addresses the `test_group` defined by Terraform.

Take a look on how Ansible sees the inventory:

```console
ansible-inventory -i inventory.yml --list
```

Run the `configuration.yml` playbook:

```console
ansible-playbook provisioning.yml
```

The first webserver is available on Port 8080, the second one on Port 8081.

## Terraform manually

In case you want to run Terraform manually, execute the following steps.

Init Terraform backend:

```console
terraform init
```

Provision infrastructure (here two Docker container):

```console
terraform apply -auto-approve
```

Destroy infrastructure:

```console
terraform destroy -auto-approve
```
