import threading
import time


class RecordPool():
    def __init__(self):
        self.pool = list()
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.pool.append(name)
            print("{} is running".format(self.pool))

    def inActive(self, name):
        with self.lock:
            self.pool.remove(name)
            print("{} is remove".format(name))

# def worker(sem, name):
#     with sem:
#         name = threading.current_thread().getName()
#         print("{} is working".format(name))
#         time.sleep(2)

def worker(s, pool):
    with s:
        name = threading.current_thread().name
        pool.makeActive(name)
        time.sleep(2)
        pool.inActive(name)

pool = RecordPool()
s = threading.Semaphore(3)
threads = list()
for i in range(10):
    t = threading.Thread(target=worker,
                         args=(s, pool),
                         name=str(i))
    threads.append(t)
    t.start()

