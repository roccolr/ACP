from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print(self, pathfile:str, tipo:str) -> None:
        pass