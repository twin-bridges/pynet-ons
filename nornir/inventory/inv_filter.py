from nornir import InitNornir
from nornir.core.filter import F
import ipdb

ipdb.set_trace()

nr = InitNornir(config_file="config.yaml")

tmp_nr = nr.filter(name="sros1")
tmp_nr = nr.filter(platform="nokia_sros")
tmp_nr = nr.filter(hostname="vmx1.lasthop.io")

sros = nr.filter(F(groups__contains="sros"))

all_devices = nr.filter(F(groups__contains="sros") | F(groups__contains="junos"))
set_intersect = nr.filter(F(groups__contains="sros") & F(name="sros3"))
