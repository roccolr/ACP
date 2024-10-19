import stomp, sys, time

class myListener(stomp.ConnectionListener):

    def __init__(self, tipo_stampante):
        self.tipo_stampante = tipo_stampante
    
    def on_message(self, frame:stomp.connect.Frame):
        message = frame.body
        print('[BW_PRINTER]\tricevuto messaggio: '+message)

        if(message.split('-')[1] == self.tipo_stampante):
            with open('/home/studente/Desktop/acp/prove_esame/2023_11_06/files/bw.txt', 'a') as file:
                file.write(message+'\n')
                print(f'[BW_PRINTER]\tmyType: {self.tipo_stampante}, scritto messaggio: {message}')
        

if __name__ == '__main__':
    try:
        tipo_stampante = sys.argv[1]
    except IndexError:
        print('specificare tipo_stampante')
    
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener('BWPrinter', myListener(tipo_stampante=tipo_stampante))
    conn.connect(wait=True)

    conn.subscribe('/topic/bw', id=1)

    

    try:
        while(True):
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('[INTERROTTO DA TASTIERA]')

    



