#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from getpass import getpass
from netmiko import ConnectHandler

if __name__ == "__main__":

    password = getpass("Enter password: ")
    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": password,
        "session_log": "my_session.txt",
    }

    net_connect = ConnectHandler(**cisco3)
    print(net_connect.find_prompt())
    print(net_connect.send_command("show ip int brief"))
    net_connect.disconnect()
