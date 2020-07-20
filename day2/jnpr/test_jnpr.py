from utilities import subprocess_runner
from ex2_jnpr_tables import gather_routes, gather_arp_table
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable


def test_jnpr_ex1():
    base_path = "."
    cmd_list = ["python", "ex1_jnpr_facts.py"]

    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=base_path)

    assert std_err == ""
    assert return_code == 0
    assert "VM5F0DDCE0AA" in std_out
    assert "vmx1" in std_out


def test_jnpr_ex2(pyez_connect):

    device = pyez_connect
    routes = gather_routes(device)
    assert isinstance(routes, RouteTable)
    assert "0.0.0.0/0" in routes.keys()

    arp_entries = gather_arp_table(device)
    assert isinstance(arp_entries, ArpTable)
    assert "00:62:ec:29:70:fe" in arp_entries.keys()
