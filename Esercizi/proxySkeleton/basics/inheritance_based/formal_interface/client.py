from interface import Subject
import socket, sys

'''
implementiamo lato client l'interfaccia Subject
'''

class Proxy(Subject):
    def __init__(self, port):
        self.port = port

    def request(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IP = 'localhost'
        PORT = self.port
        BUFFSIZE = 1024
        s.connect((IP, PORT))

        print(f'[PROXY]\t\t\tConnesso su {IP}:{PORT}')
        s.send(msg.encode('utf-8'))
        print(f'[PROXY]\t\t\tinviato messaggio {msg}')

        msg = s.recv(BUFFSIZE)
        # print(f'[PROXY]\t\t\tConnesso su {IP}:{PORT}')
        print(f'[PROXY]\t\t\tricevuto messaggio {msg}')

        s.close()

if __name__ == '__main__':
    '''
    ricevo da linea di comando porto [1], messaggio [2] come stringhe
    '''
    try:
        port = int(sys.argv[1])
        msg = sys.argv[2]
    except IndexError:
        print('Per favore specificare argomenti da linea di comando...')
    
    proxy = Proxy(port)
    proxy.request(msg)
    


