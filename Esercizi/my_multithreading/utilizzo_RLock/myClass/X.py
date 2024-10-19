import threading

class X(object):
    def __init__(self):
        self.a = 1
        self.b = 1
        self.lock = threading.RLock()
    
    def modifyA(self):
        with self.lock:
            self.a += 1

    def modifyB(self):
        with self.lock:
            self.b += self.a
    
    def modifyA_and_B(self):
        with self.lock:
            self.modifyA()
            self.modifyB()


