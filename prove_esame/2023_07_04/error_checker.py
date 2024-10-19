import sys, stomp, time

#ricezione sul topic error

class BadParameter(Exception):
    pass

class myListener(stomp.ConnectionListener):
    def __init__(self, conn,s):
        self.conn = conn
        self.string = s
    
    def on_message(self, frame):
        received = frame.body
        print('[ERROR_CHECKER]\tricevuto: '+received)
        received_splitted = received.split('-')
        print('[ERROR_CHECKER]\tsplittato: ', received_splitted)

        if(received_splitted[0] == self.string):
            with open('/home/studente/Desktop/acp/prove_esame/2023_07_04/text_files/error.txt', 'a') as file:
                file.write(received)
            print('[ERROR_CHECKER]\tricevuto: '+received)
        


if __name__ == '__main__':
    try:
        s = sys.argv[1] #riceve una stringa di tipo fatal o exception
        if (s != 'fatal' and s!= 'exception'):
            raise BadParameter()
            # print('aja')
    except IndexError:
        print('[ERROR]\tper favore specifica argomento')
    except BadParameter:
        print('[ERROR]\tErrore nel passaggio di argomento')
    else:

        conn = stomp.Connection([('127.0.0.1', 61613)])
        conn.set_listener('error_checker', myListener(conn,s))

        conn.connect()
        conn.subscribe('/topic/error', 1)

        print('[ERROR_CHECKER]\tin attesa di messaggi sul topic error')
        try:
            while (True):
                time.sleep(0.1)
        except KeyboardInterrupt:
            print('interrotto da tastiera')