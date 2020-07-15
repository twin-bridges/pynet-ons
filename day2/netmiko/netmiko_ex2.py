#!/usr/bin/env python
"""Exercises using Netmiko"""
from __future__ import print_function
from getpass import getpass
from netmiko import ConnectHandler


def main():
    """Exercises using Netmiko"""
    passwd = getpass("Enter password: ")

    sros4 = {
        "device_type": "nokia_sros",
        "host": "sros.lasthop.io",
        "username": "admin",
        "password": passwd,
        "port": 2214,
    }

    cfg_commands = ['/configure system location "San Francisco"']

    for a_device in [sros4]:
        net_connect = ConnectHandler(**a_device)
        print("Current Prompt: " + net_connect.find_prompt())

        print("\nConfiguring...")
        print("#" * 80)
        output = net_connect.send_config_set(cfg_commands)
        save_output = net_connect.save_config()
        print("\nSaving config to startup")
        print(output)
        print(save_output)
        print("#" * 80)
        print()
        net_connect.disconnect()


if __name__ == "__main__":
    main()
