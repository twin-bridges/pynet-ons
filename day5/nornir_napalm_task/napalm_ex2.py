from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(platform="junos")
    agg_result = nr.run(task=napalm_get, getters=["config"])

    print()
    for device_name, m_result in agg_result.items():
        print("-" * 50)
        print(device_name)
        print(m_result[0].result["config"]["running"])
        print("-" * 50)
    print()
