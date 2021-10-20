import multiprocessing
import time
import sys


def daemon():
    name = multiprocessing.current_process().name
    print("starting : ", name)
    sys.stdout.flush()
    time.sleep(2)

    print("Exiting ", name)
    sys.stdout.flush()

def non_daemon():
    name = multiprocessing.current_process().name
    print("Starting, {}".format(name))
    print("Exiting : ", name)
    sys.stdout.flush()


if __name__ == "__main__":
    d = multiprocessing.Process(
        name="daemon",
        target=daemon,
    )
    d.daemon = True

    h = multiprocessing.Process(
        name="non_daemon",
        target=non_daemon,
    )
    d.daemon = False

    d.start()
    time.sleep(3)
    h.start()
    print("d_process:{}".format(h.is_alive()))
    h.join()
    # d.join()
