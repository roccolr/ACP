from interface import Subject
import sys, logging, socket

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)-0s]%(message)s')

class Proxy(Subject):
    def __init__(self, port):
        self.port = port
    
    def request(self, data):
        msg = data.encode('utf-8')
        IP = 'localhost'
        PORT = self.port
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
        s.send(msg)
        msg = s.recv(1024)
        msg = msg.decode('utf-8')
        logging.debug('\t\t\tmessaggio ricevuto: %s', msg)

        s.close()


if __name__ == '__main__':
    try:
        PORT = int(sys.argv[1])
        MESSAGE = sys.argv[2]
    except IndexError:
        logging.debug('\t\t\tPlease specify PORT and MESSAGE argument')
    
    proxy = Proxy(PORT)
    proxy.request(MESSAGE)