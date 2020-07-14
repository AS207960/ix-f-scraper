import json
import csv
import os
import requests
import ASNInfo
import csvWrite
from pprint import pprint
from networktoolkit import vendorlookup
from ipaddress import IPv4Address, IPv6Address, ip_address


def macLookup(asn: int, ixf: str):

    info = dict()

    member = ASNInfo(asn=asn, ixf=ixf)

    for connection in member["connection_list"]:
        for vlan in connection["vlan_list"]:
            for ipVersion, ipData in vlan.items():
                if ipVersion == "vlan_id":
                    pass
                else:
                    print(ipData["address"])
                    try:
                        ip = ip_address(ipData["address"])
                    except ValueError as e:
                        return e

                    if type(ip) is IPv4Address:
                        for mac in ipData["mac_addresses"]:
                            mac_vendor = vendorlookup.lookup_vendor(mac)
                            if mac_vendor is not None:
                                csvWrite(
                                    asn=member["asnum"],
                                    ip=ipData["address"],
                                    mac=mac,
                                    vendor=mac_vendor,
                                )
                                info["v4"] = {
                                    "asn": member["asnum"],
                                    "ip": ipData["address"],
                                    "mac": mac,
                                    "vendor": mac_vendor,
                                }
                            else:
                                csvWrite(
                                    asn=member["asnum"],
                                    ip=ipData["address"],
                                    mac=mac,
                                    vendor="Unknown",
                                )
                                info["v4"] = {
                                    "asn": member["asnum"],
                                    "ip": ipData["address"],
                                    "mac": mac,
                                    "vendor": "Unknown",
                                }
                    elif type(ip) is IPv6Address:
                        for mac in ipData["mac_addresses"]:
                            mac_vendor = vendorlookup.lookup_vendor(mac)
                            if mac_vendor is not None:
                                csvWrite(
                                    asn=member["asnum"],
                                    ip=ipData["address"],
                                    mac=mac,
                                    vendor=mac_vendor,
                                )
                                info["v6"] = {
                                    "asn": member["asnum"],
                                    "ip": ipData["address"],
                                    "mac": mac,
                                    "vendor": mac_vendor,
                                }
                            else:
                                csvWrite(
                                    asn=member["asnum"],
                                    ip=ipData["address"],
                                    mac=mac,
                                    vendor="Unknown",
                                )
                                info["v6"] = {
                                    "asn": member["asnum"],
                                    "ip": ipData["address"],
                                    "mac": mac,
                                    "vendor": "Unknown",
                                }
                    # else:
                    #    raise ValueError()

            return info

            # if mac_vendor is not None:
            #     print(f"{member['asnum']} {ipAddr} {mac} {mac_vendor}")
            # else:
            #     print(f"{member['asnum']} {ipAddr} {mac} Unknown")

    #                for ipDetails in (
    #                    ipData.items() if ipVersion == "ipv4" or ipVersion == "ipv6" else []
    #                ):
    #                    print("ASN IP Details")
    #                    pprint(ipDetails)
    #                    for mac in ipDetails["mac_addresses"]:
    #                        pprint(mac)


#        for peerASN, peerDetails in (
#            ixDetails["peers"].items() if ixDetails["peers"] else []
#        ):
