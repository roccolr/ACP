from interface import Subject
import sys, logging, threading, socket

logging.basicConfig(level=logging.DEBUG, format= '[%(threadName)-0s]%(message)s')


def worker(c:socket.socket, self):
    logging.debug('\t\t\tinizio')
    
    data = c.recv(1024)
    msg = data.decode('utf-8')
    logging.debug('\t\t\tricevuto messaggio: %s', msg)
    logging.debug('\t\t\telaborazione...')

    msg = self.request(msg)
    c.send(msg.encode('utf-8'))
    logging.debug('\t\t\tinviato messaggio: [%s]', msg)
    c.close()
    logging.debug('\t\t\tconnessione chiusa')


class Skeleton(Subject):
    def __init__(self, port, subject):
        self.port= port
        self.subject = subject

    def request(self, data):
        return (self.subject.request(data))
    
    def run_skeleton(self):
        IP = 'localhost'
        PORT = self.port
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((IP, PORT))
        logging.debug('\t\t\tistanziata socket su %s:%d', IP, PORT)

        logging.debug('\t\t\tin ascolto...')
        s.listen()

        i = 0
        while True:
            (c, a) = s.accept()
            t = threading.Thread(name= 'Thread '+str(i), target=worker, args=(c, self))
            t.start()
            i+=1
        

class RealSubject(Subject):
    def request(self, data):
        '''
        data è già una stringa
        '''

        return data[::-1]

if __name__ == '__main__':
    try:
        IP = 'localhost'
        PORT = int(sys.argv[1])
    except IndexError:
        logging.debug('\t\t\tSPECIFICARE PORTO')
    
    realSubject = RealSubject()
    skeleton = Skeleton(PORT, realSubject)
    skeleton.run_skeleton()
