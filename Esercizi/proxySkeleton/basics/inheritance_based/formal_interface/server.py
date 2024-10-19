from interface import Subject
import socket, sys
from abc import ABC, abstractmethod
import threading

def worker(c:socket.socket, a: tuple, self)->None:
    data = c.recv(1024)
    msg = data.decode('utf-8')
    print(f'[{threading.current_thread().name}]\t\t\tricevuto: {msg} da {a[0]}:{a[1]}')
    print(f'[{threading.current_thread().name}]\t\t\tinizio elaborazione')

    msg = self.request(msg)

    c.send(msg.encode('utf-8'))
    print(f'[{threading.current_thread().name}]\t\t\tinviato: {msg} a {a[0]}:{a[1]}')

    c.close()



class Skeleton(Subject, ABC):
    '''
    classe astratta che implementa l'aspetto comunicativo del Server, liberando la parte di
    business logic dall'onere di gestire una connessione.
    '''

    def __init__(self, port):
        self.port = port

    @abstractmethod
    def request(self, data:str)->str:
        pass

    def run_skeleton(self):
        IP = 'localhost'
        
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((IP, self.port))

        s.listen(5)
        print(f'[SKELETON]\t\t\tin ascolto su {IP}:{self.port}')

        i = 0
        while True:
            (conn, addr) = s.accept()
            print(f'[SKELETON]\t\t\taccettata connessione {addr[0]}:{addr[1]}')

            # invochiamo un thread per gestire la richiesta
            t = threading.Thread(name= 'Thread '+str(i), target=worker, args=(conn, addr, self))
            t.start()
            i+=1
        
class RealSubject(Skeleton):
    '''
    classe che 'materializza' skeleton, implementando il metodo request() ovvero il servizio effettivamente richiesto
    '''

    def request(self, data:str)->str:
        return (data[::-1])
    
if __name__ == '__main__':
    try:
        PORT = int(sys.argv[1])
    except IndexError:
        print('per favore specifica il porto da linea di comando')
    
    realSubject = RealSubject(PORT)
    realSubject.run_skeleton()    
        
