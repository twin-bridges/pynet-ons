from nornir import InitNornir
from nornir.plugins.functions.text import print_result


def exercise_task(task):

    host = task.host
    msg = f"""

Host: {host.name}
Hostname: {host.hostname}
Port: {host.port}

"""
    return msg


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    results = nr.run(task=exercise_task)
    print_result(results)
