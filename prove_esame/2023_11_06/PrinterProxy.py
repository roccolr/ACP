from IPrinter import IPrinter
import socket


class PrinterProxy(IPrinter):

    def __init__(self, host:str ,port:int):
        self.host = host
        self.port = port

    def print(self, pathfile:str, tipo:str) -> None:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host,self.port))

        messagetosend = pathfile+'-'+tipo
        s.send(messagetosend.encode('utf-8'))
        

        print(f'[PROXY]\tinviato {messagetosend}')

        s.close()
    