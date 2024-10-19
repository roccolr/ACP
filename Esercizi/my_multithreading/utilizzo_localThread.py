import logging 
import threading
import random


logging.basicConfig(level=logging.DEBUG, format=('(%(threadName)-0s)%(message)s'))


def show(d : threading.local) -> None:
    '''
    funzione che accetta in ingresso un tipo threading.local, e cerca di stamparne a video il contenuto
    '''
    try:
        val = d.val
    except AttributeError:
        logging.debug('no value yet')
    else:
        logging.debug('value=%s', d.val)

def fun(d):
    show(d)
    d.val = random.randint(1,100)
    show(d)

if __name__ == '__main__':
    n_threads = 10
    d = threading.local()
    show(d)
    d.val = random.randint(1,100)
    show(d)

    threads = []

    for i in range(n_threads):
        t = threading.Thread(target= fun, args=(d,))
        threads.append(t)
        t.start()

    for i in range(n_threads):
        threads[i].join()


