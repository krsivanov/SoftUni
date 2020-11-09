class Worker:

    def work(self):
        print("I'm working!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        # this ->
        # if isinstance(worker,Worker):
        #     self.worker = worker
        # else:
        #     raise AssertionError('`worker` must be of type {}'.format(Worker))
        # equal to this ->
        # assert isinstance(worker, Worker), '`worker` must be of type {}'.format(Worker)

        if "Worker" in [e.__name__ for e in worker.__class__.__mro__]:
            self.worker = worker
        else:
            raise AssertionError('`worker` must be of type {}'.format(Worker))

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(Worker):

    def work(self):
        print("I work very hard!!!")


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
except AssertionError:
    print("manager fails to support super_worker....")
