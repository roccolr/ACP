import hellosalerno_pb2, hellosalerno_pb2_grpc, grpc
from concurrent import futures

class Greeter(hellosalerno_pb2_grpc.GreeterServicer):
    def sayHello(self, request_iterator, context):
        print(f'[SERVER]\t\t\tinvocato metodo SayHello()')

        for r in request_iterator:
            print(f'[SERVER]\t\t\tricevuta richiesta per il nome: {r.nome}')
            yield hellosalerno_pb2.helloReply(msg='CIAO '+r.nome + '!!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    hellosalerno_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    port = server.add_insecure_port('localhost:0') ##primo porto disponibile

    server.start()

    print(f'[SERVER]\t\t\tin ascolto su localhost:{port}')

    server.wait_for_termination()


if __name__ == '__main__':
    serve()