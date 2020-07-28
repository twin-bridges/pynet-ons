from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.tasks.networking import netmiko_save_config
from nornir.plugins.functions.text import print_result


if __name__ == "__main__":

    cfg = [
        "/configure system time ntp peer 130.126.24.24",
        "/configure system time ntp peer 152.2.21.1",
    ]

    nr = InitNornir(config_file="config.yaml")
    sros = nr.filter(F(groups__contains="sros"))

    # import ipdb; ipdb.set_trace()
    agg_result = sros.run(task=netmiko_send_config, config_commands=cfg)
    print_result(agg_result)

    agg_result = sros.run(task=netmiko_save_config)
    print_result(agg_result)
