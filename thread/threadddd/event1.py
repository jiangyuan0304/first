import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(threadName)s] - %(message)s'
)

def monkey(e):
    logging.debug("waiting for event starting")
    event_is_set = e.wait()
    logging.debug("event status is {},\
                  then start monkey work".format(event_is_set))

def autotest(e):
    logging.debug("start autotest task")
    time.sleep(5)
    e.set()
    logging.debug("autotest task ending")

e = threading.Event()

t = threading.Thread(
    target=monkey,
    name="monkey",
    args=(e,)
)
t.start()

k = threading.Thread(
    target=autotest,
    name="aiqiyi-test",
    args=(e,)

)
k.start()



