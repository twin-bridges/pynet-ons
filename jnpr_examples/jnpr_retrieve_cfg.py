from jnpr.junos import Device
from lxml import etree
from getpass import getpass
import ipdb

ipdb.set_trace()

password = getpass()
vmx1 = {"host": "vmx1.lasthop.io", "user": "pyclass", "password": password}

dev = Device(**vmx1)
dev = dev.open()
config = dev.cli("show configuration")

xml_out = dev.rpc.get_config()
print(etree.tostring(xml_out, encoding="unicode", pretty_print=True))
