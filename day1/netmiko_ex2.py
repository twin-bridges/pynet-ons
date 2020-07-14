#!/usr/bin/env python
"""Exercises using Netmiko"""
from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler


def main():
    """Exercises using Netmiko"""
    passwd = getpass("Enter password: ")

    nxos1 = {
        "device_type": "cisco_nxos",
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": passwd,
    }

    cfg_commands = ["logging console 3"]

    for a_device in [nxos1]:
        net_connect = ConnectHandler(**a_device)
        print("Current Prompt: " + net_connect.find_prompt())

        print("\nConfiguring logging")
        print("#" * 80)
        output = net_connect.send_config_set(cfg_commands)
        print("\nSaving config to startup")
        net_connect.save_config()
        print(output)
        print("#" * 80)
        print()


if __name__ == "__main__":
    main()
