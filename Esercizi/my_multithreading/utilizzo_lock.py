import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-0f)%(message)s')


x = 10 #variabile globale

'''
Se commento acquire() e release() e la sleep il codice funziona comunque, perchè interviene il GIL a garantire che 
operi solo un thread per volta. Infatti, quando un thread chiama la funzione time.sleep(), rilascia il GIL a favore
dell'esecuzione di un altro thread
'''

def increment(by : int, lock : threading.Lock) -> None:
    global x #le modifiche effettuate su x si rifletteranno anche sul chiamante: lo scope non è locale

    lock.acquire()

    local_value = x 
    local_value += by 

    time.sleep(1)
    
    x = local_value

    # logging.debug('valore x: %s, incrementato di: %s ', x, by)
    print(f'{threading.current_thread().getName()} increments x by {by}, x = {x}')
    lock.release()


if __name__ == '__main__':

    lock = threading.Lock()

    thread1 = threading.Thread(target=increment, args=(1, lock))
    thread2 = threading.Thread(target=increment, args=(10, lock))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'[MAIN] - Valore finale x={x}')

