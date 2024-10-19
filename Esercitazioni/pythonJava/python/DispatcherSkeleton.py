from IDispatcher import IDispatcher
from abc import ABC
import socket, multiprocessing


def Worker(remoteSocket:socket.socket, skeleton):
    msg = remoteSocket.recv(1024).decode()

    splitted_msg = msg.split('-')

    if('deposita' in msg):
        skeleton.deposita(int(splitted_msg[1]))
    elif('preleva' in msg):
        res = str(skeleton.preleva())
        remoteSocket.send((res+"\n").encode())
    else:
        print('[SERVER]\t richiesta non riconosciuta')

    remoteSocket.close()

class DispatcherSkeleton(IDispatcher, ABC):
    #port 6969
    def run_skeleton(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 6969))
        s.listen()

        while(True):
            (remoteSocket, addr) = s.accept()
            worker = multiprocessing.Process(target=Worker, args=(remoteSocket, self))
            worker.start()
        
