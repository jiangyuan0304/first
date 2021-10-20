import logging
import threading
import time
import random

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(thread)d] [%(threadName)s] - %(message)s'
)

def worker():
    pause = random.randint(1, 5) / 10
    logging.debug("sleeping {}".format(pause))
    time.sleep(pause)
    logging.debug("ending")


for i in range(3):
    t = threading.Thread(target=worker)
    t.start()

print(threading.enumerate())
# main_thread = threading.main_thread()
# for t in threading.enumerate():
#     if t is main_thread:
#         continue
#     logging.debug("joining {}".format(t.getName()))
#     t.join()