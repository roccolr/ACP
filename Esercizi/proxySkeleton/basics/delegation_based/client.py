from interface import Subject
import sys, logging, socket

logging.basicConfig(level=logging.DEBUG, format= '[%(threadName)-0s]%(message)s')

class Proxy(Subject):
    def __init__(self, port):
        self.port = port

    def request(self, data):
        IP = 'localhost'
        PORT = self.port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        logging.debug('\t\t\tstabilita connessione con %s:%d', IP, PORT)
        s.send(data.encode('utf-8'))
        logging.debug('\t\t\tinviato: %s', data)
        msg = s.recv(1024)
        logging.debug('\t\t\tricevuto: %s', msg.decode('utf-8'))
        s.close()
        logging.debug('\t\t\tconnessione chiusa')


if __name__ == '__main__':
    try:
        PORT = int(sys.argv[1])
        MESSAGE = sys.argv[2]
    except IndexError:
        logging.debug('\t\t\tSPECIFICARE PORTO E MESSAGGIO...')
    
    proxy = Proxy(PORT)
    proxy.request(MESSAGE)

