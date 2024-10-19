import concurrent.futures
from random import randint
from time import sleep

from logger import logger

def greeting(name):
    delay = randint(0, 5)
    logger.debug(f'greeting for: {name}, {delay = }')
    sleep(delay)
    return f"Hello {name}"


arguments = (
    "Bill",
    "Jill",
    "Till",
    "Sam",
    "Tom",
    "John",
)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(greeting, arguments))

    logger.debug(results)
