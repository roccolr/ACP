import stomp, sys, threading, random, time

def worker(conn:stomp.Connection, destination:str, flag:bool, operator:str):
    tipo_richiesta = None
    if(flag == True):
        tipo_richiesta = 'create'
        client = 'user'+str(random.randint(0,1000))
        hotel = 'hotel ' + str(random.randint(0,1000))
        nights = random.randint(1,10)
        people = random.randint(1,20)
        cost = random.randint(100,5000)
        body = tipo_richiesta+'-'+client+'-'+hotel+'-'+operator+'-'+str(nights)+'-'+str(people)+'-'+str(cost)
        conn.send(destination=destination, body= body)

        print(f'[{threading.current_thread().getName()}]\tinviato messaggio: {body}')
    else:
        tipo_richiesta = 'update'
        discount = random.randint(0,60)+40
        nights = 5    
        body = tipo_richiesta+'-'+operator+'-'+str(discount)+'-'+str(nights)

        conn.send(destination=destination, body= body)

        print(f'[{threading.current_thread().getName()}]\tinviato messaggio: {body}')

    
class ResponseListener(stomp.ConnectionListener):
    def on_message(self, frame):
        print(f'[LISTENER]\tottenuta risposta: {frame.body}')

if __name__ == '__main__':

    try:
        operator = sys.argv[1]
    except IndexError:
        print('specificare operatore...')
    else:
        conn = stomp.Connection([('127.0.0.1', 61613)])

        conn.connect(wait=True)
        conn.subscribe('/topic/response', id=1)
        conn.set_listener('ResponseListener', ResponseListener())
        # CREATE: tipo_richista-client-hotel-operator-nights-people-cost
        # UPDATE: tipo_richiesta-discount-operator-nights
        request_destination = '/topic/request'

        threadlist = []
        for i in range(0,6):
            flag = True
            if (i>=4):
                flag = False
            w = threading.Thread(name='THREAD_WORKER_'+str(i), target= worker, args=(conn, request_destination, flag, operator))
            threadlist.append(w)
            w.start()

        for thread in threadlist:
            thread.join()
            print('[OPERATOR]\tthread joinato con successo')

        try:
            time.sleep(60)
        except KeyboardInterrupt:
            print('[OPERATOR]\tinterrotto da tastiera')
            
        