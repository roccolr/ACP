from abc import ABC, abstractmethod

'''
Definizione di un interfaccia 
'''

class Subject(ABC):
    
    @abstractmethod
    def request(self, data):
        pass


