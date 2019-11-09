import os
import ipinfo

IPINFOIO_ACCESS_TOKEN = os.getenv('IPINFOIO_ACCESS_TOKEN')

cached_location = None


def get_location():
    global cached_location
    if not (cached_location is None):
        return cached_location
    handler = ipinfo.getHandler(IPINFOIO_ACCESS_TOKEN)
    cached_location = handler.getDetails()
    return cached_location