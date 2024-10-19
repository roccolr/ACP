import stomp
from time import sleep

class myListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn
    
    def on_message(self, frame):
        print(f'[RECEIVER]\t\t\tricevuto messaggio: {frame.body}')
    
if __name__ == '__main__':
    conn = stomp.Connection(host_and_ports=[('127.0.0.1', 61613)], auto_content_length=False)

    conn.set_listener('Brock', myListener(conn))
    conn.connect(wait=True, headers={"client-id":"Brock_durable"})
    conn.subscribe(destination='/topic/myTopic', id=1, ack='auto', headers={"activemq.subscriptionName":"DURABLESUB_Brock"}, persistent=True)

    try:
        while True:
            sleep(1)
        
    except KeyboardInterrupt:
        print('[RECEIVER]\t\t\tInterrotto manualmente ')
    finally:
        conn.disconnect()
