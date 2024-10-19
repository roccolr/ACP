from IMagazzino import IMagazzino
import socket

class MagazzinoProxy(IMagazzino):

    def deposita(self, value:int)->str:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1',6969))

        s.send(("deposita-"+str(value)).encode())
        res = s.recv(1024).decode()
        # ritorna deposited se il deposito ha successo
        return res
    
    def preleva(self, value:int)->int:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1',6969))

        # s.send(str(value).encode())
        s.send(("preleva-"+str(value)).encode())

        res = s.recv(1024).decode()
        # ritorna ID dell'elemento prelevato -> int
        return res