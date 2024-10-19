import stomp, sys


if __name__ == '__main__':
    try:
        MSG = sys.argv[1]
    except IndexError:
        print('PLEASE SPECIFY MSG ARGUMENT')
    
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)

    conn.send('/queue/test', MSG)

    print(f'[SENDER]\t\t\tinviato messaggio {MSG}')

    conn.disconnect()

    

