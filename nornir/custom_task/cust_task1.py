from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def my_task(task):
    print()
    print('-' * 40)
    print(f"Task: {task}")
    print(f"Host: {task.host.name}")
    print('-' * 40)
    print()


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    agg_result = nr.run(task=my_task)
