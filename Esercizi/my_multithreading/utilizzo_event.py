import threading 
from time import sleep

def fun(time : int, event: threading.Event) -> None:
    got_event = event.wait(timeout=time)

    if(got_event == True):
        print(f'[{threading.currentThread().getName()}] - riscontrato evento atteso')
    else:
        print(f'[{threading.currentThread().getName()}] - timeout... passati {time} secondi')


if __name__ == '__main__':
    e = threading.Event()

    thread = threading.Thread(name='Thread 1', target= fun, args=(3, e))
    thread.start()

    # sleep(3)
    sleep(2)

    e.set()

    thread.join()
    print('[MAIN] - terminato')
        
