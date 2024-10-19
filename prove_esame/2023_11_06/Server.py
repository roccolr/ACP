from PrinterReal import PrinterReal
import multiprocessing, stomp

def consumatore(q:multiprocessing.Queue):
    while True:
        message = q.get()
        split = message.split('-')
        print('[CONSUMATORE]\tConsumato messaggio '+message)
        # publisher stomp
        conn = stomp.Connection([('127.0.0.1',61613)])
        conn.connect(wait=True)

        

        if (split[1]== 'color'):
            conn.send('/topic/color', message)
        else:
            conn.send('/topic/bw', message)
        
        print('[PUBLISHER]\tinviato sulla giusta coda il messaggio: '+message)

        conn.disconnect()


if __name__ == '__main__':
    queue = multiprocessing.Queue(5)

    w = multiprocessing.Process(target=consumatore, args=(queue,))
    w.start()
    printer = PrinterReal(6969, queue)
    printer.run_skeleton()