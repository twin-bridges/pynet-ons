from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

sros1 = nr.inventory.hosts["sros3"]
print()
print(f"Name: {sros1.name}")
print(f"Host: {sros1.hostname}")
print(f"Port: {sros1.port}")
print(f"Groups: {sros1.groups}")
print(f"Platform: {sros1.platform}")
print(f"Platform: {sros1.username}")
print(f"Platform: {sros1.password}")
print()
