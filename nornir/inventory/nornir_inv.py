from nornir import InitNornir
import ipdb

nr = InitNornir(config_file="config.yaml")
ipdb.set_trace()
print(nr)
