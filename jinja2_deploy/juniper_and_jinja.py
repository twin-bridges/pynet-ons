#!/usr/bin/env python
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from getpass import getpass
from pprint import pprint

USER = "pyclass"
PASSWORD = getpass()

def render_configs():
    pass

def load_configs():
    pass



if __name__ == "__main__":

    template_file = "juniper_bgp.j2"

    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader([".", "./templates/"])

    with open(template_file) as f:
        bgp_template = f.read()

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

        # Render configs
        template = env.get_template(template_file)
        config_section = template.render(**bgp_vars)

        # Store generated config
        configs[device_name] = config_section

    # Load configurations
    for host, load_config in configs.items():

        import ipdb; ipdb.set_trace()

        # PyEZ connection
        a_device = Device(host=host, user=USER, password=PASSWORD)
        a_device.open()
        a_device.timeout = 90

        # Load config object
        cfg = Config(a_device)
        cfg.load(load_config, format="text", merge=True)

        print()
        print("-" * 70)
        print("Working on device: {}".format(host))
        print("Configuring BGP")

        print("Current config differences: ")
        print(cfg.diff())
        if cfg.diff():
            print("Performing commit")
            # cfg.commit()
        print()
