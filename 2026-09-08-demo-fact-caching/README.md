# Demo - Fact caching

This demo shows the usage of fact caching/presistent facts.

## Prepare Demo environment

Create Python VE:

```bash
python3 -m venv community-call-ve
```

Activate VE:

```bash
source community-call-ve/bin/activate
```

Install requirements:

```bash
pip3 install -r requirements.txt
```

```bash
ansible-galaxy collection install -r requirements.yml
```

Create demo instances:

```bash
ansible-playbook demo-environment.yml
```

## Demo Walkthrough

The persistent cache used JSON files by default.

```bash
ansible-playbook fact-cache.yml
```

### Redis backend

Change from JSON file cache to Redis cache, change lines with `fact_caching` and `fact_caching_connection` to:

```ini
fact_caching = community.general.redis
fact_caching_connection = localhost:6379:0
```

Open the [Redis Web UI](http://localhost:8001) to show the gathered facts.

## Clear facts cache

```bash
ansible all -m meta -a clear_facts
```

## Smart gathering

Add following key under defaults sections of `ansible.cfg`:

```ini
gathering = smart
```

Now, facts will be gathered when necessary (facts cache is empty or facts are outdated), otherwise gathering facts tasks is not executed.

## Constructed inventory

Cached facts allow the usage of constructed inventories (with Jinja2 conditionals and expressions).

With given (dynamic) inventory:

```bash
ansible-inventory --graph
```

Together with constructed inventory:

```bash
ansible-inventory -i inventory.yml -i jinja2-constructed-inventory.yml --graph
```

> [!WARNING]
> **Inventories are loaded in alphabetical order!**  
> Ideally you should prefix the inventory files with numbers to ensure the correct order, e.g. `01-inventory.yml` and `02-constructed-inventory.yml`.
