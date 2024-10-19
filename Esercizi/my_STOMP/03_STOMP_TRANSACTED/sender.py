import stomp, sys, random

HOST = '127.0.0.1'
PORT = 61613

if __name__ == '__main__':
    try:
        MSG = sys.argv[1]
    except IndexError:
        print('[SENDER]\t\t\tplease specify message parameter')
    
    conn = stomp.Connection(host_and_ports=[(HOST, PORT)], auto_content_length=False)
    conn.connect(wait=True)

    trID = conn.begin()

    try:
        for i in range(2):
            value = random.randint(0,1)
            if value == 0:
                print(f'[SENDER]\t\t\tmandando messaggio n:{i} \n{MSG}')
                conn.send('/topic/myTopic', MSG+' #'+str(i), transaction=trID)
            else:
                raise IOError('[ERRORE]\t\t\tverificato errore improvviso\n')

    except IOError as e:
        print(e)
        conn.abort(trID)
        print('[SENDER]\t\t\tmessage aborted')

    else:
        conn.commit(trID)
        print('[SENDER]\t\t\tmessage committed')
