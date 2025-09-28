# Migrate roles to collections

This demo shows how to move existing roles (and playbooks) into a collection and consuming the content again.

## Demo environment

Create a demo environment by running the `demo-environment.yml` playbook:

```console
ansible-playbook demo-environment.yml
```

After the demo, delete the demo environment again:

```console
ansible-playbook demo-environment.yml -e delete=true
```

## How-to

> The solution is already achieved (the old `roles` folder is still there, although it is not used anymore)! Remove the `collections` folder and follow the steps below for a new demo.

Follow these steps for demo walkthrough.

1. 
    Create new collection (in a playbook-adjancent folder):

    ```console
    ansible-galaxy collection init computacenter.demo --init-path collections/ansible_collections
    ```

2. 
    Move the role to the collection and adjust the name (as folders and files in collections only support underscores!):

    ```console
    mv roles/welcome-html collections/ansible_collections/computacenter/demo/roles/welcome_html
    ```

3. 
    Create folder for *filter* plugins in the collection:

    ```console
    mkdir collections/ansible_collections/computacenter/demo/plugins/filter
    ```

    Move the *filter* plugin from the role to the Collection:

    ```console
    mv roles/welcome-html/filter_plugins/welcome_filter_plugins.py collections/ansible_collections/computacenter/demo/plugins/filter/
    ```

    Remove the old `filter_plugins` folder:

    ```console
    rmdir collections/ansible_collections/computacenter/demo/roles/welcome_html/filter_plugins
    ```

4. 
    Adjust the used filter plugin in the template of the role to the *Full Qualified Collection Name*:

    ```console
    sed -i 's/attendee_list_displayable/computacenter.demo.attendee_list_displayable/g' collections/ansible_collections/computacenter/demo/roles/welcome_html/templates/welcome.html
    ```

5. 
    Update `playbook.yml` but adjusting the used role to `computacenter.demo.welcome_html`:

    ```yaml
    ---
    - name: Run role to greet all community call attendees
      hosts: managed_nodes
      gather_facts: false
      roles:
        - computacenter.demo.welcome_html
    ```

    Remove the old roles folder:

    ```console
    rmdir roles
    ```

6. 
    **Copy** the playbook to the collection after creating a `playbooks` folder there:

    ```console
    mkdir collections/ansible_collections/computacenter/demo/playbooks
    ```

    ```console
    cp playbook.yml collections/ansible_collections/computacenter/demo/playbooks/welcome.yml
    ```

    > The playbook needs to reference the *full qualified* role name!

    Update the original `playbook.yml` to import the collection playbook:

    ```yaml
    ---
    - ansible.builtin.import_playbook: computacenter.demo.welcome # noqa name[play]
    ```
