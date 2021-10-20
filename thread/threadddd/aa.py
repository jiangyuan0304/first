import threading
import time
import sys

def worker():
    time.sleep(2)
    # print(threading.current_thread().name)
    print(threading.current_thread().getName())
    sys.stdout.flush()


def spend_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))

    return wrapper

# @showtime
# def five_worker():
#     for i in range(5):
#         worker()

@spend_time
def five_worker():
    threads = []
    for i in range(5):
            t = threading.Thread(target=worker)
            threads.append(t)
            t.start()

    for k in threads:
        k.join()
five_worker()