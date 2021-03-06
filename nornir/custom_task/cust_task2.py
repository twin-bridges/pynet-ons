from nornir import InitNornir
from nornir.plugins.functions.text import print_result


def my_task(task):
    print()
    print("-" * 40)
    print(f"Task: {task}")
    print(f"Host: {task.host.name}")
    print("-" * 40)
    print()
    return "\n\nHello world\n\n"


if __name__ == "__main__":

    # import ipdb; ipdb.set_trace()
    nr = InitNornir(config_file="config.yaml")
    agg_result = nr.run(task=my_task)
    print_result(agg_result)
