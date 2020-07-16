from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

password = getpass()
vmx1 = {
    "host": "vmx1.lasthop.io",
    "user": "pyclass",
    "password": password
}

a_device = Device(**vmx1)
a_device.open()
pprint(a_device.facts)
