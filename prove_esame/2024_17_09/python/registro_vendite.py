import threading, stomp, time, pandas

def vWorker(msg:str, queue:list, lock:threading.Lock, cv_produttore: threading.Condition, cv_consumatore: threading.Condition):
    splitted_msg = msg.split('-')
    targa = splitted_msg[0]
    quotazione = splitted_msg[1]

    cv_consumatore.acquire()
    print('[Consumatore]\tentrato nel monitor')
    print(queue)
    while(len(queue)==0):
        cv_consumatore.wait()
    print('[Consumatore]\tattesa finita')
    
    index = -1
    utente = None
    # la lista è tipo [{k:v}, {k,v}, {k,v}]
    for i in range(0, len(queue)):
        dict_temp = queue[i]
        budget = list(dict_temp.values())[0]
        utente = list(dict_temp.keys())[0]
        if(budget>=quotazione):
            index = i
            queue.remove(queue[i])
            break
    
    if (index < 0):
        print('[CONSUMATORE\t non trovato]')
    else:
        data = {
            'targa':[targa],
            'utente':[utente],
            'quotazione':[quotazione]
        }
        df = pandas.DataFrame(data)
        df.to_csv('/home/studente/Desktop/acp/prove_esame/2024_17_09/record.csv', mode='a', index=False, header=True)
        print(f'[CONSUMATORE]\t scritto su csv file t: {targa}, u:{utente}, q: {quotazione}')
    
    cv_produttore.notify()
    print('[CONSUMATORE]\tuscito dal monitor')
    cv_consumatore.release()


def cWorker(msg:str, queue:list, lock:threading.Lock, cv_produttore: threading.Condition, cv_consumatore: threading.Condition):
    splitted_msg = msg.split('-')
    entry = {splitted_msg[0]:splitted_msg[1]}

    # sincronizzazione
    cv_produttore.acquire()

    while(len(queue) == 10):
        cv_produttore.wait()

    queue.append(entry)

    cv_consumatore.notify()
    cv_produttore.release()
    print('[REGISTER]\tinserito in coda la entry, coda: '+ queue.__str__())

class cListener(stomp.ConnectionListener):
    def __init__(self, queue:list, lock:threading.Lock, cv_produttore: threading.Condition, cv_consumatore: threading.Condition):
        self.queue = queue
        self.lock = lock
        self.cv_produttore = cv_produttore
        self.cv_consumatore = cv_consumatore

    def on_message(self, frame:stomp.utils.Frame):
        msg = frame.body
        print('[PRODUTTORE]\tricevuto messaggio:'+msg)
        p = threading.Thread(target=cWorker, args=(msg, self.queue, self.lock, self.cv_produttore, self.cv_consumatore))
        p.start()

class vListener(stomp.ConnectionListener):
    def __init__(self, queue:list, lock:threading.Lock, cv_produttore: threading.Condition, cv_consumatore: threading.Condition):
        self.queue = queue
        self.lock = lock
        self.cv_produttore = cv_produttore
        self.cv_consumatore = cv_consumatore

    def on_message(self, frame:stomp.utils.Frame):
        msg = frame.body
        print('[Consumatore]\tricevuto messaggio:'+msg)

        p = threading.Thread(target=vWorker, args=(msg, self.queue, self.lock, self.cv_produttore, self.cv_consumatore))
        p.start()

if __name__ == '__main__':
    q = []
    lock = threading.Lock()
    cv_produttore = threading.Condition(lock=lock)
    cv_consumatore = threading.Condition(lock=lock)

    conn1 = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    conn2 = stomp.Connection([('127.0.0.1', 61613)], auto_content_length=False)
    conn1.connect()
    conn2.connect()
    conn2.subscribe('/topic/vendi_topic', id=1)
    conn1.subscribe('/topic/compra_topic', id=2)
    
    
    conn1.set_listener('register_c', cListener(q, lock, cv_produttore, cv_consumatore))
    conn2.set_listener('register_v', vListener(q, lock, cv_produttore, cv_consumatore))


    try:
        time.sleep(60)
    except KeyboardInterrupt:
        print('register off')
    
