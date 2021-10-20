import logging
import random
import time
import threading

logging.basicConfig(
    level=logging.DEBUG,
    # format='[%(threadName)s] - %(message)s'
    format='进程：%(process)d 线程：[%(thread)d] - %(message)s'
)

class Counter():
    def __init__(self, start = 0):
        self.lock = threading.Lock()
        self.value = start

    def increament(self):
        logging.debug("waiting for lock")
        self.lock.acquire()
        try:
            logging.debug("acquired lock")
            self.value += 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.randint(1,4)
        logging.debug("sleeping {}".format(pause))
        time.sleep(pause)
        c.increament()
    logging.debug("Done")

count = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(count, ))
    t.start()

main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()

logging.debug('Counter {}'.format(count.value))

logging.debug("waiting for worker threads")
# 主线程用于执行 当前代码程序段

