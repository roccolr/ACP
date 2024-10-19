import threading
import random 

def producer(q, free_space, message_ready, mutex_P)-> int:
    '''
    Produce un messaggio se la coda ha uno spazio disponibile e se il mutex dei produttori non è 
    già stato preso da un altro thread produttore
    '''

    msg = random.randint(1,100)

    free_space.acquire()
    mutex_P.acquire()

    q.append(msg)

    mutex_P.release()
    message_ready.release()

    return msg
