from nornir import InitNornir
from nornir.plugins.functions.text import print_result  # noqa


def netmiko_direct(task):

    # Manually create Netmiko connection
    net_connect = task.host.get_connection("netmiko", task.nornir.config)

    # Use the connection
    print()
    print("#" * 80)
    print(net_connect.find_prompt())
    output = net_connect.send_command("show system ntp")
    print(output)
    print("#" * 80)
    print()

    # Close the connection
    task.host.close_connection("netmiko")


if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(name="sros1")
    nr.run(task=netmiko_direct, num_workers=1)
