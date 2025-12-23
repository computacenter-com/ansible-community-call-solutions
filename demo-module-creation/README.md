# Module creation

This demo shows the creation of a custom Ansible module. The Module will target an API to get some [useless facts](https://uselessfacts.jsph.pl/).

The API provides a couple of endpoints:

* `/api/v2/facts/random` - gets a *random* fact every time
* `/api/v2/facts/today` - gets a new fact daily
* `/api/v2/facts/<id>` - returns a fact defined by a permalink/id

The language of the fact can be chose by appending `?language=en` or `?language=de`.

```console
curl -s https://uselessfacts.jsph.pl/api/v2/facts/random | python -m json.tool
```

Example output:

```json
{
   "id" : "8538ccb6853eb994e971ac1183ce49db",
   "language" : "de",
   "permalink" : "https://uselessfacts.jsph.pl/api/v2/facts/8538ccb6853eb994e971ac1183ce49db",
   "source" : "NEON",
   "source_url" : "http://www.neon.de/artikel/kaufen/produkte/die-meisten-arbeitsunfaelle-passieren-montags/1137681",
   "text" : "Die meisten Arbeitsunfälle passieren montags"
}
```

## What should be achieved

New module created which **should not use any external libaries** (should work with `ansible-core`, not additional Python packages should be necessary on the controller). The new module can (at least) be configured to target the `random` or `today` **fact type** and the **language** can be chosen.

```yaml
- name: Test useless_facts module
  computacenter.ansible_community.useless_facts:
    fact_type: random
    language: de
  register: output

- name: Output module result
  ansible.builtin.debug:
    msg: "{{ output }}"
```

## Making API call

The module will use the [requests library](https://requests.readthedocs.io/en/latest/)

## How to create the custom module

1. Create collection:

    ```console
    ansible-galaxy collection init computacenter.ansible_community --init-path collections/ansible_collections
    ```

2. Create file `collections/ansible_collections/computacenter/ansible_community/plugins/modules/useless_facts.py` for module content.

3. Copy module template from [Ansible documentation](https://docs.ansible.com/projects/ansible/latest/dev_guide/developing_modules_general.html#creating-a-module-in-a-collection)

4. Consult documentation

    Ansible has already loads of content/utils for interacting with APIs. Take a look at the [module_utils code in the ansible/ansible repository](https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/urls.py) and the `Request` class.

    The original/derived Python library [urllib documentation](https://docs.python.org/3/library/urllib.request.html#) has additional information.

5. Create an *arguments* file, e.g. `module_args.json` for faster development iteration, this avoids going through Ansible.

    ```json
    {
      "ANSIBLE_MODULE_ARGS": {
          "fact_type": "today",
          "language": "de"
      }
    }
    ```

    Now, test the module:

    ```console
    python3 collections/ansible_collections/computacenter/ansible_community/plugins/modules/useless_facts.py module_args.json
    ```
