import threading 
import random
import time

#creiamo 10 thread che eseguono la funzione func

def func(id):
    rtime = random.randint(1, 3)
    time.sleep(rtime)
    print(f'[THREAD {id}] - running\n')

if __name__ == '__main__':
    threads = []
    for i in range(10):
        t = threading.Thread(target= func, args= (i,))
        threads.append(t)
        t.start()

    print('[MAIN] - doing my business...')
    
    for i in range(10):
        threads[i].join()
    
    print("[MAIN] - Threads terminati")