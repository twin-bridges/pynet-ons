from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

vmx2 = {
    "host": "vmx2.lasthop.io",
    "user": "pyclass",
    "password": getpass(),
}

dev = Device(**vmx2)
dev.open()

xml_out = dev.rpc.get_interface_information()
intf_addr = xml_out.findall(".//interface-address/ifa-local")

new_addresses = []
for addr in intf_addr:
    addr_text = addr.text
    addr_family = addr.getparent().getparent()
    af_name = addr_family.find("./address-family-name")
    af_name = af_name.text.strip()
    if "inet" in af_name:
        new_addresses.append(addr_text.strip())

pprint(new_addresses)
