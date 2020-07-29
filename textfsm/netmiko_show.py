#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler
from pprint import pprint

password = getpass()

device = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command(
    "show ip interface brief", use_textfsm=True, textfsm_template="new_template.tpl"
)
net_connect.disconnect()

print("-" * 50)
pprint(output)
print("-" * 50)
