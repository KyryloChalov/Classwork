from random import randint
from time import sleep
from threading import Thread

def worker(param):
    rand = randint(0,5)
    # rand = randint(0,5)
    # print('Thread # ', param, ' sleep ', rand)
    print(param, ' sleep ', rand)
    sleep(rand)
    # print('Thread # ', param, ' up')
    print(param, 'end')

if __name__ == "__main__":
    for i in range(55):
        # print('Thread # ', i, ' call')
        # th = Thread(target=th_function, args=(i, ))
        th = Thread(target=worker, args=(f"Count thread - {i}", ))
        th.start()
        # print('Thread # ', i, ' stop')