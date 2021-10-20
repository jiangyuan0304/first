import logging
import multiprocessing
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(process)d]  - %(message)s'
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


if __name__ == "__main__":
    e = multiprocessing.Event()

    t = multiprocessing.Process(
        target=monkey,
        name="monkey",
        args=(e,)
    )
    t.start()

    k = multiprocessing.Process(
        target=autotest,
        name="aiqiyi-test",
        args=(e,)

    )
    k.start()



