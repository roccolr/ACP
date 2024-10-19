import stomp, sys

if __name__ == '__main__':
    try:
        MSG = sys.argv[1]
    except IndexError:
        print('ERROR\t\t\tIndicare argomento msg')
    
    conn = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)

    conn.connect(wait=True)

    conn.send(destination='/topic/myTopic', body=MSG)

    print(f'[SENDER]\t\t\tmandato al topic il messaggio: {MSG}')

    conn.disconnect()

    print('[SENDER]\t\t\tDisconnesso!!')