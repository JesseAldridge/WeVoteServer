# geoip/controllers.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-
import json

from django.http import HttpResponse
# requires an installation of the C library at https://github.com/maxmind/geoip-api-c
from django.contrib.gis.geoip import GeoIP

import wevote_functions.admin

logger = wevote_functions.admin.get_logger(__name__)


def voter_location_retrieve_from_ip_for_api(ip_address):
    """
    Used by the api
    :param ip_address:
    :return:
    """
    g = GeoIP()
    location = g.city(ip_address)
    if location is None:
        return HttpResponse('no matching location for this IP address', status=400)
    response_content = {
        'success': True,
        'voter_location': '{0[city]}, {0[region]} {0[postal_code]}'.format(location)
    }

    return HttpResponse(json.dumps(response_content), content_type='application/json')
