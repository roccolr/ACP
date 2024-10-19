import hellosalerno_pb2_grpc, hellosalerno_pb2, grpc
from concurrent import futures

class Greeter(hellosalerno_pb2_grpc.GreeterServicer):
    def sayHello(self, request, context):
        print(f'[SERVER]\t\t\tInvocata funzione SayHello() - Ritorna 5 messaggi\n')
        for i in range(5):
            yield hellosalerno_pb2.HelloResponse(f'HELLO {request.name} {i}')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hellosalerno_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    port = server.add_insecure_port("0.0.0.0:0")


    server.start()

    print(f'[SERVER]\t\t\tstarted on {port}')

    server.wait_for_termination()

if __name__ == '__main__':
    serve()

