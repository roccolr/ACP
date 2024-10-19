from threading import *
from time import sleep
import random

sem = Semaphore(value= 3)

def fun(name: str) -> None:
    sem.acquire()

    sleep_time = random.randint(1,3)
    sleep(sleep_time)

    print(f'[THREAD {name}] - ha dormito per {sleep_time} secondi')

    sem.release()

if __name__ == '__main__':
    threads = []

    for i in range(10):
        t = Thread(target= fun, args= (f'{i}',))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()