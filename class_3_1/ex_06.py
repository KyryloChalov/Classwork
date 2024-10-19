from threading import Thread, Event
from logger import logger
from time import sleep


def worker(event: Event):
    logger.debug('Worker ready to work')
    event.wait()
    logger.debug('The worker can do the work')


def master_th(event: Event):
    logger.debug('Master doing some work')
    sleep(2)
    logger.debug('Informing that workers can do the work')
    event.set()


if __name__ == '__main__':
    event = Event()
    master = Thread(name='master', target=master_th, args=(event, ))

    worker_one = Thread(name='worker_one', target=worker, args=(event, ))
    worker_two = Thread(name='worker_two', target=worker, args=(event,))
    worker_one.start()
    worker_two.start()
    master.start()

    logger.debug('End program')
