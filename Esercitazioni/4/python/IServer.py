from abc import ABC, abstractmethod

class IServer(ABC):
    @abstractmethod
    def deposita(self,val):
        pass
    
    @abstractmethod
    def preleva(self)->int:
        pass