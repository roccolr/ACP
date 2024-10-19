from IPrinter import IPrinter
import socket, multiprocessing
from abc import ABC, abstractmethod

def worker(remote_socket:socket.socket, skeleton):
    received = remote_socket.recv(1024).decode('utf-8')

    pathfile = received.split('-')[0]
    tipo = received.split('-')[1]

    print(f'[{multiprocessing.current_process()._name}]\tricevuti parametri pathfile:{pathfile}, tipo:{tipo}')

    skeleton.print(pathfile, tipo)

    print(f'[{multiprocessing.current_process()._name}]\tinvocato print()')




class PrinterSkeleton(IPrinter, ABC):

    def __init__(self, port):
        self.port = port
    
    def print(self, pathfile:str, tipo:str) -> None:
        pass

    def run_skeleton(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1',self.port))
        s.listen()
        print(f'[SERVER SKELETON]\tin attesa sul porto {self.port}')

        i = 0
        while True:
            (remote_socket, addr) = s.accept()
            w = multiprocessing.Process(name='WORKER-'+str(i), target=worker, args=(remote_socket, self))
            w.start()
            i+=1

        s.close()