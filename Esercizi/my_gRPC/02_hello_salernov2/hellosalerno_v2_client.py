import hellosalerno_v2_pb2, hellosalerno_v2_pb2_grpc, grpc, sys

def run(port:int):
    #creare il canale di comunicazione
    with grpc.insecure_channel(f"localhost:{str(port)}") as channel:

        #creiamo l'oggetto stub
        stub = hellosalerno_v2_pb2_grpc.GreeterStub(channel)
        print(f'[CLIENT]\t\t\tCreato canale sul porto: {port} e contestualmente creato stub\n')


        #invochiamo i metodi
        print(f'[CLIENT]\t\t\tInvoco il metodo SayHello() sullo stub\n')
        res = stub.SayHello(hellosalerno_v2_pb2.HelloRequest(nome='Broccolo'))
        print(f'[CLIENT]\t\t\tRicevuto: {res.msg}')


        print(f'[CLIENT]\t\t\tInvoco il metodo SayHelloAgain() sullo stub\n')
        res = stub.SayHelloAgain(hellosalerno_v2_pb2.HelloRequest(nome='Broccolo'))
        print(f'[CLIENT]\t\t\tRicevuto: {res.msg}')


if __name__ == '__main__':
    try:
        PORT = int(sys.argv[1])
    except IndexError:
        print('PLEASE SPECIFY PORT...')

    run(PORT)

        


