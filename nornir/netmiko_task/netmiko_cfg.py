from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_config, netmiko_save_config


def main():

    config_commands = ['/configure system location "San Francisco"']

    # Initialize Nornir
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(F(groups__contains="sros"))

    # Send configuration
    result = nr.run(task=netmiko_send_config, config_commands=config_commands)
    print_result(result)

    # Save running config to startup
    nr.run(task=netmiko_save_config)


if __name__ == "__main__":
    main()
