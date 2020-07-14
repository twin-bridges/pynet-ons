# content of test_sample.py
import pytest
from getpass import getpass
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def netmiko_connect():
    """Establish a netmiko connection."""
    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
    }
    return ConnectHandler(**cisco3)
