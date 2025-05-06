# ansible-sign usage

This session shows how to use the ansible-sign utility which is used for signing and verifying Ansible content.

## Prepare demo

Run the playbook `prepare-demo.yml`:

```bash
ansible-playbook prepare-demo.yml
```

A new GPG key-pair was created:

```bash
gpg --list-keys
```

The *ansible-sign* utility was installed:

```bash
ansible-sign --version
```

## Use ansible-sign

Verfiy GPG signature and checksum on the manifest:

```bash
ansible-sign project gpg-verify .
```

> Signature file does not yet exist, sign the project first!

```bash
ansible-sign project gpg-sign .
```

A new hidden folder was created, the file `.ansible-sign/sha256sum.txt` contains checksums for every file in the project folder (if not explicitly excluded in the `MANIFEST.in`)

Verify the project again:

```bash
ansible-sign project gpg-verify .
```

As a test, copy over a playbook from another Community Call session:

```bash
cp ../2025-03-11-demo-logging-ansible-content/playbook.yml .
```

> The checksum validation failed as a new file was added!

Adjust the `MANIFEST.in` file, add the line `include playbook.yml` (or add the file to the first line `include prepare-demo.yml playbook.yml`).  
Re-sign the project:

```bash
ansible-sign project gpg-sign .
```

Now, the validation/verification succeeds.

## Remove GPG keys

Once you are finished, you may remove the GPG key-pair. Remove the secret key first:

```bash
gpg --delete-secret-key Community-Call-Demo
```

> You'll need to confirm the deletion multiple times!

You can check if the secret key was removed with the following command:

```bash
gpg --list-secret-keys
```

Now, remove the public key:

```bash
gpg --delete-key Community-Call-Demo
```

> You'll need to confirm the deletion!

You can check if the public key was removed with the following command:

```bash
gpg --list-keys
```
