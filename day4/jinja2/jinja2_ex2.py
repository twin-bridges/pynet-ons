from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment


def main():
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")

    interface = "Ethernet2/1"
    nxos1 = {
        "host": "nxos1",
        "interface": interface,
        "ipv4_address": "10.1.100.1",
        "ipv4_netmask": "24",
    }
    nxos2 = {
        "host": "nxos2",
        "interface": interface,
        "ipv4_address": "10.1.100.2",
        "ipv4_netmask": "24",
    }

    print()
    for j2_vars in (nxos1, nxos2):
        template_file = "nxos_ipv4_intf.j2"
        template = env.get_template(template_file)
        output = template.render(**j2_vars)
        print("-" * 10)
        print(j2_vars["host"])
        print("-" * 10)
        print(output.lstrip())
    print()


if __name__ == "__main__":
    main()
