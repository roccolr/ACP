from ServiceImpl import ServiceImpl
import multiprocessing, stomp

def ServerWorker(q:multiprocessing.Queue):
    # stomp una tantum
    conn = stomp.Connection([('127.0.0.1', 61613)])
    conn.connect(wait=True)
    print('[SERVER-WORKER]\tConnesso a stomp')
    while True:
        msg = q.get()
        print('[SERVER-WORKER]\tConsumato messaggio: '+msg)

        msg_list = msg.split('-')
        if(int(msg_list[1])==2):
            conn.send('/topic/error', msg)
            print('[SERVER-WORKER]\tInviato al topic error:'+msg)

        else:
            conn.send('/topic/info', msg)
            print('[SERVER-WORKER]\tInviato al topic info:'+msg)


if __name__ == '__main__':
    q = multiprocessing.Queue(5)

    w = multiprocessing.Process(target=ServerWorker, args=(q,), name='PROCESS_SENDER')
    w.start()

    skeleton = ServiceImpl(q)
    skeleton.run_skeleton()