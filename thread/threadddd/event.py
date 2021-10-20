import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(threadName)s] - %(message)s'
)

def wait_for_event(e):
    logging.debug("waiting for event starting")
    logging.debug("event set:{}".format(e.wait()))


def wait_for_time_out(e, t):
    while not e.is_set():
        logging.debug("wait for event timeout starting")
        event_status = e.wait(t)
        logging.debug("event set :{}".format(event_status))
        if event_status:
            logging.debug("processing event")
        else:
            logging.debug("doing other work")


e = threading.Event()
t = threading.Thread(
    target=wait_for_event,
    name="service1",
    args=(e,)
)
t.start()

k = threading.Thread(
    target=wait_for_time_out,
    name="service_time_out",
    args=(e, 2)

)
k.start()


logging.debug("wait event set")
time.sleep(2.1)
e.set()
logging.debug("event is set")

