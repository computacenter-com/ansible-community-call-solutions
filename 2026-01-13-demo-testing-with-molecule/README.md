# Testing with Molecule

This demo shows the testing with Molecule, either in a *classic* role structure, or in a *collection* structure.

## Demo environment

> This is only necessary if you want to run the playbooks for demo purposes.

Create a Python VE to install Molecule:

```console
python3 -m venv ve-molecule
```

Activate Python VE:

```console
source ve-molecule/bin/activate
```

Install ansible-core 2.16.14 (as we are automating against RHEL8) and Molecule.

```console
pip3 install ansible-core==2.16.14
```

Install Molecule and the Molecule-Podman-Plugin:

```console
pip3 install molecule molecule-plugins[podman]
```

## Demo walkthrough

Change into `welcome` role directory:

```console
cd roles/welcome
```

Run Molecule here.

```console
molecule test
```

Change into collection root directory:

```console
cd collections/ansible_collections/cc_ansible_community/demo
```

Run Molecule here.

```console
molecule test
```
