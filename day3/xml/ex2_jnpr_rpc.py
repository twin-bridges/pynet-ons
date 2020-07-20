#!/usr/bin/env python
import os
from getpass import getpass
from jnpr.junos import Device

# For automated testing
password = os.getenv("JNPR_PASSWORD")
if password is None:
    password = getpass("Enter vMX password: ")

device = {"host": "vmx1.lasthop.io", "user": "pyclass", "password": password}
a_device = Device(**device)
a_device.open()

# Retrieve 'show interfaces terse' in XML form
xml_out = a_device.rpc.get_interface_information()
ip_interfaces = xml_out.findall(".//interface-address/ifa-local")

print()
print("-" * 80)
for intf in ip_interfaces:
    address_family = intf.getparent().getparent()
    af_name = address_family.find("./address-family-name").text
    if "inet" in af_name:
        print(f"Address Family: {af_name.strip()}")
        print(f">>> {intf.text.strip()}")
        print()
print("-" * 80)
print()
