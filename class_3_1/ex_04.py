from threading import Thread, RLock
from logger import logger
from time import time, sleep

lock = RLock()


def func(locker, delay):
    timer = time()
    locker.acquire()
    sleep(delay)
    locker.release()
    logger.debug(f'Done {time() - timer}')


if __name__ == '__main__':
    t1 = Thread(target=func, args=(lock, 2))
    t2 = Thread(target=func, args=(lock, 2))
    t1.start()
    t2.start()
    logger.debug('Started')
