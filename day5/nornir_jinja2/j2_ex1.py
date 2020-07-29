from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_configure
from nornir.plugins.tasks.text import template_file

def generate_config(task):

    host = task.host
    template = "dns_ntp.j2"
    result = task.run(
        task=template_file, template=template, path=".", **host
    )

    # Save the config to the host
    host.data['config'] = result.result


def config_device(task):
    host = task.host
    my_config = host['config']
    task.run(task=napalm_configure, configuration=my_config, dry_run=True)


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(platform="junos")
    nr.run(task=generate_config, num_workers=10)
    agg_result = nr.run(task=config_device, num_workers=10)

    # Print the "diff" out
    for hostname, multi_result in agg_result.items():
        print()
        print("-" * 40)
        print(f"Hostname: {hostname}")
        print("-" * 25)
        print(multi_result[1].diff)
        print("-" * 40)
        print()
