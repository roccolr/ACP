import random  
import multiprocess
import time 

'''
prod cons con multiprocess e uso di semafori. Sarà necessario creare una coda condivisa IPC tramite multiprocess.Queue()
semafori necessari: nessuno, perchè la coda usa pipe e semafori
'''

size = 5
NCONSUMATORI = 10
NPRODUTTORI = 10

def produci(queue: multiprocess.Queue)->int:
    x = random.randint(1,100)
    queue.put(x)
    return x

def consuma(queue: multiprocess.Queue())->int:
    return queue.get()

def produttore(queue):
    time.sleep(1.0)
    r = produci(queue)
    print(f'[{multiprocess.current_process().pid}]\t\t\tprodotto: {r}')

def consumatore(queue):
    time.sleep(1.0)
    r = consuma(queue)
    print(f'[{multiprocess.current_process().pid}]\t\t\tconsumato {r}')

if __name__== '__main__':
    print(f'[{multiprocess.current_process().pid} - MAIN]\t\t\tinizio')

    q = multiprocess.Queue(size)

    producers = []
    consumers = []

    for i in range(NCONSUMATORI):
        p = multiprocess.Process(target=consumatore, args=(q,))
        consumers.append(p)
        p.start()
    
    for i in range(NPRODUTTORI):
        p = multiprocess.Process(target=produttore, args=(q,))
        producers.append(p)
        p.start()

    for process in producers:
        process.join()
    
    for process in consumers:
        process.join()
    
    print(f'[{multiprocess.current_process().pid} - MAIN]\t\t\tfine')
    