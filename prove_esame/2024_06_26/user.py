import grpc, service_pb2_grpc, service_pb2, threading, random

def worker(flag:bool, proxy: service_pb2_grpc.ManagementStub):
    res = ""
    if (flag==True):
        res = proxy.buy(service_pb2.buy_request())
    else:
        id = random.randint(0,100)
        res = proxy.sell(service_pb2.sell_request(id=id))
    print(threading.current_thread().getName()+"\tricevuto valore di ritorno: "+str(res))


if __name__ == '__main__':
    with grpc.insecure_channel('127.0.0.1:6969') as channel:
        proxy = service_pb2_grpc.ManagementStub(channel)
        thread_list = []
        for i in range(0,10):
            if(i%2==0):
                flag = True
                t = threading.Thread(target=worker, args=(flag, proxy))
                t.start()
                thread_list.append(t)
            else:
                flag = False
                t = threading.Thread(target=worker, args=(flag, proxy))
                t.start()
                thread_list.append(t)

        for thread in thread_list:
            thread.join()
            print('[MAIN]\tthread joinato')
        
        print('[MAIN]\tfine')
