from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    results = nr.run(task=netmiko_send_command, command_string="show version")
    print_result(results)
