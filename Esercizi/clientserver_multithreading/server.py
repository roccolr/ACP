import socket 
import threading
import logging 

logging.basicConfig(level=logging.DEBUG, format= '[%(threadName)-0s]%(message)s')
BUFFSIZE = 1024
LOCAL_IP = 'localhost'


class WorkerThread(threading.Thread):
    def __init__(self, c : socket.socket, addr : tuple, nome : str):
        threading.Thread.__init__(self, name=nome)
        self.c = c
        self.addr = addr
    
    def run(self):
        logging.debug('\t\t\tInizio')
        msg = self.c.recv(BUFFSIZE)
        logging.debug('\t\t\tricevuto messaggio: %s da %s : %d', msg.decode('utf-8'), self.addr[0], self.addr[1])
        msg = f'risposta - {self.name}'.encode('utf-8')
        self.c.send(msg)
    

if __name__ == '__main__':
    logging.debug('\t\t\tcreazione socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((LOCAL_IP, 0))
    logging.debug('\t\t\tin ascolto sul porto: %d', s.getsockname()[1])
    s.listen(5)

    i = 0
    while 1:
        (c, a) = s.accept()
        logging.debug('\t\t\taccettata connessione con %s:%d', a[0], a[1])
        logging.debug('\t\t\tpassando dati al thread')
        t = WorkerThread(c, a, 'Thread '+str(i))
        t.start()
        i+=1
    
    s.close()