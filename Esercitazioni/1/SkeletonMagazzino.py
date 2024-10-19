from IMagazzino import IMagazzino
from SkeletonImpl import SkeletonImpl
import socket, threading

def worker(skeleton, conn:socket.socket):
    msg = conn.recv(1024).decode()
    splitted_msg = msg.split('-')

    if(len(splitted_msg)>1):
        print(f'[{threading.current_thread().getName()}]\t[SERVER] - Ricevuta richiesta di deposito')
        skeleton.deposita(splitted_msg[0], int(splitted_msg[1]))
        print(f'[{threading.current_thread().getName()}]\t[SERVER] - Deposito avvenuto con successo')
    elif(len(splitted_msg)==1):
        print(f'[{threading.current_thread().getName()}]\t[SERVER] - Ricevuta richiesta di prelievo')
        res = skeleton.preleva(splitted_msg[0])
        print(f'[{threading.current_thread().getName()}]\t[SERVER] - Prelievo avvenuto con successo id:{res}')
        conn.send(str(res).encode())
        print(f'[{threading.current_thread().getName()}]\t[SERVER] - Inviata risposta')

    else:
        print(f'[{threading.current_thread().getName()}]\t[SERVER] - Errore nel marshalling dei parametri')
        

class MagazzinoSkeleton(IMagazzino):
    def __init__(self, skeleton:SkeletonImpl):
        self.skeleton = skeleton
    
    def deposita(self, articolo:str , id:int)->None:
            self.skeleton.deposita(articolo, id)
            
    def preleva(self, articolo:str) ->int:
        return self.skeleton.preleva(articolo)

    def run_skeleton(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('127.0.0.1', 6969))
            s.listen()
            i = 0
            while(True):
                (conn, addr) = s.accept()
                t = threading.Thread(name='WORKER_SERVER '+str(i), target=worker, args=(self, conn))
                t.start()
                i+=1
        except KeyboardInterrupt:
            print('[SERVER]\tinterrotto manualmente')
        
        
            
