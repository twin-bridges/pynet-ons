from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_configure


def main():

    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(F(groups__contains="junos"))

    config = """
set system ntp server 130.126.24.24
set system ntp server 152.2.21.1
"""

    import ipdb

    ipdb.set_trace()  # noqa

    agg_result = nr.run(task=napalm_configure, configuration=config, dry_run=True)
    print_result(agg_result)


if __name__ == "__main__":
    main()
