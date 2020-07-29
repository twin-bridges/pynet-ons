from nornir import InitNornir
from nornir.plugins.functions.text import print_result


def my_task(task):
    msg = f"\nHello host: {task.host.name}\n"
    return msg


if __name__ == "__main__":

    import ipdb; ipdb.set_trace()
    nr = InitNornir(config_file="config.yaml")
    aggr_result = nr.run(task=my_task)
    print_result(aggr_result)
