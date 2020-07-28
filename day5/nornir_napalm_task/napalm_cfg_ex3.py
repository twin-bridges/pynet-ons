from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_configure


def main():

    nr = InitNornir(config_file="config.yaml")
    vmx1 = nr.filter(name="vmx1")

    config_file = "my_routes.conf"

    agg_result = vmx1.run(task=napalm_configure, filename=config_file, dry_run=True)

    # Print the "diff" out
    print()
    print("-" * 40)
    print(agg_result["vmx1"][0].diff)
    print("-" * 40)
    print()


if __name__ == "__main__":
    main()
