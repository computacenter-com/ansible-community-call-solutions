from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleError 
from ansible.module_utils.common.text.converters import to_native, to_text 

import types

try:
    import netaddr 
except ImportError as e:
    raise AnsibleError('Missing dependency! - %s' % to_native(e))


def sort_ip(unsorted_ip_list): 
# Function sorts a given list of IP addresses

    if not isinstance(unsorted_ip_list, list): 
        raise AnsibleError("Filter needs list input, got '%s'" % type(unsorted_ip_list))
    else:
        sorted_ip_list = sorted(unsorted_ip_list, key=netaddr.IPAddress) 

    return sorted_ip_list 

def add_stage_as_domain(input_list, identifier):

    if not isinstance(input_list, list): 
        raise AnsibleError("Filter needs list input, got '%s'" % type(input_list))
    else:
        output_list = map(lambda orig_item: orig_item + '.' + identifier, input_list)
    
    return output_list

def sort_hosts(input_list):

    if not isinstance(input_list, list): 
        raise AnsibleError("Filter needs list input, got '%s'" % type(input_list))
    else:
        output_list = sorted(input_list)
    
    return output_list

class FilterModule(object): 

    def filters(self):
        return {
            # Sorting list of IP Addresses
            'sort_ip': sort_ip,
            'add_stage_as_domain': add_stage_as_domain,
            'sort_hosts': sort_hosts
        }