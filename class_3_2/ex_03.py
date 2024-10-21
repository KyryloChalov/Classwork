import sys
from multiprocessing import Process

# import logging
import os
from time import sleep

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)


def example_work(params):
    sleep(0.5)
    print(params)
    # logger.debug(params)
    sys.exit(0)


if __name__ == "__main__":
    processes = []
    for i in range(5):
        pr = Process(target=example_work, args=(f"Count process function - {i}",))
        pr.start()
        print(f"pr.pid[{i}] = {pr.pid}")
        processes.append(pr)

    # [print(el.exitcode, end=" ") for el in processes]
    num_to_kill = 3
    process_pid = processes[num_to_kill].pid
    print(f"processes[{num_to_kill}].pid = {process_pid}")
    os.kill(process_pid, 9)
    [el.join() for el in processes]
    [print(el.exitcode, end=" ") for el in processes]
    print()

    print("End program")
