import stomp, sys, time

class myListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_message(self, frame):
        print(f'ricevuto messaggio:\n[BODY]: {frame.body}\n[HEADERS]: {frame.headers}\n[CMD]: {frame.cmd}')

if __name__ == '__main__':
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener('Rocchitobabe', myListener(conn))

    conn.connect(headers={"client-id":"RocchitobabeDurable"}, wait=True)

    conn.subscribe('/topic/myTopictest', id=1, headers={"activemq.subscriptionName":"durable_sub_1"}, persistent=True)

    try:
        while(True):
            time.sleep(1)
    except KeyboardInterrupt:
        print("[SUBSCRIBER]\tinterrotto da tastiera...")