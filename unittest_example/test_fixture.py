import pytest
from getpass import getpass
from netmiko import ConnectHandler

# Fixtures
@pytest.fixture(scope="module")
def netmiko_connect():
    cisco3 = {
        "device_type": "cisco_ios",
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
    }
    return ConnectHandler(**cisco3)


def test_prompt(netmiko_connect):
    # print(netmiko_connect.find_prompt())
    assert netmiko_connect.find_prompt() == "cisco3#"


def test_show_version(netmiko_connect):
    output = netmiko_connect.send_command("show version")
    assert "Configuration register is 0x2102" in output
