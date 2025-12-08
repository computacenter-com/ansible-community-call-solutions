
# Changes with ansible-core 2.19+

This demo shows changes with newer Ansible (-Core) versions, especially with pre-and post release of 2.19 for example differences in templates and conditionals.

> The `playbook.yml` already contains all fixes to work with old and new ansible-core versions. For a new demo, copy the snippets from the README.md file.

Note, running the playbook *as is* will fail (as expected!) during the assertion in task 3 and file check in task 5. Comment these tasks **or** change comparions in line 18 to `!=` and comparison in line 33 to `is not false`

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

### Failure message in general

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

### Conditionals must have boolean result

```yaml
- name: Output all facts when providing a variable with ansible-core {{ ansible_version.full }}
  ansible.builtin.debug:
    var: ansible_facts
  when: show_all_facts | default(false)    
```

Run with `-e show_all_facts=true`. Fix by adding `| bool` filter expression.

### Expression syntax error

Previous Ansible releases could mask some expression syntax errors as a truthy result.

```yaml
    - name: Ensure inventory hostname and managed node hostname match with ansible-core {{ ansible_version.full }}
      ansible.builtin.assert:
        that:
          - ansible_hostname == inventory_hostname,
        success_msg: "{{ inventory_hostname }} matches {{ ansible_hostname }}"
        fail_msg: "{{ inventory_hostname }} does not match {{ ansible_hostname }}!"
        quiet: fals
```

Fix boolean value in `quiet` key, afterwards, remove *comma* from assertion.

### Conditional is unintentional truthy

The last part of this conditional is erroneously quoted. The quoted part becomes the expression result (evaluated as truthy), so the expression can never be `False`.

```yaml
    - name: Validate hostname with ansible-core {{ ansible_version.full }}
      ansible.builtin.assert:
        that:
          - ansible_hostname is defined and ansible_hostname | length > 0 and 'ansible_hostname == demo-node-instance1'
        quiet: true
```

Fix by changing last expression to `ansible_hostname == 'demo-node-instance1'`.

### Missing attribute

This task incorrectly references an undefined exists attribute from a stat result in a conditional. The undefined value was not detected in previous versions because it is passed to the false Jinja test plugin, which silently ignores undefined values. As a result, this conditional could never be True in earlier versions of ansible-core, and there was no indication that the failed_when expression was invalid.

```yaml
    - name: Check for existence file on managed node with ansible-core {{ ansible_version.full }}
      ansible.builtin.stat:
        path: /etc/containers/regsitries.conf
      register: result
      failed_when: result.exists is false
```

Show file on host without Ansible:

```console
podman exec -it instance1 ls -l /etc/containers/registries.conf
```

Fix by updating to `failed_when: result.stat.exists is false`.

### Range filter - Intentional list conversion

```yaml
    - name: Get content of /etc/filesystems with ansible-core {{ ansible_version.full }}
      ansible.builtin.command:
        cmd: cat /etc/filesystems
      changed_when: false
      register: filesystems_output

    - name: Line by line output of first 7 lines from /etc/filesystems with ansible-core {{ ansible_version.full }}
      ansible.builtin.debug:
        msg: "{{ filesystems_output['stdout_lines'][item] }}"
      loop: "{{ range(0, 7) }}"
```

Fix by adding `| list` filter expression after `range` filter.

### Unintentional string conversion

Erroneously pass a list to the `replace` filter, which operates only on strings. The filter **silently converts the list input to a string**. Due to some string results previously parsing as lists, this mistake often went undetected in earlier versions.

```yaml
    - name: Loop with string manipulation with ansible-core {{ ansible_version.full }}
      ansible.builtin.debug:
        msg: "{{ item }}"
      loop: "{{ device_list | replace('test', 'prod') }}"
      vars:
        device_list:
          - test1
          - test2
          - test3
```

Fix by changing to *map* filter: `device_list | map(replace', 'test', 'prod')`

### Unintentional None result

If a template evaluated to `None`, it was implicitly converted to an **empty string** in previous versions of ansible-core. This can now result in the template evaluating to the value `None`.

```yaml
    - name: Output host report
      ansible.builtin.debug:
        msg: "{{ report_content }}"
      vars:
        report_content: "{{ lookup('template', 'template.j2') }}"
      when: report_content | length > 0
```

Run with `-e report=true` to fulfill condition in template, fix by changing to `when: report_content is not none and report_content | length > 0`.
