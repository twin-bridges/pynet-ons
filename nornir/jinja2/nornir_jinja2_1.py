from nornir import InitNornir
from nornir.plugins.tasks.text import template_string


if __name__ == "__main__":

    TEMPLATE_STR = """
interface loopback{{ int_num }}
  description {{ descr | lower }}
  no shut

"""

    nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
    nr = nr.filter(name="srx2")

    my_vars = {
        "int_num": "99",
        "descr": "My Description",
    }

    agg_result = nr.run(task=template_string, template=TEMPLATE_STR, **my_vars)

    print()
    print("-" * 40)
    print(agg_result["srx2"][0].result)
    print("-" * 40)
    print()
