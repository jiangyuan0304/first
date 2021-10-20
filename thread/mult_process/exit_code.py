import sys
import multiprocessing
import logging
def aa():
    print(aa)
    sys.stdout.flush()


# print(aa.__name__)
if __name__ == "__main__":
    multiprocessing.log_to_stderr(logging.INFO)
    d = multiprocessing.Process(target=aa)
    d.start()
    d.join()