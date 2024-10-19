from abc import ABC, abstractmethod
from IMagazzino import IMagazzino
import multiprocessing, socket

def Worker(skeleton, remote_socket: socket.socket):
    msg = remote_socket.recv(1024).decode()
    print(f'[{multiprocessing.current_process().name}]\tricevuta richiesta: {msg}')

    s_msg = msg.split('-')
    res = ''
    if (s_msg[0] == 'deposita'):
        res = skeleton.deposita(int(s_msg[1]))

    elif(s_msg[0] == 'preleva'):
        res = skeleton.preleva(int(s_msg[1]))
    else:
        print(f'[{multiprocessing.current_process().name}]\tOperazione non supportata')

    remote_socket.send(res.encode())
    print(f'[{multiprocessing.current_process().name}]\tinviata risposta: {res}')
            

class MagazzinoSkeleton(IMagazzino, ABC):
    
    def run_skeleton(self):
        print('[SERVER]\trunning on localhost:6969')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind(('127.0.0.1', 6969))
        s.listen()

        i = 0
        while(True):
            (remote_socket, addr) = s.accept()
            p = multiprocessing.Process(name= 'PROCESS_'+str(i), target=Worker, args=(self, remote_socket))
            p.start()
            i+=1