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

cfg_commands = [
    '/configure router interface "rtr1" no shutdown',
    '/configure router interface "rtr1" address 10.20.1.1/24',
]

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_config_set(cfg_commands)
    output += net_connect.save_config()

print("-" * 50)
print(output)
print("-" * 50)
