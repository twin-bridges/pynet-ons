from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.data import load_yaml # noqa
from nornir.plugins.tasks.data import load_json # noqa


def custom_task(task):
    import ipdb; ipdb.set_trace()
    # my_data = task.run(task=load_yaml, file=f"sros/{task.host.name}.yaml")
    my_data = task.run(task=load_json, file=f"sros/{task.host.name}.json")
    print(my_data.result)


def main():
    nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
    nr = nr.filter(name="sros1")
    result = nr.run(task=custom_task)
    print_result(result)


if __name__ == "__main__":
    main()
