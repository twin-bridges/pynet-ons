# content of test_sample.py
import os
import pytest
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def netmiko_connect():
    """Establish a netmiko connection."""
    device = {
        "device_type": "juniper_junos",
        "host": "vmx2.lasthop.io",
        "username": "pyclass",
        "password": os.environ["JNPR_PASSWORD"],
    }
    return ConnectHandler(**device)
