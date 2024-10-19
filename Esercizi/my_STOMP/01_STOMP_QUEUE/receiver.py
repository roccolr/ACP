import sys, stomp, time

class myListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    
    def on_message(self, frame):
        print(f'[RECEIVER]\t\t\tricevuto: \nMESSAGGIO: {frame.body}\nHEADERS: {frame.headers}\nCOMANDO: {frame.cmd}')


if __name__ == '__main__':
    conn = stomp.Connection([('127.0.0.1', '61613')])

    conn.set_listener('myListener1', myListener(conn))

    conn.connect(wait=True)

    conn.subscribe(destination='/queue/test', id=1)

    # try:
    #     while True:
    #         print('[RECEIVER]\t\t\tWaiting 4 messages\n')
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     print('[RECEIVER]\t\t\tinterrotto da tastiera')
    # finally:
    #     conn.disconnect()
    print('[RECEIVER]\t\t\tWaiting 4 messages\n')
    
    time.sleep(60)
    conn.disconnect()

