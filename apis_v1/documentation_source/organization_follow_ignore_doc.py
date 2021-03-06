# apis_v1/documentation_source/organization_follow_ignore_doc.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-


def organization_follow_ignore_doc_template_values(url_root):
    """
    Show documentation about organizationFollowIgnore
    """
    required_query_parameter_list = [
        {
            'name':         'voter_device_id',
            'value':        'string (from cookie)',  # boolean, integer, long, string
            'description':  'An 88 character unique identifier linked to a voter record on the server',
        },
        {
            'name':         'organization_id',
            'value':        'integer',  # boolean, integer, long, string
            'description':  'Internal database unique identifier for organization',
        },
        {
            'name':         'api_key',
            'value':        'string (from post, cookie, or get (in that order))',  # boolean, integer, long, string
            'description':  'The unique key provided to any organization using the WeVoteServer APIs',
        },
    ]
    optional_query_parameter_list = [
    ]

    potential_status_codes_list = [
        {
            'code':         'VALID_VOTER_DEVICE_ID_MISSING',
            'description':  'A valid voter_device_id parameter was not included. Cannot proceed.',
        },
        {
            'code':         'VALID_VOTER_ID_MISSING',
            'description':  'A valid voter_id was not found from voter_device_id. Cannot proceed.',
        },
        {
            'code':         'VALID_ORGANIZATION_ID_MISSING',
            'description':  'A valid organization_id was not found. Cannot proceed.',
        },
        {
            'code':         'ORGANIZATION_NOT_FOUND_ON_CREATE FOLLOW_IGNORE',
            'description':  'An organization with that organization_id was not found. Cannot proceed.',
        },
        {
            'code':         'FOLLOW_IGNORE',
            'description':  'Successfully ignoring this organization',
        },
    ]

    try_now_link_variables_dict = {
        'organization_id': '1',
    }

    api_response = '{\n' \
                   '  "status": string,\n' \
                   '  "success": boolean,\n' \
                   '  "voter_device_id": string (88 characters long),\n' \
                   '  "organization_id": integer,\n' \
                   '}'

    template_values = {
        'api_name': 'organizationFollowIgnore',
        'api_slug': 'organizationFollowIgnore',
        'api_introduction':
            "Call this to save that the voter is ignoring this organization.",
        'try_now_link': 'apis_v1:organizationFollowIgnoreView',
        'try_now_link_variables_dict': try_now_link_variables_dict,
        'url_root': url_root,
        'get_or_post': 'GET',
        'required_query_parameter_list': required_query_parameter_list,
        'optional_query_parameter_list': optional_query_parameter_list,
        'api_response': api_response,
        'api_response_notes':
            "",
        'potential_status_codes_list': potential_status_codes_list,
    }
    return template_values
