import threading 

class Coda:
    def __init__(self, dim):
        self.dim = dim
        # self.lock = threading.Lock()
        self.cv_consumatore = threading.Condition()
        self.cv_produttore = threading.Condition()
        self.data = []
    
    def is_empty(self)->bool:
        if (len(self.data)==0):
            return True
        else:
            return False
    
    def is_full(self)->bool:
        if (len(self.data) == self.dim):
            return True
        else:
            return False
    
    def put(self, val):
        with self.cv_produttore:
            
            while(self.is_full()):
                print('coda_piena')
                self.cv_produttore.wait()
            self.data.append(val)

            self.cv_consumatore.notify()

    
    def get(self)->int:
        with self.cv_consumatore:

            while(self.is_empty()):
                print('coda_vuota')
                self.cv_consumatore.wait()
            
            res = self.data.pop(0)

            self.cv_produttore.notify()
            
        return res
    
