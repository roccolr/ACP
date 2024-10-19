from DispatcherSkeleton import DispatcherSkeleton
import multiprocessing

class RealDispatcher(DispatcherSkeleton):
    def __init__(self, q: multiprocessing.Queue):
        self.q = q
    
    def deposita(self, value:int)->None:
        self.q.put(value)
        print(f'[SERVER]\tinserito valore {value}')

    
    def preleva(self) ->int:
        res = self.q.get()
        print(f'[SERVER]\tprelevato valore {res}')
        return res