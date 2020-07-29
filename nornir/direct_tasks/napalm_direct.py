from lxml import etree

from nornir import InitNornir
from nornir.core.filter import F


def direct(task):

    # Manually create NAPALM connection
    napalm = task.host.get_connection("napalm", task.nornir.config)

    # PyEZ connection
    jnpr_conn = napalm.device

    # PyEZ RPC
    xml_output = jnpr_conn.rpc.get_software_information()
    print()
    print("-" * 40)
    print(etree.tostring(xml_output, encoding="unicode", pretty_print=True))
    print("-" * 40)
    print()


if __name__ == "__main__":
    with InitNornir(config_file="config.yaml") as nr:
        filt = F(groups__contains="junos")
        nr = nr.filter(filt)
        nr.run(task=direct, num_workers=10)
