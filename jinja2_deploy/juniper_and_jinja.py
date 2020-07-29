#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from getpass import getpass

USER = "pyclass"
PASSWORD = getpass()


def render_configs(j2_env, template_file, my_vars):
    # Render configs
    template = j2_env.get_template(template_file)
    config_section = template.render(**my_vars)
    return config_section


def load_configs(host, config, junos_format="text"):

    # PyEZ connection
    a_device = Device(host=host, user=USER, password=PASSWORD)
    a_device.open()
    a_device.timeout = 90

    # Load config object
    cfg = Config(a_device)
    cfg.load(config, format=junos_format, merge=True)
    return cfg


if __name__ == "__main__":

    template_file = "juniper_bgp.j2"

    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader([".", "./templates/"])

    rtr1 = {
        "device_name": "vmx1.lasthop.io",
        "local_as": 10,
        "neighbor_ip": "10.100.1.2",
        "neighbor_as": 20,
    }

    rtr2 = {
        "device_name": "vmx2.lasthop.io",
        "local_as": 20,
        "neighbor_ip": "10.100.1.1",
        "neighbor_as": 10,
    }

    configs = {}
    for bgp_vars in [rtr1, rtr2]:
        device_name = bgp_vars["device_name"]

        config_section = render_configs(
            env, template_file=template_file, my_vars=bgp_vars
        )

        # Store generated config
        configs[device_name] = config_section

    # Load configurations
    for host, load_config in configs.items():

        import ipdb

        ipdb.set_trace()

        cfg = load_configs(host, config=load_config, junos_format="text")
        commit = False

        print()
        print("-" * 70)
        print("Working on device: {}".format(host))
        print("Configuring BGP")

        print("Current config differences: ")
        print(cfg.diff())

        if commit:
            print("Performing commit")
            cfg.commit()
        else:
            cfg.rollback(0)
        print()
