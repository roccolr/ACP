from .funzioni.consumer import consumer
import threading

class ThreadConsumatore(threading.Thread):
    def __init__(self, q, free_space, message_ready, mutex_C, name):
        threading.Thread.__init__(self, name=name)
        self.q = q 
        # self.name = name 
        self.free_space = free_space
        self.message_ready = message_ready
        self.mutex_C = mutex_C
    
    def run(self):
        r = consumer(self.q, self.free_space, self.message_ready, self.mutex_C)
        print(f'[THREAD {self.name}] - Consumato valore {r}\n')