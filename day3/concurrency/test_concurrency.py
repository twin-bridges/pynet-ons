import os
import pytest
from concurrency_ex1 import show_command

SROS1 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": os.environ["SROS_PASSWORD"],
    "port": 2211,
}
SROS2 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": os.environ["SROS_PASSWORD"],
    "port": 2212,
}
SROS3 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": os.environ["SROS_PASSWORD"],
    "port": 2213,
}
SROS4 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": os.environ["SROS_PASSWORD"],
    "port": 2214,
}


def test_concurrency_ex1a():
    device = SROS1
    cmd = "show router arp"
    output = show_command(device, cmd)
    assert "10.217.12.1" in output


@pytest.mark.parametrize(
    "device, arp_entry",
    [
        (SROS1, "10.217.12.1"),
        (SROS2, "10.217.12.2"),
        (SROS3, "10.217.34.1"),
        (SROS4, "10.217.34.2"),
    ],
)
def test_concurrency_ex1b(device, arp_entry):
    cmd = "show router arp"
    output = show_command(device, cmd)
    assert arp_entry in output
