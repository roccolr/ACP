from abc import ABC, abstractmethod

class IService(ABC):
    @abstractmethod
    def log(self, messaggioLog, tipo):
        pass
