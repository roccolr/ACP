from PrinterSkeleton import PrinterSkeleton
import multiprocessing

class PrinterReal(PrinterSkeleton):
    def __init__(self, port, queue:multiprocessing.Queue):
        self.port = port
        self.queue = queue

    def print(self, pathfile:str, tipo:str) -> None:
        message = pathfile+'-'+tipo
        self.queue.put(message)
        print(f'[SERVER]\tinserito nella coda il messaggio: {message}')
