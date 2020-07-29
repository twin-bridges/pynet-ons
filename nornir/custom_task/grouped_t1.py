from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import netmiko_send_config, netmiko_save_config


def my_task(task):
    config_commands = ['/configure system location "San Francisco"']

    # Send configuration
    task.run(task=netmiko_send_config, config_commands=config_commands)

    # Save running config to startup
    task.run(task=netmiko_save_config)

    return "whatever"


if __name__ == "__main__":

    # Initialize Nornir
    nr = InitNornir(config_file="config.yaml")
    sros = nr.filter(F(groups__contains="sros"))

    # Run task
    import ipdb; ipdb.set_trace()
    aggr_result = sros.run(task=my_task)

    # Print results
    print()
    print('-' * 30)
    print(f"SROS1-result0:\n{aggr_result['sros1'][0].result}")
    print('-' * 30)
    print(f"SROS1-result1:\n{aggr_result['sros1'][1].result}")
    print('-' * 30)
    print(f"SROS1-result2:\n{aggr_result['sros1'][2].result}")
    print('-' * 30)
    print()
