import os
from getpass import getpass
from pprint import pprint
from jnpr.junos import Device


# For automated testing
password = os.getenv("JNPR_PASSWORD")
if password is None:
    password = getpass("Enter vMX password: ")

# Create pyez Device object for vmx1
my_dev = Device(host="vmx1.lasthop.io", user="pyclass", password=password)

# Create NETCONF connection to device
my_dev.open()

print()
print("Print device facts")
print("-" * 20)
pprint(my_dev.facts)

print("\n\n")
print("Print hostname from device facts")
print("-" * 20)
print(my_dev.facts["hostname"])
print()
