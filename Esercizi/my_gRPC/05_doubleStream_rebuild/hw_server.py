import helloworld_pb2, helloworld_pb2_grpc, grpc
from concurrent import futures

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def say_hello(self, request, context):
        # names = []
        for req in request:
            # names.append(req.name)
            print(f'[SERVER]\tricevuta richiesta, invio risposta per il nome{req.name}')
            yield helloworld_pb2.HelloReply(msg=f"Hello {req.name}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(5))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    port = server.add_insecure_port("127.0.0.1:6969")
    server.start()
    print(f"Server running on {port}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()