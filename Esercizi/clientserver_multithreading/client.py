import socket
import sys

'''
da linea di comando viene passato un porto [1] e una stringa [2]
'''

if __name__ == '__main__':
    porto = int(sys.argv[1])
    msg = sys.argv[2]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', porto))

    print(f'[client] - connesso a: localhost:{porto}')

    s.send(msg.encode('utf-8'))
    msg = s.recv(1024)
    print('[client] - messaggio ricevuto: '+msg.decode('utf-8'))
    s.close()