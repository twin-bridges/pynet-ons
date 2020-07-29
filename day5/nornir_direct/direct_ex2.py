from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result


def direct(task):

    # Manually create NAPALM connection
    napalm = task.host.get_connection("napalm", task.nornir.config)

    # PyEZ connection
    jnpr_conn = napalm.device
    return jnpr_conn.facts


if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    filt = F(groups__contains="junos")
    nr = nr.filter(filt)
    aggr_result = nr.run(task=direct, num_workers=10)
    print_result(aggr_result)
