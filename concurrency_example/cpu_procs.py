"""
Purpose of this example is to demonstrate multiple processes 
being used -- in this case up to the PROC_POOL size.

So we submit TASKS=N to the worker pool and as processes free
up, the tasks get executed.

Use top or activity/system monitor to see multiple instances
of Python.
"""
from concurrent.futures import ProcessPoolExecutor, wait
import math
import random


TASKS = 20
PROC_POOL = 8


def math_calculation():
    for i in range(random.randint(10000000, 30000000)):
        final_sqrt = math.sqrt(i)
    return final_sqrt


def main():
    # Create process pool
    pool = ProcessPoolExecutor(max_workers=PROC_POOL)
    futures = []

    # Submit work to process pool
    for _ in range(TASKS):
        futures.append(pool.submit(math_calculation))

    # Block waiting for tasks to complete
    wait(futures)
    for task_result in futures:
        print(task_result.result())


if __name__ == "__main__":
    main()
