from nornir import InitNornir
from nornir.plugins.tasks.text import template_file


def my_task(task):
    result = task.run(
        task=template_file, template="interfaces.j2", path=".", **task.host
    )
    print()
    print("-" * 40)
    print(result[0].result)
    print("-" * 40)
    print()


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
    nr = nr.filter(name="srx2")
    nr.run(task=my_task)
