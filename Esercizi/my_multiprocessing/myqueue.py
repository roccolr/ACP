from multiprocess import *
import random
from numpy import pi

def fun(queue) -> None:
    msg = [random.randint(1,1000), 'CIAO', pi]
    try:
        queue.put(msg)
    except:
        print('rilevato problema...')

if __name__ == '__main__':
    q = Queue()

    p = Process(target = fun, args = (q,))
    p.start()

    val = q.get()
    print(val)

    p.join()
