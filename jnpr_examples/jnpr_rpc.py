#!/usr/bin/env python
from jnpr.junos import Device
from lxml import etree
from getpass import getpass

password = getpass()
device = {"host": "vmx1.lasthop.io", "user": "pyclass", "password": password}

a_device = Device(**device)
a_device.open()

import ipdb  # noqa

ipdb.set_trace()
# show version | display xml rpc
# <get-software-information>
xml_out = a_device.rpc.get_software_information()
print(etree.tostring(xml_out, encoding="unicode", pretty_print=True))

# get_lldp_neighbors_information()
xml_out = a_device.rpc.get_lldp_neighbors_information()
print(etree.tostring(xml_out, encoding="unicode", pretty_print=True))
