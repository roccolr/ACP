import stomp, sys, random,time

class ResponseListener(stomp.ConnectionListener):
    def on_message(self, frame:stomp.utils.Frame):
        msg = frame.body
        print(f'[CLIENT]\tricevuto: {msg}')

if __name__ == '__main__':
    dict_tipo = {0:'deposita', 1:'preleva'}
    n_messaggi=0
    try:
        n_messaggi = int(sys.argv[1])
    except IndexError:
        print('[CLIENT]\tindicare parametri')

    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True, headers={"client-id":"client1"})
    conn.set_listener('responseListener', ResponseListener())

    for i in range(0,n_messaggi):
        tipo = dict_tipo[random.randint(0,1)]
        # tipo = 'deposita'
        id = random.randint(1,100)
        conn.send('/queue/richiesta', tipo+'-'+str(id))
        print(f'[CLIENT]\tinviata richiesta {tipo+"-"+str(id)}')
    
    # conn.subscribe('/queue/risposta', id=1, ack='auto', persistent = True, headers={"activemq.subscriptionName":"durableClientListener"})
    conn.subscribe('/queue/risposta', id=1)
    print('debug')

    try:
        time.sleep(5)
    except KeyboardInterrupt:
        print('[CLIENT]\tinterrotto manualmente')
    finally:
        conn.disconnect()


