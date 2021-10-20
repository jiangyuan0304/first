import  logging
import threading
import time


logging.basicConfig(
    level=logging.DEBUG,
    # format='[%(threadName)s] - %(message)s'
    format='进程：%(process)d 线程：[%(thread)d] - %(message)s'
)


def consumer(cond, name):
    logging.debug("[{}] waiting [release version]".format(name))
    with cond:
        cond.wait()
        logging.debug(" [{}] starting version check!!".format(name))

def producer(cond, name):
    logging.debug("starting produce thread ")
    with cond:
        logging.debug("[{}] makeing [release version]".format(name))
        time.sleep(2)
        cond.notifyAll()


cond = threading.Condition()

t1 = threading.Thread(target=consumer, name="C1", args=(cond, "小辉"))
t2 = threading.Thread(target=consumer, name="C2", args=(cond, "小明"))
p2 = threading.Thread(target=producer, name="p2", args=(cond, "小龙"))

t1.start()
time.sleep(2)
t2.start()
time.sleep(3)
p2.start()
