# Module creation

This demo shows the creation of a custom Ansible module. The Module will target an API to get some [useless facts](https://uselessfacts.jsph.pl/).

The API provides a couple of endpoints:

* `/api/v2/facts/random` - gets a *random* fact every time
* `/api/v2/facts/today` - gets a new fact daily
* `/api/v2/facts/<id>` - returns a fact defined by a permalink/id

The language of the fact can be chose by appending `?language=en` or `?language=de`.

```console
curl -s https://uselessfacts.jsph.pl/api/v2/facts/random | python3 -m json.tool
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

> [!WARNING]
> ***Facts* have a special meaning in Ansible!**  
> The newly module should **NOT** be called `something_facts` as, by [convention]([trivia_language](https://docs.ansible.com/projects/ansible/latest/dev_guide/developing_modules_general.html#creating-an-info-or-a-facts-module)), `*_facts` modules **MUST** return in the ansible_facts field of the result dictionary so other modules can access them.  

✅ **The module will be called `useless_trivia`!**

## What should be achieved

New module created which **should not use any external libaries** (should work with `ansible-core`, not additional Python packages should be necessary on the controller). The new module can (at least) be configured to target the `random` or `today` **mode** and chose the **language**.

```yaml
- name: Test useless_trivia module
  computacenter.ansible_community.useless_trivia:
    mode: random
    language: de
  register: output

- name: Output module result
  ansible.builtin.debug:
    msg: "{{ output }}"
```

## Prepare development environment

You just need `ansible-core` installed to test and develop the module.  
Create a *Python Virtual Environment* to ensure not other dependencies are used/present:

```console
python3 -m venv ~/ve-module-dev
```

Activate the VE:

```console
source ~/ve-module-dev/bin/activate
```

## How to create the custom module

1. Create collection:

    ```console
    ansible-galaxy collection init computacenter.ansible_community --init-path collections/ansible_collections
    ```

2. Create file `collections/ansible_collections/computacenter/ansible_community/plugins/modules/useless_trivia.py` for module content.

3. Copy module template from [Ansible documentation](https://docs.ansible.com/projects/ansible/latest/dev_guide/developing_modules_general.html#creating-a-module-in-a-collection)

4. Consult documentation

    Ansible has already loads of content/utils for interacting with APIs. Take a look at the [module_utils code in the ansible/ansible repository](https://github.com/ansible/ansible/blob/devel/lib/ansible/module_utils/urls.py) and the [`Request` class](https://github.com/ansible/ansible/blob/6b5301eba7ce385056af747f309c11b5cbf79095/lib/ansible/module_utils/urls.py#L708).

    The original/derived Python library [urllib documentation](https://docs.python.org/3/library/urllib.request.html#) has additional information.

### Test and develop

To use the `print()` statement during development, you can avoid going through Ansible by [creating an *arguments* file](https://docs.ansible.com/projects/ansible/latest/dev_guide/developing_modules_general.html#verifying-your-module-code-locally), e.g. `module_args.json`:

```json
{
  "ANSIBLE_MODULE_ARGS": {
      "mode": "today",
      "language": "de"
  }
}
```

Now, test the module:

```console
python3 collections/ansible_collections/computacenter/ansible_community/plugins/modules/useless_trivia.py module_args.json
```

#### Sanity tests

Sanity tests are made up of scripts and tools used to perform static code analysis. The primary purpose of these tests is to enforce Ansible coding standards and requirements.

Run all sanity tests (run twice as loads of stuff is installed during first run):

```console
ansible-test sanity
```

Run `pep8` sanity test:

```console
ansible-test sanity --test pep8
```

Install `autopep8` to check **and enforce** the style guide:

```console
pip3 install autopep8
```

Run tool against module code, first without parameter to only output changes, then with `--in-place` to enforce on actual code:

```console
autopep8 plugins/modules/useless_trivia.py --in-place
```

Run `validate-modules` sanity test:

```console
ansible-test sanity --test validate-modules
```
