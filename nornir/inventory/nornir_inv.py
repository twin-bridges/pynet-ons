from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
import ipdb

nr = InitNornir(config_file="config.yaml")
ipdb.set_trace()
print(nr)
