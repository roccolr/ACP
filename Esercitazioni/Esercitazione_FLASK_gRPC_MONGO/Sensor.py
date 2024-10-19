import random, requests, threading, random

def worker_sensor(data_type:str) -> None:
    print(f'[{threading.current_thread().getName().capitalize()} - {data_type.capitalize()}]\t started')
    _id = int((threading.current_thread().name).split('-')[1])

    #registrazione
    res=requests.post('http://127.0.0.1:5000/sensor', json= {'_id':_id, 'data_type':data_type})
    if(res.json()['result']=='success'):
        print(f'[{threading.current_thread().getName().capitalize()} - Registrato con successo')
    else:
        print(f'[{threading.current_thread().getName().capitalize()} - Registrazione fallita')
    
    #effettuo misure
    for i in range(0,5):
        request = {
            'sensor_id':_id,
            'data':random.randint(1, 50)
        }

        res = requests.post(f'http://127.0.0.1:5000/data/{data_type}', json=request)

        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            print('ERRORE...', res.status_code)
        else:
            print(f'[{threading.current_thread().getName().capitalize()} - {data_type.capitalize()}]\t misurazione {i} comunicata')

data_dict = {0:'temp', 1:'press'}

if __name__ == '__main__':
    threads = []
    for i in range(0,5):
        w = threading.Thread(target=worker_sensor, args=(data_dict[random.randint(0,1)],), name=f"THREAD-{i}")
        threads.append(w)
        w.start()
    
    for t in threads:
        t.join()
    
    print('[SENSOR_CLIENT]\tTerminato')
        


