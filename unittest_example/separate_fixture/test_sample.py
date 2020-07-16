def test_prompt(netmiko_connect):
    assert netmiko_connect.find_prompt() == "pyclass@vmx2>"


def test_show_version(netmiko_connect):
    output = netmiko_connect.send_command("show version")
    assert "Junos: 18.4R1.8" in output


def test_config_mode(netmiko_connect):
    netmiko_connect.config_mode()
    prompt = netmiko_connect.find_prompt()
    assert prompt == "pyclass@vmx2#"
