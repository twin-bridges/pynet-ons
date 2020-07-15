#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter router password: ")
    device = {
        "device_type": "cisco_ios_telnet",
        "host": "cisco1.lasthop.io",
        "username": "pyclass",
        "password": password,
    }

    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt())
