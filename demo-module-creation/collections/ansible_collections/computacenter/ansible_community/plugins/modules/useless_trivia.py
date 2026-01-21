#!/usr/bin/python

# Copyright: (c) 2026, Tim Grützmacher <tim.gruetzmacher@computacenter.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

DOCUMENTATION = r"""
---
module: useless_trivia

short_description: This module returns useless trivia by calling an external API.

version_added: "1.0.0"

description: This module returns useless trivia for demonstration purposes.
options:
    type:
        description: Gets random trivia or the trivia for today, both will always result in changed state.
        required: false
        type: str
        choices:
            - random
            - today
        default: random
    language:
        description: The language of the trivia fact.
        required: false
        type: str
        choices:
            - en
            - de
        default: en
    id:
        description: ID of a specific fact to retrieve. This will always result in unchanged state.
        required: false
        type: str

author:
    - Tim Grützmacher (@TimGrt)
"""

EXAMPLES = r"""
- name: Get useless trivia for today in English
  computacenter.ansible_community.useless_trivia:
    type: today

- name: Get random useless trivia in German
  computacenter.ansible_community.useless_trivia:
    type: random
    language: de

- name: Get specific useless trivia by ID
  computacenter.ansible_community.useless_trivia:
    id: 9be1bce8fcc1f3e0b96a7e7dea4bb4ed
"""

RETURN = r"""
id:
    description: The API ID of the useless fact.
    type: str
    returned: always
    sample: '9be1bce8fcc1f3e0b96a7e7dea4bb4ed'
trivia_language:
    description: The language of the fact.
    type: str
    returned: always
    sample: 'de'
trivia_permalink:
    description: The API permalink to the useless fact.
    type: str
    returned: always
    sample: 'https://uselessfacts.jsph.pl/9be1bce8fcc1f3e0b96a7e7dea4bb4ed'
trivia_source:
    description: The source of the useless fact.
    type: str
    returned: always
    sample: 'NEON'
trivia_source_url:
    description: The full URL to the fact source.
    type: str
    returned: always
    sample: 'http://www.neon.de/artikel/kaufen/produkte/konrad-adenauer-hat-die-sojawurst-erfunden/1477333'
trivia_text:
    description: The useless fact text retrieved from the API.
    type: str
    returned: always
    sample: 'Konrad Adenauer hat die Sojawurst erfunden.'
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
import json


def build_api_url(api_endpoint, trivia_language, id=None):
    api_base_url = "https://uselessfacts.jsph.pl/api/v2/facts"
    # If an ID is provided, get the specific trivia, otherwise get by type and language
    if id is not None:
        return f"{api_base_url}/{id}"
    else:
        return f"{api_base_url}/{api_endpoint}?language={trivia_language}"


def run_module():
    module_args = dict(
        type=dict(
            type="str",
            default="random",
            choices=["random", "today"],
            required=False,
        ),
        language=dict(type="str", default="en", choices=[
                      "en", "de"], required=False),
        id=dict(type="str", required=False),
    )

    # The result dictionary with all fields returned by the API
    result = dict(
        changed=False,
        trivia_text="",
        trivia_id="",
        trivia_language="",
        trivia_permalink="",
        trivia_source="",
        trivia_source_url="",
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        mutually_exclusive=[("id", "type"), ("id", "language")],
        required_one_of=[
            ("id", "type"),
        ],
    )

    if module.check_mode:
        module.exit_json(**result)

    # Build the API URL based on module parameters
    api_url = build_api_url(
        module.params["type"], module.params["language"], module.params["id"])

    # Call the external API to get the trivia fact
    resp, info = fetch_url(module, api_url)

    # Parse the response and handle errors
    body = resp.read()
    if info["status"] >= 400:
        body = info["body"]
        # print(info)
        module.fail_json(
            msg=f"Error fetching trivia from API: {info['url']}", status=info['status'], body=body.strip())

    # Parse the API response content by decoding the byte string and loading as JSON content
    api_result_content = json.loads(body.decode("utf-8"))

    # Fill the result dictionary with the API response content from the function call
    result["trivia_text"] = api_result_content["text"]
    result["id"] = api_result_content["id"]
    result["trivia_language"] = api_result_content["language"]
    result["trivia_permalink"] = api_result_content["permalink"]
    result["trivia_source"] = api_result_content["source"]
    result["trivia_source_url"] = api_result_content["source_url"]

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
