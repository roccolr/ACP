from abc import ABC, abstractmethod

class IDispatcher(ABC):
    @abstractmethod
    def deposita(self, value:int)->None:
        pass

    @abstractmethod
    def preleva(self) ->int:
        pass