import ProxyMagazzino, random, sys, time

dict_prodotti = {0:'smartphone', 1:'laptop'}


if __name__ == '__main__':
    try:
        tipo = sys.argv[1]
    except IndexError:
        print('[CLIENT]\tErrore, specificare tipologia')
    

    proxy = ProxyMagazzino.ProxyMagazzino()
    if (tipo == 'deposita'):
        for i in range(0,5):
            sleep_time = random.randint(2,4)
            prodotto = dict_prodotti[random.randint(0,1)]
            id = random.randint(1,100)
            proxy.deposita(prodotto, id)
            print(f'[CLIENT]\tInviata richiesta deposito({prodotto},{id})')
            time.sleep(sleep_time)
    elif (tipo == 'preleva'):
        for i in range(0,5):
            sleep_time = random.randint(2,4)
            prodotto = dict_prodotti[random.randint(0,1)]
            res = proxy.preleva(prodotto)
            print(f'[CLIENT]\tInviata richiesta preleva({prodotto})')
            print(f'[CLIENT]\tricevuto id: {res}')
            time.sleep(sleep_time)