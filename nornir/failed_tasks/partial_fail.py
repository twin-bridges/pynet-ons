from nornir import InitNornir
from nornir.core.exceptions import NornirExecutionError
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

def failed_task(task):
    print()
    print('-' * 60)
    print(f"This is a host that earlier failed: {task.host.name}")
    print('-' * 60)
    print()

if __name__ == "__main__":

    import ipdb; ipdb.set_trace()
    nr = InitNornir(config_file="config2.yaml")
    aggr_result = nr.run(task=netmiko_send_command, command_string="show configuration")

    print(aggr_result.failed)
    print(aggr_result.failed_hosts.keys())

    # Run second task on only successful hosts
    aggr_result = nr.run(task=netmiko_send_command, command_string="show arp")
    print_result(aggr_result)    

    # Run a task on the failed hosts
    aggr_result = nr.run(task=failed_task, on_failed=True, on_good=False)

    # Recover specific host
    print(f"Failed Hosts: {nr.data.failed_hosts}")
    nr.data.recover_host("vmx2") 

    # Reset failed hosts
    print(f"Failed Hosts: {nr.data.failed_hosts}")
    print("Reset failed hosts")
    nr.data.reset_failed_hosts()
    print(f"Failed Hosts: {nr.data.failed_hosts}")
