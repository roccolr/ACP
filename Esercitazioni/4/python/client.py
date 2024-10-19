import stomp, random, time

class ResponseListener(stomp.ConnectionListener):
    def on_message(self, frame:stomp.utils.Frame):
        risposta = frame.body
        print(f'[CLIENT]\tricevuta risposta {risposta}')
        

if __name__ == '__main__':
    tipi_richiesta = {0:'deposita', 1:'preleva'}
    num_richieste = 10
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False) #interoperabilità
    conn.connect(wait=True)
    conn.set_listener('response_listener', ResponseListener())
    conn.subscribe('/queue/risposta', id=1)

    for i in range(0,num_richieste):
        tipo_richiesta = tipi_richiesta[random.randint(0,1)]
        id_articolo = random.randint(0,1000)
        msg = tipo_richiesta+'-'+str(id_articolo)
        conn.send('/queue/richiesta', msg ,headers={'reply-to':'/queue/risposta'})
        print(f'[CLIENT]\tinviata richiesta {msg}')
    
    try:
        time.sleep(3)
    except KeyboardInterrupt:
        print('[CLIENT]\tinterrotto manualmente')


