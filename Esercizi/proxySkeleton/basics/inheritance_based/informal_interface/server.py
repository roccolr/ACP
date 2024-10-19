from interface import Subject
import threading, socket, logging, sys

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)-0s]%(message)s')

def worker(c: socket.socket, self)->None:
    data = c.recv(1024)
    msg = data.decode('utf-8')
    logging.debug('\t\t\tricevuto messaggio: %s', msg)

    logging.debug('\t\t\tinizio elaborazione')
    msg = self.request(msg)

    c.send(msg.encode('utf-8'))
    logging.debug('\t\t\tinviato messaggio: %s', msg)

    c.close()


class Skeleton(Subject):
    def __init__(self, port):
        self.port = port
    
    def request(self, data):
        pass

    def run_skeleton(self):
        IP = 'localhost'
        PORT = self.port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((IP, PORT))

        s.listen()
        
        i = 0
        while True:
            (conn, add) = s.accept()
            t = threading.Thread(name= 'THREAD '+str(i), target=worker, args=(conn, self))
            t.start()
            i+=1
        s.close()

class RealSubject(Skeleton):
    def request(self, data):
        return data[::-1]

if __name__ == '__main__':
    try:
        IP = 'localhost'
        PORT = int(sys.argv[1])
    except IndexError:
        logging.debug('\t\t\tSpecify a PORT parameter')
    
    realSubject = RealSubject(PORT)
    realSubject.run_skeleton()