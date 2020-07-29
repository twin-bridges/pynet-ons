from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_configure


def main():

    nr = InitNornir(config_file="config.yaml")
    junos = nr.filter(platform="junos")

    config_file = "dns_ntp.set"
    agg_result = junos.run(task=napalm_configure, filename=config_file, dry_run=True)

    # Print the "diff" out
    for hostname, multi_result in agg_result.items():
        print()
        print("-" * 40)
        print(f"Hostname: {hostname}")
        print("-" * 25)
        print(multi_result[0].diff)
        print("-" * 40)
        print()


if __name__ == "__main__":
    main()
