import IService
import socket

class ProxyService(IService.IService):
    def log(self, messaggioLog:str, tipo:int):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # socket.bind('127.0.0.1:0')
        sock.connect(('127.0.0.1',6969))

        msg = messaggioLog+'#'+str(tipo)
        sock.send(msg.encode('utf-8'))

        sock.close()
