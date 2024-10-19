import grpc
import hellosalerno_pb2
import hellosalerno_pb2_grpc
from concurrent import futures

# implementiamo i metodi remoti, ovvero creiamo la classe implementativa

class Greeter(hellosalerno_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print('[SERVER]\t\t\tInvocazione di SayHello()\n')

        #nella specifica (nel protobuf) sappiamo che questa funzione deve restituire un HelloReply

        return hellosalerno_pb2.HelloReply(message='CIAO %s' %request.name)


# definiamo un metodo 'equivalente' a run_skeleton()
def serve():
    port = "50051" #di default 443, può essere qualsiasi

    #non usiamo le socket, ma una classe propria di grpc: grpc.server()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    #si aggiunge un oggetto della classe implementativa al server
    hellosalerno_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    #a questo punto si effettua un 'bind' 
    # server.add_insecure_port("localhost:"+port)
    server.add_insecure_port("[::]:"+port)

    #si avvia il server
    server.start()

    print('Server hellosalerno avviato sulla porta ', port, '\n')

    server.wait_for_termination()


if __name__ == '__main__':
    serve()

