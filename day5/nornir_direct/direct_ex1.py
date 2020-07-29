from nornir import InitNornir
from nornir.plugins.functions.text import print_result


def netmiko_direct(task):

    # Manually create Netmiko connection
    net_connect = task.host.get_connection("netmiko", task.nornir.config)
    prompt = net_connect.find_prompt()
    task.host.close_connection("netmiko")
    msg = f"\n\n{prompt}\n\n"
    return msg


if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(platform="nokia_sros")
    aggr_results = nr.run(task=netmiko_direct, num_workers=10)
    print_result(aggr_results)
