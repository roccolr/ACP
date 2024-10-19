from MagazzinoProxy import MagazzinoProxy
import stomp, multiprocessing

def worker(proxy:MagazzinoProxy, conn:stomp.Connection, msg:str):
    s_msg = msg.split('-')
    res = ''
    if(s_msg[0]=='deposita'):
        res = proxy.deposita(int(s_msg[1]))
    elif(s_msg[0]=='preleva'):
        res = proxy.preleva(int(s_msg[1]))
    else:
        res = 'error'
    conn.send('/queue/risposta', res)
    print(f'[DISPATCHER]\tinviato messaggio sulla coda di risposta {res}')


class DispatcherListener(stomp.ConnectionListener):
    def __init__(self, proxy:MagazzinoProxy, conn:stomp.Connection):
        self.proxy = proxy
        self.conn = conn

    def on_message(self,frame:stomp.utils.Frame):
        msg = frame.body
        print(f'[DISPATCHER]\tricevuto messaggio: {msg}')
        p = multiprocessing.Process(target=worker, args=(self.proxy, self.conn, msg))
        p.start()

if __name__ == '__main__':
    proxy = MagazzinoProxy()
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.set_listener('dispatcher_listener', DispatcherListener(proxy=proxy, conn=conn))

    conn.connect(wait=True, headers={"client-id":"dispatcher1"})
    # conn.subscribe('/queue/richiesta', id=1, headers={"activemq.subscriptionName":"dispatcherDurable"}, persistent=True)
    conn.subscribe('/queue/richiesta', id=1)
    print('debug')


    try:
        while(True):
            pass
    except KeyboardInterrupt:
        print('[DISPATCHER]\tinterrotto manualmente')
    finally:
        conn.disconnect()
