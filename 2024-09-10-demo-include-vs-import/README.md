# Demo include vs. import statements

Walkthrough for demo.

Why you (mostly) should use `import_*` instead of `include_`!

## 1. Playbooks can be imported

An `import_playbook` is available, no include representation available. But `import_playbook` can't be a task

Add this as a task:

```yaml
    - ansible.builtin.import_playbook: another-playbook.yml
```

Results in syntax error, move back to play-level.

## 2. Title/Name of task shown/not shown

Change from `import_tasks` to `include_tasks`, with *include* a separate task is used and shown.

Also show output of `--list-tasks`

### import

```console
...

TASK [Install webserver] ***************************************************************************************
ok: [localhost] => {
    "msg": "Running task from installation.yml"
}

...
```

### include

```console
...

TASK [Use installation.yml task-file] **************************************************************************
included: /home/timgrt/semaphore/installation.yml for localhost

TASK [Install webserver] ***************************************************************************************
ok: [localhost] => {
    "msg": "Running task from installation.yml"
}

...
```

## 3. start-at-task not working

With import-statements, using `--start-at-task "Configure something"` works, it will skip the installation tasks.  
Using it with include-statements results in an error.

## 4. Syntax-Errors not recognized

Create syntax error in imported/included file, e.g.

```yaml
- name: Install webserver
  ansible.builtin.debug:
  msg: Running task 1 from installation.yml
```

### import

Error is recognized.

### include

Run `ansible-playbook playbook.yml --syntax-check` or `ansible-lint`, no errors are shown!

## 5. Loops

Loops only work with `include_*` statements. Add `loop: "{{ range(0, 2) | list }}"` to task.

## 6. Tags

Tags within *included* task-files are not used.  
Add `tags: configure` to imported task-file `configuration.yml`. Run playbook with `-t configure`

Start with demoing import.

### import

With import, a tag on a single task *inside* the imported file works, it will be excuted.  
A tag on the import-statement itself will run all tasks within the imported file.

List tags with `--list-tags`.

### include

No tasks (except fact gathering) are executed, you have to use this to run all tasks within the included file:

```yaml
- name: Use installation.yml task-file
  ansible.builtin.include_tasks:
    file: configuration.yml
    apply:
        tags: configure
  tags: configure
```

Both *tag* statements are absolutely necessary to run all tasks

## 7. Variable-Files

Using `include_vars` available, no representation for import-statements.

Add this to `playbook.yml`:

```yaml
  tasks:
    - name: Use variables
      ansible.builtin.include_vars: variables.yml"
```

Add this to `configuration.yml`:

```yaml
- name: Show variable content
  ansible.builtin.debug:
    msg: "{{ demo }}"
```

For import-statements, use `vars_files`, this also works for include statements.

## 8. Use files with variable

Add this to `playbook.yml`:

```yaml
    - name: Use distribution-specific task-file
      ansible.builtin.import_tasks: "{{ ansible_distribution }}.yml"
```

This works with *include_tasks*, not with *import_tasks*.

## 9. Handlers

Start demo with include.

Add this to `playbook.yml`:

```yaml
  handlers:
    - name: Restart services
      ansible.builtin.include_tasks: restarts.yml
```

Adjust task in `configuration.yml` to always trigger handler:

```yaml
- name: Configure something else
  ansible.builtin.debug:
    msg: Running task 2 from configuration.yml
  changed_when: true
  notify: Restart services
```

### include

Works as expected, both tasks in the included file are run.

### import

Using *import_tasks* in handler does not work.  
It can be worked around by not notifying the handler itself, but the tasks within the imported file.

```yaml
- name: Configure something else
  ansible.builtin.debug:
    msg: Running task 2 from configuration.yml
  changed_when: true
  notify:
    - Restart Service1
    - Restart Service2
```

## 10. Task options

Options like `become` act differently. Add the following tasks to `installation.yml` (either ensure you can run without having to provide sudo password or run with `-k`):

```yaml
- name: Change user/use become statement
  ansible.builtin.command:
    cmd: whoami
  become: true

- name: Change user/use become statement again
  ansible.builtin.command:
    cmd: whoami
```

Using the `become` at with `include_tasks` does not work, only works with `import_tasks` BUT now all tasks in the imported file run as root!

Run the overall playbook with `-v` to show the output of the command tasks.
