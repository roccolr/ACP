import stomp, sys

if __name__ == '__main__':
    try:
        msg = sys.argv[1]
    except IndexError:
        print(f'FORNIRE MESSAGGIO!!')
    
    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.connect()

    conn.send('/topic/myTopictest', msg)
    print(f'[PUBLISHER]\tmandato messaggio: {msg}')

    conn.disconnect()