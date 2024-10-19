from abc import ABC 
from IServer import IServer
import socket, multiprocessing

def worker(skeleton, remote_socket:socket.socket):
    msg = remote_socket.recv(1024).decode()
    msg_s = msg.split('-')
    print(f'[SERVER]\tricevuta richiesta: {msg}')
    risposta = "Errore"
    if("preleva" in msg):
        risposta = str(skeleton.preleva())+"\n"
        remote_socket.send(risposta.encode())
    elif("deposita" in msg):
        skeleton.deposita(int(msg_s[1]))
    remote_socket.close()


class ServerSkeleton(IServer, ABC):
    def run_skeleton(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 6969))
        s.listen()
        print('[SERVER]\tserver listening on: 6969')

        while(True):
            (remote_socket, addr) = s.accept()
            p = multiprocessing.Process(target=worker, args=(self, remote_socket))
            p.start()
