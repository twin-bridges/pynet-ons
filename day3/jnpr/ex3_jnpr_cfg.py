import os
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config

password = os.getenv("JNPR_PASSWORD")
if password is None:
    password = getpass("Enter vMX password: ")

import ipdb; ipdb.set_trace()
# Create pyez Device object for vmx2
my_device = Device(host="vmx2.lasthop.io", user="pyclass", password=password)
my_device.open()

# Create device Config object
my_device_cfg = Config(my_device)

# Lock device configuration
my_device_cfg.lock()

# Try to acquire Lock again
print()
try:
    my_device_cfg.lock()
    print("Lock acquired!")
except LockError:
    print("Device is already locked.")

# Stage a config to change the device hostname
my_device_cfg.load("set system host-name test-name", format="set", merge=True)

# Check the diff of the staged vs running config
print()
print("Check diff of staged-config vs running-config")
print("-" * 20)
print(my_device_cfg.diff())

# Rollback staged configuration
my_device_cfg.rollback(0)

# Check the diff after the rollback operation
print()
print("Check diff of staged-config vs running-config")
print("-" * 20)
print(my_device_cfg.diff())
print()

my_device_cfg.unlock()
