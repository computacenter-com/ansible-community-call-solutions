# Demo - Content documentation

Using and executing Ansible content requires a couple of how-to steps. At least, you should document how to run the playbook, but also which requiresments are necessary (Python packages, Collections, ...), credential handling (Vault password, ...), which roles or playbooks are there, who wrote or is responsible for the content and much more.

## ansible-docsmith

Install utility:

```bash
pipx install ansible-docsmith
```

## VScode KI Chat

Use the following instructions for the AI assistant:

```text
Create a Readme with usage instructions, requirements and variables for the Ansible role demo_environment
```

## Playbook Grapher

Install Graphiz:

```bash
sudo apt-get install graphviz
```

Install Playbook Grapher:

```bash
pipx install ansible-playbook-grapher
```

Create Mermaid diagram of playbook:

```bash
ansible-playbook-grapher --include-role-tasks --renderer mermaid-flowchart demo_environment_playbook.yml
```

## Demo environment playbook

Run playbook to deploy demo instances:

```bash
ansible-playbook demo_environment_playbook.yml
```

Delete demo instances:

```bash
demo_environment_playbook.yml -e managed_nodes_state=absent
```
