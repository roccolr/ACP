import stomp, time

class myListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_message(self,frame):
        print(f'[LISTENER]\tricevuto messaggio: {frame.body}\nHEADERS: {frame.headers}\nCOMAND: {frame.cmd}')


if __name__ == '__main__':
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.set_listener('RockTheBrock', myListener(conn))
    conn.connect(wait=True)

    conn.subscribe('/queue/reQueue', id=1)

    try:
        while(True):
            time.sleep(1)
    except KeyboardInterrupt:
        print("[RECEIVER]\tinterrotto da tastiera")