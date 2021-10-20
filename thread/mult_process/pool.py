import multiprocessing

def cala(data):
    return data ** 2


def start_process():
    print("starting {}".format(multiprocessing.current_process().name))

if __name__ == "__main__":
    pool_size = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
    )

    pool_output = pool.map(cala, list(range(10)))
    pool.close()
    pool.join()
    print(pool_output)
