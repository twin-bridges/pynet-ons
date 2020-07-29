from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def my_task(task):
    msg = f"""

---------------------------
Task: {task}
Host: {task.host.name}
---------------------------

"""
    return msg


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    agg_result = nr.run(task=my_task)
    print_result(agg_result)
