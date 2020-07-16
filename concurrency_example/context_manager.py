from concurrent.futures import ProcessPoolExecutor
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
    # Context manager defaults to waiting for all procs to complete
    # Same as using the `wait` function
    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as pool:
        procs = []
        for _ in range(AMOUNT_OF_MATHS):
            procs.append(pool.submit(do_maths))

    for proc in procs:
        print(proc.result())


if __name__ == "__main__":
    main()
