import json
import csv
import os
import requests
from pprint import pprint
from networktoolkit import vendorlookup
from ipaddress import IPv4Address, IPv6Address, ip_address

# asn,ip,mac,speed,state,as-macro


def ASNInfo(asn: int, ixf: str):

    try:
        request = requests.get(ixf)
        request.raise_for_status()
    except (
        requests.ConnectionError,
        requests.RequestException,
        requests.HTTPError,
        requests.Timeout,
        requests.TooManyRedirects,
    ) as e:
        raise e

    data = request.json()

    for member in data["member_list"]:
        if member["asnum"] != asn:
            continue
        else:
            return member

    raise ValueError("ASN does not exist in provided IX-F file")
