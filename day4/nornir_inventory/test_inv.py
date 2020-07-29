from nornir import InitNornir

def test_nornir_inv():

    # import ipdb; ipdb.set_trace()
    nr = InitNornir(config_file="config.yaml")
    assert len(nr.inventory.hosts.keys()) == 4
    assert len(nr.inventory.groups.keys()) == 2
    sros1 = nr.inventory.hosts["sros1"]
    assert sros1.name == "sros1"
    assert sros1.hostname == "sros.lasthop.io"
    assert sros1.platform == "nokia_sros"
    assert sros1.port == 2211
    assert sros1.username == "nokia"
    assert sros1.password == "test123"

