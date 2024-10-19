import multiprocess as mp

def fun(id: int, lock: mp.Lock)->None:

    lock.acquire()

    print(f'[PROCESS {id}] - running')

    lock.release()

if __name__ == '__main__':

    lock = mp.Lock()
    process_list = []

    for i in range(10):
        p = mp.Process(target=fun, args=(i, lock))
        process_list.append(p)
        p.start()
    
    for process in process_list:
        process.join()