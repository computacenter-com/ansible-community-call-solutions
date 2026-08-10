# Demo - Variable precedence

This contains a playbook, inventory (single host, running against localhost), role and multiple variable definitions to showcase the Ansible variable precedence.

Run the playbook:

```bash
ansible-playbook -i inventories/inventory.ini playbook.yml
```

> [!NOTE]
> **The playbook starts with an interactive variable prompt**, accept the default answer with enter.

The playbook references the role in the `roles` key (this will run first, not because it is defined before the `tasks` section, but because roles are always executed first), but also a `tasks` section (which does `include_role` the role once more).

*Comment tasks or variable definitions and see how the variable value changes according to its precedence.*
