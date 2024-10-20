from threading import Thread, Event
from logger import logger
from time import sleep


def example_work(event_for_exit: Event):
    while True:
        sleep(1)
        logger.debug("Run event work")

        if event_for_exit.is_set():
            break


if __name__ == "__main__":
    event = Event()
    thread = Thread(target=example_work, args=(event,))
    thread.start()

    sleep(5)
    event.set()

    logger.debug("End program")
