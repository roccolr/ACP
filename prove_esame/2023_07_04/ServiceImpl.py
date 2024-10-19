from ServiceSkeleton import ServiceSkeleton
import multiprocessing


class ServiceImpl(ServiceSkeleton):

    def __init__(self, queue: multiprocessing.Queue):
        self.queue = queue

    def log(self, messaggioLog, tipo):
        item = messaggioLog+'-'+str(tipo)
        self.queue.put(item)

        