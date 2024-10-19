from threading import Thread, Condition
from logger import logger
from time import sleep


def worker(condition: Condition):
    logger.debug('Worker ready to work')
    with condition:
        condition.wait()
        logger.debug('The worker can do the work')


def master_th(condition: Condition):
    logger.debug('Master doing some work')
    sleep(2)
    with condition:
        logger.debug('Informing that workers can do the work')
        condition.notify_all()


if __name__ == '__main__':
    condition = Condition()
    master = Thread(name='master', target=master_th, args=(condition,))

    worker_one = Thread(name='worker_one', target=worker, args=(condition, ))
    worker_two = Thread(name='worker_two', target=worker, args=(condition,))
    worker_one.start()
    worker_two.start()
    master.start()

    logger.debug('End program')
