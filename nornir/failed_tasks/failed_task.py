from nornir import InitNornir
from nornir.core.exceptions import NornirExecutionError
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


if __name__ == "__main__":

    import ipdb; ipdb.set_trace()
    nr = InitNornir(config_file="config.yaml")
    aggr_result = nr.run(task=netmiko_send_command, command_string="show configuration")

    print(aggr_result.failed)
    print(aggr_result.failed_hosts.keys())

    vmx1 = aggr_result.failed_hosts['vmx1']
    print(vmx1.exception)

    try:
        aggr_result.raise_on_error()
    except NornirExecutionError:
        print("We can cause this exception to be raised")

