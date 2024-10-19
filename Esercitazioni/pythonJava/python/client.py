import stomp, time

class myListener(stomp.ConnectionListener):
    def on_message(self, frame: stomp.utils.Frame):
        msg = frame.body
        print(f'[PYTHON CLIENT]\t ricevuto messaggio: {msg}')




if __name__ == '__main__':
    numero_messaggi = 10

    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False) #traccia di interoperabilità
    conn.connect(wait=True)

    print("[PYTHON CLIENT]\tConnesso al message broker")


    for i in range(0,numero_messaggi):
        #se i è pari, inviamo un messaggio di tipo deposita: 'deposita-intero'
        #se i è dispari, inviamo un messaggio di tipo preleva: 'preleva'

        if (i%2 == 0):
            conn.send('/queue/richiesta', 'deposita-'+str(i), headers={'reply-to':'/queue/risposta'})
        else:
            conn.send('/queue/richiesta', 'preleva', headers={'reply-to':'/queue/risposta'})
        
        # l'header reply-to sarà utilizzato dall'applicazione JAVA per inizializzare una Coda di risposta

    print('[PYTHON CLIENT]\tRichieste inoltrate al message broker con successo')

    # a questo punto, il client si mette in attesa asincrona sulla coda /queue/risposta
    conn.subscribe('/queue/risposta', id=1, ack='auto')
    conn.set_listener('risposta_listener', myListener())

    while(True):
        time.sleep(1)

    conn.disconnect()
    