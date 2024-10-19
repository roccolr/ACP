import grpc, hellosalerno_v2_pb2, hellosalerno_v2_pb2_grpc
from concurrent import futures

class Greeter(hellosalerno_v2_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f'[SERVER]\t\t\tInvocato SayHello(), id self: {hex(id(self))}\n')
        return hellosalerno_v2_pb2.HelloReply(msg= 'Ciao! %s' % request.nome)
    
    def SayHelloAgain(self, request, context):
        print(f'[SERVER]\t\t\tInvocato SayHelloAgain()\n')
        return hellosalerno_v2_pb2.HelloReply(msg='Ciao Again! %s' %request.nome)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    hellosalerno_v2_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    port = server.add_insecure_port("0.0.0.0:0") #bind del server al primo porto libero

    server.start()

    print(f'[SERVER]\t\t\tserver in ascolto su {port}')

    server.wait_for_termination()

if __name__ == '__main__':
    serve()
