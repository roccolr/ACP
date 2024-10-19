import threading

def consumer(q, free_space, message_ready, mutex_C) -> int:
    '''
    funzione eseguita dai threads consumatori. Il thread consuma un valore se la coda non è vuota e 
    se un altro thread consumatore non ha già acquisito il mutex sul consumatore
    '''


    message_ready.acquire()
    mutex_C.acquire()

    msg = q.pop(0)

    mutex_C.release()
    free_space.release()

    return msg

