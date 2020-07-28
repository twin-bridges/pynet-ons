
from nornir import InitNornir
from nornir.plugins.functions.text import print_result


def my_task(task):
    msg = f"\nHello host: {task.host.name}\n"
    return msg


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    results = nr.run(task=my_task)
    print_result(results)
