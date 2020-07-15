# content of test_sample.py
import os
import pytest
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def netmiko_connect_sros4():
    """Establish a netmiko connection."""
    device = {
        "device_type": "nokia_sros",
        "host": "sros.lasthop.io",
        "username": "admin",
        "password": os.environ["SROS_PASSWORD"],
        "port": 2214,
    }
    return ConnectHandler(**device)
