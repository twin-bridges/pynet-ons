from concurrent.futures import ThreadPoolExecutor
from getpass import getpass
from netmiko import ConnectHandler


PASSWORD = getpass()
DEVICES = [
    {
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": PASSWORD,
        "device_type": "cisco_ios",
    },
    {
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": PASSWORD,
        "device_type": "cisco_ios",
    },
    {
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": PASSWORD,
        "device_type": "arista_eos",
    },
    {
        "host": "arista2.lasthop.io",
        "username": "pyclass",
        "password": PASSWORD,
        "device_type": "arista_eos",
    },
]


def show_command(dev, cmd):
    conn = ConnectHandler(**dev)
    output = conn.send_command(cmd)
    conn.disconnect()
    return output


def main():
    with ThreadPoolExecutor(max_workers=8) as pool:
        threads = []
        for dev in DEVICES:
            threads.append(pool.submit(show_command, dev, "show ip arp"))

    for thread in threads:
        print()
        print(thread.result())
        print()


if __name__ == "__main__":
    main()
