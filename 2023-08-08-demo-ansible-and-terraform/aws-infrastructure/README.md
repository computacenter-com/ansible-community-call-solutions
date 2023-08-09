# AWS VM Deployment using Ansible with Terraform modules
This demo provisions virtual machines on AWS using the community.general.terraform module within Ansible. The number of VMs is determined by user input upon playbook execution. The VMs are then configured as web servers, hosting a publicly accessible index.html.

## Requirements
Install terraform:  
```console
ansible-galaxy role install timgrt.terraform
ansible-playbook terraform-install.yml --ask-become-pass
```
Save AWS credentials as environment variables (take caution, as this will appear in your history):  
```console
export AWS_ACCESS_KEY_ID=<access key>
export AWS_SECRET_ACCESS_KEY=<secret key>
```

## Provision and configure
To provision virtual machines on AWS execute terraform_provision.yml playbook:  
```console
ansible-playbook terraform_provision.yml
```
To configure provisioned VMs as webservers, execute deploy_webserver.yml playbook:  
```console
ansible-playbook -i inventory.ml deploy_webserver.yml
```

## Test
Access index.html using http://\<VM IP\>:80