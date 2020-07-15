#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

password = getpass()

sros1 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": password,
    "port": 2211,
}

sros2 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": password,
    "port": 2212,
}

sros3 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": password,
    "port": 2213,
}

sros4 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": password,
    "port": 2214,
}

for device in (sros1, sros2, sros3, sros4):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show system lldp neighbor")

    print()
    print(f"Host: {net_connect.host}:{net_connect.port}")
    print("-" * 50)
    print(output)
    print("-" * 50)
    net_connect.disconnect()
