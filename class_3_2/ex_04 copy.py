from multiprocessing import Process, Value, RLock, current_process
from time import sleep
import logging
import sys

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(val: Value):
    logger.debug(f"Started {current_process().name}")
    sleep(1)
    with val.get_lock():
        val.value += 1
    logger.debug(f"Done {current_process().name}")
    sys.exit(0)


if __name__ == "__main__":
    lock = RLock()
    value = Value("d", 0, lock=lock)
    prs = []
    for _ in range(5):
        pr = Process(target=worker, args=(value,))
        pr.start()
        prs.append(pr)

    [pr.join() for pr in prs]

    # sleep(1)

    print(value.value)  # 5.0
