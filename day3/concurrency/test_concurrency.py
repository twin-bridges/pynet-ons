import os
from concurrency_ex1 import show_command


def test_concurrency_ex1():

    device = {
        "device_type": "nokia_sros",
        "host": "sros.lasthop.io",
        "username": "admin",
        "password": os.environ["SROS_PASSWORD"],
        "port": 2211,
    }

    cmd = "show router arp"

    output = show_command(device, cmd)
    assert "10.217.12.1" in output

