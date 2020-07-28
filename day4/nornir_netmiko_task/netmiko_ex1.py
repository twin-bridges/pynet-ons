from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    jnpr = nr.filter(F(groups__contains="junos"))

    results = jnpr.run(task=netmiko_send_command, command_string="show arp")
    print_result(results)
