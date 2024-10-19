from IMagazzino import IMagazzino
import socket, threading

class ProxyMagazzino(IMagazzino):
    
    def deposita(self, articolo:str , id:int)->None:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('127.0.0.1', 6969))
        msg = articolo + '-' + str(id)
        s.send(msg.encode())
        s.close()
        print(f'[{threading.current_thread().getName()}]\t[CLIENT] - inviata stringa: {msg}')
    
    def preleva(self, articolo:str) ->int:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('127.0.0.1', 6969))
        msg = articolo
        s.send(msg.encode())
        msg = s.recv(1024).decode()
        s.close()
        return int(msg)