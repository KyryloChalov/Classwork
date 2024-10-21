from multiprocessing import Process
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def example_work(params):
    sleep(0.5)
    logger.debug(params)


if __name__ == "__main__":
    processes = []
    for i in range(5):
        pr = Process(target=example_work, args=(f"Count process function - {i}",))
        pr.start()
        processes.append(pr)

    [print(el.exitcode, end=" ") for el in processes]
    print()
    [el.join() for el in processes]
    [print(el.exitcode, end=" ") for el in processes]

    logger.debug("End program")
