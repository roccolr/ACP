import ServiceProxy, time, random

tipi = {0:'DEBUG', 1:'INFO', 2:'ERROR'}
messaggi_log = {0:'success', 1:'checking', 2:'fatal', 3:'exception'}

if __name__ == '__main__':
    messaggio_log = ''
    proxy = ServiceProxy.ProxyService()
    for i in range(0,10):
        # seed = random.randint(0,2)
        tipo = random.randint(0,2)
        if(tipo < 2):
            messaggio_log = messaggi_log[random.randint(0,1)]
        else:
            messaggio_log = messaggi_log[random.randint(2,3)]
        
        proxy.log(messaggio_log, tipo)
        time.sleep(1)

print('[CLIENT-SERVICE]\tTerminato')
        
