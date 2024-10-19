import hellosalerno_pb2, hellosalerno_pb2_grpc, grpc
from concurrent import futures

class Greeter(hellosalerno_pb2_grpc.GreeterServicer):
    def sayHello(self, request_iterator, context):
        print(f'[SERVER]\t\t\tinvocato sayHello()...\n')

        nomi = []

        for r in request_iterator:
            nomi.append(r.nome)
        
        riposta = 'Hello! ' + ' '.join(nomi)
        return hellosalerno_pb2.helloReply(msg=riposta)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    hellosalerno_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    port = server.add_insecure_port('localhost:0')

    server.start()

    print(f'[SERVER]\t\t\tin ascolto su localhost:{port}')

    server.wait_for_termination()

if __name__ == '__main__':
    serve()
    