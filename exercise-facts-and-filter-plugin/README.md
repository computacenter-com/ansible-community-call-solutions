# Custom facts and custom plugins

> **This respository contains a sample solution!**

The following exercises will cover extending Ansible Core functionality with self-developed custom facts and plugins. You will write some Python code, don't worry, we will guide you through the *complicated* stuff.

**Good luck!**

## Task 1

Add a *static* custom fact for localhost, which should identify your host as part of the `development` stage.

Running the playbook should result in this output:

```bash
TASK [Output host identifier from custom fact] *********************************************************************
ok: [localhost] => {
    "msg": {
        "identifier": {
            "environment": {
                "stage": "development"
            }
        }
    }
}
```

Take a look at the [Ansible Best Practice Guide](https://timgrt.github.io/Ansible-Best-Practices/development/extending/#static-facts) on how to create a custom static fact.

> Note: The file-extension must be `.fact`! 

## Task 2

The `playbook.yml` contains a list of hostnames, you need to add the domain to every hostname. The domain should be the value of the *stage* fact from the previous task. For example, the host `node1` in the list should be adjusted to `node1.development`.  
This must be achieved with a *custom filter plugin*.

Create a new collection `computacenter.utils` **in your projects folder**, the [Ansible Best Practice Guide](https://timgrt.github.io/Ansible-Best-Practices/development/extending/#store-custom-content) is helpful here, too.

Create the correct folder for the plugin type and create the Python file containing the code for your filter (copy the example filter from the Best Practice Guide as a starting point).

## Task 3

The new filter should be called `add_stage_as_domain`, add a new definition which expects a list of strings (e.g. `input_list`, this gets *the hosts* later) as the first parameter and another string variable as the second parameter (e.g. `identifier` or `domain`, this gets *the domain* later).  

<p>
<details>
<summary><b>Help wanted?</b></summary>
 
This is the defintion start:

```python
def add_stage_as_domain(input_list, identifier):
```

</details>
</p>

The definition should return another list (e.g. `output_list`), with string of the second paramater appended to every list item. The logic to achieve this is the following, include it in your Python code:

```python
map(lambda orig_item: orig_item + '.' + identifier, input_list)
```

You may need to adjust the variables, if you used other names.

Running the playbook should result in the following output:

```bash
$ ansible-playbook -i inventory.ini playbook.yml 

PLAY [Community Call Dojo - Custom facts and custom filter plugin] *************************************************

TASK [Gathering Facts] *********************************************************************************************
ok: [localhost]

TASK [Output host identifier from custom fact] *********************************************************************
ok: [localhost] => {
    "msg": {
        "identifier": {
            "environment": {
                "stage": "development"
            }
        }
    }
}

TASK [Add with filter plugin] **************************************************************************************
ok: [localhost] => {
    "msg": [
        "node1.development",
        "node4.development",
        "node3.development",
        "node2.development"
    ]
}

PLAY RECAP *********************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

> Filter plugin not found? Remember to use FQCN not only for your modules...

## Task 4

As you can see, the hosts are not sorted correctly. Can you implement another filter plugin called `sort_hosts` which brings them in the correct order?

Use the example filter which sorts IP addresses as a reference, the Python builtin `sorted` function can be used, it only needs the unsorted list as a parameter.

In your playbook, chain both filter plugins together, like this:

```yaml
- name: Sort hosts with custom filter plugin
      ansible.builtin.debug:
        msg: "{{ host_list | filter1 | filter2 }}"
```

The result should look like this:

```bash
TASK [Sort host with custom filter plugin] *************************************
ok: [localhost] => {
    "msg": [
        "node1.development",
        "node2.development",
        "node3.development",
        "node4.development"
    ]
}
```