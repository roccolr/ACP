import IService, socket, multiprocessing
from abc import ABC, abstractmethod

def Worker(remote_socket:socket.socket, skeleton):
    print('['+multiprocessing.current_process().name+']\tinvocato')
    msg = remote_socket.recv(1024).decode('utf-8')
    msg_splitted = msg.split('#')
    messaggioLog = msg_splitted[0]
    tipo = int(msg_splitted[1])
    skeleton.log(messaggioLog, tipo)

    remote_socket.close()
    print('['+multiprocessing.current_process().name+']\tterminato')


class ServiceSkeleton(IService.IService, ABC):

    @abstractmethod
    def log(self, messaggioLog, tipo):
        pass

    def run_skeleton(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind(('127.0.0.1', 6969))
        server_socket.listen()
        print(f'[SERVER]\tlistening on 127.0.0.1:6969')
        i = 0
        while(True):
            (remote_socket, address) = server_socket.accept()
            w = multiprocessing.Process(name='PROCESSO_'+str(i), target=Worker, args=(remote_socket, self))
            w.start()
            i+=1