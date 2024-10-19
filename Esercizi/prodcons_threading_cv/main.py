import threading
import time 
import random 
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(threadName)-0s]%(message)s')

N_CONSUMATORI = 10
N_PRODUTTORI = 10
DIM = 5

'''
usiamo un solo lock per entrambe le condition variable, e questo rappresenta il monitor.
Acquisito il monitor, quando si aspetta su una condizione il lock viene rilasciato, per poi 
venire riacquisito non appena la condizione diventa true e il thread viene risvegliato  
'''

def item_available(queue:list) -> bool:
    '''
    ritorna vero se la coda non è vuota
    '''
    return not(len(queue) == 0)

def space_available(queue:list) -> bool:
    '''
    ritorna vero se la coda ha uno spazio libero
    '''
    return not(len(queue) == DIM)

def produce_item(queue:list) -> int:
    x = random.randint(1,100)
    queue.append(x)
    return x

def consume_item(queue:list) -> int:
    return queue.pop(0)

def producer(q:list, producer_cv: threading.Condition, consumer_cv: threading.Condition)->None:
    logging.debug('\t\t\tinizio')
    #entra nel monitor
    producer_cv.acquire()
    logging.debug('\t\t\tentrato nel monitor')

    #while perchè usiamo una strategia signal and continue
    while(not(space_available(q))):
        logging.debug('\t\t\taspettando...')
        producer_cv.wait()
    
    logging.debug('\t\t\tattesa terminata')

    r = produce_item(q)
    logging.debug('\t\t\tprodotto %d', r)

    consumer_cv.notify()
    logging.debug('\t\t\tnotificati i consumatori')

    producer_cv.release()
    logging.debug('\t\t\tuscito dal monitor')

def consumer(q:list, producer_cv:threading.Condition, consumer_cv:threading.Condition) -> None:
    logging.debug('\t\t\tinizio')
    consumer_cv.acquire()
    logging.debug('\t\t\tentrato nel monitor')

    while(not(item_available(q))):
        logging.debug('\t\t\taspettando...')
        consumer_cv.wait()
    
    logging.debug('\t\t\tattesa terminata')

    time.sleep(1)
    logging.debug('\t\t\tconsumato: %d', consume_item(q))

    producer_cv.notify()
    logging.debug('\t\t\tnotificati i produttori')

    consumer_cv.release()
    logging.debug('\t\t\tuscito dal monitor')
    

if __name__ == '__main__':
    logging.debug('\t\t\tiniziato')
    # creazione cv
    lock = threading.Lock()
    producer_cv = threading.Condition(lock=lock)
    consumer_cv = threading.Condition(lock=lock)


    #creazione coda 
    q = []

    #creazione thread consumatori
    consumatori = []
    for i in range(N_CONSUMATORI):
        t = threading.Thread(target= consumer, args=(q, producer_cv, consumer_cv), name='CONSUMATORE '+str(i))
        consumatori.append(t)
        t.start()
    
    logging.debug('\t\t\tcreati consumatori')

    #creazione thread produttori
    produttori = []
    for i in range(N_PRODUTTORI):
        t = threading.Thread(target= producer, args=(q, producer_cv, consumer_cv), name= 'PRODUTTORE '+str(i))
        produttori.append(t)
        t.start()

    logging.debug('\t\t\tcreati produttori')

    for c in consumatori:
        c.join()
    
    for p in produttori:
        p.join()
    
    logging.debug('\t\t\tfine')
    

    

