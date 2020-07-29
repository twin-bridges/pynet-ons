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
    "global_delay_factor": 4,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show system lldp neighbor")
net_connect.disconnect()

print("-" * 50)
print(output)
print("-" * 50)
