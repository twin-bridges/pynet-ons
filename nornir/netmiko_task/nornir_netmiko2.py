from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    sros = nr.filter(F(groups__contains="sros"))
    agg_result = sros.run(task=netmiko_send_command, command_string="admin display-config")
    # junos = nr.filter(F(groups__contains="junos"))
    # agg_result = junos.run(task=netmiko_send_command, command_string="show configuration")
    print_result(agg_result)
