#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

device = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": password,
    "port": 2211,
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt())
# net_connect.disconnect()
