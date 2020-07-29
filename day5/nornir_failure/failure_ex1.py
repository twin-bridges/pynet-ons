from nornir import InitNornir


def my_task(task):
    raise ValueError("An error happened in my_task.")


def simple_task(task):
    print(f"Host: {task.host.name}")


if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    aggr_results = nr.run(task=my_task)

    print()
    if aggr_results.failed is True:
        print("Task failed")
        print(aggr_results.failed)
        print()

    vmx1 = aggr_results["vmx1"]
    print(f"Exception on vmx1: {vmx1.exception}\n")

    print(f"Failed Hosts:\n{nr.data.failed_hosts}\n")

    # Recover vmx1 and vmx2
    print("Recovering 'vmx1' and 'vmx2'\n")
    nr.data.recover_host("vmx1")
    nr.data.recover_host("vmx2")

    # Run a task on the remaining failed hosts
    print("Executing task on the still failed hosts.")
    aggr_result = nr.run(task=simple_task, on_failed=True, on_good=False)
    print()
