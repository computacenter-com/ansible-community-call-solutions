# Demo - Install collections when Galaxy is down

Install collections from `requirements.yml`:

```bash
ansible-galaxy collection install -r requirements.yml
```

Show collections:

```bash
ansible-galaxy collection list
```

Remove collections folder:

```bash
rm -rf collections/
```

Uncomment `source` and `type` key from `requirements.yml` and install again:

```bash
ansible-galaxy collection install -r requirements.yml
```

## Use updated requirements.yml in EE build

The collections source from Git does not matter for EE builds, this will still work.

```bash
ansible-builder build -t demo-ee -v 3
```

Show collections in image:

```bash
podman run -it demo-ee:latest ansible-galaxy collection list
```

Or with Navigator:

```bash
ansible-navigator images -d ansible_collections
```
