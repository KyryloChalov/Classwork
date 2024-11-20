# import concurrent.futures

from multiprocessing import Process, cpu_count
from multiprocessing.dummy import Pool  # Thread с оболонкою Process
from threading import Thread
from time import time


def worker(values, filename):
    # print('filename: ', filename)
    # print('values: ', values)
    with open(filename, "a") as f:
        for num in values:
            # f.write(f'{num}\n')
            f.write(f"{num ** 2}\n")


if __name__ == "__main__":

    step = 1_000_000
    number_ = 12
    quantity = step * number_
    # print('quantity: ', quantity)
    print(f"quantity: {quantity:,}".replace(",", "_"))
    print("cpu_count =", cpu_count())

    values = list(range(quantity))

    # threads
    th_filename = "th_squares.txt"
    threads = []
    for i in range(number_):
        threads.append(
            Thread(target=worker, args=(values[i * step : (i + 1) * step], th_filename))
        )

    timer = time()
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    print(f"Done by {number_} threads: {round(time() - timer, 4)}")

    # processes
    pr_filename = "pr_squares.txt"
    processes = []
    for i in range(number_):
        processes.append(
            Process(
                target=worker, args=(values[i * step : (i + 1) * step], pr_filename)
            )
        )

    timer = time()
    [process.start() for process in processes]
    [process.join() for process in processes]
    [process.close() for process in processes]
    print(f"Done by {number_} processes: {round(time() - timer, 4)}")

    # 1 process
    timer = time()
    worker(values, "squares.txt")
    print(f"Done by 1 process: {round(time() - timer, 4)}")

    # pool processes
    pl_filename = "pl_squares.txt"
    pool_list = []
    pool_list = [
        (values[i * step : (i + 1) * step], pl_filename) for i in range(number_)
    ]

    timer = time()
    with Pool(number_) as pool:
        result = pool.starmap(worker, pool_list)
    print(f"Done by {number_} pool processes dummy: {round(time() - timer, 4)}")


# # concurrent # TODO or not TODO
#     pp_filename = 'pp_squares.txt'
#     # print('pp_filename: ', pp_filename)
#     conc_list = []
#     conc_list = [(values[i * step : (i + 1) * step]) for i in range(number_)]
#     timer = time()
#     with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
#         # print('pp_filename: ', pp_filename)
#         # result = executor.map(worker, conc_list, pp_filename)
#         for _, func in zip(conc_list, executor.map(worker, conc_list, pp_filename)):
#             # print('pp_filename: ', pp_filename)
#             func
#     print(f'Done by {number_} concurrent: {round(time() - timer, 4)}')
