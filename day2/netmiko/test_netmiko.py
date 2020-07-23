import re
import os.path
from utilities import subprocess_runner


def test_file_write_func():
    from netmiko_ex1 import save_file

    # Save content to a file
    my_file = "test_save_file.txt"
    test_string = "some text content"
    save_file(my_file, test_string)

    # Read content written out back from file
    with open(my_file) as f:
        content = f.read()
        assert test_string in content


def test_netmiko_ex1():
    base_path = "."
    cmd_list = ["python", "netmiko_ex1.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)

    # import ipdb; ipdb.set_trace()

    assert return_code == 0
    assert std_err == ""
    assert "sros1" in std_out
    assert "vmx1" in std_out
    assert "TiMOS-B-20.5.R2" in std_out
    assert "18.4R1.8" in std_out

    # Checks SR-OS
    assert "A:sros1#" in std_out
    assert re.search(r"TiMOS-B-20.5.R2.*Nokia", std_out)

    # Checks Juniper
    assert "pyclass@vmx1>" in std_out
    assert re.search(r"Hostname:.*vmx1", std_out)
    assert re.search(r"Model:.vmx", std_out)
    assert re.search(r"Junos:.18.4R1.8", std_out)

    # Check for file existence
    files = ["A:sros1.txt", "pyclass@vmx1.txt"]
    for a_file in files:
        assert os.path.isfile(a_file)


def test_config_location(netmiko_connect_sros4):
    config = netmiko_connect_sros4.send_command("admin display-config")
    assert 'location "San Francisco"' in config
