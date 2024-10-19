import threading
from .funzioni.producer import producer

class ThreadProduttore(threading.Thread):
    def __init__(self, free_space, message_ready, mutex_P, q, name):
        threading.Thread.__init__(self, name=name)
        self.free_space = free_space
        self.message_ready = message_ready
        self.mutex_P = mutex_P
        self.q = q
        # self.name = name

    def run(self):
        r = producer(self.q, self.free_space, self.message_ready, self.mutex_P)
        print(f'[THREAD {self.name}] - prodotto valore {r}\n')

