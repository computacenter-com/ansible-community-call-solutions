from __future__ import annotations

def attendee_list_displayable(attendee_list):
    """ Creates comma-separated string from list, last item is joined with ampersand """
    if not attendee_list:
        return ""
    if len(attendee_list) == 1:
        return attendee_list[0]
    return ", ".join(attendee_list[:-1]) + " & " + attendee_list[-1]

class FilterModule(object):

    def filters(self):
        filters = {
            'attendee_list_displayable': attendee_list_displayable
        }
        return filters
