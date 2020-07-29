from nornir import InitNornir


def my_task(task):
    return f"Host is {task.host.name}"


if __name__ == "__main__":

    import ipdb

    ipdb.set_trace()
    nr = InitNornir(config_file="config.yaml")
    aggr_results = nr.run(task=my_task)
