"""
Purpose of this example is to demonstrate multiple threads
being used -- in this case up to the THREAD_POOL size.

So we submit TASKS=N to the worker pool and as threads free
up, the tasks get executed.

Use top or activity/system monitor to see a single instance
of Python being ran with a very high CPU utilization.
"""
from concurrent.futures import ThreadPoolExecutor, wait
import math
import random


TASKS = 20
WORKERS = 8


def math_calculation():
    for i in range(random.randint(10000000, 30000000)):
        final_sqrt = math.sqrt(i)
    return final_sqrt


def main():
    # Create your thread pool
    pool = ThreadPoolExecutor(max_workers=WORKERS)
    futures = []

    # Submit the work to the thread pool
    for _ in range(TASKS):
        futures.append(pool.submit(math_calculation))

    # 'wait' will block until all of the tasks are complete
    wait(futures)
    for task_result in futures:
        print(task_result.result())


if __name__ == "__main__":
    main()
