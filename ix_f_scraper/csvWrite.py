import json
import csv
import os
import requests
import ASNInfo
from pprint import pprint
from networktoolkit import vendorlookup
from ipaddress import IPv4Address, IPv6Address, ip_address


def csvWrite(asn: int, ip: str, mac: str, vendor: str):

    ipSanitised = ip_address(address=ip)

    if type(ipSanitised) is IPv4Address or IPv6Address:
        fileEmpty = os.stat("output.csv").st_size == 0
        try:
            with open("output.csv", mode="a") as csvOutput:
                # asn,ip,mac,speed,state,as-macro
                fieldnames = [
                    "asn",
                    "ip",
                    "mac",
                    "vendor",
                    "speed",
                    "state",
                    "as-macro",
                ]
                csvWriter = csv.DictWriter(csvOutput, fieldnames=fieldnames,)

                if fileEmpty:
                    csvWriter.writeheader()  # file doesn't exist yet, write a header

                csvWriter.writerow(
                    {"asn": asn, "ip": ipSanitised, "mac": mac, "vendor": vendor}
                )

        except (
            OSError,
            FileExistsError,
            PermissionError,
            UnicodeError,
            ValueError,
        ) as e:
            raise e


def ipLookup(asn: int, ixf: str):
    return


# Shit

# for connection in member["connection_list"]:
#     print("ASN connection")
#     # pprint(connection)
#     for vlan in connection["vlan_list"]:
#         print("ASN VLAN")
#         # pprint(vlan)
#         # for ipVersion, ipData in vlan.items():
#         for ipVersion, ipData in vlan.items():
#             if ipVersion == "vlan_id":
#                 pass
#             else:
#                 print("ASN Port Info per IP Version")
#                 #                pprint(f"{ipVersion}: {ipData}")
#                 # pprint(ipData)
#                 print(ipData["address"])
#                 for mac in ipData["mac_addresses"]:
#                     mac_vendor = vendorlookup.lookup_vendor(mac)
#                     if mac_vendor is not None:
#                         info = f"{member['asnum']} {mac} {mac_vendor}"
#                         print(info)
#                     else:
#                         info = f"{member['asnum']} {mac} Unknown"
#                         print(info)

#                     return info
#                     # csvWrite(member['asnum'], ipData["address"], mac)

#    else:
#        pprint(data["member_list"])
#        raise ValueError("ASN may be invalid or does not exist in IXF File")
