import pytest
from getpass import getpass
from netmiko import ConnectHandler

# Fixtures
@pytest.fixture(scope="module")
def netmiko_connect():
    device = {
        "device_type": "cisco_ios",
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
    }
    return ConnectHandler(**device)


def test_prompt(netmiko_connect):
    assert netmiko_connect.find_prompt() == "cisco4#"


def test_show_ip_int_brief(netmiko_connect):
    output = netmiko_connect.send_command("show ip int brief")
    assert "10.220.88.23" in output
