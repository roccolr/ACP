import grpc, service_pb2, service_pb2_grpc, threading, requests
from concurrent import futures
from coda import Coda

class Management(service_pb2_grpc.ManagementServicer):
    def __init__(self, queue:list, dim):
        self.queue = queue
        self.dim = dim
        self.lock = threading.Lock()
        self.cv_produttore = threading.Condition(self.lock)
        self.cv_consumatore = threading.Condition(self.lock)

    def buy(self, request:service_pb2.buy_request, context):

        with self.cv_consumatore:
            while(len(self.queue)== 0):
                print('coda_vuota')
                self.cv_consumatore.wait()

            res = self.queue.pop(0)
            # with self.cv_produttore:
            self.cv_produttore.notify()

        print(f'[MANAGER]\tprelevato elemento con id: {res}')
        #flask

        msg ={
            'operation':'buy',
            'serial_number':str(res)
        }
        result = requests.post('http://127.0.0.1:5000/update_history', json=msg)
        if result.status_code == 200:
            return service_pb2.buy_response(id = res)
        else:
            return service_pb2.buy_response(id = 122)


    def sell(self, request:service_pb2.sell_request, context):
        id = request.id

        with self.cv_produttore:
            while(len(self.queue) == self.dim):
                print('coda_piena')
                cv_produttore.wait()
            self.queue.append(id)
            # with self.cv_consumatore:
            self.cv_consumatore.notify()
        
        print(f'[MANAGER]\tinserito elemento con id: {id}')
        #flask

        msg ={
            'operation':'sell',
            'serial_number':str(id)
        }
        res = requests.post('http://127.0.0.1:5000/update_history', json=msg)

        if (res.status_code == 200):
            return service_pb2.sell_response(res = True)
        else:
            return service_pb2.sell_response(res = False)

def serve():
    queue = []
    server = grpc.server(futures.ThreadPoolExecutor(5))
    port = server.add_insecure_port('127.0.0.1:6969')
    service_pb2_grpc.add_ManagementServicer_to_server(Management(queue, 5), server)
    server.start()

    print(f'[MANAGER]\tserver avviato sul porto: {port}')

    server.wait_for_termination()

if __name__ == '__main__':
    serve()    

    