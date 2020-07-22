import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from getpass import getpass
from netmiko import ConnectHandler


def show_command(dev, cmd):
    conn = ConnectHandler(**dev)
    output = conn.send_command(cmd)
    conn.disconnect()
    return output


def main():

    # For automated testing
    password = os.getenv("SROS_PASSWORD")
    if password is None:
        password = getpass("Enter SR-OS password: ")

    devices = [
        {
            "host": "sros.lasthop.io",
            "username": "admin",
            "password": password,
            "device_type": "nokia_sros",
            "port": 2211,
        },
        {
            "host": "sros.lasthop.io",
            "username": "admin",
            "password": password,
            "device_type": "nokia_sros",
            "port": 2212,
        },
        {
            "host": "sros.lasthop.io",
            "username": "admin",
            "password": password,
            "device_type": "nokia_sros",
            "port": 2213,
        },
        {
            "host": "sros.lasthop.io",
            "username": "admin",
            "password": password,
            "device_type": "nokia_sros",
            "port": 2214,
        },
    ]

    # Create the thread-pool
    pool = ProcessPoolExecutor(max_workers=2)
    futures = []

    # Submit the work to the threadpool (SSH-connection to each device)
    for dev in devices:
        new_future = pool.submit(show_command, dev, "show router arp")
        futures.append(new_future)

    # Process the results as_completed
    print()
    print("-" * 80)
    for result in as_completed(futures):
        print()
        print(result.result())
        print()
    print("-" * 80)
    print()


if __name__ == "__main__":
    main()
