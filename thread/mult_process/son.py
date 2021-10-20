import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        print(self.name)
        return



if __name__ == "__main__":
    jobs = []
    for i in range(3):
        p = Worker()
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()
