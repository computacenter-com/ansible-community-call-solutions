
# Changes with ansible-core 2.19+

This demo shows changes with newer Ansible (-Core) versions, especially with pre-and post release of 2.19 for example differences in templates and conditionals.

## Demo environment

> This is only necessary if you want to run the playbooks for demo purposes.

Create a demo environment by running the `demo-environment.yml` playbook:

```console
ansible-playbook demo-environment.yml
```

Activate Python VEs in separate terminal windows, e.g.:

```console
source ve-ansible-2.20/bin/activate
```

After the demo, delete the demo environment again:

```console
ansible-playbook demo-environment.yml -e delete=true
```

## Demo walkthrough

The following are the *wrong*/*failing* content snippets, which (mostly) work up to 2.18, but not in 2.19+.

1. Failure message in general

    ```yaml
    - name: Show distribution of managed node with ansible-core {{ ansible_version.full }}
      ansible.builtin.debug:
      msg: "{{ ansible_hostname }}"
    ```

    Fix by indenting `msg` correctly.

    ```yaml
    - name: Show distribution of managed node with ansible-core {{ ansible_version.full }}
      ansible.builtin.debug:
        msg: {{ ansible_hostname }}
    ```

    Fix by adding quotes around the *msg* *value*.

2. Conditionals must have boolean result

    ```yaml
    - name: Output all facts when providing a variable with ansible-core {{ ansible_version.full }}
      ansible.builtin.debug:
        var: ansible_facts
      when: show_all_facts | default(false)    
    ```

    Run with `-e show_all_facts=true`. Fix by adding `| bool` filter expression.