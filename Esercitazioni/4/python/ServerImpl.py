from ServerSkeleton import ServerSkeleton
import multiprocessing

class ServerImpl(ServerSkeleton):
    def __init__(self, queue:multiprocessing.Queue):
        self.queue = queue
    

    def deposita(self,val):
        self.queue.put(val)
    

    def preleva(self)->int:
        return self.queue.get()