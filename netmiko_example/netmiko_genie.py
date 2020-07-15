#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter password: ")
    device = {
        "device_type": "cisco_xe",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    net_connect = ConnectHandler(**device)
    pprint(net_connect.send_command("show ip int brief", use_genie=True))
    net_connect.disconnect()
