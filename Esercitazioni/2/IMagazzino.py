from abc import ABC, abstractmethod

class IMagazzino(ABC):
    @abstractmethod
    def deposita(self, value:int)->str:
        pass
    
    @abstractmethod
    def preleva(self, value:int)->int:
        pass
