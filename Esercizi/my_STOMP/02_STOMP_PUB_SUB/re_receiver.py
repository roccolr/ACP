import stomp
from time import sleep

class myListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, frame):
        print(f'[RE-RECEIVER]\nbody:{frame.body}\nheaders:{frame.headers}\ncommand:{frame.cmd}')


if __name__ == '__main__':
    conn = stomp.Connection(host_and_ports=[('127.0.0.1', 61613)], auto_content_length=False)

    conn.set_listener('Rocco2', myListener(conn))

    conn.connect(wait=True, headers={"client-id":"Broccolo_durable"})
    conn.subscribe(destination='/topic/myTopic', id=2, ack='auto', persistent=True, headers={"activemq.subscriptionName":"DURABLESUB_BROCCOLO"})

    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        print('[RE-RECEIVER]\t\t\tInterrotto manualmente!')

