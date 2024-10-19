import stomp, sys

if __name__ == '__main__':

    MSG = sys.argv[1]

    conn = stomp.Connection([('127.0.0.1', 61613)])
    
    conn.connect()

    conn.send('/queue/reQueue', MSG)

    print(f'[SENDER]\tmandato messaggio {MSG}')

    conn.disconnect()