"""
Purpose of this example is to demonstrate multiple threads
(Python instances) being spawned -- in this case up to the
AMOUNT_OF_MATHS.

Use top or activity/system monitor to see a single instance
of Python being ran with very high CPU.
"""
from concurrent.futures import ThreadPoolExecutor, wait
import math
import random


AMOUNT_OF_MATHS = 8
# Note: max_workers  will default to num processors on maching * 5 if not given
MAX_WORKERS = 8


def do_maths():
    for i in range(random.randint(10000000, 30000000)):
        final_sqrt = math.sqrt(i)
    return final_sqrt


def main():
    pool = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    threads = []
    for _ in range(AMOUNT_OF_MATHS):
        threads.append(pool.submit(do_maths))
    wait(threads)
    for thread in threads:
        print(thread.result())


if __name__ == "__main__":
    main()
