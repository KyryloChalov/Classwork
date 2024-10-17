from threading import Thread, RLock
from random import randint
from logger import logger
from time import time, sleep

counter = 0
lock = RLock()


def func(th, ):
    global counter
    while True:
        with lock:
            timer = time()
            counter += 1
            delay = randint(1, 3)
            sleep(delay)
            with open('result_04.txt', 'a') as fd:
                fd.write(f'{th}: {counter = }  {delay = } ({time() - timer})\n')
            # print(f'{th}: {counter = }  {delay = } ({time() - timer})')
        # logger.debug(f'{counter = }')


if __name__ == '__main__':
    logger.debug('Started')
    for i in range(5):
        # delay = randint(1, 3)
        # sleep(delay)
        name=f"Th # {i}"
        th = Thread(name=name, target = func, args=(name, ))
        th.start()
        logger.debug(th)
    logger.debug('End')
