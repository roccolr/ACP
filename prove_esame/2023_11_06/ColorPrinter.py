import stomp, sys, time

class myListener(stomp.ConnectionListener):

    def __init__(self, tipo_estensione):
        self.tipo_estensione = tipo_estensione
    
    def on_message(self, frame:stomp.connect.Frame):
        message = frame.body
        print('[COLOR_PRINTER]\tricevuto messaggio: '+message)
        splitted_message_dot = message.split('.')
        ext = splitted_message_dot[1].split('-')[0]
        if(ext == tipo_estensione):
            with open('/home/studente/Desktop/acp/prove_esame/2023_11_06/files/color.txt', 'a') as file:
                file.write(message+'\n')
                print(f'[COLOR_PRINTER]\tmyType: {self.tipo_estensione}, scritto messaggio: {message}')
        

if __name__ == '__main__':
    try:
        tipo_estensione = sys.argv[1]
    except IndexError:
        print('specificare tipo_estensione')
    
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener('ColorPrinter', myListener(tipo_estensione=tipo_estensione))
    conn.connect(wait=True)
    conn.subscribe('/topic/color', id=2)

    try:
        while(True):
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('[INTERROTTO DA TASTIERA]')

    



