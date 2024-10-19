import stomp
from time import sleep

class myListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn
    
    def on_message(self, frame):
        print(f'[RECEIVER]\t\t\tricevuto:\nbody: {frame.body}\nheaders:{frame.headers}\ncommand:{frame.cmd}\n')


if __name__ == '__main__':
    conn = stomp.Connection(host_and_ports=[('127.0.0.1', 61613)], auto_content_length=False )

    conn.set_listener('Rocco', myListener(conn))

    conn.connect(wait=True, headers= {"client-id":"Rocco_durable"})

    conn.subscribe(destination='/topic/myTopic', id=1, ack='auto',persistent=True, headers={"activemq.subscriptionName":"DURABLESUB_Rocco"})

    print(f'[RECEIVER] - In attesa di messasggi...')

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print(f'[RECEIVER]\t\t\tinterrotto manualmente')
    finally:
        conn.disconnect()
        
