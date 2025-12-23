#!/usr/bin/python

# Copyright: (c) 2026, Tim Grützmacher <tim.gruetzmacher@computacenter.com>
# The MIT License (see LICENSE or https://opensource.org/license/mit)
from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: useless_facts

short_description: This module returns useless facts by calling an external API.

version_added: "1.0.0"

description: This module returns useless facts for demonstration purposes.
options:
    type:
        description: This is the message to send to the test module.
        required: false
        type: str
    language:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: str
    id:
        description: ID of a specific fact to retrieve.
        required: false
        type: str

author:
    - Tim Grützmacher (@TimGrt)
"""

EXAMPLES = r"""
- name: Get useless fact for today in English
  computacenter.ansible_community.useless_facts:
    type: today

- name: Get random useless fact in German
  computacenter.ansible_community.useless_facts:
    type: random
    language: de

- name: Get specific useless fact by ID
  computacenter.ansible_community.useless_facts:
    id: 9be1bce8fcc1f3e0b96a7e7dea4bb4ed
"""

RETURN = r"""
id:
    description: The API ID of the useless fact.
    type: str
    returned: always
    sample: '9be1bce8fcc1f3e0b96a7e7dea4bb4ed'
fact_language:
    description: The language of the fact.
    type: str
    returned: always
    sample: 'de'
fact_permalink:
    description: The API permalink to the useless fact.
    type: str
    returned: always
    sample: 'https://uselessfacts.jsph.pl/9be1bce8fcc1f3e0b96a7e7dea4bb4ed'
fact_source:
    description: The source of the useless fact.
    type: str
    returned: always
    sample: 'NEON'
fact_source_url:
    description: The full URL to the fact source.
    type: str
    returned: always
    sample: 'http://www.neon.de/artikel/kaufen/produkte/konrad-adenauer-hat-die-sojawurst-erfunden/1477333'
fact_text:
    description: The useless fact text retrieved from the API.
    type: str
    returned: always
    sample: 'Konrad Adenauer hat die Sojawurst erfunden.'
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import Request
import json


def get_useless_fact(type, fact_language, id=None):
    # Build the API call URL based on the input parameters
    url_base = "https://uselessfacts.jsph.pl"
    api_base = "/api/v2"
    api_endpoint = "/facts/"
    language_query_string = "?language=" + fact_language

    # If an ID is provided, get the specific fact, otherwise get by type and language
    if id is not None:
        api_call = Request().open("GET", url_base + api_base + api_endpoint + id).read()
    else:
        api_call =Request().open("GET", url_base + api_base + api_endpoint + type + language_query_string).read()

    # Parse the API response content by decoding the byte string and loading as JSON content
    api_result_content = json.loads(api_call.decode("utf-8"))

    return api_result_content


def run_module():
    module_args = dict(
        type=dict(
            type="str",
            default="random",
            choices=["random", "today"],
            required=False,
        ),
        language=dict(type="str", default="en", choices=["en", "de"], required=False),
        id=dict(type="str", required=False),
    )

    # The result dictionary with all fields returned by the API
    result = dict(
        changed=False,
        fact_text="",
        fact_id="",
        fact_language="",
        fact_permalink="",
        fact_source="",
        fact_source_url="",
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[("id", "type")],
        required_one_of=[
            ("id", "type"),
        ],
    )

    if module.check_mode:
        module.exit_json(**result)

    # Call the function to get the useless fact and provide the input parameters of the module to the function
    fact_content = get_useless_fact(
        module.params.get("type"),
        module.params.get("language"),
        module.params.get("id"),
    )

    # Fill the result dictionary with the API response content from the function call
    result["fact_text"] = fact_content["text"]
    result["id"] = fact_content["id"]
    result["fact_language"] = fact_content["language"]
    result["fact_permalink"] = fact_content["permalink"]
    result["fact_source"] = fact_content["source"]
    result["fact_source_url"] = fact_content["source_url"]

    # In most cases the API returns a new fact each time, only if a specific
    # id is requested, the result is always the same and thus not changed
    if module.params["id"] is not None:
        result["changed"] = False
    else:
        result["changed"] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
