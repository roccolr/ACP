from PrinterProxy import PrinterProxy
import sys, random, time

type_dict = {0:'bw', 1:'gs', 2:'color'}
ext_dict = {0:'txt', 1:'doc'}

if __name__ == '__main__':

    try:
        port = int(sys.argv[1])
    except IndexError:
        print('specifica porto...')
    else:
        host = '127.0.0.1'
        proxy = PrinterProxy(host, port)
        path = '/user/file_'
        for i in range(0,10):
            pathfile=path+str(random.randint(0,100))+'.'+ext_dict[random.randint(0,1)]
            tipo=type_dict[random.randint(0,2)]
            proxy.print(pathfile, tipo)
            print(f'[CLIENT]\tinviata richiesta {pathfile} di tipo {tipo}')
            time.sleep(1)
        print('[CLIENT]\tfinito')
