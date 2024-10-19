from my_threads.ThreadProduttore import ThreadProduttore
from my_threads.ThreadConsumatore import ThreadConsumatore
import threading 

if __name__ == '__main__':
    dim_coda = 4
    n_produttori = 10
    n_consumatori = 10

    # la coda può essere semplicemente realizzata attraverso una lista 

    q = []

    free_space = threading.Semaphore(dim_coda)
    message_ready = threading.Semaphore(0)
    mutex_C = threading.Semaphore(1)
    mutex_P = threading.Semaphore(1)

    produttori = []
    consumatori = []
    
    #creazioni thread produttori 


    for i in range(n_produttori):
        t = ThreadProduttore(free_space, message_ready, mutex_P, q, 'Produttore '+str(i))
        produttori.append(t)
        t.start()
    
    #creazione thread consumatori

    for i in range(n_consumatori):
        t = ThreadConsumatore(q, free_space, message_ready, mutex_C, 'Consumatore '+str(i))
        consumatori.append(t)
        t.start()


    # print('debug')

    #join produttori 
    for produttore in produttori:
        produttore.join()
        print(f'[MAIN] - joinato thread {produttore.getName()} \n')

    #join consumatori 
    for consumatore in consumatori:
        consumatore.join()
        print(f'[MAIN] - joinato thread {consumatore.getName()} \n')

