from threading import Timer
from logger import logger
from time import sleep


def example_work():
    logger.debug("Start!")


if __name__ == "__main__":

    first = Timer(0.5, example_work)
    first.name = "First thread"
    second = Timer(0.7, example_work)
    second.name = "Second thread"
    logger.debug("Start timers")
    first.start()
    second.start()
    sleep(0.6)
    second.cancel()

    logger.debug("End program")
