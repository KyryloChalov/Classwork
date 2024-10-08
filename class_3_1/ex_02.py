from threading import Thread
from logger import logger
from time import sleep
from random import randint



class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        logger.debug('- Sleep')
        sleep(self.args[1])
        logger.debug('Wake up!')
        logger.debug(f"In my thread: {self.args}")


if __name__ == '__main__':
    threads = []
    logger.debug('Begin cycle')
    for i in range(5):
        rand = randint(0,3)
        thread = MyThread(name=f' > Tread #{i}', args=(f"Count thread - {i}", rand))
        thread.start()
        threads.append(thread)
    logger.debug('End cycle')
    sleep(2)
    logger.debug('End program')
