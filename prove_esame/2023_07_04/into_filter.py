import sys, stomp, time

#ricezione sul topic info

class myListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn
        
    
    def on_message(self, frame):
        received = frame.body
        print('[INFO_FILTER]\tricevuto: '+received)
        
        received_splitted = received.split('-')
        print('[INFO_FILTER]\tsplittato: ', received_splitted)

        if(int(received_splitted[1]) == 1):
            with open('/home/studente/Desktop/acp/prove_esame/2023_07_04/text_files/info.txt', 'a') as file:
                file.write(received+'\n')
            print('[INFO_FILTER]\tricevuto: '+received)
        


if __name__ == '__main__':
    # try:
    #     s = sys.argv[1] #riceve una stringa di tipo fatal o exception
    #     if (s != 'fatal' or s!= 'exception'):
    #         raise Exception
    # except IndexError:
    #     print('[ERROR]\tper favore specifica argomento')
    # except Exception:
    #     print('[ERROR]\tErrore nel passaggio di argomento')
    # else:

    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.set_listener('info_filter', myListener(conn))

    conn.connect()
    conn.subscribe('/topic/info', 1)
    print('[INFO_FILTER]\tin attesa di messaggi sul topic info')

    try:
        while (True):
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('interrotto da tastiera')