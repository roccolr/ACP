from MagazzinoSkeleton import MagazzinoSkeleton
import multiprocessing

class MagazzinoImpl(MagazzinoSkeleton):
    def __init__(self,queue:multiprocessing.Queue, cv_consumatore, cv_produttore):
        self.queue = queue
        self.cv_cons = cv_consumatore
        self.cv_prod = cv_produttore
    
    def deposita(self, value:int)->str:
        # with self.cv_prod:
        #     while(self.queue.full()):
        #         self.cv_prod.wait()

        #     self.queue.put(value)
        #     self.cv_cons.notify()
        self.queue.put(value)
        return 'deposited'
    
    
    def preleva(self, value:int)->int:
        # res = ''
        # with self.cv_cons:
        #     while(self.queue.empty()):
        #         self.cv_cons.wait()
        # res = self.queue.get()
        # self.cv_prod.notify()    
        res = self.queue.get()

        return str(res)

    