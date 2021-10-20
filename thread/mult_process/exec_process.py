import multiprocessing
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='进程：%(process)d 线程：[%(thread)d] - %(message)s'
)

def worker():
    logging.debug("worker {}".format(
        # multiprocessing.Process.name
        multiprocessing.current_process().name))
    time.sleep(1)


if __name__ == "__main__":
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(name=str(i), target=worker )
        jobs.append(p)
        p.start()