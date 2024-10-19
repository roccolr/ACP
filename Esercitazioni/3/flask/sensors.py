import threading, requests, random

dict_tipologie = {0:'temp', 1:'press'}

def sensor(id:int, data_type:str):
    # registrazione
    reg = {
        '_id':id,
        'data_type':data_type
    }
    res = requests.post('http://127.0.0.1:5000/sensor', json=reg)
    
    if(res.status_code == 200):
        print(f'[{threading.current_thread().getName()}]\tsensore registrato con successo')
    else:
        print(f'[{threading.current_thread().getName()}]\terrore durante la registrazione del sensore')
    
    # misurazioni
    for i in range(0,5):
        data = random.randint(0,40)

        mis = {
            'sensor_id':id,
            'data':data
        }

        res = requests.post('http://127.0.0.1:5000/sensor/'+data_type, json=mis)
        
        if(res.status_code == 200):
            print(f'[{threading.current_thread().getName()}]\t misura {id}:{data} registrata con successo')
        else:
            print(f'[{threading.current_thread().getName()}]\terrore durante la registrazione della misura')
    


if __name__ == '__main__':
    thread_list = []
    for i in range(0,5):
        id = random.randint(1,1000)
        t = threading.Thread(name='THREAD_'+str(i), target=sensor, args=(id, dict_tipologie[random.randint(0,1)]))
        t.start()

    for thread in thread_list:
        t.join()